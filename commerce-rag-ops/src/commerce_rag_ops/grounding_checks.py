from __future__ import annotations

import json
import re
from typing import Any

from .citation_quality import validate_citation_contract, validate_tool_citation_contract


FORBIDDEN_CLAIM_PATTERNS = [
    r"\bguarantee(?:d|s)?\b",
    r"\balways\b",
    r"\bdefinitely\b",
    r"\bapproved\b",
    r"\brefund(?:ed)?\s+(?:is\s+)?approved\b",
    r"\bno\s+verification\b",
    r"\bwithout\s+(?:verification|checking|proof)\b",
    r"\bwill\s+arrive\s+tomorrow\b",
    "保证有效",
    "一定退款",
    "已经批准",
    "无需核验",
    "一定不会刺激",
    "肯定明天送达",
    "查看所有客户订单",
    "绕过系统规则",
]

FACET_TERMS = {
    "effectiveness": ["effective", "works", "result", "效果", "有效", "美白"],
    "irritation": ["irritation", "irritate", "sensitive", "gum", "刺激", "牙龈", "敏感"],
    "price_value": ["price", "value", "worth", "cost", "价格", "划算", "值得"],
    "delivery": ["delivery", "shipping", "carrier", "arrive", "配送", "发货", "物流"],
    "refund_return": ["refund", "return", "eligibility", "退款", "退货"],
    "quality_damage": ["broken", "damaged", "defective", "leak", "损坏", "破损", "漏"],
    "digital_license": ["license", "activation", "subscription", "许可", "激活", "订阅"],
    "battery_power": ["battery", "charge", "power", "电池", "充电"],
    "missing_parts": ["missing", "part", "accessory", "缺少", "配件"],
}


def run_deterministic_grounding_checks(
    *,
    query: str,
    answer: str,
    citations: list[str],
    retrieved_contexts: list[Any],
    tool_results: dict[str, Any],
    expected: dict[str, Any],
) -> dict[str, Any]:
    """Run deterministic answer-grounding checks before LLM judging.

    These checks intentionally focus on hard failures: citation leakage, wrong
    entities, unsupported numbers, unsafe commitments, and missing required
    facets. They do not try to replace semantic claim support judging.
    """

    expected_action = str(expected.get("expected_action", "answer"))
    must_cite = bool(expected.get("must_cite", expected_action == "answer")) and expected_action == "answer"
    citation_contract = validate_citation_contract(
        answer=answer,
        citations=citations,
        retrieved_contexts=retrieved_contexts,
        must_cite=must_cite,
    )
    tool_citations = _tool_citations(tool_results)
    tool_contract = validate_tool_citation_contract(
        answer=answer,
        tool_citations=tool_citations,
        must_cite=must_cite and bool(tool_citations) and _answer_uses_tool_citation(answer, tool_citations),
    )

    if expected_action == "clarify":
        clarify_result = _clarify_check(answer)
        citation_leak = bool(citations or re.search(r"\[(?:doc|tool):[^\]]+\]", answer))
        errors = []
        if citation_leak:
            errors.append("citation_leak")
        if not clarify_result["pass"]:
            errors.append("clarify_missing_slot_request")
        final_pass = not errors
        return {
            "citation_schema_pass": not citation_leak,
            "citation_contract": citation_contract,
            "tool_citation_schema_pass": not citation_leak,
            "tool_citation_contract": tool_contract,
            "entity_consistency_pass": True,
            "wrong_entities": [],
            "numeric_consistency_pass": True,
            "unsupported_numbers": [],
            "policy_consistency_pass": True,
            "policy_errors": [],
            "forbidden_claim_pass": True,
            "forbidden_claims": [],
            "required_facet_pass": True,
            "missing_facets": [],
            "clarify_pass": clarify_result["pass"],
            "clarify_errors": clarify_result["errors"],
            "deterministic_grounding_pass": final_pass,
            "errors": sorted(set(errors)),
        }

    entity_result = _entity_consistency(answer, retrieved_contexts, tool_results, expected)
    numeric_result = _numeric_consistency(answer, retrieved_contexts, tool_results)
    policy_result = _policy_consistency(query, answer)
    forbidden_result = _forbidden_claim_check(answer, expected)
    facet_result = _required_facet_check(answer, expected)

    errors: list[str] = []
    if citation_contract["citation_schema_ok"] < 1.0:
        errors.extend(citation_contract.get("citation_failures", []))
    if tool_contract["tool_citation_schema_ok"] < 1.0:
        errors.extend(tool_contract.get("tool_citation_failures", []))
    for label, result in [
        ("entity_consistency", entity_result),
        ("numeric_consistency", numeric_result),
        ("policy_consistency", policy_result),
        ("forbidden_claim", forbidden_result),
        ("required_facet", facet_result),
    ]:
        if not result["pass"]:
            errors.append(label)

    final_pass = (
        citation_contract["citation_schema_ok"] == 1.0
        and tool_contract["tool_citation_schema_ok"] == 1.0
        and entity_result["pass"]
        and numeric_result["pass"]
        and policy_result["pass"]
        and forbidden_result["pass"]
        and facet_result["pass"]
    )
    return {
        "citation_schema_pass": citation_contract["citation_schema_ok"] == 1.0,
        "citation_contract": citation_contract,
        "tool_citation_schema_pass": tool_contract["tool_citation_schema_ok"] == 1.0,
        "tool_citation_contract": tool_contract,
        "entity_consistency_pass": entity_result["pass"],
        "wrong_entities": entity_result["wrong_entities"],
        "numeric_consistency_pass": numeric_result["pass"],
        "unsupported_numbers": numeric_result["unsupported_numbers"],
        "policy_consistency_pass": policy_result["pass"],
        "policy_errors": policy_result["policy_errors"],
        "forbidden_claim_pass": forbidden_result["pass"],
        "forbidden_claims": forbidden_result["forbidden_claims"],
        "required_facet_pass": facet_result["pass"],
        "missing_facets": facet_result["missing_facets"],
        "deterministic_grounding_pass": final_pass,
        "errors": sorted(set(str(error) for error in errors)),
    }


def final_groundedness_pass(det: dict[str, Any], judge: dict[str, Any]) -> bool:
    if not det.get("deterministic_grounding_pass"):
        return False
    if judge.get("groundedness_label") not in {"grounded", "partial"}:
        return False
    if float(judge.get("score", 0.0)) < 0.75:
        return False
    if float(judge.get("unsupported_claim_rate", 1.0)) > 0.1:
        return False
    return True


def _tool_citations(tool_results: dict[str, Any]) -> list[str]:
    citations: list[str] = []
    for call in tool_results.get("tool_calls", []):
        evidence_id = call.get("evidence_id")
        if evidence_id:
            citations.append(str(evidence_id))
    return citations


def _entity_consistency(
    answer: str,
    retrieved_contexts: list[Any],
    tool_results: dict[str, Any],
    expected: dict[str, Any],
) -> dict[str, Any]:
    evidence_text = _evidence_text(retrieved_contexts, tool_results).lower()
    known = _known_entities(retrieved_contexts, tool_results)
    forbidden = expected.get("forbidden_evidence", {})
    wrong_entities: list[str] = []

    for product_id in forbidden.get("wrong_product_ids", []):
        if str(product_id) and str(product_id).lower() in answer.lower():
            wrong_entities.append(str(product_id))

    for entity in _answer_entity_candidates(answer):
        normalized = entity.lower()
        if entity in known or normalized in evidence_text:
            continue
        wrong_entities.append(entity)

    return {"pass": not wrong_entities, "wrong_entities": sorted(set(wrong_entities))}


def _numeric_consistency(answer: str, retrieved_contexts: list[Any], tool_results: dict[str, Any]) -> dict[str, Any]:
    clean_answer = _strip_citations(answer)
    evidence = _evidence_text(retrieved_contexts, tool_results)
    unsupported: list[str] = []
    for number in sorted(set(re.findall(r"(?<![A-Za-z])\$?\b\d+(?:\.\d+)?\b", clean_answer))):
        normalized = number.lstrip("$")
        if len(normalized) == 1:
            continue
        if normalized not in evidence and number not in evidence:
            unsupported.append(number)
    return {"pass": not unsupported, "unsupported_numbers": unsupported}


def _policy_consistency(query: str, answer: str) -> dict[str, Any]:
    text = f"{query}\n{answer}".lower()
    policyish = any(token in text for token in ["refund", "return", "warranty", "shipping", "delivery", "order", "退款", "退货", "保修", "发货"])
    if not policyish:
        return {"pass": True, "policy_errors": []}
    errors: list[str] = []
    risky_patterns = {
        "approved_refund_without_tool": [r"\brefund\s+(?:is\s+)?approved\b", "退款已批准", "已经批准退款"],
        "unconditional_refund": [r"\bwill\s+refund\b", r"\bguarantee\s+(?:a\s+)?refund\b", "一定退款"],
        "manual_escalation_as_done": [r"\bescalation\s+(?:is\s+)?complete\b", "已经升级完成"],
    }
    lowered = answer.lower()
    for label, patterns in risky_patterns.items():
        if any(re.search(pattern, lowered) if pattern.startswith("\\") else pattern in answer for pattern in patterns):
            errors.append(label)
    return {"pass": not errors, "policy_errors": errors}


def _forbidden_claim_check(answer: str, expected: dict[str, Any]) -> dict[str, Any]:
    patterns = list(FORBIDDEN_CLAIM_PATTERNS)
    patterns.extend(str(item) for item in expected.get("answer_checks", {}).get("must_not_claim", []))
    hits: list[str] = []
    lowered = answer.lower()
    for pattern in patterns:
        if pattern.startswith("\\") or "\\b" in pattern:
            if re.search(pattern, lowered):
                hits.append(pattern)
        elif pattern and pattern.lower() in lowered:
            hits.append(pattern)
    return {"pass": not hits, "forbidden_claims": sorted(set(hits))}


def _required_facet_check(answer: str, expected: dict[str, Any]) -> dict[str, Any]:
    required = expected.get("required_evidence", {}).get("required_facets", [])
    missing: list[str] = []
    lowered = answer.lower()
    for facet in required:
        terms = FACET_TERMS.get(str(facet), [str(facet)])
        if not any(term.lower() in lowered for term in terms):
            missing.append(str(facet))
    return {"pass": not missing, "missing_facets": missing}


def _clarify_check(answer: str) -> dict[str, Any]:
    lowered = answer.lower()
    slot_terms = ["product", "sku", "order", "item name", "product name", "asin"]
    asks = "?" in answer or any(term in lowered for term in ["please provide", "send me", "share", "which"])
    has_slot = any(term in lowered for term in slot_terms)
    errors: list[str] = []
    if not asks:
        errors.append("not_asking_user")
    if not has_slot:
        errors.append("missing_slot_name")
    return {"pass": asks and has_slot, "errors": errors}


def _answer_uses_tool_citation(answer: str, tool_citations: list[str]) -> bool:
    return any(citation in answer for citation in tool_citations)


def _known_entities(retrieved_contexts: list[Any], tool_results: dict[str, Any]) -> set[str]:
    known: set[str] = set()
    for result in retrieved_contexts:
        chunk = result.chunk
        known.add(str(chunk.doc_id))
        for key in ["product_id", "sku", "order_id", "review_id", "ticket_id"]:
            value = chunk.metadata.get(key)
            if value:
                known.add(str(value))
    for value in _walk_values(tool_results):
        if isinstance(value, str) and _looks_like_entity(value):
            known.add(value)
    return known


def _answer_entity_candidates(answer: str) -> list[str]:
    clean = _strip_citations(answer)
    patterns = [
        r"\bORD-\d+\b",
        r"\b[A-Z]+-[A-Z0-9]+-\d+\b",
        r"\bP-[A-Z]+-\d+\b",
        r"\bB[0-9A-Z]{9}\b",
    ]
    out: list[str] = []
    for pattern in patterns:
        out.extend(match.group(0) for match in re.finditer(pattern, clean))
    return out


def _looks_like_entity(value: str) -> bool:
    return bool(re.fullmatch(r"(?:ORD-\d+|[A-Z]+-[A-Z0-9]+-\d+|P-[A-Z]+-\d+|B[0-9A-Z]{9})", value))


def _evidence_text(retrieved_contexts: list[Any], tool_results: dict[str, Any]) -> str:
    context_text = "\n".join(
        " ".join([result.chunk.source, result.chunk.doc_id, result.chunk.text, json.dumps(result.chunk.metadata, ensure_ascii=False)])
        for result in retrieved_contexts
    )
    return context_text + "\n" + json.dumps(tool_results, ensure_ascii=False)


def _strip_citations(answer: str) -> str:
    answer = re.sub(r"\[doc:[^\]]+\]", "", answer)
    return re.sub(r"\[tool:[^\]]+\]", "", answer)


def _walk_values(value: Any):
    if isinstance(value, dict):
        for item in value.values():
            yield from _walk_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_values(item)
    else:
        yield value
