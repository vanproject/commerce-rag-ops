from __future__ import annotations

from typing import Any, Callable

from ..models import SearchResult
from .base import ToolSpec
from .registry import ToolRegistry


SemanticSearchFn = Callable[[str, list[str], int, int], tuple[list[SearchResult], dict[str, Any]]]


def register_semantic_memory_tool(registry: ToolRegistry, *, search_fn: SemanticSearchFn) -> None:
    registry.register(
        ToolSpec(
            name="memory.semantic_retrieve",
            description="Read-only semantic long-term memory retrieval over policy, product, review, and ticket chunks.",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"},
                    "sources": {"type": "array", "items": {"type": "string"}},
                    "top_k": {"type": "integer", "minimum": 1, "maximum": 10},
                    "candidate_k": {"type": "integer", "minimum": 5, "maximum": 100},
                    "reason": {"type": "string"},
                },
                "required": ["query"],
            },
            output_schema={
                "type": "object",
                "properties": {
                    "found": {"type": "boolean"},
                    "memory_type": {"type": "string"},
                    "contexts": {"type": "array"},
                    "doc_citations": {"type": "array", "items": {"type": "string"}},
                    "diagnostics": {"type": "object"},
                },
            },
            read_only=True,
            risk_level="medium",
            requires_confirmation=False,
            handler=lambda payload: _semantic_memory_handler(payload, search_fn),
            allowed_intents=["support", "recommendation", "customer_ops", "sku_order"],
            allowed_domains=["support", "recommendation", "customer_ops", "order"],
            max_rows=10,
        )
    )


def _semantic_memory_handler(payload: dict[str, Any], search_fn: SemanticSearchFn) -> dict[str, Any]:
    query = str(payload.get("query") or "").strip()
    sources = _valid_sources(payload.get("sources"))
    top_k = _bounded_int(payload.get("top_k"), default=6, minimum=1, maximum=10)
    candidate_k = _bounded_int(payload.get("candidate_k"), default=30, minimum=5, maximum=100)
    reason = str(payload.get("reason") or "agent_requested_semantic_memory")
    if not query:
        return {
            "found": False,
            "memory_type": "semantic_long_term",
            "contexts": [],
            "doc_citations": [],
            "diagnostics": {"error": "empty_query"},
            "reason": reason,
        }
    results, diagnostics = search_fn(query, sources, top_k, candidate_k)
    contexts = [_result_payload(result) for result in results[:top_k]]
    return {
        "found": bool(contexts),
        "memory_type": "semantic_long_term",
        "contexts": contexts,
        "doc_citations": [_citation(result) for result in results[:top_k]],
        "diagnostics": diagnostics,
        "reason": reason,
        "query": query,
        "sources": sources,
        "top_k": top_k,
        "candidate_k": candidate_k,
    }


def _result_payload(result: SearchResult) -> dict[str, Any]:
    metadata = result.chunk.metadata
    return {
        "context_id": f"doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}",
        "source": result.chunk.source,
        "doc_id": result.chunk.doc_id,
        "chunk_id": result.chunk.chunk_id,
        "doc_type": metadata.get("doc_type") or metadata.get("document_type") or result.chunk.source,
        "metadata": metadata,
        "preview": result.chunk.text[:240],
        "score": round(result.score, 4),
        "rerank_score": round(result.rerank_score or 0.0, 4),
    }


def _citation(result: SearchResult) -> str:
    return f"[doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}]"


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


def _bounded_int(value: Any, *, default: int, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        parsed = default
    return max(minimum, min(parsed, maximum))
