from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .state import RunState
from .step import AgentStep, AgentStepRecord, Observation


StepExecutor = Callable[[AgentStep, RunState], Observation]


@dataclass(frozen=True)
class LoopResult:
    executed_steps: int
    blocked_steps: int
    terminal: bool = False


class AgentLoop:
    def __init__(self, *, max_steps: int = 6, max_tool_calls: int = 5, max_retrieval_calls: int = 2):
        self.max_steps = max_steps
        self.max_tool_calls = max_tool_calls
        self.max_retrieval_calls = max_retrieval_calls

    def run_agent(self, state: RunState, *, agent: object, execute_step: StepExecutor) -> LoopResult:
        state.budgets.max_steps = self.max_steps
        state.budgets.max_tool_calls = self.max_tool_calls
        state.budgets.max_retrieval_calls = self.max_retrieval_calls
        executed = 0
        blocked = 0
        while state.budgets.remaining():
            step = agent.next_step(state)
            if step.action_type == "final_answer":
                break
            if not state.budgets.remaining():
                blocked += 1
                state.steps.append(AgentStepRecord(step=step, status="blocked", rejected_reason="step_budget_exhausted"))
                break
            budget_block = self._budget_block_reason(state, step)
            if budget_block:
                blocked += 1
                state.steps.append(AgentStepRecord(step=step, status="blocked", rejected_reason=budget_block))
                state.observations.append(
                    Observation(
                        source=step.tool_name or step.action_type,
                        kind="system",
                        status="blocked",
                        payload={"reason": budget_block, "step": _step_payload(step)},
                    )
                )
                continue
            state.budgets.steps_used += 1
            self._consume_action_budget(state, step)
            record = AgentStepRecord(step=step, status="running")
            state.steps.append(record)
            observation = execute_step(step, state)
            state.observations.append(observation)
            record.status = observation.status
            record.observation_id = f"obs-{len(state.observations)}"
            executed += 1
            if step.action_type in {"final_answer", "refuse", "ask_user", "escalate"}:
                state.final_action = step.action_type
                return LoopResult(executed, blocked, terminal=True)
        return LoopResult(executed, blocked, terminal=bool(state.final_action))

    def _budget_block_reason(self, state: RunState, step: AgentStep) -> str:
        if step.tool_name == "memory.semantic_retrieve":
            if state.budgets.retrieval_calls_used >= state.budgets.max_retrieval_calls:
                return "retrieval_budget_exhausted"
            return ""
        if step.action_type == "tool_call":
            if _is_write_draft_step(step):
                if state.budgets.write_tool_drafts_used >= state.budgets.max_write_tool_drafts:
                    return "write_tool_draft_budget_exhausted"
                return ""
            if state.budgets.tool_calls_used >= state.budgets.max_tool_calls:
                return "tool_budget_exhausted"
        return ""

    def _consume_action_budget(self, state: RunState, step: AgentStep) -> None:
        if step.tool_name == "memory.semantic_retrieve":
            state.budgets.retrieval_calls_used += 1
        elif _is_write_draft_step(step):
            state.budgets.write_tool_drafts_used += 1
        elif step.action_type == "tool_call":
            state.budgets.tool_calls_used += 1


def _step_payload(step: AgentStep) -> dict:
    return {
        "action_type": step.action_type,
        "tool_name": step.tool_name,
        "tool_input": step.tool_input,
        "reason_summary": step.reason_summary,
        "expected_evidence": step.expected_evidence,
    }


def _is_write_draft_step(step: AgentStep) -> bool:
    return bool(step.tool_name and step.tool_name.startswith("ops."))
