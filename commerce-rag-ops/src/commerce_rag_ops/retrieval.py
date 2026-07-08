from __future__ import annotations

import math
import re
import hashlib
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from typing import Iterable, Literal

from .models import DocumentChunk, SearchResult
from .rerankers import CrossEncoderReranker, build_env_reranker
from .text import cosine_similarity, expand_query, tokenize

RetrievalMode = Literal["dense", "bm25", "hybrid", "hybrid_rerank"]


def reciprocal_rank_fusion(rankings: list[list[int]], k: int = 60) -> dict[int, float]:
    scores: dict[int, float] = defaultdict(float)
    for ranking in rankings:
        for rank, doc_index in enumerate(ranking, start=1):
            scores[doc_index] += 1.0 / (k + rank)
    return dict(scores)


def _chunk_key(chunk: DocumentChunk) -> tuple[str, str, str]:
    return (chunk.source, chunk.doc_id, chunk.chunk_id)


def _content_hash(text: str) -> str:
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()


@dataclass
class HybridRetriever:
    chunks: list[DocumentChunk]
    reranker: CrossEncoderReranker | None = None
    use_env_reranker: bool = True

    def __post_init__(self) -> None:
        if self.reranker is None and self.use_env_reranker:
            self.reranker = build_env_reranker()
        self.tokens = [tokenize(chunk.text) for chunk in self.chunks]
        self.indices_by_doc_type: dict[str, list[int]] = defaultdict(list)
        self.indices_by_doc_type_title_token: dict[tuple[str, str], list[int]] = defaultdict(list)
        self.indices_by_doc_type_title_key: dict[tuple[str, str], list[int]] = defaultdict(list)
        self.indices_by_doc_type_product_id: dict[tuple[str, str], list[int]] = defaultdict(list)
        self.indices_by_doc_type_product_aspect: dict[tuple[str, str, str], list[int]] = defaultdict(list)
        self.indices_by_product_id: dict[str, list[int]] = defaultdict(list)
        self.indices_by_review_id: dict[str, list[int]] = defaultdict(list)
        self.product_ids_by_title_key: dict[str, set[str]] = defaultdict(set)
        self.title_tokens_by_product_id: dict[str, set[str]] = {}
        self.normalized_title_by_product_id: dict[str, str] = {}
        self.curated_product_tokens_by_product_id: dict[str, set[str]] = defaultdict(set)
        self.product_ids_by_sku: dict[str, set[str]] = defaultdict(set)
        for idx, chunk in enumerate(self.chunks):
            doc_type = _chunk_doc_type(chunk)
            self.indices_by_doc_type[doc_type].append(idx)
            title = str(chunk.metadata.get("title", ""))
            title_key = _title_key(title)
            product_id = str(chunk.metadata.get("product_id", "")).strip()
            if product_id:
                self.indices_by_product_id[product_id].append(idx)
                self.indices_by_doc_type_product_id[(doc_type, product_id)].append(idx)
                for aspect in _chunk_aspects(chunk):
                    self.indices_by_doc_type_product_aspect[(doc_type, product_id, aspect)].append(idx)
                if title:
                    self.title_tokens_by_product_id.setdefault(product_id, set(tokenize(title)))
                    self.normalized_title_by_product_id.setdefault(product_id, _normalized_title(title))
                if title_key:
                    self.product_ids_by_title_key[title_key].add(product_id)
                if not bool(chunk.metadata.get("scale_dataset")):
                    sku = str(chunk.metadata.get("sku", "")).strip()
                    if sku:
                        self.product_ids_by_sku[_sku_key(sku)].add(product_id)
                    self.curated_product_tokens_by_product_id[product_id].update(_significant_tokens(chunk.text))
            review_id = str(chunk.metadata.get("review_id", "")).strip()
            if review_id:
                self.indices_by_review_id[review_id].append(idx)
            if title_key:
                self.indices_by_doc_type_title_key[(doc_type, title_key)].append(idx)
            for token in set(tokenize(title)):
                if len(token) > 2:
                    self.indices_by_doc_type_title_token[(doc_type, token)].append(idx)
        self.term_freqs = [Counter(tokens) for tokens in self.tokens]
        self.doc_freq: Counter[str] = Counter()
        for tokens in self.tokens:
            for token in set(tokens):
                self.doc_freq[token] += 1
        self.avg_doc_len = sum(len(tokens) for tokens in self.tokens) / max(len(self.tokens), 1)
        self.idf = {
            token: math.log(1 + (len(self.chunks) - df + 0.5) / (df + 0.5))
            for token, df in self.doc_freq.items()
        }

    def search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        search_started = time.perf_counter()
        self.last_diagnostics = {
            "query": query,
            "sources": list(sources or []),
            "mode": mode,
            "top_k": top_k,
            "candidate_k": candidate_k,
            "stages": [],
            "candidates": [],
        }
        source_filter = set(sources or [])
        allowed = [
            idx
            for idx, chunk in enumerate(self.chunks)
            if not source_filter or chunk.source in source_filter
        ]
        if not allowed:
            self.last_diagnostics["stages"].append({"name": "source_filter", "duration_ms": 0, "allowed": 0})
            return []

        stage_started = time.perf_counter()
        query_product_ids = self._query_product_ids(query)
        query_rating = _extract_query_rating(query)
        query_aspect = _extract_query_aspect(query)
        query_token_set = set(tokenize(query))
        support_review_ids = self._support_derived_review_ids(query, query_product_ids, query_aspect)
        self.last_diagnostics["stages"].append(
            {
                "name": "query_analysis",
                "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                "query_product_ids": sorted(query_product_ids),
                "query_rating": query_rating,
                "query_aspect": query_aspect,
                "support_review_ids": sorted(support_review_ids),
            }
        )
        stage_started = time.perf_counter()
        dense_scores = self._dense_scores(query, allowed)
        self.last_diagnostics["stages"].append(
            {"name": "dense.search", "duration_ms": int((time.perf_counter() - stage_started) * 1000), "candidates": len(dense_scores)}
        )
        stage_started = time.perf_counter()
        bm25_scores = self._bm25_scores(query, allowed)
        self.last_diagnostics["stages"].append(
            {"name": "bm25.search", "duration_ms": int((time.perf_counter() - stage_started) * 1000), "candidates": len(bm25_scores)}
        )
        stage_started = time.perf_counter()
        dense_rank = [idx for idx, _ in sorted(dense_scores.items(), key=lambda x: x[1], reverse=True)[:candidate_k]]
        bm25_rank = [idx for idx, _ in sorted(bm25_scores.items(), key=lambda x: x[1], reverse=True)[:candidate_k]]
        dense_ranks = {idx: rank for rank, idx in enumerate(dense_rank, start=1)}
        bm25_ranks = {idx: rank for rank, idx in enumerate(bm25_rank, start=1)}
        forced_reasons: dict[int, str] = {}
        rrf_scores: dict[int, float] = {}

        if mode == "dense":
            candidates = [(idx, dense_scores[idx]) for idx in dense_rank[:candidate_k]]
        elif mode == "bm25":
            candidates = [(idx, bm25_scores[idx]) for idx in bm25_rank[:candidate_k]]
        else:
            rrf_scores = reciprocal_rank_fusion([dense_rank, bm25_rank])
            candidates = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)[:candidate_k]
            self.last_diagnostics["stages"].append(
                {
                    "name": "rrf.fusion",
                    "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                    "dense_ranked": len(dense_rank),
                    "bm25_ranked": len(bm25_rank),
                    "fused_candidates": len(candidates),
                }
            )
            stage_started = time.perf_counter()
            forced_doc_type = self._forced_doc_type_candidates(query, allowed, set(idx for idx, _ in candidates))
            for idx in forced_doc_type:
                forced_reasons[idx] = "doc_type_policy"
            forced_entity = self._forced_curated_entity_candidates(
                query_product_ids,
                allowed,
                set(idx for idx, _ in candidates) | set(forced_doc_type),
            )
            for idx in forced_entity:
                forced_reasons[idx] = "curated_entity"
            forced_support = self._forced_support_evidence_candidates(
                query,
                query_product_ids,
                query_aspect,
                allowed,
                set(idx for idx, _ in candidates) | set(forced_doc_type) | set(forced_entity),
            )
            for idx in forced_support:
                forced_reasons[idx] = "support_lineage"
            forced = forced_doc_type + forced_entity + forced_support
            candidates.extend((idx, 0.0) for idx in forced)
            self.last_diagnostics["stages"].append(
                {
                    "name": "forced_candidates",
                    "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                    "doc_type_added": len(forced_doc_type),
                    "entity_added": len(forced_entity),
                    "support_added": len(forced_support),
                }
            )

        if mode in {"dense", "bm25"}:
            self.last_diagnostics["stages"].append(
                {
                    "name": f"{mode}.ranking",
                    "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                    "ranked_candidates": len(candidates),
                }
            )

        stage_started = time.perf_counter()
        results: list[SearchResult] = []
        for idx, base_score in candidates:
            rerank = self._rerank_score(
                query,
                self.chunks[idx],
                dense_scores.get(idx, 0.0),
                bm25_scores.get(idx, 0.0),
                query_product_ids=query_product_ids,
                query_rating=query_rating,
                query_aspect=query_aspect,
                query_tokens=query_token_set,
                support_review_ids=support_review_ids,
            )
            results.append(
                SearchResult(
                    chunk=self.chunks[idx],
                    score=base_score,
                    dense_rank=dense_ranks.get(idx),
                    bm25_rank=bm25_ranks.get(idx),
                    rerank_score=rerank,
                )
            )
        self.last_diagnostics["stages"].append(
            {
                "name": "heuristic_rerank",
                "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                "candidates": len(results),
            }
        )
        if mode == "hybrid_rerank":
            results.sort(key=lambda r: (r.rerank_score or 0.0, r.score), reverse=True)
            if self.reranker is not None:
                stage_started = time.perf_counter()
                results = self.reranker.rerank(query, results[: max(candidate_k, top_k)])
                self.last_diagnostics["stages"].append(
                    {
                        "name": "cross_encoder_rerank",
                        "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                        "model": self.reranker.model_name,
                        "candidates": len(results),
                    }
                )
        else:
            results.sort(key=lambda r: r.score, reverse=True)
        stage_started = time.perf_counter()
        final_results = _diversify_results(
            results,
            top_k,
            query,
            product_ids=query_product_ids,
            rating=query_rating,
            aspect=query_aspect,
            support_review_ids=support_review_ids,
        )
        self.last_diagnostics["stages"].append(
            {
                "name": "diversify",
                "duration_ms": int((time.perf_counter() - stage_started) * 1000),
                "input_candidates": len(results),
                "selected": len(final_results),
            }
        )
        selected_keys = {_chunk_key(result.chunk): rank for rank, result in enumerate(final_results, start=1)}
        result_scores = {_chunk_key(result.chunk): result for result in results}
        rrf_ranks = {idx: rank for rank, (idx, _) in enumerate(sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True), start=1)}
        candidate_rows = []
        for idx, base_score in candidates:
            chunk = self.chunks[idx]
            key = _chunk_key(chunk)
            final_rank = selected_keys.get(key)
            ranked_result = result_scores.get(key)
            candidate_rows.append(
                {
                    "source": chunk.source,
                    "doc_id": chunk.doc_id,
                    "chunk_id": chunk.chunk_id,
                    "doc_type": _chunk_doc_type(chunk),
                    "rank_dense": dense_ranks.get(idx),
                    "rank_bm25": bm25_ranks.get(idx),
                    "rank_rrf": rrf_ranks.get(idx),
                    "rank_final": final_rank,
                    "dense_score": round(dense_scores.get(idx, 0.0), 6),
                    "bm25_score": round(bm25_scores.get(idx, 0.0), 6),
                    "rrf_score": round(rrf_scores.get(idx, 0.0), 6),
                    "rerank_score": round((ranked_result.rerank_score if ranked_result else None) or 0.0, 6),
                    "forced": idx in forced_reasons,
                    "forced_reason": forced_reasons.get(idx),
                    "selected": final_rank is not None,
                    "dropped_reason": None if final_rank is not None else "diversify_or_top_k",
                    "content_hash": _content_hash(chunk.text),
                    "preview": chunk.text[:160],
                }
            )
        self.last_diagnostics["candidates"] = candidate_rows
        self.last_diagnostics["latency_ms"] = int((time.perf_counter() - search_started) * 1000)
        return final_results

    def _query_product_ids(self, query: str) -> set[str]:
        sku_matches = self._query_product_ids_by_sku(query)
        if sku_matches:
            return sku_matches
        query_title = _extract_query_title(query)
        title_key = _title_key(query_title)
        if not title_key:
            return self._query_curated_product_ids(query)
        candidates = set(self.product_ids_by_title_key.get(title_key, set()))
        query_tokens = set(tokenize(query_title))
        if not candidates or not query_tokens:
            return candidates
        query_title_norm = _normalized_title(query_title)
        exact_matches = {
            product_id
            for product_id in candidates
            if query_title_norm and self.normalized_title_by_product_id.get(product_id) == query_title_norm
        }
        if exact_matches:
            return exact_matches
        query_numbers = {token for token in query_tokens if token.isdigit()}
        scored: list[tuple[str, float]] = []
        for product_id in candidates:
            title_tokens = self.title_tokens_by_product_id.get(product_id, set())
            if query_numbers and not query_numbers.issubset({token for token in title_tokens if token.isdigit()}):
                continue
            score = len(query_tokens & title_tokens) / max(len(query_tokens), 1)
            if score >= 0.72:
                scored.append((product_id, score))
        if not scored:
            return candidates
        best = max(score for _, score in scored)
        return {product_id for product_id, score in scored if score >= best - 0.02}

    def _query_product_ids_by_sku(self, query: str) -> set[str]:
        product_ids: set[str] = set()
        for token in re.findall(r"[a-z0-9][a-z0-9-]{2,}", query.lower()):
            product_ids.update(self.product_ids_by_sku.get(_sku_key(token), set()))
        return product_ids

    def _query_curated_product_ids(self, query: str) -> set[str]:
        query_tokens = _significant_tokens(query)
        if query_tokens & {"trend", "cluster"}:
            return set()
        if not query_tokens:
            return set()
        scored: list[tuple[str, float, int]] = []
        for product_id, product_tokens in self.curated_product_tokens_by_product_id.items():
            overlap = query_tokens & product_tokens
            if not overlap:
                continue
            score = len(overlap) / max(len(query_tokens), 1)
            if len(overlap) >= 2 or (score >= 0.28 and query_tokens & {"baby", "beauty", "software"}):
                scored.append((product_id, score, len(overlap)))
        if not scored:
            return set()
        best_score = max(score for _, score, _ in scored)
        best_overlap = max(overlap for _, _, overlap in scored)
        min_overlap = 1 if best_overlap == 1 and query_tokens & {"baby", "beauty", "software"} else max(2, best_overlap - 1)
        return {
            product_id
            for product_id, score, overlap in scored
            if score >= best_score - 0.04 and overlap >= min_overlap
        }

    def _support_derived_review_ids(self, query: str, product_ids: set[str], aspect: str) -> set[str]:
        query_tokens = set(tokenize(query))
        if not product_ids or not (query_tokens & {"support", "handle", "case"}):
            return set()
        review_ids: set[str] = set()
        for product_id in product_ids:
            faq_indices: list[int] = []
            if aspect:
                faq_indices.extend(self.indices_by_doc_type_product_aspect.get(("faq_case", product_id, aspect), []))
            faq_indices.extend(self.indices_by_doc_type_product_id.get(("faq_case", product_id), []))
            for idx in _unique_limited(faq_indices, 20):
                derived = str(self.chunks[idx].metadata.get("derived_from_review_id", "")).strip()
                if derived:
                    review_ids.add(derived)
        return review_ids

    def _dense_scores(self, query: str, allowed: list[int]) -> dict[int, float]:
        expanded_queries = expand_query(query)
        query_counter = Counter(tokenize(" ".join(expanded_queries)))
        scores: dict[int, float] = {}
        for idx in allowed:
            scores[idx] = cosine_similarity(query_counter, self.term_freqs[idx])
        return scores

    def _forced_doc_type_candidates(self, query: str, allowed: list[int], existing: set[int]) -> list[int]:
        query_tokens = set(tokenize(query))
        wanted: set[str] = set()
        if query_tokens & {"trend", "cluster", "negative", "complaint", "complaints"}:
            wanted.add("complaint_cluster")
            wanted.add("review_aspect_summary")
        if query_tokens & {"aspect", "issues", "customer", "ops", "around"}:
            wanted.add("review_aspect_summary")
            wanted.add("product_profile")
            wanted.add("review_evidence")
        if query_tokens & {"recommend", "summarize", "product"}:
            wanted.add("product_profile")
            wanted.add("review_aspect_summary")
            wanted.add("review_evidence")
        if query_tokens & {"review", "evidence", "feedback"}:
            wanted.add("review_evidence")
            wanted.add("product_profile")
            wanted.add("review_aspect_summary")
        if query_tokens & {"support", "handle", "case"}:
            wanted.add("faq_case")
            wanted.add("review_evidence")
            wanted.add("review_aspect_summary")
            wanted.add("policy_markdown")
            wanted.add("html_policy_page")
            wanted.add("structured_table")
        if query_tokens & {"refund", "return", "money", "warranty", "delivery", "shipping", "license", "cancel", "renewed", "renewal", "subscription", "missing"}:
            wanted.add("policy_markdown")
            wanted.add("html_policy_page")
            wanted.add("structured_table")
            wanted.add("text_notice")
            wanted.add("ocr_image")
        if not wanted:
            return []
        buckets: dict[str, list[int]] = {doc_type: [] for doc_type in wanted}
        query_text = " ".join(query_tokens)
        query_title_key = _title_key(_extract_query_title(query))
        query_product_ids = self._query_product_ids(query)
        query_rating = _extract_query_rating(query)
        query_aspect = _extract_query_aspect(query)
        allowed_set = set(allowed)
        scan_indices: list[int] = []
        for doc_type in wanted:
            for product_id in query_product_ids:
                if query_aspect:
                    scan_indices.extend(self.indices_by_doc_type_product_aspect.get((doc_type, product_id, query_aspect), []))
                scan_indices.extend(self.indices_by_doc_type_product_id.get((doc_type, product_id), []))
            if query_title_key:
                scan_indices.extend(self.indices_by_doc_type_title_key.get((doc_type, query_title_key), []))
            if doc_type in {"product_profile", "review_aspect_summary", "review_evidence", "faq_case"}:
                title_hits: list[int] = []
                for token in query_tokens:
                    if len(token) > 2:
                        title_hits.extend(self.indices_by_doc_type_title_token.get((doc_type, token), []))
                if title_hits:
                    scan_indices.extend(_unique_limited(title_hits, 500))
                else:
                    scan_indices.extend(self.indices_by_doc_type.get(doc_type, [])[:200])
            else:
                scan_indices.extend(self.indices_by_doc_type.get(doc_type, []))
        if not scan_indices:
            return []
        for idx in scan_indices:
            if idx not in allowed_set:
                continue
            if idx in existing:
                continue
            chunk = self.chunks[idx]
            doc_type = _chunk_doc_type(chunk)
            if doc_type not in wanted:
                continue
            category = str(chunk.metadata.get("category", "")).lower().replace("_", " ")
            aspect = str(chunk.metadata.get("aspect", "")).lower().replace("_", " ")
            title_tokens = set(tokenize(str(chunk.metadata.get("title", ""))))
            product_id = str(chunk.metadata.get("product_id", "")).strip()
            exact_product = product_id in query_product_ids if query_product_ids else False
            if query_rating is not None and doc_type == "review_evidence":
                try:
                    if int(chunk.metadata.get("rating", -1)) != query_rating:
                        continue
                except (TypeError, ValueError):
                    continue
            if query_aspect and doc_type in {"complaint_cluster", "review_aspect_summary"}:
                if str(chunk.metadata.get("aspect", "")).lower() != query_aspect:
                    continue
            if query_aspect and doc_type == "review_evidence" and query_product_ids:
                if query_aspect not in _chunk_aspects(chunk):
                    continue
            if category and not exact_product and not (set(category.split()) & query_tokens):
                continue
            if aspect and doc_type in {"complaint_cluster", "review_aspect_summary"} and not (set(aspect.split()) & query_tokens or aspect in query_text):
                continue
            if title_tokens and doc_type in {"product_profile", "review_aspect_summary", "review_evidence", "faq_case"}:
                if not exact_product and not (title_tokens & query_tokens):
                    continue
            buckets.setdefault(doc_type, []).append(idx)
        forced: list[int] = []
        for doc_type in _preferred_doc_types(query_tokens):
            if doc_type not in wanted:
                continue
            forced.extend(buckets.get(doc_type, [])[:30])
        for doc_type, values in buckets.items():
            if doc_type not in _preferred_doc_types(query_tokens):
                forced.extend(values[:15])
        if len(forced) > 120:
            forced = forced[:120]
        return forced

    def _forced_curated_entity_candidates(self, product_ids: set[str], allowed: list[int], existing: set[int]) -> list[int]:
        if not product_ids:
            return []
        allowed_set = set(allowed)
        preferred_sources = {"product": 0, "review": 1, "ticket": 2}
        candidates: list[tuple[int, int]] = []
        for product_id in product_ids:
            for idx in self.indices_by_product_id.get(product_id, []):
                if idx in existing or idx not in allowed_set:
                    continue
                chunk = self.chunks[idx]
                if bool(chunk.metadata.get("scale_dataset")):
                    continue
                candidates.append((preferred_sources.get(chunk.source, 3), idx))
        return [idx for _, idx in sorted(candidates)[:30]]

    def _forced_support_evidence_candidates(
        self,
        query: str,
        product_ids: set[str],
        aspect: str,
        allowed: list[int],
        existing: set[int],
    ) -> list[int]:
        query_tokens = set(tokenize(query))
        if not product_ids or not (query_tokens & {"support", "handle", "case"}):
            return []
        allowed_set = set(allowed)
        forced: list[int] = []
        seen = set(existing)

        def add(idx: int) -> None:
            if idx in seen or idx not in allowed_set:
                return
            seen.add(idx)
            forced.append(idx)

        faq_indices: list[int] = []
        for product_id in product_ids:
            if aspect:
                faq_indices.extend(self.indices_by_doc_type_product_aspect.get(("faq_case", product_id, aspect), []))
            faq_indices.extend(self.indices_by_doc_type_product_id.get(("faq_case", product_id), []))
        for idx in _unique_limited(faq_indices, 12):
            add(idx)
            derived_review_id = str(self.chunks[idx].metadata.get("derived_from_review_id", "")).strip()
            if derived_review_id:
                for review_idx in self.indices_by_review_id.get(derived_review_id, []):
                    add(review_idx)

        for product_id in product_ids:
            if aspect and aspect != "general_support":
                for idx in self.indices_by_doc_type_product_aspect.get(("review_aspect_summary", product_id, aspect), [])[:8]:
                    add(idx)
                for idx in self.indices_by_doc_type_product_aspect.get(("review_evidence", product_id, aspect), [])[:12]:
                    add(idx)
            else:
                for idx in self.indices_by_doc_type_product_id.get(("review_evidence", product_id), [])[:12]:
                    add(idx)
                for idx in self.indices_by_doc_type_product_id.get(("review_aspect_summary", product_id), [])[:8]:
                    add(idx)
        return forced[:40]

    def _bm25_scores(self, query: str, allowed: list[int]) -> dict[int, float]:
        query_tokens = tokenize(query)
        k1 = 1.2
        b = 0.75
        scores: dict[int, float] = {}
        for idx in allowed:
            tf = self.term_freqs[idx]
            doc_len = len(self.tokens[idx])
            score = 0.0
            for token in query_tokens:
                if token not in tf:
                    continue
                numerator = tf[token] * (k1 + 1)
                denominator = tf[token] + k1 * (1 - b + b * doc_len / max(self.avg_doc_len, 1))
                score += self.idf.get(token, 0.0) * numerator / denominator
            scores[idx] = score
        return scores

    def _rerank_score(
        self,
        query: str,
        chunk: DocumentChunk,
        dense: float,
        bm25: float,
        *,
        query_product_ids: set[str],
        query_rating: int | None,
        query_aspect: str,
        query_tokens: set[str],
        support_review_ids: set[str],
    ) -> float:
        chunk_tokens = set(tokenize(chunk.text))
        overlap = len(query_tokens & chunk_tokens) / max(len(query_tokens), 1)
        source_bonus = {
            "kb": 0.06,
            "ticket": 0.05,
            "product": 0.04,
            "review": 0.03,
        }.get(chunk.source, 0.0)
        rating_bonus = 0.0
        if chunk.source == "product":
            rating_bonus = float(chunk.metadata.get("average_rating", 0.0)) / 100.0
        review_intent_bonus = 0.0
        if chunk.source == "review" and query_tokens & {"review", "reviews", "negative", "complaint", "issues"}:
            review_intent_bonus += 0.08
            if int(chunk.metadata.get("rating", 5)) <= 3 and query_tokens & {"negative", "complaint", "issues"}:
                review_intent_bonus += 0.08
        entity_bonus = 0.0
        product_id = str(chunk.metadata.get("product_id", "")).strip()
        if query_product_ids:
            entity_bonus += 0.28 if product_id in query_product_ids else -0.08
        if query_rating is not None and "rating" in chunk.metadata:
            try:
                entity_bonus += 0.08 if int(chunk.metadata.get("rating", -1)) == query_rating else -0.04
            except (TypeError, ValueError):
                pass
        if query_aspect:
            aspects = _chunk_aspects(chunk)
            if aspects:
                entity_bonus += 0.12 if query_aspect in aspects else -0.05
            entity_bonus += _policy_match_bonus(query_aspect, chunk)
        entity_bonus += _policy_keyword_bonus(query_tokens, chunk)
        if query_product_ids and product_id in query_product_ids and not bool(chunk.metadata.get("scale_dataset")):
            entity_bonus += 0.18
        review_id = str(chunk.metadata.get("review_id", "")).strip()
        if support_review_ids and review_id in support_review_ids:
            entity_bonus += 0.24
        doc_type_bonus = self._doc_type_bonus(query_tokens, chunk)
        metadata_bonus = self._metadata_bonus(query_tokens, chunk)
        return (
            0.5 * dense
            + 0.25 * min(bm25 / 10.0, 1.0)
            + 0.14 * overlap
            + source_bonus
            + rating_bonus
            + review_intent_bonus
            + entity_bonus
            + doc_type_bonus
            + metadata_bonus
        )

    def _doc_type_bonus(self, query_tokens: set[str], chunk: DocumentChunk) -> float:
        doc_type = _chunk_doc_type(chunk)
        bonus = 0.0
        if doc_type in {"product_profile", "product"} and query_tokens & {"recommend", "summarize", "product", "rating", "signals"}:
            bonus += 0.2
        if doc_type in {"review_evidence", "review"} and query_tokens & {"review", "reviews", "evidence", "feedback", "rating"}:
            bonus += 0.12
        if doc_type == "ticket" and query_tokens & {"customer", "ops", "issues", "support", "case", "refund", "warranty", "cancel"}:
            bonus += 0.12
        if doc_type == "review_aspect_summary" and query_tokens & {"aspect", "issues", "customer", "ops", "around"}:
            bonus += 0.22
        if doc_type == "complaint_cluster" and query_tokens & {"trend", "cluster", "negative", "complaint", "complaints"}:
            bonus += 0.32
        if doc_type == "faq_case" and query_tokens & {"support", "handle", "case", "evidence"}:
            bonus += 0.2
        if doc_type in {"policy_markdown", "html_policy_page", "structured_table", "text_notice", "ocr_image"} and query_tokens & {"support", "handle", "case", "policy", "refund", "return", "delivery", "missing"}:
            bonus += 0.14
        if doc_type == "review_evidence" and query_tokens & {"trend", "cluster"}:
            bonus -= 0.08
        return bonus

    def _metadata_bonus(self, query_tokens: set[str], chunk: DocumentChunk) -> float:
        bonus = 0.0
        category = str(chunk.metadata.get("category", "")).lower()
        if category and set(category.replace("_", " ").split()) & query_tokens:
            bonus += 0.05
        aspect = str(chunk.metadata.get("aspect", "")).lower()
        if aspect:
            aspect_tokens = set(aspect.replace("_", " ").split())
            if aspect_tokens & query_tokens or aspect in " ".join(query_tokens):
                bonus += 0.08
        title = str(chunk.metadata.get("title", "")).lower()
        title_tokens = set(tokenize(title))
        if title_tokens:
            title_overlap = len(title_tokens & query_tokens) / max(len(query_tokens), 1)
            bonus += min(0.1, title_overlap * 0.25)
        return bonus


def _diversify_results(
    results: list[SearchResult],
    top_k: int,
    query: str,
    *,
    product_ids: set[str] | None = None,
    rating: int | None = None,
    aspect: str = "",
    support_review_ids: set[str] | None = None,
) -> list[SearchResult]:
    deduped: list[SearchResult] = []
    seen: set[tuple[str, str]] = set()
    for result in results:
        key = (result.chunk.source, result.chunk.doc_id)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(result)

    query_tokens = set(tokenize(query))
    preferred = _preferred_doc_types(query_tokens)
    selected: list[SearchResult] = []
    selected_doc_types: set[str] = set()
    exact_product_ids = product_ids or set()
    query_category = _extract_query_category(query)
    trend_query = bool(query_tokens & {"trend", "cluster", "complaint", "complaints"})
    evidence_query = bool(query_tokens & {"review", "reviews", "evidence", "feedback"})
    curated_scope = _is_curated_product_scope(exact_product_ids)
    strict_policy_types = _policy_types_for_query(query_tokens) if curated_scope else set()
    target_k = _curated_context_budget(query_tokens, top_k) if curated_scope else top_k
    support_lineage_ids = support_review_ids or set()

    if exact_product_ids:
        exact = [
            result
            for result in deduped
            if str(result.chunk.metadata.get("product_id", "")).strip() in exact_product_ids
        ]
        if rating is not None:
            rating_matches = [
                result
                for result in exact
                if _doc_type(result) != "review_evidence" or _metadata_int(result.chunk.metadata, "rating") == rating
            ]
            if rating_matches:
                exact = rating_matches
        if aspect:
            aspect_matches = [
                result
                for result in exact
                if _doc_type(result) not in {"review_aspect_summary", "complaint_cluster", "review_evidence"}
                or aspect in _chunk_aspects(result.chunk)
            ]
            if aspect_matches:
                exact = aspect_matches
        if exact:
            deduped = exact + [result for result in deduped if result not in exact]
    if query_tokens & {"support", "handle", "case"} and aspect == "general_support" and exact_product_ids:
        deduped = sorted(
            deduped,
            key=lambda result: _support_general_result_order(result, support_lineage_ids),
        )
    if not curated_scope and query_tokens & {"support", "handle", "case"}:
        target_k = _support_context_budget(deduped, exact_product_ids, aspect, top_k)

    evidence_pack = _matching_review_evidence(deduped, exact_product_ids, rating)
    if not curated_scope and evidence_query and rating is not None and len(evidence_pack) >= top_k:
        return evidence_pack[:top_k]

    for doc_type in preferred:
        match = None
        if exact_product_ids and doc_type == "review_aspect_summary" and evidence_query and rating is not None:
            covered_aspects = _selected_review_aspects(selected)
            if covered_aspects:
                match = next(
                    (
                        result
                        for result in deduped
                        if _doc_type(result) == doc_type
                        and result not in selected
                        and _result_product_id(result) in exact_product_ids
                        and not (_chunk_aspects(result.chunk) & covered_aspects)
                        and _result_allowed_for_query(
                            result,
                            exact_product_ids,
                            query_category,
                            trend_query,
                            aspect,
                            evidence_query,
                            rating,
                            query_tokens,
                            strict_policy_types,
                            curated_scope,
                        )
                    ),
                    None,
                )
        if exact_product_ids and doc_type in _PRODUCT_SCOPED_DOC_TYPES:
            if match is None:
                match = next(
                    (
                        result
                        for result in deduped
                        if _doc_type(result) == doc_type
                        and result not in selected
                        and _result_product_id(result) in exact_product_ids
                        and _result_allowed_for_query(
                            result,
                            exact_product_ids,
                            query_category,
                            trend_query,
                            aspect,
                            evidence_query,
                            rating,
                            query_tokens,
                            strict_policy_types,
                            curated_scope,
                        )
                    ),
                    None,
                )
        if match is None:
            match = next(
                (
                    result
                    for result in deduped
                    if _doc_type(result) == doc_type
                    and result not in selected
                    and (not exact_product_ids or _result_product_id(result) in exact_product_ids or not _result_product_id(result) or doc_type not in _PRODUCT_SCOPED_DOC_TYPES)
                    and _result_allowed_for_query(
                        result,
                        exact_product_ids,
                        query_category,
                        trend_query,
                        aspect,
                        evidence_query,
                        rating,
                        query_tokens,
                        strict_policy_types,
                        curated_scope,
                    )
                ),
                None,
            )
        if match:
            selected.append(match)
            selected_doc_types.add(doc_type)
        if len(selected) >= target_k:
            return selected

    if exact_product_ids:
        for result in deduped:
            if result in selected:
                continue
            product_id = _result_product_id(result)
            if product_id and product_id not in exact_product_ids and _doc_type(result) in _PRODUCT_SCOPED_DOC_TYPES:
                continue
            if not _result_allowed_for_query(
                result,
                exact_product_ids,
                query_category,
                trend_query,
                aspect,
                evidence_query,
                rating,
                query_tokens,
                strict_policy_types,
                curated_scope,
            ):
                continue
            selected.append(result)
            selected_doc_types.add(_doc_type(result))
            if len(selected) >= target_k:
                return selected

    for result in deduped:
        doc_type = _doc_type(result)
        if result in selected:
            continue
        if not _result_allowed_for_query(
            result,
            exact_product_ids,
            query_category,
            trend_query,
            aspect,
            evidence_query,
            rating,
            query_tokens,
            strict_policy_types,
            curated_scope,
        ):
            continue
        if len(selected) >= max(3, target_k - 1) and doc_type in selected_doc_types:
            continue
        selected.append(result)
        selected_doc_types.add(doc_type)
        if len(selected) >= target_k:
            return selected

    for result in deduped:
        if result not in selected:
            if not _result_allowed_for_query(
                result,
                exact_product_ids,
                query_category,
                trend_query,
                aspect,
                evidence_query,
                rating,
                query_tokens,
                strict_policy_types,
                curated_scope,
            ):
                continue
            selected.append(result)
        if len(selected) >= target_k:
            break
    return selected


def _doc_type(result: SearchResult) -> str:
    return _chunk_doc_type(result.chunk)


_PRODUCT_SCOPED_DOC_TYPES = {
    "product_profile",
    "review_evidence",
    "review_aspect_summary",
    "faq_case",
    "product",
    "review",
    "ticket",
}


def _result_product_id(result: SearchResult) -> str:
    return str(result.chunk.metadata.get("product_id", "")).strip()


def _matching_review_evidence(
    results: list[SearchResult],
    product_ids: set[str],
    rating: int | None,
) -> list[SearchResult]:
    if not product_ids or rating is None:
        return []
    return [
        result
        for result in results
        if _doc_type(result) == "review_evidence"
        and _result_product_id(result) in product_ids
        and _metadata_int(result.chunk.metadata, "rating") == rating
    ]


def _selected_review_aspects(results: list[SearchResult]) -> set[str]:
    aspects: set[str] = set()
    for result in results:
        if _doc_type(result) in {"review_evidence", "review"}:
            aspects.update(_chunk_aspects(result.chunk))
    return aspects


def _support_general_result_order(result: SearchResult, support_review_ids: set[str]) -> tuple[int, int]:
    if _doc_type(result) not in {"review_evidence", "review"}:
        return (0, 0)
    review_id = str(result.chunk.metadata.get("review_id", "")).strip()
    if review_id in support_review_ids:
        return (1, 0)
    return (2, _doc_sort_number(result.chunk.doc_id))


def _support_context_budget(
    results: list[SearchResult],
    product_ids: set[str],
    aspect: str,
    top_k: int,
) -> int:
    if not product_ids:
        return top_k
    if aspect == "general_support":
        faq_count = sum(
            1
            for result in results
            if _doc_type(result) == "faq_case" and _result_product_id(result) in product_ids
        )
        return top_k if faq_count > 1 else min(top_k, 4)
    if aspect == "battery_power":
        has_aspect_summary = any(
            _doc_type(result) == "review_aspect_summary"
            and _result_product_id(result) in product_ids
            and aspect in _chunk_aspects(result.chunk)
            for result in results
        )
        return top_k if has_aspect_summary else min(top_k, 4)
    return top_k


def _doc_sort_number(doc_id: str) -> int:
    match = re.search(r"(\d+)$", doc_id)
    return int(match.group(1)) if match else 999_999_999


def _result_allowed_for_query(
    result: SearchResult,
    exact_product_ids: set[str],
    query_category: str,
    trend_query: bool,
    query_aspect: str,
    evidence_query: bool,
    query_rating: int | None,
    query_tokens: set[str],
    strict_policy_types: set[str],
    curated_scope: bool,
) -> bool:
    doc_type = _doc_type(result)
    product_id = _result_product_id(result)
    support_query = bool(query_tokens & {"support", "handle", "case"})
    if exact_product_ids and product_id and product_id not in exact_product_ids and doc_type in _PRODUCT_SCOPED_DOC_TYPES:
        return False
    if support_query and doc_type == "complaint_cluster":
        return False
    if support_query and query_aspect == "general_support" and doc_type == "review_aspect_summary":
        return False
    if not support_query and query_aspect and exact_product_ids:
        if doc_type == "complaint_cluster":
            return False
        if doc_type in {"review_aspect_summary", "review_evidence", "complaint_cluster", "faq_case"}:
            if query_aspect not in _chunk_aspects(result.chunk):
                return False
    if support_query and query_aspect and query_aspect != "general_support":
        if doc_type == "review_aspect_summary" and query_aspect not in _chunk_aspects(result.chunk):
            return False
        if query_aspect == "battery_power" and result.chunk.source == "kb":
            if str(result.chunk.metadata.get("policy_type", "")).strip() == "reason_codes":
                return False
    if strict_policy_types and result.chunk.source == "kb":
        policy_type = str(result.chunk.metadata.get("policy_type", "")).strip()
        if policy_type not in strict_policy_types:
            return False
    if curated_scope and query_tokens & {"negative", "complaint", "complaints", "issues"}:
        if doc_type in {"review", "review_evidence"}:
            rating = _metadata_int(result.chunk.metadata, "rating")
            if rating is not None and rating >= 4:
                return False
    if curated_scope and query_tokens & {"good", "positive", "recommend"}:
        if doc_type in {"review", "review_evidence"}:
            rating = _metadata_int(result.chunk.metadata, "rating")
            if rating is not None and rating <= 3:
                return False
    if trend_query and query_category:
        category = str(result.chunk.metadata.get("category", "")).strip().lower()
        if category and category != query_category:
            return False
    if trend_query and query_aspect:
        aspects = _chunk_aspects(result.chunk)
        if doc_type == "complaint_cluster":
            return query_aspect in aspects or query_aspect in result.chunk.doc_id.lower()
        if doc_type in {"review_aspect_summary", "review_evidence", "faq_case"}:
            return query_aspect in aspects
    if evidence_query and exact_product_ids:
        if doc_type == "review_evidence" and query_rating is not None:
            return _metadata_int(result.chunk.metadata, "rating") == query_rating
        if doc_type == "complaint_cluster":
            return False
    if query_aspect in {"general_support", "skin_scent"} and result.chunk.source == "kb":
        return result.chunk.doc_id == "KB001_return_refund_policy"
    return True


def _is_curated_product_scope(product_ids: set[str]) -> bool:
    return bool(product_ids) and all(product_id.startswith("P-") for product_id in product_ids)


def _curated_context_budget(query_tokens: set[str], top_k: int) -> int:
    if query_tokens & {"negative", "complaint", "complaints", "issues", "customer", "ops"}:
        return min(top_k, 4)
    if query_tokens & {"recommend", "good", "positive"}:
        return min(top_k, 2)
    return min(top_k, 2)


def _policy_types_for_query(query_tokens: set[str]) -> set[str]:
    if query_tokens & {"warranty", "defect", "defective", "working", "stopped"}:
        return {"warranty_policy"}
    if query_tokens & {"renewed", "renewal", "subscription", "cancel", "payment"}:
        return {"payment_refund_policy"}
    if query_tokens & {"delivery", "shipping", "license", "email"}:
        return {"shipping_delivery_policy"}
    if query_tokens & {"missing", "part", "cap", "replacement", "replace"}:
        return {"missing_parts_policy"}
    if query_tokens & {"refund", "return", "money", "leaking", "broken", "damaged"}:
        return {"return_refund_policy"}
    return set()


def _chunk_aspects(chunk: DocumentChunk) -> set[str]:
    aspects: set[str] = set()
    aspect = str(chunk.metadata.get("aspect", "")).lower().strip()
    if aspect:
        aspects.add(aspect)
    raw_aspects = chunk.metadata.get("aspects", [])
    if isinstance(raw_aspects, list):
        aspects.update(str(item).lower().strip() for item in raw_aspects if str(item).strip())
    return aspects


def _chunk_doc_type(chunk: DocumentChunk) -> str:
    return str(chunk.metadata.get("doc_type") or chunk.metadata.get("document_type") or chunk.source)


def _preferred_doc_types(query_tokens: set[str]) -> list[str]:
    if query_tokens & {"trend", "cluster", "negative", "complaint", "complaints"}:
        return ["complaint_cluster", "review_aspect_summary", "review_evidence", "review", "ticket"]
    if query_tokens & {"review", "evidence", "feedback"}:
        return ["review_evidence", "product_profile", "product", "review_aspect_summary", "review"]
    if query_tokens & {"aspect", "issues", "customer", "ops", "around"}:
        return ["review_aspect_summary", "review_evidence", "review", "ticket", "product_profile", "product"]
    if query_tokens & {"support", "handle", "case"}:
        return ["faq_case", "ticket", "policy_markdown", "review_evidence", "review", "review_aspect_summary", "structured_table", "html_policy_page"]
    if query_tokens & {"recommend", "summarize", "product"}:
        return ["product_profile", "product", "review_aspect_summary", "review_evidence", "review"]
    return []


def _unique_limited(values: list[int], limit: int) -> list[int]:
    output: list[int] = []
    seen: set[int] = set()
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        output.append(value)
        if len(output) >= limit:
            break
    return output


def _metadata_int(metadata: dict[str, object], key: str) -> int | None:
    try:
        return int(metadata.get(key, -1))
    except (TypeError, ValueError):
        return None


def _extract_query_title(query: str) -> str:
    lowered = query.strip()
    patterns = [
        (r"recommend or summarize product (.+?) in [a-z_]+ using", 1),
        (r"find review evidence for (.+?) with rating", 1),
        (r"what customer ops issues appear for (.+?) around", 1),
        (r"how should support handle this .+? case for (.+?)(?:\?|$)", 1),
    ]
    normalized = lowered.lower()
    for pattern, group in patterns:
        match = re.search(pattern, normalized)
        if match:
            return match.group(group)
    return ""


def _extract_query_rating(query: str) -> int | None:
    match = re.search(r"\brating\s+([1-5])\b", query.lower())
    return int(match.group(1)) if match else None


def _extract_query_aspect(query: str) -> str:
    normalized = query.lower()
    patterns = [
        r"\baround\s+([a-z_]+)\??$",
        r"\bfor\s+([a-z_]+)\s+complaints\??$",
        r"\bthis\s+([a-z_]+)\s+case\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, normalized)
        if match:
            return match.group(1)
    return ""


def _extract_query_category(query: str) -> str:
    normalized = query.lower()
    for category in ("all_beauty", "baby_products", "software"):
        if category in normalized:
            return category
    return ""


def _policy_match_bonus(query_aspect: str, chunk: DocumentChunk) -> float:
    doc_type = _chunk_doc_type(chunk)
    if doc_type not in {"policy_markdown", "html_policy_page", "structured_table", "text_notice", "ocr_image"}:
        return 0.0
    policy_text = " ".join(
        [
            str(chunk.metadata.get("policy_type", "")),
            str(chunk.metadata.get("title", "")),
            str(chunk.metadata.get("filename", "")),
            chunk.text[:240],
        ]
    ).lower()
    wanted = {
        "delivery": {"shipping", "delivery", "carrier", "late_delivery"},
        "refund_return": {"refund", "return", "payment", "subscription"},
        "price_value": {"refund", "return", "payment", "reason_codes"},
        "missing_parts": {"missing", "part", "replacement"},
        "quality_damage": {"damage", "damaged", "defective", "warranty", "return", "missing"},
        "digital_license": {"digital", "license", "payment", "subscription", "delivery"},
        "battery_power": {"warranty", "defective", "return"},
    }.get(query_aspect, set())
    if not wanted:
        return 0.0
    if any(token in policy_text for token in wanted):
        return 0.16
    return -0.06


def _policy_keyword_bonus(query_tokens: set[str], chunk: DocumentChunk) -> float:
    doc_type = _chunk_doc_type(chunk)
    if doc_type not in {"policy_markdown", "html_policy_page", "structured_table", "text_notice", "ocr_image"}:
        return 0.0
    policy_text = " ".join(
        [
            str(chunk.metadata.get("policy_type", "")),
            str(chunk.metadata.get("title", "")),
            str(chunk.metadata.get("filename", "")),
            chunk.text[:300],
        ]
    ).lower()
    policy_rules = [
        ({"refund", "return", "money", "leaking", "broken", "damaged"}, {"return", "refund", "damage", "reason_codes"}),
        ({"warranty", "defect", "defective", "working", "stopped"}, {"warranty", "defect"}),
        ({"delivery", "shipping", "late", "license", "email"}, {"shipping", "delivery", "digital", "carrier"}),
        ({"cancel", "renewed", "renewal", "subscription", "money"}, {"payment", "subscription", "renewal", "refund"}),
        ({"missing", "part", "cap", "replace", "replacement"}, {"missing", "replacement", "part"}),
    ]
    for query_needles, policy_needles in policy_rules:
        if query_tokens & query_needles:
            if any(token in policy_text for token in policy_needles):
                return 0.16
    return 0.0


_SIGNIFICANT_STOPWORDS = {
    "the",
    "and",
    "with",
    "for",
    "from",
    "this",
    "that",
    "product",
    "products",
    "review",
    "reviews",
    "rating",
    "price",
    "good",
    "best",
    "recommend",
    "summarize",
    "what",
    "which",
    "about",
    "appear",
    "using",
    "context",
    "check",
    "can",
    "get",
    "available",
    "after",
    "before",
    "month",
    "one",
}


def _significant_tokens(text: str) -> set[str]:
    return {token for token in tokenize(text) if len(token) > 2 and token not in _SIGNIFICANT_STOPWORDS}


def _sku_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower())


def _title_key(title: str) -> str:
    stop = {
        "the",
        "and",
        "with",
        "for",
        "pack",
        "new",
        "set",
        "case",
        "from",
        "this",
        "that",
        "product",
    }
    tokens = [token for token in tokenize(title) if token not in stop and len(token) > 1]
    if not tokens:
        return ""
    return " ".join(tokens[:6])


def _normalized_title(title: str) -> str:
    return " ".join(tokenize(title))
