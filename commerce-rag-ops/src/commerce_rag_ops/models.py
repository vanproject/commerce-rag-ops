from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal


Intent = Literal["support", "recommendation", "customer_ops", "sku_order", "unknown"]
RiskLevel = Literal["low", "medium", "high"]
AgentAction = Literal["answer", "retry", "refuse", "escalate"]


@dataclass(frozen=True)
class Product:
    product_id: str
    sku: str
    title: str
    category: str
    price: float
    stock: int
    average_rating: float
    rating_number: int
    features: list[str]
    description: str


@dataclass(frozen=True)
class Review:
    review_id: str
    product_id: str
    rating: int
    text: str
    verified_purchase: bool
    timestamp: str


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    category: str
    product_id: str
    customer_query: str
    resolution: str
    status: str
    date: str
    expected_policy_doc: str


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_id: str
    product_id: str
    sku: str
    status: str
    delivery_status: str
    order_date: str
    total: float


@dataclass(frozen=True)
class OrderItem:
    order_id: str
    product_id: str
    sku: str
    quantity: int
    unit_price: float
    line_total: float


@dataclass(frozen=True)
class CustomerSegment:
    customer_id: str
    segment: str
    preferred_category: str
    lifetime_value: float
    churn_risk: str
    notes: str


@dataclass(frozen=True)
class DocumentChunk:
    chunk_id: str
    source: str
    doc_id: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class SearchResult:
    chunk: DocumentChunk
    score: float
    dense_rank: int | None = None
    bm25_rank: int | None = None
    rerank_score: float | None = None


@dataclass
class AgentState:
    query: str
    trace_id: str = ""
    original_query: str | None = None
    memory_context: dict[str, Any] = field(default_factory=dict)
    resolved_entities: list[dict[str, Any]] = field(default_factory=list)
    context_resolution: dict[str, Any] = field(default_factory=dict)
    llm_advice: dict[str, Any] = field(default_factory=dict)
    agent_plan: dict[str, Any] = field(default_factory=dict)
    memory_reads: list[dict[str, Any]] = field(default_factory=list)
    skipped_memory_reason: str | None = None
    domain: str = "refusal"
    route_decision: dict[str, Any] = field(default_factory=dict)
    runtime_state: dict[str, Any] = field(default_factory=dict)
    evidence_pack: dict[str, Any] = field(default_factory=dict)
    verification: dict[str, Any] = field(default_factory=dict)
    repair_plan: dict[str, Any] = field(default_factory=dict)
    intent: Intent = "unknown"
    risk_level: RiskLevel = "low"
    semantic_memory_source_defaults: list[str] = field(default_factory=list)
    # Deprecated compatibility mirror. The agent no longer treats this as a
    # control-plane retrieval plan; semantic memory is called through tools.
    retrieval_plan: list[str] = field(default_factory=list)
    retrieved_contexts: list[SearchResult] = field(default_factory=list)
    tool_results: dict[str, Any] = field(default_factory=dict)
    tool_citations: list[str] = field(default_factory=list)
    answer: str = ""
    citations: list[str] = field(default_factory=list)
    grader_scores: dict[str, float] = field(default_factory=dict)
    action: AgentAction = "answer"
    attempts: int = 0
    trace: list[dict[str, Any]] = field(default_factory=list)
    trace_run: dict[str, Any] = field(default_factory=dict)
    trace_spans: list[dict[str, Any]] = field(default_factory=list)
    trace_artifacts: list[dict[str, Any]] = field(default_factory=list)
    retrieval_candidates: list[dict[str, Any]] = field(default_factory=list)
