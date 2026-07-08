from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


ToolHandler = Callable[[dict[str, Any]], dict[str, Any]]


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: dict[str, Any]
    output_schema: dict[str, Any]
    read_only: bool
    risk_level: str
    requires_confirmation: bool
    handler: ToolHandler
    allowed_intents: list[str] = field(default_factory=list)
    allowed_domains: list[str] = field(default_factory=list)
    max_rows: int = 1
    redact_fields: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ToolCall:
    tool_name: str
    input: dict[str, Any]
    reason: str
    required: bool = True


@dataclass
class ToolResult:
    tool_name: str
    input: dict[str, Any]
    output: dict[str, Any]
    found: bool
    latency_ms: int
    error: str | None = None
    policy_decision: str = "allowed"
    evidence_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool_name": self.tool_name,
            "input": self.input,
            "output": self.output,
            "found": self.found,
            "latency_ms": self.latency_ms,
            "error": self.error,
            "policy_decision": self.policy_decision,
            "evidence_id": self.evidence_id,
        }
