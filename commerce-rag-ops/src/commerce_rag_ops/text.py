from __future__ import annotations

import math
import re
import hashlib
from collections import Counter
from typing import Iterable


TOKEN_RE = re.compile(r"[a-z0-9]+")

SYNONYMS: dict[str, set[str]] = {
    "refund": {"return", "money", "reimbursement"},
    "return": {"refund", "send", "exchange"},
    "broken": {"damaged", "defective", "not", "working"},
    "delivery": {"shipping", "shipment", "late"},
    "warranty": {"guarantee", "repair"},
    "recommend": {"suggest", "best", "looking"},
    "cheap": {"budget", "affordable", "low", "price"},
    "baby": {"infant", "toddler", "child"},
    "beauty": {"skin", "makeup", "cosmetic"},
    "software": {"app", "license", "subscription"},
}


def normalize_text(text: str) -> str:
    text = text.replace("\n", " ").replace("\t", " ").strip().lower()
    return re.sub(r"\s+", " ", text)


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(normalize_text(text))


def expand_query(query: str) -> list[str]:
    tokens = tokenize(query)
    expanded = set(tokens)
    for token in tokens:
        expanded.update(SYNONYMS.get(token, set()))
    if not expanded:
        return [query]
    return [query, " ".join(sorted(expanded))]


def cosine_similarity(left: Counter[str], right: Counter[str]) -> float:
    if not left or not right:
        return 0.0
    shared = set(left) & set(right)
    dot = sum(left[t] * right[t] for t in shared)
    left_norm = math.sqrt(sum(v * v for v in left.values()))
    right_norm = math.sqrt(sum(v * v for v in right.values()))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return dot / (left_norm * right_norm)


def keyword_coverage(text: str, expected_keywords: Iterable[str]) -> float:
    expected = [k.lower() for k in expected_keywords if k]
    if not expected:
        return 1.0
    actual = normalize_text(text)
    matched = sum(1 for keyword in expected if keyword in actual)
    return matched / len(expected)


def hashed_embedding(text: str, *, dimensions: int = 384) -> list[float]:
    """Deterministic local embedding for Qdrant demos without model downloads."""
    vector = [0.0] * dimensions
    for token in tokenize(text):
        index = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16) % dimensions
        vector[index] += 1.0
    norm = math.sqrt(sum(value * value for value in vector))
    if norm == 0:
        return vector
    return [value / norm for value in vector]
