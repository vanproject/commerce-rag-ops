from __future__ import annotations

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from .agent import CommerceRAGAgent
from .conversation_store import ConversationStore
from .entity_memory import EntityResolver, context_resolution_to_legacy_payload, extract_entities_from_state


def run_memory_evaluation(
    agent: CommerceRAGAgent,
    data_dir: Path,
    *,
    path: Path | None = None,
) -> dict[str, Any]:
    cases = _read_jsonl(path or data_dir / "eval" / "multiturn_memory.jsonl")
    rows = []
    with TemporaryDirectory() as temp_dir:
        store = ConversationStore(Path(temp_dir) / "memory_eval.db")
        resolver = EntityResolver()
        for case in cases:
            conversation_id = None
            final_resolution: dict[str, Any] = {}
            final_resolved_query = ""
            for turn_index, query in enumerate(case["turns"], start=1):
                context = store.load_context(conversation_id, user_id=f"eval-{case['case_id']}")
                conversation_id = context["conversation_id"]
                context_resolution = resolver.resolve_context(query, context)
                resolution = context_resolution_to_legacy_payload(query, context_resolution)
                agent_query = query
                final_resolution = resolution
                final_resolved_query = agent_query
                context["original_query"] = query
                context["resolved_query"] = agent_query
                context["entity_resolution"] = resolution
                context["context_resolution"] = context_resolution.to_dict()
                context["resolved_entities"] = resolution.get("used_entities", [])
                state = agent.run(agent_query, max_retries=0, memory_context=context)
                turn_ids = store.append_exchange(
                    conversation_id=conversation_id,
                    user_id=f"eval-{case['case_id']}",
                    original_query=query,
                    resolved_query=agent_query,
                    state=state,
                )
                clear_types = _entity_types_to_clear(resolution)
                store.clear_entities(conversation_id, clear_types)
                store.upsert_entities(conversation_id, extract_entities_from_state(state), turn_id=turn_ids["user_turn_id"])
            active = store.load_context(conversation_id, user_id=f"eval-{case['case_id']}")["active_entities"]
            row = _score_case(case, final_resolved_query, final_resolution, active)
            rows.append(row)
    return _summarize(rows)


def write_memory_eval_report(path: Path, report: dict[str, Any]) -> None:
    lines = [
        "# 多轮记忆评测报告",
        "",
        f"- 样本数: {report['n']}",
        f"- Entity carryover accuracy: {report['entity_carryover_accuracy']:.4f}",
        f"- Wrong entity leak rate: {report['wrong_entity_leak_rate']:.4f}",
        f"- Clarification/block rate when ambiguous: {report['clarification_rate_when_ambiguous']:.4f}",
        f"- Privacy memory block rate: {report['privacy_memory_block_rate']:.4f}",
        f"- Multi-turn success rate: {report['multi_turn_answer_success_rate']:.4f}",
        "",
        "| case_id | pass | agent_query | observed_entities | used_entities | blocked_reasons |",
        "|---|---:|---|---|---|---|",
    ]
    for row in report["rows"]:
        lines.append(
            "| {case_id} | {passed} | {agent_query} | {observed_entities} | {used_entities} | {blocked_reasons} |".format(
                case_id=row["case_id"],
                passed=1 if row["passed"] else 0,
                agent_query=str(row["agent_query"]).replace("|", "\\|"),
                observed_entities=",".join(row["observed_entity_values"]),
                used_entities=",".join(row["used_entity_types"]),
                blocked_reasons=",".join(row["blocked_reasons"]),
            )
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _score_case(
    case: dict[str, Any],
    resolved_query: str,
    resolution: dict[str, Any],
    active_entities: dict[str, Any],
) -> dict[str, Any]:
    used_entity_types = [entity["entity_type"] for entity in resolution.get("used_entities", [])]
    blocked_reasons = resolution.get("blocked_reasons", [])
    observed_values = _observed_entity_values(resolved_query, resolution, active_entities)
    contains_ok = all(_contains_observed(text, observed_values) for text in case.get("expected_resolved_contains", []))
    not_contains_ok = all(not _contains_observed(text, observed_values) for text in case.get("expected_resolved_not_contains", []))
    used_ok = all(entity_type in used_entity_types for entity_type in case.get("expected_used_entity_types", []))
    blocked_ok = all(reason in blocked_reasons for reason in case.get("expected_blocked_reasons", []))
    entity_count_ok = True
    if "expected_entity_count" in case:
        entity_count_ok = len(active_entities) == int(case["expected_entity_count"])
    passed = contains_ok and not_contains_ok and used_ok and blocked_ok and entity_count_ok
    return {
        "case_id": case["case_id"],
        "passed": passed,
        "agent_query": resolved_query,
        "resolved_query": resolved_query,
        "observed_entity_values": observed_values,
        "used_entity_types": used_entity_types,
        "blocked_reasons": blocked_reasons,
        "active_entities": active_entities,
        "contains_ok": contains_ok,
        "not_contains_ok": not_contains_ok,
        "used_ok": used_ok,
        "blocked_ok": blocked_ok,
        "entity_count_ok": entity_count_ok,
    }


def _summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    n = len(rows)
    carryover_rows = [row for row in rows if row["case_id"] in {"order_refund_carryover", "product_complaint_carryover"}]
    wrong_leak_rows = [row for row in rows if row["case_id"] in {"explicit_sku_override", "ambiguous_product_no_carryover"}]
    ambiguous_rows = [row for row in rows if row["case_id"] == "ambiguous_product_no_carryover"]
    privacy_rows = [row for row in rows if row["case_id"] == "privacy_memory_block"]
    return {
        "n": n,
        "entity_carryover_accuracy": _rate(row["used_ok"] and row["contains_ok"] for row in carryover_rows),
        "wrong_entity_leak_rate": 1.0 - _rate(row["not_contains_ok"] for row in wrong_leak_rows),
        "clarification_rate_when_ambiguous": _rate(row["blocked_ok"] for row in ambiguous_rows),
        "privacy_memory_block_rate": _rate(row["blocked_ok"] and row["entity_count_ok"] for row in privacy_rows),
        "multi_turn_answer_success_rate": _rate(row["passed"] for row in rows),
        "rows": rows,
    }


def _entity_types_to_clear(resolution: dict[str, Any]) -> list[str]:
    explicit = resolution.get("explicit_entities", {})
    if explicit.get("order_id"):
        return ["order_id", "sku", "product_id"]
    if explicit.get("sku"):
        return ["sku", "product_id"]
    return []


def _rate(values) -> float:
    values = list(values)
    if not values:
        return 1.0
    return sum(1 for value in values if value) / len(values)


def _observed_entity_values(agent_query: str, resolution: dict[str, Any], active_entities: dict[str, Any]) -> list[str]:
    values = [agent_query]
    for entity in resolution.get("used_entities", []):
        values.append(str(entity.get("entity_value", "")))
    for value_list in resolution.get("explicit_entities", {}).values():
        values.extend(str(value) for value in value_list)
    values.extend(str(value) for value in active_entities.values())
    return [value for value in values if value]


def _contains_observed(expected: str, observed_values: list[str]) -> bool:
    expected_norm = expected.lower()
    return any(expected_norm in value.lower() for value in observed_values)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
