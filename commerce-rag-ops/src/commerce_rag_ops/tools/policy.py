from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .base import ToolCall, ToolSpec


PRIVACY_TERMS = {
    "all orders",
    "every customer",
    "payment details",
    "address",
    "emails",
    "private notes",
    "full database rows",
    "print every customer order",
}

MAX_REFUND_AMOUNT = 100.0


@dataclass(frozen=True)
class ToolPolicyDecision:
    allowed: bool
    decision: str
    reason: str


class ToolPolicy:
    def check(
        self,
        call: ToolCall,
        spec: ToolSpec,
        *,
        query: str,
        intent: str = "",
        domain: str | None = None,
        action_type: str = "tool_call",
        risk_level: str = "low",
        user_confirmed: bool = False,
    ) -> ToolPolicyDecision:
        normalized = query.lower()
        if any(term in normalized for term in PRIVACY_TERMS):
            return ToolPolicyDecision(False, "blocked", "privacy_boundary")
        if action_type != "tool_call":
            return ToolPolicyDecision(False, "blocked", f"unsupported_tool_action:{action_type}")
        if spec.allowed_domains and domain and domain not in spec.allowed_domains:
            return ToolPolicyDecision(False, "blocked", f"domain_not_allowed:{domain}")
        if spec.allowed_intents and not domain and intent not in spec.allowed_intents:
            return ToolPolicyDecision(False, "blocked", f"intent_not_allowed:{intent}")
        if _is_refund_like_write(call.tool_name) and _amount(call.input) > MAX_REFUND_AMOUNT:
            return ToolPolicyDecision(False, "blocked", "refund_amount_exceeds_limit")
        if spec.requires_confirmation and not user_confirmed:
            return ToolPolicyDecision(False, "requires_confirmation", "write_tool_requires_user_confirmation")
        if risk_level == "high" and not spec.read_only and not user_confirmed:
            return ToolPolicyDecision(False, "requires_confirmation", "high_risk_write_requires_user_confirmation")
        return ToolPolicyDecision(True, "allowed", "policy_ok")


def redact_tool_output(output: dict[str, Any], spec: ToolSpec) -> dict[str, Any]:
    redacted = dict(output)
    for field in spec.redact_fields:
        if field in redacted:
            redacted[field] = "[REDACTED]"
    return redacted


def _is_refund_like_write(tool_name: str) -> bool:
    return any(term in tool_name for term in ["refund", "coupon", "credit", "compensation"])


def _amount(payload: dict[str, Any]) -> float:
    for key in ["amount", "refund_amount", "credit_amount", "total"]:
        if key not in payload:
            continue
        try:
            return float(payload.get(key) or 0.0)
        except (TypeError, ValueError):
            continue
    return 0.0
