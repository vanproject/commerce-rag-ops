# Fallback 压力测试报告

本报告通过脚本化检索失败来验证关键 Agentic fallback 行为。
该流程不会修改或重新打分 `data/eval/golden.jsonl`。

- 用例数: 7
- 是否通过: True
- 触发重试用例数: 7
- 最终回答用例数: 4
- 最终拒答用例数: 3

| 用例 | 意图 | 预期缺口 | 首轮缺口 | 最终缺口 | 尝试次数 | 预期动作 | 实际动作 | 引用数 | 状态 |
|---|---|---|---|---|---:|---|---|---:|---|
| FS-001 | recommendation | missing_review | missing_review | none | 2 | answer | answer | 2 | PASS |
| FS-002 | support | missing_policy | missing_policy | none | 2 | answer | answer | 2 | PASS |
| FS-003 | customer_ops | missing_customer_voice | missing_customer_voice | none | 2 | answer | answer | 2 | PASS |
| FS-004 | sku_order | missing_product_context | missing_structured_entity, missing_product_context | none | 2 | answer | answer | 2 | PASS |
| FS-005 | sku_order | missing_structured_entity | missing_structured_entity, missing_product_context | missing_structured_entity, missing_product_context | 2 | refuse | refuse | 0 | PASS |
| FS-006 | sku_order | missing_structured_entity | missing_structured_entity, missing_product_context | missing_structured_entity, missing_product_context | 2 | refuse | refuse | 0 | PASS |
| FS-007 | support | no_context | insufficient_context, no_context | insufficient_context, no_context | 2 | refuse | refuse | 0 | PASS |

## 原始用例

### FS-001

- Query: Recommend a baby monitor with good night vision reviews
- 预期关键缺口: `missing_review`
- 预期动作: `answer`
- 首轮缺口: `missing_review`
- 最终缺口: `none`

### FS-002

- Query: My serum arrived broken. Can I get a refund?
- 预期关键缺口: `missing_policy`
- 预期动作: `answer`
- 首轮缺口: `missing_policy`
- 最终缺口: `none`

### FS-003

- Query: What customer ops issues appear in baby product complaints?
- 预期关键缺口: `missing_customer_voice`
- 预期动作: `answer`
- 首轮缺口: `missing_customer_voice`
- 最终缺口: `none`

### FS-004

- Query: Check inventory status for the matched item.
- 预期关键缺口: `missing_product_context`
- 预期动作: `answer`
- 首轮缺口: `missing_structured_entity, missing_product_context`
- 最终缺口: `none`

### FS-005

- Query: Check SKU TEMP-404 inventory status.
- 预期关键缺口: `missing_structured_entity`
- 预期动作: `refuse`
- 首轮缺口: `missing_structured_entity, missing_product_context`
- 最终缺口: `missing_structured_entity, missing_product_context`

### FS-006

- Query: Check order ORD-404 status.
- 预期关键缺口: `missing_structured_entity`
- 预期动作: `refuse`
- 首轮缺口: `missing_structured_entity, missing_product_context`
- 最终缺口: `missing_structured_entity, missing_product_context`

### FS-007

- Query: Can I get a refund for an unknown discontinued item with no order details?
- 预期关键缺口: `no_context`
- 预期动作: `refuse`
- 首轮缺口: `insufficient_context, no_context`
- 最终缺口: `insufficient_context, no_context`
