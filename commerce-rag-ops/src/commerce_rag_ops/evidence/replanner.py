from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..runtime import AgentStep
from .critic import VerificationResult


@dataclass(frozen=True)
class RepairPlan:
    reason: str
    steps: list[AgentStep] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "reason": self.reason,
            "steps": [
                {
                    "action_type": step.action_type,
                    "tool_name": step.tool_name,
                    "tool_input": step.tool_input,
                    "reason_summary": step.reason_summary,
                    "expected_evidence": step.expected_evidence,
                }
                for step in self.steps
            ],
        }


class Replanner:
    def replan(self, verification: VerificationResult, *, query: str, domain: str) -> RepairPlan:
        missing = set(verification.missing_evidence)
        steps: list[AgentStep] = []
        if "missing_policy" in missing:
            steps.append(
                AgentStep(
                    "tool_call",
                    tool_name="memory.semantic_retrieve",
                    tool_input={"query": f"{query} refund return defective policy", "sources": ["kb"], "top_k": 5},
                    reason_summary="repair missing policy evidence",
                    expected_evidence=["policy"],
                )
            )
        if missing & {"missing_review", "missing_customer_voice"}:
            steps.append(
                AgentStep(
                    "tool_call",
                    tool_name="memory.semantic_retrieve",
                    tool_input={"query": f"{query} verified review complaint customer feedback", "sources": ["review", "ticket"], "top_k": 5},
                    reason_summary="repair missing customer voice evidence",
                    expected_evidence=["review", "ticket"],
                )
            )
        if "missing_product_context" in missing:
            steps.append(
                AgentStep(
                    "tool_call",
                    tool_name="memory.semantic_retrieve",
                    tool_input={"query": f"{query} product profile policy", "sources": ["product", "kb"], "top_k": 5},
                    reason_summary="repair missing product context",
                    expected_evidence=["product"],
                )
            )
        if not steps and verification.action == "ask_user":
            steps.append(AgentStep("ask_user", reason_summary="critic requires user clarification"))
        return RepairPlan(reason=";".join(sorted(missing)) or f"{domain}_verification_failed", steps=steps)
