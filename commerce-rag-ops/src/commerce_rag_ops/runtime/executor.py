from __future__ import annotations

from typing import Any, Callable

from ..tools import ToolCall, ToolExecutor, ToolResult, normalize_tool_results
from .state import RunState
from .step import AgentStep, Observation


ToolResultSync = Callable[[list[ToolResult]], None]
SemanticToolExecutor = Callable[[AgentStep, list[ToolResult], str], dict[str, Any]]


class AgentStepExecutor:
    def __init__(
        self,
        *,
        recorder: Any,
        parent_span_id: str,
        attempt: int,
        query: str,
        intent: str,
        tool_executor: ToolExecutor,
        result_backend: str,
        semantic_tool_name: str,
        execute_semantic_tool: SemanticToolExecutor,
        sync_tool_results: ToolResultSync,
    ):
        self.recorder = recorder
        self.parent_span_id = parent_span_id
        self.attempt = attempt
        self.query = query
        self.intent = intent
        self.tool_executor = tool_executor
        self.result_backend = result_backend
        self.semantic_tool_name = semantic_tool_name
        self.execute_semantic_tool = execute_semantic_tool
        self.sync_tool_results = sync_tool_results
        self.structured_results: list[ToolResult] = []

    def execute(self, step: AgentStep, run_state: RunState) -> Observation:
        step_span = self.recorder.start_span(
            "domain_agent.step",
            kind="agent",
            parent_id=self.parent_span_id,
            attempt=self.attempt,
            inputs={
                "action_type": step.action_type,
                "tool_name": step.tool_name,
                "tool_input": step.tool_input,
                "reason_summary": step.reason_summary,
                "proposed_by": step.proposed_by,
                "accepted": step.accepted,
                "rejected_reason": step.rejected_reason,
            },
        )
        try:
            if step.tool_name == self.semantic_tool_name:
                self._record_policy_check(step, run_state, step_span)
                self.sync_tool_results(self.structured_results)
                memory_read = self.execute_semantic_tool(step, self.structured_results, step_span)
                status = "ok" if memory_read.get("found") else "failed"
                self.recorder.end_span(step_span, outputs=memory_read, metrics={"latency_ms": memory_read.get("latency_ms", 0)})
                return Observation(
                    source=self.semantic_tool_name,
                    kind="retrieval",
                    status=status,
                    payload=memory_read,
                    citations=memory_read.get("output", {}).get("doc_citations", []),
                )
            if step.action_type == "tool_call" and step.tool_name:
                call = ToolCall(step.tool_name, step.tool_input, step.reason_summary)
                self._record_policy_check(step, run_state, step_span, call=call)
                result = self.tool_executor.run(
                    [call],
                    query=self.query,
                    intent=self.intent,
                    domain=run_state.domain,
                    risk_level=run_state.risk_level,
                    action_type=step.action_type,
                )[0]
                self.structured_results.append(result)
                self.sync_tool_results(self.structured_results)
                status = _observation_status(result.policy_decision, result.found, result.error)
                payload = result.to_dict()
                self.recorder.end_span(step_span, outputs=payload, metrics={"latency_ms": result.latency_ms})
                return Observation(
                    source=step.tool_name,
                    kind="tool",
                    status=status,
                    payload=payload,
                    citations=[result.evidence_id] if result.evidence_id else [],
                )
            self.recorder.end_span(step_span, outputs={"status": "ok"})
            return Observation(source=step.tool_name or step.action_type, kind="system", status="ok", payload={"step": step.reason_summary})
        except Exception as exc:
            self.recorder.end_span(step_span, outputs={"error": str(exc)}, error=exc)
            return Observation(
                source=step.tool_name or step.action_type,
                kind="system",
                status="failed",
                payload={"error": str(exc), "step": step.reason_summary},
            )

    def normalized_tool_results(self) -> dict[str, Any]:
        return normalize_tool_results(self.structured_results, backend=self.result_backend)

    def _record_policy_check(
        self,
        step: AgentStep,
        run_state: RunState,
        parent_span_id: str,
        *,
        call: ToolCall | None = None,
    ) -> None:
        if not step.tool_name:
            return
        policy_span = self.recorder.start_span(
            "policy.check",
            kind="policy",
            parent_id=parent_span_id,
            attempt=self.attempt,
            inputs={
                "action_type": step.action_type,
                "tool_name": step.tool_name,
                "domain": run_state.domain,
                "risk_level": run_state.risk_level,
            },
        )
        try:
            spec = self.tool_executor.registry.get(step.tool_name)
            tool_call = call or ToolCall(step.tool_name, step.tool_input, step.reason_summary)
            decision = self.tool_executor.policy.check(
                tool_call,
                spec,
                query=self.query,
                intent=self.intent,
                domain=run_state.domain,
                risk_level=run_state.risk_level,
                action_type=step.action_type,
            )
            self.recorder.end_span(
                policy_span,
                outputs={
                    "allowed": decision.allowed,
                    "decision": decision.decision,
                    "reason": decision.reason,
                    "allowed_domains": spec.allowed_domains,
                    "allowed_intents_compat": spec.allowed_intents,
                    "read_only": spec.read_only,
                    "requires_confirmation": spec.requires_confirmation,
                },
            )
        except Exception as exc:
            self.recorder.end_span(policy_span, outputs={"error": str(exc)}, error=exc)


def _observation_status(policy_decision: str, found: bool, error: str | None) -> str:
    if policy_decision == "requires_confirmation":
        return "requires_confirmation"
    if policy_decision in {"blocked", "error"} or error:
        return "blocked" if policy_decision == "blocked" else "failed"
    return "ok" if found else "failed"
