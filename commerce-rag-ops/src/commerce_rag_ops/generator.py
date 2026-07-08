from __future__ import annotations

import json
import os
import time
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .models import AgentState
from .text import normalize_text

DEFAULT_LLM_ENDPOINT = "https://opencode.ai/zen/go/v1"
DEFAULT_LLM_MODEL = "deepseek-v4-flash"


class AnswerGenerator(Protocol):
    def generate(self, state: AgentState, citations: list[str], *, weak_retrieval: bool) -> str:
        """Generate a final answer from agent state and grounded citations."""


class TemplateAnswerGenerator:
    """Deterministic generator used for local tests and resume demos.

    A production implementation can replace this with an LLM-backed generator
    that receives the same state, contexts, tool outputs, and citations.
    """

    def generate(self, state: AgentState, citations: list[str], *, weak_retrieval: bool) -> str:
        if weak_retrieval:
            return (
                "I do not have enough grounded context to answer this safely. "
                "Please provide the SKU, order detail, or let me escalate this to a human support specialist."
            )
        if state.intent == "recommendation":
            return self._recommendation_answer(state, citations)
        if state.intent == "customer_ops":
            return self._customer_ops_answer(state, citations)
        if state.intent == "sku_order":
            return self._sku_answer(state, citations)
        return self._support_answer(state, citations)

    def _support_answer(self, state: AgentState, citations: list[str]) -> str:
        answer_context = build_answer_context(state, citations)
        evidence = " ".join(item.get("preview", "") for item in answer_context["doc_evidence"][:3])
        normalized = normalize_text(state.query)
        tool_citations = _format_tool_citations_from_context(answer_context)
        if "refund" in normalized or "return" in normalized:
            summary = "The return/refund path depends on the return window, item condition, and proof of purchase."
        elif "warranty" in normalized:
            summary = "Warranty cases require product identification, proof of purchase, and a defect description."
        elif "shipping" in normalized or "delivery" in normalized:
            summary = "Shipping issues should be checked against the shipping policy and the latest carrier status."
        else:
            summary = "The safest support response is to answer from the matching policy and similar ticket history."
        return (
            f"{summary} Based on the retrieved policy/ticket evidence, I would respond with a grounded support "
            f"answer and cite {', '.join(citations)}. Structured tool evidence: {tool_citations}. Evidence summary: {evidence[:360]}"
        )

    def _recommendation_answer(self, state: AgentState, citations: list[str]) -> str:
        answer_context = build_answer_context(state, citations)
        products = _products_from_answer_context(answer_context)
        tool_citations = _format_tool_citations_from_context(answer_context)
        if products:
            product_lines = [
                f"{p['title']} ({p['sku']}) at ${p['price']}, rating {p['average_rating']}, stock {p['stock']}"
                for p in products[:3]
            ]
            return (
                "Recommended options: "
                + "; ".join(product_lines)
                + f". I used product/review evidence from {', '.join(citations)} and structured tool evidence {tool_citations}."
            )
        contexts = "; ".join(item.get("preview", "")[:150] for item in answer_context["doc_evidence"][:3])
        return f"I found matching product and review evidence: {contexts}. Citations: {', '.join(citations)}."

    def _customer_ops_answer(self, state: AgentState, citations: list[str]) -> str:
        answer_context = build_answer_context(state, citations)
        negative = [
            item
            for item in answer_context["doc_evidence"]
            if _safe_int(item.get("metadata", {}).get("rating"), default=5) <= 2
        ]
        tool_citations = _format_tool_citations_from_context(answer_context)
        if negative:
            signals = "; ".join(item.get("preview", "")[:160] for item in negative[:3])
            return (
                f"Customer ops signals show recurring low-rating issues: {signals}. Suggested action: inspect product "
                f"quality, shipping promises, and post-purchase messaging. Citations: {', '.join(citations)}. Tool evidence: {tool_citations}."
            )
        signals = "; ".join(item.get("preview", "")[:180] for item in answer_context["doc_evidence"][:3])
        return f"Customer ops summary should focus on repeated review/ticket themes: {signals}. Citations: {', '.join(citations)}."

    def _sku_answer(self, state: AgentState, citations: list[str]) -> str:
        answer_context = build_answer_context(state, citations)
        order = _first_fact_value(answer_context, "order_fact")
        tool_citations = _format_tool_citations_from_context(answer_context)
        if order:
            items = _first_fact_value(answer_context, "order_items") or []
            item_text = ""
            if items:
                item_text = " Items: " + "; ".join(
                    f"{item['sku']} x{item['quantity']} (${item['line_total']})" for item in items[:3]
                ) + "."
            return (
                f"Order {order['order_id']} is {order['status']} with delivery status {order['delivery_status']}. "
                f"It contains SKU {order['sku']} and total ${order['total']}.{item_text} "
                f"Tool evidence: {tool_citations}. Supporting context: {', '.join(citations)}."
            )
        products = _products_from_answer_context(answer_context)
        if not products:
            return f"I could not find a matching SKU in the structured product tool. Related policy/product evidence: {', '.join(citations)}."
        product = products[0]
        return (
            f"SKU {product['sku']} maps to {product['title']}. Current demo inventory is {product['stock']} units "
            f"at ${product['price']}. Tool evidence: {tool_citations}. Supporting context: {', '.join(citations)}."
        )


class OpenAICompatibleGenerator:
    """Optional LLM generator using a chat-completions compatible HTTP API.

    Required env vars:
    - `COMMERCE_RAG_LLM_API_KEY`

    Optional env vars:
    - `COMMERCE_RAG_LLM_ENDPOINT`, default `https://opencode.ai/zen/go/v1`
    - `COMMERCE_RAG_LLM_MODEL`, default `deepseek-v4-flash`
    - `COMMERCE_RAG_LLM_TIMEOUT`, default `120`
    - `COMMERCE_RAG_LLM_RETRIES`, default `3`
    """

    def __init__(
        self,
        *,
        endpoint: str | None = None,
        api_key: str | None = None,
        model: str | None = None,
        timeout_seconds: int | None = None,
    ):
        self.endpoint = endpoint or os.getenv("COMMERCE_RAG_LLM_ENDPOINT") or DEFAULT_LLM_ENDPOINT
        self.api_key = api_key or os.getenv("COMMERCE_RAG_LLM_API_KEY")
        self.model = model or os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL)
        self.timeout_seconds = timeout_seconds or int(os.getenv("COMMERCE_RAG_LLM_TIMEOUT", "120"))
        self.retries = int(os.getenv("COMMERCE_RAG_LLM_RETRIES", "3"))
        if not self.api_key:
            raise RuntimeError(
                "OpenAICompatibleGenerator requires COMMERCE_RAG_LLM_API_KEY. "
                "COMMERCE_RAG_LLM_ENDPOINT and COMMERCE_RAG_LLM_MODEL have production defaults."
            )
        self.endpoint = self._normalize_endpoint(self.endpoint)

    def generate(self, state: AgentState, citations: list[str], *, weak_retrieval: bool) -> str:
        if weak_retrieval:
            return TemplateAnswerGenerator().generate(state, citations, weak_retrieval=True)
        prompt = self._build_prompt(state, citations)
        payload = {
            "model": self.model,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are an ecommerce support and customer operations assistant. "
                        "Answer only from the provided evidence pack and verification result. "
                        "Include the provided document citations and tool citations when making factual claims. "
                        "Refuse or ask for escalation if evidence is insufficient."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        }
        req = Request(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
                "User-Agent": "commerce-rag-ops/0.1",
                "Accept": "application/json",
            },
            method="POST",
        )
        data = self._post_with_retries(req)
        try:
            return str(data["choices"][0]["message"]["content"]).strip()
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(f"Unexpected LLM response schema: {data}") from exc

    def _post_with_retries(self, req: Request) -> dict:
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                with urlopen(req, timeout=self.timeout_seconds) as response:
                    return json.loads(response.read().decode("utf-8"))
            except HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:500]
                if exc.code < 500 and exc.code not in {408, 409, 425, 429}:
                    raise RuntimeError(f"LLM HTTP error {exc.code}: {body}") from exc
                last_error = RuntimeError(f"LLM HTTP error {exc.code}: {body}")
            except (TimeoutError, URLError, OSError) as exc:
                last_error = exc
            if attempt < self.retries:
                time.sleep(min(2**attempt, 8))
        raise RuntimeError(f"LLM request failed after {self.retries + 1} attempts: {last_error}") from last_error

    def _build_prompt(self, state: AgentState, citations: list[str]) -> str:
        answer_context = build_answer_context(state, citations)
        prompt = {
            "query": state.query,
            "original_query": state.original_query,
            "domain": state.domain,
            "risk_level": state.risk_level,
            "memory_context": {
                "conversation_id": state.memory_context.get("conversation_id"),
                "context_resolution": state.context_resolution,
                "recent_turn_count": state.memory_context.get("recent_turn_count", 0),
            },
            "evidence_pack": answer_context["evidence_pack"],
            "verification": state.verification,
            "required_output": {
                "answer": "grounded natural-language answer",
                "citations": citations,
                "tool_citations": answer_context["tool_citations"],
            },
        }
        return json.dumps(prompt, ensure_ascii=False, indent=2)

    @staticmethod
    def _normalize_endpoint(endpoint: str) -> str:
        endpoint = endpoint.rstrip("/")
        if endpoint.endswith("/chat/completions"):
            return endpoint
        if endpoint.endswith("/v1"):
            return f"{endpoint}/chat/completions"
        return f"{endpoint}/v1/chat/completions"


def build_generator(name: str) -> AnswerGenerator:
    if name == "template":
        return TemplateAnswerGenerator()
    if name in {"openai-compatible", "llm"}:
        return OpenAICompatibleGenerator()
    raise ValueError(f"Unknown generator: {name}")


def build_answer_context(state: AgentState, citations: list[str]) -> dict[str, Any]:
    evidence_pack = state.evidence_pack or {}
    structured_facts = list(evidence_pack.get("structured_facts", []))
    doc_evidence = []
    for key in ["policy_evidence", "product_evidence", "review_evidence", "ticket_evidence"]:
        doc_evidence.extend(evidence_pack.get(key, []))
    allowed_doc_evidence = [
        item
        for item in doc_evidence
        if not citations or item.get("citation") in citations
    ]
    return {
        "evidence_pack": {
            "structured_facts": structured_facts,
            "doc_evidence": allowed_doc_evidence,
            "unresolved_conflicts": evidence_pack.get("unresolved_conflicts", []),
            "missing_requirements": evidence_pack.get("missing_requirements", []),
        },
        "structured_facts": structured_facts,
        "doc_evidence": allowed_doc_evidence,
        "doc_citations": citations,
        "tool_citations": [
            fact.get("citation")
            for fact in structured_facts
            if fact.get("citation") and fact.get("citation") in state.tool_citations
        ],
    }


def _format_tool_citations_from_context(answer_context: dict[str, Any]) -> str:
    tool_citations = list(dict.fromkeys(answer_context.get("tool_citations", [])))
    return ", ".join(tool_citations) if tool_citations else "none"


def _first_fact_value(answer_context: dict[str, Any], fact_type: str) -> Any:
    for fact in answer_context.get("structured_facts", []):
        if fact.get("fact_type") == fact_type:
            return fact.get("value")
    return None


def _products_from_answer_context(answer_context: dict[str, Any]) -> list[dict[str, Any]]:
    products = []
    for fact in answer_context.get("structured_facts", []):
        if fact.get("fact_type") != "product_fact":
            continue
        value = fact.get("value") or {}
        if "products" in value:
            products.extend(value.get("products", []))
        elif value:
            products.append(value)
    return products


def _safe_int(value: Any, *, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def check_openai_compatible_llm() -> dict:
    try:
        generator = OpenAICompatibleGenerator()
        endpoint = generator.endpoint
        masked_endpoint = endpoint.replace("/chat/completions", "/...")
        payload = {
            "model": generator.model,
            "temperature": 0,
            "messages": [
                {"role": "system", "content": "Reply with OK only."},
                {"role": "user", "content": "Connectivity check."},
            ],
        }
        req = Request(
            generator.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {generator.api_key}",
                "User-Agent": "commerce-rag-ops/0.1",
                "Accept": "application/json",
            },
            method="POST",
        )
        with urlopen(req, timeout=generator.timeout_seconds) as response:
            data = json.loads(response.read().decode("utf-8"))
        answer = str(data["choices"][0]["message"]["content"]).strip()
        return {"ok": True, "endpoint": masked_endpoint, "model": generator.model, "answer_preview": answer[:120]}
    except Exception as exc:
        endpoint = os.getenv("COMMERCE_RAG_LLM_ENDPOINT") or DEFAULT_LLM_ENDPOINT
        model = os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL)
        return {
            "ok": False,
            "endpoint": OpenAICompatibleGenerator._normalize_endpoint(endpoint).replace("/chat/completions", "/..."),
            "model": model,
            "error": str(exc),
        }
