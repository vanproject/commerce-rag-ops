from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .etl import read_jsonl, write_jsonl


DEICTIC_PATTERNS = [
    "this item",
    "this product",
    "this app",
    "this baby item",
    "this beauty item",
    "this digital purchase",
    "that item",
    "that product",
    "that app",
    "same product",
]
EXPLICIT_ENTITY_RE = re.compile(
    r"\b(?:sku|order|ord-|model|license|asin|b[0-9a-z]{9}|[a-z]+-[a-z0-9]+-\d+)\b",
    re.IGNORECASE,
)


def is_context_required(row: dict[str, Any]) -> bool:
    """Return True when a blind single-turn query asks about an unbound reference."""

    q = str(row.get("query", "")).lower()
    has_deictic = any(pattern in q for pattern in DEICTIC_PATTERNS) or bool(re.search(r"\b(?:it|that|this)\b", q))
    has_explicit_entity = bool(EXPLICIT_ENTITY_RE.search(q))
    has_product_name_hint = len(q.split()) > 12 and not has_deictic
    return has_deictic and not has_explicit_entity and not has_product_name_hint


def repair_eval_row(row: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    repaired = json.loads(json.dumps(row, ensure_ascii=False))
    changes: list[str] = []
    target_product = str(repaired.get("target_entities", {}).get("product_id") or "").strip()
    forbidden = repaired.setdefault("forbidden_evidence", {})
    wrong_products = [str(item) for item in forbidden.get("wrong_product_ids", [])]
    if target_product and target_product in wrong_products:
        forbidden["wrong_product_ids"] = [item for item in wrong_products if item != target_product]
        changes.append("removed_target_from_wrong_product_ids")
    return repaired, changes


def split_and_repair_humanlike_evalset(
    *,
    data_dir: Path,
    source_filename: str = "humanlike_blind.jsonl",
    resolvable_filename: str = "humanlike_single_turn_resolvable.jsonl",
    context_required_filename: str = "humanlike_context_required.jsonl",
    repair_original: bool = True,
    repair_challenge: bool = True,
) -> dict[str, Any]:
    eval_dir = data_dir / "eval"
    source_path = eval_dir / source_filename
    source_rows = read_jsonl(source_path)
    resolvable_rows: list[dict[str, Any]] = []
    context_required_rows: list[dict[str, Any]] = []
    source_changes: list[dict[str, Any]] = []

    for row in source_rows:
        repaired, changes = repair_eval_row(row)
        if changes:
            source_changes.append({"query_id": row.get("query_id"), "changes": changes})
        if is_context_required(repaired):
            repaired["expected_action"] = "clarify"
            repaired["must_cite"] = False
            repaired.setdefault("answer_checks", {}).setdefault("must_not_claim", [])
            context_required_rows.append(repaired)
        else:
            repaired["expected_action"] = repaired.get("expected_action") or "answer"
            resolvable_rows.append(repaired)

    write_jsonl(eval_dir / resolvable_filename, resolvable_rows)
    write_jsonl(eval_dir / context_required_filename, context_required_rows)
    if repair_original:
        write_jsonl(source_path, resolvable_rows + context_required_rows)

    challenge_changes: list[dict[str, Any]] = []
    challenge_path = eval_dir / "challenge.jsonl"
    if repair_challenge and challenge_path.exists():
        repaired_challenge: list[dict[str, Any]] = []
        for row in read_jsonl(challenge_path):
            repaired, changes = repair_eval_row(row)
            repaired_challenge.append(repaired)
            if changes:
                challenge_changes.append({"query_id": row.get("query_id"), "changes": changes})
        write_jsonl(challenge_path, repaired_challenge)

    report = {
        "source": str(source_path),
        "source_rows": len(source_rows),
        "resolvable_output": str(eval_dir / resolvable_filename),
        "resolvable_rows": len(resolvable_rows),
        "context_required_output": str(eval_dir / context_required_filename),
        "context_required_rows": len(context_required_rows),
        "source_repairs": source_changes,
        "challenge_repairs": challenge_changes,
        "repair_original": repair_original,
    }
    return report


def write_eval_repair_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Eval Fairness Repair Report",
        "",
        "本报告由 `python -m commerce_rag_ops.cli repair-evalsets` 生成。",
        "",
        f"- Source rows: {report['source_rows']}",
        f"- Resolvable rows: {report['resolvable_rows']}",
        f"- Context-required rows: {report['context_required_rows']}",
        f"- Source repairs: {len(report['source_repairs'])}",
        f"- Challenge repairs: {len(report['challenge_repairs'])}",
        f"- Resolvable output: `{report['resolvable_output']}`",
        f"- Context-required output: `{report['context_required_output']}`",
        "",
        "## Forbidden Evidence Repairs",
        "",
    ]
    repairs = list(report.get("source_repairs", [])) + list(report.get("challenge_repairs", []))
    if not repairs:
        lines.append("No target-product leakage found in `wrong_product_ids`.")
    else:
        lines.append("| query_id | changes |")
        lines.append("| --- | --- |")
        for item in repairs:
            lines.append(f"| {item.get('query_id')} | {', '.join(item.get('changes', []))} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
