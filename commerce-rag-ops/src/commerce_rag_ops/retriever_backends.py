from __future__ import annotations

from dataclasses import dataclass
import hashlib
import time
from typing import Iterable, Protocol

from .embeddings import EmbeddingModel, build_embedding_model
from .models import DocumentChunk, SearchResult
from .rerankers import CrossEncoderReranker, build_env_reranker
from .retrieval import HybridRetriever, RetrievalMode, reciprocal_rank_fusion


class RetrieverBackend(Protocol):
    def search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        """Return ranked retrieval results."""


@dataclass
class LocalHybridBackend:
    """Dependency-free backend used by tests, CLI, and local demos."""

    chunks: list[DocumentChunk]

    def __post_init__(self) -> None:
        self.retriever = HybridRetriever(self.chunks)

    def search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        return self.retriever.search(query, sources=sources, top_k=top_k, candidate_k=candidate_k, mode=mode)


class QdrantBackend:
    """Local Qdrant backend with pluggable embeddings.

    It supports embedded local Qdrant (`path=...`) for resume demos and tests.
    Use `embedding_backend=sentence-transformers` for local neural embeddings,
    or keep `hash` for dependency-free tests.
    """

    def __init__(
        self,
        collection_name: str,
        *,
        chunks: list[DocumentChunk] | None = None,
        path: str | None = None,
        url: str | None = None,
        embedding_model: EmbeddingModel | None = None,
        embedding_backend: str = "hash",
        embedding_model_name: str = "BAAI/bge-large-en-v1.5",
        embedding_device: str = "cuda",
        embedding_batch_size: int = 64,
        reranker: CrossEncoderReranker | None = None,
    ):
        try:
            from qdrant_client import QdrantClient  # type: ignore
        except ImportError as exc:
            raise RuntimeError("Install qdrant-client and run Qdrant before using QdrantBackend.") from exc
        if path:
            self.client = QdrantClient(path=path)
        else:
            self.client = QdrantClient(url=url or "http://localhost:6333")
        self.collection_name = collection_name
        self.chunks = chunks or []
        self.embedding_model = embedding_model or build_embedding_model(
            embedding_backend,
            model_name=embedding_model_name,
            device=embedding_device,
            batch_size=embedding_batch_size,
        )
        self.reranker = reranker or build_env_reranker()

    def recreate(self, chunks: list[DocumentChunk]) -> int:
        from qdrant_client.models import Distance, PointStruct, VectorParams  # type: ignore

        self.chunks = chunks
        if self.client.collection_exists(self.collection_name):
            self.client.delete_collection(self.collection_name)
        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(size=self.embedding_model.dimensions, distance=Distance.COSINE),
        )
        batch_size = 512
        total = 0
        for start in range(0, len(chunks), batch_size):
            batch = chunks[start : start + batch_size]
            vectors = self.embedding_model.encode_documents([chunk.text for chunk in batch])
            points = []
            for offset, (chunk, vector) in enumerate(zip(batch, vectors)):
                idx = start + offset
                points.append(
                    PointStruct(
                        id=idx,
                        vector=vector,
                        payload={
                            "idx": idx,
                            "chunk_id": chunk.chunk_id,
                            "source": chunk.source,
                            "doc_id": chunk.doc_id,
                            "text": chunk.text,
                            "metadata": chunk.metadata,
                            "embedding_model": self.embedding_model.name,
                            "embedding_dimensions": self.embedding_model.dimensions,
                        },
                    )
                )
            if points:
                self.client.upsert(collection_name=self.collection_name, points=points)
                total += len(points)
        return total

    def search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        started = time.perf_counter()
        if mode == "bm25":
            retriever = HybridRetriever(self.chunks, reranker=None, use_env_reranker=False)
            results = retriever.search(
                query,
                sources=sources,
                top_k=top_k,
                candidate_k=candidate_k,
                mode="bm25",
            )
            self.last_diagnostics = getattr(retriever, "last_diagnostics", _diagnostics_from_results(query, sources, mode, results, started))
            return results
        if mode in {"hybrid", "hybrid_rerank"}:
            results = self._hybrid_search(query, sources=sources, top_k=top_k, candidate_k=candidate_k, mode=mode)
            self.last_diagnostics = _diagnostics_from_results(query, sources, mode, results, started)
            return results
        results = self._dense_search(query, sources=sources, top_k=top_k, candidate_k=candidate_k)
        self.last_diagnostics = _diagnostics_from_results(query, sources, mode, results, started)
        return results

    def _dense_search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
    ) -> list[SearchResult]:
        source_filter = set(sources or [])
        query_vector = self.embedding_model.encode_query(query)
        limit = max(candidate_k, top_k) * (3 if source_filter else 1)
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,
            limit=limit,
            with_payload=True,
        )
        results: list[SearchResult] = []
        for point in response.points:
            payload = point.payload or {}
            if source_filter and payload.get("source") not in source_filter:
                continue
            chunk = DocumentChunk(
                chunk_id=str(payload["chunk_id"]),
                source=str(payload["source"]),
                doc_id=str(payload["doc_id"]),
                text=str(payload["text"]),
                metadata=dict(payload.get("metadata") or {}),
            )
            results.append(
                SearchResult(
                    chunk=chunk,
                    score=float(point.score),
                    dense_rank=len(results) + 1,
                    bm25_rank=None,
                    rerank_score=float(point.score),
                )
            )
            if len(results) >= candidate_k:
                break
        return results[:top_k]

    def _hybrid_search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        dense_results = self._dense_search(query, sources=sources, top_k=candidate_k, candidate_k=candidate_k)
        bm25_results = HybridRetriever(self.chunks, reranker=None, use_env_reranker=False).search(
            query,
            sources=sources,
            top_k=candidate_k,
            candidate_k=candidate_k,
            mode="bm25",
        )
        dense_rank_keys = [_result_key(result) for result in dense_results]
        bm25_rank_keys = [_result_key(result) for result in bm25_results]
        rrf_scores = reciprocal_rank_fusion(
            [
                list(range(len(dense_rank_keys))),
                list(range(len(dense_rank_keys), len(dense_rank_keys) + len(bm25_rank_keys))),
            ]
        )
        key_to_result: dict[tuple[str, str, str], SearchResult] = {}
        synthetic_index_to_key: dict[int, tuple[str, str, str]] = {}
        for idx, result in enumerate(dense_results):
            key = _result_key(result)
            key_to_result[key] = result
            synthetic_index_to_key[idx] = key
        offset = len(dense_results)
        for idx, result in enumerate(bm25_results):
            key = _result_key(result)
            key_to_result.setdefault(key, result)
            synthetic_index_to_key[offset + idx] = key

        fused_scores: dict[tuple[str, str, str], float] = {}
        for synthetic_idx, score in rrf_scores.items():
            key = synthetic_index_to_key[synthetic_idx]
            fused_scores[key] = fused_scores.get(key, 0.0) + score

        dense_ranks = {key: rank for rank, key in enumerate(dense_rank_keys, start=1)}
        bm25_ranks = {key: rank for rank, key in enumerate(bm25_rank_keys, start=1)}
        results = [
            SearchResult(
                chunk=result.chunk,
                score=fused_scores.get(key, 0.0),
                dense_rank=dense_ranks.get(key),
                bm25_rank=bm25_ranks.get(key),
                rerank_score=fused_scores.get(key, 0.0),
            )
            for key, result in key_to_result.items()
        ]
        results.sort(key=lambda item: item.score, reverse=True)
        if mode == "hybrid_rerank" and results:
            reranker = HybridRetriever(
                [result.chunk for result in results],
                reranker=self.reranker,
                use_env_reranker=False,
            )
            reranked = reranker.search(query, sources=sources, top_k=top_k, candidate_k=len(results), mode="hybrid_rerank")
            return reranked
        return results[:top_k]

    def close(self) -> None:
        close = getattr(self.client, "close", None)
        if callable(close):
            close()


def _result_key(result: SearchResult) -> tuple[str, str, str]:
    chunk = result.chunk
    return (chunk.source, chunk.doc_id, chunk.chunk_id)


def _diagnostics_from_results(
    query: str,
    sources: Iterable[str] | None,
    mode: RetrievalMode,
    results: list[SearchResult],
    started: float,
) -> dict:
    return {
        "query": query,
        "sources": list(sources or []),
        "mode": mode,
        "latency_ms": int((time.perf_counter() - started) * 1000),
        "stages": [
            {
                "name": f"qdrant.{mode}",
                "duration_ms": int((time.perf_counter() - started) * 1000),
                "selected": len(results),
            }
        ],
        "candidates": [
            {
                "source": result.chunk.source,
                "doc_id": result.chunk.doc_id,
                "chunk_id": result.chunk.chunk_id,
                "doc_type": result.chunk.metadata.get("doc_type") or result.chunk.metadata.get("document_type") or result.chunk.source,
                "rank_dense": result.dense_rank,
                "rank_bm25": result.bm25_rank,
                "rank_rrf": None,
                "rank_final": rank,
                "dense_score": result.score if result.dense_rank else None,
                "bm25_score": None,
                "rrf_score": result.score,
                "rerank_score": result.rerank_score,
                "forced": False,
                "forced_reason": None,
                "selected": True,
                "dropped_reason": None,
                "content_hash": "sha256:" + hashlib.sha256(result.chunk.text.encode("utf-8")).hexdigest(),
                "preview": result.chunk.text[:160],
            }
            for rank, result in enumerate(results, start=1)
        ],
    }
