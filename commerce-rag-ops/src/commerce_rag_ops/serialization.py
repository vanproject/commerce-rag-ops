from __future__ import annotations

from .models import AgentState


def agent_state_to_dict(state: AgentState) -> dict:
    return {
        "trace_id": state.trace_id,
        "query": state.query,
        "original_query": state.original_query,
        "memory_context": state.memory_context,
        "eval_context": state.eval_context,
        "resolved_entities": state.resolved_entities,
        "context_resolution": state.context_resolution,
        "llm_advice": state.llm_advice,
        "agent_plan": state.agent_plan,
        "memory_reads": state.memory_reads,
        "skipped_memory_reason": state.skipped_memory_reason,
        "domain": state.domain,
        "route_decision": state.route_decision,
        "runtime_state": state.runtime_state,
        "evidence_pack": state.evidence_pack,
        "verification": state.verification,
        "repair_plan": state.repair_plan,
        "intent": state.intent,
        "risk_level": state.risk_level,
        "semantic_memory_source_defaults": state.semantic_memory_source_defaults,
        "retrieval_plan": state.retrieval_plan,
        "action": state.action,
        "answer": state.answer,
        "citations": state.citations,
        "tool_citations": state.tool_citations,
        "grader_scores": state.grader_scores,
        "tool_results": state.tool_results,
        "attempts": state.attempts,
        "trace": state.trace,
        "trace_run": state.trace_run,
        "trace_spans": state.trace_spans,
        "trace_artifacts": state.trace_artifacts,
        "retrieval_candidates": state.retrieval_candidates,
    }
