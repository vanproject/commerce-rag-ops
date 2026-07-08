from __future__ import annotations

from typing import Any

from ..models import Order
from ..sql_store import SQLStore
from .base import ToolSpec


def register_order_tools(registry, *, sql_store: SQLStore | None, orders: dict[str, Order]) -> None:
    def order_by_id(payload: dict[str, Any]) -> dict[str, Any]:
        order_id = str(payload.get("order_id", "")).strip()
        order = sql_store.order_by_id(order_id) if sql_store else orders.get(order_id.lower())
        return {"found": order is not None, **(_order_payload(order) if order else {})}

    def order_items_by_order_id(payload: dict[str, Any]) -> dict[str, Any]:
        order_id = str(payload.get("order_id", "")).strip()
        if sql_store:
            items = sql_store.order_items_by_order_id(order_id)
        else:
            order = orders.get(order_id.lower())
            items = [_order_item_payload(order)] if order else []
        return {"found": bool(items), "order_id": order_id.upper(), "items": items}

    registry.register(
        ToolSpec(
            name="sql.order_by_id",
            description="Look up a single order by order_id.",
            input_schema={"type": "object", "required": ["order_id"]},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="medium",
            requires_confirmation=False,
            handler=order_by_id,
            allowed_intents=["sku_order", "support"],
            allowed_domains=["order", "support"],
            max_rows=1,
            redact_fields=["customer_id"],
        )
    )
    registry.register(
        ToolSpec(
            name="sql.order_items_by_order_id",
            description="Look up item-level lines for a single order.",
            input_schema={"type": "object", "required": ["order_id"]},
            output_schema={"type": "object"},
            read_only=True,
            risk_level="medium",
            requires_confirmation=False,
            handler=order_items_by_order_id,
            allowed_intents=["sku_order", "support"],
            allowed_domains=["order", "support"],
            max_rows=20,
        )
    )


def _order_payload(order: Order | None) -> dict[str, Any]:
    if not order:
        return {}
    return {
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "product_id": order.product_id,
        "sku": order.sku,
        "status": order.status,
        "delivery_status": order.delivery_status,
        "order_date": order.order_date,
        "total": order.total,
    }


def _order_item_payload(order: Order | None) -> dict[str, Any]:
    if not order:
        return {}
    return {
        "order_id": order.order_id,
        "product_id": order.product_id,
        "sku": order.sku,
        "quantity": 1,
        "unit_price": order.total,
        "line_total": order.total,
    }
