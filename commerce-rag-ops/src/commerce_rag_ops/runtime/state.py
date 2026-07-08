from __future__ import annotations

from dataclasses import dataclass, field

from .step import AgentStepRecord, Observation


@dataclass
class BudgetState:
    max_steps: int = 6
    max_tool_calls: int = 5
    max_retrieval_calls: int = 2
    max_write_tool_drafts: int = 1
    steps_used: int = 0
    tool_calls_used: int = 0
    retrieval_calls_used: int = 0
    write_tool_drafts_used: int = 0

    def remaining(self) -> bool:
        return self.steps_used < self.max_steps


@dataclass
class RunState:
    run_id: str
    original_query: str
    conversation_id: str | None = None
    domain: str | None = None
    risk_level: str = "low"
    context: dict | None = None
    context_resolution: dict | None = None
    steps: list[AgentStepRecord] = field(default_factory=list)
    observations: list[Observation] = field(default_factory=list)
    evidence_pack: dict | None = None
    verification: dict | None = None
    final_action: str | None = None
    final_answer: str | None = None
    citations: list[str] = field(default_factory=list)
    budgets: BudgetState = field(default_factory=BudgetState)
