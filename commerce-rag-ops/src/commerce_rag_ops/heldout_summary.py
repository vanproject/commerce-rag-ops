from __future__ import annotations

import re
from pathlib import Path
from typing import Any


RETRIEVAL_REPORTS = [
    ("humanlike_blind", "humanlike_blind_report.md"),
    ("humanlike_single_turn_resolvable", "humanlike_single_turn_resolvable_report.md"),
    ("humanlike_context_required", "humanlike_context_required_report.md"),
    ("challenge", "challenge_report.md"),
]

STRONG_SMOKE_REPORTS = [
    ("humanlike_single_turn_resolvable", "qdrant+bge+reranker", "humanlike_single_turn_resolvable_qdrant_bge_reranker_report.md"),
    ("challenge", "qdrant+bge+reranker", "challenge_qdrant_bge_reranker_report.md"),
]

GROUNDEDNESS_REPORTS = [
    ("humanlike_blind", "humanlike_blind_groundedness_report.md"),
    ("challenge", "challenge_groundedness_report.md"),
]


def build_frozen_heldout_summary(reports_dir: Path) -> dict[str, Any]:
    retrieval = [_retrieval_row(split, reports_dir / filename) for split, filename in RETRIEVAL_REPORTS]
    strong_smoke = [_retrieval_row(split, reports_dir / filename, profile=profile) for split, profile, filename in STRONG_SMOKE_REPORTS]
    groundedness = [_groundedness_row(split, reports_dir / filename) for split, filename in GROUNDEDNESS_REPORTS]
    refusal = _refusal_row(reports_dir / "refusal_eval_report.md")
    memory = _memory_row(reports_dir / "memory_eval_report.md")
    return {
        "retrieval": retrieval,
        "strong_smoke": strong_smoke,
        "groundedness": groundedness,
        "refusal": refusal,
        "memory": memory,
    }


def write_frozen_heldout_summary(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# Frozen Heldout Eval Summary",
        "",
        "This report summarizes the current frozen/designed heldout artifacts already written under `reports/`.",
        "All referenced eval reports were generated with real `openai-compatible` LLM calls; no template generator is used for heldout results.",
        "",
        "## Retrieval / Support Eval",
        "",
        "| Split | Scope | N | backend | embedding | reranker | llm | exact@5 | acceptable@5 | entity@5 | aspect@5 | forbidden@5 | action_acc | citation_schema | Report |",
        "|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for row in report["retrieval"]:
        lines.append(_retrieval_markdown_row(row))
    lines.extend(
        [
            "",
            "## Strong Retrieval Smoke Matrix",
            "",
            "These rows are smoke runs, not full heldout runs; they are kept separate until the full matrix is regenerated.",
            "",
            "| Split | Profile | Scope | N | backend | embedding | reranker | llm | exact@5 | acceptable@5 | entity@5 | aspect@5 | forbidden@5 | action_acc | citation_schema | Report |",
            "|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in report["strong_smoke"]:
        lines.append(_retrieval_markdown_row(row, include_profile=True))
    lines.extend(
        [
            "",
            "## Answer Groundedness",
            "",
            "| Split | N | Judge model | Business QA Pass | final_groundedness | claim_support | unsupported_claim | citation_schema | required_facet | Report |",
            "|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in report["groundedness"]:
        lines.append(
            f"| {row['split']} | {row['n']} | {row['judge_model']} | {row['business_qa_pass_rate']} | {row['final_groundedness_pass_rate']} | {row['claim_support_rate']} | {row['unsupported_claim_rate']} | {row['citation_schema_pass_rate']} | {row['required_facet_pass_rate']} | `{row['path']}` |"
        )
    refusal = report["refusal"]
    memory = report["memory"]
    lines.extend(
        [
            "",
            "## Safety / Memory",
            "",
            "| Split | N | Key metrics | Report |",
            "|---|---:|---|---|",
            f"| refusal_safety_heldout | {refusal['n']} | pass_rate={refusal['pass_rate']}, refusal_rate={refusal['refusal_rate']}, citation_leak_rate={refusal['citation_leak_rate']} | `{refusal['path']}` |",
            f"| multiturn_memory_heldout | {memory['n']} | carryover={memory['entity_carryover_accuracy']}, wrong_entity_leak={memory['wrong_entity_leak_rate']}, privacy_block={memory['privacy_memory_block_rate']}, success={memory['multi_turn_success_rate']} | `{memory['path']}` |",
            "",
            "## Notes",
            "",
            "- `humanlike_blind` remains in this table for historical comparability; post-repair primary single-turn quality should focus on `humanlike_single_turn_resolvable` and `humanlike_context_required`.",
            "- Strong retrieval rows currently present are smoke runs. Full local/BGE/BGE+reranker/Qdrant matrix regeneration remains open.",
            "- Groundedness rows are older full heldout judge runs and still show the remaining citation/facet/action-contract gap.",
        ]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _retrieval_markdown_row(row: dict[str, Any], *, include_profile: bool = False) -> str:
    prefix = f"| {row['split']} | {row.get('profile', '')} | " if include_profile else f"| {row['split']} | "
    return (
        f"{prefix}{row.get('scope', '')} | {row['n']} | {row['backend']} | {row['embedding_model']} | {row['reranker_model']} | {row['llm_model']} | "
        f"{row['exact_recall@5']} | {row['acceptable_recall@5']} | {row['entity_accuracy@5']} | {row['aspect_accuracy@5']} | "
        f"{row['forbidden_rate@5']} | {row['action_accuracy']} | {row['citation_schema_ok']} | `{row['path']}` |"
    )


def _retrieval_row(split: str, path: Path, *, profile: str = "") -> dict[str, Any]:
    text = _read(path)
    return {
        "split": split,
        "profile": profile,
        "path": _report_path(path),
        "n": _metric(text, "样本数"),
        "scope": _retrieval_scope(split, _metric(text, "样本数")),
        "backend": _metric(text, "检索后端", default="unknown"),
        "embedding_model": _metric(text, "Embedding 模型", default="n/a"),
        "reranker_model": _metric(text, "Reranker 模型", default="n/a"),
        "llm_model": _metric(text, "LLM 模型", default="n/a"),
        "exact_recall@5": _metric(text, "exact_recall@5"),
        "acceptable_recall@5": _metric(text, "acceptable_recall@5"),
        "entity_accuracy@5": _metric(text, "entity_accuracy@5"),
        "aspect_accuracy@5": _metric(text, "aspect_accuracy@5"),
        "forbidden_rate@5": _metric(text, "forbidden_rate@5"),
        "action_accuracy": _metric(text, "Action accuracy", default="n/a"),
        "citation_schema_ok": _metric(text, "Citation schema OK", default="n/a"),
    }


def _groundedness_row(split: str, path: Path) -> dict[str, Any]:
    text = _read(path)
    return {
        "split": split,
        "path": _report_path(path),
        "n": _metric(text, "n"),
        "judge_model": _metric(text, "Judge model", default="unknown"),
        "business_qa_pass_rate": _metric(text, "Business QA Pass Rate"),
        "final_groundedness_pass_rate": _metric(text, "final_groundedness_pass_rate"),
        "claim_support_rate": _metric(text, "claim_support_rate"),
        "unsupported_claim_rate": _metric(text, "unsupported_claim_rate"),
        "citation_schema_pass_rate": _metric(text, "citation_schema_pass_rate"),
        "required_facet_pass_rate": _metric(text, "required_facet_pass_rate"),
    }


def _refusal_row(path: Path) -> dict[str, Any]:
    text = _read(path)
    return {
        "path": _report_path(path),
        "n": _metric(text, "样本数"),
        "pass_rate": _metric(text, "通过率"),
        "refusal_rate": _metric(text, "拒答率"),
        "citation_leak_rate": _metric(text, "引用泄漏率"),
    }


def _memory_row(path: Path) -> dict[str, Any]:
    text = _read(path)
    return {
        "path": _report_path(path),
        "n": _metric(text, "样本数"),
        "entity_carryover_accuracy": _metric(text, "Entity carryover accuracy"),
        "wrong_entity_leak_rate": _metric(text, "Wrong entity leak rate"),
        "privacy_memory_block_rate": _metric(text, "Privacy memory block rate"),
        "multi_turn_success_rate": _metric(text, "Multi-turn success rate"),
    }


def _metric(text: str, label: str, *, default: str = "0.0") -> str:
    pattern = re.compile(rf"^- {re.escape(label)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(text)
    return match.group(1).strip() if match else default


def _read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _report_path(path: Path) -> str:
    return f"reports/{path.name}"


def _retrieval_scope(split: str, n: str) -> str:
    if split == "humanlike_blind":
        return "historical-full"
    try:
        count = int(float(n))
    except ValueError:
        return "unknown"
    return "full" if count >= 100 else "smoke"
