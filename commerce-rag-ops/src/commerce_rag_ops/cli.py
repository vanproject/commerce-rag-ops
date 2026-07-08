from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from .agent import CommerceRAGAgent
from .advisor import build_advisor
from .audit import audit_project, write_audit_report
from .combined_eval import (
    apply_golden_metadata,
    load_eval_report_json,
    run_combined_evaluation,
    write_combined_eval_report,
)
from .config import load_dotenv
from .conversation_store import ConversationStore
from .etl import load_processed_chunks, persist_processed
from .entity_memory import EntityResolver, context_resolution_to_legacy_payload, entity_types_to_clear, extract_entities_from_state
from .eval_repair import split_and_repair_humanlike_evalset, write_eval_repair_report
from .evaluation import (
    evaluate_quality_gates,
    run_ablation,
    run_evaluation,
    run_groundedness_evaluation,
    write_ablation_report,
    write_eval_report,
    write_groundedness_report,
    write_quality_gate_report,
)
from .fallback_stress import run_fallback_stress, write_fallback_stress_report
from .generator import DEFAULT_LLM_MODEL, build_generator, check_openai_compatible_llm
from .heldout_summary import build_frozen_heldout_summary, write_frozen_heldout_summary
from .humanlike_eval import audit_eval_leakage, build_designed_evalsets, build_humanlike_evalset, write_leakage_report
from .importers import download_amazon_reviews_full, import_amazon_reviews_sample
from .llm_judge import run_llm_judge_evaluation, write_llm_judge_report
from .memory_eval import run_memory_evaluation, write_memory_eval_report
from .refusal_eval import run_refusal_evaluation, write_refusal_eval_report
from .rerankers import CrossEncoderReranker
from .retrieval import HybridRetriever
from .retriever_backends import QdrantBackend
from .scale_builder import DEFAULT_CATEGORIES, build_scale_subset
from .serialization import agent_state_to_dict
from .sql_store import build_sqlite_store, default_db_path, summarize_sqlite_store
from .tool_eval import run_tool_evaluation, write_tool_eval_report
from .trace_store import TraceSQLiteStore, TraceStore

DEFAULT_EMBEDDING_MODEL = "BAAI/bge-large-en-v1.5"
DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-large"


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_data_dir() -> Path:
    return project_root() / "data"


def load_project_env() -> None:
    load_dotenv(project_root() / ".env")


def build_agent(
    data_dir: Path,
    *,
    generator_name: str = "template",
    advisor_name: str = "rule",
    reranker: CrossEncoderReranker | None = None,
    use_env_reranker: bool = True,
) -> CommerceRAGAgent:
    chunks = load_processed_chunks(data_dir)
    retriever = HybridRetriever(chunks, reranker=reranker, use_env_reranker=use_env_reranker)
    return CommerceRAGAgent(retriever, data_dir, generator=build_generator(generator_name), advisor=build_advisor(advisor_name))


def build_cli_reranker(args: argparse.Namespace) -> CrossEncoderReranker | None:
    model_name = getattr(args, "reranker_model", DEFAULT_RERANKER_MODEL)
    if model_name.lower() in {"", "none", "off", "disabled"}:
        return None
    return CrossEncoderReranker(
        model_name,
        device=getattr(args, "reranker_device", "cuda"),
        batch_size=getattr(args, "reranker_batch_size", 16),
    )


def cli_uses_env_reranker(args: argparse.Namespace) -> bool:
    model_name = getattr(args, "reranker_model", DEFAULT_RERANKER_MODEL)
    return model_name.lower() not in {"", "none", "off", "disabled"}


def add_generator_arg(parser: argparse.ArgumentParser, *, default: str) -> None:
    parser.add_argument("--generator", choices=["template", "openai-compatible", "llm"], default=default)


def add_advisor_arg(parser: argparse.ArgumentParser, *, default: str) -> None:
    parser.add_argument(
        "--advisor",
        choices=["rule", "auto", "openai-compatible", "llm"],
        default=default,
        help="LLM planning advisor for intent/tool/action suggestions; rules and ToolPolicy remain final safeguards.",
    )


def add_reranker_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--reranker-model",
        default=DEFAULT_RERANKER_MODEL,
        help="CrossEncoder reranker model; use 'none' to disable neural reranking.",
    )
    parser.add_argument("--reranker-device", default="cuda")
    parser.add_argument("--reranker-batch-size", type=int, default=16)


def add_eval_backend_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--backend", choices=["local", "qdrant"], default="local")
    parser.add_argument("--qdrant-path", type=Path, default=project_root() / ".qdrant")
    parser.add_argument("--collection", default="commerce_rag_chunks")
    parser.add_argument("--embedding-backend", choices=["auto", "hash", "sentence-transformers", "local"], default="auto")
    parser.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    parser.add_argument("--embedding-device", default="cuda")
    parser.add_argument("--embedding-batch-size", type=int, default=32)


def build_retriever_backend(args: argparse.Namespace, chunks: list):
    if getattr(args, "backend", "local") == "qdrant":
        embedding_args = resolve_qdrant_embedding_args(args)
        return QdrantBackend(
            args.collection,
            chunks=chunks,
            path=str(args.qdrant_path),
            reranker=build_cli_reranker(args),
            **embedding_args,
        )
    return HybridRetriever(
        chunks,
        reranker=build_cli_reranker(args),
        use_env_reranker=cli_uses_env_reranker(args),
    )


def model_config(args: argparse.Namespace) -> dict[str, str]:
    backend = getattr(args, "backend", "local")
    llm_model = os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL)
    if getattr(args, "generator", "template") == "template":
        llm_model = "template"
    if backend == "qdrant":
        embedding_args = resolve_qdrant_embedding_args(args)
        return {
            "embedding_model": embedding_args["embedding_model_name"],
            "embedding_backend": embedding_args["embedding_backend"],
            "reranker_model": getattr(args, "reranker_model", DEFAULT_RERANKER_MODEL),
            "llm_model": llm_model,
        }
    return {
        "embedding_model": "local-token-cosine",
        "embedding_backend": "local",
        "reranker_model": getattr(args, "reranker_model", DEFAULT_RERANKER_MODEL),
        "llm_model": llm_model,
    }


def require_real_generator(args: argparse.Namespace, command_name: str) -> None:
    if getattr(args, "generator", "openai-compatible") == "template":
        raise SystemExit(f"{command_name} requires a real API generator; use --generator openai-compatible or --generator llm.")


def qdrant_embedding_config_path(qdrant_path: Path, collection: str) -> Path:
    return qdrant_path / f"{collection}.embedding.json"


def write_qdrant_embedding_config(args: argparse.Namespace) -> None:
    args.qdrant_path.mkdir(parents=True, exist_ok=True)
    payload = {
        "embedding_backend": args.embedding_backend,
        "embedding_model": args.embedding_model,
        "embedding_device": args.embedding_device,
        "embedding_batch_size": args.embedding_batch_size,
    }
    qdrant_embedding_config_path(args.qdrant_path, args.collection).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def resolve_qdrant_embedding_args(args: argparse.Namespace) -> dict:
    if args.embedding_backend != "auto":
        return {
            "embedding_backend": args.embedding_backend,
            "embedding_model_name": args.embedding_model,
            "embedding_device": args.embedding_device,
            "embedding_batch_size": args.embedding_batch_size,
        }
    path = qdrant_embedding_config_path(args.qdrant_path, args.collection)
    if path.exists():
        payload = json.loads(path.read_text(encoding="utf-8"))
        return {
            "embedding_backend": payload.get("embedding_backend", "hash"),
            "embedding_model_name": payload.get("embedding_model", DEFAULT_EMBEDDING_MODEL),
            "embedding_device": payload.get("embedding_device", "cuda"),
            "embedding_batch_size": int(payload.get("embedding_batch_size", 64)),
        }
    return {
        "embedding_backend": "sentence-transformers",
        "embedding_model_name": args.embedding_model,
        "embedding_device": args.embedding_device,
        "embedding_batch_size": args.embedding_batch_size,
    }


def cmd_ingest(args: argparse.Namespace) -> None:
    chunks = persist_processed(args.data_dir)
    print(f"Built {len(chunks)} chunks at {args.data_dir / 'processed' / 'chunks.jsonl'}")


def cmd_ask(args: argparse.Namespace) -> None:
    agent = build_agent(
        args.data_dir,
        generator_name=args.generator,
        advisor_name=args.advisor,
        reranker=build_cli_reranker(args),
        use_env_reranker=cli_uses_env_reranker(args),
    )
    state, memory_payload = run_with_optional_memory(agent, args.query, args)
    payload = agent_state_to_dict(state)
    payload.update(memory_payload)
    if args.trace_out:
        args.trace_out.parent.mkdir(parents=True, exist_ok=True)
        args.trace_out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    if args.trace_store:
        payload["stored_trace"] = TraceStore(args.trace_store).append(state)
    if args.trace_db:
        payload["stored_trace_db"] = TraceSQLiteStore(args.trace_db).append(state)
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def cmd_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_evaluation(
        agent,
        retriever,
        args.data_dir,
        mode=args.mode,
        limit=args.limit,
        backend_name=args.backend,
        model_config=model_config(args),
        eval_filename=args.eval_filename,
        use_oracle_sources=args.use_oracle_sources,
    )
    report_name = {
        "scripted_regression": "scripted_regression_report.md",
        "humanlike_blind": "humanlike_blind_report.md",
        "humanlike_single_turn_resolvable": "humanlike_single_turn_resolvable_report.md",
        "humanlike_context_required": "humanlike_context_required_report.md",
        "challenge": "challenge_report.md",
    }.get(str(report.get("suite")), f"{report.get('suite', 'evaluation')}_report.md")
    report_path = args.output or project_root() / "reports" / report_name
    write_eval_report(report_path, report)
    print(json.dumps(report["retrieval"] | report["support_quality"] | report["latency"], indent=2))


def cmd_repair_evalsets(args: argparse.Namespace) -> None:
    report = split_and_repair_humanlike_evalset(
        data_dir=args.data_dir,
        source_filename=args.source_filename,
        resolvable_filename=args.resolvable_filename,
        context_required_filename=args.context_required_filename,
        repair_original=not args.keep_original,
        repair_challenge=not args.skip_challenge,
    )
    write_eval_repair_report(project_root() / "reports" / "eval_fairness_repair_report.md", report)
    print(json.dumps(report, indent=2, ensure_ascii=False))


def cmd_ablate(args: argparse.Namespace) -> None:
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    report = run_ablation(
        retriever,
        args.data_dir,
        limit=args.limit,
        eval_filename=args.eval_filename,
        use_oracle_sources=args.use_oracle_sources,
    )
    write_ablation_report(project_root() / "reports" / "ablation_report.md", report)
    print(json.dumps({mode: data["summary"] for mode, data in report["modes"].items()}, indent=2))


def cmd_gate(args: argparse.Namespace) -> None:
    require_real_generator(args, "gate")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_evaluation(
        agent,
        retriever,
        args.data_dir,
        limit=args.limit,
        backend_name=args.backend,
        model_config=model_config(args),
        eval_filename=args.eval_filename,
        use_oracle_sources=args.use_oracle_sources,
    )
    gate_report = evaluate_quality_gates(report, args.gates)
    write_eval_report(project_root() / "reports" / "evaluation_report.md", report)
    write_quality_gate_report(project_root() / "reports" / "quality_gate_report.md", gate_report)
    print(json.dumps(gate_report, indent=2))
    if not gate_report["passed"]:
        raise SystemExit(1)


def cmd_import_amazon_sample(args: argparse.Namespace) -> None:
    result = import_amazon_reviews_sample(
        args.data_dir,
        categories=args.categories,
        review_limit_per_category=args.review_limit,
        product_limit_per_category=args.product_limit,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_download_amazon_full(args: argparse.Namespace) -> None:
    result = download_amazon_reviews_full(
        args.data_dir,
        categories=args.categories,
        count_rows=args.count_rows,
        force=args.force,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_build_scale_subset(args: argparse.Namespace) -> None:
    result = build_scale_subset(
        args.data_dir,
        categories=args.categories,
        reviews_per_category=args.reviews_per_category,
        products_per_category=args.products_per_category,
        eval_size=args.eval_size,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_build_humanlike_eval(args: argparse.Namespace) -> None:
    result = build_humanlike_evalset(input_path=args.input, output_path=args.output, n=args.n)
    write_leakage_report(project_root() / "reports" / "humanlike_blind_leakage_report.md", result["leakage"])
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_audit_eval_leakage(args: argparse.Namespace) -> None:
    report = audit_eval_leakage(eval_path=args.input, docs_path=args.docs)
    write_leakage_report(project_root() / "reports" / "humanlike_blind_leakage_report.md", report)
    print(json.dumps(report, indent=2, ensure_ascii=False))


def cmd_build_designed_evalsets(args: argparse.Namespace) -> None:
    result = build_designed_evalsets(
        data_dir=args.data_dir,
        normal_n=args.humanlike_normal,
        challenge_n=args.challenge,
        refusal_n=args.refusal_safety,
        multiturn_n=args.multiturn_memory,
    )
    write_leakage_report(project_root() / "reports" / "humanlike_blind_leakage_report.md", result["leakage"]["humanlike_blind"])
    write_leakage_report(project_root() / "reports" / "challenge_leakage_report.md", result["leakage"]["challenge"])
    print(json.dumps(result, indent=2, ensure_ascii=False))


def cmd_qdrant_index(args: argparse.Namespace) -> None:
    chunks = load_processed_chunks(args.data_dir)
    backend = QdrantBackend(
        args.collection,
        chunks=chunks,
        path=str(args.qdrant_path),
        embedding_backend=args.embedding_backend,
        embedding_model_name=args.embedding_model,
        embedding_device=args.embedding_device,
        embedding_batch_size=args.embedding_batch_size,
    )
    count = backend.recreate(chunks)
    write_qdrant_embedding_config(args)
    print(
        json.dumps(
            {
                "collection": args.collection,
                "points": count,
                "path": str(args.qdrant_path),
                "embedding_backend": args.embedding_backend,
                "embedding_model": backend.embedding_model.name,
                "embedding_dimensions": backend.embedding_model.dimensions,
            },
            indent=2,
        )
    )


def cmd_qdrant_ask(args: argparse.Namespace) -> None:
    chunks = load_processed_chunks(args.data_dir)
    embedding_args = resolve_qdrant_embedding_args(args)
    backend = QdrantBackend(args.collection, chunks=chunks, path=str(args.qdrant_path), **embedding_args)
    agent = CommerceRAGAgent(backend, args.data_dir, generator=build_generator(args.generator), advisor=build_advisor(args.advisor))
    state, memory_payload = run_with_optional_memory(agent, args.query, args)
    payload = agent_state_to_dict(state)
    payload.update(memory_payload)
    if args.trace_db:
        payload["stored_trace_db"] = TraceSQLiteStore(args.trace_db).append(state)
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def run_with_optional_memory(agent: CommerceRAGAgent, query: str, args: argparse.Namespace) -> tuple:
    conversation_db = getattr(args, "conversation_db", None)
    if conversation_db is None:
        return agent.run(query, max_retries=args.max_retries), {}
    store = ConversationStore(conversation_db)
    resolver = EntityResolver()
    user_id = getattr(args, "user_id", None)
    memory_context = store.load_context(getattr(args, "conversation_id", None), user_id)
    context_resolution = resolver.resolve_context(query, memory_context)
    resolution = context_resolution_to_legacy_payload(query, context_resolution)
    agent_query = query
    memory_context["original_query"] = query
    memory_context["resolved_query"] = agent_query
    memory_context["entity_resolution"] = resolution
    memory_context["context_resolution"] = context_resolution.to_dict()
    memory_context["resolved_entities"] = resolution.get("used_entities", [])
    state = agent.run(agent_query, max_retries=args.max_retries, memory_context=memory_context)
    turn_ids = store.append_exchange(
        conversation_id=memory_context["conversation_id"],
        user_id=user_id,
        original_query=query,
        resolved_query=agent_query,
        state=state,
    )
    extracted_entities = extract_entities_from_state(state)
    clear_types = entity_types_to_clear(resolution)
    store.clear_entities(memory_context["conversation_id"], clear_types)
    store.upsert_entities(memory_context["conversation_id"], extracted_entities, turn_id=turn_ids["user_turn_id"])
    state.trace.append(
        {
            "event": "entity_update",
            "conversation_id": memory_context["conversation_id"],
            "cleared_entity_types": clear_types,
            "entity_count": len(extracted_entities),
            "entities": extracted_entities,
        }
    )
    return state, {
        "conversation_id": memory_context["conversation_id"],
        "resolved_query": agent_query,
        "context_resolution": context_resolution.to_dict(),
        "memory_used": {
            "recent_turns": len(memory_context.get("recent_turns", [])),
            "entities": resolution.get("used_entities", []),
            "blocked_reasons": resolution.get("blocked_reasons", []),
        },
    }


def cmd_build_sql(args: argparse.Namespace) -> None:
    summary = build_sqlite_store(args.data_dir, args.db_path)
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def cmd_sql_summary(args: argparse.Namespace) -> None:
    print(json.dumps(summarize_sqlite_store(args.db_path), indent=2, ensure_ascii=False))


def cmd_audit(args: argparse.Namespace) -> None:
    report = audit_project(args.data_dir, args.qdrant_path)
    write_audit_report(project_root() / "reports" / "project_audit.md", report)
    print(json.dumps(report, indent=2, ensure_ascii=False))


def cmd_llm_check(args: argparse.Namespace) -> None:
    print(json.dumps(check_openai_compatible_llm(), indent=2, ensure_ascii=False))


def cmd_traces(args: argparse.Namespace) -> None:
    command = args.trace_command or "list"
    if command == "legacy-jsonl":
        rows = TraceStore(args.trace_store).tail(args.limit)
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    store = TraceSQLiteStore(args.trace_db)
    if command == "list":
        rows = store.list_runs(limit=args.limit, intent=args.intent, action=args.action)
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    if command == "show":
        run = store.get_run(args.trace_id)
        if not run:
            raise SystemExit(f"Trace not found: {args.trace_id}")
        payload = {"run": run, "spans": store.spans(args.trace_id)}
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return
    if command == "tree":
        spans = store.spans(args.trace_id)
        if not spans:
            raise SystemExit(f"Trace spans not found: {args.trace_id}")
        print(_format_span_tree(spans))
        return
    if command == "candidates":
        rows = store.candidates(args.trace_id, attempt=args.attempt)
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    if command == "tools":
        rows = store.tool_trace(args.trace_id)
        if not rows:
            raise SystemExit(f"Tool trace not found: {args.trace_id}")
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    if command == "failures":
        rows = store.failures(intent=args.intent, limit=args.limit)
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return
    raise SystemExit(f"Unknown traces command: {command}")


def cmd_fallback_stress(args: argparse.Namespace) -> None:
    report = run_fallback_stress(args.data_dir)
    write_fallback_stress_report(project_root() / "reports" / "fallback_stress_report.md", report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if not report["passed"]:
        raise SystemExit(1)


def cmd_refusal_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "refusal-eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_refusal_evaluation(agent, args.data_dir, path=args.refusal_path)
    write_refusal_eval_report(project_root() / "reports" / "refusal_eval_report.md", report)
    print(json.dumps({key: report[key] for key in ["n", "pass_rate", "refusal_rate", "citation_leak_rate", "action_counts", "intent_counts"]}, indent=2, ensure_ascii=False))
    if report["pass_rate"] < args.min_pass_rate:
        raise SystemExit(1)


def cmd_combined_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "combined-eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    if args.normal_report:
        normal_report = apply_golden_metadata(load_eval_report_json(args.normal_report), args.data_dir / "eval" / "golden.jsonl")
    else:
        normal_report = run_evaluation(
            agent,
            retriever,
            args.data_dir,
            mode=args.mode,
            limit=args.limit,
            backend_name=args.backend,
            model_config=model_config(args),
        )
    refusal_report = run_refusal_evaluation(agent, args.data_dir, path=args.refusal_path)
    report = run_combined_evaluation(normal_report, refusal_report)
    write_combined_eval_report(project_root() / "reports" / "combined_eval_report.md", report)
    print(
        json.dumps(
            {
                "normal_n": report["normal_n"],
                "boundary_n": report["boundary_n"],
                "n": report["n"],
                "pass_rate": report["pass_rate"],
                "action_match_rate": report["action_match_rate"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_judge_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "judge-eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_llm_judge_evaluation(agent, args.data_dir, limit=args.limit, offset=args.offset)
    write_llm_judge_report(project_root() / "reports" / "llm_judge_report.md", report)
    print(
        json.dumps(
            {
                "n": report["n"],
                "judge_model": report["judge_model"],
                "pass_rate": report["pass_rate"],
                "groundedness": report["groundedness"],
                "relevance": report["relevance"],
                "citation_support": report["citation_support"],
                "safety": report["safety"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_groundedness_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "groundedness-eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_groundedness_evaluation(
        agent,
        args.data_dir,
        eval_filename=args.eval_filename,
        limit=args.limit,
        offset=args.offset,
    )
    report_stem = args.eval_filename.replace(".jsonl", "")
    write_groundedness_report(project_root() / "reports" / f"{report_stem}_groundedness_report.md", report)
    print(
        json.dumps(
            {
                "n": report["n"],
                "judge_model": report["judge_model"],
                "Business QA Pass Rate": report["business_qa_pass_rate"],
                "final_groundedness_pass_rate": report["final_groundedness_pass_rate"],
                "unsupported_claim_rate": report["unsupported_claim_rate"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_memory_eval(args: argparse.Namespace) -> None:
    require_real_generator(args, "memory-eval")
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator(args.generator))
    report = run_memory_evaluation(agent, args.data_dir, path=args.memory_eval_path)
    write_memory_eval_report(project_root() / "reports" / "memory_eval_report.md", report)
    print(
        json.dumps(
            {
                "n": report["n"],
                "entity_carryover_accuracy": report["entity_carryover_accuracy"],
                "wrong_entity_leak_rate": report["wrong_entity_leak_rate"],
                "clarification_rate_when_ambiguous": report["clarification_rate_when_ambiguous"],
                "privacy_memory_block_rate": report["privacy_memory_block_rate"],
                "multi_turn_answer_success_rate": report["multi_turn_answer_success_rate"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_tool_eval(args: argparse.Namespace) -> None:
    chunks = load_processed_chunks(args.data_dir)
    retriever = build_retriever_backend(args, chunks)
    agent = CommerceRAGAgent(retriever, args.data_dir, generator=build_generator("template"))
    report = run_tool_evaluation(agent, args.data_dir, path=args.tool_eval_path)
    write_tool_eval_report(project_root() / "reports" / "tool_eval_report.md", report)
    print(
        json.dumps(
            {
                "n": report["n"],
                "tool_call_precision": report["tool_call_precision"],
                "tool_call_recall": report["tool_call_recall"],
                "missing_required_tool_rate": report["missing_required_tool_rate"],
                "forbidden_tool_call_rate": report["forbidden_tool_call_rate"],
                "structured_fact_accuracy": report["structured_fact_accuracy"],
                "tool_grounded_answer_rate": report["tool_grounded_answer_rate"],
                "unknown_entity_refusal_rate": report["unknown_entity_refusal_rate"],
                "write_tool_confirmation_rate": report["write_tool_confirmation_rate"],
                "pass_rate": report["pass_rate"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def cmd_heldout_summary(args: argparse.Namespace) -> None:
    report = build_frozen_heldout_summary(project_root() / "reports")
    output = args.output or project_root() / "reports" / "frozen_heldout_eval_summary.md"
    write_frozen_heldout_summary(output, report)
    print(json.dumps({"output": str(output), "retrieval_rows": len(report["retrieval"])}, indent=2, ensure_ascii=False))


def _format_span_tree(spans: list[dict]) -> str:
    by_parent: dict[str | None, list[dict]] = {}
    by_id = {span["span_id"]: span for span in spans}
    for span in spans:
        by_parent.setdefault(span.get("parent_span_id"), []).append(span)
    roots = [span for span in spans if span.get("parent_span_id") not in by_id]
    lines: list[str] = []

    def render(span: dict, prefix: str = "", is_last: bool = True, depth: int = 0) -> None:
        connector = "" if depth == 0 else ("└─ " if is_last else "├─ ")
        duration = span.get("duration_ms")
        status = span.get("status") or "ok"
        outputs = span.get("outputs") or {}
        metrics = span.get("metrics") or {}
        suffix = ""
        if "action" in outputs:
            suffix = f" -> {outputs['action']}"
        elif "intent" in outputs:
            suffix = f" -> {outputs['intent']}"
        elif "planned_sources" in outputs:
            suffix = " -> " + ",".join(outputs["planned_sources"])
        elif "selected" in metrics:
            suffix = f" selected={metrics['selected']}"
        lines.append(f"{prefix}{connector}{span['name']} {duration if duration is not None else '?'}ms {status}{suffix}")
        children = by_parent.get(span["span_id"], [])
        child_prefix = prefix + ("   " if is_last else "│  ") if depth > 0 else ""
        for index, child in enumerate(children):
            render(child, child_prefix, index == len(children) - 1, depth + 1)

    for index, root in enumerate(roots):
        render(root, "", index == len(roots) - 1, 0)
    return "\n".join(lines)


def main() -> None:
    load_project_env()
    parser = argparse.ArgumentParser(description="CommerceRAG Ops CLI")
    parser.add_argument("--data-dir", type=Path, default=default_data_dir())
    sub = parser.add_subparsers(dest="command", required=True)

    ingest = sub.add_parser("ingest", help="Build processed chunks from raw data")
    ingest.set_defaults(func=cmd_ingest)

    ask = sub.add_parser("ask", help="Run the agentic RAG flow")
    ask.add_argument("query")
    ask.add_argument("--max-retries", type=int, default=1)
    add_generator_arg(ask, default="openai-compatible")
    add_advisor_arg(ask, default="auto")
    add_reranker_args(ask)
    ask.add_argument("--trace-out", type=Path, default=None, help="Write full AgentState trace JSON")
    ask.add_argument("--trace-store", type=Path, default=None, help="Append full AgentState trace to JSONL store")
    ask.add_argument("--trace-db", type=Path, default=None, help="Append span trace to a SQLite trace DB")
    ask.add_argument("--conversation-db", type=Path, default=None, help="Enable conversation/entity memory with this SQLite DB")
    ask.add_argument("--conversation-id", default=None)
    ask.add_argument("--user-id", default=None)
    ask.set_defaults(func=cmd_ask)

    eval_cmd = sub.add_parser("eval", help="Run retrieval and support-quality evaluation")
    eval_cmd.add_argument("--mode", choices=["dense", "bm25", "hybrid", "hybrid_rerank"], default="hybrid_rerank")
    eval_cmd.add_argument("--limit", type=int, default=None)
    eval_cmd.add_argument("--eval-filename", default=None, help="Eval JSONL under data/eval; defaults to scripted_regression.jsonl when present")
    eval_cmd.add_argument("--use-oracle-sources", action="store_true", help="Use row['sources'] as an oracle source filter")
    eval_cmd.add_argument("--output", type=Path, default=None, help="Write markdown report to this path instead of the suite default")
    add_eval_backend_args(eval_cmd)
    add_generator_arg(eval_cmd, default="openai-compatible")
    add_reranker_args(eval_cmd)
    eval_cmd.set_defaults(func=cmd_eval)

    ablate = sub.add_parser("ablate", help="Run retrieval ablation across dense/BM25/hybrid modes")
    ablate.add_argument("--limit", type=int, default=None)
    ablate.add_argument("--eval-filename", default=None)
    ablate.add_argument("--use-oracle-sources", action="store_true")
    add_eval_backend_args(ablate)
    add_reranker_args(ablate)
    ablate.set_defaults(func=cmd_ablate)

    gate = sub.add_parser("gate", help="Run eval and enforce quality gates")
    gate.add_argument("--gates", type=Path, default=default_data_dir() / "quality_gates.json")
    gate.add_argument("--limit", type=int, default=None)
    gate.add_argument("--eval-filename", default=None)
    gate.add_argument("--use-oracle-sources", action="store_true")
    add_eval_backend_args(gate)
    add_generator_arg(gate, default="openai-compatible")
    add_reranker_args(gate)
    gate.set_defaults(func=cmd_gate)

    import_cmd = sub.add_parser("import-amazon-sample", help="Import a small Amazon Reviews 2023 sample")
    import_cmd.add_argument("--categories", nargs="+", default=["All_Beauty"])
    import_cmd.add_argument("--review-limit", type=int, default=50)
    import_cmd.add_argument("--product-limit", type=int, default=50)
    import_cmd.set_defaults(func=cmd_import_amazon_sample)

    full_cmd = sub.add_parser("download-amazon-full", help="Download official full Amazon Reviews 2023 gzip files")
    full_cmd.add_argument("--categories", nargs="+", default=["All_Beauty", "Software", "Baby_Products"])
    full_cmd.add_argument("--count-rows", action="store_true")
    full_cmd.add_argument("--force", action="store_true", help="Redownload files even if they already exist")
    full_cmd.set_defaults(func=cmd_download_amazon_full)

    scale_cmd = sub.add_parser("build-scale-subset", help="Build realistic Amazon subset, multi-granularity RAG docs, and 300+ eval set")
    scale_cmd.add_argument("--categories", nargs="+", default=DEFAULT_CATEGORIES)
    scale_cmd.add_argument("--reviews-per-category", type=int, default=5000)
    scale_cmd.add_argument("--products-per-category", type=int, default=1000)
    scale_cmd.add_argument("--eval-size", type=int, default=360)
    scale_cmd.set_defaults(func=cmd_build_scale_subset)

    humanlike = sub.add_parser("build-humanlike-eval", help="Build blind humanlike eval queries with a real LLM API")
    humanlike.add_argument("--input", type=Path, default=default_data_dir() / "scale" / "rag_documents.jsonl")
    humanlike.add_argument("--output", type=Path, default=default_data_dir() / "eval" / "humanlike_blind.jsonl")
    humanlike.add_argument("--n", type=int, default=300)
    humanlike.set_defaults(func=cmd_build_humanlike_eval)

    leak = sub.add_parser("audit-eval-leakage", help="Audit humanlike eval query leakage")
    leak.add_argument("--input", type=Path, default=default_data_dir() / "eval" / "humanlike_blind.jsonl")
    leak.add_argument("--docs", type=Path, default=default_data_dir() / "scale" / "rag_documents.jsonl")
    leak.set_defaults(func=cmd_audit_eval_leakage)

    repair_evalsets = sub.add_parser("repair-evalsets", help="Split unfair humanlike rows and repair forbidden_evidence labels")
    repair_evalsets.add_argument("--source-filename", default="humanlike_blind.jsonl")
    repair_evalsets.add_argument("--resolvable-filename", default="humanlike_single_turn_resolvable.jsonl")
    repair_evalsets.add_argument("--context-required-filename", default="humanlike_context_required.jsonl")
    repair_evalsets.add_argument("--keep-original", action="store_true", help="Do not rewrite the source eval file with repaired rows")
    repair_evalsets.add_argument("--skip-challenge", action="store_true", help="Do not repair challenge.jsonl forbidden_evidence")
    repair_evalsets.set_defaults(func=cmd_repair_evalsets)

    designed = sub.add_parser("build-designed-evalsets", help="Build V2 heldout evalsets at the designed scale with a real LLM API")
    designed.add_argument("--humanlike-normal", type=int, default=200)
    designed.add_argument("--challenge", type=int, default=100)
    designed.add_argument("--refusal-safety", type=int, default=50)
    designed.add_argument("--multiturn-memory", type=int, default=50)
    designed.set_defaults(func=cmd_build_designed_evalsets)

    qindex = sub.add_parser("qdrant-index", help="Build an embedded local Qdrant collection from processed chunks")
    qindex.add_argument("--qdrant-path", type=Path, default=project_root() / ".qdrant")
    qindex.add_argument("--collection", default="commerce_rag_chunks")
    qindex.add_argument("--embedding-backend", choices=["hash", "sentence-transformers", "local"], default="sentence-transformers")
    qindex.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    qindex.add_argument("--embedding-device", default="cuda")
    qindex.add_argument("--embedding-batch-size", type=int, default=32)
    qindex.set_defaults(func=cmd_qdrant_index)

    qask = sub.add_parser("qdrant-ask", help="Ask using the embedded local Qdrant backend")
    qask.add_argument("query")
    qask.add_argument("--qdrant-path", type=Path, default=project_root() / ".qdrant")
    qask.add_argument("--collection", default="commerce_rag_chunks")
    qask.add_argument("--max-retries", type=int, default=1)
    add_generator_arg(qask, default="openai-compatible")
    add_advisor_arg(qask, default="auto")
    qask.add_argument("--embedding-backend", choices=["auto", "hash", "sentence-transformers", "local"], default="auto")
    qask.add_argument("--embedding-model", default=DEFAULT_EMBEDDING_MODEL)
    qask.add_argument("--embedding-device", default="cuda")
    qask.add_argument("--embedding-batch-size", type=int, default=32)
    qask.add_argument("--trace-db", type=Path, default=None, help="Append span trace to a SQLite trace DB")
    qask.add_argument("--conversation-db", type=Path, default=None, help="Enable conversation/entity memory with this SQLite DB")
    qask.add_argument("--conversation-id", default=None)
    qask.add_argument("--user-id", default=None)
    qask.set_defaults(func=cmd_qdrant_ask)

    build_sql = sub.add_parser("build-sql", help="Build SQLite structured store from raw, generated, and downloaded metadata")
    build_sql.add_argument("--db-path", type=Path, default=default_db_path(default_data_dir()))
    build_sql.set_defaults(func=cmd_build_sql)

    sql_summary = sub.add_parser("sql-summary", help="Summarize the SQLite structured store")
    sql_summary.add_argument("--db-path", type=Path, default=default_db_path(default_data_dir()))
    sql_summary.set_defaults(func=cmd_sql_summary)

    audit = sub.add_parser("audit", help="Audit data coverage, downloaded samples, Qdrant, and LLM config")
    audit.add_argument("--qdrant-path", type=Path, default=project_root() / ".qdrant")
    audit.set_defaults(func=cmd_audit)

    llm_check = sub.add_parser("llm-check", help="Check OpenAI-compatible LLM connectivity using env vars")
    llm_check.set_defaults(func=cmd_llm_check)

    traces = sub.add_parser("traces", help="Query span traces from SQLite or legacy JSONL")
    traces.add_argument("--trace-db", type=Path, default=project_root() / "reports" / "traces.db")
    traces.add_argument("--trace-store", type=Path, default=project_root() / "reports" / "traces.jsonl")
    traces.add_argument("--limit", type=int, default=20)
    traces.add_argument("--intent", default=None)
    traces.add_argument("--action", default=None)
    trace_sub = traces.add_subparsers(dest="trace_command")

    trace_list = trace_sub.add_parser("list", help="List recent traces")
    trace_list.add_argument("--limit", type=int, default=20)
    trace_list.add_argument("--intent", default=None)
    trace_list.add_argument("--action", default=None)
    trace_list.set_defaults(func=cmd_traces)

    trace_show = trace_sub.add_parser("show", help="Show a trace run and spans")
    trace_show.add_argument("trace_id")
    trace_show.set_defaults(func=cmd_traces)

    trace_tree = trace_sub.add_parser("tree", help="Print a trace span tree")
    trace_tree.add_argument("trace_id")
    trace_tree.set_defaults(func=cmd_traces)

    trace_candidates = trace_sub.add_parser("candidates", help="Show retrieval candidates for a trace")
    trace_candidates.add_argument("trace_id")
    trace_candidates.add_argument("--attempt", type=int, default=None)
    trace_candidates.set_defaults(func=cmd_traces)

    trace_tools = trace_sub.add_parser("tools", help="Show tool plan, calls, and tool citation validation for a trace")
    trace_tools.add_argument("trace_id")
    trace_tools.set_defaults(func=cmd_traces)

    trace_failures = trace_sub.add_parser("failures", help="List refuse/escalate traces")
    trace_failures.add_argument("--intent", default=None)
    trace_failures.add_argument("--limit", type=int, default=50)
    trace_failures.set_defaults(func=cmd_traces)

    trace_jsonl = trace_sub.add_parser("legacy-jsonl", help="Read legacy JSONL traces")
    trace_jsonl.add_argument("--limit", type=int, default=20)
    trace_jsonl.set_defaults(func=cmd_traces)
    traces.set_defaults(func=cmd_traces)

    fallback_stress = sub.add_parser("fallback-stress", help="Run scripted agentic fallback stress cases")
    fallback_stress.set_defaults(func=cmd_fallback_stress)

    refusal_eval = sub.add_parser("refusal-eval", help="Run unknown/refusal boundary evaluation")
    refusal_eval.add_argument("--refusal-path", type=Path, default=default_data_dir() / "eval" / "refusal.jsonl")
    refusal_eval.add_argument("--min-pass-rate", type=float, default=0.95)
    add_eval_backend_args(refusal_eval)
    add_generator_arg(refusal_eval, default="openai-compatible")
    add_reranker_args(refusal_eval)
    refusal_eval.set_defaults(func=cmd_refusal_eval)

    combined_eval = sub.add_parser("combined-eval", help="Run normal eval plus refusal eval and write a 414+ case combined report")
    combined_eval.add_argument("--mode", choices=["dense", "bm25", "hybrid", "hybrid_rerank"], default="hybrid_rerank")
    combined_eval.add_argument("--limit", type=int, default=None)
    combined_eval.add_argument("--refusal-path", type=Path, default=default_data_dir() / "eval" / "refusal.jsonl")
    combined_eval.add_argument(
        "--normal-report",
        type=Path,
        default=None,
        help="Reuse an existing eval markdown report instead of rerunning normal golden queries.",
    )
    add_eval_backend_args(combined_eval)
    add_generator_arg(combined_eval, default="openai-compatible")
    add_reranker_args(combined_eval)
    combined_eval.set_defaults(func=cmd_combined_eval)

    judge_eval = sub.add_parser("judge-eval", help="Run LLM-as-judge groundedness/citation/safety evaluation on a sample")
    judge_eval.add_argument("--limit", type=int, default=12)
    judge_eval.add_argument("--offset", type=int, default=0)
    add_eval_backend_args(judge_eval)
    add_generator_arg(judge_eval, default="openai-compatible")
    add_reranker_args(judge_eval)
    judge_eval.set_defaults(func=cmd_judge_eval)

    groundedness = sub.add_parser("groundedness-eval", help="Run deterministic + real LLM judge groundedness evaluation")
    groundedness.add_argument("--eval-filename", default="humanlike_blind.jsonl")
    groundedness.add_argument("--limit", type=int, default=None)
    groundedness.add_argument("--offset", type=int, default=0)
    add_eval_backend_args(groundedness)
    add_generator_arg(groundedness, default="openai-compatible")
    add_reranker_args(groundedness)
    groundedness.set_defaults(func=cmd_groundedness_eval)

    memory_eval = sub.add_parser("memory-eval", help="Run multi-turn conversation/entity memory evaluation")
    memory_eval.add_argument("--memory-eval-path", type=Path, default=default_data_dir() / "eval" / "multiturn_memory.jsonl")
    add_eval_backend_args(memory_eval)
    add_generator_arg(memory_eval, default="openai-compatible")
    add_reranker_args(memory_eval)
    memory_eval.set_defaults(func=cmd_memory_eval)

    tool_eval = sub.add_parser("tool-eval", help="Run structured tool planning/execution evaluation")
    tool_eval.add_argument("--tool-eval-path", type=Path, default=default_data_dir() / "eval" / "tool_golden.jsonl")
    add_eval_backend_args(tool_eval)
    add_reranker_args(tool_eval)
    tool_eval.set_defaults(func=cmd_tool_eval)

    heldout_summary = sub.add_parser("heldout-summary", help="Regenerate frozen heldout summary from existing reports")
    heldout_summary.add_argument("--output", type=Path, default=None)
    heldout_summary.set_defaults(func=cmd_heldout_summary)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
