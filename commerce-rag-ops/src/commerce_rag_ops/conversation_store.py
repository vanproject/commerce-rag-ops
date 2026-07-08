from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any
from uuid import uuid4

from .models import AgentState
from .trace import redact_trace_payload, utc_now


class ConversationStore:
    """Conversation-scoped memory store.

    This store intentionally keeps only recent turns and safe business
    entities. Full AgentState/trace payloads stay in TraceStore.
    """

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._init_schema()

    def ensure_conversation(self, conversation_id: str | None = None, user_id: str | None = None) -> str:
        now = utc_now()
        conversation_id = conversation_id or str(uuid4())
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT conversation_id FROM conversations WHERE conversation_id = ?",
                (conversation_id,),
            ).fetchone()
            if row:
                conn.execute(
                    "UPDATE conversations SET updated_at = ?, user_id = COALESCE(user_id, ?) WHERE conversation_id = ?",
                    (now, user_id, conversation_id),
                )
            else:
                conn.execute(
                    """
                    INSERT INTO conversations (conversation_id, user_id, created_at, updated_at, status)
                    VALUES (?, ?, ?, ?, 'active')
                    """,
                    (conversation_id, user_id, now, now),
                )
            conn.commit()
        return conversation_id

    def load_context(self, conversation_id: str | None, user_id: str | None = None, *, limit: int = 6) -> dict[str, Any]:
        conversation_id = self.ensure_conversation(conversation_id, user_id)
        recent_turns = self.recent_turns(conversation_id, limit=limit)
        entities = self.active_entities(conversation_id)
        return {
            "conversation_id": conversation_id,
            "user_id": user_id,
            "recent_turns": recent_turns,
            "active_entities": entities["active_entities"],
            "entity_candidates": entities["entity_candidates"],
            "ambiguous_entity_types": entities["ambiguous_entity_types"],
        }

    def recent_turns(self, conversation_id: str, *, limit: int = 6) -> list[dict[str, Any]]:
        with closing(self._connect()) as conn:
            rows = conn.execute(
                """
                SELECT turn_id, role, content, resolved_query, intent, risk_level, action,
                       citations_json, tool_results_json, created_at
                FROM conversation_turns
                WHERE conversation_id = ?
                ORDER BY created_at DESC, rowid DESC
                LIMIT ?
                """,
                (conversation_id, limit),
            ).fetchall()
        turns = [_decode_turn(dict(row)) for row in rows]
        return list(reversed(turns))

    def active_entities(self, conversation_id: str) -> dict[str, Any]:
        with closing(self._connect()) as conn:
            rows = [
                dict(row)
                for row in conn.execute(
                    """
                    SELECT entity_type, entity_value, normalized_value, source, confidence,
                           first_seen_turn_id, last_seen_turn_id, metadata_json
                    FROM conversation_entities
                    WHERE conversation_id = ? AND (expires_at IS NULL OR expires_at > ?)
                    ORDER BY entity_type, confidence DESC, rowid DESC
                    """,
                    (conversation_id, utc_now()),
                )
            ]
        candidates: dict[str, list[dict[str, Any]]] = {}
        for row in rows:
            row["metadata"] = json.loads(row.pop("metadata_json") or "{}")
            candidates.setdefault(row["entity_type"], []).append(row)
        active: dict[str, Any] = {}
        ambiguous: list[str] = []
        for entity_type, values in candidates.items():
            normalized_values = {item["normalized_value"] for item in values}
            if entity_type in {"sku", "order_id", "product_id"} and len(normalized_values) > 1:
                ambiguous.append(entity_type)
                continue
            active[entity_type] = values[0]["entity_value"]
        return {
            "active_entities": active,
            "entity_candidates": candidates,
            "ambiguous_entity_types": ambiguous,
        }

    def append_exchange(
        self,
        *,
        conversation_id: str,
        user_id: str | None,
        original_query: str,
        resolved_query: str,
        state: AgentState,
    ) -> dict[str, str]:
        conversation_id = self.ensure_conversation(conversation_id, user_id)
        user_turn_id = str(uuid4())
        assistant_turn_id = str(uuid4())
        now = utc_now()
        with closing(self._connect()) as conn:
            conn.execute(
                """
                INSERT INTO conversation_turns (
                  turn_id, conversation_id, role, content, resolved_query, intent,
                  risk_level, action, citations_json, tool_results_json, created_at
                ) VALUES (?, ?, 'user', ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_turn_id,
                    conversation_id,
                    redact_trace_payload(original_query),
                    redact_trace_payload(resolved_query),
                    state.intent,
                    state.risk_level,
                    state.action,
                    json.dumps(state.citations, ensure_ascii=False),
                    json.dumps(_safe_tool_results(state.tool_results), ensure_ascii=False),
                    now,
                ),
            )
            conn.execute(
                """
                INSERT INTO conversation_turns (
                  turn_id, conversation_id, role, content, resolved_query, intent,
                  risk_level, action, citations_json, tool_results_json, created_at
                ) VALUES (?, ?, 'assistant', ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    assistant_turn_id,
                    conversation_id,
                    redact_trace_payload(state.answer),
                    redact_trace_payload(resolved_query),
                    state.intent,
                    state.risk_level,
                    state.action,
                    json.dumps(state.citations, ensure_ascii=False),
                    json.dumps(_safe_tool_results(state.tool_results), ensure_ascii=False),
                    now,
                ),
            )
            conn.execute("UPDATE conversations SET updated_at = ? WHERE conversation_id = ?", (now, conversation_id))
            conn.commit()
        return {"user_turn_id": user_turn_id, "assistant_turn_id": assistant_turn_id}

    def upsert_entities(self, conversation_id: str, entities: list[dict[str, Any]], *, turn_id: str) -> None:
        if not entities:
            return
        with closing(self._connect()) as conn:
            for entity in entities:
                entity_type = str(entity["entity_type"])
                normalized_value = str(entity["normalized_value"])
                entity_value = str(entity["entity_value"])
                row = conn.execute(
                    """
                    SELECT entity_id, first_seen_turn_id FROM conversation_entities
                    WHERE conversation_id = ? AND entity_type = ? AND normalized_value = ?
                    """,
                    (conversation_id, entity_type, normalized_value),
                ).fetchone()
                metadata_json = json.dumps(entity.get("metadata", {}), ensure_ascii=False)
                if row:
                    conn.execute(
                        """
                        UPDATE conversation_entities
                        SET entity_value = ?, source = ?, confidence = ?, last_seen_turn_id = ?,
                            expires_at = ?, metadata_json = ?
                        WHERE entity_id = ?
                        """,
                        (
                            entity_value,
                            entity.get("source", "unknown"),
                            float(entity.get("confidence", 0.5)),
                            turn_id,
                            entity.get("expires_at"),
                            metadata_json,
                            row["entity_id"],
                        ),
                    )
                else:
                    conn.execute(
                        """
                        INSERT INTO conversation_entities (
                          entity_id, conversation_id, entity_type, entity_value,
                          normalized_value, source, confidence, first_seen_turn_id,
                          last_seen_turn_id, expires_at, metadata_json
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            str(uuid4()),
                            conversation_id,
                            entity_type,
                            entity_value,
                            normalized_value,
                            entity.get("source", "unknown"),
                            float(entity.get("confidence", 0.5)),
                            turn_id,
                            turn_id,
                            entity.get("expires_at"),
                            metadata_json,
                        ),
                    )
            conn.commit()

    def clear_entities(self, conversation_id: str, entity_types: list[str]) -> None:
        if not entity_types:
            return
        placeholders = ",".join("?" for _ in entity_types)
        with closing(self._connect()) as conn:
            conn.execute(
                f"DELETE FROM conversation_entities WHERE conversation_id = ? AND entity_type IN ({placeholders})",
                [conversation_id, *entity_types],
            )
            conn.commit()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_schema(self) -> None:
        with closing(self._connect()) as conn:
            conn.executescript(
                """
                CREATE TABLE IF NOT EXISTS conversations (
                    conversation_id TEXT PRIMARY KEY,
                    user_id TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'active'
                );
                CREATE TABLE IF NOT EXISTS conversation_turns (
                    turn_id TEXT PRIMARY KEY,
                    conversation_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    resolved_query TEXT,
                    intent TEXT,
                    risk_level TEXT,
                    action TEXT,
                    citations_json TEXT NOT NULL DEFAULT '[]',
                    tool_results_json TEXT NOT NULL DEFAULT '{}',
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(conversation_id) REFERENCES conversations(conversation_id)
                );
                CREATE TABLE IF NOT EXISTS conversation_entities (
                    entity_id TEXT PRIMARY KEY,
                    conversation_id TEXT NOT NULL,
                    entity_type TEXT NOT NULL,
                    entity_value TEXT NOT NULL,
                    normalized_value TEXT NOT NULL,
                    source TEXT NOT NULL,
                    confidence REAL NOT NULL,
                    first_seen_turn_id TEXT NOT NULL,
                    last_seen_turn_id TEXT NOT NULL,
                    expires_at TEXT,
                    metadata_json TEXT NOT NULL DEFAULT '{}',
                    FOREIGN KEY(conversation_id) REFERENCES conversations(conversation_id)
                );
                CREATE INDEX IF NOT EXISTS idx_conversation_turns_conv_created
                  ON conversation_turns(conversation_id, created_at);
                CREATE INDEX IF NOT EXISTS idx_conversation_entities_active
                  ON conversation_entities(conversation_id, entity_type, normalized_value);
                """
            )
            conn.commit()


def _decode_turn(row: dict[str, Any]) -> dict[str, Any]:
    row["citations"] = json.loads(row.pop("citations_json") or "[]")
    row["tool_results"] = json.loads(row.pop("tool_results_json") or "{}")
    return row


def _safe_tool_results(tool_results: dict[str, Any]) -> dict[str, Any]:
    return {
        "backend": tool_results.get("backend"),
        "products": tool_results.get("products", []),
        "orders": [
            {
                "order_id": order.get("order_id"),
                "sku": order.get("sku"),
                "status": order.get("status"),
                "delivery_status": order.get("delivery_status"),
                "product_id": order.get("product_id"),
            }
            for order in tool_results.get("orders", [])
        ],
        "mentioned_order_ids": tool_results.get("mentioned_order_ids", []),
        "missing_order_ids": tool_results.get("missing_order_ids", []),
        "mentioned_skus": tool_results.get("mentioned_skus", []),
        "missing_skus": tool_results.get("missing_skus", []),
    }
