from __future__ import annotations

from datetime import date
from typing import Any

from ..models import Order, Product
from .base import ToolSpec


def register_policy_tools(registry, *, orders: dict[str, Order], products_by_sku: dict[str, Product]) -> None:
    def return_eligibility(payload: dict[str, Any]) -> dict[str, Any]:
        order_id = str(payload.get("order_id", "")).strip()
        sku = str(payload.get("sku", "")).strip()
        reason = str(payload.get("reason", "unspecified")).strip() or "unspecified"
        order = orders.get(order_id.lower()) if order_id else None
        product = products_by_sku.get(sku.lower()) if sku else None
        if order and not product:
            product = products_by_sku.get(order.sku.lower())
        found = order is not None or product is not None
        high_evidence_reason = reason.lower() in {"defective", "broken", "damaged", "leaking", "warranty"}
        return {
            "found": found,
            "eligible": bool(found),
            "decision": "eligible_for_review" if found else "insufficient_structured_facts",
            "reason_codes": _reason_codes(found, high_evidence_reason),
            "required_evidence": ["proof_of_purchase", "defect_description", "photo_or_video"] if high_evidence_reason else ["proof_of_purchase"],
            "policy_citations": ["doc:kb:KB001_return_refund_policy", "doc:kb:KB003_payment_refund_policy"],
            "order_id": order.order_id if order else order_id,
            "sku": product.sku if product else (order.sku if order else sku),
            "request_date": payload.get("request_date") or date.today().isoformat(),
        }

    registry.register(
        ToolSpec(
            name="policy.return_eligibility",
            description="Combine order/product facts with return policy rules.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="high",
            requires_confirmation=False,
            handler=return_eligibility,
            allowed_intents=["support", "sku_order"],
            allowed_domains=["support"],
        )
    )


def _reason_codes(found: bool, high_evidence_reason: bool) -> list[str]:
    if not found:
        return ["missing_order_or_product"]
    codes = ["within_demo_return_review_scope"]
    if high_evidence_reason:
        codes.append("defect_claim_requires_evidence")
    return codes
