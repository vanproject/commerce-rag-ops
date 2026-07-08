from __future__ import annotations

from ..models import AgentState
from ..runtime import AgentStep
from .base import DomainAgent, DomainPlan, EvidenceContract


class SupportAgent(DomainAgent):
    name = "support"
    allowed_tools = [
        "sql.order_by_id",
        "sql.order_items_by_order_id",
        "sql.product_by_sku",
        "sql.product_search",
        "policy.return_eligibility",
        "ticket.similar_cases",
        "memory.semantic_retrieve",
        "ops.escalate_ticket",
        "ops.refund_request_draft",
    ]
    evidence_contract = EvidenceContract(required=["policy_or_clear_ineligibility"], preferred=["ticket_or_review_case"])

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        return DomainPlan(
            goal="Resolve support request with structured facts and policy/case evidence",
            actions=["call_tools", "retrieve_memory", "decide_action"],
            steps=[
                AgentStep("tool_call", reason_summary="confirm structured order/product/support facts"),
                AgentStep(
                    "tool_call",
                    tool_name="memory.semantic_retrieve",
                    tool_input={"query": query, "sources": sources or ["kb", "ticket"], "top_k": 6},
                    reason_summary="retrieve policy and support-case semantic memory",
                    expected_evidence=["policy", "ticket_or_review_case"],
                ),
            ],
            memory_request={
                "query": query,
                "sources": sources or ["kb", "ticket"],
                "top_k": 6,
                "reason": "support domain requires policy and support-case semantic memory",
            },
        )


class RecommendationAgent(DomainAgent):
    name = "recommendation"
    allowed_tools = ["sql.product_search", "sql.product_by_sku", "review.aspect_summary", "memory.semantic_retrieve"]
    evidence_contract = EvidenceContract(required=["product"], preferred=["review"])

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        return DomainPlan(
            goal="Recommend products using product facts and review evidence",
            actions=["call_tools", "retrieve_memory", "decide_action"],
            steps=[
                AgentStep("tool_call", reason_summary="find candidate products and review summaries"),
                AgentStep("tool_call", tool_name="memory.semantic_retrieve", tool_input={"query": query, "sources": sources or ["product", "review"], "top_k": 6}, reason_summary="retrieve product/review semantic memory"),
            ],
            memory_request={"query": query, "sources": sources or ["product", "review"], "top_k": 6, "reason": "recommendation requires product and review semantic memory"},
        )


class CustomerOpsAgent(DomainAgent):
    name = "customer_ops"
    allowed_tools = ["sql.product_search", "review.aspect_summary", "ticket.similar_cases", "memory.semantic_retrieve"]
    evidence_contract = EvidenceContract(required=["customer_voice"], preferred=["ticket_case"])

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        return DomainPlan(
            goal="Summarize customer voice from review/ticket evidence",
            actions=["call_tools", "retrieve_memory", "decide_action"],
            steps=[
                AgentStep("tool_call", reason_summary="get aspect summary and similar tickets"),
                AgentStep("tool_call", tool_name="memory.semantic_retrieve", tool_input={"query": query, "sources": sources or ["review", "ticket", "product"], "top_k": 6}, reason_summary="retrieve customer-voice semantic memory"),
            ],
            memory_request={"query": query, "sources": sources or ["review", "ticket", "product"], "top_k": 6, "reason": "customer ops requires customer voice semantic memory"},
        )


class OrderAgent(DomainAgent):
    name = "order"
    allowed_tools = [
        "sql.order_by_id",
        "sql.order_items_by_order_id",
        "sql.product_by_sku",
        "sql.product_by_id",
        "sql.inventory_by_sku",
        "memory.semantic_retrieve",
    ]
    evidence_contract = EvidenceContract(required=["structured_order_or_product_fact"])

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        has_structured_reference = bool(
            state.resolved_entities
            or state.tool_results.get("orders")
            or state.tool_results.get("products")
            or "ord-" in query.lower()
            or any(token in query.lower() for token in ["sku ", "sku-", "soft-", "baby-", "beauty-"])
        )
        needs_policy_context = any(term in query.lower() for term in ["policy", "refund", "return", "warranty", "delivery context", "shipping context"])
        if needs_policy_context or not has_structured_reference:
            return DomainPlan(
                goal="Answer order/SKU question with structured facts plus policy context",
                actions=["call_tools", "retrieve_memory", "decide_action"],
                steps=[
                    AgentStep("tool_call", reason_summary="confirm order/SKU structured facts"),
                    AgentStep("tool_call", tool_name="memory.semantic_retrieve", tool_input={"query": query, "sources": sources or ["product", "kb", "ticket"], "top_k": 6}, reason_summary="retrieve optional policy/product semantic memory"),
                ],
                memory_request={"query": query, "sources": sources or ["product", "kb", "ticket"], "top_k": 6, "reason": "order question requested policy/product context"},
            )
        return DomainPlan(
            goal="Answer order/SKU question from structured tools",
            actions=["call_tools", "decide_action"],
            steps=[AgentStep("tool_call", reason_summary="structured tools are authoritative for order/SKU facts")],
            skip_memory_reason="structured_tools_sufficient_for_order_domain",
        )


class RefusalAgent(DomainAgent):
    name = "refusal"
    allowed_tools: list[str] = []
    evidence_contract = EvidenceContract(required=["safe_refusal"])

    def plan(self, query: str, state: AgentState, *, sources: list[str], evidence_gaps: list[str]) -> DomainPlan:
        return DomainPlan(
            goal="Refuse or ask for clarification without tool or memory access",
            actions=["decide_action"],
            steps=[AgentStep("refuse", reason_summary="safety boundary or unsupported intent")],
            skip_memory_reason="refusal_domain_does_not_use_semantic_memory",
        )


def default_domain_agents() -> dict[str, DomainAgent]:
    return {
        "support": SupportAgent(),
        "recommendation": RecommendationAgent(),
        "customer_ops": CustomerOpsAgent(),
        "order": OrderAgent(),
        "refusal": RefusalAgent(),
    }
