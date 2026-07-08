from __future__ import annotations

from typing import Any

from .base import ToolSpec


def register_escalation_tools(registry) -> None:
    def escalate_ticket(payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "created": False,
            "status": "requires_user_confirmation",
            "reason": payload.get("reason"),
            "order_id": payload.get("order_id"),
        }

    def refund_request_draft(payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "created": False,
            "status": "requires_user_confirmation",
            "order_id": payload.get("order_id"),
            "refund_amount": payload.get("refund_amount"),
            "reason": payload.get("reason"),
            "summary": payload.get("summary"),
        }

    registry.register(
        ToolSpec(
            name="ops.escalate_ticket",
            description="Create a human escalation ticket. Write operation; requires confirmation.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=False,
            risk_level="high",
            requires_confirmation=True,
            handler=escalate_ticket,
            allowed_intents=["support"],
            allowed_domains=["support"],
        )
    )
    registry.register(
        ToolSpec(
            name="ops.refund_request_draft",
            description="Draft a refund request for user confirmation. Does not approve or issue money.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=False,
            risk_level="high",
            requires_confirmation=True,
            handler=refund_request_draft,
            allowed_intents=["support"],
            allowed_domains=["support"],
        )
    )
