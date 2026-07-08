from __future__ import annotations

import json
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Any

from .etl import (
    load_customer_segments,
    load_order_items,
    load_orders,
    load_processed_chunks,
    load_products,
    load_reviews,
    load_tickets,
    read_jsonl,
)
from .document_loaders import load_knowledge_documents
from .models import Order, Product


def default_db_path(data_dir: Path) -> Path:
    return data_dir / "structured" / "commerce.db"


class SQLStore:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def product_by_id(self, product_id: str) -> Product | None:
        with closing(self.connect()) as conn:
            row = conn.execute("SELECT * FROM products WHERE product_id = ?", (product_id,)).fetchone()
        return _product_from_row(row) if row else None

    def product_by_sku(self, sku: str) -> Product | None:
        with closing(self.connect()) as conn:
            row = conn.execute("SELECT * FROM products WHERE lower(sku) = lower(?)", (sku,)).fetchone()
        return _product_from_row(row) if row else None

    def order_by_id(self, order_id: str) -> Order | None:
        with closing(self.connect()) as conn:
            row = conn.execute("SELECT * FROM orders WHERE lower(order_id) = lower(?)", (order_id,)).fetchone()
        return _order_from_row(row) if row else None

    def order_items_by_order_id(self, order_id: str) -> list[dict[str, Any]]:
        with closing(self.connect()) as conn:
            try:
                rows = conn.execute(
                    """
                    SELECT order_id, product_id, sku, quantity, unit_price, line_total
                    FROM order_items
                    WHERE lower(order_id) = lower(?)
                    ORDER BY rowid
                    """,
                    (order_id,),
                ).fetchall()
            except sqlite3.OperationalError:
                order = self.order_by_id(order_id)
                if not order:
                    return []
                return [
                    {
                        "order_id": order.order_id,
                        "product_id": order.product_id,
                        "sku": order.sku,
                        "quantity": 1,
                        "unit_price": order.total,
                        "line_total": order.total,
                    }
                ]
        return [dict(row) for row in rows]

    def summary(self) -> dict[str, Any]:
        return summarize_sqlite_store(self.db_path)


def build_sqlite_store(data_dir: Path, db_path: Path | None = None) -> dict[str, Any]:
    db_path = db_path or default_db_path(data_dir)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if db_path.exists():
        db_path.unlink()

    with closing(sqlite3.connect(db_path)) as conn:
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA foreign_keys=ON")
        _create_schema(conn)
        _insert_seed_operational_data(conn, data_dir)
        _insert_generated_data(conn, data_dir)
        _insert_downloaded_data_registry(conn, data_dir)
        _create_indexes(conn)
        conn.commit()

    return summarize_sqlite_store(db_path)


def summarize_sqlite_store(db_path: Path) -> dict[str, Any]:
    if not db_path.exists():
        return {"exists": False, "path": str(db_path), "tables": {}}

    with closing(sqlite3.connect(db_path)) as conn:
        tables = [
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
        counts = {table: conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0] for table in tables}
        indexes = [
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='index' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
    return {"exists": True, "path": str(db_path), "tables": counts, "indexes": indexes}


def _create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE products (
            product_id TEXT PRIMARY KEY,
            sku TEXT UNIQUE NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL,
            average_rating REAL NOT NULL,
            rating_number INTEGER NOT NULL,
            features_json TEXT NOT NULL,
            description TEXT NOT NULL
        );

        CREATE TABLE reviews (
            review_id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            rating INTEGER NOT NULL,
            text TEXT NOT NULL,
            verified_purchase INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        );

        CREATE TABLE support_tickets (
            ticket_id TEXT PRIMARY KEY,
            category TEXT NOT NULL,
            product_id TEXT NOT NULL,
            customer_query TEXT NOT NULL,
            resolution TEXT NOT NULL,
            status TEXT NOT NULL,
            date TEXT NOT NULL,
            expected_policy_doc TEXT NOT NULL
        );

        CREATE TABLE orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT NOT NULL,
            product_id TEXT NOT NULL,
            sku TEXT NOT NULL,
            status TEXT NOT NULL,
            delivery_status TEXT NOT NULL,
            order_date TEXT NOT NULL,
            total REAL NOT NULL
        );

        CREATE TABLE order_items (
            order_id TEXT NOT NULL,
            product_id TEXT NOT NULL,
            sku TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            line_total REAL NOT NULL,
            FOREIGN KEY(order_id) REFERENCES orders(order_id)
        );

        CREATE TABLE customer_segments (
            customer_id TEXT PRIMARY KEY,
            segment TEXT NOT NULL,
            preferred_category TEXT NOT NULL,
            lifetime_value REAL NOT NULL,
            churn_risk TEXT NOT NULL,
            notes TEXT NOT NULL
        );

        CREATE TABLE kb_articles (
            doc_id TEXT PRIMARY KEY,
            filename TEXT NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        );

        CREATE TABLE golden_eval (
            query_id TEXT PRIMARY KEY,
            query TEXT NOT NULL,
            sources_json TEXT NOT NULL,
            relevant_doc_ids_json TEXT NOT NULL,
            expected_keywords_json TEXT NOT NULL,
            must_cite INTEGER NOT NULL
        );

        CREATE TABLE document_chunks (
            chunk_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            doc_id TEXT NOT NULL,
            text TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        );

        CREATE TABLE amazon_sample_products (
            product_id TEXT PRIMARY KEY,
            sku TEXT NOT NULL,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL,
            average_rating REAL NOT NULL,
            rating_number INTEGER NOT NULL,
            features_json TEXT NOT NULL,
            description TEXT NOT NULL
        );

        CREATE TABLE amazon_sample_reviews (
            review_id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            rating INTEGER NOT NULL,
            text TEXT NOT NULL,
            verified_purchase INTEGER NOT NULL,
            timestamp TEXT NOT NULL
        );

        CREATE TABLE public_data_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT NOT NULL,
            category TEXT NOT NULL,
            kind TEXT NOT NULL,
            url TEXT NOT NULL,
            path TEXT NOT NULL,
            bytes INTEGER NOT NULL,
            rows INTEGER NOT NULL
        );

        CREATE TABLE scale_products (
            product_id TEXT PRIMARY KEY,
            sku TEXT NOT NULL,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            average_rating REAL NOT NULL,
            rating_number INTEGER NOT NULL,
            price REAL NOT NULL,
            store TEXT NOT NULL,
            features_json TEXT NOT NULL,
            description TEXT NOT NULL,
            details_json TEXT NOT NULL
        );

        CREATE TABLE scale_reviews (
            review_id TEXT PRIMARY KEY,
            product_id TEXT NOT NULL,
            category TEXT NOT NULL,
            rating INTEGER NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            verified_purchase INTEGER NOT NULL,
            timestamp TEXT NOT NULL,
            helpful_vote INTEGER NOT NULL,
            aspects_json TEXT NOT NULL
        );

        CREATE TABLE scale_rag_documents (
            doc_id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            doc_type TEXT NOT NULL,
            product_id TEXT NOT NULL,
            category TEXT NOT NULL,
            title TEXT NOT NULL,
            text TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        );
        """
    )


def _insert_seed_operational_data(conn: sqlite3.Connection, data_dir: Path) -> None:
    conn.executemany(
        """
        INSERT INTO products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                p.product_id,
                p.sku,
                p.title,
                p.category,
                p.price,
                p.stock,
                p.average_rating,
                p.rating_number,
                json.dumps(p.features, ensure_ascii=False),
                p.description,
            )
            for p in load_products(data_dir)
        ],
    )
    conn.executemany(
        "INSERT INTO reviews VALUES (?, ?, ?, ?, ?, ?)",
        [(r.review_id, r.product_id, r.rating, r.text, int(r.verified_purchase), r.timestamp) for r in load_reviews(data_dir)],
    )
    conn.executemany(
        "INSERT INTO support_tickets VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                t.ticket_id,
                t.category,
                t.product_id,
                t.customer_query,
                t.resolution,
                t.status,
                t.date,
                t.expected_policy_doc,
            )
            for t in load_tickets(data_dir)
        ],
    )
    conn.executemany(
        "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (o.order_id, o.customer_id, o.product_id, o.sku, o.status, o.delivery_status, o.order_date, o.total)
            for o in load_orders(data_dir)
        ],
    )
    conn.executemany(
        "INSERT INTO order_items VALUES (?, ?, ?, ?, ?, ?)",
        [
            (item.order_id, item.product_id, item.sku, item.quantity, item.unit_price, item.line_total)
            for item in load_order_items(data_dir)
        ],
    )
    conn.executemany(
        "INSERT INTO customer_segments VALUES (?, ?, ?, ?, ?, ?)",
        [
            (c.customer_id, c.segment, c.preferred_category, c.lifetime_value, c.churn_risk, c.notes)
            for c in load_customer_segments(data_dir)
        ],
    )

    conn.executemany(
        "INSERT INTO kb_articles VALUES (?, ?, ?, ?, ?)",
        [
            (
                doc.doc_id,
                doc.metadata.get("filename", doc.doc_id),
                doc.title,
                doc.text,
                json.dumps(doc.metadata, ensure_ascii=False),
            )
            for doc in load_knowledge_documents(data_dir)
        ],
    )


def _insert_generated_data(conn: sqlite3.Connection, data_dir: Path) -> None:
    conn.executemany(
        "INSERT INTO golden_eval VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["query_id"],
                row["query"],
                json.dumps(row.get("sources", []), ensure_ascii=False),
                json.dumps(row.get("relevant_doc_ids", []), ensure_ascii=False),
                json.dumps(row.get("expected_keywords", []), ensure_ascii=False),
                int(row.get("must_cite", False)),
            )
            for row in read_jsonl(data_dir / "eval" / "golden.jsonl")
        ],
    )
    conn.executemany(
        "INSERT INTO document_chunks VALUES (?, ?, ?, ?, ?)",
        [
            (chunk.chunk_id, chunk.source, chunk.doc_id, chunk.text, json.dumps(chunk.metadata, ensure_ascii=False))
            for chunk in load_processed_chunks(data_dir)
        ],
    )
    scale_products = read_jsonl(data_dir / "scale" / "products.jsonl")
    scale_reviews = read_jsonl(data_dir / "scale" / "reviews.jsonl")
    scale_docs = read_jsonl(data_dir / "scale" / "rag_documents.jsonl")
    conn.executemany(
        "INSERT INTO scale_products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["product_id"],
                row.get("sku", row["product_id"]),
                row.get("category", ""),
                row.get("title", ""),
                float(row.get("average_rating", 0.0)),
                int(row.get("rating_number", 0)),
                float(row.get("price", 0.0)),
                row.get("store", ""),
                json.dumps(row.get("features", []), ensure_ascii=False),
                row.get("description", ""),
                row.get("details_json", "{}"),
            )
            for row in scale_products
        ],
    )
    conn.executemany(
        "INSERT INTO scale_reviews VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["review_id"],
                row["product_id"],
                row["category"],
                int(row.get("rating", 0)),
                row.get("title", ""),
                row.get("text", ""),
                int(row.get("verified_purchase", False)),
                str(row.get("timestamp", "")),
                int(row.get("helpful_vote", 0)),
                json.dumps(row.get("aspects", []), ensure_ascii=False),
            )
            for row in scale_reviews
        ],
    )
    conn.executemany(
        "INSERT INTO scale_rag_documents VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["doc_id"],
                row["source"],
                row["doc_type"],
                row.get("product_id", ""),
                row.get("category", ""),
                row.get("title", ""),
                row.get("text", ""),
                json.dumps(row.get("metadata", {}), ensure_ascii=False),
            )
            for row in scale_docs
        ],
    )


def _insert_downloaded_data_registry(conn: sqlite3.Connection, data_dir: Path) -> None:
    sample_products = read_jsonl(data_dir / "raw" / "products.amazon_sample.jsonl")
    sample_reviews = read_jsonl(data_dir / "raw" / "reviews.amazon_sample.jsonl")
    conn.executemany(
        "INSERT INTO amazon_sample_products VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
        [
            (
                row["product_id"],
                row.get("sku", row["product_id"]),
                row.get("title", ""),
                row.get("category", ""),
                float(row.get("price", 0.0)),
                float(row.get("average_rating", 0.0)),
                int(row.get("rating_number", 0)),
                json.dumps(row.get("features", []), ensure_ascii=False),
                row.get("description", ""),
            )
            for row in sample_products
        ],
    )
    conn.executemany(
        "INSERT INTO amazon_sample_reviews VALUES (?, ?, ?, ?, ?, ?)",
        [
            (
                row["review_id"],
                row["product_id"],
                int(row.get("rating", 0)),
                row.get("text", ""),
                int(row.get("verified_purchase", False)),
                str(row.get("timestamp", "")),
            )
            for row in sample_reviews
        ],
    )

    manifest_path = data_dir / "raw" / "amazon_reviews_2023" / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        conn.executemany(
            "INSERT INTO public_data_files (source, category, kind, url, path, bytes, rows) VALUES (?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    manifest.get("source", ""),
                    item.get("category", ""),
                    item.get("kind", ""),
                    item.get("url", ""),
                    item.get("path", ""),
                    int(item.get("bytes", 0)),
                    int(item.get("rows", 0)),
                )
                for item in manifest.get("files", [])
            ],
        )


def _create_indexes(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE INDEX idx_products_category ON products(category);
        CREATE INDEX idx_products_sku_lower ON products(lower(sku));
        CREATE INDEX idx_reviews_product_id ON reviews(product_id);
        CREATE INDEX idx_reviews_rating ON reviews(rating);
        CREATE INDEX idx_tickets_product_id ON support_tickets(product_id);
        CREATE INDEX idx_orders_customer_id ON orders(customer_id);
        CREATE INDEX idx_orders_sku ON orders(sku);
        CREATE INDEX idx_order_items_order_id ON order_items(order_id);
        CREATE INDEX idx_order_items_sku ON order_items(sku);
        CREATE INDEX idx_segments_churn_risk ON customer_segments(churn_risk);
        CREATE INDEX idx_chunks_source_doc ON document_chunks(source, doc_id);
        CREATE INDEX idx_public_data_files_category ON public_data_files(category, kind);
        CREATE INDEX idx_scale_products_category ON scale_products(category);
        CREATE INDEX idx_scale_reviews_product_id ON scale_reviews(product_id);
        CREATE INDEX idx_scale_reviews_category_rating ON scale_reviews(category, rating);
        CREATE INDEX idx_scale_rag_documents_type ON scale_rag_documents(doc_type);
        CREATE INDEX idx_scale_rag_documents_product_id ON scale_rag_documents(product_id);
        """
    )


def _product_from_row(row: sqlite3.Row) -> Product:
    return Product(
        product_id=row["product_id"],
        sku=row["sku"],
        title=row["title"],
        category=row["category"],
        price=float(row["price"]),
        stock=int(row["stock"]),
        average_rating=float(row["average_rating"]),
        rating_number=int(row["rating_number"]),
        features=json.loads(row["features_json"]),
        description=row["description"],
    )


def _order_from_row(row: sqlite3.Row) -> Order:
    return Order(
        order_id=row["order_id"],
        customer_id=row["customer_id"],
        product_id=row["product_id"],
        sku=row["sku"],
        status=row["status"],
        delivery_status=row["delivery_status"],
        order_date=row["order_date"],
        total=float(row["total"]),
    )
