from __future__ import annotations

from collections import Counter
from typing import Any

from ..models import Review
from ..text import tokenize
from .base import ToolSpec


def register_review_tools(registry, *, reviews: list[Review]) -> None:
    def aspect_summary(payload: dict[str, Any]) -> dict[str, Any]:
        product_id = str(payload.get("product_id", "")).strip()
        aspect = str(payload.get("aspect", "")).strip().lower()
        rating_lte = int(payload.get("rating_lte", 2))
        matches = [
            review
            for review in reviews
            if (not product_id or review.product_id == product_id)
            and review.rating <= rating_lte
            and (not aspect or aspect in review.text.lower())
        ]
        complaint_terms = Counter(
            token
            for review in matches
            for token in tokenize(review.text)
            if token not in {"the", "and", "for", "with", "this", "that", "was", "but", "not"}
        )
        return {
            "found": bool(matches),
            "product_id": product_id,
            "aspect": aspect or "general",
            "negative_review_count": len(matches),
            "top_complaints": [term for term, _ in complaint_terms.most_common(5)],
            "sample_review_ids": [review.review_id for review in matches[:5]],
        }

    registry.register(
        ToolSpec(
            name="review.aspect_summary",
            description="Summarize low-rating review signals for a product/aspect.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="low",
            requires_confirmation=False,
            handler=aspect_summary,
            allowed_intents=["customer_ops", "recommendation", "support"],
            allowed_domains=["customer_ops", "recommendation", "support"],
        )
    )
