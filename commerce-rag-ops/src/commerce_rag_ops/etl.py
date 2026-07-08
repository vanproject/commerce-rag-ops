from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

from .chunking import sentence_aware_chunks
from .document_loaders import load_knowledge_documents
from .models import CustomerSegment, DocumentChunk, Order, OrderItem, Product, Review, Ticket
from .text import normalize_text


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def load_products(data_dir: Path) -> list[Product]:
    return [Product(**row) for row in read_jsonl(data_dir / "raw" / "products.jsonl")]


def load_reviews(data_dir: Path) -> list[Review]:
    return [Review(**row) for row in read_jsonl(data_dir / "raw" / "reviews.jsonl")]


def load_tickets(data_dir: Path) -> list[Ticket]:
    return [Ticket(**row) for row in read_jsonl(data_dir / "raw" / "support_tickets.jsonl")]


def load_orders(data_dir: Path) -> list[Order]:
    return [Order(**row) for row in read_jsonl(data_dir / "raw" / "orders.jsonl")]


def load_order_items(data_dir: Path) -> list[OrderItem]:
    path = data_dir / "raw" / "order_items.jsonl"
    if path.exists():
        return [OrderItem(**row) for row in read_jsonl(path)]
    return [
        OrderItem(
            order_id=order.order_id,
            product_id=order.product_id,
            sku=order.sku,
            quantity=1,
            unit_price=order.total,
            line_total=order.total,
        )
        for order in load_orders(data_dir)
    ]


def load_customer_segments(data_dir: Path) -> list[CustomerSegment]:
    return [CustomerSegment(**row) for row in read_jsonl(data_dir / "raw" / "customer_segments.jsonl")]


def load_kb_chunks(data_dir: Path) -> list[DocumentChunk]:
    chunks: list[DocumentChunk] = []
    for doc in load_knowledge_documents(data_dir):
        chunk_size, chunk_overlap = _knowledge_chunk_profile(doc.metadata.get("document_type", ""))
        chunks.extend(
            sentence_aware_chunks(
                doc.text,
                source="kb",
                doc_id=doc.doc_id,
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                metadata={
                    **doc.metadata,
                    "title": doc.title,
                    "policy_type": doc.doc_id.split("_", 1)[-1],
                },
            )
        )
    return chunks


def _knowledge_chunk_profile(document_type: str) -> tuple[int, int]:
    if document_type == "structured_table":
        return 420, 50
    if document_type == "ocr_image":
        return 360, 45
    return 520, 60


def build_product_chunks(products: list[Product]) -> list[DocumentChunk]:
    chunks: list[DocumentChunk] = []
    for product in products:
        text = " ".join(
            [
                product.title,
                product.category,
                product.description,
                " ".join(product.features),
                f"price {product.price}",
                f"rating {product.average_rating}",
            ]
        )
        chunks.extend(
            sentence_aware_chunks(
                normalize_text(text),
                source="product",
                doc_id=product.product_id,
                chunk_size=480,
                chunk_overlap=40,
                metadata={
                    "product_id": product.product_id,
                    "sku": product.sku,
                    "category": product.category,
                    "price": product.price,
                    "average_rating": product.average_rating,
                    "stock": product.stock,
                },
            )
        )
    return chunks


def build_review_chunks(reviews: list[Review], products: list[Product]) -> list[DocumentChunk]:
    product_by_id = {product.product_id: product for product in products}
    chunks: list[DocumentChunk] = []
    for review in reviews:
        product = product_by_id.get(review.product_id)
        title = product.title if product else review.product_id
        text = f"Review for {title}. Rating {review.rating}. {review.text}"
        chunks.extend(
            sentence_aware_chunks(
                text,
                source="review",
                doc_id=review.review_id,
                chunk_size=360,
                chunk_overlap=30,
                metadata={
                    "review_id": review.review_id,
                    "product_id": review.product_id,
                    "rating": review.rating,
                    "verified_purchase": review.verified_purchase,
                    "timestamp": review.timestamp,
                },
            )
        )
    return chunks


def build_ticket_chunks(tickets: list[Ticket]) -> list[DocumentChunk]:
    chunks: list[DocumentChunk] = []
    for ticket in tickets:
        text = f"Customer Query: {ticket.customer_query}\nResolution: {ticket.resolution}"
        chunks.extend(
            sentence_aware_chunks(
                text,
                source="ticket",
                doc_id=ticket.ticket_id,
                chunk_size=280,
                chunk_overlap=35,
                metadata={
                    "ticket_id": ticket.ticket_id,
                    "category": ticket.category,
                    "product_id": ticket.product_id,
                    "status": ticket.status,
                    "date": ticket.date,
                    "expected_policy_doc": ticket.expected_policy_doc,
                },
            )
        )
    return chunks


def build_scale_chunks(data_dir: Path) -> list[DocumentChunk]:
    from .scale_builder import load_scale_rag_documents

    chunks: list[DocumentChunk] = []
    for doc in load_scale_rag_documents(data_dir):
        chunk_size, chunk_overlap = _scale_chunk_profile(doc.get("doc_type", ""))
        metadata = {
            **doc.get("metadata", {}),
            "doc_type": doc.get("doc_type", ""),
            "title": doc.get("title", ""),
            "product_id": doc.get("product_id", ""),
            "category": doc.get("category", ""),
            "scale_dataset": True,
        }
        chunks.extend(
            sentence_aware_chunks(
                doc["text"],
                source=doc["source"],
                doc_id=doc["doc_id"],
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
                metadata=metadata,
            )
        )
    return chunks


def _scale_chunk_profile(doc_type: str) -> tuple[int, int]:
    if doc_type == "product_profile":
        return 720, 80
    if doc_type == "review_evidence":
        return 420, 35
    if doc_type == "faq_case":
        return 360, 40
    return 560, 60


def build_all_chunks(data_dir: Path) -> list[DocumentChunk]:
    products = load_products(data_dir)
    reviews = load_reviews(data_dir)
    tickets = load_tickets(data_dir)
    return [
        *load_kb_chunks(data_dir),
        *build_product_chunks(products),
        *build_review_chunks(reviews, products),
        *build_ticket_chunks(tickets),
        *build_scale_chunks(data_dir),
    ]


def persist_processed(data_dir: Path) -> list[DocumentChunk]:
    chunks = build_all_chunks(data_dir)
    write_jsonl(data_dir / "processed" / "chunks.jsonl", [chunk_to_dict(c) for c in chunks])
    return chunks


def chunk_to_dict(chunk: DocumentChunk) -> dict:
    return {
        "chunk_id": chunk.chunk_id,
        "source": chunk.source,
        "doc_id": chunk.doc_id,
        "text": chunk.text,
        "metadata": chunk.metadata,
    }


def chunk_from_dict(row: dict) -> DocumentChunk:
    return DocumentChunk(
        chunk_id=row["chunk_id"],
        source=row["source"],
        doc_id=row["doc_id"],
        text=row["text"],
        metadata=row.get("metadata", {}),
    )


def load_processed_chunks(data_dir: Path) -> list[DocumentChunk]:
    path = data_dir / "processed" / "chunks.jsonl"
    if not path.exists():
        return persist_processed(data_dir)
    return [chunk_from_dict(row) for row in read_jsonl(path)]
