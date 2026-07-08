from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .agent import CommerceRAGAgent
from .etl import read_jsonl


def run_refusal_evaluation(agent: CommerceRAGAgent, data_dir: Path, *, path: Path | None = None) -> dict[str, Any]:
    rows = read_jsonl(path or data_dir / "eval" / "refusal.jsonl")
    results: list[dict[str, Any]] = []
    for row in rows:
        state = agent.run(row["query"], max_retries=1)
        expected_action = row.get("expected_action", "refuse")
        passed = state.action == expected_action and not state.citations
        results.append(
            {
                "case_id": row["case_id"],
                "category": row.get("category", "unknown"),
                "query": row["query"],
                "expected_action": expected_action,
                "expected_intent": row.get("expected_intent", "unknown"),
                "actual_intent": state.intent,
                "action": state.action,
                "citations": len(state.citations),
                "attempts": state.attempts,
                "evidence_gaps": _state_evidence_gaps(state),
                "passed": passed,
                "answer_preview": state.answer[:180],
            }
        )
    return _summarize(results)


def write_refusal_eval_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Refusal / Unknown 评测报告",
        "",
        "本报告独立评估 unknown、越权、未知实体、上下文不足和不安全承诺场景，不修改 `data/eval/golden.jsonl`。",
        "",
        f"- 样本数: {report['n']}",
        f"- 通过率: {report['pass_rate']}",
        f"- 拒答率: {report['refusal_rate']}",
        f"- 引用泄漏率: {report['citation_leak_rate']}",
        "",
        "## 按类别统计",
        "",
        "| 类别 | N | 通过率 | 拒答率 | 引用泄漏率 |",
        "|---|---:|---:|---:|---:|",
    ]
    for category, item in report["by_category"].items():
        lines.append(
            f"| {category} | {item['n']} | {item['pass_rate']} | {item['refusal_rate']} | {item['citation_leak_rate']} |"
        )
    lines.extend(
        [
            "",
            "## 失败用例",
            "",
            "| Case | Category | Expected | Action | Citations | Intent | Evidence gaps |",
            "|---|---|---|---|---:|---|---|",
        ]
    )
    failures = [row for row in report["rows"] if not row["passed"]]
    if failures:
        for row in failures:
            lines.append(
                f"| {row['case_id']} | {row['category']} | {row['expected_action']} | {row['action']} | {row['citations']} | {row['actual_intent']} | {', '.join(row['evidence_gaps']) or 'none'} |"
            )
    else:
        lines.append("| none | none | none | none | 0 | none | none |")
    lines.extend(["", "## 原始 JSON", "", "```json", json.dumps(report, indent=2, ensure_ascii=False), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def _summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(rows)
    by_category: dict[str, Any] = {}
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        buckets[str(row.get("category", "unknown"))].append(row)
    for category, values in sorted(buckets.items()):
        by_category[category] = _metrics(values)
    return {
        "n": total,
        **_metrics(rows),
        "by_category": by_category,
        "action_counts": dict(sorted(Counter(row["action"] for row in rows).items())),
        "intent_counts": dict(sorted(Counter(row["actual_intent"] for row in rows).items())),
        "rows": rows,
    }


def _metrics(rows: list[dict[str, Any]]) -> dict[str, float | int]:
    if not rows:
        return {"n": 0, "pass_rate": 0.0, "refusal_rate": 0.0, "citation_leak_rate": 0.0}
    n = len(rows)
    return {
        "n": n,
        "pass_rate": round(sum(1 for row in rows if row["passed"]) / n, 4),
        "refusal_rate": round(sum(1 for row in rows if row["action"] == "refuse") / n, 4),
        "citation_leak_rate": round(sum(1 for row in rows if row["citations"] > 0) / n, 4),
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
