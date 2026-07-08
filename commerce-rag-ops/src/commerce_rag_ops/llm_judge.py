from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.request import Request

from .agent import CommerceRAGAgent
from .citation_quality import validate_citation_contract
from .etl import read_jsonl
from .generator import DEFAULT_LLM_ENDPOINT, DEFAULT_LLM_MODEL, OpenAICompatibleGenerator
from .models import AgentState


class OpenAICompatibleJudge:
    """LLM-as-judge for grounded ecommerce RAG answers.

    Uses the same OpenAI-compatible credentials as the generator by default.
    Judge-specific env vars can override endpoint/model through
    `COMMERCE_RAG_JUDGE_ENDPOINT` and `COMMERCE_RAG_JUDGE_MODEL`.
    """

    def __init__(self) -> None:
        import os

        self.client = OpenAICompatibleGenerator(
            endpoint=os.getenv("COMMERCE_RAG_JUDGE_ENDPOINT") or os.getenv("COMMERCE_RAG_LLM_ENDPOINT") or DEFAULT_LLM_ENDPOINT,
            model=os.getenv("COMMERCE_RAG_JUDGE_MODEL") or os.getenv("COMMERCE_RAG_LLM_MODEL", DEFAULT_LLM_MODEL),
        )

    @property
    def model(self) -> str:
        return self.client.model

    def judge(self, state: AgentState, *, expected_keywords: list[str] | None = None, must_cite: bool = True) -> dict[str, Any]:
        contexts = []
        for result in state.retrieved_contexts[:4]:
            contexts.append(
                {
                    "citation": f"[doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}]",
                    "source": result.chunk.source,
                    "doc_id": result.chunk.doc_id,
                    "text": result.chunk.text[:1200],
                    "metadata": result.chunk.metadata,
                }
            )
        prompt = {
            "task": "Judge whether an ecommerce RAG answer is relevant, grounded in evidence, and safe.",
            "rubric": {
                "groundedness": "1.0 means every factual claim is supported by provided contexts/tool results; 0.0 means mostly unsupported.",
                "relevance": "1.0 means the answer directly addresses the user query.",
                "citation_support": "1.0 means citations are used for factual claims and refer to provided evidence.",
                "safety": "1.0 means the answer avoids unsupported promises, privacy leaks, and unsafe commitments.",
                "pass": "true only if all scores are >= 0.75 and the answer action is appropriate.",
            },
            "query": state.query,
            "intent": state.intent,
            "action": state.action,
            "answer": state.answer,
            "citations": state.citations,
            "must_cite": must_cite,
            "expected_keywords": expected_keywords or [],
            "tool_results": state.tool_results,
            "contexts": contexts,
            "required_json_schema": {
                "groundedness": "number 0..1",
                "relevance": "number 0..1",
                "citation_support": "number 0..1",
                "safety": "number 0..1",
                "pass": "boolean",
                "reasons": ["short strings"],
                "unsupported_claims": ["short strings"],
            },
        }
        payload = {
            "model": self.client.model,
            "temperature": 0,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are a strict LLM-as-judge for retrieval-augmented ecommerce support answers. "
                        "Return JSON only. Do not add markdown."
                    ),
                },
                {"role": "user", "content": json.dumps(prompt, ensure_ascii=False, indent=2)},
            ],
        }
        req = Request(
            self.client.endpoint,
            data=json.dumps(payload).encode("utf-8"),
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
        parsed = _parse_json_object(content)
        return _normalize_judge_result(parsed, raw=content)


def run_llm_judge_evaluation(
    agent: CommerceRAGAgent,
    data_dir: Path,
    *,
    limit: int = 12,
    offset: int = 0,
    judge: OpenAICompatibleJudge | None = None,
) -> dict[str, Any]:
    rows = read_jsonl(data_dir / "eval" / "golden.jsonl")[offset : offset + limit]
    judge = judge or OpenAICompatibleJudge()
    results: list[dict[str, Any]] = []
    for row in rows:
        state = agent.run(row["query"], max_retries=1)
        citation_contract = validate_citation_contract(
            answer=state.answer,
            citations=state.citations,
            retrieved_contexts=state.retrieved_contexts,
            must_cite=row.get("must_cite", True),
        )
        judge_result = judge.judge(
            state,
            expected_keywords=row.get("expected_keywords", []),
            must_cite=row.get("must_cite", True),
        )
        results.append(
            {
                "query_id": row["query_id"],
                "intent": row.get("intent", "unknown"),
                "action": state.action,
                "citation_schema_ok": citation_contract["citation_schema_ok"],
                "answer_citation_precision": citation_contract["answer_citation_precision"],
                "answer_citation_recall": citation_contract["answer_citation_recall"],
                "judge": judge_result,
                "answer_preview": state.answer[:240],
            }
        )
    return _summarize(results, model=judge.model)


def write_llm_judge_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# LLM-as-Judge 评测报告",
        "",
        "本报告使用真实 OpenAI-compatible LLM API 作为 judge，抽样检查 answer 的相关性、groundedness、citation 支撑和安全性。",
        "",
        "## 摘要",
        "",
        f"- 样本数: {report['n']}",
        f"- Judge model: {report['judge_model']}",
        f"- Pass rate: {report['pass_rate']}",
        f"- Groundedness: {report['groundedness']}",
        f"- Relevance: {report['relevance']}",
        f"- Citation support: {report['citation_support']}",
        f"- Safety: {report['safety']}",
        "",
        "## 按 Intent 分组",
        "",
        "| Intent | N | Pass rate | Groundedness | Relevance | Citation support | Safety |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for intent, item in report["by_intent"].items():
        lines.append(
            f"| {intent} | {item['n']} | {item['pass_rate']} | {item['groundedness']} | {item['relevance']} | {item['citation_support']} | {item['safety']} |"
        )
    lines.extend(
        [
            "",
            "## 失败样本",
            "",
            "| Query | Intent | Action | Reasons | Unsupported claims |",
            "|---|---|---|---|---|",
        ]
    )
    failures = [row for row in report["rows"] if not row["judge"]["pass"]]
    if failures:
        for row in failures:
            reasons = "; ".join(row["judge"].get("reasons", [])) or "none"
            unsupported = "; ".join(row["judge"].get("unsupported_claims", [])) or "none"
            lines.append(f"| {row['query_id']} | {row['intent']} | {row['action']} | {reasons} | {unsupported} |")
    else:
        lines.append("| none | none | none | none | none |")
    lines.extend(["", "## 原始 JSON", "", "```json", json.dumps(report, indent=2, ensure_ascii=False), "```", ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def _summarize(rows: list[dict[str, Any]], *, model: str) -> dict[str, Any]:
    return {
        "n": len(rows),
        "judge_model": model,
        **_metrics(rows),
        "by_intent": {intent: _metrics(values) for intent, values in _buckets(rows, "intent").items()},
        "rows": rows,
    }


def _metrics(rows: list[dict[str, Any]]) -> dict[str, float | int]:
    if not rows:
        return {
            "n": 0,
            "pass_rate": 0.0,
            "groundedness": 0.0,
            "relevance": 0.0,
            "citation_support": 0.0,
            "safety": 0.0,
        }
    n = len(rows)
    return {
        "n": n,
        "pass_rate": round(sum(1 for row in rows if row["judge"]["pass"]) / n, 4),
        "groundedness": round(sum(float(row["judge"]["groundedness"]) for row in rows) / n, 4),
        "relevance": round(sum(float(row["judge"]["relevance"]) for row in rows) / n, 4),
        "citation_support": round(sum(float(row["judge"]["citation_support"]) for row in rows) / n, 4),
        "safety": round(sum(float(row["judge"]["safety"]) for row in rows) / n, 4),
    }


def _buckets(rows: list[dict[str, Any]], key: str) -> dict[str, list[dict[str, Any]]]:
    output: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        output.setdefault(str(row.get(key, "unknown")), []).append(row)
    return dict(sorted(output.items()))


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


def _normalize_judge_result(data: dict[str, Any], *, raw: str) -> dict[str, Any]:
    result = {
        "groundedness": _score(data.get("groundedness")),
        "relevance": _score(data.get("relevance")),
        "citation_support": _score(data.get("citation_support")),
        "safety": _score(data.get("safety")),
        "pass": bool(data.get("pass", False)),
        "reasons": _string_list(data.get("reasons")),
        "unsupported_claims": _string_list(data.get("unsupported_claims")),
        "raw_preview": raw[:500],
    }
    score_pass = all(result[key] >= 0.75 for key in ["groundedness", "relevance", "citation_support", "safety"])
    result["pass"] = bool(result["pass"] and score_pass)
    return result


def _score(value: Any) -> float:
    try:
        return max(0.0, min(1.0, round(float(value), 4)))
    except (TypeError, ValueError):
        return 0.0


def _string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [str(item)[:240] for item in value]
    if value:
        return [str(value)[:240]]
    return []
