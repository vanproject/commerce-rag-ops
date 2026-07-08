from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any, Callable

from ..generator import AnswerGenerator, build_answer_context
from ..models import AgentState, SearchResult


WeakRetrievalFn = Callable[[AgentState], bool]
CitationFormatter = Callable[[SearchResult], str]


@dataclass(frozen=True)
class FinalAnswerResult:
    answer: str
    citations: list[str]
    latency_ms: int
    prompt_artifact_id: str
    weak_retrieval: bool


class FinalAnswerBuilder:
    """Generate the user-facing answer from the verified EvidencePack view.

    This component is intentionally narrow: it chooses allowed document
    citations, builds an EvidencePack-derived answer context for trace/debug,
    and delegates language generation to the configured generator.
    """

    def __init__(
        self,
        *,
        generator: AnswerGenerator,
        weak_retrieval: WeakRetrievalFn,
        citation_formatter: CitationFormatter,
    ):
        self.generator = generator
        self.weak_retrieval = weak_retrieval
        self.citation_formatter = citation_formatter

    def generate(
        self,
        *,
        state: AgentState,
        recorder: Any,
        parent_span_id: str,
        attempt: int,
    ) -> FinalAnswerResult:
        weak_retrieval = self.weak_retrieval(state)
        citations = [] if weak_retrieval else [self.citation_formatter(result) for result in state.retrieved_contexts[:4]]
        answer_span = recorder.start_span(
            "answer.generate",
            kind="answer",
            parent_id=parent_span_id,
            attempt=attempt,
            inputs={
                "domain": state.domain,
                "intent": state.intent,
                "risk_level": state.risk_level,
                "weak_retrieval": weak_retrieval,
                "citation_count": len(citations),
            },
        )
        generation_span = recorder.start_span(
            "generation.llm",
            kind="llm",
            parent_id=answer_span,
            attempt=attempt,
            inputs={
                "generator": self.generator.__class__.__name__,
                "weak_retrieval": weak_retrieval,
                "doc_citations": citations,
            },
        )
        prompt_artifact_id = recorder.add_artifact(
            generation_span,
            "generation_context",
            _generation_context_payload(state, citations),
            metadata={"attempt": attempt, "prompt_policy": "evidence_pack_only"},
        )
        started = time.perf_counter()
        answer = self.generator.generate(state, citations, weak_retrieval=weak_retrieval)
        latency_ms = int((time.perf_counter() - started) * 1000)
        recorder.end_span(
            generation_span,
            outputs={
                "answer_preview": answer[:240],
                "citations": citations,
                "prompt_artifact_id": prompt_artifact_id,
            },
            metrics={
                "latency_ms": latency_ms,
                "input_doc_citation_count": len(citations),
                "output_chars": len(answer),
            },
        )
        recorder.end_span(
            answer_span,
            outputs={
                "answer_preview": answer[:240],
                "citations": citations,
                "prompt_artifact_id": prompt_artifact_id,
            },
            metrics={"latency_ms": latency_ms},
        )
        return FinalAnswerResult(
            answer=answer,
            citations=citations,
            latency_ms=latency_ms,
            prompt_artifact_id=prompt_artifact_id,
            weak_retrieval=weak_retrieval,
        )


def _generation_context_payload(state: AgentState, citations: list[str]) -> dict[str, Any]:
    answer_context = build_answer_context(state, citations)
    return {
        "query": state.query,
        "original_query": state.original_query,
        "domain": state.domain,
        "intent": state.intent,
        "risk_level": state.risk_level,
        "memory_context": {
            "conversation_id": state.memory_context.get("conversation_id"),
            "context_resolution": state.context_resolution,
            "recent_turn_count": state.memory_context.get("recent_turn_count", 0),
        },
        "evidence_pack": answer_context["evidence_pack"],
        "doc_citations": citations,
        "tool_citations": answer_context["tool_citations"],
        "verification": state.verification,
    }
