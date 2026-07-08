from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Literal

from .evidence_types import EvidencePack


@dataclass
class VerificationResult:
    passed: bool
    action: Literal["answer", "repair", "refuse", "escalate", "ask_user"]
    missing_evidence: list[str] = field(default_factory=list)
    invalid_claims: list[str] = field(default_factory=list)
    citation_errors: list[str] = field(default_factory=list)
    tool_fact_errors: list[str] = field(default_factory=list)
    safety_errors: list[str] = field(default_factory=list)
    repair_hints: list[dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class CriticVerifier:
    def verify(
        self,
        *,
        domain: str,
        evidence_pack: EvidencePack,
        evidence_gaps: list[str],
        citation_validation: dict[str, Any],
        tool_citation_validation: dict[str, Any],
    ) -> VerificationResult:
        citation_errors = list(citation_validation.get("citation_failures", []))
        tool_errors = list(tool_citation_validation.get("tool_citation_failures", []))
        safety_errors = [gap for gap in evidence_gaps if gap in {"safety_boundary", "privacy_violation", "unsafe_commitment", "conflicting_instruction"}]
        missing = list(dict.fromkeys([*evidence_pack.missing_requirements, *evidence_gaps]))
        if safety_errors:
            return VerificationResult(False, "refuse", missing_evidence=missing, citation_errors=citation_errors, tool_fact_errors=tool_errors, safety_errors=safety_errors)
        if citation_errors or tool_errors:
            return VerificationResult(False, "repair", missing_evidence=missing, citation_errors=citation_errors, tool_fact_errors=tool_errors, repair_hints=_repair_hints(missing))
        if missing:
            action = "refuse" if any(gap in {"unknown_intent", "missing_structured_entity", "insufficient_context", "no_context"} for gap in missing) else "repair"
            return VerificationResult(False, action, missing_evidence=missing, repair_hints=_repair_hints(missing))
        return VerificationResult(True, "answer")

    def decide_action(
        self,
        verification: VerificationResult,
        *,
        intent: str,
        risk_level: str,
        citations: list[str],
        grader_scores: dict[str, float],
        weak_retrieval: bool,
        tool_evidence_satisfies: bool,
        attempt: int,
        max_retries: int,
    ) -> str:
        evidence_gaps = verification.missing_evidence
        can_retry = attempt < max_retries
        refusal_gaps = {
            "unknown_intent",
            "safety_boundary",
            "privacy_violation",
            "unsafe_commitment",
            "insufficient_context",
            "conflicting_instruction",
        }
        if set(evidence_gaps) & refusal_gaps:
            return "retry" if can_retry else "refuse"
        critical_gaps = {
            "no_context",
            "unknown_intent",
            "safety_boundary",
            "privacy_violation",
            "unsafe_commitment",
            "insufficient_context",
            "conflicting_instruction",
            "missing_policy",
            "missing_product",
            "missing_review",
            "missing_customer_voice",
            "missing_structured_entity",
        }
        has_critical_gap = bool(set(evidence_gaps) & critical_gaps)
        if intent == "sku_order" and "missing_product_context" in evidence_gaps and can_retry:
            return "retry"
        if verification.action == "repair" and can_retry:
            return "retry"
        if evidence_gaps and can_retry and (has_critical_gap or weak_retrieval):
            return "retry"
        if weak_retrieval:
            return "retry" if can_retry else "refuse"
        if risk_level == "high" and not citations:
            return "escalate"
        if risk_level == "high" and "missing_policy" in evidence_gaps:
            return "escalate"
        if intent == "sku_order" and "missing_structured_entity" in evidence_gaps:
            return "retry" if can_retry else "refuse"
        if intent == "unknown" or "unknown_intent" in evidence_gaps:
            return "retry" if can_retry else "refuse"
        if tool_evidence_satisfies:
            return "answer"
        if verification.passed:
            return "answer"
        if grader_scores.get("relevance_proxy", 0.0) < 0.45:
            return "retry" if can_retry else "refuse"
        if verification.action in {"refuse", "escalate", "ask_user"}:
            return verification.action
        return "answer"


def _repair_hints(missing: list[str]) -> list[dict[str, Any]]:
    hints = []
    if "missing_policy" in missing:
        hints.append({"action_type": "tool_call", "tool_name": "memory.semantic_retrieve", "sources": ["kb"], "query_terms": ["refund", "return", "policy"]})
    if "missing_review" in missing or "missing_customer_voice" in missing:
        hints.append({"action_type": "tool_call", "tool_name": "memory.semantic_retrieve", "sources": ["review", "ticket"], "query_terms": ["review", "complaint", "customer feedback"]})
    if "missing_product_context" in missing:
        hints.append({"action_type": "tool_call", "tool_name": "memory.semantic_retrieve", "sources": ["product", "kb"], "query_terms": ["product profile", "policy"]})
    return hints
