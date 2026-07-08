from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


AgentActionType = Literal[
    "tool_call",
    "build_evidence",
    "verify",
    "final_answer",
    "refuse",
    "ask_user",
    "escalate",
]


@dataclass(frozen=True)
class AgentStep:
    action_type: AgentActionType
    tool_name: str | None = None
    tool_input: dict[str, Any] = field(default_factory=dict)
    reason_summary: str = ""
    expected_evidence: list[str] = field(default_factory=list)
    proposed_by: str = "domain_agent"
    accepted: bool = True
    rejected_reason: str = ""


@dataclass
class AgentStepRecord:
    step: AgentStep
    status: str = "proposed"
    observation_id: str | None = None
    rejected_reason: str = ""


@dataclass
class Observation:
    source: str
    kind: Literal["tool", "retrieval", "verification", "user", "system"]
    status: Literal["ok", "blocked", "failed", "requires_confirmation"]
    payload: dict[str, Any] = field(default_factory=dict)
    citations: list[str] = field(default_factory=list)
    structured_entities: list[dict[str, Any]] = field(default_factory=list)
