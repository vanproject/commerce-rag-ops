from __future__ import annotations

import json
import os
import time
from typing import Any, Protocol
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .generator import DEFAULT_LLM_ENDPOINT, DEFAULT_LLM_MODEL, OpenAICompatibleGenerator
from .models import AgentState
from .tools.base import ToolCall


VALID_INTENTS = {"support", "recommendation", "customer_ops", "sku_order", "unknown"}
VALID_ACTIONS = {"answer", "retry", "refuse", "escalate"}
VALID_PLAN_ACTIONS = {"direct_answer", "ask_user", "call_tools", "retrieve_memory", "decide_action"}


class AgentAdvisor(Protocol):
    name: str

    def advise_route(self, query: str, *, rule_decision: dict[str, Any], memory_context: dict[str, Any]) -> dict[str, Any]:
        ...

    def advise_plan(
        self,
        query: str,
        *,
        state: AgentState,
        rule_plan: dict[str, Any],
        available_tools: list[str],
        attempt: int,
        evidence_gaps: list[str],
    ) -> dict[str, Any]:
        ...

    def advise_tools(
        self,
        query: str,
        *,
        state: AgentState,
        rule_calls: list[ToolCall],
        available_tools: list[str],
    ) -> dict[str, Any]:
        ...

    def advise_action(
        self,
        *,
        state: AgentState,
        evidence_gaps: list[str],
        rule_action: str,
        attempt: int,
        max_retries: int,
    ) -> dict[str, Any]:
        ...


class RuleOnlyAdvisor:
    name = "rule-only"

    def advise_route(self, query: str, *, rule_decision: dict[str, Any], memory_context: dict[str, Any]) -> dict[str, Any]:
        return {"source": self.name, "used": False}

    def advise_plan(
        self,
        query: str,
        *,
        state: AgentState,
        rule_plan: dict[str, Any],
        available_tools: list[str],
        attempt: int,
        evidence_gaps: list[str],
    ) -> dict[str, Any]:
        return {"source": self.name, "used": False, **rule_plan}

    def advise_tools(
        self,
        query: str,
        *,
        state: AgentState,
        rule_calls: list[ToolCall],
        available_tools: list[str],
    ) -> dict[str, Any]:
        return {"source": self.name, "used": False, "tool_calls": []}

    def advise_action(
        self,
        *,
        state: AgentState,
        evidence_gaps: list[str],
        rule_action: str,
        attempt: int,
        max_retries: int,
    ) -> dict[str, Any]:
        return {"source": self.name, "used": False, "action": rule_action}


class OpenAICompatibleAdvisor:
    name = "openai-compatible-advisor"

    def __init__(
        self,
        *,
        endpoint: str | None = None,
        api_key: str | None = None,
        model: str | None = None,
        timeout_seconds: int | None = None,
    ):
        self.endpoint = OpenAICompatibleGenerator._normalize_endpoint(
            endpoint or os.getenv("COMMERCE_RAG_LLM_ENDPOINT") or DEFAULT_LLM_ENDPOINT
        )
        self.api_key = api_key or os.getenv("COMMERCE_RAG_LLM_API_KEY")
        self.model = model or os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL)
        self.timeout_seconds = timeout_seconds or int(os.getenv("COMMERCE_RAG_LLM_TIMEOUT", "120"))
        self.retries = int(os.getenv("COMMERCE_RAG_LLM_RETRIES", "3"))
        if not self.api_key:
            raise RuntimeError("OpenAICompatibleAdvisor requires COMMERCE_RAG_LLM_API_KEY")

    def advise_route(self, query: str, *, rule_decision: dict[str, Any], memory_context: dict[str, Any]) -> dict[str, Any]:
        prompt = {
            "task": "Suggest ecommerce intent routing. You propose only; deterministic policy will make the final decision.",
            "valid_intents": sorted(VALID_INTENTS),
            "query": query,
            "memory_context": {
                "active_entities": memory_context.get("active_entities", {}),
                "resolved_entities": memory_context.get("resolved_entities", []),
                "recent_turn_count": len(memory_context.get("recent_turns", [])),
            },
            "rule_decision": rule_decision,
            "output_schema": {
                "intent": "one of valid_intents",
                "confidence": "0..1",
                "reason": "short reason",
            },
        }
        return self._complete_json(prompt, default={"source": self.name, "used": False})

    def advise_plan(
        self,
        query: str,
        *,
        state: AgentState,
        rule_plan: dict[str, Any],
        available_tools: list[str],
        attempt: int,
        evidence_gaps: list[str],
    ) -> dict[str, Any]:
        prompt = {
            "task": (
                "Suggest an execution plan for an ecommerce agent. RAG is only semantic long-term memory, "
                "not a mandatory pipeline step. Decide whether to call structured tools, retrieve semantic memory, "
                "ask the user, answer directly, or move to final decision. You propose only; deterministic policy validates."
            ),
            "valid_plan_actions": sorted(VALID_PLAN_ACTIONS),
            "query": query,
            "intent": state.intent,
            "risk_level": state.risk_level,
            "attempt": attempt + 1,
            "evidence_gaps": evidence_gaps,
            "available_tools": available_tools,
            "rule_plan": rule_plan,
            "memory_context": {
                "active_entities": state.memory_context.get("active_entities", {}),
                "resolved_entities": state.resolved_entities,
                "recent_turn_count": state.memory_context.get("recent_turn_count", 0),
            },
            "output_schema": {
                "goal": "short task goal",
                "actions": ["direct_answer | ask_user | call_tools | retrieve_memory | decide_action"],
                "tool_calls": [
                    {
                        "tool_name": "name from available_tools",
                        "input": "json object",
                        "reason": "short reason",
                        "required": False,
                    }
                ],
                "memory_request": {
                    "query": "semantic memory query",
                    "sources": ["kb | ticket | product | review"],
                    "top_k": 6,
                    "reason": "why semantic memory is needed",
                },
                "skip_memory_reason": "reason when semantic memory is not needed",
                "risk_notes": ["short guardrail note"],
            },
        }
        return self._complete_json(default={"source": self.name, "used": False, **rule_plan}, prompt=prompt)

    def advise_tools(
        self,
        query: str,
        *,
        state: AgentState,
        rule_calls: list[ToolCall],
        available_tools: list[str],
    ) -> dict[str, Any]:
        prompt = {
            "task": (
                "Suggest additional tool calls for the ecommerce agent. You cannot bypass ToolPolicy. "
                "Prefer drafting/escalation tools for user confirmation instead of approving refunds."
            ),
            "query": query,
            "intent": state.intent,
            "risk_level": state.risk_level,
            "available_tools": available_tools,
            "rule_tool_calls": [call.__dict__ for call in rule_calls],
            "active_entities": state.memory_context.get("active_entities", {}),
            "output_schema": {
                "tool_calls": [
                    {
                        "tool_name": "name from available_tools",
                        "input": "json object",
                        "reason": "short reason",
                        "required": False,
                    }
                ],
                "reason": "short reason",
            },
        }
        return self._complete_json(prompt, default={"source": self.name, "used": False, "tool_calls": []})

    def advise_action(
        self,
        *,
        state: AgentState,
        evidence_gaps: list[str],
        rule_action: str,
        attempt: int,
        max_retries: int,
    ) -> dict[str, Any]:
        prompt = {
            "task": (
                "Suggest final action for an ecommerce support agent. You can propose answer, retry, refuse, or escalate. "
                "Do not approve refunds or bypass missing evidence; suggest escalation/confirmation for risky operations."
            ),
            "query": state.query,
            "intent": state.intent,
            "risk_level": state.risk_level,
            "evidence_gaps": evidence_gaps,
            "rule_action": rule_action,
            "attempt": attempt + 1,
            "max_retries": max_retries,
            "tool_summary": {
                "products": len(state.tool_results.get("products", [])),
                "orders": len(state.tool_results.get("orders", [])),
                "return_eligibility": state.tool_results.get("return_eligibility", []),
                "tool_policy_decisions": [
                    {
                        "tool_name": call.get("tool_name"),
                        "policy_decision": call.get("policy_decision"),
                        "found": call.get("found"),
                    }
                    for call in state.tool_results.get("tool_calls", [])
                ],
            },
            "output_schema": {
                "action": "answer | retry | refuse | escalate",
                "confidence": "0..1",
                "reason": "short reason",
                "customer_confirmation": "optional confirmation text",
            },
        }
        return self._complete_json(prompt, default={"source": self.name, "used": False, "action": rule_action})

    def _complete_json(self, prompt: dict[str, Any], *, default: dict[str, Any]) -> dict[str, Any]:
        payload = {
            "model": self.model,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a constrained planning advisor for an ecommerce Agentic RAG system. "
                        "Return only a compact JSON object. You propose; deterministic policy makes final decisions."
                    ),
                },
                {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
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
        try:
            data = self._post_with_retries(req)
            raw = str(data["choices"][0]["message"]["content"]).strip()
            parsed = _parse_json_object(raw)
            parsed["source"] = self.name
            parsed["used"] = True
            return parsed
        except Exception as exc:
            return {**default, "source": self.name, "used": False, "error": str(exc)}

    def _post_with_retries(self, req: Request) -> dict[str, Any]:
        last_error: Exception | None = None
        for attempt in range(self.retries + 1):
            try:
                with urlopen(req, timeout=self.timeout_seconds) as response:
                    return json.loads(response.read().decode("utf-8"))
            except HTTPError as exc:
                body = exc.read().decode("utf-8", errors="replace")[:500]
                if exc.code < 500 and exc.code not in {408, 409, 425, 429}:
                    raise RuntimeError(f"LLM advisor HTTP error {exc.code}: {body}") from exc
                last_error = RuntimeError(f"LLM advisor HTTP error {exc.code}: {body}")
            except (TimeoutError, URLError, OSError) as exc:
                last_error = exc
            if attempt < self.retries:
                time.sleep(min(2**attempt, 8))
        raise RuntimeError(f"LLM advisor failed after {self.retries + 1} attempts: {last_error}") from last_error


def build_advisor(name: str) -> AgentAdvisor:
    if name in {"rule", "none", "off", "template"}:
        return RuleOnlyAdvisor()
    if name in {"llm", "openai-compatible"}:
        return OpenAICompatibleAdvisor()
    if name == "auto":
        if os.getenv("COMMERCE_RAG_LLM_API_KEY"):
            return OpenAICompatibleAdvisor()
        return RuleOnlyAdvisor()
    raise ValueError(f"Unknown advisor: {name}")


def _parse_json_object(text: str) -> dict[str, Any]:
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:].strip()
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end >= start:
        text = text[start : end + 1]
    parsed = json.loads(text)
    return parsed if isinstance(parsed, dict) else {}
