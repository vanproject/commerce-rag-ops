# Conversation Memory 与 Entity Memory 设计

本文记录多轮记忆系统的实现思路。目标不是做长期用户画像，而是在同一个 `conversation_id` 内支持安全、可解释的上下文续接。

## 设计边界

本项目采用 conversation-scoped memory：

- 只记最近若干轮 conversation turns。
- 只记安全业务实体：`sku`、`order_id`、`product_id`、`category`、`support_topic`。
- 不记邮箱、电话、地址、支付信息、全量订单、客户隐私字段。
- SKU/订单即使从记忆继承，也必须在下一轮通过 SQL/工具再次确认。
- 完整 trace 仍走 TraceStore；记忆层不保存完整 AgentState 和内部调试大对象。

## ConversationStore

新增 `src/commerce_rag_ops/conversation_store.py`，使用 SQLite：

- `conversations`：conversation 元数据。
- `conversation_turns`：最近用户/助手轮次、resolved query、intent、action、citations、脱敏 tool summary。
- `conversation_entities`：conversation 作用域内的安全实体。

默认本地库路径建议为 `reports/conversations.db`，已通过 `.gitignore` 排除。

## ContextResolver

新增 `src/commerce_rag_ops/memory/context_resolver.py`。`src/commerce_rag_ops/entity_memory.py` 仍保留 `EntityResolver` 兼容包装和实体抽取函数，但主路径已经使用 `ContextResolution`，不再把历史实体拼成自然语言 query suffix。

实体来源分三层：

| 来源 | 可信度 | 说明 |
|---|---:|---|
| 用户 query | 中 | 用规则抽 SKU/order_id/support topic |
| SQL tool_results | 高 | 工具确认过的 SKU、order_id、product_id |
| retrieved_contexts/citations | 低 | 用于检索续接，不作为强事实承诺 |

实体继承规则：

- 如果当前 query 显式出现 SKU/order，显式实体优先，不使用历史实体。
- 如果 query 出现 `it`、`that`、`that product`、`that order`、`刚才那个`、`这个订单` 等指代词，才尝试继承。
- refund/status/delivery/order 类 follow-up 优先继承 `order_id`。
- review/complaint/feedback/product 类 follow-up 优先继承 `product_id` 或 `sku`。
- 如果历史里存在多个 active product/SKU/order，标记 ambiguous，不强行选择。
- 如果 query 命中隐私边界，阻止实体继承，也不写入实体记忆。

## Agent 接入

`CommerceRAGAgent.run()` 新增 `memory_context`，调用方传入原始 query 和结构化解析结果：

```python
agent.run(
    query,
    max_retries=1,
    memory_context={
        "conversation_id": "...",
        "recent_turns": [...],
        "active_entities": {...},
        "context_resolution": {
            "original_query": "Can I get a refund for that?",
            "is_followup": True,
            "referenced_entities": [
                {
                    "entity_type": "order_id",
                    "entity_value": "ORD-1003",
                    "source": "entity_memory",
                    "confidence": 0.92,
                    "requires_tool_confirmation": True
                }
            ],
            "resolution_source": "memory"
        },
        "entity_resolution": {...},  # deprecated compatibility mirror
    },
)
```

`AgentState` 新增：

- `original_query`
- `memory_context`
- `resolved_entities`

Trace 新增：

- `memory_load`
- `entity_resolve`
- `entity_update`

LLM prompt 中加入轻量 `memory_context`，只包含 conversation id、active entities、resolved entities 和 recent turn count，不拼接完整历史。

## API/CLI 行为

HTTP `/ask` 支持：

```json
{
  "query": "Can I get a refund for that?",
  "conversation_id": "optional",
  "user_id": "optional",
  "max_retries": 1
}
```

返回增加：

- `conversation_id`
- `context_resolution`
- `resolved_query`：兼容字段，当前等于原始 query，不再承载自然语言拼接结果。
- `memory_used`

CLI 可选开启 memory：

```powershell
python -m commerce_rag_ops.cli ask "Check order ORD-1003 status." `
  --generator template `
  --reranker-model none `
  --conversation-db reports/conversations.db `
  --conversation-id demo-1

python -m commerce_rag_ops.cli ask "Can I get a refund for that?" `
  --generator template `
  --reranker-model none `
  --conversation-db reports/conversations.db `
  --conversation-id demo-1
```

## 多轮评测

新增评测集：

- `data/eval/multiturn_memory.jsonl`

新增命令：

```powershell
python -m commerce_rag_ops.cli memory-eval --reranker-model none
```

指标：

- `entity_carryover_accuracy`
- `wrong_entity_leak_rate`
- `clarification_rate_when_ambiguous`
- `privacy_memory_block_rate`
- `multi_turn_answer_success_rate`

当前 smoke 结果见 `reports/memory_eval_report.md`。

## 面试讲法

可以这样说：

> 我没有把历史对话直接全塞进 prompt，也没有把实体拼到 query 后面，而是做了 conversation-scoped memory。系统保存最近 turns 和经过白名单过滤的业务实体，再由 ContextResolver 产出结构化 ContextResolution。只有出现 it/that/刚才那个 等指代时才继承实体；如果用户显式给了新 SKU/订单，新实体覆盖旧实体；如果历史有多个候选，就不强行选择。订单和 SKU 每轮仍然要走 SQL 工具确认，所以记忆只提供结构化 reference，不替代事实源。

## 当前边界

- 目前没有长期用户画像和跨 conversation 记忆。
- 目前没有自动生成长期 conversation summary，只保存 recent turns 和安全实体。
- 歧义场景现在通过 blocked reason 标记，生成层还没有专门输出“请明确产品”的模板。
- PII 过滤是规则式，生产环境需要更强的脱敏/合规审计。
