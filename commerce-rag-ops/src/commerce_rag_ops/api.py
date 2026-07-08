from __future__ import annotations

import argparse
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any

from .agent import CommerceRAGAgent
from .advisor import build_advisor
from .conversation_store import ConversationStore
from .etl import load_processed_chunks
from .entity_memory import EntityResolver, context_resolution_to_legacy_payload, entity_types_to_clear, extract_entities_from_state
from .evaluation import run_evaluation
from .generator import build_generator
from .retrieval import HybridRetriever
from .serialization import agent_state_to_dict
from .trace_store import TraceStore


def project_root() -> Path:
    return Path(__file__).resolve().parents[2]


def build_agent(data_dir: Path, *, generator_name: str = "template", advisor_name: str = "rule") -> CommerceRAGAgent:
    return CommerceRAGAgent(
        HybridRetriever(load_processed_chunks(data_dir)),
        data_dir,
        generator=build_generator(generator_name),
        advisor=build_advisor(advisor_name),
    )


class CommerceRAGRequestHandler(BaseHTTPRequestHandler):
    agent: CommerceRAGAgent
    data_dir: Path
    trace_store: TraceStore
    conversation_store: ConversationStore
    entity_resolver: EntityResolver

    def do_GET(self) -> None:
        if self.path in ("/", "/index.html"):
            self._html((project_root() / "web" / "index.html").read_text(encoding="utf-8"))
            return
        if self.path == "/health":
            self._json({"status": "ok", "service": "commerce-rag-ops"})
            return
        if self.path == "/metrics":
            report = run_evaluation(self.agent, self.agent.retriever, self.data_dir)
            self._json({"retrieval": report["retrieval"], "support_quality": report["support_quality"], "latency": report["latency"]})
            return
        if self.path.startswith("/traces"):
            self._json({"traces": self.trace_store.tail(20)})
            return
        self._json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:
        if self.path != "/ask":
            self._json({"error": "not found"}, status=HTTPStatus.NOT_FOUND)
            return
        try:
            payload = self._read_json()
            query = str(payload.get("query") or "").strip()
            if not query:
                self._json({"error": "query is required"}, status=HTTPStatus.BAD_REQUEST)
                return
            max_retries = int(payload.get("max_retries", 1))
            user_id = str(payload.get("user_id") or "").strip() or None
            memory_context = self.conversation_store.load_context(
                str(payload.get("conversation_id") or "").strip() or None,
                user_id,
            )
            context_resolution = self.entity_resolver.resolve_context(query, memory_context)
            resolution = context_resolution_to_legacy_payload(query, context_resolution)
            agent_query = query
            memory_context["original_query"] = query
            memory_context["resolved_query"] = agent_query
            memory_context["entity_resolution"] = resolution
            memory_context["context_resolution"] = context_resolution.to_dict()
            memory_context["resolved_entities"] = resolution.get("used_entities", [])
            state = self.agent.run(agent_query, max_retries=max_retries, memory_context=memory_context)
            turn_ids = self.conversation_store.append_exchange(
                conversation_id=memory_context["conversation_id"],
                user_id=user_id,
                original_query=query,
                resolved_query=agent_query,
                state=state,
            )
            extracted_entities = extract_entities_from_state(state)
            clear_types = entity_types_to_clear(resolution)
            self.conversation_store.clear_entities(memory_context["conversation_id"], clear_types)
            self.conversation_store.upsert_entities(
                memory_context["conversation_id"],
                extracted_entities,
                turn_id=turn_ids["user_turn_id"],
            )
            state.trace.append(
                {
                    "event": "entity_update",
                    "conversation_id": memory_context["conversation_id"],
                    "cleared_entity_types": clear_types,
                    "entity_count": len(extracted_entities),
                    "entities": extracted_entities,
                }
            )
            stored = self.trace_store.append(state)
            response = agent_state_to_dict(state)
            response["trace_id"] = stored["trace_id"]
            response["conversation_id"] = memory_context["conversation_id"]
            response["resolved_query"] = agent_query
            response["context_resolution"] = context_resolution.to_dict()
            response["memory_used"] = {
                "recent_turns": len(memory_context.get("recent_turns", [])),
                "entities": resolution.get("used_entities", []),
                "blocked_reasons": resolution.get("blocked_reasons", []),
            }
            self._json(response)
        except Exception as exc:  # Keep the demo server debuggable.
            self._json({"error": str(exc)}, status=HTTPStatus.INTERNAL_SERVER_ERROR)

    def log_message(self, format: str, *args: Any) -> None:
        return

    def _read_json(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode("utf-8") if length else "{}"
        return json.loads(body or "{}")

    def _json(self, payload: dict[str, Any], *, status: HTTPStatus = HTTPStatus.OK) -> None:
        encoded = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status.value)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def _html(self, html: str, *, status: HTTPStatus = HTTPStatus.OK) -> None:
        encoded = html.encode("utf-8")
        self.send_response(status.value)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)


def serve(
    host: str,
    port: int,
    data_dir: Path,
    trace_store_path: Path,
    conversation_store_path: Path,
    generator_name: str,
    advisor_name: str,
) -> None:
    handler = CommerceRAGRequestHandler
    handler.agent = build_agent(data_dir, generator_name=generator_name, advisor_name=advisor_name)
    handler.data_dir = data_dir
    handler.trace_store = TraceStore(trace_store_path)
    handler.conversation_store = ConversationStore(conversation_store_path)
    handler.entity_resolver = EntityResolver()
    server = ThreadingHTTPServer((host, port), handler)
    print(f"CommerceRAG Ops API listening on http://{host}:{port}")
    print("Endpoints: GET /, GET /health, GET /metrics, POST /ask, GET /traces")
    server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser(description="CommerceRAG Ops HTTP API")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--data-dir", type=Path, default=project_root() / "data")
    parser.add_argument("--trace-store", type=Path, default=project_root() / "reports" / "api_traces.jsonl")
    parser.add_argument("--conversation-store", type=Path, default=project_root() / "reports" / "conversations.db")
    parser.add_argument("--generator", choices=["template", "openai-compatible", "llm"], default="template")
    parser.add_argument("--advisor", choices=["rule", "auto", "openai-compatible", "llm"], default="auto")
    args = parser.parse_args()
    serve(args.host, args.port, args.data_dir, args.trace_store, args.conversation_store, args.generator, args.advisor)


if __name__ == "__main__":
    main()
