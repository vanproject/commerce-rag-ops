from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from ..models import AgentState
from .base import ToolCall
from .planner import ToolPlanner


@dataclass(frozen=True)
class ActionCandidate:
    action_type: str
    tool_name: str | None = None
    tool_input: dict[str, Any] | None = None
    reason: str = ""
    required: bool = True
    proposed_by: str = "heuristic_tool_suggester"

    def to_tool_call(self) -> ToolCall | None:
        if self.action_type != "tool_call" or not self.tool_name:
            return None
        return ToolCall(
            self.tool_name,
            dict(self.tool_input or {}),
            self.reason or "heuristic_tool_suggester",
            required=self.required,
        )


class ToolSuggester:
    def __init__(self):
        self._legacy_planner = ToolPlanner()

    def suggest(self, query: str, state: AgentState, *, domain: str) -> list[ActionCandidate]:
        return [
            ActionCandidate(
                action_type="tool_call",
                tool_name=call.tool_name,
                tool_input=call.input,
                reason=call.reason,
                required=call.required,
            )
            for call in self._legacy_planner.plan(query, state)
        ]

    def suggest_tool_calls(self, query: str, state: AgentState, *, domain: str) -> list[ToolCall]:
        calls = []
        for candidate in self.suggest(query, state, domain=domain):
            call = candidate.to_tool_call()
            if call:
                calls.append(call)
        return calls
