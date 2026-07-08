# Tool Registry 重构实现历程

本文记录工具体系从 Agent 内部硬编码升级为 Tool Registry / Tool Planner / Tool Policy / Tool Trace / Tool Eval 的过程，方便后续复盘和面试讲解。

## 背景

重构前，工具逻辑集中在 `CommerceRAGAgent._run_tools()`：

- 解析 SKU / order_id。
- 直接查 SQLite 或 JSONL。
- 组装 `products`、`orders`、`missing_skus`、`missing_order_ids`。
- 为 trace 拼出类似 `sql.product_by_sku`、`sql.order_by_id` 的伪工具调用。

这个实现能跑，但问题是工具不可扩展、权限不可控、评测也只能间接观察。

## 重构目标

目标是把工具能力拆成五层：

```text
Tool Planner
  -> Tool Registry
  -> Tool Policy
  -> Tool Executor
  -> Tool Eval / Tool Trace
```

同时把主链路调整为：

```text
intent/risk/entity
  -> agent plan
  -> tool plan
  -> tool execution
  -> optional memory.semantic_retrieve with tool constraints
  -> structured context filter
  -> generation
  -> citation/tool evidence validation
  -> decision
```

## 已实现模块

新增 `src/commerce_rag_ops/tools/`：

| 文件 | 职责 |
|---|---|
| `base.py` | `ToolSpec`、`ToolCall`、`ToolResult` 基础类型 |
| `registry.py` | `ToolRegistry` 注册和查询 |
| `policy.py` | `ToolPolicy`，包含 domain/action allowlist、隐私边界、写操作确认和退款金额上限 |
| `planner.py` | 规则优先 Tool Planner |
| `executor.py` | ToolPolicy 检查、执行、耗时、evidence id、兼容输出归一化 |
| `product_tools.py` | `sql.product_by_sku`、`sql.product_by_id`、`sql.inventory_by_sku`、`sql.product_search` |
| `order_tools.py` | `sql.order_by_id`、`sql.order_items_by_order_id` |
| `policy_tools.py` | `policy.return_eligibility` |
| `review_tools.py` | `review.aspect_summary` |
| `ticket_tools.py` | `ticket.similar_cases` |
| `escalation_tools.py` | `ops.escalate_ticket`、`ops.refund_request_draft`，写操作默认 requires confirmation |

## Tool-first / Memory-on-demand

重构前：

```text
retrieve -> tool -> filter -> generate
```

重构后：

```text
agent_plan -> tool_plan -> tool_exec -> optional memory.semantic_retrieve -> filter -> generate
```

例如订单问题：

```text
Check order ORD-1003 status and delivery context.
```

系统先调用：

```text
sql.order_by_id({"order_id": "ORD-1003"})
sql.order_items_by_order_id({"order_id": "ORD-1003"})
```

如果 Agent plan 判断还需要政策、商品、评论或工单证据，再把工具确认的 `order_id/product_id/sku` 拼入 `memory.semantic_retrieve` query，降低相似商品或相似订单污染。若只是明确订单状态查询，结构化工具足够时可以跳过 RAG。当前 seed 数据是一单一商品，`order_items` 表会从订单自动派生；如果后续接入一单多商品，只需要写入多行 `order_items`。

## Tool Policy

当前策略：

- `allowed_domains`：Agent-first 主路径下，工具可被哪些 DomainAgent 调用，例如 `support`、`order`、`customer_ops`。
- `allowed_intents`：兼容旧评测/CLI 的 legacy 字段；当没有 domain 上下文时作为 fallback。
- `action_type`：只有 `tool_call` 可以进入 ToolExecutor，避免非工具 step 被伪装执行。
- `risk_level`：高风险写操作必须用户确认。
- `requires_confirmation`：写操作默认不执行。
- `redact_fields`：例如 `sql.order_by_id` 会脱敏 `customer_id`。
- 隐私边界：`all orders`、`payment details`、`address`、`emails` 等触发工具层阻断。

`ops.escalate_ticket` 和 `ops.refund_request_draft` 已注册为写工具，但不会直接创建工单或批准退款，只返回 `requires_confirmation` 草稿。若退款类工具输入金额超过当前 demo 阈值 `100.0`，ToolPolicy 会直接返回 `blocked/refund_amount_exceeds_limit`。

## Tool Trace

Agent trace 新增：

- `tool.plan` span：记录计划调用哪些工具及 reason。
- `policy.check` span：挂在每个 `domain_agent.step` 下，记录 domain、action、risk、allowed domains、policy decision 和阻断原因。
- `tools.execute` span：记录每个工具调用、输入、输出 preview、policy decision、found、latency、evidence id。
- `tool_use` 兼容事件：保留 `summary` 和 `tool_calls`，供旧报告/接口读取。

`state.tool_results` 仍保持兼容：

- `products`
- `context_inferred_products`
- `orders`
- `order_items`
- `inventory`
- `return_eligibility`
- `review_summaries`
- `similar_cases`
- `tool_calls`
- `missing_skus`
- `missing_order_ids`

## Tool Eval

新增：

- `data/eval/tool_golden.jsonl`
- `src/commerce_rag_ops/tool_eval.py`
- `reports/tool_eval_report.md`
- CLI：`python -m commerce_rag_ops.cli tool-eval --reranker-model none`

当前指标：

- `tool_call_precision`
- `tool_call_recall`
- `missing_required_tool_rate`
- `forbidden_tool_call_rate`
- `structured_fact_accuracy`
- `tool_grounded_answer_rate`
- `unknown_entity_refusal_rate`
- `write_tool_confirmation_rate`
- `pass_rate`

当前 smoke 结果：

| 指标 | 值 |
|---|---:|
| 样本数 | 7 |
| Tool call recall | 1.0 |
| Missing required tool rate | 0.0 |
| Forbidden tool call rate | 0.0 |
| Structured fact accuracy | 1.0 |
| Tool grounded answer rate | 1.0 |
| Unknown entity refusal rate | 1.0 |
| Write tool confirmation rate | 1.0 |
| Pass rate | 1.0 |

`tool_call_precision` 低于 1.0 是因为 planner 会额外调用 `sql.product_search`、`ticket.similar_cases` 等低风险上下文工具，用于提高证据覆盖；这属于 recall-oriented planning，不是 forbidden call。

## Tool-first 与检索推断的边界

显式 SKU/订单必须由工具确认；如果 `missing_skus` 或 `missing_order_ids` 非空，系统 retry 后仍会拒答，不借相似商品硬答。

但在多轮 follow-up 或 fallback stress 中，用户可能只说 “matched item” 这类无显式实体 query。此时如果检索结果里只有一个商品画像上下文，Agent 会：

- 从该商品画像读取唯一 `product_id`。
- 回查本地商品表补齐 SKU、价格、库存等结构化字段。
- 写入 `tool_results.context_inferred_products` 和兼容的 `tool_results.products`。
- 在 event trace 中记录 `structured_entity_infer`，说明这是 `retrieved_product_context` 推断，而不是用户显式实体或工具命中。

这个分支只服务“无显式实体但上下文唯一”的恢复场景，不影响 unknown SKU / unknown order 的拒答边界。

## 工具引用与验证

工具调用成功后会生成 `evidence_id`，例如：

```text
[tool:sql.order_by_id:ORD-1003]
[tool:sql.order_items_by_order_id:ORD-1003]
[tool:policy.return_eligibility:ORD-1001]
```

Agent 在生成前把这些 ID 写入 `state.tool_citations`，模板生成器会把结构化事实和 `[tool:...]` marker 一起写入答案。真实 LLM prompt 也会收到 `tool_citations`，并被要求在结构化事实声明中使用这些 marker。

生成后新增 `tool_citation.validate` span，检查：

- answer-side `[tool:...]` 语法是否正确；
- marker 是否来自本轮成功工具调用；
- 需要工具证据的回答是否遗漏工具 marker；
- precision/recall 形式的答案侧工具引用覆盖。

这样可以把结构化事实来源和 RAG 文档来源分开：价格/库存/订单状态/退货资格看 `[tool:...]`，政策/评论/工单解释看 `[doc:...]`。

## Tool Dashboard / CLI

浏览器 dashboard 的 Tool Trace 面板已经拆成：

- Tool Plan：工具名、reason、required/optional、输入；
- Tool Calls：found、policy decision、latency、evidence_id；
- Retrieval Constraints：工具反向约束出的 product_id / sku / order_id；
- Context Inference：唯一商品上下文推断出的 product。

CLI 也新增：

```powershell
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db tools <trace_id>
```

用于直接查看 `tool.plan`、`tools.execute` 和 `tool_citation.validate` span。

## 面试讲法

可以这样说：

> 我把原来写在 Agent 内部的 SKU/订单查询拆成了 Tool Registry。每个工具都有 ToolSpec，声明输入输出、风险等级、只读/写操作、是否需要确认、allowed domains、legacy allowed intents 和脱敏字段。Agent 不再直接查 SQL，而是由 ToolSuggester 提供候选，DomainAgent.next_step 选择下一步 ToolCall，再经过 ToolPolicy 按 domain/action/risk/confirmation 检查并落 `policy.check` span，最后由 ToolExecutor 执行并生成 structured evidence。工具结果反过来约束 RAG 检索 query，避免相似 SKU/订单污染。回答里结构化事实会带 `[tool:...]` citation，并由 `tool_citation.validate` 检查。最后用 tool golden eval 单独评测工具调用 recall、禁用工具调用、结构化事实准确率、工具 grounded answer、写工具确认和未知实体拒答。

## 当前边界

- `policy.return_eligibility` 目前是 demo 级规则工具，不是完整售后规则引擎。
- 当前 seed 订单是一单一商品；`order_items` schema 和工具已支持多行，后续只需要补多商品订单数据。
- Tool citation 已支持答案侧 `[tool:...]` marker 和 deterministic validator；真实 LLM 仍可能漏引，因此评测会单独统计 tool grounded answer rate。
- Dashboard 已有 Tool Plan/Calls/Constraints 面板，但还不是独立的企业级观测系统。
- 写操作注册了 `ops.escalate_ticket` 和 `ops.refund_request_draft` 的确认占位，没有真正创建工单或批准退款；大额退款建议会被策略阻断。

## P0-P5 完成对照

| 阶段 | 计划要求 | 当前状态 | 证据 |
|---|---|---|---|
| P0 | 拆出 `ToolSpec` / `ToolRegistry` / product & order tools，保持 `tool_results` 兼容 | 已完成 | `src/commerce_rag_ops/tools/base.py`, `registry.py`, `product_tools.py`, `order_tools.py`, `agent.py` |
| P1 | 补 `product_by_id`、`inventory_by_sku`、`ticket.similar_cases`、`review.aspect_summary`、`policy.return_eligibility` | 已完成，并额外补了 `sql.order_items_by_order_id` | `src/commerce_rag_ops/tools/*.py`, `tests/test_core.py::test_tool_registry_planner_policy_and_eval` |
| P2 | 主链路改为 `route -> risk -> tool_plan -> tool_exec -> retrieval` | 已完成 | `CommerceRAGAgent.run`, `reports/end_to_end_trace_sample.json` |
| P3 | Tool Policy、PII redaction、allowed domains、legacy allowed intents、requires confirmation | 已完成；本地单租户 demo 未实现 tenant scope | `src/commerce_rag_ops/tools/policy.py`, `order_tools.py`, `escalation_tools.py` |
| P4 | 工具 evidence id、工具 citation、工具 citation validator | 已完成 | `src/commerce_rag_ops/citation_quality.py`, `agent.py`, `generator.py` |
| P5 | Tool trace panel、tool eval、tool golden、tool eval report | 已完成 | `web/index.html`, `src/commerce_rag_ops/tool_eval.py`, `data/eval/tool_golden.jsonl`, `reports/tool_eval_report.md` |

最后验证快照：

- `pytest -q`：31 passed
- `fallback-stress`：7/7 passed
- `tool-eval --reranker-model none`：7/7 passed
- 敏感信息扫描：无命中
