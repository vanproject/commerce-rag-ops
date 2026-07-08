from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4
from typing import Any

from .models import AgentState
from .serialization import agent_state_to_dict


class TraceStore:
    """JSONL trace store for local observability and interview demos."""

    def __init__(self, path: Path):
        self.path = path

    def append(self, state: AgentState) -> dict:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "trace_id": state.trace_id or str(uuid4()),
            "created_at": datetime.now(timezone.utc).isoformat(),
            **agent_state_to_dict(state),
        }
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record

    def tail(self, limit: int = 20) -> list[dict]:
        if not self.path.exists():
            return []
        rows = [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines() if line.strip()]
        return rows[-limit:]


class TraceSQLiteStore:
    """Queryable SQLite trace store for span traces and retrieval diagnostics."""

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def append(self, state: AgentState) -> dict[str, Any]:
        payload = agent_state_to_dict(state)
        trace_run = payload.get("trace_run") or {}
        trace_id = state.trace_id or trace_run.get("trace_id") or str(uuid4())
        created_at = trace_run.get("created_at") or datetime.now(timezone.utc).isoformat()
        with closing(self._connect()) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO trace_runs (
                  trace_id, created_at, query, normalized_query, intent, risk_level,
                  final_action, answer, citations_json, latency_ms, attempts,
                  config_json, dataset_manifest_json, git_sha
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    trace_id,
                    created_at,
                    payload.get("query"),
                    trace_run.get("normalized_query"),
                    payload.get("intent"),
                    payload.get("risk_level"),
                    payload.get("action"),
                    payload.get("answer"),
                    _json(payload.get("citations", [])),
                    trace_run.get("latency_ms"),
                    payload.get("attempts"),
                    _json(trace_run.get("config", {})),
                    _json(trace_run.get("dataset_manifest", {})),
                    trace_run.get("git_sha"),
                ),
            )
            conn.execute("DELETE FROM trace_spans WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM retrieval_candidates WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM trace_artifacts WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM trace_steps WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM trace_observations WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM trace_evidence WHERE trace_id = ?", (trace_id,))
            conn.execute("DELETE FROM trace_verifications WHERE trace_id = ?", (trace_id,))
            conn.executemany(
                """
                INSERT INTO trace_spans (
                  span_id, trace_id, parent_span_id, name, kind, attempt, start_time,
                  end_time, duration_ms, status, error, inputs_json, outputs_json,
                  metrics_json, tags_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        span.get("span_id"),
                        trace_id,
                        span.get("parent_span_id"),
                        span.get("name"),
                        span.get("kind"),
                        span.get("attempt"),
                        span.get("start_time"),
                        span.get("end_time"),
                        span.get("duration_ms"),
                        span.get("status"),
                        span.get("error"),
                        _json(span.get("inputs", {})),
                        _json(span.get("outputs", {})),
                        _json(span.get("metrics", {})),
                        _json(span.get("tags", {})),
                    )
                    for span in payload.get("trace_spans", [])
                ],
            )
            conn.executemany(
                """
                INSERT INTO retrieval_candidates (
                  trace_id, span_id, attempt, source, doc_id, chunk_id, doc_type,
                  rank_dense, rank_bm25, rank_rrf, rank_final, dense_score,
                  bm25_score, rrf_score, rerank_score, forced, forced_reason,
                  selected, dropped_reason
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        trace_id,
                        row.get("span_id"),
                        row.get("attempt"),
                        row.get("source"),
                        row.get("doc_id"),
                        row.get("chunk_id"),
                        row.get("doc_type"),
                        row.get("rank_dense"),
                        row.get("rank_bm25"),
                        row.get("rank_rrf"),
                        row.get("rank_final"),
                        row.get("dense_score"),
                        row.get("bm25_score"),
                        row.get("rrf_score"),
                        row.get("rerank_score"),
                        1 if row.get("forced") else 0,
                        row.get("forced_reason"),
                        1 if row.get("selected") else 0,
                        row.get("dropped_reason"),
                    )
                    for row in payload.get("retrieval_candidates", [])
                ],
            )
            conn.executemany(
                """
                INSERT INTO trace_artifacts (
                  artifact_id, trace_id, span_id, artifact_type, path,
                  content_hash, preview, metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        artifact.get("artifact_id"),
                        trace_id,
                        artifact.get("span_id"),
                        artifact.get("artifact_type"),
                        artifact.get("path"),
                        artifact.get("content_hash"),
                        artifact.get("preview"),
                        _json(artifact.get("metadata", {})),
                    )
                    for artifact in payload.get("trace_artifacts", [])
                ],
            )
            runtime_state = payload.get("runtime_state") or {}
            conn.executemany(
                """
                INSERT INTO trace_steps (
                  trace_id, step_index, action_type, tool_name, status,
                  observation_id, proposed_by, accepted, rejected_reason,
                  reason_summary, tool_input_json, expected_evidence_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        trace_id,
                        index + 1,
                        step.get("action_type"),
                        step.get("tool_name"),
                        step.get("status"),
                        step.get("observation_id"),
                        step.get("proposed_by"),
                        1 if step.get("accepted", True) else 0,
                        step.get("rejected_reason"),
                        step.get("reason_summary"),
                        _json(step.get("tool_input", {})),
                        _json(step.get("expected_evidence", [])),
                    )
                    for index, step in enumerate(runtime_state.get("steps", []))
                ],
            )
            conn.executemany(
                """
                INSERT INTO trace_observations (
                  trace_id, observation_index, source, kind, status,
                  payload_json, citations_json, structured_entities_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                [
                    (
                        trace_id,
                        index + 1,
                        observation.get("source"),
                        observation.get("kind"),
                        observation.get("status"),
                        _json(observation.get("payload", {})),
                        _json(observation.get("citations", [])),
                        _json(observation.get("structured_entities", [])),
                    )
                    for index, observation in enumerate(runtime_state.get("observations", []))
                ],
            )
            conn.executemany(
                """
                INSERT INTO trace_evidence (
                  trace_id, evidence_group, evidence_index, evidence_type,
                  source, doc_id, chunk_id, fact_type, citation, payload_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                _evidence_rows(trace_id, payload.get("evidence_pack") or {}),
            )
            verification = payload.get("verification") or {}
            if verification:
                conn.execute(
                    """
                    INSERT INTO trace_verifications (
                      trace_id, passed, action, missing_evidence_json,
                      citation_errors_json, tool_fact_errors_json,
                      safety_errors_json, repair_hints_json, payload_json
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        trace_id,
                        1 if verification.get("passed") else 0,
                        verification.get("action"),
                        _json(verification.get("missing_evidence", [])),
                        _json(verification.get("citation_errors", [])),
                        _json(verification.get("tool_fact_errors", [])),
                        _json(verification.get("safety_errors", [])),
                        _json(verification.get("repair_hints", [])),
                        _json(verification),
                    ),
                )
            conn.commit()
        return {"trace_id": trace_id, "created_at": created_at, "db_path": str(self.path)}

    def list_runs(self, *, limit: int = 20, intent: str | None = None, action: str | None = None) -> list[dict[str, Any]]:
        where = []
        params: list[Any] = []
        if intent:
            where.append("intent = ?")
            params.append(intent)
        if action:
            where.append("final_action = ?")
            params.append(action)
        query = """
            SELECT trace_id, created_at, query, intent, risk_level, final_action, attempts, latency_ms
            FROM trace_runs
        """
        if where:
            query += " WHERE " + " AND ".join(where)
        query += " ORDER BY created_at DESC LIMIT ?"
        params.append(limit)
        with closing(self._connect()) as conn:
            return [dict(row) for row in conn.execute(query, params)]

    def get_run(self, trace_id: str) -> dict[str, Any] | None:
        with closing(self._connect()) as conn:
            row = conn.execute("SELECT * FROM trace_runs WHERE trace_id = ?", (trace_id,)).fetchone()
            return dict(row) if row else None

    def spans(self, trace_id: str) -> list[dict[str, Any]]:
        with closing(self._connect()) as conn:
            return [
                _decode_span(dict(row))
                for row in conn.execute(
                    "SELECT * FROM trace_spans WHERE trace_id = ? ORDER BY start_time, rowid",
                    (trace_id,),
                )
            ]

    def candidates(self, trace_id: str, *, attempt: int | None = None) -> list[dict[str, Any]]:
        query = "SELECT * FROM retrieval_candidates WHERE trace_id = ?"
        params: list[Any] = [trace_id]
        if attempt is not None:
            query += " AND attempt = ?"
            params.append(attempt)
        query += " ORDER BY attempt, COALESCE(rank_final, 999999), COALESCE(rank_rrf, 999999), rowid"
        with closing(self._connect()) as conn:
            return [dict(row) for row in conn.execute(query, params)]

    def steps(self, trace_id: str) -> list[dict[str, Any]]:
        with closing(self._connect()) as conn:
            return [
                _decode_step(dict(row))
                for row in conn.execute(
                    "SELECT * FROM trace_steps WHERE trace_id = ? ORDER BY step_index",
                    (trace_id,),
                )
            ]

    def observations(self, trace_id: str) -> list[dict[str, Any]]:
        with closing(self._connect()) as conn:
            return [
                _decode_observation(dict(row))
                for row in conn.execute(
                    "SELECT * FROM trace_observations WHERE trace_id = ? ORDER BY observation_index",
                    (trace_id,),
                )
            ]

    def evidence(self, trace_id: str) -> list[dict[str, Any]]:
        with closing(self._connect()) as conn:
            return [
                _decode_evidence(dict(row))
                for row in conn.execute(
                    "SELECT * FROM trace_evidence WHERE trace_id = ? ORDER BY evidence_group, evidence_index",
                    (trace_id,),
                )
            ]

    def verification(self, trace_id: str) -> dict[str, Any] | None:
        with closing(self._connect()) as conn:
            row = conn.execute("SELECT * FROM trace_verifications WHERE trace_id = ?", (trace_id,)).fetchone()
            return _decode_verification(dict(row)) if row else None

    def tool_trace(self, trace_id: str) -> list[dict[str, Any]]:
        spans = [
            span
            for span in self.spans(trace_id)
            if span.get("name") in {"tool.plan", "tools.execute", "tool_citation.validate"}
        ]
        rows = []
        for span in spans:
            rows.append(
                {
                    "span": span.get("name"),
                    "attempt": span.get("attempt"),
                    "inputs": span.get("inputs", {}),
                    "outputs": span.get("outputs", {}),
                    "metrics": span.get("metrics", {}),
                }
            )
        return rows

    def failures(self, *, intent: str | None = None, limit: int = 50) -> list[dict[str, Any]]:
        where = ["final_action IN ('refuse', 'escalate')"]
        params: list[Any] = []
        if intent:
            where.append("intent = ?")
            params.append(intent)
        query = f"""
            SELECT trace_id, created_at, query, intent, final_action, attempts, latency_ms
            FROM trace_runs
            WHERE {' AND '.join(where)}
            ORDER BY created_at DESC
            LIMIT ?
        """
        params.append(limit)
        with closing(self._connect()) as conn:
            return [dict(row) for row in conn.execute(query, params)]

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with closing(self._connect()) as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS trace_runs (
                  trace_id TEXT PRIMARY KEY,
                  created_at TEXT NOT NULL,
                  query TEXT NOT NULL,
                  normalized_query TEXT,
                  intent TEXT,
                  risk_level TEXT,
                  final_action TEXT,
                  answer TEXT,
                  citations_json TEXT,
                  latency_ms INTEGER,
                  attempts INTEGER,
                  config_json TEXT,
                  dataset_manifest_json TEXT,
                  git_sha TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_spans (
                  span_id TEXT PRIMARY KEY,
                  trace_id TEXT NOT NULL,
                  parent_span_id TEXT,
                  name TEXT NOT NULL,
                  kind TEXT NOT NULL,
                  attempt INTEGER,
                  start_time TEXT,
                  end_time TEXT,
                  duration_ms INTEGER,
                  status TEXT,
                  error TEXT,
                  inputs_json TEXT,
                  outputs_json TEXT,
                  metrics_json TEXT,
                  tags_json TEXT
                );
                CREATE TABLE IF NOT EXISTS retrieval_candidates (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  trace_id TEXT NOT NULL,
                  span_id TEXT NOT NULL,
                  attempt INTEGER,
                  source TEXT,
                  doc_id TEXT,
                  chunk_id TEXT,
                  doc_type TEXT,
                  rank_dense INTEGER,
                  rank_bm25 INTEGER,
                  rank_rrf INTEGER,
                  rank_final INTEGER,
                  dense_score REAL,
                  bm25_score REAL,
                  rrf_score REAL,
                  rerank_score REAL,
                  forced INTEGER,
                  forced_reason TEXT,
                  selected INTEGER,
                  dropped_reason TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_artifacts (
                  artifact_id TEXT PRIMARY KEY,
                  trace_id TEXT NOT NULL,
                  span_id TEXT,
                  artifact_type TEXT,
                  path TEXT,
                  content_hash TEXT,
                  preview TEXT,
                  metadata_json TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_steps (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  trace_id TEXT NOT NULL,
                  step_index INTEGER NOT NULL,
                  action_type TEXT,
                  tool_name TEXT,
                  status TEXT,
                  observation_id TEXT,
                  proposed_by TEXT,
                  accepted INTEGER,
                  rejected_reason TEXT,
                  reason_summary TEXT,
                  tool_input_json TEXT,
                  expected_evidence_json TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_observations (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  trace_id TEXT NOT NULL,
                  observation_index INTEGER NOT NULL,
                  source TEXT,
                  kind TEXT,
                  status TEXT,
                  payload_json TEXT,
                  citations_json TEXT,
                  structured_entities_json TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_evidence (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  trace_id TEXT NOT NULL,
                  evidence_group TEXT NOT NULL,
                  evidence_index INTEGER NOT NULL,
                  evidence_type TEXT,
                  source TEXT,
                  doc_id TEXT,
                  chunk_id TEXT,
                  fact_type TEXT,
                  citation TEXT,
                  payload_json TEXT
                );
                CREATE TABLE IF NOT EXISTS trace_verifications (
                  trace_id TEXT PRIMARY KEY,
                  passed INTEGER,
                  action TEXT,
                  missing_evidence_json TEXT,
                  citation_errors_json TEXT,
                  tool_fact_errors_json TEXT,
                  safety_errors_json TEXT,
                  repair_hints_json TEXT,
                  payload_json TEXT
                );
                CREATE INDEX IF NOT EXISTS idx_trace_runs_created_at ON trace_runs(created_at);
                CREATE INDEX IF NOT EXISTS idx_trace_runs_intent ON trace_runs(intent);
                CREATE INDEX IF NOT EXISTS idx_trace_runs_action ON trace_runs(final_action);
                CREATE INDEX IF NOT EXISTS idx_trace_spans_trace_id ON trace_spans(trace_id);
                CREATE INDEX IF NOT EXISTS idx_candidates_trace_attempt ON retrieval_candidates(trace_id, attempt);
                CREATE INDEX IF NOT EXISTS idx_trace_steps_trace_id ON trace_steps(trace_id);
                CREATE INDEX IF NOT EXISTS idx_trace_observations_trace_id ON trace_observations(trace_id);
                CREATE INDEX IF NOT EXISTS idx_trace_evidence_trace_id ON trace_evidence(trace_id);
                """
            )
            conn.commit()


def _json(payload: Any) -> str:
    return json.dumps(payload, ensure_ascii=False, default=str)


def _decode_span(row: dict[str, Any]) -> dict[str, Any]:
    for key in ["inputs_json", "outputs_json", "metrics_json", "tags_json"]:
        row[key.replace("_json", "")] = json.loads(row.pop(key) or "{}")
    return row


def _decode_step(row: dict[str, Any]) -> dict[str, Any]:
    row["accepted"] = bool(row.get("accepted"))
    row["tool_input"] = json.loads(row.pop("tool_input_json") or "{}")
    row["expected_evidence"] = json.loads(row.pop("expected_evidence_json") or "[]")
    return row


def _decode_observation(row: dict[str, Any]) -> dict[str, Any]:
    row["payload"] = json.loads(row.pop("payload_json") or "{}")
    row["citations"] = json.loads(row.pop("citations_json") or "[]")
    row["structured_entities"] = json.loads(row.pop("structured_entities_json") or "[]")
    return row


def _decode_evidence(row: dict[str, Any]) -> dict[str, Any]:
    row["payload"] = json.loads(row.pop("payload_json") or "{}")
    return row


def _decode_verification(row: dict[str, Any]) -> dict[str, Any]:
    row["passed"] = bool(row.get("passed"))
    row["missing_evidence"] = json.loads(row.pop("missing_evidence_json") or "[]")
    row["citation_errors"] = json.loads(row.pop("citation_errors_json") or "[]")
    row["tool_fact_errors"] = json.loads(row.pop("tool_fact_errors_json") or "[]")
    row["safety_errors"] = json.loads(row.pop("safety_errors_json") or "[]")
    row["repair_hints"] = json.loads(row.pop("repair_hints_json") or "[]")
    row["payload"] = json.loads(row.pop("payload_json") or "{}")
    return row


def _evidence_rows(trace_id: str, evidence_pack: dict[str, Any]) -> list[tuple[Any, ...]]:
    rows: list[tuple[Any, ...]] = []
    for index, fact in enumerate(evidence_pack.get("structured_facts", []), start=1):
        rows.append(
            (
                trace_id,
                "structured_facts",
                index,
                "structured_fact",
                fact.get("source_tool"),
                None,
                None,
                fact.get("fact_type"),
                fact.get("citation"),
                _json(fact),
            )
        )
    for group in ["policy_evidence", "product_evidence", "review_evidence", "ticket_evidence"]:
        for index, item in enumerate(evidence_pack.get(group, []), start=1):
            rows.append(
                (
                    trace_id,
                    group,
                    index,
                    item.get("evidence_type"),
                    item.get("source"),
                    item.get("doc_id"),
                    item.get("chunk_id"),
                    None,
                    item.get("citation"),
                    _json(item),
                )
            )
    for index, conflict in enumerate(evidence_pack.get("unresolved_conflicts", []), start=1):
        rows.append(
            (
                trace_id,
                "unresolved_conflicts",
                index,
                conflict.get("conflict_type"),
                None,
                None,
                None,
                None,
                None,
                _json(conflict),
            )
        )
    for index, requirement in enumerate(evidence_pack.get("missing_requirements", []), start=1):
        rows.append(
            (
                trace_id,
                "missing_requirements",
                index,
                "missing_requirement",
                None,
                None,
                None,
                None,
                None,
                _json({"requirement": requirement}),
            )
        )
    return rows
