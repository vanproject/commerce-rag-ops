from __future__ import annotations

import os
from dataclasses import dataclass

from .models import SearchResult


@dataclass
class CrossEncoderReranker:
    model_name: str
    device: str = "cuda"
    batch_size: int = 32

    def __post_init__(self) -> None:
        try:
            from sentence_transformers import CrossEncoder  # type: ignore
        except ImportError as exc:
            raise RuntimeError("Install sentence-transformers to use CrossEncoder reranking.") from exc
        self.model = CrossEncoder(self.model_name, device=self.device)

    def rerank(self, query: str, results: list[SearchResult]) -> list[SearchResult]:
        if not results:
            return results
        pairs = [(query, result.chunk.text) for result in results]
        scores = self.model.predict(pairs, batch_size=self.batch_size, show_progress_bar=False)
        rescored: list[SearchResult] = []
        for result, score in zip(results, scores):
            base = result.rerank_score or result.score
            # Keep heuristic score as a weak prior so doc-type planning is not erased.
            result = SearchResult(
                chunk=result.chunk,
                score=result.score,
                dense_rank=result.dense_rank,
                bm25_rank=result.bm25_rank,
                rerank_score=float(score) + 0.08 * base,
            )
            rescored.append(result)
        return sorted(rescored, key=lambda item: item.rerank_score or 0.0, reverse=True)


def build_env_reranker() -> CrossEncoderReranker | None:
    model_name = os.getenv("COMMERCE_RAG_RERANKER_MODEL", "").strip()
    if not model_name:
        return None
    return CrossEncoderReranker(
        model_name,
        device=os.getenv("COMMERCE_RAG_RERANKER_DEVICE", "cuda"),
        batch_size=int(os.getenv("COMMERCE_RAG_RERANKER_BATCH_SIZE", "32")),
    )
