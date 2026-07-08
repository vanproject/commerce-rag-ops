from __future__ import annotations

import hashlib
import re

from .models import DocumentChunk
from .text import normalize_text


SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


def stable_chunk_id(source: str, doc_id: str, index: int, text: str) -> str:
    digest = hashlib.sha256(f"{source}:{doc_id}:{index}:{text}".encode("utf-8")).hexdigest()
    return digest[:16]


def sentence_aware_chunks(
    text: str,
    *,
    source: str,
    doc_id: str,
    chunk_size: int,
    chunk_overlap: int,
    metadata: dict | None = None,
) -> list[DocumentChunk]:
    clean = normalize_text(text)
    if not clean:
        return []

    sentences = [s.strip() for s in SENTENCE_SPLIT_RE.split(clean) if s.strip()]
    chunks: list[str] = []
    current = ""

    for sentence in sentences:
        candidate = f"{current} {sentence}".strip()
        if len(candidate) <= chunk_size or not current:
            current = candidate
            continue
        chunks.append(current)
        overlap = current[-chunk_overlap:] if chunk_overlap > 0 else ""
        current = f"{overlap} {sentence}".strip()

    if current:
        chunks.append(current)

    output: list[DocumentChunk] = []
    for index, chunk_text in enumerate(chunks):
        chunk_id = stable_chunk_id(source, doc_id, index, chunk_text)
        output.append(
            DocumentChunk(
                chunk_id=chunk_id,
                source=source,
                doc_id=doc_id,
                text=chunk_text,
                metadata={**(metadata or {}), "chunk_index": index, "total_chunks": len(chunks)},
            )
        )
    return output

