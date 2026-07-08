from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .text import hashed_embedding


class EmbeddingModel(Protocol):
    name: str
    dimensions: int

    def encode_documents(self, texts: list[str]) -> list[list[float]]:
        """Embed passage/document texts."""

    def encode_query(self, text: str) -> list[float]:
        """Embed a search query."""


@dataclass
class HashEmbeddingModel:
    dimensions: int = 384
    name: str = "hash"

    def encode_documents(self, texts: list[str]) -> list[list[float]]:
        return [hashed_embedding(text, dimensions=self.dimensions) for text in texts]

    def encode_query(self, text: str) -> list[float]:
        return hashed_embedding(text, dimensions=self.dimensions)


class SentenceTransformerEmbeddingModel:
    def __init__(
        self,
        model_name: str = "BAAI/bge-large-en-v1.5",
        *,
        device: str = "cuda",
        batch_size: int = 64,
        query_instruction: str | None = None,
    ):
        try:
            from sentence_transformers import SentenceTransformer  # type: ignore
        except ImportError as exc:
            raise RuntimeError("Install sentence-transformers to use local neural embeddings.") from exc
        self.name = model_name
        self.batch_size = batch_size
        self.query_instruction = query_instruction or _default_query_instruction(model_name)
        self.model = SentenceTransformer(model_name, device=device)
        dimension = getattr(self.model, "get_sentence_embedding_dimension", lambda: None)()
        if not dimension:
            dimension = len(self.encode_query("dimension probe"))
        self.dimensions = int(dimension)

    def encode_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = self.model.encode(
            texts,
            batch_size=self.batch_size,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return [vector.astype(float).tolist() for vector in vectors]

    def encode_query(self, text: str) -> list[float]:
        query = f"{self.query_instruction}{text}" if self.query_instruction else text
        vector = self.model.encode(
            query,
            normalize_embeddings=True,
            show_progress_bar=False,
        )
        return vector.astype(float).tolist()


def build_embedding_model(
    backend: str = "hash",
    *,
    model_name: str = "BAAI/bge-large-en-v1.5",
    device: str = "cuda",
    batch_size: int = 64,
) -> EmbeddingModel:
    if backend == "hash":
        return HashEmbeddingModel()
    if backend in {"sentence-transformers", "sentence_transformers", "local"}:
        return SentenceTransformerEmbeddingModel(model_name, device=device, batch_size=batch_size)
    raise ValueError(f"Unknown embedding backend: {backend}")


def _default_query_instruction(model_name: str) -> str:
    lowered = model_name.lower()
    if "bge" in lowered:
        return "Represent this sentence for searching relevant passages: "
    return ""
