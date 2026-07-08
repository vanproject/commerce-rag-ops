from __future__ import annotations

import re
from typing import Any

from .citation_quality import DOC_CITATION_PATTERN, TOOL_CITATION_PATTERN


def strip_citations(answer: str) -> str:
    answer = DOC_CITATION_PATTERN.sub("", answer)
    answer = TOOL_CITATION_PATTERN.sub("", answer)
    return re.sub(r"\s{2,}", " ", answer).strip()


def repair_answer_citations(
    *,
    answer: str,
    action: str,
    citations: list[str],
    tool_citations: list[str],
    require_doc_citation: bool,
    require_tool_citation: bool = False,
) -> dict[str, Any]:
    """Apply deterministic citation contract repair after LLM generation."""

    changes: list[str] = []
    repaired = answer.strip()
    doc_citations = list(dict.fromkeys(citations))
    usable_tool_citations = list(dict.fromkeys(tool_citations))

    if action in {"refuse", "clarify"}:
        stripped = strip_citations(repaired)
        if stripped != repaired:
            changes.append("stripped_citations_for_non_answer")
        return {
            "answer": stripped,
            "citations": [],
            "tool_citations": [],
            "changes": changes,
        }

    known_docs = set(doc_citations)
    answer_docs = [match.group(0) for match in DOC_CITATION_PATTERN.finditer(repaired)]
    unknown_docs = [citation for citation in answer_docs if citation not in known_docs]
    for citation in unknown_docs:
        repaired = repaired.replace(citation, "")
        changes.append("removed_unknown_doc_citation")

    if require_doc_citation and doc_citations and not any(citation in repaired for citation in doc_citations):
        repaired = _append_marker(repaired, doc_citations[0])
        changes.append("appended_doc_citation")

    known_tools = set(usable_tool_citations)
    answer_tools = [match.group(0) for match in TOOL_CITATION_PATTERN.finditer(repaired)]
    unknown_tools = [citation for citation in answer_tools if citation not in known_tools]
    for citation in unknown_tools:
        repaired = repaired.replace(citation, "")
        changes.append("removed_unknown_tool_citation")

    if require_tool_citation and usable_tool_citations and not any(citation in repaired for citation in usable_tool_citations):
        repaired = _append_marker(repaired, usable_tool_citations[0])
        changes.append("appended_tool_citation")

    return {
        "answer": re.sub(r"\s{2,}", " ", repaired).strip(),
        "citations": doc_citations,
        "tool_citations": usable_tool_citations,
        "changes": sorted(set(changes)),
    }


def answer_uses_tool_fact(answer: str, tool_results: dict[str, Any]) -> bool:
    """Conservative heuristic: require tool citation only when answer names a returned structured entity."""

    lowered = answer.lower()
    for value in _walk_values(tool_results):
        if not isinstance(value, str):
            continue
        text = value.strip()
        if len(text) < 4:
            continue
        if text.lower() in lowered and _looks_structured_fact(text):
            return True
    return False


def _append_marker(answer: str, marker: str) -> str:
    if not answer:
        return marker
    if answer.endswith((".", "!", "?", "。", "！", "？")):
        return f"{answer} {marker}"
    return f"{answer}. {marker}"


def _looks_structured_fact(value: str) -> bool:
    return bool(re.fullmatch(r"(?:ORD-[A-Za-z0-9-]+|[A-Z]+-[A-Z0-9]+-\d+|P-[A-Z]+-\d+|B[0-9A-Z]{9})", value))


def _walk_values(value: Any):
    if isinstance(value, dict):
        for item in value.values():
            yield from _walk_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from _walk_values(item)
    else:
        yield value
