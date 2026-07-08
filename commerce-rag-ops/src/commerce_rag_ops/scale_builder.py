from __future__ import annotations

import gzip
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

from .etl import read_jsonl, write_jsonl
from .text import normalize_text


DEFAULT_CATEGORIES = ["All_Beauty", "Software", "Baby_Products"]

ASPECT_KEYWORDS: dict[str, set[str]] = {
    "delivery": {"delivery", "shipping", "ship", "late", "package", "carrier", "lost", "arrived"},
    "refund_return": {"refund", "return", "replacement", "money", "exchange", "cancel"},
    "quality_damage": {"broken", "damaged", "defective", "leaking", "cracked", "stopped", "quality"},
    "digital_license": {"license", "key", "email", "activation", "subscription", "account", "renewal"},
    "battery_power": {"battery", "charge", "charging", "power", "drain", "overnight"},
    "skin_scent": {"skin", "scent", "smell", "hair", "irritate", "fragrance"},
    "missing_parts": {"missing", "part", "cap", "accessory", "piece", "included"},
    "price_value": {"price", "expensive", "cheap", "value", "worth", "cost"},
}


def build_scale_subset(
    data_dir: Path,
    *,
    categories: list[str] | None = None,
    reviews_per_category: int = 5000,
    products_per_category: int = 1000,
    eval_size: int = 360,
) -> dict[str, Any]:
    categories = categories or DEFAULT_CATEGORIES
    scale_dir = data_dir / "scale"
    scale_dir.mkdir(parents=True, exist_ok=True)

    all_products: list[dict[str, Any]] = []
    all_reviews: list[dict[str, Any]] = []
    category_summaries: list[dict[str, Any]] = []

    for category in categories:
        reviews = _sample_reviews(data_dir, category, reviews_per_category, products_per_category)
        product_ids = {row["product_id"] for row in reviews}
        products = _load_matching_products(data_dir, category, product_ids)
        products = [_fallback_product(product_id, category) for product_id in product_ids - {p["product_id"] for p in products}] + products
        products = sorted(products, key=lambda row: row["product_id"])
        all_reviews.extend(reviews)
        all_products.extend(products)
        category_summaries.append(
            {
                "category": category,
                "reviews": len(reviews),
                "products": len(products),
                "avg_rating": round(mean([r["rating"] for r in reviews]), 4) if reviews else 0.0,
            }
        )

    write_jsonl(scale_dir / "products.jsonl", all_products)
    write_jsonl(scale_dir / "reviews.jsonl", all_reviews)

    rag_documents = _build_rag_documents(all_products, all_reviews)
    write_jsonl(scale_dir / "rag_documents.jsonl", rag_documents)

    seed_golden = read_jsonl(data_dir / "eval" / "golden.seed.jsonl")
    if not seed_golden:
        seed_golden = read_jsonl(data_dir / "eval" / "golden.jsonl")
        write_jsonl(data_dir / "eval" / "golden.seed.jsonl", seed_golden)
    golden = [*seed_golden, *_build_scaled_eval(rag_documents, eval_size)]
    write_jsonl(data_dir / "eval" / "scripted_regression.jsonl", golden)
    write_jsonl(data_dir / "eval" / "golden.jsonl", golden)

    manifest = {
        "source": "Amazon Reviews 2023 full gzip subset",
        "categories": category_summaries,
        "reviews_per_category_target": reviews_per_category,
        "products_per_category_limit": products_per_category,
        "products": len(all_products),
        "reviews": len(all_reviews),
        "rag_documents": len(rag_documents),
        "golden_eval_queries": len(golden),
        "document_types": dict(Counter(doc["doc_type"] for doc in rag_documents)),
    }
    (scale_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    return manifest


def load_scale_rag_documents(data_dir: Path) -> list[dict[str, Any]]:
    return read_jsonl(data_dir / "scale" / "rag_documents.jsonl")


def load_scale_manifest(data_dir: Path) -> dict[str, Any] | None:
    path = data_dir / "scale" / "manifest.json"
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _sample_reviews(data_dir: Path, category: str, review_limit: int, product_limit: int) -> list[dict[str, Any]]:
    path = data_dir / "raw" / "amazon_reviews_2023" / category / "reviews.jsonl.gz"
    selected_products: dict[str, int] = {}
    seen_reviews: set[tuple[str, str, int]] = set()
    reviews: list[dict[str, Any]] = []
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for raw_index, line in enumerate(handle):
            row = json.loads(line)
            product_id = str(row.get("parent_asin") or row.get("asin") or "").strip()
            text = normalize_text(str(row.get("text") or ""))
            if not product_id or len(text) < 40:
                continue
            rating = int(round(float(row.get("rating") or 0)))
            if rating <= 0:
                continue
            if product_id not in selected_products:
                if len(selected_products) >= product_limit:
                    continue
                selected_products[product_id] = len(selected_products) + 1
            dedupe_key = (product_id, text[:120], rating)
            if dedupe_key in seen_reviews:
                continue
            seen_reviews.add(dedupe_key)
            review_id = f"AMZREV-{category}-{len(reviews)+1:05d}"
            reviews.append(
                {
                    "review_id": review_id,
                    "product_id": product_id,
                    "category": category,
                    "rating": rating,
                    "title": normalize_text(str(row.get("title") or ""))[:220],
                    "text": text[:1200],
                    "verified_purchase": bool(row.get("verified_purchase")),
                    "timestamp": str(row.get("timestamp") or ""),
                    "helpful_vote": int(row.get("helpful_vote") or 0),
                    "raw_index": raw_index,
                    "aspects": sorted(_detect_aspects(text)),
                }
            )
            if len(reviews) >= review_limit:
                break
    return reviews


def _load_matching_products(data_dir: Path, category: str, product_ids: set[str]) -> list[dict[str, Any]]:
    if not product_ids:
        return []
    path = data_dir / "raw" / "amazon_reviews_2023" / category / "metadata.jsonl.gz"
    products: list[dict[str, Any]] = []
    with gzip.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            row = json.loads(line)
            product_id = str(row.get("parent_asin") or "").strip()
            if product_id not in product_ids:
                continue
            products.append(
                {
                    "product_id": product_id,
                    "sku": product_id,
                    "category": category,
                    "title": normalize_text(str(row.get("title") or product_id))[:300],
                    "main_category": str(row.get("main_category") or category),
                    "average_rating": float(row.get("average_rating") or 0.0),
                    "rating_number": int(row.get("rating_number") or 0),
                    "price": float(row.get("price") or 0.0),
                    "store": str(row.get("store") or ""),
                    "features": _string_list(row.get("features")),
                    "description": " ".join(_string_list(row.get("description")))[:1200],
                    "details_json": json.dumps(row.get("details") or {}, ensure_ascii=False),
                }
            )
            if len(products) >= len(product_ids):
                break
    return products


def _build_rag_documents(products: list[dict[str, Any]], reviews: list[dict[str, Any]]) -> list[dict[str, Any]]:
    docs: list[dict[str, Any]] = []
    products_by_id = {p["product_id"]: p for p in products}
    reviews_by_product: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for review in reviews:
        reviews_by_product[review["product_id"]].append(review)

    for product in products:
        product_reviews = reviews_by_product.get(product["product_id"], [])
        docs.append(_product_profile_doc(product, product_reviews))

    for review in reviews:
        product = products_by_id.get(review["product_id"], _fallback_product(review["product_id"], review["category"]))
        docs.append(_review_evidence_doc(product, review))

    docs.extend(_aspect_summary_docs(products_by_id, reviews_by_product))
    docs.extend(_complaint_cluster_docs(reviews, products_by_id))
    docs.extend(_faq_case_docs(reviews, products_by_id, limit_per_category=180))
    return docs


def _product_profile_doc(product: dict[str, Any], reviews: list[dict[str, Any]]) -> dict[str, Any]:
    ratings = [r["rating"] for r in reviews]
    low = [r for r in reviews if r["rating"] <= 2]
    positive = [r for r in reviews if r["rating"] >= 4]
    top_aspects = Counter(aspect for r in reviews for aspect in r["aspects"]).most_common(5)
    text = " ".join(
        [
            f"Product profile for {product['title']} SKU {product['sku']} in category {product['category']}.",
            f"Catalog rating {product['average_rating']} from {product['rating_number']} public ratings; subset reviews {len(reviews)} with average {round(mean(ratings), 3) if ratings else 0.0}.",
            f"Features: {', '.join(product.get('features', [])[:8])}.",
            f"Description: {product.get('description') or product['title']}.",
            f"Top review aspects: {', '.join(f'{a}={c}' for a, c in top_aspects) or 'none'}.",
            f"Positive signals: {' | '.join(r['text'][:160] for r in positive[:2])}.",
            f"Risk signals: {' | '.join(r['text'][:160] for r in low[:2])}.",
        ]
    )
    return _rag_doc(
        source="product",
        doc_type="product_profile",
        doc_id=f"PP-{product['category']}-{product['product_id']}",
        text=text,
        product_id=product["product_id"],
        category=product["category"],
        title=product["title"],
        metadata={"review_count": len(reviews), "average_rating": product["average_rating"]},
    )


def _review_evidence_doc(product: dict[str, Any], review: dict[str, Any]) -> dict[str, Any]:
    text = " ".join(
        [
            f"Review evidence for {product['title']} SKU {product['sku']} in category {review['category']}.",
            f"Rating {review['rating']}. Verified purchase {review['verified_purchase']}.",
            f"Review title: {review['title']}.",
            f"Customer text: {review['text']}.",
            f"Detected aspects: {', '.join(review['aspects']) or 'general'}."
        ]
    )
    return _rag_doc(
        source="review",
        doc_type="review_evidence",
        doc_id=f"RV-{review['review_id']}",
        text=text,
        product_id=review["product_id"],
        category=review["category"],
        title=product["title"],
        metadata={
            "review_id": review["review_id"],
            "rating": review["rating"],
            "timestamp": review["timestamp"],
            "verified_purchase": review["verified_purchase"],
            "helpful_vote": review["helpful_vote"],
            "aspects": review["aspects"],
        },
    )


def _aspect_summary_docs(
    products_by_id: dict[str, dict[str, Any]], reviews_by_product: dict[str, list[dict[str, Any]]]
) -> list[dict[str, Any]]:
    docs: list[dict[str, Any]] = []
    for product_id, product_reviews in reviews_by_product.items():
        product = products_by_id.get(product_id, _fallback_product(product_id, product_reviews[0]["category"]))
        aspect_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for review in product_reviews:
            for aspect in review["aspects"]:
                aspect_groups[aspect].append(review)
        for aspect, rows in sorted(aspect_groups.items()):
            if len(rows) < 2:
                continue
            negative = [r for r in rows if r["rating"] <= 3]
            text = " ".join(
                [
                    f"Review aspect summary for {product['title']} aspect {aspect}.",
                    f"Category {product['category']}; matched reviews {len(rows)}; low rating reviews {len(negative)}.",
                    f"Representative evidence: {' | '.join(r['text'][:180] for r in rows[:4])}.",
                    f"Operational interpretation: monitor {aspect} complaints, compare recent low ratings, and route severe cases to support policy."
                ]
            )
            docs.append(
                _rag_doc(
                    source="review",
                    doc_type="review_aspect_summary",
                    doc_id=f"AS-{product['category']}-{product_id}-{aspect}",
                    text=text,
                    product_id=product_id,
                    category=product["category"],
                    title=product["title"],
                    metadata={"aspect": aspect, "review_count": len(rows), "negative_count": len(negative)},
                )
            )
    return docs


def _complaint_cluster_docs(reviews: list[dict[str, Any]], products_by_id: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for review in reviews:
        if review["rating"] > 3:
            continue
        aspects = review["aspects"] or ["general_complaint"]
        for aspect in aspects:
            groups[(review["category"], aspect)].append(review)
    docs: list[dict[str, Any]] = []
    for (category, aspect), rows in sorted(groups.items()):
        if len(rows) < 5:
            continue
        products = [products_by_id.get(r["product_id"], _fallback_product(r["product_id"], category))["title"] for r in rows[:8]]
        text = " ".join(
            [
                f"Complaint cluster for category {category} and aspect {aspect}.",
                f"Cluster size {len(rows)} from public review subset, average rating {round(mean([r['rating'] for r in rows]), 3)}.",
                f"Affected products include: {', '.join(products)}.",
                f"Representative complaints: {' | '.join(r['text'][:180] for r in rows[:5])}.",
                "Customer operations action: quantify trend, inspect product detail pages, update support macros, and escalate repeated severe defects."
            ]
        )
        docs.append(
            _rag_doc(
                source="review",
                doc_type="complaint_cluster",
                doc_id=f"CL-{category}-{aspect}",
                text=text,
                product_id="",
                category=category,
                title=f"{category} {aspect} complaint cluster",
                metadata={"aspect": aspect, "cluster_size": len(rows), "avg_rating": round(mean([r["rating"] for r in rows]), 3)},
            )
        )
    return docs


def _faq_case_docs(
    reviews: list[dict[str, Any]], products_by_id: dict[str, dict[str, Any]], *, limit_per_category: int
) -> list[dict[str, Any]]:
    docs: list[dict[str, Any]] = []
    counts: Counter[str] = Counter()
    for review in reviews:
        if counts[review["category"]] >= limit_per_category:
            continue
        if review["rating"] > 3 and not (set(review["aspects"]) & {"delivery", "refund_return", "quality_damage", "digital_license", "missing_parts"}):
            continue
        product = products_by_id.get(review["product_id"], _fallback_product(review["product_id"], review["category"]))
        aspect = (review["aspects"] or ["general_support"])[0]
        policy_hint = _policy_hint(aspect)
        question = f"Customer asks about {aspect} for {product['title']} after saying: {review['text'][:180]}"
        resolution = f"Validate order and SKU, collect required evidence, cite {policy_hint}, and avoid promising refund before eligibility is confirmed."
        counts[review["category"]] += 1
        text = f"FAQ case for {product['title']}. Question: {question}. Suggested resolution: {resolution}"
        docs.append(
            _rag_doc(
                source="ticket",
                doc_type="faq_case",
                doc_id=f"FAQ-{review['category']}-{counts[review['category']]:04d}",
                text=text,
                product_id=review["product_id"],
                category=review["category"],
                title=product["title"],
                metadata={"aspect": aspect, "rating": review["rating"], "derived_from_review_id": review["review_id"]},
            )
        )
    return docs


def _build_scaled_eval(rag_documents: list[dict[str, Any]], eval_size: int) -> list[dict[str, Any]]:
    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for doc in rag_documents:
        buckets[doc["doc_type"]].append(doc)
    related = _related_doc_ids(rag_documents)
    quotas = {
        "product_profile": eval_size // 4,
        "review_evidence": eval_size // 4,
        "review_aspect_summary": eval_size // 5,
        "complaint_cluster": eval_size // 8,
        "faq_case": eval_size,
    }
    rows: list[dict[str, Any]] = []
    for doc_type, quota in quotas.items():
        accepted = 0
        for doc in buckets.get(doc_type, []):
            if not _queryable_title(doc.get("title", "")):
                continue
            rows.append(_eval_row(len(rows) + 1, doc, related))
            accepted += 1
            if len(rows) >= eval_size:
                break
            if accepted >= quota:
                break
        if len(rows) >= eval_size:
            break
    return rows[:eval_size]


def _related_doc_ids(rag_documents: list[dict[str, Any]]) -> dict[str, dict[str, list[str]]]:
    by_product: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    by_product_rating: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    by_product_aspect: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    by_category_aspect: dict[tuple[str, str], dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for doc in rag_documents:
        full_id = f"{doc['source']}:{doc['doc_id']}"
        product_id = doc.get("product_id", "")
        doc_type = doc["doc_type"]
        if product_id:
            by_product[product_id][doc_type].append(full_id)
            rating = doc.get("metadata", {}).get("rating")
            if rating is not None:
                by_product_rating[(product_id, str(rating))][doc_type].append(full_id)
        aspect = doc.get("metadata", {}).get("aspect")
        if aspect:
            if product_id:
                by_product_aspect[(product_id, str(aspect))][doc_type].append(full_id)
            by_category_aspect[(doc.get("category", ""), str(aspect))][doc_type].append(full_id)
        for review_aspect in doc.get("metadata", {}).get("aspects", []):
            if product_id:
                by_product_aspect[(product_id, str(review_aspect))][doc_type].append(full_id)
    return {
        "by_product": {key: dict(value) for key, value in by_product.items()},
        "by_product_rating": {f"{key[0]}::{key[1]}": dict(value) for key, value in by_product_rating.items()},
        "by_product_aspect": {f"{key[0]}::{key[1]}": dict(value) for key, value in by_product_aspect.items()},
        "by_category_aspect": {f"{key[0]}::{key[1]}": dict(value) for key, value in by_category_aspect.items()},
    }


def _eval_row(index: int, doc: dict[str, Any], related: dict[str, dict[str, list[str]]]) -> dict[str, Any]:
    doc_type = doc["doc_type"]
    title = doc["title"][:80]
    aspect = doc["metadata"].get("aspect", "")
    category = doc["category"]
    relevant = _expanded_relevant_doc_ids(doc, related)
    if doc_type == "product_profile":
        query = f"Recommend or summarize product {title} in {category} using rating and review signals."
        intent = "recommendation"
        sources = ["product", "review"]
        keywords = ["rating", "review", category.split("_")[0].lower()]
        difficulty = "medium"
    elif doc_type == "review_evidence":
        rating = doc["metadata"].get("rating", "")
        query = f"Find review evidence for {title} with rating {rating} and explain customer feedback."
        intent = "customer_ops"
        sources = ["product", "review"]
        keywords = ["review", "rating", str(rating)]
        difficulty = "easy"
    elif doc_type == "review_aspect_summary":
        query = f"What customer ops issues appear for {title} around {aspect}?"
        intent = "customer_ops"
        sources = ["product", "review"]
        keywords = ["customer", "ops", str(aspect)]
        difficulty = "hard"
    elif doc_type == "complaint_cluster":
        query = f"What negative review trend appears in {category} for {aspect} complaints?"
        intent = "customer_ops"
        sources = ["review", "ticket"]
        keywords = ["negative", "review", str(aspect)]
        difficulty = "hard"
    else:
        query = f"How should support handle this {aspect} case for {title}?"
        intent = "support"
        sources = ["ticket", "kb", "review"]
        keywords = ["support", str(aspect), "evidence"]
        difficulty = "medium"
    return {
        "query_id": f"QS-{index:04d}",
        "query": query,
        "intent": intent,
        "difficulty": difficulty,
        "sources": sources,
        "relevant_doc_ids": relevant,
        "expected_keywords": [k for k in keywords if k],
        "must_cite": True,
        "expected_sql_entities": {
            "product_id": doc.get("product_id", ""),
            "category": category,
            "doc_type": doc_type,
        },
    }


def _expanded_relevant_doc_ids(doc: dict[str, Any], related: dict[str, dict[str, list[str]]]) -> list[str]:
    own = f"{doc['source']}:{doc['doc_id']}"
    product_id = doc.get("product_id", "")
    category = doc.get("category", "")
    aspect = str(doc.get("metadata", {}).get("aspect", ""))
    by_product = related["by_product"].get(product_id, {}) if product_id else {}
    rating = str(doc.get("metadata", {}).get("rating", ""))
    by_rating = related["by_product_rating"].get(f"{product_id}::{rating}", {}) if product_id and rating else {}
    by_aspect = related["by_category_aspect"].get(f"{category}::{aspect}", {}) if aspect else {}
    by_product_aspect = related["by_product_aspect"].get(f"{product_id}::{aspect}", {}) if product_id and aspect else {}
    relevant = [own]
    doc_type = doc["doc_type"]
    if doc_type == "product_profile":
        relevant.extend(by_product.get("review_aspect_summary", [])[:2])
        relevant.extend(by_product.get("review_evidence", [])[:3])
    elif doc_type == "review_evidence":
        relevant.extend([doc_id for doc_id in by_rating.get("review_evidence", [])[:12] if doc_id != own])
        relevant.extend(by_product.get("product_profile", [])[:1])
        relevant.extend(by_product.get("review_aspect_summary", [])[:2])
    elif doc_type == "review_aspect_summary":
        relevant.extend(by_product_aspect.get("review_evidence", [])[:7])
        relevant.extend(by_product.get("product_profile", [])[:1])
    elif doc_type == "complaint_cluster":
        relevant.extend(by_aspect.get("review_aspect_summary", [])[:4])
        relevant.extend(by_aspect.get("review_evidence", [])[:4])
    elif doc_type == "faq_case":
        aspect_reviews = by_product_aspect.get("review_evidence", [])
        aspect_summaries = by_product_aspect.get("review_aspect_summary", [])
        relevant.extend(aspect_reviews[:3] if aspect_reviews else by_product.get("review_evidence", [])[:2])
        relevant.extend(aspect_summaries[:1] if aspect_summaries else by_product.get("review_aspect_summary", [])[:1])
        relevant.extend(_support_policy_doc_ids(aspect))
    deduped: list[str] = []
    for item in relevant:
        if item and item not in deduped:
            deduped.append(item)
    return deduped[:8]


def _support_policy_doc_ids(aspect: str) -> list[str]:
    if aspect == "delivery":
        return ["kb:KB004_shipping_delivery_policy"]
    if aspect in {"missing_parts"}:
        return ["kb:KB005_missing_parts_policy"]
    if aspect in {"missing_parts", "quality_damage"}:
        return ["kb:KB001_return_refund_policy", "kb:KB005_missing_parts_policy"]
    if aspect in {"refund_return", "price_value"}:
        return ["kb:KB001_return_refund_policy", "kb:KB003_payment_refund_policy"]
    if aspect in {"digital_license"}:
        return ["kb:KB003_payment_refund_policy", "kb:KB004_shipping_delivery_policy"]
    if aspect in {"battery_power"}:
        return ["kb:KB002_warranty_policy"]
    return ["kb:KB001_return_refund_policy"]


def _rag_doc(
    *,
    source: str,
    doc_type: str,
    doc_id: str,
    text: str,
    product_id: str,
    category: str,
    title: str,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    return {
        "source": source,
        "doc_type": doc_type,
        "doc_id": _safe_id(doc_id),
        "product_id": product_id,
        "category": category,
        "title": title,
        "text": normalize_text(text),
        "metadata": metadata,
    }


def _queryable_title(title: str) -> bool:
    tokens = re.findall(r"[a-z0-9]+", normalize_text(title))
    alpha_tokens = [token for token in tokens if re.search(r"[a-z]", token)]
    return len(alpha_tokens) >= 2


def _detect_aspects(text: str) -> set[str]:
    tokens = set(re.findall(r"[a-z0-9]+", normalize_text(text)))
    aspects = {aspect for aspect, keywords in ASPECT_KEYWORDS.items() if tokens & keywords}
    return aspects


def _policy_hint(aspect: str) -> str:
    return {
        "delivery": "shipping and digital delivery policy",
        "refund_return": "return and refund policy",
        "quality_damage": "return and warranty policy",
        "digital_license": "digital delivery and payment policy",
        "battery_power": "warranty policy",
        "missing_parts": "missing parts policy",
    }.get(aspect, "support knowledge base")


def _string_list(value: Any) -> list[str]:
    if isinstance(value, list):
        return [normalize_text(str(item)) for item in value if str(item).strip()]
    if isinstance(value, str) and value.strip():
        return [normalize_text(value)]
    return []


def _fallback_product(product_id: str, category: str) -> dict[str, Any]:
    return {
        "product_id": product_id,
        "sku": product_id,
        "category": category,
        "title": product_id,
        "main_category": category,
        "average_rating": 0.0,
        "rating_number": 0,
        "price": 0.0,
        "store": "",
        "features": [],
        "description": "",
        "details_json": "{}",
    }


def _safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", value)
