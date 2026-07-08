from __future__ import annotations

from typing import Any

from ..models import Ticket
from ..text import tokenize
from .base import ToolSpec


def register_ticket_tools(registry, *, tickets: dict[str, Ticket]) -> None:
    def similar_cases(payload: dict[str, Any]) -> dict[str, Any]:
        query = str(payload.get("query", "")).strip()
        product_id = str(payload.get("product_id", "")).strip()
        top_k = int(payload.get("top_k", 5))
        query_tokens = set(tokenize(query))
        scored = []
        for ticket in tickets.values():
            if product_id and ticket.product_id != product_id:
                continue
            text = " ".join([ticket.customer_query, ticket.resolution, ticket.category])
            score = len(query_tokens & set(tokenize(text)))
            if score:
                scored.append((score, ticket))
        scored.sort(key=lambda item: item[0], reverse=True)
        return {
            "found": bool(scored),
            "cases": [
                {
                    "ticket_id": ticket.ticket_id,
                    "customer_query": ticket.customer_query,
                    "resolution": ticket.resolution,
                    "status": ticket.status,
                    "expected_policy_doc": ticket.expected_policy_doc,
                    "product_id": ticket.product_id,
                }
                for _, ticket in scored[:top_k]
            ],
        }

    registry.register(
        ToolSpec(
            name="ticket.similar_cases",
            description="Find similar support cases for a support query.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="medium",
            requires_confirmation=False,
            handler=similar_cases,
            allowed_intents=["support", "customer_ops", "sku_order"],
            allowed_domains=["support", "customer_ops"],
            max_rows=5,
        )
    )
