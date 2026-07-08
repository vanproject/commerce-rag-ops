from __future__ import annotations

import re
from dataclasses import asdict, dataclass, field
from typing import Any, Literal

from ..text import normalize_text, tokenize


ANAPHORA_TERMS = {
    "it",
    "that",
    "that product",
    "that order",
    "the one",
    "this order",
    "this product",
    "刚才那个",
    "那个",
    "这个订单",
    "这个商品",
}

ORDER_FOLLOWUP_TERMS = {"order", "delivery", "status", "tracking", "refund", "return", "warranty"}
PRODUCT_FOLLOWUP_TERMS = {"complaint", "complaints", "negative", "reviews", "review", "feedback", "issues", "refund", "return", "warranty"}
PRIVACY_TERMS = {"email", "emails", "address", "payment", "card", "phone", "all orders", "every customer", "private notes"}


@dataclass(frozen=True)
class ResolvedEntity:
    entity_type: str
    entity_value: str
    source: str
    confidence: float
    requires_tool_confirmation: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EntityCandidate:
    entity_type: str
    entity_value: str
    source: str
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ContextResolution:
    original_query: str
    is_followup: bool
    referenced_entities: list[ResolvedEntity] = field(default_factory=list)
    ambiguous_entities: list[EntityCandidate] = field(default_factory=list)
    explicit_entities: dict[str, list[str]] = field(default_factory=dict)
    blocked_reasons: list[str] = field(default_factory=list)
    resolution_source: Literal["explicit", "memory", "llm_candidate", "none"] = "none"

    def to_dict(self) -> dict[str, Any]:
        return {
            "original_query": self.original_query,
            "is_followup": self.is_followup,
            "referenced_entities": [asdict(entity) for entity in self.referenced_entities],
            "ambiguous_entities": [asdict(entity) for entity in self.ambiguous_entities],
            "explicit_entities": self.explicit_entities,
            "blocked_reasons": self.blocked_reasons,
            "resolution_source": self.resolution_source,
        }


class ContextResolver:
    def resolve(self, query: str, memory_context: dict[str, Any] | None) -> ContextResolution:
        memory_context = memory_context or {}
        active = dict(memory_context.get("active_entities") or {})
        ambiguous = set(memory_context.get("ambiguous_entity_types") or [])
        q = normalize_text(query)
        explicit = _explicit_entities(query)
        if _has_privacy_signal(q):
            return ContextResolution(
                original_query=query,
                is_followup=False,
                explicit_entities=explicit,
                blocked_reasons=["privacy_boundary"],
                resolution_source="none",
            )
        if explicit:
            return ContextResolution(
                original_query=query,
                is_followup=False,
                explicit_entities=explicit,
                resolution_source="explicit",
            )
        is_followup = _is_followup(q)
        if not is_followup:
            return ContextResolution(original_query=query, is_followup=False, resolution_source="none")

        referenced: list[ResolvedEntity] = []
        ambiguous_entities: list[EntityCandidate] = []
        blocked_reasons: list[str] = []
        for entity_type in sorted(ambiguous):
            if active.get(entity_type):
                ambiguous_entities.append(EntityCandidate(entity_type, str(active[entity_type]), "entity_memory", 0.4))
            blocked_reasons.append(f"ambiguous_{entity_type}_memory")
        if {"product_id", "sku"} & ambiguous:
            blocked_reasons.append("ambiguous_product_memory")

        tokens = set(tokenize(query))
        wants_order = bool(tokens & ORDER_FOLLOWUP_TERMS) or "order" in q or "这个订单" in q
        wants_product = bool(tokens & PRODUCT_FOLLOWUP_TERMS) or any(term in q for term in ["that product", "这个商品", "刚才那个", "it", "that"])

        if wants_order and "order_id" not in ambiguous and active.get("order_id"):
            referenced.append(_resolved("order_id", active["order_id"], 0.92))
            if active.get("sku") and "sku" not in ambiguous:
                referenced.append(_resolved("sku", active["sku"], 0.78))
            if active.get("product_id") and "product_id" not in ambiguous:
                referenced.append(_resolved("product_id", active["product_id"], 0.75))
        elif wants_product and not ({"product_id", "sku"} & ambiguous) and (active.get("product_id") or active.get("sku")):
            if active.get("product_id"):
                referenced.append(_resolved("product_id", active["product_id"], 0.85))
            if active.get("sku"):
                referenced.append(_resolved("sku", active["sku"], 0.82))
            if active.get("category"):
                referenced.append(_resolved("category", active["category"], 0.65, requires_tool_confirmation=False))
        elif active.get("category"):
            referenced.append(_resolved("category", active["category"], 0.55, requires_tool_confirmation=False))

        if not referenced:
            blocked_reasons.append("no_compatible_entity")
        return ContextResolution(
            original_query=query,
            is_followup=is_followup,
            referenced_entities=referenced,
            ambiguous_entities=ambiguous_entities,
            explicit_entities={},
            blocked_reasons=list(dict.fromkeys(blocked_reasons)),
            resolution_source="memory" if referenced else "none",
        )


def _resolved(entity_type: str, value: Any, confidence: float, *, requires_tool_confirmation: bool = True) -> ResolvedEntity:
    return ResolvedEntity(
        entity_type=entity_type,
        entity_value=str(value).strip().upper() if entity_type in {"order_id", "sku", "product_id"} else str(value).strip(),
        source="entity_memory",
        confidence=confidence,
        requires_tool_confirmation=requires_tool_confirmation,
    )


def _explicit_entities(query: str) -> dict[str, list[str]]:
    values: dict[str, list[str]] = {}
    order_ids = sorted({match.upper() for match in re.findall(r"\bord-[a-z0-9-]+\b", query.lower())})
    product_ids = sorted({match.upper() for match in re.findall(r"\bP-[A-Z0-9]+-\d+\b", query.upper())})
    sku_candidates = sorted(
        {
            match.upper()
            for match in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b", query.lower())
            if not match.lower().startswith("ord-") and match.upper() not in product_ids
        }
    )
    if order_ids:
        values["order_id"] = order_ids
    if product_ids:
        values["product_id"] = product_ids
    if sku_candidates:
        values["sku"] = sku_candidates
    return values


def _is_followup(q: str) -> bool:
    return any(term in q for term in ANAPHORA_TERMS) or len(tokenize(q)) <= 7


def _has_privacy_signal(q: str) -> bool:
    return any(term in q for term in PRIVACY_TERMS)
