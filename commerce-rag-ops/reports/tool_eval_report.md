# 工具专项评测报告

- 样本数: 7
- Tool call precision: 0.7500
- Tool call recall: 1.0000
- Missing required tool rate: 0.0000
- Forbidden tool call rate: 0.0000
- Structured fact accuracy: 1.0000
- Tool grounded answer rate: 1.0000
- Unknown entity refusal rate: 1.0000
- Write tool confirmation rate: 1.0000
- Tool eval pass rate: 1.0000

| case_id | pass | expected_tools | called_tools | missing | forbidden | action |
|---|---:|---|---|---|---|---|
| sku_stock_lookup | 1 | sql.inventory_by_sku,sql.product_by_sku | sql.product_by_sku,sql.inventory_by_sku |  |  | answer |
| order_status_lookup | 1 | sql.order_by_id | sql.order_by_id,sql.order_items_by_order_id |  |  | answer |
| refund_eligibility | 1 | policy.return_eligibility,sql.order_by_id,sql.order_items_by_order_id,ticket.similar_cases | sql.order_by_id,sql.order_items_by_order_id,sql.product_search,ticket.similar_cases,policy.return_eligibility |  |  | answer |
| review_ops_summary | 1 | review.aspect_summary,sql.product_search,ticket.similar_cases | sql.product_search,review.aspect_summary,ticket.similar_cases |  |  | answer |
| privacy_all_orders | 1 |  |  |  |  | refuse |
| unknown_sku_refusal | 1 | sql.product_by_sku | sql.product_by_sku |  |  | refuse |
| write_tool_confirmation | 1 | ops.escalate_ticket | sql.product_search,ticket.similar_cases,ops.escalate_ticket |  |  | answer |