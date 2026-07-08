from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from .models import DocumentChunk, SearchResult
from .text import cosine_similarity, tokenize


@dataclass(frozen=True)
class EntityCandidate:
    product_id: str
    sku: str = ""
    title: str = ""
    category: str = ""
    confidence: float = 0.0
    evidence: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "product_id": self.product_id,
            "sku": self.sku,
            "title": self.title,
            "category": self.category,
            "confidence": round(self.confidence, 4),
            "evidence": list(self.evidence),
        }


@dataclass
class _EntityProfile:
    product_id: str
    sku: str = ""
    title: str = ""
    category: str = ""
    text_parts: list[str] = field(default_factory=list)
    doc_count: int = 0

    @property
    def text(self) -> str:
        return " ".join(part for part in self.text_parts if part)


class EntityCandidateRetriever:
    """Product-first retrieval over chunk metadata and product profile text."""

    def __init__(self, chunks: Iterable[DocumentChunk]):
        self.profiles: dict[str, _EntityProfile] = {}
        self.chunks_by_product_id: dict[str, list[DocumentChunk]] = defaultdict(list)
        self.title_tokens: dict[str, set[str]] = {}
        self.profile_vectors: dict[str, Counter[str]] = {}
        self.product_ids_by_sku: dict[str, set[str]] = defaultdict(set)
        self.product_ids_by_token: dict[str, set[str]] = defaultdict(set)

        for chunk in chunks:
            product_id = str(chunk.metadata.get("product_id", "")).strip()
            if not product_id:
                continue
            self.chunks_by_product_id[product_id].append(chunk)
            profile = self.profiles.setdefault(product_id, _EntityProfile(product_id=product_id))
            profile.doc_count += 1
            title = str(chunk.metadata.get("title") or "").strip()
            sku = str(chunk.metadata.get("sku") or "").strip()
            category = str(chunk.metadata.get("category") or "").strip()
            if title and (not profile.title or _doc_type(chunk) == "product_profile"):
                profile.title = title
            if sku:
                profile.sku = sku
                self.product_ids_by_sku[_sku_key(sku)].add(product_id)
            if category and (not profile.category or _doc_type(chunk) == "product_profile"):
                profile.category = category
            if _doc_type(chunk) == "product_profile" or chunk.source == "product":
                profile.text_parts.append(" ".join([title, sku, category, chunk.text[:1200]]))
            elif profile.doc_count <= 8:
                profile.text_parts.append(chunk.text[:300])

        for product_id, profile in self.profiles.items():
            title_tokens = _content_tokens(profile.title)
            self.title_tokens[product_id] = title_tokens
            self.profile_vectors[product_id] = Counter(_content_tokens(profile.text))
            for token in title_tokens:
                self.product_ids_by_token[token].add(product_id)

    def retrieve(self, query: str, *, top_k: int = 5) -> list[EntityCandidate]:
        query_tokens = _content_tokens(query)
        if not query_tokens:
            return []
        scores: dict[str, float] = defaultdict(float)
        evidence: dict[str, list[str]] = defaultdict(list)

        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", query.lower()):
            for product_id in self.product_ids_by_sku.get(_sku_key(token), set()):
                scores[product_id] += 1.2
                evidence[product_id].append("sku_alias_match")

        candidate_ids: set[str] = set()
        for token in query_tokens:
            candidate_ids.update(self.product_ids_by_token.get(token, set()))
        if not candidate_ids:
            candidate_ids = set(self.profiles)

        query_counter = Counter(query_tokens)
        query_category = _category_hint(query_tokens)
        for product_id in candidate_ids:
            profile = self.profiles[product_id]
            title_tokens = self.title_tokens.get(product_id, set())
            title_overlap = query_tokens & title_tokens
            if title_overlap:
                title_precision = len(title_overlap) / max(len(title_tokens), 1)
                query_coverage = len(title_overlap) / max(len(query_tokens), 1)
                scores[product_id] += min(0.68, 0.12 * len(title_overlap) + 0.25 * title_precision + 0.55 * query_coverage)
                evidence[product_id].append("lexical_product_title")
            profile_similarity = cosine_similarity(query_counter, self.profile_vectors.get(product_id, Counter()))
            if profile_similarity > 0:
                scores[product_id] += min(0.38, profile_similarity)
                evidence[product_id].append("semantic_product_profile")
            if query_category and profile.category.lower() == query_category:
                scores[product_id] += 0.08
                evidence[product_id].append("category_intent_match")

        ranked: list[EntityCandidate] = []
        for product_id, score in scores.items():
            profile = self.profiles[product_id]
            confidence = _confidence(score, len(query_tokens & self.title_tokens.get(product_id, set())))
            if confidence < 0.18:
                continue
            ranked.append(
                EntityCandidate(
                    product_id=product_id,
                    sku=profile.sku,
                    title=profile.title,
                    category=profile.category,
                    confidence=confidence,
                    evidence=list(dict.fromkeys(evidence[product_id])),
                )
            )
        ranked.sort(key=lambda item: item.confidence, reverse=True)
        return ranked[:top_k]

    def evidence_results(
        self,
        product_id: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        facets: Iterable[str] | None = None,
    ) -> list[SearchResult]:
        source_filter = set(sources or [])
        required_facets = {str(facet).lower().strip() for facet in facets or [] if str(facet).strip()}
        chunks = [
            chunk
            for chunk in self.chunks_by_product_id.get(product_id, [])
            if not source_filter or chunk.source in source_filter
        ]
        chunks.sort(key=lambda chunk: _evidence_chunk_order(chunk, required_facets))
        results: list[SearchResult] = []
        for rank, chunk in enumerate(chunks[:top_k], start=1):
            score = max(0.1, 1.0 - rank * 0.05)
            results.append(SearchResult(chunk=chunk, score=score, rerank_score=score))
        return results

    def complete_entity_evidence(
        self,
        results: list[SearchResult],
        product_id: str,
        *,
        sources: Iterable[str] | None = None,
        facets: Iterable[str] | None = None,
        top_k: int = 5,
    ) -> list[SearchResult]:
        if not product_id:
            return results[:top_k]
        required_facets = {str(facet).lower().strip() for facet in facets or [] if str(facet).strip()}
        source_filter = set(sources or [])
        selected = constrain_results_to_entity(results, product_id)
        selected = [result for result in selected if _result_product_id(result) in {"", product_id}]
        needed_chunks: list[DocumentChunk] = []
        if not any(_doc_type(result.chunk) == "product_profile" for result in selected):
            needed_chunks.extend(self._matching_chunks(product_id, doc_types={"product_profile", "product"}, sources=source_filter))
        covered_facets = set().union(*(_chunk_aspects(result.chunk) for result in selected)) if selected else set()
        missing_facets = required_facets - covered_facets
        for facet in sorted(missing_facets):
            needed_chunks.extend(
                self._matching_chunks(
                    product_id,
                    doc_types={"review_aspect_summary", "review_evidence", "faq_case", "review", "ticket"},
                    sources=source_filter,
                    facet=facet,
                )
            )
        completed: list[SearchResult] = []
        seen: set[tuple[str, str, str]] = set()
        for chunk in needed_chunks:
            key = _chunk_key(chunk)
            if key in seen:
                continue
            seen.add(key)
            score = 1.05 if _doc_type(chunk) == "product_profile" else 1.0
            completed.append(SearchResult(chunk=chunk, score=score, rerank_score=score))
        for result in selected:
            key = _chunk_key(result.chunk)
            if key in seen:
                continue
            seen.add(key)
            completed.append(result)
        completed.sort(key=lambda result: _evidence_chunk_order(result.chunk, required_facets))
        return completed[:top_k]

    def _matching_chunks(
        self,
        product_id: str,
        *,
        doc_types: set[str],
        sources: set[str],
        facet: str | None = None,
    ) -> list[DocumentChunk]:
        chunks = []
        for chunk in self.chunks_by_product_id.get(product_id, []):
            if sources and chunk.source not in sources:
                continue
            if _doc_type(chunk) not in doc_types:
                continue
            if facet and facet not in _chunk_aspects(chunk) and facet not in chunk.text.lower():
                continue
            chunks.append(chunk)
        chunks.sort(key=lambda chunk: _evidence_chunk_order(chunk, {facet} if facet else set()))
        return chunks


def constrain_results_to_entity(results: list[SearchResult], product_id: str) -> list[SearchResult]:
    if not product_id:
        return results
    scoped: list[SearchResult] = []
    neutral: list[SearchResult] = []
    for result in results:
        chunk_product_id = str(result.chunk.metadata.get("product_id", "")).strip()
        if chunk_product_id == product_id or result.chunk.doc_id.endswith(product_id):
            scoped.append(result)
        elif not chunk_product_id:
            neutral.append(result)
    return scoped + neutral


def should_clarify_for_entity(query: str, candidates: list[EntityCandidate], *, threshold: float = 0.34, margin: float = 0.08) -> bool:
    if not _requires_specific_product(query):
        return False
    if _has_explicit_identifier(query):
        return False
    if not candidates:
        return True
    if candidates[0].confidence < threshold:
        return True
    if len(candidates) > 1 and candidates[0].confidence - candidates[1].confidence < margin:
        return True
    return False


def _confidence(score: float, title_overlap: int) -> float:
    bonus = 0.1 if title_overlap >= 2 else 0.0
    return max(0.0, min(0.99, score + bonus))


def _content_tokens(text: str) -> set[str]:
    return {token for token in tokenize(text) if len(token) > 2 and token not in _STOPWORDS}


def _category_hint(tokens: set[str]) -> str:
    if tokens & {"baby", "infant", "toddler", "crib", "diaper", "feeding"}:
        return "baby_products"
    if tokens & {"software", "app", "license", "digital", "subscription", "game"}:
        return "software"
    if tokens & {"beauty", "skin", "scent", "serum", "facial", "hair", "nail"}:
        return "all_beauty"
    return ""


def _requires_specific_product(query: str) -> bool:
    tokens = set(tokenize(query))
    return bool(
        tokens
        & {
            "rating",
            "reviews",
            "review",
            "complaints",
            "issues",
            "smell",
            "scent",
            "features",
            "price",
            "dimensions",
            "battery",
            "support",
            "refund",
            "return",
            "defective",
            "damaged",
            "license",
        }
    )


def _has_explicit_identifier(query: str) -> bool:
    return bool(re.search(r"\bB[0-9A-Z]{9}\b|\bP-[A-Z]+-\d+\b|\b[A-Z]+-[A-Z0-9-]{3,}\b|\bORD-\d+\b", query, flags=re.IGNORECASE))


def _doc_type(chunk: DocumentChunk) -> str:
    return str(chunk.metadata.get("doc_type") or chunk.metadata.get("document_type") or chunk.source)


def _evidence_chunk_order(chunk: DocumentChunk, required_facets: set[str] | None = None) -> tuple[int, int, str, str]:
    required_facets = required_facets or set()
    priority = {
        "product_profile": 0,
        "product": 0,
        "review_aspect_summary": 1,
        "review_evidence": 2,
        "review": 2,
        "faq_case": 3,
        "ticket": 3,
    }
    facet_penalty = 0
    if required_facets and not (_chunk_aspects(chunk) & required_facets):
        facet_penalty = 1
    return (priority.get(_doc_type(chunk), 9), facet_penalty, chunk.source, chunk.doc_id)


def _result_product_id(result: SearchResult) -> str:
    return str(result.chunk.metadata.get("product_id", "")).strip()


def _chunk_key(chunk: DocumentChunk) -> tuple[str, str, str]:
    return (chunk.source, chunk.doc_id, chunk.chunk_id)


def _chunk_aspects(chunk: DocumentChunk) -> set[str]:
    aspects: set[str] = set()
    aspect = str(chunk.metadata.get("aspect", "")).lower().strip()
    if aspect:
        aspects.add(aspect)
    raw_aspects = chunk.metadata.get("aspects", [])
    if isinstance(raw_aspects, list):
        aspects.update(str(item).lower().strip() for item in raw_aspects if str(item).strip())
    return aspects


def _sku_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


_STOPWORDS = {
    "the",
    "and",
    "for",
    "with",
    "this",
    "that",
    "these",
    "those",
    "product",
    "products",
    "item",
    "items",
    "review",
    "reviews",
    "rating",
    "customer",
    "customers",
    "what",
    "which",
    "does",
    "about",
    "have",
    "from",
    "your",
    "their",
    "available",
    "common",
    "support",
    "options",
}
