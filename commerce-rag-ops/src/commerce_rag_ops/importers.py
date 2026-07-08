from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any
from urllib.request import urlopen

from .etl import write_jsonl


def import_amazon_reviews_sample(
    data_dir: Path,
    *,
    categories: list[str],
    review_limit_per_category: int = 50,
    product_limit_per_category: int = 50,
) -> dict[str, Any]:
    """Import a small Amazon Reviews 2023 sample through HuggingFace datasets.

    This is optional on purpose. The repository ships with synthetic seed data so
    the project is always runnable; this importer is the bridge to public
    real-world ecommerce data when the `datasets` package and network access are
    available.
    """
    products: dict[str, dict[str, Any]] = {}
    reviews: list[dict[str, Any]] = []

    for category in categories:
        try:
            review_rows, meta_rows = _load_via_huggingface(
                category,
                review_limit_per_category=review_limit_per_category,
                product_limit_per_category=product_limit_per_category,
            )
            loader = "huggingface"
        except Exception:
            review_rows = _load_native_jsonl_gz(
                f"https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/{category}.jsonl.gz",
                review_limit_per_category,
            )
            meta_rows = _load_native_jsonl_gz(
                f"https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_{category}.jsonl.gz",
                product_limit_per_category,
            )
            loader = "native_jsonl_gz"

        for row in meta_rows:
            product_id = str(row.get("parent_asin") or row.get("asin") or "").strip()
            if not product_id:
                continue
            products[product_id] = {
                "product_id": product_id,
                "sku": product_id,
                "title": str(row.get("title") or "Untitled product"),
                "category": category,
                "price": _safe_float(row.get("price"), 0.0),
                "stock": 0,
                "average_rating": _safe_float(row.get("average_rating"), 0.0),
                "rating_number": int(_safe_float(row.get("rating_number"), 0.0)),
                "features": _safe_string_list(row.get("features")),
                "description": _join_description(row),
            }

        for idx, row in enumerate(review_rows):
            product_id = str(row.get("parent_asin") or row.get("asin") or "").strip()
            if not product_id:
                continue
            reviews.append(
                {
                    "review_id": f"{category}-{idx:06d}",
                    "product_id": product_id,
                    "rating": int(_safe_float(row.get("rating"), 0.0)),
                    "text": str(row.get("text") or row.get("title") or ""),
                    "verified_purchase": bool(row.get("verified_purchase", False)),
                    "timestamp": str(row.get("timestamp") or ""),
                }
            )

    write_jsonl(data_dir / "raw" / "products.amazon_sample.jsonl", products.values())
    write_jsonl(data_dir / "raw" / "reviews.amazon_sample.jsonl", reviews)
    return {
        "categories": categories,
        "loader": loader,
        "products": len(products),
        "reviews": len(reviews),
        "products_path": str(data_dir / "raw" / "products.amazon_sample.jsonl"),
        "reviews_path": str(data_dir / "raw" / "reviews.amazon_sample.jsonl"),
        "note": "Generated sample files are separate from the default seed data. Review before replacing products.jsonl/reviews.jsonl.",
    }


def _load_via_huggingface(
    category: str,
    *,
    review_limit_per_category: int,
    product_limit_per_category: int,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    from datasets import load_dataset

    review_rows = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023",
        f"raw_review_{category}",
        split=f"full[:{review_limit_per_category}]",
    )
    meta_rows = load_dataset(
        "McAuley-Lab/Amazon-Reviews-2023",
        f"raw_meta_{category}",
        split=f"full[:{product_limit_per_category}]",
    )
    return list(review_rows), list(meta_rows)


def _load_native_jsonl_gz(url: str, limit: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with urlopen(url, timeout=60) as response:
        with gzip.GzipFile(fileobj=response) as gz:
            for raw_line in gz:
                if len(rows) >= limit:
                    break
                line = raw_line.decode("utf-8").strip()
                if line:
                    rows.append(json.loads(line))
    return rows


def download_amazon_reviews_full(
    data_dir: Path,
    *,
    categories: list[str],
    count_rows: bool = False,
    force: bool = False,
) -> dict[str, Any]:
    """Download official Amazon Reviews 2023 raw gzip files for categories."""
    root = data_dir / "raw" / "amazon_reviews_2023"
    root.mkdir(parents=True, exist_ok=True)
    files: list[dict[str, Any]] = []
    for category in categories:
        category_dir = root / category
        category_dir.mkdir(parents=True, exist_ok=True)
        specs = [
            (
                "reviews",
                f"https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/{category}.jsonl.gz",
                category_dir / "reviews.jsonl.gz",
            ),
            (
                "metadata",
                f"https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_{category}.jsonl.gz",
                category_dir / "metadata.jsonl.gz",
            ),
        ]
        for kind, url, path in specs:
            if force and path.exists():
                path.unlink()
            if not path.exists():
                _download_file(url, path)
            row_count = count_jsonl_gz(path) if count_rows else None
            files.append(
                {
                    "category": category,
                    "kind": kind,
                    "url": url,
                    "path": str(path),
                    "bytes": path.stat().st_size,
                    "rows": row_count,
                }
            )
    manifest = {"source": "Amazon Reviews 2023 / UCSD McAuley Lab", "categories": categories, "files": files}
    manifest_path = root / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return {"manifest_path": str(manifest_path), **manifest}


def _download_file(url: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".part")
    with urlopen(url, timeout=120) as response:
        with tmp_path.open("wb") as out:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                out.write(chunk)
    tmp_path.replace(path)


def count_jsonl_gz(path: Path) -> int:
    count = 0
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                count += 1
    return count


def _safe_float(value: Any, default: float) -> float:
    try:
        if value in (None, ""):
            return default
        return float(str(value).replace("$", "").replace(",", ""))
    except (TypeError, ValueError):
        return default


def _safe_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if item]
    return [str(value)]


def _join_description(row: dict[str, Any]) -> str:
    parts: list[str] = []
    for field in ("title", "description"):
        value = row.get(field)
        if isinstance(value, list):
            parts.extend(str(item) for item in value if item)
        elif value:
            parts.append(str(value))
    parts.extend(_safe_string_list(row.get("features")))
    return " ".join(parts)
