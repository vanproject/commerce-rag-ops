from __future__ import annotations

import json
import re
import time
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any

from .agent import CommerceRAGAgent, answer_contains_keywords
from .citation_quality import validate_citation_contract
from .etl import read_jsonl
from .grounding_checks import final_groundedness_pass, run_deterministic_grounding_checks
from .judge import OpenAICompatibleGroundednessJudge
from .retrieval import RetrievalMode
from .retriever_backends import RetrieverBackend

SUPPORT_QUALITY_KEYS = [
    "action_accuracy",
    "citation_ok",
    "citation_leak_rate",
    "citation_schema_ok",
    "answer_citation_precision",
    "answer_citation_recall",
    "citation_grounded_rate",
    "keyword_coverage",
    "groundedness_proxy",
]

RETRIEVAL_V2_KEYS = [
    "exact_recall@5",
    "acceptable_recall@5",
    "entity_accuracy@5",
    "aspect_accuracy@5",
    "forbidden_rate@5",
]


class RelevanceLevel:
    EXACT = 2
    ACCEPTABLE = 1
    WRONG = 0
    FORBIDDEN = -1


def precision_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    if not retrieved:
        return 0.0
    relevant_set = set(relevant)
    seen: set[str] = set()
    hits = 0
    for item in retrieved[:k]:
        if item in seen:
            continue
        seen.add(item)
        if item in relevant_set:
            hits += 1
    return hits / min(k, len(retrieved))


def recall_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    if not relevant:
        return 0.0
    relevant_set = set(relevant)
    return len(set(retrieved[:k]) & relevant_set) / len(relevant_set)


def mrr(retrieved: list[str], relevant: list[str]) -> float:
    relevant_set = set(relevant)
    seen: set[str] = set()
    for idx, item in enumerate(retrieved, start=1):
        if item in seen:
            continue
        seen.add(item)
        if item in relevant_set:
            return 1.0 / idx
    return 0.0


def ndcg_at_k(retrieved: list[str], relevant: list[str], k: int) -> float:
    import math

    relevant_set = set(relevant)
    seen: set[str] = set()
    dcg = 0.0
    for idx, item in enumerate(retrieved[:k], start=1):
        if item in seen:
            continue
        seen.add(item)
        if item in relevant_set:
            dcg += 1.0 / math.log2(idx + 1)
    ideal_hits = min(k, len(relevant))
    idcg = sum(1.0 / math.log2(idx + 1) for idx in range(1, ideal_hits + 1))
    return dcg / idcg if idcg else 0.0


def precision_flags_at_k(flags: list[bool], k: int) -> float:
    if not flags:
        return 0.0
    return sum(1 for flag in flags[:k] if flag) / min(k, len(flags))


def recall_flags_at_k(flags: list[bool], relevant_count: int, k: int) -> float:
    if relevant_count <= 0:
        return 0.0
    return min(sum(1 for flag in flags[:k] if flag), relevant_count) / relevant_count


def mrr_flags(flags: list[bool]) -> float:
    for idx, flag in enumerate(flags, start=1):
        if flag:
            return 1.0 / idx
    return 0.0


def ndcg_flags_at_k(flags: list[bool], relevant_count: int, k: int) -> float:
    import math

    dcg = 0.0
    counted_hits = 0
    for idx, flag in enumerate(flags[:k], start=1):
        if flag and counted_hits < relevant_count:
            dcg += 1.0 / math.log2(idx + 1)
            counted_hits += 1
    ideal_hits = min(k, relevant_count)
    idcg = sum(1.0 / math.log2(idx + 1) for idx in range(1, ideal_hits + 1))
    return dcg / idcg if idcg else 0.0


def percentile(values: list[int], pct: int) -> int:
    if not values:
        return 0
    values = sorted(values)
    index = round((len(values) - 1) * pct / 100)
    return values[index]


def run_evaluation(
    agent: CommerceRAGAgent,
    retriever: RetrieverBackend,
    data_dir: Path,
    *,
    mode: RetrievalMode = "hybrid_rerank",
    limit: int | None = None,
    backend_name: str = "local",
    model_config: dict[str, Any] | None = None,
    eval_filename: str | None = None,
    use_oracle_sources: bool = False,
) -> dict[str, Any]:
    eval_path = _default_scripted_eval_path(data_dir, eval_filename)
    golden = read_jsonl(eval_path)
    if limit is not None:
        golden = golden[:limit]
    retrieval_rows: list[dict[str, Any]] = []
    support_rows: list[dict[str, Any]] = []
    latencies: list[int] = []

    for row in golden:
        sources = row.get("sources") if use_oracle_sources else None
        results = retriever.search(row["query"], sources=sources, top_k=5, mode=mode)
        retrieved_ids = [f"{r.chunk.source}:{r.chunk.doc_id}" for r in results]
        relevant_ids = _legacy_relevant_ids(row)
        relevant_flags = _relevance_flags(row, results, relevant_ids)
        relevance_levels = _relevance_levels(row, results, relevant_ids)
        result_signals = _result_signals(row, results, relevant_ids, relevant_flags)
        retrieval_rows.append(
            {
                "query_id": row["query_id"],
                "intent": row.get("intent", "unknown"),
                "expected_action": row.get("expected_action", "answer"),
                "safety_category": row.get("safety_category", "normal"),
                "difficulty": row.get("difficulty", "unknown"),
                "precision@5": precision_flags_at_k(relevant_flags, 5),
                "recall@5": recall_flags_at_k(relevant_flags, len(relevant_ids), 5),
                "mrr": mrr_flags(relevant_flags),
                "ndcg@5": ndcg_flags_at_k(relevant_flags, len(relevant_ids), 5),
                "exact_recall@5": _level_recall_at_k(relevance_levels, RelevanceLevel.EXACT, 5),
                "acceptable_recall@5": _acceptable_recall_at_k(row, relevance_levels, 5),
                "entity_accuracy@5": _entity_accuracy_at_k(row, results, 5),
                "aspect_accuracy@5": _aspect_accuracy_at_k(row, results, 5),
                "forbidden_rate@5": _forbidden_rate_at_k(relevance_levels, 5),
                "retrieved": retrieved_ids,
                "signals": result_signals,
            }
        )

        started = time.perf_counter()
        state = agent.run(row["query"], max_retries=1)
        latencies.append(int((time.perf_counter() - started) * 1000))
        evidence_gaps = _state_evidence_gaps(state)
        citation_contract = validate_citation_contract(
            answer=state.answer,
            citations=state.citations,
            retrieved_contexts=state.retrieved_contexts,
            must_cite=row.get("must_cite", True),
        )
        support_rows.append(
            {
                "query_id": row["query_id"],
                "expected_intent": row.get("intent", "unknown"),
                "intent": state.intent,
                "expected_action": row.get("expected_action", "answer"),
                "safety_category": row.get("safety_category", "normal"),
                "difficulty": row.get("difficulty", "unknown"),
                "action": state.action,
                "attempts": state.attempts,
                "evidence_gaps": evidence_gaps,
                "action_accuracy": 1.0 if state.action == row.get("expected_action", "answer") else 0.0,
                "citation_ok": 1.0 if state.citations or not row.get("must_cite", True) else 0.0,
                "citation_leak_rate": _citation_leak_rate(state, row, citation_contract),
                **citation_contract,
                "keyword_coverage": answer_contains_keywords(state.answer, row.get("expected_keywords", [])),
                "groundedness_proxy": state.grader_scores.get("groundedness_proxy", 0.0),
                "answer_preview": state.answer[:240],
            }
        )

    retrieval_summary = _average_metrics(retrieval_rows, ["precision@5", "recall@5", "mrr", "ndcg@5"])
    retrieval_summary.update(_average_metrics(retrieval_rows, RETRIEVAL_V2_KEYS))
    support_summary = _average_metrics(support_rows, SUPPORT_QUALITY_KEYS)
    return {
        "suite": _suite_name(eval_path),
        "eval_path": str(eval_path),
        "use_oracle_sources": use_oracle_sources,
        "n": len(golden),
        "retrieval_backend": backend_name,
        "retrieval_mode": mode,
        "model_config": model_config or {},
        "retrieval": retrieval_summary,
        "support_quality": support_summary,
        "latency": {"p50_ms": percentile(latencies, 50), "p95_ms": percentile(latencies, 95)},
        "by_intent": _group_metrics(retrieval_rows, support_rows, "intent"),
        "by_difficulty": _group_metrics(retrieval_rows, support_rows, "difficulty"),
        "retrieval_diagnostics": _diagnostic_summary(retrieval_rows),
        "agentic_diagnostics": _agentic_diagnostic_summary(support_rows),
        "retrieval_rows": retrieval_rows,
        "support_rows": support_rows,
    }


def run_ablation(
    retriever: RetrieverBackend,
    data_dir: Path,
    *,
    limit: int | None = None,
    eval_filename: str | None = None,
    use_oracle_sources: bool = False,
) -> dict[str, Any]:
    eval_path = _default_scripted_eval_path(data_dir, eval_filename)
    rows = read_jsonl(eval_path)
    if limit is not None:
        rows = rows[:limit]
    modes: list[RetrievalMode] = ["dense", "bm25", "hybrid", "hybrid_rerank"]
    by_mode: dict[str, Any] = {}
    for mode in modes:
        per_query: list[dict[str, Any]] = []
        for row in rows:
            sources = row.get("sources") if use_oracle_sources else None
            results = retriever.search(row["query"], sources=sources, top_k=5, mode=mode)
            retrieved_ids = [f"{r.chunk.source}:{r.chunk.doc_id}" for r in results]
            relevant_ids = _legacy_relevant_ids(row)
            relevant_flags = _relevance_flags(row, results, relevant_ids)
            per_query.append(
                {
                    "query_id": row["query_id"],
                    "intent": row.get("intent", "unknown"),
                    "expected_action": row.get("expected_action", "answer"),
                    "safety_category": row.get("safety_category", "normal"),
                    "difficulty": row.get("difficulty", "unknown"),
                    "precision@5": precision_flags_at_k(relevant_flags, 5),
                    "recall@5": recall_flags_at_k(relevant_flags, len(relevant_ids), 5),
                    "mrr": mrr_flags(relevant_flags),
                    "ndcg@5": ndcg_flags_at_k(relevant_flags, len(relevant_ids), 5),
                    "retrieved": retrieved_ids,
                }
            )
        by_mode[mode] = {
            "summary": _average_metrics(per_query, ["precision@5", "recall@5", "mrr", "ndcg@5"]),
            "rows": per_query,
        }
    return {"n": len(rows), "suite": _suite_name(eval_path), "eval_path": str(eval_path), "use_oracle_sources": use_oracle_sources, "modes": by_mode}


def evaluate_quality_gates(report: dict[str, Any], gates_path: Path) -> dict[str, Any]:
    gates = json.loads(gates_path.read_text(encoding="utf-8"))
    observed: dict[str, Any] = {
        "precision@5": report["retrieval"]["precision@5"],
        "recall@5": report["retrieval"]["recall@5"],
        "mrr": report["retrieval"]["mrr"],
        "ndcg@5": report["retrieval"]["ndcg@5"],
        "citation_ok": report["support_quality"]["citation_ok"],
        "citation_schema_ok": report["support_quality"].get("citation_schema_ok", 0.0),
        "answer_citation_precision": report["support_quality"].get("answer_citation_precision", 0.0),
        "answer_citation_recall": report["support_quality"].get("answer_citation_recall", 0.0),
        "citation_grounded_rate": report["support_quality"].get("citation_grounded_rate", 0.0),
        "keyword_coverage": report["support_quality"]["keyword_coverage"],
        "groundedness_proxy": report["support_quality"]["groundedness_proxy"],
        "latency_p95_ms": report["latency"]["p95_ms"],
    }
    checks: list[dict[str, Any]] = []
    for gate_name, threshold in gates.items():
        if gate_name.endswith("_min"):
            metric = gate_name[:-4]
            value = _metric_value(report, observed, metric)
            if value is None:
                checks.append(_skipped_gate(metric, ">=", threshold))
                continue
            passed = value >= threshold
            op = ">="
        elif gate_name.endswith("_max"):
            metric = gate_name[:-4]
            value = _metric_value(report, observed, metric)
            if value is None:
                checks.append(_skipped_gate(metric, "<=", threshold))
                continue
            passed = value <= threshold
            op = "<="
        else:
            continue
        checks.append(
            {
                "metric": metric,
                "observed": value,
                "operator": op,
                "threshold": threshold,
                "passed": passed,
            }
        )
    return {"passed": all(check["passed"] for check in checks if not check.get("skipped")), "checks": checks}


def run_groundedness_evaluation(
    agent: CommerceRAGAgent,
    data_dir: Path,
    *,
    eval_filename: str = "humanlike_blind.jsonl",
    limit: int | None = None,
    offset: int = 0,
    judge: OpenAICompatibleGroundednessJudge | None = None,
) -> dict[str, Any]:
    rows = read_jsonl(data_dir / "eval" / eval_filename)[offset : None if limit is None else offset + limit]
    judge = judge or OpenAICompatibleGroundednessJudge()
    results: list[dict[str, Any]] = []
    for row in rows:
        state = agent.run(row["query"], max_retries=1)
        det = run_deterministic_grounding_checks(
            query=row["query"],
            answer=state.answer,
            citations=state.citations,
            retrieved_contexts=state.retrieved_contexts,
            tool_results=state.tool_results,
            expected=row,
        )
        judge_result = judge.judge(
            query=row["query"],
            answer=state.answer,
            citations=state.citations,
            retrieved_contexts=state.retrieved_contexts,
            tool_results=state.tool_results,
            expected=row,
        )
        expected_action = row.get("expected_action", "answer")
        if expected_action == "clarify":
            final_pass = bool(det.get("deterministic_grounding_pass"))
            business_pass = state.action == "clarify" and final_pass and not judge_result["unsafe_commitment"]
        else:
            final_pass = final_groundedness_pass(det, judge_result)
            business_pass = (
                state.action == expected_action
                and judge_result["answer_relevant"]
                and final_pass
                and det["required_facet_pass"]
                and not judge_result["unsafe_commitment"]
            )
        results.append(
            {
                "query_id": row["query_id"],
                "query": row["query"],
                "intent": row.get("intent", "unknown"),
                "expected_action": expected_action,
                "action": state.action,
                "deterministic": det,
                "judge": judge_result,
                "final_groundedness_pass": final_pass,
                "business_qa_pass": business_pass,
                "answer_preview": state.answer[:240],
                "retrieved_doc_ids": [f"{r.chunk.source}:{r.chunk.doc_id}" for r in state.retrieved_contexts],
            }
        )
    return _summarize_groundedness_rows(results, judge_model=judge.model, eval_filename=eval_filename)


def _metric_value(report: dict[str, Any], observed: dict[str, Any], metric: str) -> float | None:
    if metric in observed:
        return float(observed[metric])
    current: Any = report
    for part in metric.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return float(current)


def _skipped_gate(metric: str, operator: str, threshold: float) -> dict[str, Any]:
    return {
        "metric": metric,
        "observed": None,
        "operator": operator,
        "threshold": threshold,
        "passed": True,
        "skipped": True,
    }


def _citation_leak_rate(state: Any, row: dict[str, Any], citation_contract: dict[str, Any]) -> float:
    if row.get("expected_action") not in {"refuse", "clarify"}:
        return 0.0
    answer_citations = int(citation_contract.get("answer_citation_count", 0))
    state_citations = len(getattr(state, "citations", []) or [])
    tool_citations = len(getattr(state, "tool_citations", []) or [])
    return 1.0 if answer_citations or state_citations or tool_citations else 0.0


def _default_scripted_eval_path(data_dir: Path, eval_filename: str | None) -> Path:
    if eval_filename:
        return data_dir / "eval" / eval_filename
    scripted = data_dir / "eval" / "scripted_regression.jsonl"
    if scripted.exists():
        return scripted
    return data_dir / "eval" / "golden.jsonl"


def _suite_name(eval_path: Path) -> str:
    if eval_path.name == "scripted_regression.jsonl":
        return "scripted_regression"
    if eval_path.name == "humanlike_blind.jsonl":
        return "humanlike_blind"
    if eval_path.name == "challenge.jsonl":
        return "challenge"
    return eval_path.stem


def _legacy_relevant_ids(row: dict[str, Any]) -> list[str]:
    if "relevant_doc_ids" in row:
        return list(row.get("relevant_doc_ids", []))
    required = row.get("required_evidence", {})
    return list(required.get("exact_doc_ids", [])) + list(required.get("acceptable_doc_ids", []))


def _relevance_flags(row: dict[str, Any], results: list[Any], relevant_ids: list[str]) -> list[bool]:
    relevant_set = set(relevant_ids)
    return [_is_relevant_result(row, result, relevant_set) for result in results]


def _relevance_levels(row: dict[str, Any], results: list[Any], relevant_ids: list[str]) -> list[int]:
    required = row.get("required_evidence", {})
    forbidden = row.get("forbidden_evidence", {})
    exact = set(required.get("exact_doc_ids", []))
    acceptable = set(required.get("acceptable_doc_ids", []))
    if not exact and not acceptable:
        exact = set(relevant_ids)
    wrong_products = {str(item) for item in forbidden.get("wrong_product_ids", [])}
    wrong_aspects = {str(item).lower() for item in forbidden.get("wrong_aspects", [])}
    levels: list[int] = []
    for result in results:
        chunk = result.chunk
        full_id = f"{chunk.source}:{chunk.doc_id}"
        product_id = str(chunk.metadata.get("product_id", "")).strip() or str(chunk.doc_id)
        aspects = _metadata_aspects(chunk.metadata)
        if full_id in exact:
            levels.append(RelevanceLevel.EXACT)
        elif full_id in acceptable or _is_relevant_result(row, result, set(relevant_ids)):
            levels.append(RelevanceLevel.ACCEPTABLE)
        elif (product_id and product_id in wrong_products) or (wrong_aspects and aspects & wrong_aspects):
            levels.append(RelevanceLevel.FORBIDDEN)
        else:
            levels.append(RelevanceLevel.WRONG)
    return levels


def _level_recall_at_k(levels: list[int], level: int, k: int) -> float:
    return 1.0 if any(item == level for item in levels[:k]) else 0.0


def _acceptable_recall_at_k(row: dict[str, Any], levels: list[int], k: int) -> float:
    required = row.get("required_evidence", {})
    has_acceptable_target = bool(required.get("acceptable_doc_ids") or required.get("exact_doc_ids"))
    if not has_acceptable_target:
        return 1.0 if any(item >= RelevanceLevel.ACCEPTABLE for item in levels[:k]) else 0.0
    return 1.0 if any(item >= RelevanceLevel.ACCEPTABLE for item in levels[:k]) else 0.0


def _forbidden_rate_at_k(levels: list[int], k: int) -> float:
    if not levels:
        return 0.0
    return round(sum(1 for item in levels[:k] if item == RelevanceLevel.FORBIDDEN) / min(k, len(levels)), 4)


def _entity_accuracy_at_k(row: dict[str, Any], results: list[Any], k: int) -> float:
    product_id = str(row.get("target_entities", {}).get("product_id") or row.get("expected_sql_entities", {}).get("product_id") or "").strip()
    if not product_id:
        return 1.0
    for result in results[:k]:
        chunk_product = str(result.chunk.metadata.get("product_id", "")).strip()
        if chunk_product == product_id or result.chunk.doc_id.endswith(product_id):
            return 1.0
    return 0.0


def _aspect_accuracy_at_k(row: dict[str, Any], results: list[Any], k: int) -> float:
    required_facets = [str(item).lower() for item in row.get("required_evidence", {}).get("required_facets", [])]
    query_aspect = _query_aspect(str(row.get("query", "")))
    if query_aspect:
        required_facets.append(query_aspect)
    required_facets = [item for item in dict.fromkeys(required_facets) if item]
    if not required_facets:
        return 1.0
    for result in results[:k]:
        if _metadata_aspects(result.chunk.metadata) & set(required_facets):
            return 1.0
    return 0.0


def _is_relevant_result(row: dict[str, Any], result: Any, relevant_set: set[str]) -> bool:
    chunk = result.chunk
    full_id = f"{chunk.source}:{chunk.doc_id}"
    if full_id in relevant_set:
        return True
    expected = row.get("expected_sql_entities", {})
    expected_doc_type = str(expected.get("doc_type", ""))
    expected_product_id = str(expected.get("product_id", "")).strip()
    expected_category = str(expected.get("category", "")).strip()
    doc_type = str(chunk.metadata.get("doc_type") or chunk.metadata.get("document_type") or chunk.source)
    product_id = str(chunk.metadata.get("product_id", "")).strip()
    category = str(chunk.metadata.get("category", "")).strip()
    query_rating = _query_rating(str(row.get("query", "")))
    query_aspect = _query_aspect(str(row.get("query", "")))
    aspects = _metadata_aspects(chunk.metadata)

    if expected_doc_type == "review_evidence":
        if doc_type == "review_evidence" and product_id == expected_product_id:
            return query_rating is None or _metadata_int(chunk.metadata, "rating") == query_rating
    if expected_doc_type == "product_profile":
        if product_id == expected_product_id and doc_type in {"product_profile", "review_evidence", "review_aspect_summary"}:
            return True
    if expected_doc_type == "review_aspect_summary":
        if product_id == expected_product_id and query_aspect and query_aspect in aspects:
            return doc_type in {"review_evidence", "review_aspect_summary"}
        if product_id == expected_product_id and doc_type == "product_profile":
            return True
    if expected_doc_type == "faq_case":
        if product_id == expected_product_id and doc_type in {"faq_case", "review_evidence", "review_aspect_summary"}:
            return not query_aspect or doc_type == "faq_case" or query_aspect in aspects
        if chunk.source == "kb":
            return _policy_match(query_aspect, chunk)
    if expected_doc_type == "complaint_cluster":
        if expected_category and category == expected_category and query_aspect:
            return query_aspect in aspects or (doc_type == "complaint_cluster" and query_aspect in chunk.doc_id.lower())
    return False


def _result_signals(
    row: dict[str, Any],
    results: list[Any],
    relevant_ids: list[str],
    relevant_flags: list[bool],
) -> list[dict[str, Any]]:
    expected = row.get("expected_sql_entities", {})
    expected_product_id = str(expected.get("product_id", "")).strip()
    query_aspect = _query_aspect(str(row.get("query", "")))
    relevant_set = set(relevant_ids)
    signals: list[dict[str, Any]] = []
    for rank, result in enumerate(results, start=1):
        chunk = result.chunk
        full_id = f"{chunk.source}:{chunk.doc_id}"
        doc_type = str(chunk.metadata.get("doc_type") or chunk.metadata.get("document_type") or chunk.source)
        product_id = str(chunk.metadata.get("product_id", "")).strip()
        aspects = _metadata_aspects(chunk.metadata)
        result_signals = []
        if result.dense_rank is not None:
            result_signals.append("dense")
        if result.bm25_rank is not None:
            result_signals.append("bm25")
        if result.dense_rank is None and result.bm25_rank is None:
            result_signals.append("forced_fallback")
        if expected_product_id and product_id == expected_product_id:
            result_signals.append("entity_match")
        if query_aspect and query_aspect in aspects:
            result_signals.append("aspect_match")
        if chunk.source == "kb":
            result_signals.append("policy_fallback")
        if (
            "entity_match" in result_signals
            and "aspect_match" in result_signals
            and doc_type in {"review_evidence", "review_aspect_summary", "faq_case"}
        ):
            result_signals.append("sibling_expansion")
        signals.append(
            {
                "rank": rank,
                "doc_id": full_id,
                "doc_type": doc_type,
                "relevant": relevant_flags[rank - 1] if rank - 1 < len(relevant_flags) else full_id in relevant_set,
                "dense_rank": result.dense_rank,
                "bm25_rank": result.bm25_rank,
                "signals": result_signals,
            }
        )
    return signals


def _diagnostic_summary(retrieval_rows: list[dict[str, Any]]) -> dict[str, Any]:
    returned = Counter()
    relevant_hits = Counter()
    by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    for row in retrieval_rows:
        intent = str(row.get("intent", "unknown"))
        for item in row.get("signals", []):
            for signal in item.get("signals", []):
                returned[signal] += 1
                if item.get("relevant"):
                    relevant_hits[signal] += 1
                    by_intent[intent][signal] += 1
    return {
        "returned_signal_counts": dict(sorted(returned.items())),
        "relevant_hit_signal_counts": dict(sorted(relevant_hits.items())),
        "relevant_hit_signals_by_intent": {
            intent: dict(sorted(counter.items())) for intent, counter in sorted(by_intent.items())
        },
    }


def _state_evidence_gaps(state: Any) -> list[str]:
    gaps: list[str] = []
    for event in state.trace:
        if event.get("event") != "grade":
            continue
        for gap in event.get("evidence_gaps", []):
            if gap not in gaps:
                gaps.append(str(gap))
    return gaps


def _agentic_diagnostic_summary(support_rows: list[dict[str, Any]]) -> dict[str, Any]:
    action_counts = Counter(str(row.get("action", "unknown")) for row in support_rows)
    attempt_counts = Counter(str(row.get("attempts", 0)) for row in support_rows)
    gap_counts: Counter[str] = Counter()
    citation_failure_counts: Counter[str] = Counter()
    gaps_by_intent: dict[str, Counter[str]] = defaultdict(Counter)
    retried = 0
    for row in support_rows:
        attempts = int(row.get("attempts", 0))
        if attempts > 1:
            retried += 1
        intent = str(row.get("expected_intent", row.get("intent", "unknown")))
        for gap in row.get("evidence_gaps", []):
            gap_counts[str(gap)] += 1
            gaps_by_intent[intent][str(gap)] += 1
        for failure in row.get("citation_failures", []):
            citation_failure_counts[str(failure)] += 1
    return {
        "action_counts": dict(sorted(action_counts.items())),
        "attempt_counts": dict(sorted(attempt_counts.items())),
        "retry_rate": round(retried / len(support_rows), 4) if support_rows else 0.0,
        "evidence_gap_counts": dict(sorted(gap_counts.items())),
        "citation_failure_counts": dict(sorted(citation_failure_counts.items())),
        "evidence_gaps_by_intent": {
            intent: dict(sorted(counter.items())) for intent, counter in sorted(gaps_by_intent.items())
        },
    }


def _query_aspect(query: str) -> str:
    normalized = query.lower()
    patterns = [
        r"\baround\s+([a-z_]+)\??$",
        r"\bfor\s+([a-z_]+)\s+complaints\??$",
        r"\bthis\s+([a-z_]+)\s+case\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, normalized)
        if match:
            return match.group(1)
    return ""


def _query_rating(query: str) -> int | None:
    match = re.search(r"\brating\s+([1-5])\b", query.lower())
    return int(match.group(1)) if match else None


def _metadata_int(metadata: dict[str, Any], key: str) -> int | None:
    try:
        return int(metadata.get(key, -1))
    except (TypeError, ValueError):
        return None


def _metadata_aspects(metadata: dict[str, Any]) -> set[str]:
    aspects: set[str] = set()
    aspect = str(metadata.get("aspect", "")).lower().strip()
    if aspect:
        aspects.add(aspect)
    raw_aspects = metadata.get("aspects", [])
    if isinstance(raw_aspects, list):
        aspects.update(str(item).lower().strip() for item in raw_aspects if str(item).strip())
    return aspects


def _policy_match(query_aspect: str, chunk: Any) -> bool:
    if not query_aspect:
        return False
    policy_text = " ".join(
        [
            str(chunk.metadata.get("policy_type", "")),
            str(chunk.metadata.get("title", "")),
            str(chunk.metadata.get("filename", "")),
            chunk.text[:240],
        ]
    ).lower()
    wanted = {
        "delivery": {"shipping", "delivery", "carrier", "late_delivery"},
        "refund_return": {"refund", "return", "payment", "subscription"},
        "price_value": {"refund", "return", "payment", "reason_codes"},
        "missing_parts": {"missing", "part", "replacement"},
        "quality_damage": {"damage", "damaged", "defective", "warranty", "return", "missing"},
        "digital_license": {"digital", "license", "payment", "subscription", "delivery"},
        "battery_power": {"warranty", "defective", "return"},
    }.get(query_aspect, set())
    return bool(wanted and any(token in policy_text for token in wanted))


def _average_metrics(rows: list[dict[str, Any]], keys: list[str]) -> dict[str, float]:
    if not rows:
        return {key: 0.0 for key in keys}
    return {key: round(mean(float(row[key]) for row in rows), 4) for key in keys}


def _group_metrics(retrieval_rows: list[dict[str, Any]], support_rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    support_key = "expected_intent" if key == "intent" else key
    groups = sorted(
        {str(row.get(key, "unknown")) for row in retrieval_rows}
        | {str(row.get(support_key, "unknown")) for row in support_rows}
    )
    output: dict[str, Any] = {}
    for group in groups:
        r_rows = [row for row in retrieval_rows if str(row.get(key, "unknown")) == group]
        s_rows = [row for row in support_rows if str(row.get(support_key, "unknown")) == group]
        output[group] = {
            "n": len(r_rows),
            "retrieval": _average_metrics(r_rows, ["precision@5", "recall@5", "mrr", "ndcg@5"]),
        "support_quality": _average_metrics(s_rows, SUPPORT_QUALITY_KEYS),
        }
    return output


def write_eval_report(report_path: Path, report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 评测报告",
        "",
        "本报告由 `python -m commerce_rag_ops.cli eval` 生成。",
        "",
        f"- Suite: {report.get('suite', 'unknown')}",
        f"- Eval path: {report.get('eval_path', 'unknown')}",
        f"- Oracle sources: {report.get('use_oracle_sources', False)}",
        "",
    ]
    if report.get("suite") == "scripted_regression":
        lines.extend(
            [
                "> This is a scripted regression benchmark, not a production generalization benchmark.",
                "",
            ]
        )
    lines.extend(
        [
        "## 摘要",
        "",
        f"- 样本数: {report['n']}",
        f"- 检索后端: {report.get('retrieval_backend', 'local')}",
        f"- 检索模式: {report.get('retrieval_mode', 'hybrid_rerank')}",
        f"- Precision@5: {report['retrieval']['precision@5']}",
        f"- Recall@5: {report['retrieval']['recall@5']}",
        f"- MRR: {report['retrieval']['mrr']}",
        f"- NDCG@5: {report['retrieval']['ndcg@5']}",
        f"- exact_recall@5: {report['retrieval'].get('exact_recall@5', 0.0)}",
        f"- acceptable_recall@5: {report['retrieval'].get('acceptable_recall@5', 0.0)}",
        f"- entity_accuracy@5: {report['retrieval'].get('entity_accuracy@5', 0.0)}",
        f"- aspect_accuracy@5: {report['retrieval'].get('aspect_accuracy@5', 0.0)}",
        f"- forbidden_rate@5: {report['retrieval'].get('forbidden_rate@5', 0.0)}",
        f"- Action accuracy: {report['support_quality'].get('action_accuracy', 0.0)}",
        f"- 引用率: {report['support_quality']['citation_ok']}",
        f"- Citation leak rate(refuse/clarify): {report['support_quality'].get('citation_leak_rate', 0.0)}",
        f"- Citation schema OK: {report['support_quality'].get('citation_schema_ok', 0.0)}",
        f"- Answer citation precision/recall: {report['support_quality'].get('answer_citation_precision', 0.0)} / {report['support_quality'].get('answer_citation_recall', 0.0)}",
        f"- Citation grounded rate: {report['support_quality'].get('citation_grounded_rate', 0.0)}",
        f"- 关键词覆盖率: {report['support_quality']['keyword_coverage']}",
        f"- groundedness 代理指标: {report['support_quality']['groundedness_proxy']}",
        f"- 延迟 p50/p95: {report['latency']['p50_ms']} ms / {report['latency']['p95_ms']} ms",
        ]
    )
    model_config = report.get("model_config", {})
    if model_config:
        lines.extend(
            [
                f"- Embedding 模型: {model_config.get('embedding_model', 'n/a')}",
                f"- Reranker 模型: {model_config.get('reranker_model', 'n/a')}",
                f"- LLM 模型: {model_config.get('llm_model', 'n/a')}",
            ]
        )
    lines.extend(
        [
            "",
            "## 按意图分组",
            "",
            "| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for intent, data in report.get("by_intent", {}).items():
        quality = data["support_quality"]
        lines.append(
            f"| {intent} | {data['n']} | {data['retrieval']['precision@5']} | {data['retrieval']['recall@5']} | {data['retrieval']['mrr']} | {data['retrieval']['ndcg@5']} | {quality['citation_ok']} | {quality.get('citation_schema_ok', 0.0)} | {quality.get('answer_citation_precision', 0.0)} / {quality.get('answer_citation_recall', 0.0)} | {quality['keyword_coverage']} |"
        )
    lines.extend(
        [
            "",
            "## 按难度分组",
            "",
            "| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for difficulty, data in report.get("by_difficulty", {}).items():
        quality = data["support_quality"]
        lines.append(
            f"| {difficulty} | {data['n']} | {data['retrieval']['precision@5']} | {data['retrieval']['recall@5']} | {data['retrieval']['mrr']} | {data['retrieval']['ndcg@5']} | {quality['citation_ok']} | {quality.get('citation_schema_ok', 0.0)} | {quality.get('answer_citation_precision', 0.0)} / {quality.get('answer_citation_recall', 0.0)} | {quality['keyword_coverage']} |"
        )
    lines.extend(
        [
            "",
            "## 检索诊断",
            "",
            "| 信号 | 返回次数 | 命中相关次数 |",
            "|---|---:|---:|",
        ]
    )
    diagnostics = report.get("retrieval_diagnostics", {})
    returned_signals = diagnostics.get("returned_signal_counts", {})
    hit_signals = diagnostics.get("relevant_hit_signal_counts", {})
    for signal in sorted(set(returned_signals) | set(hit_signals)):
        lines.append(f"| {signal} | {returned_signals.get(signal, 0)} | {hit_signals.get(signal, 0)} |")
    lines.extend(
        [
            "",
            "### 按意图统计的相关命中信号",
            "",
            "| 意图 | 信号计数 |",
            "|---|---|",
        ]
    )
    for intent, counts in diagnostics.get("relevant_hit_signals_by_intent", {}).items():
        rendered = ", ".join(f"{signal}: {count}" for signal, count in counts.items())
        lines.append(f"| {intent} | {rendered} |")
    agentic = report.get("agentic_diagnostics", {})
    lines.extend(
        [
            "",
            "## Agentic 证据诊断",
            "",
            f"- 重试率: {agentic.get('retry_rate', 0.0)}",
            "",
            "### 动作与尝试次数",
            "",
            "| 类型 | 计数 |",
            "|---|---|",
            f"| 动作 | {_render_counts(agentic.get('action_counts', {}))} |",
            f"| 尝试次数 | {_render_counts(agentic.get('attempt_counts', {}))} |",
            "",
            "### 证据缺口",
            "",
            "| 缺口 | 次数 |",
            "|---|---:|",
        ]
    )
    gap_counts = agentic.get("evidence_gap_counts", {})
    if gap_counts:
        for gap, count in gap_counts.items():
            lines.append(f"| {gap} | {count} |")
    else:
        lines.append("| none | 0 |")
    lines.extend(
        [
            "",
            "### Citation schema 失败原因",
            "",
            "| 原因 | 次数 |",
            "|---|---:|",
        ]
    )
    citation_failures = agentic.get("citation_failure_counts", {})
    if citation_failures:
        for failure, count in citation_failures.items():
            lines.append(f"| {failure} | {count} |")
    else:
        lines.append("| none | 0 |")
    lines.extend(
        [
            "",
            "### 按意图统计的证据缺口",
            "",
            "| 意图 | 缺口计数 |",
            "|---|---|",
        ]
    )
    gaps_by_intent = agentic.get("evidence_gaps_by_intent", {})
    if gaps_by_intent:
        for intent, counts in gaps_by_intent.items():
            lines.append(f"| {intent} | {_render_counts(counts)} |")
    else:
        lines.append("| none | none |")
    lines.extend(
        [
            "",
            "## 原始 JSON",
            "",
            "```json",
            json.dumps(report, indent=2, ensure_ascii=False),
            "```",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def _render_counts(counts: dict[str, Any]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in counts.items()) if counts else "none"


def _summarize_groundedness_rows(rows: list[dict[str, Any]], *, judge_model: str, eval_filename: str) -> dict[str, Any]:
    n = len(rows)

    def rate(predicate) -> float:
        return round(sum(1 for row in rows if predicate(row)) / n, 4) if n else 0.0

    return {
        "n": n,
        "suite": eval_filename.replace(".jsonl", ""),
        "judge_model": judge_model,
        "business_qa_pass_rate": rate(lambda row: row["business_qa_pass"]),
        "final_groundedness_pass_rate": rate(lambda row: row["final_groundedness_pass"]),
        "claim_support_rate": _avg_claim_support(rows),
        "unsupported_claim_rate": round(mean(float(row["judge"].get("unsupported_claim_rate", 0.0)) for row in rows), 4) if rows else 0.0,
        "citation_schema_pass_rate": rate(lambda row: row["deterministic"]["citation_schema_pass"]),
        "entity_consistency_pass_rate": rate(lambda row: row["deterministic"]["entity_consistency_pass"]),
        "numeric_consistency_pass_rate": rate(lambda row: row["deterministic"]["numeric_consistency_pass"]),
        "policy_consistency_pass_rate": rate(lambda row: row["deterministic"]["policy_consistency_pass"]),
        "forbidden_claim_pass_rate": rate(lambda row: row["deterministic"]["forbidden_claim_pass"]),
        "required_facet_pass_rate": rate(lambda row: row["deterministic"]["required_facet_pass"]),
        "action_accuracy": rate(lambda row: row["action"] == row["expected_action"]),
        "clarify_accuracy": rate(lambda row: row["expected_action"] != "clarify" or row["action"] == "clarify"),
        "citation_leak_rate": rate(
            lambda row: bool(row["deterministic"].get("citation_contract", {}).get("answer_citation_count", 0))
            or bool(row["deterministic"].get("tool_citation_contract", {}).get("answer_tool_citation_count", 0))
            if row["expected_action"] in {"refuse", "clarify"}
            else False
        ),
        "answer_relevance": rate(lambda row: row["judge"]["answer_relevant"]),
        "rows": rows,
    }


def _avg_claim_support(rows: list[dict[str, Any]]) -> float:
    supported = 0
    total = 0
    for row in rows:
        for claim in row["judge"].get("claims", []):
            if not isinstance(claim, dict):
                continue
            total += 1
            if str(claim.get("support", "")).lower() == "supported":
                supported += 1
    return round(supported / total, 4) if total else 0.0


def write_groundedness_report(report_path: Path, report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Humanlike Blind Groundedness Report",
        "",
        "本报告使用真实 OpenAI-compatible judge API，并结合 deterministic grounding checks 评估 answer-level factual support。",
        "",
        "## Summary",
        "",
        f"- n: {report['n']}",
        f"- Judge model: {report['judge_model']}",
        f"- Business QA Pass Rate: {report['business_qa_pass_rate']}",
        f"- final_groundedness_pass_rate: {report['final_groundedness_pass_rate']}",
        f"- claim_support_rate: {report['claim_support_rate']}",
        f"- unsupported_claim_rate: {report['unsupported_claim_rate']}",
        f"- citation_schema_pass_rate: {report['citation_schema_pass_rate']}",
        f"- entity_consistency_pass_rate: {report['entity_consistency_pass_rate']}",
        f"- numeric_consistency_pass_rate: {report['numeric_consistency_pass_rate']}",
        f"- policy_consistency_pass_rate: {report['policy_consistency_pass_rate']}",
        f"- forbidden_claim_pass_rate: {report['forbidden_claim_pass_rate']}",
        f"- required_facet_pass_rate: {report['required_facet_pass_rate']}",
        f"- action_accuracy: {report.get('action_accuracy', 0.0)}",
        f"- clarify_accuracy: {report.get('clarify_accuracy', 0.0)}",
        f"- citation_leak_rate(refuse/clarify): {report.get('citation_leak_rate', 0.0)}",
        "",
        "## Failure Samples",
        "",
        "| Query ID | Query | Failed checks | Unsupported claims | Wrong entities | Missing facets | Retrieved doc ids |",
        "|---|---|---|---|---|---|---|",
    ]
    failures = [row for row in report["rows"] if not row["business_qa_pass"]]
    for row in failures[:30]:
        det = row["deterministic"]
        failed = ", ".join(det.get("errors", [])) or "judge_or_business_rule"
        unsupported = "; ".join(row["judge"].get("unsupported_claims", [])) or "none"
        wrong_entities = ", ".join(det.get("wrong_entities", [])) or "none"
        missing_facets = ", ".join(det.get("missing_facets", [])) or "none"
        retrieved = ", ".join(row.get("retrieved_doc_ids", [])[:8])
        lines.append(
            f"| {row['query_id']} | {row['query']} | {failed} | {unsupported} | {wrong_entities} | {missing_facets} | {retrieved} |"
        )
    if not failures:
        lines.append("| none | none | none | none | none | none | none |")
    lines.extend(["", "## Raw JSON", "", "```json", json.dumps(report, indent=2, ensure_ascii=False), "```", ""])
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_ablation_report(report_path: Path, report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 检索消融报告",
        "",
        "本报告比较 dense-only、BM25-only、hybrid RRF、以及带 rerank 的 hybrid RRF。",
        "",
        "| 模式 | Precision@5 | Recall@5 | MRR | NDCG@5 |",
        "|---|---:|---:|---:|---:|",
    ]
    for mode, data in report["modes"].items():
        summary = data["summary"]
        lines.append(
            f"| {mode} | {summary['precision@5']} | {summary['recall@5']} | {summary['mrr']} | {summary['ndcg@5']} |"
        )
    lines.extend(
        [
            "",
            "## 原始 JSON",
            "",
            "```json",
            json.dumps(report, indent=2, ensure_ascii=False),
            "```",
            "",
        ]
    )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def write_quality_gate_report(report_path: Path, gate_report: dict[str, Any]) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 质量门禁报告",
        "",
        f"总体状态: {'PASS' if gate_report['passed'] else 'FAIL'}",
        "",
        "| 指标 | 观测值 | 门禁 | 状态 |",
        "|---|---:|---:|---|",
    ]
    for check in gate_report["checks"]:
        observed = "SKIP" if check.get("skipped") else check["observed"]
        status = "SKIP" if check.get("skipped") else ("PASS" if check["passed"] else "FAIL")
        lines.append(
            f"| {check['metric']} | {observed} | {check['operator']} {check['threshold']} | {status} |"
        )
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
