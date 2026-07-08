from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def load_eval_report_json(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## 原始 JSON\s+```json\s+(.*?)\s+```", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Could not find raw JSON block in {path}")
    return json.loads(match.group(1))


def apply_golden_metadata(normal_report: dict[str, Any], golden_path: Path) -> dict[str, Any]:
    metadata = {}
    for line in golden_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        metadata[row["query_id"]] = row
    for row in normal_report.get("support_rows", []):
        meta = metadata.get(row.get("query_id"))
        if not meta:
            continue
        row["expected_intent"] = meta.get("intent", row.get("expected_intent", "unknown"))
        row["expected_action"] = meta.get("expected_action", row.get("expected_action", "answer"))
        row["safety_category"] = meta.get("safety_category", row.get("safety_category", "normal"))
        row["difficulty"] = meta.get("difficulty", row.get("difficulty", "unknown"))
    for row in normal_report.get("retrieval_rows", []):
        meta = metadata.get(row.get("query_id"))
        if not meta:
            continue
        row["intent"] = meta.get("intent", row.get("intent", "unknown"))
        row["expected_action"] = meta.get("expected_action", row.get("expected_action", "answer"))
        row["safety_category"] = meta.get("safety_category", row.get("safety_category", "normal"))
        row["difficulty"] = meta.get("difficulty", row.get("difficulty", "unknown"))
    return normal_report


def run_combined_evaluation(normal_report: dict[str, Any], refusal_report: dict[str, Any]) -> dict[str, Any]:
    rows = [_normal_row(row) for row in normal_report.get("support_rows", [])]
    rows.extend(_boundary_row(row) for row in refusal_report.get("rows", []))
    return {
        "n": len(rows),
        "normal_n": normal_report.get("n", 0),
        "boundary_n": refusal_report.get("n", 0),
        "pass_rate": _rate(row["passed"] for row in rows),
        "action_match_rate": _rate(row["action"] == row["expected_action"] for row in rows),
        "by_intent": _group(rows, "expected_intent"),
        "by_actual_intent": _group(rows, "actual_intent"),
        "by_expected_action": _group(rows, "expected_action"),
        "by_safety_category": _group(rows, "safety_category"),
        "normal_summary": {
            "retrieval": normal_report.get("retrieval", {}),
            "support_quality": normal_report.get("support_quality", {}),
            "latency": normal_report.get("latency", {}),
        },
        "boundary_summary": {
            "pass_rate": refusal_report.get("pass_rate", 0.0),
            "refusal_rate": refusal_report.get("refusal_rate", 0.0),
            "citation_leak_rate": refusal_report.get("citation_leak_rate", 0.0),
        },
        "rows": rows,
    }


def write_combined_eval_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normal = report["normal_summary"]
    boundary = report["boundary_summary"]
    lines = [
        "# 合并评测报告",
        "",
        "本报告把正常业务问答与边界/拒答问答放到同一张表中观察。正常业务仍使用 `data/eval/golden.jsonl` 的检索与生成指标；边界/拒答仍使用 `data/eval/refusal.jsonl` 的安全通过率。",
        "",
        "## 摘要",
        "",
        f"- 正常业务问答: {report['normal_n']}",
        f"- 边界/拒答问答: {report['boundary_n']}",
        f"- 合并总量: {report['n']}",
        f"- 合并 pass rate: {report['pass_rate']}",
        f"- 动作匹配率: {report['action_match_rate']}",
        "",
        "## 正常业务指标",
        "",
        f"- Precision@5: {normal['retrieval'].get('precision@5', 0.0)}",
        f"- Recall@5: {normal['retrieval'].get('recall@5', 0.0)}",
        f"- MRR: {normal['retrieval'].get('mrr', 0.0)}",
        f"- NDCG@5: {normal['retrieval'].get('ndcg@5', 0.0)}",
        f"- Citation rate: {normal['support_quality'].get('citation_ok', 0.0)}",
        f"- Citation schema OK: {normal['support_quality'].get('citation_schema_ok', 0.0)}",
        f"- Answer citation precision/recall: {normal['support_quality'].get('answer_citation_precision', 0.0)} / {normal['support_quality'].get('answer_citation_recall', 0.0)}",
        f"- Citation grounded rate: {normal['support_quality'].get('citation_grounded_rate', 0.0)}",
        f"- Keyword coverage: {normal['support_quality'].get('keyword_coverage', 0.0)}",
        f"- p50/p95 latency: {normal['latency'].get('p50_ms', 0)} ms / {normal['latency'].get('p95_ms', 0)} ms",
        "",
        "## 边界/拒答指标",
        "",
        f"- Pass rate: {boundary.get('pass_rate', 0.0)}",
        f"- Refusal rate: {boundary.get('refusal_rate', 0.0)}",
        f"- Citation leak rate: {boundary.get('citation_leak_rate', 0.0)}",
        "",
        "## 按 Expected Intent 分组",
        "",
        _group_table(report["by_intent"], "Expected intent"),
        "",
        "## 按 Actual Intent 分组",
        "",
        _group_table(report["by_actual_intent"], "Actual intent"),
        "",
        "## 按 Expected Action 分组",
        "",
        _group_table(report["by_expected_action"], "Expected action"),
        "",
        "## 按 Safety Category 分组",
        "",
        _group_table(report["by_safety_category"], "Safety category"),
        "",
        "## 说明",
        "",
        "- `normal` 表示可回答的业务问题，默认 `expected_action=answer`。",
        "- `refusal` 表示安全边界、未知实体、上下文不足、隐私和越权问题，默认 `expected_action=refuse`。",
        "- `unknown` 只表示真实的未知/域外意图，不再包含缺失 intent 的 seed 标注。",
        "",
        "## 原始 JSON",
        "",
        "```json",
        json.dumps(report, indent=2, ensure_ascii=False),
        "```",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def _normal_row(row: dict[str, Any]) -> dict[str, Any]:
    expected_action = str(row.get("expected_action", "answer"))
    action = str(row.get("action", "unknown"))
    citation_ok = float(row.get("citation_ok", 0.0))
    citation_schema_ok = float(row.get("citation_schema_ok", citation_ok))
    passed = action == expected_action
    if expected_action == "answer":
        passed = passed and citation_schema_ok > 0.0
    return {
        "case_id": row.get("query_id", "unknown"),
        "suite": "normal",
        "safety_category": row.get("safety_category", "normal"),
        "expected_intent": row.get("expected_intent", row.get("intent", "unknown")),
        "actual_intent": row.get("intent", "unknown"),
        "expected_action": expected_action,
        "action": action,
        "passed": passed,
        "citations": int(citation_ok > 0.0),
        "citation_schema_ok": citation_schema_ok,
        "attempts": row.get("attempts", 0),
        "evidence_gaps": row.get("evidence_gaps", []),
    }


def _boundary_row(row: dict[str, Any]) -> dict[str, Any]:
    return {
        "case_id": row.get("case_id", "unknown"),
        "suite": "refusal",
        "safety_category": row.get("category", "unknown"),
        "expected_intent": row.get("expected_intent", "unknown"),
        "actual_intent": row.get("actual_intent", "unknown"),
        "expected_action": row.get("expected_action", "refuse"),
        "action": row.get("action", "unknown"),
        "passed": bool(row.get("passed", False)),
        "citations": row.get("citations", 0),
        "attempts": row.get("attempts", 0),
        "evidence_gaps": row.get("evidence_gaps", []),
    }


def _group(rows: list[dict[str, Any]], key: str) -> dict[str, Any]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[str(row.get(key, "unknown"))].append(row)
    return {name: _group_metrics(values) for name, values in sorted(buckets.items())}


def _group_metrics(rows: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(rows)
    actions = Counter(str(row.get("action", "unknown")) for row in rows)
    suites = Counter(str(row.get("suite", "unknown")) for row in rows)
    return {
        "n": n,
        "pass_rate": _rate(row.get("passed", False) for row in rows),
        "action_match_rate": _rate(row.get("action") == row.get("expected_action") for row in rows),
        "citation_leak_rate": _rate(row.get("expected_action") == "refuse" and int(row.get("citations", 0)) > 0 for row in rows),
        "actions": dict(sorted(actions.items())),
        "suites": dict(sorted(suites.items())),
    }


def _rate(values: Any) -> float:
    items = list(values)
    if not items:
        return 0.0
    return round(sum(1 for item in items if item) / len(items), 4)


def _group_table(groups: dict[str, Any], label: str) -> str:
    lines = [
        f"| {label} | N | Pass rate | Action match | Citation leak | Actions | Suites |",
        "|---|---:|---:|---:|---:|---|---|",
    ]
    for name, data in groups.items():
        lines.append(
            f"| {name} | {data['n']} | {data['pass_rate']} | {data['action_match_rate']} | {data['citation_leak_rate']} | {_render_counts(data['actions'])} | {_render_counts(data['suites'])} |"
        )
    return "\n".join(lines)


def _render_counts(counts: dict[str, Any]) -> str:
    return ", ".join(f"{key}: {value}" for key, value in counts.items()) if counts else "none"
