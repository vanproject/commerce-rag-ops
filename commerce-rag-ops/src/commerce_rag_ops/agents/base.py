from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..models import AgentState
from ..runtime import AgentStep, RunState


@dataclass(frozen=True)
class EvidenceContract:
    required: list[str] = field(default_factory=list)
    preferred: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class DomainPlan:
    goal: str
    actions: list[str]
    steps: list[AgentStep]
    memory_request: dict[str, Any] = field(default_factory=dict)
    skip_memory_reason: str = ""
    risk_notes: list[str] = field(default_factory=list)

    def to_agent_plan(self, *, source: str) -> dict[str, Any]:
        return {
            "source": source,
            "used": False,
            "goal": self.goal,
            "actions": self.actions,
            "steps": [
                {
                    "action": _plan_action(step),
                    "tool_name": step.tool_name,
                    "proposed_by": source,
                    "accepted": True,
                    "rejected_reason": "",
                    "reason_summary": step.reason_summary,
                }
                for step in self.steps
            ],
            "tool_calls": [
                {
                    "tool_name": step.tool_name,
                    "input": step.tool_input,
                    "reason": step.reason_summary,
                    "required": True,
                }
                for step in self.steps
                if step.action_type == "tool_call" and step.tool_name
            ],
            "memory_request": self.memory_request,
            "skip_memory_reason": self.skip_memory_reason,
            "risk_notes": self.risk_notes,
        }


class DomainAgent:
    name = "base"
    allowed_tools: list[str] = []
    evidence_contract = EvidenceContract()

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        raise NotImplementedError

    def next_step(self, state: RunState) -> AgentStep:
        context = state.context if isinstance(state.context, dict) else {}
        attempted = {_step_key(record.step) for record in state.steps}
        for raw in context.get("action_suggestions", []):
            step = _coerce_step(raw)
            if not step.accepted:
                continue
            if not step.tool_name or step.tool_name not in self.allowed_tools:
                continue
            if _step_key(step) in attempted:
                continue
            return step
        memory_step = _semantic_memory_step(context.get("semantic_memory_request"))
        if memory_step and memory_step.tool_name in self.allowed_tools and _step_key(memory_step) not in attempted:
            return memory_step
        terminal_step = _terminal_step_from_plan(context.get("agent_plan"))
        if terminal_step and _step_key(terminal_step) not in attempted:
            return terminal_step
        return AgentStep("final_answer", reason_summary="domain agent has no remaining useful action")


def _plan_action(step: AgentStep) -> str:
    if step.tool_name == "memory.semantic_retrieve":
        return "retrieve_memory"
    if step.action_type == "tool_call":
        return "call_tools"
    if step.action_type == "ask_user":
        return "ask_user"
    if step.action_type in {"refuse", "escalate", "final_answer"}:
        return "decide_action"
    return step.action_type


def _coerce_step(raw: Any) -> AgentStep:
    if isinstance(raw, AgentStep):
        return raw
    if isinstance(raw, dict):
        return AgentStep(
            action_type=raw.get("action_type", "final_answer"),
            tool_name=raw.get("tool_name"),
            tool_input=dict(raw.get("tool_input", {})),
            reason_summary=str(raw.get("reason_summary", "")),
            expected_evidence=list(raw.get("expected_evidence", [])),
            proposed_by=str(raw.get("proposed_by", "runtime_context")),
            accepted=bool(raw.get("accepted", True)),
            rejected_reason=str(raw.get("rejected_reason", "")),
        )
    return AgentStep("final_answer", reason_summary="invalid action suggestion")


def _semantic_memory_step(raw_request: Any) -> AgentStep | None:
    if not isinstance(raw_request, dict) or not raw_request:
        return None
    return AgentStep(
        "tool_call",
        tool_name="memory.semantic_retrieve",
        tool_input=dict(raw_request),
        reason_summary=str(raw_request.get("reason") or "semantic memory requested by domain agent"),
        expected_evidence=list(raw_request.get("expected_evidence", [])),
        proposed_by=str(raw_request.get("proposed_by", "agent_plan")),
    )


def _terminal_step_from_plan(raw_plan: Any) -> AgentStep | None:
    if not isinstance(raw_plan, dict):
        return None
    actions = [str(action) for action in raw_plan.get("actions", [])]
    if "ask_user" in actions:
        return AgentStep("ask_user", reason_summary=str(raw_plan.get("ask_user_reason") or raw_plan.get("goal") or "agent plan asks user"), proposed_by=str(raw_plan.get("selected_by", "agent_plan")))
    if "direct_answer" in actions:
        return AgentStep("final_answer", reason_summary=str(raw_plan.get("goal") or "agent plan can answer directly"), proposed_by=str(raw_plan.get("selected_by", "agent_plan")))
    if actions == ["decide_action"] or ("refuse" in actions):
        return AgentStep("refuse", reason_summary=str(raw_plan.get("skip_memory_reason") or raw_plan.get("goal") or "agent plan refuses"), proposed_by=str(raw_plan.get("selected_by", "agent_plan")))
    return None


def _step_key(step: AgentStep) -> tuple[str, str | None, tuple[tuple[str, str], ...]]:
    return (
        step.action_type,
        step.tool_name,
        tuple(sorted((str(key), str(value)) for key, value in step.tool_input.items())),
    )
