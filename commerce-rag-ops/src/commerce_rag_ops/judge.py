from __future__ import annotations

import json
import re
from typing import Any
from urllib.request import Request

from .generator import DEFAULT_LLM_ENDPOINT, DEFAULT_LLM_MODEL, OpenAICompatibleGenerator


class OpenAICompatibleGroundednessJudge:
    """Strict answer-level judge backed by a real OpenAI-compatible API."""

    def __init__(self) -> None:
        import os

        self.client = OpenAICompatibleGenerator(
            endpoint=os.getenv("COMMERCE_RAG_JUDGE_ENDPOINT") or os.getenv("COMMERCE_RAG_LLM_ENDPOINT") or DEFAULT_LLM_ENDPOINT,
            model=os.getenv("COMMERCE_RAG_JUDGE_MODEL") or os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL),
        )

    @property
    def model(self) -> str:
        return self.client.model

    def judge(
        self,
        *,
        query: str,
        answer: str,
        citations: list[str],
        retrieved_contexts: list[Any],
        tool_results: dict[str, Any],
        expected: dict[str, Any],
    ) -> dict[str, Any]:
        payload = {
            "query": query,
            "expected_action": expected.get("expected_action", "answer"),
            "target_entities": expected.get("target_entities", {}),
            "required_facets": expected.get("required_evidence", {}).get("required_facets", []),
            "retrieved_contexts": [_context_payload(result) for result in retrieved_contexts[:8]],
            "tool_results": tool_results,
            "answer": answer,
            "citations": citations,
            "required_json_schema": {
                "action_correct": "boolean",
                "intent_correct": "boolean",
                "answer_relevant": "boolean",
                "claims": [
                    {
                        "claim": "string",
                        "support": "supported|partially_supported|unsupported|contradicted|not_applicable",
                        "supporting_citations": ["string"],
                        "reason": "string",
                    }
                ],
                "missing_required_facets": ["string"],
                "unsupported_claims": ["string"],
                "unsafe_commitment": "boolean",
                "citation_support": "full|partial|none",
                "groundedness_label": "grounded|partial|ungrounded|unsafe",
                "score": "number 0..1",
            },
        }
        request_payload = {
            "model": self.client.model,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a strict RAG evaluator. Return JSON only. "
                        "Use only the provided retrieved_contexts and tool_results. "
                        "Do not use external knowledge. Do not reward fluency. "
                        "Extract factual claims, then mark each claim supported only when the evidence directly supports it. "
                        "Claims about refunds, warranties, delivery, privacy, permissions, orders, prices, and inventory require strict tool or policy evidence."
                    ),
                },
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False, indent=2)},
            ],
        }
        req = Request(
            self.client.endpoint,
            data=json.dumps(request_payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.client.api_key}",
                "User-Agent": "commerce-rag-ops/0.1",
                "Accept": "application/json",
            },
            method="POST",
        )
        response = self.client._post_with_retries(req)
        content = str(response["choices"][0]["message"]["content"]).strip()
        return normalize_groundedness_judge_result(_parse_json_object(content), raw=content)


def judge_answer_groundedness(
    *,
    query: str,
    answer: str,
    citations: list[str],
    retrieved_contexts: list[Any],
    tool_results: dict[str, Any],
    expected: dict[str, Any],
    judge: OpenAICompatibleGroundednessJudge | None = None,
) -> dict[str, Any]:
    return (judge or OpenAICompatibleGroundednessJudge()).judge(
        query=query,
        answer=answer,
        citations=citations,
        retrieved_contexts=retrieved_contexts,
        tool_results=tool_results,
        expected=expected,
    )


def normalize_groundedness_judge_result(data: dict[str, Any], *, raw: str = "") -> dict[str, Any]:
    claims = data.get("claims", [])
    if not isinstance(claims, list):
        claims = []
    unsupported = _string_list(data.get("unsupported_claims"))
    if not unsupported:
        unsupported = [
            str(claim.get("claim", ""))[:240]
            for claim in claims
            if isinstance(claim, dict) and str(claim.get("support", "")).lower() in {"unsupported", "contradicted"}
        ]
    total_claims = len([claim for claim in claims if isinstance(claim, dict)])
    unsupported_rate = len(unsupported) / total_claims if total_claims else 0.0
    label = str(data.get("groundedness_label", "ungrounded")).lower()
    if label not in {"grounded", "partial", "ungrounded", "unsafe"}:
        label = "ungrounded"
    citation_support = str(data.get("citation_support", "none")).lower()
    if citation_support not in {"full", "partial", "none"}:
        citation_support = "none"
    return {
        "action_correct": bool(data.get("action_correct", False)),
        "intent_correct": bool(data.get("intent_correct", False)),
        "answer_relevant": bool(data.get("answer_relevant", False)),
        "claims": claims,
        "missing_required_facets": _string_list(data.get("missing_required_facets")),
        "unsupported_claims": unsupported,
        "unsupported_claim_rate": round(unsupported_rate, 4),
        "unsafe_commitment": bool(data.get("unsafe_commitment", False)),
        "citation_support": citation_support,
        "groundedness_label": label,
        "score": _score(data.get("score")),
        "raw_preview": raw[:500],
    }


def _context_payload(result: Any) -> dict[str, Any]:
    chunk = result.chunk
    return {
        "doc_id": f"{chunk.source}:{chunk.doc_id}",
        "source": chunk.source,
        "text": chunk.text[:1800],
        "metadata": chunk.metadata,
        "citation": f"[doc:{chunk.source}:{chunk.doc_id}#{chunk.chunk_id}]",
    }


def _parse_json_object(content: str) -> dict[str, Any]:
    cleaned = content.strip()
    if cleaned.startswith("```"):
        cleaned = re.sub(r"^```(?:json)?", "", cleaned).strip()
        cleaned = re.sub(r"```$", "", cleaned).strip()
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
        if not match:
            raise
        return json.loads(match.group(0))


def _score(value: Any) -> float:
    try:
        return max(0.0, min(1.0, round(float(value), 4)))
    except (TypeError, ValueError):
        return 0.0


def _string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item)[:240] for item in value if str(item).strip()]
    if value:
        return [str(value)[:240]]
    return []
