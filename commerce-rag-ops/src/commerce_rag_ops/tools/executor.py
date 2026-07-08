from __future__ import annotations

import time
from typing import Any

from .base import ToolCall, ToolResult
from .policy import ToolPolicy, redact_tool_output
from .registry import ToolRegistry


class ToolExecutor:
    def __init__(self, registry: ToolRegistry, policy: ToolPolicy | None = None):
        self.registry = registry
        self.policy = policy or ToolPolicy()

    def run(
        self,
        calls: list[ToolCall],
        *,
        query: str,
        intent: str,
        domain: str | None = None,
        risk_level: str = "low",
        action_type: str = "tool_call",
        user_confirmed: bool = False,
    ) -> list[ToolResult]:
        results: list[ToolResult] = []
        for call in calls:
            started = time.perf_counter()
            try:
                spec = self.registry.get(call.tool_name)
                decision = self.policy.check(
                    call,
                    spec,
                    query=query,
                    intent=intent,
                    domain=domain,
                    risk_level=risk_level,
                    action_type=action_type,
                    user_confirmed=user_confirmed,
                )
                if not decision.allowed:
                    results.append(
                        ToolResult(
                            tool_name=call.tool_name,
                            input=call.input,
                            output=_blocked_output(call, decision.reason),
                            found=False,
                            latency_ms=int((time.perf_counter() - started) * 1000),
                            policy_decision=decision.decision,
                            error=None if decision.decision == "requires_confirmation" else decision.reason,
                            evidence_id=_evidence_id(call.tool_name, call.input),
                        )
                    )
                    continue
                output = redact_tool_output(spec.handler(call.input), spec)
                results.append(
                    ToolResult(
                        tool_name=call.tool_name,
                        input=call.input,
                        output=output,
                        found=bool(output.get("found", output.get("created", False))),
                        latency_ms=int((time.perf_counter() - started) * 1000),
                        policy_decision=decision.decision,
                        evidence_id=_evidence_id(call.tool_name, call.input),
                    )
                )
            except Exception as exc:
                results.append(
                    ToolResult(
                        tool_name=call.tool_name,
                        input=call.input,
                        output={},
                        found=False,
                        latency_ms=int((time.perf_counter() - started) * 1000),
                        error=str(exc),
                        policy_decision="error",
                        evidence_id=_evidence_id(call.tool_name, call.input),
                    )
                )
        return results


def normalize_tool_results(results: list[ToolResult], *, backend: str) -> dict[str, Any]:
    products = []
    orders = []
    order_items = []
    inventory = []
    return_eligibility = []
    review_summaries = []
    similar_cases = []
    mentioned_skus = set()
    matched_skus = set()
    mentioned_order_ids = set()
    matched_order_ids = set()
    for result in results:
        output = result.output
        if result.tool_name in {"sql.product_by_sku", "sql.inventory_by_sku"}:
            sku = str(result.input.get("sku", "")).lower()
            if sku:
                mentioned_skus.add(sku)
            if result.found and output.get("sku"):
                matched_skus.add(str(output["sku"]).lower())
        if result.tool_name == "sql.product_by_sku" and result.found:
            products.append(_product_from_output(output))
        elif result.tool_name == "sql.product_by_id" and result.found:
            products.append(_product_from_output(output))
        elif result.tool_name == "sql.product_search" and result.found:
            products.extend(output.get("products", []))
        elif result.tool_name == "sql.inventory_by_sku":
            inventory.append(output)
        elif result.tool_name == "sql.order_by_id":
            order_id = str(result.input.get("order_id", "")).lower()
            if order_id:
                mentioned_order_ids.add(order_id)
            if result.found:
                matched_order_ids.add(str(output.get("order_id", "")).lower())
                orders.append(output)
                if output.get("sku"):
                    matched_skus.add(str(output["sku"]).lower())
        elif result.tool_name == "sql.order_items_by_order_id":
            if result.found:
                order_items.extend(output.get("items", []))
        elif result.tool_name == "policy.return_eligibility":
            return_eligibility.append(output)
        elif result.tool_name == "review.aspect_summary":
            review_summaries.append(output)
        elif result.tool_name == "ticket.similar_cases":
            similar_cases.extend(output.get("cases", []))
    return {
        "backend": backend,
        "products": _dedupe_by(products, "product_id")[:4],
        "orders": _dedupe_by(orders, "order_id")[:4],
        "order_items": order_items[:20],
        "inventory": inventory,
        "return_eligibility": return_eligibility,
        "review_summaries": review_summaries,
        "similar_cases": similar_cases[:5],
        "tool_calls": [result.to_dict() for result in results],
        "mentioned_order_ids": sorted(mentioned_order_ids),
        "missing_order_ids": sorted(mentioned_order_ids - matched_order_ids),
        "mentioned_skus": sorted(mentioned_skus),
        "missing_skus": sorted(mentioned_skus - matched_skus),
    }


def _product_from_output(output: dict[str, Any]) -> dict[str, Any]:
    return {
        key: output.get(key)
        for key in ["product_id", "sku", "title", "category", "price", "stock", "average_rating"]
        if key in output
    }


def _dedupe_by(rows: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    seen = set()
    output = []
    for row in rows:
        value = row.get(key)
        if value in seen:
            continue
        seen.add(value)
        output.append(row)
    return output


def _evidence_id(tool_name: str, inputs: dict[str, Any]) -> str:
    if "sku" in inputs:
        return f"[tool:{tool_name}:{inputs['sku']}]"
    if "order_id" in inputs:
        return f"[tool:{tool_name}:{inputs['order_id']}]"
    if "product_id" in inputs:
        return f"[tool:{tool_name}:{inputs['product_id']}]"
    return f"[tool:{tool_name}]"


def _blocked_output(call: ToolCall, reason: str) -> dict[str, Any]:
    if reason == "write_tool_requires_user_confirmation":
        return {
            "created": False,
            "status": "requires_user_confirmation",
            "reason": call.input.get("reason", reason),
            "order_id": call.input.get("order_id"),
            "summary": call.input.get("summary", ""),
            "confirmation_prompt": "Please confirm before I create or submit this support operation.",
        }
    return {"reason": reason}
