from __future__ import annotations

from dataclasses import asdict, dataclass, field
import re
from typing import Literal

from ..text import normalize_text, tokenize


DomainName = Literal["support", "recommendation", "customer_ops", "order", "refusal"]
HIGH_RISK_TERMS = {"refund", "return", "warranty", "chargeback", "broken", "defective", "compensation"}


@dataclass(frozen=True)
class RouteDecision:
    domain: DomainName
    risk_level: str
    confidence: float
    reasons: list[str] = field(default_factory=list)
    safety_blocks: list[str] = field(default_factory=list)
    legacy_intent: str = "unknown"

    def to_dict(self) -> dict:
        return asdict(self)


class RootRouterAgent:
    """Select the domain agent and preserve safety boundary signals.

    The legacy weighted router can still provide candidate intent signals, but
    root routing now stops at domain selection instead of planning retrieval,
    tools, or final actions.
    """

    def __init__(self, *, known_product_ids: set[str] | None = None, known_order_ids: set[str] | None = None):
        self.known_product_ids = {product_id.lower() for product_id in (known_product_ids or set())}
        self.known_order_ids = {order_id.lower() for order_id in (known_order_ids or set())}

    def decide_intent(self, query: str) -> dict:
        """Weighted deterministic routing signal generator.

        This is the legacy intent-compatible shape, but it now lives inside
        RootRouterAgent so CommerceRAGAgent no longer owns routing signals.
        Root routing still stops at domain/safety selection.
        """
        q = normalize_text(query)
        tokens = set(tokenize(query))
        scores = {
            "support": 0.0,
            "recommendation": 0.0,
            "customer_ops": 0.0,
            "sku_order": 0.0,
            "unknown": 0.0,
        }
        signals: list[dict] = []

        def add(intent: str, weight: float, source: str, reason: str) -> None:
            scores[intent] += weight
            signals.append({"intent": intent, "weight": weight, "source": source, "reason": reason})

        if "stock price" in q or "share price" in q:
            add("unknown", 4.0, "safety_domain", "financial-market/out-of-domain wording")
        for term in [
            "complaint trend",
            "customer ops",
            "pain point",
            "negative reviews",
            "negative review",
            "review trend",
            "trend appears",
            "why customers",
            "review evidence",
            "customer feedback",
            "aspect summary",
            "complaint cluster",
        ]:
            if term in q:
                add("customer_ops", 2.2, "lexical_phrase", term)
        explicit_entity_lookup = bool(self.query_order_ids(query) or self.query_skus(query))
        if explicit_entity_lookup:
            add("sku_order", 4.5, "structured_entity", "explicit order id or sku")
            if tokens & HIGH_RISK_TERMS:
                add("support", 5.5, "structured_support_case", "explicit entity with refund/return/warranty risk")
        for term in ["recommend", "best", "compare", "suggest", "looking for"]:
            if term in q:
                add("recommendation", 2.0, "lexical_phrase", term)
        if "how should support handle" in q or "support handle" in q:
            add("support", 3.0, "support_workflow", "support handle")
        has_order_status = "order" in tokens and (
            tokens & {"status", "delivery", "track", "tracking"} or any(order_id in q for order_id in self.known_order_ids)
        )
        if tokens & {"sku", "stock", "inventory"}:
            add("sku_order", 2.5, "entity_keyword", "sku/stock/inventory")
        if "delivery status" in q or has_order_status:
            add("sku_order", 2.6, "order_status", "order status/tracking")
        if "price" in tokens and "price_value" not in q and "price value" not in q:
            add("sku_order", 1.6, "entity_keyword", "price lookup")
        for term in ["refund", "return", "warranty", "shipping", "delivery", "cancel", "payment"]:
            if term in q:
                add("support", 1.8, "support_keyword", term)
        for term in [
            "privacy",
            "all orders",
            "all customer orders",
            "all customers",
            "every customer",
            "other customers",
            "payment details",
            "card details",
            "system prompt",
            "api key",
        ]:
            if term in q:
                add("unknown", 2.5, "safety_boundary", term)
        if "customer" in tokens and "payment" in tokens:
            add("unknown", 2.5, "safety_boundary", "customer payment data")
        category_hint = category_hint_for_query(query)
        if category_hint:
            add("recommendation", 0.25, "category_hint", category_hint)
            add("support", 0.15, "category_hint", category_hint)
        if not signals:
            add("unknown", 1.0, "default", "no intent signal")

        sorted_scores = dict(sorted((key, round(value, 4)) for key, value in scores.items()))
        selected = max(scores.items(), key=lambda item: (item[1], intent_tiebreaker(item[0])))[0]
        confidence = round(scores[selected] / max(sum(value for value in scores.values() if value > 0), 1.0), 4)
        return {
            "intent": selected,
            "confidence": confidence,
            "scores": sorted_scores,
            "signals": signals,
            "matched_rule": matched_rule(selected, signals),
            "matched_terms": [signal["reason"] for signal in signals if signal["intent"] == selected],
            "priority_order": ["sku_order", "customer_ops", "recommendation", "support", "unknown"],
        }

    def route(self, *, route_decision: dict, risk_level: str) -> RouteDecision:
        legacy_intent = str(route_decision.get("intent", "unknown"))
        signals = route_decision.get("signals", [])
        safety_blocks = [
            str(signal.get("reason"))
            for signal in signals
            if signal.get("source") in {"safety_boundary", "safety_domain"}
        ]
        if safety_blocks or legacy_intent == "unknown":
            domain: DomainName = "refusal"
        elif legacy_intent == "sku_order":
            domain = "order"
        elif legacy_intent == "customer_ops":
            domain = "customer_ops"
        elif legacy_intent == "recommendation":
            domain = "recommendation"
        else:
            domain = "support"
        return RouteDecision(
            domain=domain,
            risk_level=risk_level,
            confidence=float(route_decision.get("confidence", 0.0) or 0.0),
            reasons=[str(item) for item in route_decision.get("matched_terms", [])],
            safety_blocks=safety_blocks,
            legacy_intent=legacy_intent,
        )

    def query_order_ids(self, query: str) -> set[str]:
        return {match.lower() for match in re.findall(r"\bord-[a-z0-9-]+\b", query.lower())}

    def query_skus(self, query: str) -> set[str]:
        order_ids = self.query_order_ids(query)
        candidates = {
            match.lower()
            for match in re.findall(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b", query.lower())
        }
        return {
            candidate
            for candidate in candidates
            if candidate not in self.known_product_ids and candidate not in order_ids and not candidate.startswith("ord-")
        }


def category_hint_for_query(query: str) -> str | None:
    q = normalize_text(query)
    if any(term in q for term in ["beauty", "serum", "skin", "hair", "dryer"]):
        return "All_Beauty"
    if any(term in q for term in ["software", "license", "subscription", "backup", "pdf"]):
        return "Software"
    if any(term in q for term in ["baby", "infant", "nursery", "baby monitor", "baby bottle"]):
        return "Baby_products"
    return None


def matched_rule(intent: str, signals: list[dict]) -> str:
    matching = [signal for signal in signals if signal.get("intent") == intent]
    if not matching:
        return "default"
    strongest = max(matching, key=lambda signal: float(signal.get("weight", 0.0)))
    return f"{strongest.get('source')}:{strongest.get('reason')}"


def intent_tiebreaker(intent: str) -> int:
    priority = {
        "unknown": 0,
        "support": 1,
        "recommendation": 2,
        "customer_ops": 3,
        "sku_order": 4,
    }
    return priority.get(intent, 0)
