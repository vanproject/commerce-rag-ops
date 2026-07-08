from __future__ import annotations

import re
from typing import Any

from .memory import ContextResolver
from .models import AgentState
from .text import normalize_text, tokenize


PII_PATTERNS = [
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"),
    re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
]

PRIVACY_TERMS = {"email", "emails", "payment", "card", "phone", "all orders", "every customer", "private notes"}
SENSITIVE_ALWAYS_TERMS = {"bank account", "card number", "credit card", "payment method"}
ADDRESS_TERMS = {"billing address", "shipping address"}
SENSITIVE_RECALL_VERBS = {"gave", "provided", "remember", "remind", "save", "tell me", "what is", "what was"}

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

PRODUCT_FOLLOWUP_TERMS = {
    "complaint",
    "complaints",
    "negative",
    "reviews",
    "review",
    "feedback",
    "issues",
    "refundable",
    "refund",
    "warranty",
    "return",
}

ORDER_FOLLOWUP_TERMS = {"order", "delivery", "status", "tracking", "refund", "return", "warranty"}


class EntityResolver:
    def resolve_context(self, query: str, memory_context: dict[str, Any] | None) -> ContextResolution:
        return ContextResolver().resolve(query, memory_context)

    def resolve(self, query: str, memory_context: dict[str, Any] | None) -> tuple[str, dict[str, Any]]:
        resolution = self.resolve_context(query, memory_context)
        return query, context_resolution_to_legacy_payload(query, resolution)


def context_resolution_to_legacy_payload(query: str, resolution: ContextResolution) -> dict[str, Any]:
    payload = resolution.to_dict()
    used_entities = [
        {
            "entity_type": entity["entity_type"],
            "entity_value": entity["entity_value"],
            "source": entity["source"],
            "confidence": entity["confidence"],
            "requires_tool_confirmation": entity["requires_tool_confirmation"],
        }
        for entity in payload["referenced_entities"]
    ]
    rule = {
        "explicit": "explicit_entity_wins",
        "memory": "followup_entity_reference",
        "none": "no_safe_carryover" if resolution.is_followup else "no_followup_signal",
        "llm_candidate": "llm_candidate_reference",
    }.get(payload["resolution_source"], "no_followup_signal")
    return {
        "used_entities": used_entities,
        "explicit_entities": payload["explicit_entities"],
        "blocked_reasons": payload["blocked_reasons"],
        "resolved_query": query,
        "context_resolution": payload,
        "rule": rule,
    }


def entity_types_to_clear(resolution: dict[str, Any]) -> list[str]:
    blocked_reasons = set(resolution.get("blocked_reasons", []))
    if "privacy_boundary" in blocked_reasons:
        return ["order_id", "sku", "product_id", "category", "support_topic"]
    explicit = resolution.get("explicit_entities", {})
    if explicit.get("order_id"):
        return ["order_id", "sku", "product_id"]
    if explicit.get("sku"):
        return ["sku", "product_id"]
    return []


def extract_entities_from_state(state: AgentState) -> list[dict[str, Any]]:
    entities: list[dict[str, Any]] = []
    if _has_pii(state.original_query or state.query):
        return []
    for order_id in _query_order_ids(state.query):
        entities.append(_entity("order_id", order_id.upper(), "query", 0.85))
    for sku in _query_skus(state.query):
        entities.append(_entity("sku", sku.upper(), "query", 0.75))
    for product in state.tool_results.get("products", []):
        product_id = str(product.get("product_id", "")).strip()
        sku = str(product.get("sku", "")).strip()
        category = str(product.get("category", "") or product.get("metadata", {}).get("category", "")).strip()
        if product_id:
            entities.append(_entity("product_id", product_id, "tool_results", 0.95, metadata={"sku": sku}))
        if sku:
            entities.append(_entity("sku", sku, "tool_results", 0.95, metadata={"product_id": product_id}))
        if category:
            entities.append(_entity("category", category, "tool_results", 0.8))
    for order in state.tool_results.get("orders", []):
        order_id = str(order.get("order_id", "")).strip()
        sku = str(order.get("sku", "")).strip()
        product_id = str(order.get("product_id", "")).strip()
        if order_id:
            entities.append(_entity("order_id", order_id, "tool_results", 0.98, metadata={"sku": sku, "product_id": product_id}))
        if sku:
            entities.append(_entity("sku", sku, "tool_results", 0.92, metadata={"order_id": order_id, "product_id": product_id}))
        if product_id:
            entities.append(_entity("product_id", product_id, "tool_results", 0.9, metadata={"order_id": order_id, "sku": sku}))
    for result in state.retrieved_contexts[:4]:
        product_id = str(result.chunk.metadata.get("product_id", "")).strip()
        category = str(result.chunk.metadata.get("category", "")).strip()
        sku = str(result.chunk.metadata.get("sku", "")).strip()
        if product_id:
            entities.append(_entity("product_id", product_id, "retrieved_context", 0.55, metadata={"doc_id": result.chunk.doc_id}))
        if sku:
            entities.append(_entity("sku", sku, "retrieved_context", 0.55, metadata={"doc_id": result.chunk.doc_id}))
        if category:
            entities.append(_entity("category", category, "retrieved_context", 0.45))
    topic = _support_topic(state.query)
    if topic:
        entities.append(_entity("support_topic", topic, "query", 0.65))
    return _dedupe_entities(entities)


def _explicit_entities(query: str) -> dict[str, list[str]]:
    values = {}
    order_ids = sorted(_query_order_ids(query))
    skus = sorted(_query_skus(query))
    if order_ids:
        values["order_id"] = [value.upper() for value in order_ids]
    if skus:
        values["sku"] = [value.upper() for value in skus]
    return values


def _query_order_ids(query: str) -> set[str]:
    return {match.lower() for match in re.findall(r"\bord-[a-z0-9-]+\b", query.lower())}


def _query_skus(query: str) -> set[str]:
    order_ids = _query_order_ids(query)
    candidates = {
        match.lower()
        for match in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b", query.lower())
    }
    return {
        candidate
        for candidate in candidates
        if candidate not in order_ids and not candidate.startswith("ord-") and _looks_like_business_sku(candidate)
    }


def _support_topic(query: str) -> str | None:
    q = normalize_text(query)
    topic_terms = {
        "refund_return": ["refund", "return", "money back"],
        "warranty": ["warranty", "defective"],
        "shipping_delivery": ["shipping", "delivery", "tracking"],
        "payment": ["payment", "chargeback", "card"],
    }
    for topic, terms in topic_terms.items():
        if any(term in q for term in terms):
            return topic
    return None


def _is_followup(q: str) -> bool:
    return any(term in q for term in ANAPHORA_TERMS) or len(tokenize(q)) <= 7


def _has_privacy_signal(q: str) -> bool:
    if any(term in q for term in SENSITIVE_ALWAYS_TERMS):
        return True
    if any(term in q for term in ADDRESS_TERMS) and any(verb in q for verb in SENSITIVE_RECALL_VERBS):
        return True
    return any(term in q for term in PRIVACY_TERMS)


def _has_pii(text: str) -> bool:
    q = normalize_text(text)
    return _has_privacy_signal(q) or any(pattern.search(text) for pattern in PII_PATTERNS)


def _looks_like_business_sku(value: str) -> bool:
    parts = value.lower().split("-")
    if any(part.isdigit() for part in parts):
        return True
    if len(parts) >= 3:
        return True
    prefixes = {"baby", "beauty", "soft"}
    return parts[0] in prefixes


def _entity(entity_type: str, value: str, source: str, confidence: float, *, metadata: dict[str, Any] | None = None) -> dict[str, Any]:
    return {
        "entity_type": entity_type,
        "entity_value": value,
        "normalized_value": _normalize_entity_value(entity_type, value),
        "source": source,
        "confidence": confidence,
        "metadata": metadata or {},
    }


def _used(entity_type: str, value: str, source: str) -> dict[str, Any]:
    return {"entity_type": entity_type, "entity_value": value, "source": source}


def _normalize_entity_value(entity_type: str, value: str) -> str:
    if entity_type in {"sku", "order_id", "product_id", "category", "support_topic"}:
        return value.strip().upper()
    return normalize_text(value)


def _dedupe_entities(entities: list[dict[str, Any]]) -> list[dict[str, Any]]:
    best: dict[tuple[str, str], dict[str, Any]] = {}
    for entity in entities:
        key = (entity["entity_type"], entity["normalized_value"])
        if key not in best or float(entity.get("confidence", 0.0)) > float(best[key].get("confidence", 0.0)):
            best[key] = entity
    return list(best.values())
