from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .agent import CommerceRAGAgent


def run_tool_evaluation(agent: CommerceRAGAgent, data_dir: Path, *, path: Path | None = None) -> dict[str, Any]:
    cases = _read_jsonl(path or data_dir / "eval" / "tool_golden.jsonl")
    rows = []
    for case in cases:
        state = agent.run(case["query"], max_retries=1)
        tool_calls = [call.get("tool_name") for call in state.tool_results.get("tool_calls", [])]
        found_tools = {
            call.get("tool_name")
            for call in state.tool_results.get("tool_calls", [])
            if call.get("found")
        }
        expected = set(case.get("expected_tools", []))
        forbidden = set(case.get("forbidden_tools", []))
        called = set(tool_calls)
        missing_expected = sorted(expected - called)
        forbidden_called = sorted(forbidden & called)
        must_find_tool = case.get("must_find_tool")
        must_find_ok = True if not must_find_tool else must_find_tool in found_tools
        action_ok = state.action == case.get("expected_action", state.action)
        expected_gap = case.get("expected_gap")
        gap_ok = True
        if expected_gap:
            gap_ok = any(expected_gap in event.get("evidence_gaps", []) for event in state.trace if event.get("event") == "grade")
        tool_citation_ok = True
        if case.get("must_tool_cite"):
            tool_citation_ok = bool(state.tool_citations) and any(citation in state.answer for citation in state.tool_citations)
        write_confirmation_ok = True
        if "ops.escalate_ticket" in called:
            write_confirmation_ok = any(
                call.get("tool_name") == "ops.escalate_ticket" and call.get("policy_decision") == "requires_confirmation"
                for call in state.tool_results.get("tool_calls", [])
            )
        rows.append(
            {
                "case_id": case["case_id"],
                "query": case["query"],
                "expected_tools": sorted(expected),
                "called_tools": tool_calls,
                "missing_expected": missing_expected,
                "forbidden_called": forbidden_called,
                "action": state.action,
                "expected_action": case.get("expected_action"),
                "must_find_ok": must_find_ok,
                "action_ok": action_ok,
                "gap_ok": gap_ok,
                "tool_citation_ok": tool_citation_ok,
                "write_confirmation_ok": write_confirmation_ok,
                "passed": not missing_expected
                and not forbidden_called
                and must_find_ok
                and action_ok
                and gap_ok
                and tool_citation_ok
                and write_confirmation_ok,
            }
        )
    return _summary(rows)


def write_tool_eval_report(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# 工具专项评测报告",
        "",
        f"- 样本数: {report['n']}",
        f"- Tool call precision: {report['tool_call_precision']:.4f}",
        f"- Tool call recall: {report['tool_call_recall']:.4f}",
        f"- Missing required tool rate: {report['missing_required_tool_rate']:.4f}",
        f"- Forbidden tool call rate: {report['forbidden_tool_call_rate']:.4f}",
        f"- Structured fact accuracy: {report['structured_fact_accuracy']:.4f}",
        f"- Tool grounded answer rate: {report['tool_grounded_answer_rate']:.4f}",
        f"- Unknown entity refusal rate: {report['unknown_entity_refusal_rate']:.4f}",
        f"- Write tool confirmation rate: {report['write_tool_confirmation_rate']:.4f}",
        f"- Tool eval pass rate: {report['pass_rate']:.4f}",
        "",
        "| case_id | pass | expected_tools | called_tools | missing | forbidden | action |",
        "|---|---:|---|---|---|---|---|",
    ]
    for row in report["rows"]:
        lines.append(
            "| {case_id} | {passed} | {expected} | {called} | {missing} | {forbidden} | {action} |".format(
                case_id=row["case_id"],
                passed=1 if row["passed"] else 0,
                expected=",".join(row["expected_tools"]),
                called=",".join(row["called_tools"]),
                missing=",".join(row["missing_expected"]),
                forbidden=",".join(row["forbidden_called"]),
                action=row["action"],
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    expected_total = sum(len(row["expected_tools"]) for row in rows)
    expected_hit = sum(len(set(row["expected_tools"]) & set(row["called_tools"])) for row in rows)
    called_total = sum(len(row["called_tools"]) for row in rows)
    expected_called = sum(len([tool for tool in row["called_tools"] if tool in row["expected_tools"]]) for row in rows)
    forbidden_cases = [row for row in rows if row["forbidden_called"]]
    structured_rows = [row for row in rows if row["case_id"] in {"sku_stock_lookup", "order_status_lookup", "refund_eligibility"}]
    unknown_rows = [row for row in rows if row["case_id"] == "unknown_sku_refusal"]
    tool_citation_rows = [row for row in rows if row.get("tool_citation_ok") is not True or row.get("expected_tools")]
    write_rows = [row for row in rows if "ops.escalate_ticket" in row["called_tools"]]
    return {
        "n": len(rows),
        "tool_call_precision": expected_called / called_total if called_total else 1.0,
        "tool_call_recall": expected_hit / expected_total if expected_total else 1.0,
        "missing_required_tool_rate": _rate(bool(row["missing_expected"]) for row in rows),
        "forbidden_tool_call_rate": len(forbidden_cases) / len(rows) if rows else 0.0,
        "structured_fact_accuracy": _rate(row["must_find_ok"] for row in structured_rows),
        "tool_grounded_answer_rate": _rate(row["tool_citation_ok"] for row in tool_citation_rows),
        "unknown_entity_refusal_rate": _rate(row["action"] == "refuse" for row in unknown_rows),
        "write_tool_confirmation_rate": _rate(row["write_confirmation_ok"] for row in write_rows),
        "pass_rate": _rate(row["passed"] for row in rows),
        "rows": rows,
    }


def _rate(values) -> float:
    values = list(values)
    if not values:
        return 1.0
    return sum(1 for value in values if value) / len(values)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
