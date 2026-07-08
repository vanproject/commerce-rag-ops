from __future__ import annotations

from typing import Any

from ..models import AgentState
from .evidence_types import DocEvidence, EvidenceConflict, EvidencePack, StructuredFact


class EvidencePackBuilder:
    def build_from_agent_state(self, state: AgentState, *, missing_requirements: list[str] | None = None) -> EvidencePack:
        pack = EvidencePack(missing_requirements=list(missing_requirements or []))
        for call in state.tool_results.get("tool_calls", []):
            if call.get("policy_decision") != "allowed" or not call.get("found"):
                continue
            citation = str(call.get("evidence_id") or f"[tool:{call.get('tool_name')}]")
            tool_name = str(call.get("tool_name"))
            output = call.get("output", {})
            if tool_name == "sql.order_by_id":
                pack.structured_facts.extend(
                    [
                        StructuredFact("order_fact", _compact_order_output(output), tool_name, citation),
                        StructuredFact("order_status", output.get("status"), tool_name, citation),
                        StructuredFact("delivery_status", output.get("delivery_status"), tool_name, citation),
                        StructuredFact("order_total", output.get("total"), tool_name, citation),
                    ]
                )
            elif tool_name == "sql.order_items_by_order_id":
                pack.structured_facts.append(StructuredFact("order_items", output.get("items", []), tool_name, citation))
            elif tool_name in {"sql.product_by_sku", "sql.product_by_id", "sql.product_search"}:
                pack.structured_facts.append(StructuredFact("product_fact", _compact_product_output(output), tool_name, citation))
            elif tool_name == "sql.inventory_by_sku":
                pack.structured_facts.append(StructuredFact("inventory", output, tool_name, citation))
            elif tool_name == "policy.return_eligibility":
                pack.structured_facts.append(StructuredFact("return_eligibility", output, tool_name, citation))

        confirmed_products = {
            str(product.get("product_id"))
            for product in state.tool_results.get("products", [])
            if product.get("product_id")
        } | {
            str(order.get("product_id"))
            for order in state.tool_results.get("orders", [])
            if order.get("product_id")
        }
        for result in state.retrieved_contexts:
            evidence = _doc_evidence(result)
            product_id = str(result.chunk.metadata.get("product_id", ""))
            if confirmed_products and product_id and product_id not in confirmed_products:
                pack.unresolved_conflicts.append(
                    EvidenceConflict(
                        "product_mismatch",
                        {"structured_product_ids": sorted(confirmed_products), "doc_product_id": product_id, "doc_id": result.chunk.doc_id},
                        "drop_doc_evidence",
                    )
                )
                continue
            if result.chunk.source == "kb":
                pack.policy_evidence.append(evidence)
            elif result.chunk.source == "product":
                pack.product_evidence.append(evidence)
            elif result.chunk.source == "review":
                pack.review_evidence.append(evidence)
            elif result.chunk.source == "ticket":
                pack.ticket_evidence.append(evidence)
        return pack


def _compact_product_output(output: dict[str, Any]) -> dict[str, Any]:
    if "products" in output:
        return {"products": output.get("products", [])[:4]}
    return {key: output.get(key) for key in ["product_id", "sku", "title", "price", "stock", "average_rating"] if key in output}


def _compact_order_output(output: dict[str, Any]) -> dict[str, Any]:
    return {
        key: output.get(key)
        for key in ["order_id", "status", "delivery_status", "sku", "product_id", "total", "order_date"]
        if key in output
    }


def _doc_evidence(result: Any) -> DocEvidence:
    doc_type = str(result.chunk.metadata.get("doc_type") or result.chunk.metadata.get("document_type") or result.chunk.source)
    return DocEvidence(
        evidence_type=doc_type,
        source=result.chunk.source,
        doc_id=result.chunk.doc_id,
        chunk_id=result.chunk.chunk_id,
        citation=f"[doc:{result.chunk.source}:{result.chunk.doc_id}#{result.chunk.chunk_id}]",
        preview=result.chunk.text[:240],
        metadata=result.chunk.metadata,
    )
