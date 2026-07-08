from __future__ import annotations

from typing import Any

from ..models import Product
from ..sql_store import SQLStore
from ..text import tokenize
from .base import ToolSpec


def register_product_tools(registry, *, sql_store: SQLStore | None, products: dict[str, Product], products_by_sku: dict[str, Product]) -> None:
    def product_by_sku(payload: dict[str, Any]) -> dict[str, Any]:
        sku = str(payload.get("sku", "")).strip()
        product = sql_store.product_by_sku(sku) if sql_store else products_by_sku.get(sku.lower())
        return {"found": product is not None, **(_product_payload(product) if product else {})}

    def product_by_id(payload: dict[str, Any]) -> dict[str, Any]:
        product_id = str(payload.get("product_id", "")).strip()
        product = sql_store.product_by_id(product_id) if sql_store else products.get(product_id)
        return {"found": product is not None, **(_product_payload(product) if product else {})}

    def inventory_by_sku(payload: dict[str, Any]) -> dict[str, Any]:
        sku = str(payload.get("sku", "")).strip()
        product = sql_store.product_by_sku(sku) if sql_store else products_by_sku.get(sku.lower())
        if not product:
            return {"found": False, "sku": sku, "available": False, "inventory_status": "unknown"}
        return {
            "found": True,
            "sku": product.sku,
            "stock": product.stock,
            "available": product.stock > 0,
            "inventory_status": "in_stock" if product.stock > 0 else "out_of_stock",
        }

    def product_search(payload: dict[str, Any]) -> dict[str, Any]:
        query = str(payload.get("query", "")).strip()
        category = str(payload.get("category", "")).strip()
        query_tokens = set(tokenize(query))
        matches = []
        for product in products.values():
            if category and product.category != category:
                continue
            product_tokens = set(tokenize(" ".join([product.title, product.description, " ".join(product.features)])))
            score = len(query_tokens & product_tokens)
            if score:
                matches.append((score, product))
        matches.sort(key=lambda item: (item[0], item[1].average_rating), reverse=True)
        return {
            "found": bool(matches),
            "products": [_product_payload(product) for _, product in matches[: int(payload.get("top_k", 4))]],
        }

    registry.register(
        ToolSpec(
            name="sql.product_by_sku",
            description="Look up a product by SKU.",
            input_schema={"type": "object", "required": ["sku"]},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="low",
            requires_confirmation=False,
            handler=product_by_sku,
            allowed_intents=["sku_order", "support", "recommendation", "customer_ops"],
            allowed_domains=["order", "support", "recommendation", "customer_ops"],
        )
    )
    registry.register(
        ToolSpec(
            name="sql.product_by_id",
            description="Look up a product by product_id.",
            input_schema={"type": "object", "required": ["product_id"]},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="low",
            requires_confirmation=False,
            handler=product_by_id,
            allowed_intents=["sku_order", "support", "recommendation", "customer_ops"],
            allowed_domains=["order", "support", "recommendation", "customer_ops"],
        )
    )
    registry.register(
        ToolSpec(
            name="sql.inventory_by_sku",
            description="Look up inventory availability by SKU.",
            input_schema={"type": "object", "required": ["sku"]},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="low",
            requires_confirmation=False,
            handler=inventory_by_sku,
            allowed_intents=["sku_order", "support", "recommendation"],
            allowed_domains=["order", "support", "recommendation"],
        )
    )
    registry.register(
        ToolSpec(
            name="sql.product_search",
            description="Search seed products by query terms and optional category.",
            input_schema={"type": "object"},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="low",
            requires_confirmation=False,
            handler=product_search,
            allowed_intents=["recommendation", "support", "customer_ops"],
            allowed_domains=["recommendation", "support", "customer_ops"],
            max_rows=4,
        )
    )


def _product_payload(product: Product | None) -> dict[str, Any]:
    if not product:
        return {}
    return {
        "product_id": product.product_id,
        "sku": product.sku,
        "title": product.title,
        "category": product.category,
        "price": product.price,
        "stock": product.stock,
        "average_rating": product.average_rating,
        "rating_number": product.rating_number,
    }
