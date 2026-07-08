from __future__ import annotations

import hashlib
import json
import re
import subprocess
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
from typing import Any

from .text import normalize_text


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class TraceRun:
    trace_id: str
    created_at: str
    query: str
    normalized_query: str
    intent: str | None = None
    risk_level: str | None = None
    semantic_memory_source_defaults: list[str] = field(default_factory=list)
    # Deprecated compatibility mirror for older reports/CLI consumers.
    retrieval_plan: list[str] = field(default_factory=list)
    final_action: str | None = None
    answer: str | None = None
    citations: list[str] = field(default_factory=list)
    latency_ms: int | None = None
    attempts: int = 0
    config: dict[str, Any] = field(default_factory=dict)
    dataset_manifest: dict[str, Any] = field(default_factory=dict)
    git_sha: str | None = None


@dataclass
class TraceSpan:
    trace_id: str
    span_id: str
    parent_span_id: str | None
    name: str
    kind: str
    start_time: str
    end_time: str | None = None
    duration_ms: int | None = None
    attempt: int | None = None
    status: str = "ok"
    error: str | None = None
    inputs: dict[str, Any] = field(default_factory=dict)
    outputs: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, Any] = field(default_factory=dict)
    tags: dict[str, str] = field(default_factory=dict)


@dataclass
class TraceArtifact:
    trace_id: str
    artifact_id: str
    span_id: str
    artifact_type: str
    path: str | None
    content_hash: str
    preview: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


class TraceRecorder:
    def __init__(
        self,
        query: str,
        *,
        config: dict[str, Any] | None = None,
        dataset_manifest: dict[str, Any] | None = None,
        git_sha: str | None = None,
    ):
        self.run = TraceRun(
            trace_id=str(uuid4()),
            created_at=utc_now(),
            query=query,
            normalized_query=normalize_text(query),
            config=config or {},
            dataset_manifest=dataset_manifest or {},
            git_sha=git_sha,
        )
        self.spans: list[TraceSpan] = []
        self.artifacts: list[TraceArtifact] = []
        self.retrieval_candidates: list[dict[str, Any]] = []
        self._span_starts: dict[str, float] = {}
        self.root_span_id = self.start_span(
            "agent.run",
            kind="agent",
            parent_id=None,
            inputs={"query": query},
        )

    @property
    def trace_id(self) -> str:
        return self.run.trace_id

    def start_span(
        self,
        name: str,
        *,
        kind: str,
        parent_id: str | None = None,
        attempt: int | None = None,
        inputs: dict[str, Any] | None = None,
        tags: dict[str, str] | None = None,
    ) -> str:
        span_id = str(uuid4())
        self._span_starts[span_id] = time.perf_counter()
        self.spans.append(
            TraceSpan(
                trace_id=self.trace_id,
                span_id=span_id,
                parent_span_id=parent_id,
                name=name,
                kind=kind,
                start_time=utc_now(),
                attempt=attempt,
                inputs=redact_trace_payload(inputs or {}),
                tags={key: str(value) for key, value in (tags or {}).items()},
            )
        )
        return span_id

    def end_span(
        self,
        span_id: str,
        *,
        outputs: dict[str, Any] | None = None,
        metrics: dict[str, Any] | None = None,
        error: Exception | str | None = None,
    ) -> None:
        span = self._span(span_id)
        span.end_time = utc_now()
        start = self._span_starts.get(span_id)
        if start is not None:
            span.duration_ms = int((time.perf_counter() - start) * 1000)
        span.outputs = redact_trace_payload(outputs or {})
        span.metrics = redact_trace_payload(metrics or {})
        if error is not None:
            span.status = "error"
            span.error = str(error)

    def add_artifact(
        self,
        span_id: str,
        artifact_type: str,
        content: Any,
        *,
        path: Path | None = None,
        preview_chars: int = 240,
        metadata: dict[str, Any] | None = None,
    ) -> str:
        encoded = json.dumps(redact_trace_payload(content), ensure_ascii=False, sort_keys=True, default=str)
        artifact_id = str(uuid4())
        self.artifacts.append(
            TraceArtifact(
                trace_id=self.trace_id,
                artifact_id=artifact_id,
                span_id=span_id,
                artifact_type=artifact_type,
                path=str(path) if path else None,
                content_hash="sha256:" + hashlib.sha256(encoded.encode("utf-8")).hexdigest(),
                preview=encoded[:preview_chars],
                metadata=metadata or {},
            )
        )
        return artifact_id

    def add_retrieval_candidates(
        self,
        span_id: str,
        attempt: int,
        candidates: list[dict[str, Any]],
    ) -> None:
        for row in candidates:
            payload = dict(row)
            payload.setdefault("trace_id", self.trace_id)
            payload.setdefault("span_id", span_id)
            payload.setdefault("attempt", attempt)
            self.retrieval_candidates.append(redact_trace_payload(payload))

    def finalize(
        self,
        *,
        intent: str,
        risk_level: str,
        retrieval_plan: list[str],
        semantic_memory_source_defaults: list[str] | None = None,
        final_action: str,
        answer: str,
        citations: list[str],
        latency_ms: int,
        attempts: int,
    ) -> None:
        self.run.intent = intent
        self.run.risk_level = risk_level
        self.run.semantic_memory_source_defaults = list(semantic_memory_source_defaults or retrieval_plan)
        self.run.retrieval_plan = retrieval_plan
        self.run.final_action = final_action
        self.run.answer = answer
        self.run.citations = citations
        self.run.latency_ms = latency_ms
        self.run.attempts = attempts
        self.end_span(
            self.root_span_id,
            outputs={
                "intent": intent,
                "risk_level": risk_level,
                "final_action": final_action,
                "citation_count": len(citations),
            },
            metrics={"latency_ms": latency_ms, "attempts": attempts},
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "run": asdict(self.run),
            "spans": [asdict(span) for span in self.spans],
            "artifacts": [asdict(artifact) for artifact in self.artifacts],
            "retrieval_candidates": self.retrieval_candidates,
        }

    def _span(self, span_id: str) -> TraceSpan:
        for span in self.spans:
            if span.span_id == span_id:
                return span
        raise KeyError(f"Unknown trace span: {span_id}")


def redact_trace_payload(payload: Any) -> Any:
    if isinstance(payload, dict):
        return {key: redact_trace_payload(value) for key, value in payload.items()}
    if isinstance(payload, list):
        return [redact_trace_payload(value) for value in payload]
    if not isinstance(payload, str):
        return payload
    value = re.sub(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", "[REDACTED_EMAIL]", payload)
    value = re.sub(r"\b(?:\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b", "[REDACTED_PHONE]", value)
    value = re.sub(r"\b(?:\d[ -]*?){13,16}\b", "[REDACTED_PAYMENT]", value)
    value = re.sub(r"\bORD-([A-Z0-9-]*?)([A-Z0-9]{4})\b", r"ORD-***\2", value, flags=re.IGNORECASE)
    value = re.sub(r"\bsk-[A-Za-z0-9_-]{12,}\b", "[REDACTED_API_KEY]", value)
    return value


def current_git_sha(repo_root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None
