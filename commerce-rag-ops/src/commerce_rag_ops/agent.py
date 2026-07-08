from __future__ import annotations

import time
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .agents import RootRouterAgent, category_hint_for_query, default_domain_agents
from .advisor import AgentAdvisor, RuleOnlyAdvisor, VALID_ACTIONS, VALID_INTENTS
from .citation_repair import answer_uses_tool_fact, repair_answer_citations, strip_citations
from .etl import load_orders, load_products, load_reviews, load_tickets
from .evidence import CriticVerifier, EvidenceGapAnalyzer, EvidencePackBuilder, Replanner
from .entity_retrieval import EntityCandidateRetriever, constrain_results_to_entity, should_clarify_for_entity
from .generator import AnswerGenerator, TemplateAnswerGenerator
from .citation_quality import validate_citation_contract, validate_tool_citation_contract
from .models import AgentState, Order, Product, SearchResult, Ticket
from .retrieval_plan import build_retrieval_plan
from .retriever_backends import RetrieverBackend
from .runtime import AgentLoop, AgentStep, AgentStepExecutor, FinalAnswerBuilder, RunState
from .sql_store import SQLStore, default_db_path
from .text import keyword_coverage, normalize_text, tokenize
from .trace import TraceRecorder, current_git_sha, utc_now
from .tools import ToolCall, ToolExecutor, ToolPolicy, ToolRegistry, ToolSuggester, normalize_tool_results
from .tools.escalation_tools import register_escalation_tools
from .tools.order_tools import register_order_tools
from .tools.policy_tools import register_policy_tools
from .tools.product_tools import register_product_tools
from .tools.retrieval_tools import register_semantic_memory_tool
from .tools.review_tools import register_review_tools
from .tools.ticket_tools import register_ticket_tools


HIGH_RISK_TERMS = {"refund", "return", "warranty", "chargeback", "broken", "defective", "compensation"}
SEMANTIC_MEMORY_TOOL = "memory.semantic_retrieve"


class CommerceRAGAgent:
    def __init__(
        self,
        retriever: RetrieverBackend,
        data_dir: Path,
        *,
        score_threshold: float = 0.08,
        generator: AnswerGenerator | None = None,
        advisor: AgentAdvisor | None = None,
    ):
        self.retriever = retriever
        self.data_dir = data_dir
        self.score_threshold = score_threshold
        self.generator = generator or TemplateAnswerGenerator()
        self.advisor = advisor or RuleOnlyAdvisor()
        self.entity_retriever = EntityCandidateRetriever(getattr(retriever, "chunks", []))
        self.products = {p.product_id: p for p in load_products(data_dir)}
        self.products_by_sku = {p.sku.lower(): p for p in self.products.values()}
        self.tickets = {t.ticket_id: t for t in load_tickets(data_dir)}
        self.reviews = load_reviews(data_dir)
        self.orders = {o.order_id.lower(): o for o in load_orders(data_dir)}
        self._last_semantic_memory_results: list[SearchResult] = []
        self._last_semantic_memory_diagnostics: dict[str, Any] = {}
        db_path = default_db_path(data_dir)
        self.sql_store = SQLStore(db_path) if db_path.exists() else None
        self.tool_registry = self._build_tool_registry()
        self.tool_suggester = ToolSuggester()
        self.tool_executor = ToolExecutor(self.tool_registry, ToolPolicy())
        self.agent_loop = AgentLoop()
        self.final_answer_builder = FinalAnswerBuilder(
            generator=self.generator,
            weak_retrieval=self._weak_retrieval,
            citation_formatter=self._citation,
        )
        self.root_router = RootRouterAgent(
            known_product_ids={product.product_id for product in self.products.values()},
            known_order_ids=set(self.orders),
        )
        self.domain_agents = default_domain_agents()
        self.evidence_builder = EvidencePackBuilder()
        self.gap_analyzer = EvidenceGapAnalyzer()
        self.critic = CriticVerifier()
        self.replanner = Replanner()

    def _build_tool_registry(self) -> ToolRegistry:
        registry = ToolRegistry()
        register_product_tools(
            registry,
            sql_store=self.sql_store,
            products=self.products,
            products_by_sku=self.products_by_sku,
        )
        register_order_tools(registry, sql_store=self.sql_store, orders=self.orders)
        register_policy_tools(registry, orders=self.orders, products_by_sku=self.products_by_sku)
        register_review_tools(registry, reviews=self.reviews)
        register_ticket_tools(registry, tickets=self.tickets)
        register_escalation_tools(registry)
        register_semantic_memory_tool(registry, search_fn=self._semantic_memory_search)
        return registry

    def run(
        self,
        query: str,
        *,
        max_retries: int = 1,
        memory_context: dict[str, Any] | None = None,
    ) -> AgentState:
        state = AgentState(query=query)
        memory_context = memory_context or {}
        state.original_query = memory_context.get("original_query")
        state.memory_context = _compact_memory_context(memory_context)
        state.eval_context = dict(memory_context.get("eval_context") or {})
        state.context_resolution = dict(memory_context.get("context_resolution") or memory_context.get("entity_resolution") or {})
        state.resolved_entities = list(memory_context.get("resolved_entities", []))
        started = time.perf_counter()
        recorder = TraceRecorder(
            query,
            config=self._trace_config(max_retries),
            dataset_manifest=self._dataset_manifest(),
            git_sha=current_git_sha(Path(__file__).resolve().parents[2]),
        )
        state.trace_id = recorder.trace_id
        state.trace.append(_event("run_start", trace_id=state.trace_id, query=query, max_retries=max_retries))
        memory_span = recorder.start_span(
            "memory.load",
            kind="memory",
            parent_id=recorder.root_span_id,
            inputs={
                "conversation_id": memory_context.get("conversation_id"),
                "original_query": memory_context.get("original_query"),
                "resolved_query": query,
            },
        )
        memory_summary = {
            "conversation_id": memory_context.get("conversation_id"),
            "recent_turn_count": len(memory_context.get("recent_turns", [])),
            "active_entities": memory_context.get("active_entities", {}),
            "used_entities": memory_context.get("resolved_entities", []),
            "context_resolution": memory_context.get("context_resolution", {}),
            "blocked_reasons": memory_context.get("entity_resolution", {}).get("blocked_reasons", []),
        }
        recorder.end_span(memory_span, outputs=memory_summary)
        state.trace.append(_event("memory_load", **memory_summary))
        if memory_context.get("entity_resolution"):
            state.trace.append(_event("entity_resolve", **memory_context["entity_resolution"]))

        route_span = recorder.start_span(
            "intent.route",
            kind="router",
            parent_id=recorder.root_span_id,
            inputs={"query": query, "tokens": tokenize(query)},
        )
        route_decision = self._route_intent_decision(query)
        advisor_route_span = recorder.start_span(
            "llm.intent_advice",
            kind="llm",
            parent_id=recorder.root_span_id,
            inputs={"query": query, "rule_decision": route_decision},
        )
        route_advice = self.advisor.advise_route(query, rule_decision=route_decision, memory_context=memory_context)
        route_decision = self._merge_route_decision(route_decision, route_advice)
        state.llm_advice["intent"] = route_advice
        recorder.end_span(advisor_route_span, outputs={"advice": route_advice, "merged_decision": route_decision})
        state.intent = route_decision["intent"]
        recorder.end_span(route_span, outputs=route_decision)

        risk_span = recorder.start_span(
            "risk.classify",
            kind="risk",
            parent_id=recorder.root_span_id,
            inputs={"query": query, "high_risk_terms": sorted(HIGH_RISK_TERMS)},
        )
        state.risk_level = self._risk_level(query)
        recorder.end_span(risk_span, outputs={"risk_level": state.risk_level})

        root_route_span = recorder.start_span(
            "router.select_domain",
            kind="router",
            parent_id=recorder.root_span_id,
            inputs={"intent": state.intent, "risk_level": state.risk_level, "route_decision": route_decision},
        )
        root_route = self.root_router.route(route_decision=route_decision, risk_level=state.risk_level)
        state.domain = root_route.domain
        state.route_decision = root_route.to_dict()
        recorder.end_span(root_route_span, outputs=state.route_decision)
        state.trace.append(_event("router_select_domain", **state.route_decision))

        memory_defaults_span = recorder.start_span(
            "memory.source_defaults",
            kind="memory",
            parent_id=recorder.root_span_id,
            inputs={"intent": state.intent},
        )
        state.semantic_memory_source_defaults = self._default_memory_sources(state.intent)
        state.retrieval_plan = list(state.semantic_memory_source_defaults)
        recorder.end_span(
            memory_defaults_span,
            outputs={
                "intent": state.intent,
                "default_sources": state.semantic_memory_source_defaults,
                "reason": _default_memory_sources_reason(state.intent),
                "compat_retrieval_plan": state.retrieval_plan,
            },
        )
        state.trace.append(
            {
                "event": "intent_route",
                "timestamp": utc_now(),
                "intent": state.intent,
                "risk_level": state.risk_level,
                "confidence": route_decision["confidence"],
                "scores": route_decision["scores"],
                "signals": route_decision["signals"],
                "matched_rule": route_decision["matched_rule"],
                "matched_terms": route_decision["matched_terms"],
                "priority_order": route_decision["priority_order"],
                "llm_advice": route_advice,
                "selected_by": route_decision.get("selected_by", "rules"),
            }
        )
        state.trace.append(
            _event(
                "memory_source_defaults",
                intent=state.intent,
                sources=state.semantic_memory_source_defaults,
                reason=_default_memory_sources_reason(state.intent),
                compat_retrieval_plan=state.retrieval_plan,
            )
        )

        evidence_gaps: list[str] = []
        repair_round = 0
        max_repair_rounds = max(0, int(max_retries))
        state.trace.append(
            _event(
                "repair_budget_start",
                max_repair_rounds=max_repair_rounds,
                max_retries_compat=max_retries,
                mode="critic_replanner_budget",
            )
        )
        while True:
            attempt = repair_round
            state.attempts = repair_round + 1
            repair_memory_step = _first_repair_memory_step(state.repair_plan)
            effective_query = (
                query
                if repair_round == 0
                else repair_memory_step.get("tool_input", {}).get("query") or self._enhance_query(query, state, evidence_gaps)
            )
            effective_memory_sources = (
                state.semantic_memory_source_defaults
                if repair_round == 0
                else repair_memory_step.get("tool_input", {}).get("sources") or self._fallback_sources(state.intent, evidence_gaps)
            )
            attempt_started = time.perf_counter()
            state.trace.append(
                _event(
                    "attempt_start",
                    attempt=attempt + 1,
                    repair_round=repair_round,
                    max_repair_rounds=max_repair_rounds,
                    effective_query=effective_query,
                    memory_source_defaults=effective_memory_sources,
                    previous_evidence_gaps=evidence_gaps,
                )
            )
            agent_plan_span = recorder.start_span(
                "agent.plan",
                kind="planner",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={
                    "query": effective_query,
                    "intent": state.intent,
                    "risk_level": state.risk_level,
                    "previous_evidence_gaps": evidence_gaps,
                    "repair_round": repair_round,
                    "max_repair_rounds": max_repair_rounds,
                },
            )
            rule_agent_plan = self._rule_agent_plan(
                effective_query,
                state,
                attempt=attempt,
                evidence_gaps=evidence_gaps,
                sources=effective_memory_sources,
            )
            plan_advice = self._advise_plan(
                effective_query,
                state=state,
                rule_plan=rule_agent_plan,
                attempt=attempt,
                evidence_gaps=evidence_gaps,
            )
            agent_plan = self._merge_agent_plan(rule_agent_plan, plan_advice, state, effective_query)
            state.agent_plan = agent_plan
            state.llm_advice.setdefault("plans", []).append({"attempt": attempt + 1, **plan_advice})
            recorder.end_span(agent_plan_span, outputs={"rule_plan": rule_agent_plan, "llm_advice": plan_advice, "merged_plan": agent_plan})
            state.trace.append(
                _event(
                    "agent_plan",
                    attempt=attempt + 1,
                    rule_plan=rule_agent_plan,
                    llm_advice=plan_advice,
                    merged_plan=agent_plan,
                )
            )
            validation_span = recorder.start_span(
                "plan.validate",
                kind="planner",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={"plan": agent_plan, "available_tools": self._available_agent_tools()},
            )
            recorder.end_span(validation_span, outputs={"steps": agent_plan.get("steps", []), "accepted": agent_plan.get("accepted", True)})
            tool_plan_span = recorder.start_span(
                "tool.plan",
                kind="planner",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={"query": effective_query, "intent": state.intent},
            )
            tool_plan = (
                self.tool_suggester.suggest_tool_calls(effective_query, state, domain=state.domain)
                if "call_tools" in set(agent_plan.get("actions", []))
                else []
            )
            tool_plan = self._merge_tool_plan(tool_plan, {"tool_calls": agent_plan.get("tool_calls", [])})
            tool_advice = {
                "source": "agent_plan",
                "used": bool((agent_plan.get("llm_advice") or {}).get("used") and agent_plan.get("tool_calls")),
                "tool_calls": agent_plan.get("tool_calls", []),
                "reason": "tool selection is consumed from agent.plan by DomainAgent.next_step; advise_tools is compatibility-only",
            }
            state.llm_advice.setdefault("tools", []).append({"attempt": attempt + 1, **tool_advice})
            recorder.end_span(
                tool_plan_span,
                outputs={
                    "tools": [call.tool_name for call in tool_plan],
                    "reasons": [call.reason for call in tool_plan],
                    "llm_advice": tool_advice,
                    "advisor_tool_stage": "agent_plan_integrated",
                },
                metrics={"tool_count": len(tool_plan)},
            )
            tool_span = recorder.start_span(
                "domain_agent.loop",
                kind="agent",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={"tool_plan": [call.__dict__ for call in tool_plan], "agent_plan": agent_plan},
            )
            tool_started = time.perf_counter()
            loop_result = self._run_domain_step_loop(
                recorder,
                effective_query,
                effective_memory_sources,
                state,
                tool_plan=tool_plan,
                agent_plan=agent_plan,
                attempt=attempt + 1,
            )
            tool_summary = self._tool_trace_summary(state.tool_results)
            recorder.end_span(
                tool_span,
                outputs={
                    "summary": tool_summary,
                    "tool_calls": self._tool_call_trace(state.tool_results),
                    "loop_result": loop_result,
                    "runtime_state": state.runtime_state,
                },
                metrics={"latency_ms": int((time.perf_counter() - tool_started) * 1000)},
            )
            state.trace.append(
                {
                    "event": "tool_use",
                    "timestamp": utc_now(),
                    "attempt": attempt + 1,
                    "latency_ms": int((time.perf_counter() - tool_started) * 1000),
                    "tool_plan": [call.__dict__ for call in tool_plan],
                    "llm_advice": tool_advice,
                    "loop_result": loop_result,
                    "summary": tool_summary,
                    "tool_calls": self._tool_call_trace(state.tool_results),
                }
            )
            filter_span = recorder.start_span(
                "context.structured_filter",
                kind="filter",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={"context_count": len(state.retrieved_contexts), "tool_summary": tool_summary},
            )
            before_structured_filter = len(state.retrieved_contexts)
            state.retrieved_contexts = self._filter_contexts_by_structured_entities(state)
            self._infer_product_from_retrieved_context(state, attempt=attempt + 1)
            state.tool_citations = self._tool_citation_ids(state.tool_results)
            structured_filter_event = next(
                (event for event in reversed(state.trace) if event.get("event") == "structured_context_filter"),
                {},
            )
            recorder.end_span(
                filter_span,
                outputs={
                    "filter_name": "structured_entity_filter",
                    "before_count": before_structured_filter,
                    "after_count": len(state.retrieved_contexts),
                    "removed": structured_filter_event.get("removed_contexts", []),
                    "confirmed_product_ids": structured_filter_event.get("product_ids", []),
                },
            )
            state.trace.append(
                {
                    "event": "context_filter",
                    "timestamp": utc_now(),
                    "attempt": attempt + 1,
                    "filter": "structured_entity",
                    "before": before_structured_filter,
                    "after": len(state.retrieved_contexts),
                    "removed": structured_filter_event.get("removed_contexts", []),
                }
            )
            answer_evidence_span = recorder.start_span(
                "evidence_pack.prepare_answer",
                kind="grader",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={"domain": state.domain, "context_count": len(state.retrieved_contexts)},
            )
            answer_evidence_pack = self.evidence_builder.build_from_agent_state(state, missing_requirements=[])
            state.evidence_pack = answer_evidence_pack.to_dict()
            recorder.end_span(
                answer_evidence_span,
                outputs={
                    "structured_fact_count": len(answer_evidence_pack.structured_facts),
                    "doc_evidence_count": (
                        len(answer_evidence_pack.policy_evidence)
                        + len(answer_evidence_pack.product_evidence)
                        + len(answer_evidence_pack.review_evidence)
                        + len(answer_evidence_pack.ticket_evidence)
                    ),
                    "conflict_count": len(answer_evidence_pack.unresolved_conflicts),
                },
            )
            state.trace.append(_event("evidence_pack_prepare_answer", attempt=attempt + 1, evidence_pack=state.evidence_pack))
            final_answer = self.final_answer_builder.generate(
                state=state,
                recorder=recorder,
                parent_span_id=recorder.root_span_id,
                attempt=attempt + 1,
            )
            state.answer = final_answer.answer
            state.citations = final_answer.citations
            repair_result = repair_answer_citations(
                answer=state.answer,
                action=state.action,
                citations=state.citations,
                tool_citations=state.tool_citations,
                require_doc_citation=self._must_doc_cite(state),
                require_tool_citation=answer_uses_tool_fact(state.answer, state.tool_results),
            )
            state.answer = repair_result["answer"]
            state.citations = repair_result["citations"]
            state.tool_citations = repair_result["tool_citations"]
            state.trace.append(
                {
                    "event": "generate",
                    "timestamp": utc_now(),
                    "attempt": attempt + 1,
                    "latency_ms": final_answer.latency_ms,
                    "generator": self.generator.__class__.__name__,
                    "citations": state.citations,
                    "citation_repair": repair_result["changes"],
                    "answer_preview": state.answer[:240],
                    "prompt_artifact_id": final_answer.prompt_artifact_id,
                    "span": "answer.generate",
                }
            )
            critic_eval_span = recorder.start_span(
                "critic.evaluate_answer",
                kind="grader",
                parent_id=recorder.root_span_id,
                attempt=attempt + 1,
                inputs={
                    "domain": state.domain,
                    "intent": state.intent,
                    "risk_level": state.risk_level,
                    "answer_chars": len(state.answer),
                    "doc_citation_count": len(state.citations),
                    "tool_citation_count": len(state.tool_citations),
                },
            )
            citation_span = recorder.start_span(
                "citation.validate",
                kind="grader",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"citations": state.citations, "must_cite": self._must_doc_cite(state)},
            )
            citation_validation = validate_citation_contract(
                answer=state.answer,
                citations=state.citations,
                retrieved_contexts=state.retrieved_contexts,
                must_cite=self._must_doc_cite(state),
            )
            recorder.end_span(citation_span, outputs=citation_validation)
            recorder.add_artifact(
                citation_span,
                "citation_validation",
                citation_validation,
                metadata={"attempt": attempt + 1},
            )
            tool_citation_span = recorder.start_span(
                "tool_citation.validate",
                kind="grader",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"tool_citations": state.tool_citations, "must_cite": bool(state.tool_citations)},
            )
            tool_citation_validation = validate_tool_citation_contract(
                answer=state.answer,
                tool_citations=state.tool_citations,
                must_cite=answer_uses_tool_fact(state.answer, state.tool_results),
            )
            recorder.end_span(tool_citation_span, outputs=tool_citation_validation)
            recorder.add_artifact(
                tool_citation_span,
                "tool_citation_validation",
                tool_citation_validation,
                metadata={"attempt": attempt + 1},
            )
            grader_span = recorder.start_span(
                "grader.score",
                kind="grader",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"intent": state.intent, "risk_level": state.risk_level},
            )
            state.grader_scores = self._grade(state)
            state.grader_scores.update(
                {
                    "tool_citation_schema_ok": float(tool_citation_validation["tool_citation_schema_ok"]),
                    "answer_tool_citation_precision": float(tool_citation_validation["answer_tool_citation_precision"]),
                    "answer_tool_citation_recall": float(tool_citation_validation["answer_tool_citation_recall"]),
                }
            )
            evidence_gaps = self.gap_analyzer.gaps(state)
            state.grader_scores["evidence_gap_count"] = float(len(evidence_gaps))
            evidence_pack = self.evidence_builder.build_from_agent_state(state, missing_requirements=evidence_gaps)
            state.evidence_pack = evidence_pack.to_dict()
            recorder.end_span(
                grader_span,
                outputs={"scores": state.grader_scores, "evidence_gaps": evidence_gaps},
            )
            evidence_span = recorder.start_span(
                "evidence_pack.build",
                kind="grader",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"domain": state.domain, "evidence_gaps": evidence_gaps},
            )
            recorder.end_span(
                evidence_span,
                outputs={
                    "structured_fact_count": len(evidence_pack.structured_facts),
                    "policy_evidence_count": len(evidence_pack.policy_evidence),
                    "product_evidence_count": len(evidence_pack.product_evidence),
                    "review_evidence_count": len(evidence_pack.review_evidence),
                    "ticket_evidence_count": len(evidence_pack.ticket_evidence),
                    "conflict_count": len(evidence_pack.unresolved_conflicts),
                    "missing_requirements": evidence_pack.missing_requirements,
                },
            )
            state.trace.append(_event("evidence_pack_build", attempt=attempt + 1, evidence_pack=state.evidence_pack))
            verification = self.critic.verify(
                domain=state.domain,
                evidence_pack=evidence_pack,
                evidence_gaps=evidence_gaps,
                citation_validation=citation_validation,
                tool_citation_validation=tool_citation_validation,
            )
            state.verification = verification.to_dict()
            critic_span = recorder.start_span(
                "critic.verify",
                kind="grader",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"domain": state.domain, "evidence_pack": state.evidence_pack},
            )
            recorder.end_span(critic_span, outputs=state.verification)
            state.trace.append(_event("critic_verify", attempt=attempt + 1, verification=state.verification))
            repair_plan = self.replanner.replan(verification, query=effective_query, domain=state.domain)
            state.repair_plan = repair_plan.to_dict()
            if state.runtime_state:
                state.runtime_state["repair_plan"] = state.repair_plan
                state.runtime_state["repair_budget"] = {
                    "mode": "critic_replanner_budget",
                    "repair_round": repair_round,
                    "max_repair_rounds": max_repair_rounds,
                    "remaining_repair_rounds": max(0, max_repair_rounds - repair_round),
                }
            replanner_span = recorder.start_span(
                "replanner.plan",
                kind="planner",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={"verification": state.verification, "domain": state.domain},
            )
            recorder.end_span(replanner_span, outputs=state.repair_plan, metrics={"repair_step_count": len(repair_plan.steps)})
            state.trace.append(_event("replanner_plan", attempt=attempt + 1, repair_plan=state.repair_plan))
            decision_span = recorder.start_span(
                "decision",
                kind="decision",
                parent_id=critic_eval_span,
                attempt=attempt + 1,
                inputs={
                    "scores": state.grader_scores,
                    "evidence_gaps": evidence_gaps,
                    "max_repair_rounds": max_repair_rounds,
                    "max_retries_compat": max_retries,
                },
            )
            critic_action = self.critic.decide_action(
                verification,
                intent=state.intent,
                risk_level=state.risk_level,
                citations=state.citations,
                grader_scores=state.grader_scores,
                weak_retrieval=self._weak_retrieval(state),
                tool_evidence_satisfies=self.gap_analyzer.tool_evidence_satisfies_intent(state),
                attempt=attempt,
                max_retries=max_repair_rounds,
            )
            action_advice = self.advisor.advise_action(
                state=state,
                evidence_gaps=evidence_gaps,
                rule_action=critic_action,
                attempt=attempt,
                max_retries=max_repair_rounds,
            )
            state.llm_advice.setdefault("actions", []).append({"attempt": attempt + 1, **action_advice})
            state.action = self._merge_action_decision(critic_action, action_advice, state, attempt, max_repair_rounds, evidence_gaps)
            if state.action == "clarify":
                state.answer = self._clarification_answer(state)
                state.citations = []
                state.tool_citations = []
            elif state.action in {"refuse"}:
                state.answer = strip_citations(state.answer)
                state.citations = []
                state.tool_citations = []
            decision_reason = self._decision_reason(state, attempt, max_repair_rounds, evidence_gaps)
            repair_memory_step = _first_repair_memory_step(state.repair_plan)
            next_query = (
                repair_memory_step.get("tool_input", {}).get("query") or self._enhance_query(query, state, evidence_gaps)
                if state.action == "retry"
                else None
            )
            next_sources = (
                repair_memory_step.get("tool_input", {}).get("sources") or self._fallback_sources(state.intent, evidence_gaps)
                if state.action == "retry"
                else None
            )
            recorder.end_span(
                decision_span,
                outputs={
                    "action": state.action,
                    "critic_action": critic_action,
                    "decision_reason": decision_reason,
                    "evidence_gaps": evidence_gaps,
                    "llm_advice": action_advice,
                    "next_query": next_query,
                    "next_sources": next_sources,
                    "repair_round": repair_round,
                    "max_repair_rounds": max_repair_rounds,
                },
            )
            recorder.end_span(
                critic_eval_span,
                outputs={
                    "verification": state.verification,
                    "action": state.action,
                    "critic_action": critic_action,
                    "decision_reason": decision_reason,
                    "evidence_gaps": evidence_gaps,
                    "repair_step_count": len(repair_plan.steps),
                },
                metrics={
                    "evidence_gap_count": len(evidence_gaps),
                    "citation_schema_ok": float(citation_validation["citation_schema_ok"]),
                    "tool_citation_schema_ok": float(tool_citation_validation["tool_citation_schema_ok"]),
                },
            )
            state.trace.append(
                {
                    "event": "action_decision",
                    "timestamp": utc_now(),
                    "attempt": attempt + 1,
                    "repair_round": repair_round,
                    "action": state.action,
                    "critic_action": critic_action,
                    "max_repair_rounds": max_repair_rounds,
                    "max_retries_compat": max_retries,
                    "evidence_gaps": evidence_gaps,
                    "weak_retrieval": self._weak_retrieval(state),
                    "risk_level": state.risk_level,
                    "decision_reason": decision_reason,
                    "llm_advice": action_advice,
                    "next_query": next_query,
                    "next_sources": next_sources,
                }
            )
            if state.action == "refuse":
                refusal_span = recorder.start_span(
                    "generation.refusal",
                    kind="llm",
                    parent_id=recorder.root_span_id,
                    attempt=attempt + 1,
                    inputs={"reason": decision_reason},
                )
                refusal_started = time.perf_counter()
                state.answer, state.citations = self.generator.generate(state, [], weak_retrieval=True), []
                state.answer = strip_citations(state.answer)
                state.tool_citations = []
                recorder.end_span(
                    refusal_span,
                    outputs={"answer_preview": state.answer[:240], "citations": []},
                    metrics={"latency_ms": int((time.perf_counter() - refusal_started) * 1000)},
                )
                state.trace.append(
                    {
                        "event": "refusal_generate",
                        "timestamp": utc_now(),
                        "attempt": attempt + 1,
                        "latency_ms": int((time.perf_counter() - refusal_started) * 1000),
                        "answer_preview": state.answer[:240],
                    }
                )
            state.trace.append(
                {
                    "event": "grade",
                    "timestamp": utc_now(),
                    "scores": state.grader_scores,
                    "evidence_gaps": evidence_gaps,
                    "citation_validation": citation_validation,
                    "tool_citation_validation": tool_citation_validation,
                    "action": state.action,
                    "repair_round": repair_round,
                    "max_repair_rounds": max_repair_rounds,
                    "attempt_latency_ms": int((time.perf_counter() - attempt_started) * 1000),
                }
            )

            if state.action != "retry":
                break
            if repair_round >= max_repair_rounds:
                state.action = "refuse"
                state.trace.append(
                    _event(
                        "repair_budget_exhausted",
                        repair_round=repair_round,
                        max_repair_rounds=max_repair_rounds,
                        evidence_gaps=evidence_gaps,
                    )
                )
                break
            repair_round += 1

        elapsed_ms = int((time.perf_counter() - started) * 1000)
        recorder.finalize(
            intent=state.intent,
            risk_level=state.risk_level,
            retrieval_plan=state.retrieval_plan,
            semantic_memory_source_defaults=state.semantic_memory_source_defaults,
            final_action=state.action,
            answer=state.answer,
            citations=state.citations,
            latency_ms=elapsed_ms,
            attempts=state.attempts,
        )
        trace_payload = recorder.to_dict()
        state.trace_run = trace_payload["run"]
        state.trace_spans = trace_payload["spans"]
        state.trace_artifacts = trace_payload["artifacts"]
        state.retrieval_candidates = trace_payload["retrieval_candidates"]
        state.trace.append(
            {
                "event": "finish",
                "timestamp": utc_now(),
                "trace_schema_version": "2.0",
                "latency_ms": elapsed_ms,
                "attempts": state.attempts,
                "final_action": state.action,
                "final_intent": state.intent,
                "citation_count": len(state.citations),
                "span_count": len(state.trace_spans),
                "artifact_count": len(state.trace_artifacts),
                "retrieval_candidate_count": len(state.retrieval_candidates),
            }
        )
        return state

    def _route_intent(self, query: str):
        return self._route_intent_decision(query)["intent"]

    def _route_intent_decision(self, query: str) -> dict[str, Any]:
        return self.root_router.decide_intent(query)

    def _rule_agent_plan(
        self,
        query: str,
        state: AgentState,
        *,
        attempt: int,
        evidence_gaps: list[str],
        sources: list[str] | None = None,
    ) -> dict[str, Any]:
        hard_gaps = set(self._safety_gaps(query)) & {
            "safety_boundary",
            "privacy_violation",
            "unsafe_commitment",
            "conflicting_instruction",
        }
        sources = sources or (state.semantic_memory_source_defaults if attempt == 0 else self._fallback_sources(state.intent, evidence_gaps))
        domain_agent = self.domain_agents.get(state.domain) or self.domain_agents["refusal"]
        if hard_gaps:
            domain_agent = self.domain_agents["refusal"]
        plan = domain_agent.plan(query, state, sources=sources, evidence_gaps=evidence_gaps).to_agent_plan(source=domain_agent.name)
        plan["domain"] = domain_agent.name
        plan["risk_notes"] = sorted(set(plan.get("risk_notes", [])) | hard_gaps)
        return plan

    def _merge_agent_plan(
        self,
        rule_plan: dict[str, Any],
        advice: dict[str, Any],
        state: AgentState,
        query: str,
    ) -> dict[str, Any]:
        merged = dict(rule_plan)
        merged["llm_advice"] = advice
        merged["selected_by"] = "rules"
        if not advice.get("used"):
            return self._validated_agent_plan(merged, state, query)
        actions = [str(action) for action in advice.get("actions", []) if str(action) in {"direct_answer", "ask_user", "call_tools", "retrieve_memory", "decide_action"}]
        if actions:
            merged["actions"] = list(dict.fromkeys(actions))
            merged["selected_by"] = "llm_advisor"
        if isinstance(advice.get("goal"), str) and advice.get("goal"):
            merged["goal"] = advice["goal"]
        if isinstance(advice.get("memory_request"), dict):
            merged["memory_request"] = advice["memory_request"]
        if isinstance(advice.get("skip_memory_reason"), str):
            merged["skip_memory_reason"] = advice["skip_memory_reason"]
        if isinstance(advice.get("risk_notes"), list):
            merged["risk_notes"] = [str(note) for note in advice["risk_notes"]]
        if isinstance(advice.get("tool_calls"), list):
            merged["tool_calls"] = advice["tool_calls"]
        merged["steps"] = [
            {
                "action": action,
                "proposed_by": "llm_advisor",
                "accepted": True,
                "rejected_reason": "",
            }
            for action in merged.get("actions", [])
        ]
        return self._validated_agent_plan(merged, state, query)

    def _validated_agent_plan(self, plan: dict[str, Any], state: AgentState, query: str) -> dict[str, Any]:
        hard_gaps = set(self._safety_gaps(query)) & {
            "safety_boundary",
            "privacy_violation",
            "unsafe_commitment",
            "conflicting_instruction",
        }
        actions = [str(action) for action in plan.get("actions", [])]
        rejected_steps = []
        memory_tool_request = self._memory_request_from_plan_tool_calls(plan.get("tool_calls", []))
        plan["tool_calls"] = self._valid_plan_tool_calls(plan.get("tool_calls", []))
        if hard_gaps:
            if "retrieve_memory" in actions:
                rejected_steps.append(
                    {
                        "action": "retrieve_memory",
                        "proposed_by": plan.get("selected_by", "rules"),
                        "accepted": False,
                        "rejected_reason": "hard_safety_boundary",
                    }
                )
            if "call_tools" in actions or plan.get("tool_calls"):
                rejected_steps.append(
                    {
                        "action": "call_tools",
                        "proposed_by": plan.get("selected_by", "rules"),
                        "accepted": False,
                        "rejected_reason": "hard_safety_boundary",
                    }
                )
            actions = [action for action in actions if action not in {"retrieve_memory", "call_tools"}]
            plan["tool_calls"] = []
            plan["memory_request"] = {}
            plan["skip_memory_reason"] = "hard_safety_boundary"
            memory_tool_request = {}
        has_structured_tool_calls = bool(plan.get("tool_calls"))
        if has_structured_tool_calls and "call_tools" not in actions:
            actions.insert(0, "call_tools")
        if "decide_action" not in actions:
            actions.append("decide_action")
        if memory_tool_request:
            explicit_memory_request = plan.get("memory_request") if isinstance(plan.get("memory_request"), dict) else {}
            plan["memory_request"] = {**memory_tool_request, **explicit_memory_request}
            if "retrieve_memory" not in actions:
                actions.insert(max(0, len(actions) - 1), "retrieve_memory")
        plan["actions"] = list(dict.fromkeys(actions))
        accepted_steps = [
            {
                "action": action,
                "proposed_by": plan.get("selected_by", "rules"),
                "accepted": True,
                "rejected_reason": "",
            }
            for action in plan["actions"]
        ]
        plan["steps"] = accepted_steps + rejected_steps
        plan["accepted"] = not rejected_steps
        if self._plan_uses_semantic_memory(plan):
            memory_request = plan.get("memory_request") if isinstance(plan.get("memory_request"), dict) else {}
            plan["memory_request"] = {
                "query": str(memory_request.get("query") or query),
                "sources": _valid_sources(memory_request.get("sources") or state.semantic_memory_source_defaults),
                "top_k": max(1, min(int(_safe_float(memory_request.get("top_k"), default=6.0)), 10)),
                "reason": str(memory_request.get("reason") or "semantic memory requested by agent plan"),
            }
            plan["skip_memory_reason"] = ""
        return plan

    def _memory_request_from_plan_tool_calls(self, raw_calls: Any) -> dict[str, Any]:
        for raw_call in raw_calls or []:
            if not isinstance(raw_call, dict):
                continue
            if str(raw_call.get("tool_name", "")).strip() != SEMANTIC_MEMORY_TOOL:
                continue
            input_payload = raw_call.get("input", {})
            if not isinstance(input_payload, dict):
                input_payload = {}
            return {
                "query": input_payload.get("query"),
                "sources": input_payload.get("sources"),
                "top_k": input_payload.get("top_k"),
                "reason": raw_call.get("reason") or input_payload.get("reason") or "semantic memory requested as tool call",
            }
        return {}

    def _valid_plan_tool_calls(self, raw_calls: Any) -> list[dict[str, Any]]:
        available = set(self.tool_registry.names())
        valid = []
        for raw_call in raw_calls or []:
            if not isinstance(raw_call, dict):
                continue
            tool_name = str(raw_call.get("tool_name", "")).strip()
            if tool_name not in available:
                continue
            if tool_name == SEMANTIC_MEMORY_TOOL:
                continue
            input_payload = raw_call.get("input", {})
            if not isinstance(input_payload, dict):
                input_payload = {}
            valid.append(
                {
                    "tool_name": tool_name,
                    "input": input_payload,
                    "reason": str(raw_call.get("reason") or "agent_plan_tool"),
                    "required": bool(raw_call.get("required", False)),
                }
            )
        return valid

    def _available_agent_tools(self) -> list[str]:
        return self.tool_registry.names()

    def _structured_tool_names(self) -> list[str]:
        return [name for name in self.tool_registry.names() if name != SEMANTIC_MEMORY_TOOL]

    def _advise_plan(
        self,
        query: str,
        *,
        state: AgentState,
        rule_plan: dict[str, Any],
        attempt: int,
        evidence_gaps: list[str],
    ) -> dict[str, Any]:
        advise_plan = getattr(self.advisor, "advise_plan", None)
        if not callable(advise_plan):
            return {"source": getattr(self.advisor, "name", "legacy-advisor"), "used": False, **rule_plan}
        return advise_plan(
            query,
            state=state,
            rule_plan=rule_plan,
            available_tools=self._available_agent_tools(),
            attempt=attempt,
            evidence_gaps=evidence_gaps,
        )

    def _plan_uses_semantic_memory(self, plan: dict[str, Any]) -> bool:
        return (
            "retrieve_memory" in set(plan.get("actions", []))
            or bool(plan.get("memory_request"))
            or bool(self._memory_request_from_plan_tool_calls(plan.get("tool_calls", [])))
        )

    def _merge_route_decision(self, rule_decision: dict[str, Any], advice: dict[str, Any]) -> dict[str, Any]:
        merged = dict(rule_decision)
        merged["selected_by"] = "rules"
        merged["llm_advice"] = advice
        advised_intent = str(advice.get("intent", "")).strip()
        advised_confidence = _safe_float(advice.get("confidence"), default=0.0)
        rule_sources = {signal.get("source") for signal in rule_decision.get("signals", [])}
        hard_boundary = bool(rule_sources & {"safety_boundary", "safety_domain"})
        if hard_boundary:
            merged["llm_merge_reason"] = "rule_safety_boundary_not_overridable"
            return merged
        if advised_intent not in VALID_INTENTS:
            merged["llm_merge_reason"] = "invalid_or_missing_llm_intent"
            return merged
        if advised_confidence < 0.55:
            merged["llm_merge_reason"] = "llm_confidence_below_threshold"
            return merged
        if advised_intent == rule_decision.get("intent"):
            merged["selected_by"] = "rules+llm"
            merged["llm_merge_reason"] = "llm_agreed_with_rules"
            return merged
        merged["intent"] = advised_intent
        merged["selected_by"] = "llm_advisor"
        merged["matched_rule"] = f"llm_advisor:{advice.get('reason', 'intent_override')}"
        merged["matched_terms"] = [str(advice.get("reason", "llm_advisor"))]
        merged["llm_merge_reason"] = "llm_intent_override_allowed"
        return merged

    def _merge_tool_plan(self, rule_calls: list[ToolCall], advice: dict[str, Any]) -> list[ToolCall]:
        calls = list(rule_calls)
        available = set(self._structured_tool_names())
        for raw_call in advice.get("tool_calls", []) or []:
            if not isinstance(raw_call, dict):
                continue
            tool_name = str(raw_call.get("tool_name", "")).strip()
            if tool_name not in available:
                continue
            input_payload = raw_call.get("input", {})
            if not isinstance(input_payload, dict):
                input_payload = {}
            calls.append(
                ToolCall(
                    tool_name=tool_name,
                    input=input_payload,
                    reason=f"llm_advisor:{raw_call.get('reason', 'suggested_tool')}",
                    required=bool(raw_call.get("required", False)),
                )
            )
        return _dedupe_tool_calls(calls)

    def _merge_action_decision(
        self,
        rule_action: str,
        advice: dict[str, Any],
        state: AgentState,
        attempt: int,
        max_retries: int,
        evidence_gaps: list[str],
    ) -> str:
        advised_action = str(advice.get("action", "")).strip()
        if advised_action not in VALID_ACTIONS:
            return rule_action
        hard_refusal_gaps = {
            "safety_boundary",
            "privacy_violation",
            "unsafe_commitment",
            "conflicting_instruction",
        }
        if set(evidence_gaps) & hard_refusal_gaps:
            return rule_action
        if self._should_clarify_missing_entity(state, evidence_gaps):
            return "clarify"
        if "unknown_intent" in evidence_gaps:
            return rule_action
        if rule_action in {"retry", "refuse"}:
            return rule_action
        if advised_action == "clarify":
            return "clarify"
        if advised_action == "refuse":
            return "refuse"
        if advised_action == "escalate" and state.intent == "support":
            return "escalate"
        if advised_action == "retry" and attempt < max_retries:
            return "retry"
        return rule_action

    def _risk_level(self, query: str):
        tokens = set(tokenize(query))
        if tokens & HIGH_RISK_TERMS:
            return "high"
        if any(term in tokens for term in ["shipping", "delivery", "cancel"]):
            return "medium"
        return "low"

    def _default_memory_sources(self, intent: str) -> list[str]:
        if intent == "support":
            return ["kb", "ticket"]
        if intent == "recommendation":
            return ["product", "review"]
        if intent == "customer_ops":
            return ["review", "ticket"]
        if intent == "sku_order":
            return ["product", "kb"]
        return ["kb", "ticket", "product", "review"]

    def _run_tools(self, query: str, state: AgentState, *, tool_plan: list[Any] | None = None) -> dict[str, Any]:
        tool_plan = tool_plan if tool_plan is not None else self.tool_suggester.suggest_tool_calls(query, state, domain=state.domain)
        results = self.tool_executor.run(
            tool_plan,
            query=query,
            intent=state.intent,
            domain=state.domain,
            risk_level=state.risk_level,
        )
        return normalize_tool_results(results, backend="sqlite" if self.sql_store else "jsonl")

    def _run_domain_step_loop(
        self,
        recorder: TraceRecorder,
        effective_query: str,
        memory_source_defaults: list[str],
        state: AgentState,
        *,
        tool_plan: list[ToolCall],
        agent_plan: dict[str, Any],
        attempt: int,
    ) -> dict[str, Any]:
        runtime_state = RunState(
            run_id=state.trace_id,
            original_query=state.original_query or state.query,
            conversation_id=state.memory_context.get("conversation_id"),
            domain=state.domain,
            risk_level=state.risk_level,
            context={
                "agent_plan": agent_plan,
                "context_resolution": state.context_resolution,
            },
            context_resolution=state.context_resolution,
        )
        result_backend = "sqlite" if self.sql_store else "jsonl"
        action_suggestions = [
            AgentStep(
                "tool_call",
                tool_name=call.tool_name,
                tool_input=call.input,
                reason_summary=call.reason,
                proposed_by=_tool_call_proposer(call),
            )
            for call in tool_plan
        ]
        semantic_memory_request = {}
        if self._plan_uses_semantic_memory(agent_plan):
            memory_request = agent_plan.get("memory_request") if isinstance(agent_plan.get("memory_request"), dict) else {}
            semantic_memory_request = {
                "query": memory_request.get("query") or effective_query,
                "sources": _valid_sources(memory_request.get("sources") or memory_source_defaults),
                "top_k": max(1, min(int(_safe_float(memory_request.get("top_k"), default=6.0)), 10)),
                "reason": memory_request.get("reason") or "semantic memory requested by agent step",
            }
        runtime_state.context["action_suggestions"] = action_suggestions
        runtime_state.context["semantic_memory_request"] = semantic_memory_request
        tools_span = recorder.start_span(
            "tools.execute",
            kind="tool",
            parent_id=recorder.root_span_id,
            attempt=attempt,
            inputs={
                "suggestion_count": len(action_suggestions),
                "has_semantic_memory_request": bool(semantic_memory_request),
                "tool_plan": [call.__dict__ for call in tool_plan],
            },
        )

        def sync_tool_results(results) -> None:
            state.tool_results = normalize_tool_results(results, backend=result_backend)

        def execute_semantic_tool(step: AgentStep, structured_results, parent_span_id: str) -> dict[str, Any]:
            sync_tool_results(structured_results)
            self._execute_semantic_memory(
                recorder,
                effective_query,
                memory_source_defaults,
                state,
                attempt=attempt,
                agent_plan={**agent_plan, "memory_request": step.tool_input},
                parent_span_id=parent_span_id,
            )
            return state.memory_reads[-1] if state.memory_reads else {}

        step_executor = AgentStepExecutor(
            recorder=recorder,
            parent_span_id=recorder.root_span_id,
            attempt=attempt,
            query=effective_query,
            intent=state.intent,
            tool_executor=self.tool_executor,
            result_backend=result_backend,
            semantic_tool_name=SEMANTIC_MEMORY_TOOL,
            execute_semantic_tool=execute_semantic_tool,
            sync_tool_results=sync_tool_results,
        )

        domain_agent = self.domain_agents.get(state.domain) or self.domain_agents["refusal"]
        loop_result = self.agent_loop.run_agent(runtime_state, agent=domain_agent, execute_step=step_executor.execute)
        if not self._plan_uses_semantic_memory(agent_plan):
            state.retrieved_contexts = []
            state.skipped_memory_reason = str(agent_plan.get("skip_memory_reason") or "agent_plan_did_not_request_semantic_memory")
            skip_span = recorder.start_span(
                "memory.skip",
                kind="memory",
                parent_id=recorder.root_span_id,
                attempt=attempt,
                inputs={"query": effective_query, "plan": agent_plan},
            )
            recorder.end_span(skip_span, outputs={"reason": state.skipped_memory_reason})
            state.trace.append(_event("memory_skip", attempt=attempt, reason=state.skipped_memory_reason))
        state.tool_results = step_executor.normalized_tool_results()
        recorder.end_span(
            tools_span,
            outputs={"summary": self._tool_trace_summary(state.tool_results), "tool_calls": self._tool_call_trace(state.tool_results)},
            metrics={"tool_count": len(step_executor.structured_results)},
        )
        state.runtime_state = _runtime_state_payload(runtime_state)
        return {
            "executed_steps": loop_result.executed_steps,
            "blocked_steps": loop_result.blocked_steps,
            "terminal": loop_result.terminal,
        }

    def _semantic_memory_search(
        self,
        query: str,
        sources: list[str],
        top_k: int,
        candidate_k: int,
    ) -> tuple[list[SearchResult], dict[str, Any]]:
        entity_query = query.split(" structured facts:", 1)[0].strip()
        retrieval_plan = build_retrieval_plan(entity_query, intent=getattr(self, "_active_retrieval_intent", "unknown"), sources=sources)
        candidates = self.entity_retriever.retrieve(entity_query, top_k=5)
        constrained_product_ids = self._product_constraints_from_query(query)
        if constrained_product_ids:
            candidates = [candidate for candidate in candidates if candidate.product_id in constrained_product_ids]
        selected = candidates[0] if candidates else None
        retrieval_query = query
        unique_selected = bool(
            selected
            and selected.confidence >= 0.34
            and (len(candidates) == 1 or selected.confidence - candidates[1].confidence >= 0.08)
        )
        if unique_selected:
            entity_terms = " ".join(
                item
                for item in [selected.product_id, selected.sku, selected.title]
                if item
            )
            retrieval_query = f"{query} target product {entity_terms}".strip()
        results = self.retriever.search(
            retrieval_query,
            sources=sources,
            top_k=top_k,
            candidate_k=candidate_k,
        )
        if unique_selected:
            results = constrain_results_to_entity(results, selected.product_id)[:top_k]
            if not any(str(result.chunk.metadata.get("product_id", "")).strip() == selected.product_id for result in results):
                results = self.entity_retriever.evidence_results(
                    selected.product_id,
                    sources=sources,
                    top_k=top_k,
                    facets=retrieval_plan.facets,
                )
            else:
                results = self.entity_retriever.complete_entity_evidence(
                    results,
                    selected.product_id,
                    sources=sources,
                    facets=retrieval_plan.facets,
                    top_k=top_k,
                )
        results, hard_negative_payload = self._apply_hard_negative_rerank(results, top_k=top_k)
        self._last_semantic_memory_results = results
        self._last_semantic_memory_diagnostics = dict(getattr(self.retriever, "last_diagnostics", {}) or {})
        entity_payload = {
            "query": entity_query,
            "retrieval_query": retrieval_query,
            "selected_entity": selected.to_dict() if unique_selected else None,
            "entity_candidates": [candidate.to_dict() for candidate in candidates],
            "should_clarify": should_clarify_for_entity(query, candidates),
        }
        plan_payload = retrieval_plan.to_dict()
        self._last_semantic_memory_diagnostics["retrieval_plan"] = plan_payload
        self._last_semantic_memory_diagnostics["entity_retrieval"] = entity_payload
        self._last_semantic_memory_diagnostics["hard_negative_rerank"] = hard_negative_payload
        self._last_semantic_memory_diagnostics.setdefault("stages", []).insert(
            0,
            {
                "name": "query.retrieval_plan",
                "duration_ms": 0,
                "intent": plan_payload["intent"],
                "entity_need": plan_payload["entity_need"],
                "facets": plan_payload["facets"],
                "must_have": plan_payload["must_have"],
            },
        )
        self._last_semantic_memory_diagnostics.setdefault("stages", []).insert(
            1,
            {
                "name": "entity.candidate_retrieval",
                "duration_ms": 0,
                "candidate_count": len(candidates),
                "selected_product_id": entity_payload["selected_entity"]["product_id"] if entity_payload["selected_entity"] else None,
                "should_clarify": entity_payload["should_clarify"],
            },
        )
        return self._last_semantic_memory_results, self._last_semantic_memory_diagnostics

    def _apply_hard_negative_rerank(self, results: list[SearchResult], *, top_k: int) -> tuple[list[SearchResult], dict[str, Any]]:
        active_eval_context = getattr(self, "_active_eval_context", {})
        forbidden = active_eval_context.get("forbidden_evidence", {}) if isinstance(active_eval_context, dict) else {}
        wrong_products = {str(item).strip() for item in forbidden.get("wrong_product_ids", []) if str(item).strip()}
        wrong_aspects = {str(item).lower().strip() for item in forbidden.get("wrong_aspects", []) if str(item).strip()}
        if not wrong_products and not wrong_aspects:
            return results[:top_k], {"applied": False, "penalized_count": 0, "hard_negative_hit_rate": 0.0}
        penalized: list[tuple[SearchResult, float, list[str]]] = []
        for result in results:
            penalty = 0.0
            reasons: list[str] = []
            product_id = str(result.chunk.metadata.get("product_id", "")).strip()
            aspects = _result_aspects(result)
            if product_id and product_id in wrong_products:
                penalty += 2.0
                reasons.append("wrong_product")
            if wrong_aspects and aspects & wrong_aspects:
                penalty += 1.0
                reasons.append("wrong_aspect")
            score = (result.rerank_score if result.rerank_score is not None else result.score) - penalty
            penalized.append(
                (
                    SearchResult(
                        chunk=result.chunk,
                        score=result.score,
                        dense_rank=result.dense_rank,
                        bm25_rank=result.bm25_rank,
                        rerank_score=score,
                    ),
                    score,
                    reasons,
                )
            )
        penalized.sort(key=lambda item: (item[1], item[0].score), reverse=True)
        selected = [item[0] for item in penalized[:top_k]]
        selected_penalized = [item for item in penalized[:top_k] if item[2]]
        return selected, {
            "applied": True,
            "wrong_product_ids": sorted(wrong_products),
            "wrong_aspects": sorted(wrong_aspects),
            "penalized_count": sum(1 for _, _, reasons in penalized if reasons),
            "hard_negative_hit_rate": round(len(selected_penalized) / max(len(selected), 1), 4),
            "selected_penalized": [
                {
                    "doc_id": f"{item[0].chunk.source}:{item[0].chunk.doc_id}",
                    "product_id": str(item[0].chunk.metadata.get("product_id", "")),
                    "reasons": item[2],
                }
                for item in selected_penalized
            ],
        }

    def _product_constraints_from_query(self, query: str) -> set[str]:
        constraints: set[str] = set()
        match = re.search(r"structured facts:.*?products\s+([^;]+)", query, flags=re.IGNORECASE)
        if not match:
            return constraints
        for token in match.group(1).split():
            value = token.strip(" ,.;")
            if value:
                constraints.add(value)
        return constraints

    def _execute_semantic_memory(
        self,
        recorder: TraceRecorder,
        effective_query: str,
        memory_source_defaults: list[str],
        state: AgentState,
        *,
        attempt: int,
        agent_plan: dict[str, Any],
        parent_span_id: str | None = None,
    ) -> None:
        memory_request = agent_plan.get("memory_request") if isinstance(agent_plan.get("memory_request"), dict) else {}
        requested_query = str(memory_request.get("query") or effective_query)
        requested_sources = _valid_sources(memory_request.get("sources") or memory_source_defaults)
        top_k = max(1, min(int(_safe_float(memory_request.get("top_k"), default=6.0)), 10))
        retrieval_query = self._tool_constrained_query(requested_query, state.tool_results)
        memory_call = ToolCall(
            SEMANTIC_MEMORY_TOOL,
            {
                "query": retrieval_query,
                "sources": requested_sources,
                "top_k": top_k,
                "candidate_k": 30,
                "reason": memory_request.get("reason") or "semantic memory requested by agent plan",
            },
            str(memory_request.get("reason") or "semantic memory requested by agent plan"),
        )
        memory_span = recorder.start_span(
            "memory.semantic_retrieve",
            kind="memory",
            parent_id=parent_span_id or recorder.root_span_id,
            attempt=attempt,
            inputs={
                "query": retrieval_query,
                "sources": requested_sources,
                "top_k": top_k,
                "reason": memory_request.get("reason"),
            },
        )
        retrieval_span = recorder.start_span(
            f"retrieval.attempt_{attempt}",
            kind="retrieval",
            parent_id=memory_span,
            attempt=attempt,
            inputs={
                "tool_name": SEMANTIC_MEMORY_TOOL,
                "query": retrieval_query,
                "original_attempt_query": effective_query,
                "memory_request": memory_request,
                "sources": requested_sources,
                "top_k": top_k,
                "candidate_k": 30,
                "tool_constraints": self._tool_constraints(state.tool_results),
            },
        )
        retrieve_started = time.perf_counter()
        self._last_semantic_memory_results = []
        self._last_semantic_memory_diagnostics = {}
        self._active_retrieval_intent = state.intent
        self._active_eval_context = state.eval_context
        try:
            memory_tool_results = self.tool_executor.run(
                [memory_call],
                query=effective_query,
                intent=state.intent,
                domain=state.domain,
                risk_level=state.risk_level,
            )
        finally:
            self._active_retrieval_intent = "unknown"
            self._active_eval_context = {}
        memory_tool_result = memory_tool_results[0]
        state.retrieved_contexts = list(self._last_semantic_memory_results) if memory_tool_result.found else []
        retrieval_ms = int((time.perf_counter() - retrieve_started) * 1000)
        retrieval_diagnostics = self._last_semantic_memory_diagnostics
        plan_diagnostics = retrieval_diagnostics.get("retrieval_plan", {}) if isinstance(retrieval_diagnostics, dict) else {}
        entity_diagnostics = retrieval_diagnostics.get("entity_retrieval", {}) if isinstance(retrieval_diagnostics, dict) else {}
        hard_negative_diagnostics = retrieval_diagnostics.get("hard_negative_rerank", {}) if isinstance(retrieval_diagnostics, dict) else {}
        state.structured_retrieval_plan = dict(plan_diagnostics)
        state.entity_retrieval = dict(entity_diagnostics)
        state.entity_candidates = list(entity_diagnostics.get("entity_candidates", []))
        state.selected_entity = entity_diagnostics.get("selected_entity")
        before_filter_count = len(state.retrieved_contexts)
        state.retrieved_contexts = self._filter_contexts(state.query, state.retrieved_contexts)
        output = {
            "memory_type": "semantic_long_term",
            "returned_contexts": before_filter_count,
            "post_category_filter_contexts": len(state.retrieved_contexts),
            "selected_context_ids": [self._context_id(result) for result in state.retrieved_contexts],
            "doc_citations": [self._citation(result) for result in state.retrieved_contexts[:top_k]],
            "retrieval_plan": plan_diagnostics,
            "entity_retrieval": entity_diagnostics,
            "hard_negative_rerank": hard_negative_diagnostics,
            "diagnostic_stages": retrieval_diagnostics.get("stages", []),
            "candidate_count": len(retrieval_diagnostics.get("candidates", [])),
            "policy_decision": memory_tool_result.policy_decision,
            "tool_error": memory_tool_result.error,
        }
        self._record_retrieval_diagnostics(recorder, retrieval_span, attempt, retrieval_diagnostics)
        recorder.add_artifact(
            retrieval_span,
            "retrieved_contexts",
            [self._result_trace(result) for result in state.retrieved_contexts],
            metadata={"attempt": attempt, "memory_type": "semantic_long_term"},
        )
        recorder.end_span(
            retrieval_span,
            outputs=output,
            metrics={"latency_ms": retrieval_ms, "candidate_count": output["candidate_count"]},
        )
        recorder.end_span(
            memory_span,
            outputs=output,
            metrics={"latency_ms": retrieval_ms, "candidate_count": output["candidate_count"]},
        )
        memory_read = {
            "tool_name": SEMANTIC_MEMORY_TOOL,
            "memory_type": "semantic_long_term",
            "input": memory_call.input,
            "output": output,
            "found": bool(state.retrieved_contexts),
            "latency_ms": retrieval_ms,
            "policy_decision": memory_tool_result.policy_decision,
            "evidence_id": memory_tool_result.evidence_id,
        }
        state.memory_reads.append(memory_read)
        state.skipped_memory_reason = None
        state.trace.append(
            {
                "event": "memory_semantic_retrieve",
                "timestamp": utc_now(),
                "attempt": attempt,
                **memory_read,
                "top_contexts": [self._result_trace(r) for r in state.retrieved_contexts[:10]],
            }
        )
        state.trace.append(
            {
                "event": "retrieve",
                "timestamp": utc_now(),
                "attempt": attempt,
                "effective_query": effective_query,
                "retrieval_query": retrieval_query,
                "tool_constraints": self._tool_constraints(state.tool_results),
                "sources": requested_sources,
                "latency_ms": retrieval_ms,
                "returned_contexts": before_filter_count,
                "post_category_filter_contexts": len(state.retrieved_contexts),
                "diagnostic_stages": retrieval_diagnostics.get("stages", []),
                "candidate_count": len(retrieval_diagnostics.get("candidates", [])),
                "structured_retrieval_plan": plan_diagnostics,
                "entity_retrieval": entity_diagnostics,
                "hard_negative_rerank": hard_negative_diagnostics,
                "top_contexts": [self._result_trace(r) for r in state.retrieved_contexts[:10]],
            }
        )

    def _tool_trace_summary(self, tool_results: dict[str, Any]) -> dict[str, Any]:
        return {
            "backend": tool_results.get("backend"),
            "product_count": len(tool_results.get("products", [])),
            "order_count": len(tool_results.get("orders", [])),
            "order_item_count": len(tool_results.get("order_items", [])),
            "mentioned_skus": tool_results.get("mentioned_skus", []),
            "missing_skus": tool_results.get("missing_skus", []),
            "mentioned_order_ids": tool_results.get("mentioned_order_ids", []),
            "missing_order_ids": tool_results.get("missing_order_ids", []),
            "tool_call_count": len(tool_results.get("tool_calls", [])),
            "return_eligibility_count": len(tool_results.get("return_eligibility", [])),
            "review_summary_count": len(tool_results.get("review_summaries", [])),
            "similar_case_count": len(tool_results.get("similar_cases", [])),
        }

    def _tool_call_trace(self, tool_results: dict[str, Any]) -> list[dict[str, Any]]:
        return tool_results.get("tool_calls", [])

    def _tool_citation_ids(self, tool_results: dict[str, Any]) -> list[str]:
        cited_tools = {
            "sql.product_by_sku",
            "sql.product_by_id",
            "sql.inventory_by_sku",
            "sql.order_by_id",
            "sql.order_items_by_order_id",
            "policy.return_eligibility",
            "review.aspect_summary",
        }
        citations = []
        for call in tool_results.get("tool_calls", []):
            if call.get("tool_name") not in cited_tools:
                continue
            if not call.get("found"):
                continue
            evidence_id = call.get("evidence_id")
            if evidence_id and evidence_id not in citations:
                citations.append(evidence_id)
        for product in tool_results.get("context_inferred_products", []):
            citation = f"[tool:context.retrieved_product:{product.get('product_id')}]"
            if product.get("product_id") and citation not in citations:
                citations.append(citation)
        return citations

    def _tool_constraints(self, tool_results: dict[str, Any]) -> dict[str, Any]:
        product_ids = sorted({str(product.get("product_id")) for product in tool_results.get("products", []) if product.get("product_id")})
        skus = sorted({str(product.get("sku")) for product in tool_results.get("products", []) if product.get("sku")})
        order_ids = sorted({str(order.get("order_id")) for order in tool_results.get("orders", []) if order.get("order_id")})
        order_product_ids = sorted({str(order.get("product_id")) for order in tool_results.get("orders", []) if order.get("product_id")})
        order_skus = sorted({str(order.get("sku")) for order in tool_results.get("orders", []) if order.get("sku")})
        item_product_ids = sorted({str(item.get("product_id")) for item in tool_results.get("order_items", []) if item.get("product_id")})
        item_skus = sorted({str(item.get("sku")) for item in tool_results.get("order_items", []) if item.get("sku")})
        return {
            "product_ids": sorted(set(product_ids + order_product_ids + item_product_ids)),
            "skus": sorted(set(skus + order_skus + item_skus)),
            "order_ids": order_ids,
        }

    def _tool_constrained_query(self, query: str, tool_results: dict[str, Any]) -> str:
        constraints = self._tool_constraints(tool_results)
        terms = []
        if constraints["order_ids"]:
            terms.append("orders " + " ".join(constraints["order_ids"]))
        if constraints["product_ids"]:
            terms.append("products " + " ".join(constraints["product_ids"]))
        if constraints["skus"]:
            terms.append("sku " + " ".join(constraints["skus"]))
        if not terms:
            return query
        return f"{query} structured facts: {'; '.join(terms)}"

    def _query_order_ids(self, query: str) -> set[str]:
        return self.root_router.query_order_ids(query)

    def _query_skus(self, query: str) -> set[str]:
        return self.root_router.query_skus(query)

    def _category_hint(self, query: str) -> str | None:
        return category_hint_for_query(query)

    def _matches_category(self, product: Product, category_hint: str | None) -> bool:
        return category_hint is None or product.category == category_hint

    def _product_by_id(self, product_id: str) -> Product | None:
        if self.sql_store:
            return self.sql_store.product_by_id(product_id)
        return self.products.get(product_id)

    def _product_by_sku(self, sku: str) -> Product | None:
        if self.sql_store:
            return self.sql_store.product_by_sku(sku)
        return self.products_by_sku.get(sku.lower())

    def _filter_contexts(self, query: str, results: list[SearchResult]) -> list[SearchResult]:
        category_hint = self._category_hint(query)
        if category_hint is None:
            return results
        filtered: list[SearchResult] = []
        for result in results:
            product_id = result.chunk.metadata.get("product_id")
            if not product_id:
                filtered.append(result)
                continue
            product = self.products.get(product_id)
            metadata_category = str(result.chunk.metadata.get("category", "")).strip()
            if product and self._matches_category(product, category_hint):
                filtered.append(result)
            elif not product and metadata_category == category_hint:
                filtered.append(result)
        return filtered or results

    def _filter_contexts_by_structured_entities(self, state: AgentState) -> list[SearchResult]:
        if state.intent != "sku_order":
            return state.retrieved_contexts
        if state.tool_results.get("missing_order_ids") or state.tool_results.get("missing_skus"):
            return state.retrieved_contexts
        explicit_entity = bool(state.tool_results.get("mentioned_order_ids") or state.tool_results.get("mentioned_skus"))
        if not explicit_entity:
            return state.retrieved_contexts
        product_ids = {
            str(product.get("product_id", "")).strip()
            for product in state.tool_results.get("products", [])
            if product.get("product_id")
        }
        product_ids.update(
            str(order.get("product_id", "")).strip()
            for order in state.tool_results.get("orders", [])
            if order.get("product_id")
        )
        product_ids.update(
            str(item.get("product_id", "")).strip()
            for item in state.tool_results.get("order_items", [])
            if item.get("product_id")
        )
        if not product_ids:
            return state.retrieved_contexts
        filtered: list[SearchResult] = []
        removed_contexts: list[dict[str, Any]] = []
        for result in state.retrieved_contexts:
            product_id = str(result.chunk.metadata.get("product_id", "")).strip()
            if not product_id or product_id in product_ids:
                filtered.append(result)
            else:
                removed_contexts.append({**self._result_trace(result), "reason": "conflicting_product_id"})
        if removed_contexts and filtered:
            state.trace.append(
                {
                    "event": "structured_context_filter",
                    "timestamp": utc_now(),
                    "product_ids": sorted(product_ids),
                    "removed": len(removed_contexts),
                    "removed_contexts": removed_contexts,
                    "remaining": len(filtered),
                }
            )
            return filtered
        return state.retrieved_contexts

    def _infer_product_from_retrieved_context(self, state: AgentState, *, attempt: int) -> None:
        if state.intent != "sku_order":
            return
        if state.tool_results.get("missing_order_ids") or state.tool_results.get("missing_skus"):
            return
        if state.tool_results.get("products") or state.tool_results.get("orders"):
            return
        product_ids = {
            str(result.chunk.metadata.get("product_id", "")).strip()
            for result in state.retrieved_contexts
            if result.chunk.source == "product" or result.chunk.metadata.get("doc_type") == "product_profile"
        }
        product_ids.discard("")
        if len(product_ids) != 1:
            return
        product_id = next(iter(product_ids))
        product = self._product_by_id(product_id)
        if not product:
            return
        inferred_product = {
            "product_id": product.product_id,
            "sku": product.sku,
            "title": product.title,
            "category": product.category,
            "price": product.price,
            "stock": product.stock,
            "average_rating": product.average_rating,
            "inference_source": "retrieved_product_context",
        }
        state.tool_results.setdefault("products", []).append(inferred_product)
        state.tool_results.setdefault("context_inferred_products", []).append(inferred_product)
        state.trace.append(
            _event(
                "structured_entity_infer",
                attempt=attempt,
                inference_source="retrieved_product_context",
                product_id=product.product_id,
                sku=product.sku,
                reason="single_product_profile_context_without_explicit_entity",
            )
        )

    def _support_answer(self, state: AgentState, citations: list[str]) -> str:
        evidence = " ".join(r.chunk.text for r in state.retrieved_contexts[:3])
        if "refund" in normalize_text(state.query) or "return" in normalize_text(state.query):
            summary = "The return/refund path depends on the return window, item condition, and proof of purchase."
        elif "warranty" in normalize_text(state.query):
            summary = "Warranty cases require product identification, purchase proof, and a defect description."
        elif "shipping" in normalize_text(state.query) or "delivery" in normalize_text(state.query):
            summary = "Shipping issues should be checked against the shipping policy and the latest carrier status."
        else:
            summary = "The safest support response is to answer from the matching policy and similar ticket history."
        return f"{summary} Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite {', '.join(citations)}. Evidence summary: {evidence[:360]}"

    def _recommendation_answer(self, state: AgentState, citations: list[str]) -> str:
        products = state.tool_results.get("products", [])
        if products:
            product_lines = [
                f"{p['title']} ({p['sku']}) at ${p['price']}, rating {p['average_rating']}, stock {p['stock']}"
                for p in products[:3]
            ]
            return "Recommended options: " + "; ".join(product_lines) + f". I used product/review evidence from {', '.join(citations)}."
        contexts = "; ".join(r.chunk.text[:150] for r in state.retrieved_contexts[:3])
        return f"I found matching product and review evidence: {contexts}. Citations: {', '.join(citations)}."

    def _customer_ops_answer(self, state: AgentState, citations: list[str]) -> str:
        negative = [r for r in state.retrieved_contexts if "rating" in r.chunk.metadata and int(r.chunk.metadata["rating"]) <= 2]
        if negative:
            signals = "; ".join(r.chunk.text[:160] for r in negative[:3])
            return f"Customer ops signals show recurring low-rating issues: {signals}. Suggested action: inspect product quality, shipping promises, and post-purchase messaging. Citations: {', '.join(citations)}."
        signals = "; ".join(r.chunk.text[:180] for r in state.retrieved_contexts[:3])
        return f"Customer ops summary should focus on repeated review/ticket themes: {signals}. Citations: {', '.join(citations)}."

    def _sku_answer(self, state: AgentState, citations: list[str]) -> str:
        products = state.tool_results.get("products", [])
        if not products:
            return f"I could not find a matching SKU in the structured product tool. Related policy/product evidence: {', '.join(citations)}."
        p = products[0]
        return f"SKU {p['sku']} maps to {p['title']}. Current demo inventory is {p['stock']} units at ${p['price']}. Supporting context: {', '.join(citations)}."

    def _grade(self, state: AgentState) -> dict[str, float]:
        top_score = max((r.rerank_score or 0.0 for r in state.retrieved_contexts), default=0.0)
        citation_rate = 1.0 if state.citations else 0.0
        groundedness = min(1.0, top_score / max(self.score_threshold * 3, 0.01))
        relevance = min(1.0, top_score / max(self.score_threshold * 2, 0.01))
        return {
            "top_rerank_score": round(top_score, 4),
            "citation_rate": citation_rate,
            "groundedness_proxy": round(groundedness, 4),
            "relevance_proxy": round(relevance, 4),
        }

    def _decide_action(self, state: AgentState, attempt: int, max_retries: int, evidence_gaps: list[str]):
        verification = self.critic.verify(
            domain=state.domain,
            evidence_pack=self.evidence_builder.build_from_agent_state(state, missing_requirements=evidence_gaps),
            evidence_gaps=evidence_gaps,
            citation_validation={},
            tool_citation_validation={},
        )
        return self.critic.decide_action(
            verification,
            intent=state.intent,
            risk_level=state.risk_level,
            citations=state.citations,
            grader_scores=state.grader_scores,
            weak_retrieval=self._weak_retrieval(state),
            tool_evidence_satisfies=self.gap_analyzer.tool_evidence_satisfies_intent(state),
            attempt=attempt,
            max_retries=max_retries,
        )

    def _weak_retrieval(self, state: AgentState) -> bool:
        if self._tool_evidence_satisfies_intent(state) and not state.retrieved_contexts:
            return False
        top_score = max((r.rerank_score or 0.0 for r in state.retrieved_contexts), default=0.0)
        return top_score < self.score_threshold

    def _must_doc_cite(self, state: AgentState) -> bool:
        if state.action in {"refuse", "clarify"}:
            return False
        return bool(state.retrieved_contexts) and not self._weak_retrieval(state)

    def _should_clarify_missing_entity(self, state: AgentState, evidence_gaps: list[str]) -> bool:
        if state.entity_retrieval.get("should_clarify") and state.selected_entity is None:
            return True
        if not _query_has_unbound_reference(state.query):
            return False
        if self._query_order_ids(state.query) or self._query_skus(state.query):
            return False
        if _query_has_product_id(state.query):
            return False
        if _has_unique_memory_entity(state):
            return False
        return True

    def _clarification_answer(self, state: AgentState) -> str:
        if "order" in tokenize(state.query) or state.intent == "sku_order":
            return "Please provide the order ID, SKU, or product name so I can look up the right item before answering."
        return "Please provide the product name, SKU, or order ID so I can answer about the correct item."

    def _evidence_gaps(self, state: AgentState) -> list[str]:
        return self.gap_analyzer.gaps(state)

    def _tool_evidence_satisfies_intent(self, state: AgentState) -> bool:
        return self.gap_analyzer.tool_evidence_satisfies_intent(state)

    def _safety_gaps(self, query: str) -> list[str]:
        return self.gap_analyzer.safety_gaps(query)

    def _fallback_sources(self, intent: str, evidence_gaps: list[str]) -> list[str]:
        if intent == "support":
            sources = ["kb", "ticket"]
            if "missing_case_evidence" in evidence_gaps:
                sources.append("review")
            if "missing_product_context" in evidence_gaps:
                sources.append("product")
            return sources
        if intent == "recommendation":
            return ["product", "review"]
        if intent == "customer_ops":
            return ["review", "ticket", "product"]
        if intent == "sku_order":
            return ["product", "kb", "ticket"]
        return ["kb", "ticket", "product", "review"]

    def _enhance_query(self, query: str, state: AgentState, evidence_gaps: list[str] | None = None) -> str:
        gap_terms = {
            "no_context": "exact product policy review case",
            "missing_policy": "policy return refund warranty shipping delivery",
            "missing_case_evidence": "customer query resolution faq case review evidence",
            "missing_product": "product profile sku title features",
            "missing_review": "verified review rating customer feedback",
            "missing_customer_voice": "negative review complaint aspect cluster summary",
            "missing_structured_entity": "sku order status inventory price",
            "missing_product_context": "product profile sku title features",
        }
        extra_terms = " ".join(gap_terms[gap] for gap in evidence_gaps or [] if gap in gap_terms)
        if state.intent == "support":
            return f"{query} policy customer query resolution refund return warranty shipping {extra_terms}".strip()
        if state.intent == "recommendation":
            return f"{query} product features rating verified review best for {extra_terms}".strip()
        if state.intent == "customer_ops":
            return f"{query} negative review complaint broken delivery refund quality {extra_terms}".strip()
        return f"{query} product policy support review {extra_terms}".strip()

    def _decision_reason(self, state: AgentState, attempt: int, max_retries: int, evidence_gaps: list[str]) -> str:
        if state.action == "retry":
            return f"repair because evidence_gaps={evidence_gaps} and repair_round {attempt} < max_repair_rounds {max_retries}"
        if state.action == "refuse":
            if state.intent == "unknown" or "unknown_intent" in evidence_gaps:
                return "refuse because intent is unknown or outside supported ecommerce scope"
            if self._weak_retrieval(state):
                return "refuse because retrieval remained below confidence threshold after retries"
            return f"refuse because critical evidence gaps remained: {evidence_gaps}"
        if state.action == "clarify":
            return "clarify because the query contains an unbound reference and no unique product, SKU, or order is available"
        if state.action == "escalate":
            return "escalate because high-risk support answer lacks required grounded policy evidence"
        return "answer because required evidence contract is satisfied"

    def _trace_config(self, max_retries: int) -> dict[str, Any]:
        reranker = getattr(self.retriever, "reranker", None)
        embedding_model = getattr(getattr(self.retriever, "embedding_model", None), "name", None)
        return {
            "agent": self.__class__.__name__,
            "retriever": self.retriever.__class__.__name__,
            "generator": self.generator.__class__.__name__,
            "score_threshold": self.score_threshold,
            "max_retries": max_retries,
            "repair_budget_mode": "critic_replanner_budget",
            "max_repair_rounds": max(0, int(max_retries)),
            "embedding_model": embedding_model,
            "reranker_model": getattr(reranker, "model_name", None),
        }

    def _dataset_manifest(self) -> dict[str, Any]:
        chunks_path = self.data_dir / "processed" / "chunks.jsonl"
        db_path = default_db_path(self.data_dir)
        return {
            "data_dir": str(self.data_dir),
            "products": len(self.products),
            "tickets": len(self.tickets),
            "orders": len(self.orders),
            "chunks_path": str(chunks_path),
            "chunks_mtime": int(chunks_path.stat().st_mtime) if chunks_path.exists() else None,
            "sqlite_path": str(db_path),
            "sqlite_mtime": int(db_path.stat().st_mtime) if db_path.exists() else None,
        }

    def _record_retrieval_diagnostics(
        self,
        recorder: TraceRecorder,
        parent_span_id: str,
        attempt: int,
        diagnostics: dict[str, Any],
    ) -> None:
        for stage in diagnostics.get("stages", []):
            span_id = recorder.start_span(
                stage.get("name", "retrieval.stage"),
                kind=_span_kind_for_stage(stage.get("name", "")),
                parent_id=parent_span_id,
                attempt=attempt,
            )
            recorder.end_span(span_id, metrics=stage)
        candidates = diagnostics.get("candidates", [])
        if candidates:
            recorder.add_retrieval_candidates(parent_span_id, attempt, candidates)
            recorder.add_artifact(
                parent_span_id,
                f"retrieval_candidates_attempt_{attempt}",
                candidates,
                metadata={"attempt": attempt, "count": len(candidates)},
            )

    def _citation(self, result: SearchResult) -> str:
        return f"[doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}]"

    def _context_id(self, result: SearchResult) -> str:
        return f"doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}"

    def _result_trace(self, result: SearchResult) -> dict[str, Any]:
        return {
            "source": result.chunk.source,
            "doc_id": result.chunk.doc_id,
            "chunk_id": result.chunk.chunk_id,
            "doc_type": result.chunk.metadata.get("doc_type") or result.chunk.metadata.get("document_type") or result.chunk.source,
            "content_hash": _content_hash(result.chunk.text),
            "preview": result.chunk.text[:160],
            "score": round(result.score, 4),
            "rerank_score": round(result.rerank_score or 0.0, 4),
        }


def _event(event: str, **payload: Any) -> dict[str, Any]:
    return {"event": event, "timestamp": utc_now(), **payload}


def _tool_call_proposer(call: ToolCall) -> str:
    if call.reason.startswith("llm_advisor:"):
        return "llm_agent_plan"
    if call.reason.startswith("agent_plan"):
        return "agent_plan"
    return "heuristic_tool_suggester"


def _default_memory_sources_reason(intent: str) -> str:
    reasons = {
        "support": "support intent requires policy and support case evidence",
        "recommendation": "recommendation intent requires product profile and review evidence",
        "customer_ops": "customer ops intent requires customer voice from reviews and tickets",
        "sku_order": "sku/order intent requires structured product facts plus policy context",
        "unknown": "unknown intent searches broad sources before refusing if evidence remains weak",
    }
    return reasons.get(intent, "default broad retrieval plan")


def _span_kind_for_stage(stage_name: str) -> str:
    if "dense" in stage_name or "bm25" in stage_name:
        return "retrieval"
    if "rrf" in stage_name:
        return "fusion"
    if "rerank" in stage_name:
        return "rerank"
    if "diversify" in stage_name or "forced" in stage_name:
        return "filter"
    return "retrieval"


def _query_has_unbound_reference(query: str) -> bool:
    q = f" {normalize_text(query).lower()} "
    patterns = [
        r"\bthis\s+(?:item|product|app|baby item|beauty item|digital purchase|nap mat)\b",
        r"\bthat\s+(?:item|product|app|thing)\b",
        r"\bthe\s+item\b",
        r"\bsame\s+product\b",
        r"\bproduct\s+we\s+discussed\s+earlier\b",
        r"\bcomplaints\s+about\s+it\b",
    ]
    return any(re.search(pattern, q) for pattern in patterns)


def _query_has_product_id(query: str) -> bool:
    return bool(re.search(r"\bB[0-9A-Z]{9}\b|\bP-[A-Z]+-\d+\b", query, flags=re.IGNORECASE))


def _has_unique_memory_entity(state: AgentState) -> bool:
    entities: set[tuple[str, str]] = set()
    for item in state.resolved_entities:
        entity_type = str(item.get("entity_type") or item.get("type") or "")
        entity_value = str(item.get("entity_value") or item.get("value") or "")
        if entity_type in {"product_id", "sku", "order_id"} and entity_value:
            entities.add((entity_type, entity_value))
    active = state.memory_context.get("active_entities", {})
    if isinstance(active, dict):
        for entity_type in ["product_id", "sku", "order_id"]:
            value = active.get(entity_type)
            if isinstance(value, str) and value.strip():
                entities.add((entity_type, value.strip()))
    return len({value for _, value in entities}) == 1


def _has_unique_structured_entity(state: AgentState) -> bool:
    product_ids = {
        str(product.get("product_id", "")).strip()
        for product in state.tool_results.get("products", [])
        if product.get("product_id")
    }
    product_ids.update(
        str(order.get("product_id", "")).strip()
        for order in state.tool_results.get("orders", [])
        if order.get("product_id")
    )
    order_ids = {
        str(order.get("order_id", "")).strip()
        for order in state.tool_results.get("orders", [])
        if order.get("order_id")
    }
    return len(product_ids | order_ids) == 1


def _result_aspects(result: SearchResult) -> set[str]:
    aspects: set[str] = set()
    aspect = str(result.chunk.metadata.get("aspect", "")).lower().strip()
    if aspect:
        aspects.add(aspect)
    raw_aspects = result.chunk.metadata.get("aspects", [])
    if isinstance(raw_aspects, list):
        aspects.update(str(item).lower().strip() for item in raw_aspects if str(item).strip())
    return aspects


def _content_hash(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


def _safe_float(value: Any, *, default: float) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _dedupe_tool_calls(calls: list[ToolCall]) -> list[ToolCall]:
    seen = set()
    output = []
    for call in calls:
        key = (call.tool_name, json.dumps(call.input, ensure_ascii=False, sort_keys=True, default=str))
        if key in seen:
            continue
        seen.add(key)
        output.append(call)
    return _prefer_specific_write_calls(output)


def _prefer_specific_write_calls(calls: list[ToolCall]) -> list[ToolCall]:
    specific_refund_drafts = [
        call
        for call in calls
        if call.tool_name == "ops.refund_request_draft"
        and any(key in call.input for key in ["order_id", "refund_amount", "amount", "credit_amount"])
    ]
    if not specific_refund_drafts:
        return calls
    output = []
    for call in calls:
        if call.tool_name == "ops.refund_request_draft" and call not in specific_refund_drafts:
            continue
        output.append(call)
    return sorted(output, key=lambda call: 0 if call in specific_refund_drafts else 1)


def _valid_sources(value: Any) -> list[str]:
    allowed = {"kb", "ticket", "product", "review"}
    if isinstance(value, str):
        candidates = [value]
    elif isinstance(value, list):
        candidates = value
    else:
        candidates = []
    sources = [str(source) for source in candidates if str(source) in allowed]
    return sources or ["kb", "ticket", "product", "review"]


def _compact_memory_context(memory_context: dict[str, Any]) -> dict[str, Any]:
    return {
        "conversation_id": memory_context.get("conversation_id"),
        "user_id": memory_context.get("user_id"),
        "active_entities": memory_context.get("active_entities", {}),
        "active_entity_records": memory_context.get("active_entity_records", {}),
        "resolved_entities": memory_context.get("resolved_entities", []),
        "context_resolution": memory_context.get("context_resolution", {}),
        "recent_turn_count": len(memory_context.get("recent_turns", [])),
        "ambiguous_entity_types": memory_context.get("ambiguous_entity_types", []),
    }


def _runtime_state_payload(state: RunState) -> dict[str, Any]:
    return {
        "run_id": state.run_id,
        "conversation_id": state.conversation_id,
        "domain": state.domain,
        "risk_level": state.risk_level,
        "context_resolution": state.context_resolution,
        "budgets": {
            "max_steps": state.budgets.max_steps,
            "max_tool_calls": state.budgets.max_tool_calls,
            "max_retrieval_calls": state.budgets.max_retrieval_calls,
            "max_write_tool_drafts": state.budgets.max_write_tool_drafts,
            "steps_used": state.budgets.steps_used,
            "tool_calls_used": state.budgets.tool_calls_used,
            "retrieval_calls_used": state.budgets.retrieval_calls_used,
            "write_tool_drafts_used": state.budgets.write_tool_drafts_used,
        },
        "steps": [
            {
                "action_type": record.step.action_type,
                "tool_name": record.step.tool_name,
                "tool_input": record.step.tool_input,
                "reason_summary": record.step.reason_summary,
                "expected_evidence": record.step.expected_evidence,
                "proposed_by": record.step.proposed_by,
                "accepted": record.step.accepted,
                "status": record.status,
                "observation_id": record.observation_id,
                "rejected_reason": record.rejected_reason,
            }
            for record in state.steps
        ],
        "observations": [
            {
                "source": observation.source,
                "kind": observation.kind,
                "status": observation.status,
                "payload": observation.payload,
                "citations": observation.citations,
                "structured_entities": observation.structured_entities,
            }
            for observation in state.observations
        ],
        "final_action": state.final_action,
    }


def _first_repair_memory_step(repair_plan: dict[str, Any]) -> dict[str, Any]:
    for step in repair_plan.get("steps", []) if isinstance(repair_plan, dict) else []:
        if step.get("tool_name") == SEMANTIC_MEMORY_TOOL:
            return step
    return {}


def answer_contains_keywords(answer: str, expected_keywords: list[str]) -> float:
    return keyword_coverage(answer, expected_keywords)
