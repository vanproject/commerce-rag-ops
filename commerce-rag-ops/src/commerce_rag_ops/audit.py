from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from .etl import (
    load_customer_segments,
    load_kb_chunks,
    load_orders,
    load_processed_chunks,
    load_products,
    load_reviews,
    load_tickets,
    read_jsonl,
)
from .document_loaders import load_knowledge_documents_with_report
from .scale_builder import load_scale_manifest
from .sql_store import default_db_path, summarize_sqlite_store


def audit_project(data_dir: Path, qdrant_path: Path | None = None) -> dict[str, Any]:
    raw_dir = data_dir / "raw"
    amazon_products = raw_dir / "products.amazon_sample.jsonl"
    amazon_reviews = raw_dir / "reviews.amazon_sample.jsonl"
    full_manifest_path = raw_dir / "amazon_reviews_2023" / "manifest.json"
    full_manifest = json.loads(full_manifest_path.read_text(encoding="utf-8")) if full_manifest_path.exists() else None
    knowledge_report = load_knowledge_documents_with_report(data_dir)
    scale_manifest = load_scale_manifest(data_dir)
    return {
        "data_counts": {
            "products": len(load_products(data_dir)),
            "reviews": len(load_reviews(data_dir)),
            "support_tickets": len(load_tickets(data_dir)),
            "kb_chunks": len(load_kb_chunks(data_dir)),
            "orders": len(load_orders(data_dir)),
            "customer_segments": len(load_customer_segments(data_dir)),
            "processed_chunks": len(load_processed_chunks(data_dir)),
            "golden_eval_queries": len(read_jsonl(data_dir / "eval" / "golden.jsonl")),
        },
        "document_ingestion": {
            "knowledge_documents": len(knowledge_report.documents),
            "document_types": _count_by_metadata(knowledge_report.documents, "document_type"),
            "extraction_methods": _count_by_metadata(knowledge_report.documents, "extraction_method"),
            "skipped_files": knowledge_report.skipped,
        },
        "scale_subset": scale_manifest or {},
        "public_data_downloads": {
            "amazon_products_sample_exists": amazon_products.exists(),
            "amazon_products_sample_rows": len(read_jsonl(amazon_products)) if amazon_products.exists() else 0,
            "amazon_reviews_sample_exists": amazon_reviews.exists(),
            "amazon_reviews_sample_rows": len(read_jsonl(amazon_reviews)) if amazon_reviews.exists() else 0,
            "amazon_full_manifest_exists": full_manifest_path.exists(),
            "amazon_full_manifest_path": str(full_manifest_path) if full_manifest_path.exists() else "",
            "amazon_full_categories": full_manifest.get("categories", []) if full_manifest else [],
            "amazon_full_files": full_manifest.get("files", []) if full_manifest else [],
            "note": "Amazon Reviews 2023 sample is optional and stored separately from curated seed data.",
        },
        "qdrant": {
            "path": str(qdrant_path) if qdrant_path else None,
            "local_path_exists": bool(qdrant_path and qdrant_path.exists()),
            "embedding_config": _read_qdrant_embedding_config(qdrant_path),
        },
        "sqlite": summarize_sqlite_store(default_db_path(data_dir)),
        "llm": {
            "endpoint_configured": bool(os.getenv("COMMERCE_RAG_LLM_ENDPOINT")),
            "api_key_configured": bool(os.getenv("COMMERCE_RAG_LLM_API_KEY")),
            "model": os.getenv("COMMERCE_RAG_LLM_MODEL", ""),
        },
    }


def write_audit_report(path: Path, audit: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 项目覆盖审计",
        "",
        "## 数据量统计",
        "",
        "| 数据 | 数量 |",
        "|---|---:|",
    ]
    for key, value in audit["data_counts"].items():
        lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## 文档摄取",
            "",
            f"- 已抽取知识文档: {audit['document_ingestion']['knowledge_documents']}",
            f"- 跳过文件数: {len(audit['document_ingestion']['skipped_files'])}",
            "",
            "| 文档类型 | 数量 |",
            "|---|---:|",
        ]
    )
    for key, value in audit["document_ingestion"]["document_types"].items():
        lines.append(f"| {key} | {value} |")
    lines.extend(["", "| 抽取方法 | 数量 |", "|---|---:|"])
    for key, value in audit["document_ingestion"]["extraction_methods"].items():
        lines.append(f"| {key} | {value} |")
    if audit["document_ingestion"]["skipped_files"]:
        lines.extend(["", "跳过示例:"])
        for item in audit["document_ingestion"]["skipped_files"][:5]:
            lines.append(f"- `{item['path']}`: {item['reason']}")
    if audit.get("scale_subset"):
        scale = audit["scale_subset"]
        lines.extend(
            [
                "",
                "## Amazon 规模化子集",
                "",
                f"- 商品数: {scale.get('products', 0)}",
                f"- 评论数: {scale.get('reviews', 0)}",
                f"- RAG 文档数: {scale.get('rag_documents', 0)}",
                f"- Golden 评测问题数: {scale.get('golden_eval_queries', 0)}",
                "",
                "| 生成文档类型 | 数量 |",
                "|---|---:|",
            ]
        )
        for key, value in scale.get("document_types", {}).items():
            lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## 公共数据下载",
            "",
            f"- Amazon 商品样本存在: {audit['public_data_downloads']['amazon_products_sample_exists']}",
            f"- Amazon 商品样本行数: {audit['public_data_downloads']['amazon_products_sample_rows']}",
            f"- Amazon 评论样本存在: {audit['public_data_downloads']['amazon_reviews_sample_exists']}",
            f"- Amazon 评论样本行数: {audit['public_data_downloads']['amazon_reviews_sample_rows']}",
            f"- Amazon 全量 manifest 存在: {audit['public_data_downloads']['amazon_full_manifest_exists']}",
            f"- Amazon 全量分类: {', '.join(audit['public_data_downloads']['amazon_full_categories'])}",
            "",
            "## 运行时后端",
            "",
            f"- 本地 Qdrant 路径: {audit['qdrant']['path']}",
            f"- 本地 Qdrant 路径存在: {audit['qdrant']['local_path_exists']}",
            f"- Qdrant embedding 后端: {audit['qdrant']['embedding_config'].get('embedding_backend', '')}",
            f"- Qdrant embedding 模型: {audit['qdrant']['embedding_config'].get('embedding_model', '')}",
            f"- SQLite 结构化库: {audit['sqlite']['path']}",
            f"- SQLite 存在: {audit['sqlite']['exists']}",
            f"- LLM endpoint 已配置: {audit['llm']['endpoint_configured']}",
            f"- LLM API key 已配置: {audit['llm']['api_key_configured']}",
            f"- LLM 模型: {audit['llm']['model']}",
            "",
            "## 原始 JSON",
            "",
            "```json",
            json.dumps(audit, indent=2, ensure_ascii=False),
            "```",
            "",
        ]
    )
    if audit["sqlite"]["exists"]:
        lines.extend(
            [
                "## SQLite 表",
                "",
                "| 表 | 行数 |",
                "|---|---:|",
            ]
        )
        for table, count in audit["sqlite"]["tables"].items():
            lines.append(f"| {table} | {count} |")
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def _count_by_metadata(documents: list[Any], key: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for doc in documents:
        value = str(doc.metadata.get(key, "unknown"))
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items()))


def _read_qdrant_embedding_config(qdrant_path: Path | None) -> dict[str, Any]:
    if not qdrant_path:
        return {}
    configs = sorted(qdrant_path.glob("*.embedding.json")) if qdrant_path.exists() else []
    if not configs:
        return {}
    try:
        return json.loads(configs[0].read_text(encoding="utf-8"))
    except Exception:
        return {}
