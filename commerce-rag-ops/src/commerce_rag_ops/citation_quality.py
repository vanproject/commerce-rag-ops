from __future__ import annotations

import re
from typing import Any


DOC_CITATION_PATTERN = re.compile(r"\[doc:(?P<source>[a-zA-Z0-9_-]+):(?P<doc_id>[^#\]\s]+)#(?P<chunk_id>[a-zA-Z0-9_-]+)\]")
TOOL_CITATION_PATTERN = re.compile(r"\[tool:(?P<tool_name>[a-zA-Z0-9_.-]+)(?::(?P<entity>[^#\]\s]+))?\]")
CITATION_PATTERN = DOC_CITATION_PATTERN


def validate_citation_contract(
    *,
    answer: str,
    citations: list[str],
    retrieved_contexts: list[Any],
    must_cite: bool = True,
) -> dict[str, Any]:
    """Validate citation syntax and grounding against retrieved contexts.

    The contract is intentionally deterministic. It checks that:
    - agent citations match `[doc:<source>:<doc_id>#<chunk_id>]`
    - each citation maps to a retrieved chunk
    - answer-side citation markers are syntactically valid and known
    - cite-required answers include at least one answer-side citation marker
    """

    known_contexts = {
        _context_key(result): {"rank": rank, "doc_type": _doc_type(result), "citation": _context_key(result)}
        for rank, result in enumerate(retrieved_contexts, start=1)
    }
    parsed_state = [_parse_citation(citation) for citation in citations]
    answer_citations = _answer_citations(answer)
    parsed_answer = [_parse_citation(citation) for citation in answer_citations]

    failures: list[str] = []
    citation_payload: list[dict[str, Any]] = []
    grounded_state_count = 0

    for citation, parsed in zip(citations, parsed_state):
        if parsed is None:
            failures.append("malformed_state_citation")
            continue
        context = known_contexts.get(citation)
        if not context:
            failures.append("ungrounded_state_citation")
            continue
        grounded_state_count += 1
        citation_payload.append({**parsed, "rank": context["rank"], "doc_type": context["doc_type"]})

    malformed_answer_count = sum(1 for parsed in parsed_answer if parsed is None)
    if malformed_answer_count:
        failures.append("malformed_answer_citation")

    known_citation_set = set(citations)
    known_answer_citations = [citation for citation in answer_citations if citation in known_citation_set]
    unknown_answer_citations = [citation for citation in answer_citations if citation not in known_citation_set]
    if unknown_answer_citations:
        failures.append("unknown_answer_citation")
    if must_cite and not answer_citations:
        failures.append("missing_answer_citation")
    if citations and grounded_state_count < len(citations):
        failures.append("state_citation_not_fully_grounded")

    answer_precision = len(known_answer_citations) / len(answer_citations) if answer_citations else (0.0 if must_cite else 1.0)
    answer_recall = len(set(known_answer_citations)) / len(known_citation_set) if known_citation_set else (1.0 if not must_cite else 0.0)
    grounded_rate = grounded_state_count / len(citations) if citations else (1.0 if not must_cite else 0.0)

    return {
        "citation_schema_ok": 1.0 if not failures else 0.0,
        "answer_citation_precision": round(answer_precision, 4),
        "answer_citation_recall": round(answer_recall, 4),
        "citation_grounded_rate": round(grounded_rate, 4),
        "citation_count": len(citations),
        "answer_citation_count": len(answer_citations),
        "citation_failures": sorted(set(failures)),
        "citation_payload": citation_payload,
    }


def validate_tool_citation_contract(
    *,
    answer: str,
    tool_citations: list[str],
    must_cite: bool = True,
) -> dict[str, Any]:
    known_tool_citations = set(tool_citations)
    answer_tool_citations = _answer_tool_citations(answer)
    parsed_answer = [_parse_tool_citation(citation) for citation in answer_tool_citations]
    parsed_state = [_parse_tool_citation(citation) for citation in tool_citations]

    failures: list[str] = []
    if any(parsed is None for parsed in parsed_state):
        failures.append("malformed_state_tool_citation")
    if any(parsed is None for parsed in parsed_answer):
        failures.append("malformed_answer_tool_citation")
    known_answer_citations = [citation for citation in answer_tool_citations if citation in known_tool_citations]
    unknown_answer_citations = [citation for citation in answer_tool_citations if citation not in known_tool_citations]
    if unknown_answer_citations:
        failures.append("unknown_answer_tool_citation")
    if must_cite and tool_citations and not answer_tool_citations:
        failures.append("missing_answer_tool_citation")

    precision = len(known_answer_citations) / len(answer_tool_citations) if answer_tool_citations else (0.0 if must_cite and tool_citations else 1.0)
    recall = len(set(known_answer_citations)) / len(known_tool_citations) if known_tool_citations else 1.0
    return {
        "tool_citation_schema_ok": 1.0 if not failures else 0.0,
        "answer_tool_citation_precision": round(precision, 4),
        "answer_tool_citation_recall": round(recall, 4),
        "tool_citation_count": len(tool_citations),
        "answer_tool_citation_count": len(answer_tool_citations),
        "tool_citation_failures": sorted(set(failures)),
        "tool_citation_payload": [parsed for parsed in parsed_state if parsed],
    }


def _answer_citations(answer: str) -> list[str]:
    return [match.group(0) for match in DOC_CITATION_PATTERN.finditer(answer)]


def _answer_tool_citations(answer: str) -> list[str]:
    return [match.group(0) for match in TOOL_CITATION_PATTERN.finditer(answer)]


def _parse_citation(citation: str) -> dict[str, str] | None:
    match = DOC_CITATION_PATTERN.fullmatch(citation.strip())
    if not match:
        return None
    return match.groupdict()


def _parse_tool_citation(citation: str) -> dict[str, str] | None:
    match = TOOL_CITATION_PATTERN.fullmatch(citation.strip())
    if not match:
        return None
    payload = match.groupdict()
    return {key: value for key, value in payload.items() if value is not None}


def _context_key(result: Any) -> str:
    chunk = result.chunk
    return f"[doc:{chunk.source}:{chunk.doc_id}#{chunk.chunk_id}]"


def _doc_type(result: Any) -> str:
    metadata = result.chunk.metadata
    return str(metadata.get("doc_type") or metadata.get("document_type") or result.chunk.source)
