from __future__ import annotations

import re
from typing import Any

from ..models import AgentState
from ..text import normalize_text, tokenize
from .base import ToolCall


class ToolPlanner:
    def plan(self, query: str, state: AgentState) -> list[ToolCall]:
        q = normalize_text(query)
        calls: list[ToolCall] = []
        order_ids = _query_order_ids(query)
        skus = _query_skus(query)
        product_ids = _query_product_ids(query)
        for entity in state.resolved_entities:
            entity_type = str(entity.get("entity_type", ""))
            value = str(entity.get("entity_value", "")).strip()
            if not value:
                continue
            if entity_type == "order_id":
                order_ids.add(value.lower())
            elif entity_type == "sku":
                skus.add(value.lower())
            elif entity_type == "product_id":
                product_ids.add(value.upper())
        tokens = set(tokenize(query))

        for order_id in sorted(order_ids):
            calls.append(ToolCall("sql.order_by_id", {"order_id": order_id.upper()}, "explicit_order_id"))
            if state.intent in {"sku_order", "support"}:
                calls.append(
                    ToolCall(
                        "sql.order_items_by_order_id",
                        {"order_id": order_id.upper()},
                        "explicit_order_item_context",
                        required=False,
                    )
                )
        for sku in sorted(skus):
            calls.append(ToolCall("sql.product_by_sku", {"sku": sku.upper()}, "explicit_sku"))
            if tokens & {"stock", "inventory", "available", "availability"}:
                calls.append(ToolCall("sql.inventory_by_sku", {"sku": sku.upper()}, "inventory_fact_requested"))
        for product_id in sorted(product_ids):
            calls.append(ToolCall("sql.product_by_id", {"product_id": product_id.upper()}, "explicit_product_id"))

        support_like = state.intent in {"support", "sku_order"} and bool(
            tokens & {"refund", "return", "warranty", "broken", "defective", "leaking", "damaged"}
        )
        if state.intent == "support":
            if not skus and not product_ids:
                calls.append(
                    ToolCall(
                        "sql.product_search",
                        {"query": query, "category": _category_hint(q), "top_k": 4},
                        "support_product_context",
                        required=False,
                    )
                )
            calls.append(ToolCall("ticket.similar_cases", {"query": query, "top_k": 5}, "support_case_context", required=False))
        if support_like:
            for order_id in sorted(order_ids):
                calls.append(
                    ToolCall(
                        "policy.return_eligibility",
                        {"order_id": order_id.upper(), "reason": _return_reason(q)},
                        "support_return_or_warranty_request",
                    )
                )
            for sku in sorted(skus):
                calls.append(
                    ToolCall(
                        "policy.return_eligibility",
                        {"sku": sku.upper(), "reason": _return_reason(q)},
                        "support_return_or_warranty_request",
                        required=False,
                    )
                )
            calls.append(ToolCall("ticket.similar_cases", {"query": query, "top_k": 5}, "support_case_context", required=False))

        if state.intent == "customer_ops":
            product_id = next(iter(product_ids), "")
            if not product_id and not skus:
                calls.append(
                    ToolCall(
                        "sql.product_search",
                        {"query": query, "category": _category_hint(q), "top_k": 4},
                        "customer_ops_product_context",
                        required=False,
                    )
                )
            calls.append(
                ToolCall(
                    "review.aspect_summary",
                    {"product_id": product_id.upper(), "aspect": _aspect(q), "rating_lte": 2},
                    "customer_ops_review_summary",
                    required=False,
                )
            )
            calls.append(
                ToolCall(
                    "ticket.similar_cases",
                    {"query": query, "product_id": product_id.upper(), "top_k": 5},
                    "customer_ops_ticket_context",
                    required=False,
                )
            )

        if state.intent == "recommendation":
            if not skus and not product_ids:
                calls.append(
                    ToolCall(
                        "sql.product_search",
                        {"query": query, "category": _category_hint(q), "top_k": 4},
                        "recommendation_product_search",
                        required=False,
                    )
                )
        if state.intent == "recommendation" and (tokens & {"review", "reviews", "complaint", "negative"}):
            product_id = next(iter(product_ids), "")
            calls.append(
                ToolCall(
                    "review.aspect_summary",
                    {"product_id": product_id.upper(), "aspect": _aspect(q), "rating_lte": 3},
                    "recommendation_review_summary",
                    required=False,
                )
            )

        if state.action == "escalate" or "escalate" in tokens:
            calls.append(ToolCall("ops.escalate_ticket", {"reason": "agent_escalation_candidate"}, "escalation_candidate", required=False))
        if state.intent == "support" and "refund" in tokens and (tokens & {"draft", "request", "form", "ticket", "submit"}):
            calls.append(
                ToolCall(
                    "ops.refund_request_draft",
                    {"reason": _return_reason(q), "summary": query},
                    "refund_request_needs_user_confirmation",
                    required=False,
                )
            )

        return _dedupe_calls(calls)


def _query_order_ids(query: str) -> set[str]:
    return {match.lower() for match in re.findall(r"\bord-[a-z0-9-]+\b", query.lower())}


def _query_skus(query: str) -> set[str]:
    product_ids = _query_product_ids(query)
    order_ids = _query_order_ids(query)
    candidates = {
        match.lower()
        for match in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b", query.lower())
    }
    return {
        candidate
        for candidate in candidates
        if candidate not in product_ids and candidate not in order_ids and not candidate.startswith("ord-")
    }


def _query_product_ids(query: str) -> set[str]:
    return {match.upper() for match in re.findall(r"\bP-[A-Z0-9]+-\d+\b", query.upper())}


def _return_reason(q: str) -> str:
    if any(term in q for term in ["broken", "defective", "damaged", "leaking"]):
        return "defective"
    if "warranty" in q:
        return "warranty"
    return "refund_return"


def _aspect(q: str) -> str:
    for aspect in ["delivery", "shipping", "refund", "quality", "battery", "license", "payment"]:
        if aspect in q:
            return aspect
    return ""


def _category_hint(q: str) -> str:
    if any(term in q for term in ["beauty", "serum", "skin", "hair", "dryer"]):
        return "All_Beauty"
    if any(term in q for term in ["software", "license", "subscription", "backup", "pdf"]):
        return "Software"
    if any(term in q for term in ["baby", "infant", "nursery", "monitor", "bottle"]):
        return "Baby_products"
    return ""


def _dedupe_calls(calls: list[ToolCall]) -> list[ToolCall]:
    seen = set()
    output = []
    for call in calls:
        key = (call.tool_name, tuple(sorted(call.input.items())))
        if key in seen:
            continue
        seen.add(key)
        output.append(call)
    return output
