from __future__ import annotations

import re
from dataclasses import dataclass, field

from .text import tokenize


@dataclass(frozen=True)
class RetrievalPlan:
    intent: str
    entity_need: str
    facets: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)
    must_have: list[str] = field(default_factory=list)
    should_not: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "intent": self.intent,
            "entity_need": self.entity_need,
            "facets": list(self.facets),
            "sources": list(self.sources),
            "must_have": list(self.must_have),
            "should_not": list(self.should_not),
        }


def build_retrieval_plan(query: str, *, intent: str, sources: list[str]) -> RetrievalPlan:
    facets = infer_facets(query)
    must_have = ["product_profile"] if _needs_product_profile(query, intent) else []
    if facets:
        must_have.append("required_facet_evidence")
    if intent == "support":
        must_have.append("policy_or_case_evidence")
    return RetrievalPlan(
        intent=intent,
        entity_need="product" if _needs_product_entity(query, intent) else "optional",
        facets=facets,
        sources=list(dict.fromkeys(sources)),
        must_have=list(dict.fromkeys(must_have)),
        should_not=["policy_only"] if intent in {"recommendation", "customer_ops"} else [],
    )


def infer_facets(query: str) -> list[str]:
    normalized = query.lower()
    tokens = set(tokenize(query))
    facets: list[str] = []
    for facet, keywords in _FACET_KEYWORDS.items():
        if facet in normalized or tokens & keywords:
            facets.append(facet)
    for pattern in [r"\baround\s+([a-z_]+)\??$", r"\bfor\s+([a-z_]+)\s+complaints\??$", r"\bthis\s+([a-z_]+)\s+case\b"]:
        match = re.search(pattern, normalized)
        if match:
            facets.append(match.group(1))
    return list(dict.fromkeys(facets))


def _needs_product_profile(query: str, intent: str) -> bool:
    tokens = set(tokenize(query))
    if intent in {"recommendation", "customer_ops"}:
        return True
    return bool(tokens & {"rating", "reviews", "review", "features", "dimensions", "country", "product"})


def _needs_product_entity(query: str, intent: str) -> bool:
    tokens = set(tokenize(query))
    if intent in {"recommendation", "customer_ops"}:
        return True
    return bool(tokens & {"product", "item", "app", "sku", "rating", "review", "reviews", "complaints", "support"})


_FACET_KEYWORDS = {
    "skin_scent": {"smell", "scent", "fragrance", "skin", "gentle", "sensitive"},
    "quality_damage": {"quality", "damage", "damaged", "defect", "defective", "broken", "leak", "leaking"},
    "digital_license": {"license", "activation", "subscription", "email", "content", "app"},
    "battery_power": {"battery", "charge", "power", "rechargeable"},
    "price_value": {"price", "value", "worth", "deal", "cost"},
    "delivery": {"delivery", "shipping", "arrived", "received", "carrier"},
    "refund_return": {"refund", "return", "money", "cancel"},
    "missing_parts": {"missing", "part", "parts", "accessory", "incomplete"},
    "general_support": {"support", "help", "options", "case"},
}
