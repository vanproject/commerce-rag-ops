# 多路加权意图识别与端到端 Trace 设计

本文记录本轮实现思路，用于后续面试复盘和代码走查。目标是把原先较单调的规则路由升级为可解释的多路加权识别，同时让一次 Agent 运行从输入到最终动作都有完整 trace。

## 背景问题

旧版 `_route_intent` 是顺序 if/else：

- 命中 customer ops 短语就返回 `customer_ops`。
- 命中 SKU/order 就返回 `sku_order`。
- 命中 recommend/best/compare 就返回 `recommendation`。
- 命中 refund/return/shipping 等就返回 `support`。
- 其他返回 `unknown`。

这种方式可复现，但面试时不够像真实业务路由：一个 query 常常同时包含“推荐”“价格”“配送”“客服处理”等多种信号，顺序规则无法解释为什么某一路由最终胜出，也无法把冲突信号留在 trace 里。

## 新方案：多路加权识别

新实现把 weighted routing 迁入 `RootRouterAgent.decide_intent()`，`CommerceRAGAgent._route_intent_decision()` 仅作为兼容 wrapper，输出：

- `intent`：最终意图。
- `confidence`：胜出 intent 分数占正分总和的比例。
- `scores`：五类 intent 的得分，包含 `support`、`recommendation`、`customer_ops`、`sku_order`、`unknown`。
- `signals`：每条命中的信号，包含 `intent`、`weight`、`source`、`reason`。

当前信号来源：

| source | 说明 | 示例 |
|---|---|---|
| `structured_entity` | 显式 SKU 或订单号 | `SOFT-PDF-01`, `ORD-1003` |
| `entity_keyword` | SKU、库存、价格等结构化查询词 | `sku`, `stock`, `inventory`, `price` |
| `order_status` | 订单状态/配送追踪 | `order status`, `delivery status` |
| `lexical_phrase` | 业务短语 | `recommend`, `complaint trend`, `negative review` |
| `support_keyword` | 售后支持词 | `refund`, `return`, `warranty`, `delivery` |
| `support_workflow` | 客服处理流程问法 | `how should support handle` |
| `category_hint` | 类目提示 | beauty/software/baby |
| `safety_boundary` | 隐私、越权、提示注入边界 | `all orders`, `api key`, `system prompt` |
| `safety_domain` | 非电商域外问题 | `stock price`, `share price` |
| `default` | 无明显业务信号 | no intent signal |

选择规则是“最高分胜出 + tie-breaker”。Tie-breaker 只在分数相同的时候使用，优先级为：

`sku_order > customer_ops > recommendation > support > unknown`

这个优先级符合当前业务边界：显式 SKU/订单是强结构化事实，应该优先进入工具确认；客户运营和推荐/客服的冲突主要由权重决定。

## Trace v3：事件兼容 + Span Trace

Agent 运行时现在同时保留两套结构：

- `trace`：兼容旧评测/API 的轻量事件列表。
- `trace_run`、`trace_spans`、`trace_artifacts`、`retrieval_candidates`：新的可观测 span trace。

`trace_run` 记录一次请求的全局信息，包括 `trace_id`、query、normalized query、intent、risk、最终 action、answer、citations、latency、attempts、config、dataset manifest 和 git sha。这样复盘坏 case 时能知道当时用的是哪个 retriever/generator/reranker、哪个 chunks 文件和哪版代码。

`trace_spans` 是父子结构：

```text
agent.run
├─ intent.route
├─ risk.classify
├─ memory.source_defaults      # 语义记忆工具的默认 sources；不代表本轮一定检索
├─ agent.plan
├─ plan.validate
├─ tool.plan
├─ tools.execute
├─ domain_agent.step
│  ├─ policy.check
│  └─ memory.semantic_retrieve    # 仅当 agent.plan 需要长期语义记忆时出现
│     └─ retrieval.attempt_1      # semantic memory 内部的兼容检索 span
│        ├─ query_analysis
│        ├─ dense.search
│        ├─ bm25.search
│        ├─ rrf.fusion
│        ├─ forced_candidates
│        ├─ heuristic_rerank
│        └─ diversify
├─ context.structured_filter
├─ answer.generate
│  └─ generation.llm
└─ critic.evaluate_answer
   ├─ citation.validate
   ├─ tool_citation.validate
   ├─ grader.score
   ├─ evidence_pack.build
   ├─ critic.verify
   ├─ replanner.plan
   └─ decision
```

`trace_artifacts` 用于保存大对象摘要，例如 generation context、retrieval candidates、citation validation。默认保存 hash、preview 和 metadata，不把无限长 prompt/chunk 全塞进 span。

`retrieval_candidates` 是专门的检索候选表，字段包括 source、doc_id、chunk_id、doc_type、dense/BM25/RRF/final rank、dense/BM25/RRF/rerank score、forced、forced_reason、selected、dropped_reason、content_hash 和 preview。它用来解释“为什么某个 chunk 被召回但没有进最终上下文”。

旧事件列表仍然存在：

| event | 阶段 | 关键字段 |
|---|---|---|
| `run_start` | 运行开始 | query、max_retries |
| `intent_route` | 多路意图识别 | intent、risk_level、confidence、scores、signals |
| `memory_source_defaults` | 语义记忆默认源 | intent、sources、reason；仅作为 memory tool 默认参数 |
| `attempt_start` | 每轮尝试开始 | attempt、effective_query、memory_source_defaults、previous_evidence_gaps |
| `agent_plan` | Agent 执行计划 | actions、memory_request、accepted/rejected step |
| `memory_semantic_retrieve` | 长期语义记忆读取 | memory_type、doc citations、diagnostics、top_contexts |
| `memory_skip` | 跳过语义记忆 | reason |
| `retrieve` | 兼容检索事件，仅 semantic memory 被调用时出现 | latency_ms、diagnostic_stages、candidate_count、top_contexts |
| `tool_use` | SQL/结构化工具 | latency_ms、summary、tool_calls |
| `structured_context_filter` | 结构化实体收敛 | product_ids、removed、removed_contexts、remaining |
| `context_filter` | 通用上下文过滤结果 | before、after、removed |
| `generate` | 生成回答 | generator、latency_ms、citations、answer_preview、prompt_artifact_id |
| `action_decision` | 动作决策 | action、decision_reason、evidence_gaps、next_query、next_sources |
| `refusal_generate` | 拒答生成 | answer_preview、latency_ms |
| `grade` | 本轮评分 | grader scores、evidence_gaps、citation_validation、tool citation scores、attempt_latency_ms |
| `finish` | 运行结束 | trace_schema_version、latency_ms、attempts、final_action、span_count、artifact_count、retrieval_candidate_count |

## SQLite 查询存储

除了 `--trace-store` JSONL，CLI 新增 `--trace-db`，会把 span trace 写入 SQLite：

```powershell
python -m commerce_rag_ops.cli ask "Check SKU SOFT-PDF-01 price and delivery context." `
  --generator template `
  --reranker-model none `
  --trace-out reports/end_to_end_trace_sample.json `
  --trace-db reports/traces.db
```

查询命令：

```powershell
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db list --limit 20
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db show <trace_id>
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db tree <trace_id>
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db tools <trace_id>
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db candidates <trace_id> --attempt 1
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db failures --intent support --limit 50
```

SQLite 表：

- `trace_runs`
- `trace_spans`
- `retrieval_candidates`
- `trace_artifacts`
- `trace_steps`
- `trace_observations`
- `trace_evidence`
- `trace_verifications`

其中 `trace_steps` 来自 `runtime_state.steps`，`trace_observations` 来自工具/检索 observations，`trace_evidence` 来自 EvidencePack，`trace_verifications` 来自 CriticVerifier。这样不只可以看 span tree，也能直接 SQL 查询 Agent 执行了哪些动作、拿到了哪些证据、最终 critic 为什么通过或拒答。

## 面试讲法

可以这样解释：

> 我没有把 intent routing 做成一个黑盒 LLM 分类器，而是先实现了可解释的加权路由。每条 query 会同时命中结构化实体、业务短语、类目、风险边界等多路信号，系统保留每路分数和 reason。这样面试或排障时能直接看到“为什么这条从 recommendation 转成 sku_order”，也方便后续替换成 learned classifier 或 LLM router。

Trace 的讲法：

> Trace v3 不是只记录最终 answer，而是覆盖 route、agent planning、tool、semantic memory、filter、generate、critic evaluation、retry/refuse 和 finish。每轮 attempt 都能看到 effective query、证据缺口、工具命中、是否调用长期语义记忆和最终动作，因此可以解释 fallback 为什么发生、拒答是不是因为证据不足。

升级后的讲法：

> 我把 trace 从 list event 升级成了 span tree 和结构化 SQLite 表。一次请求有 trace_run，下面是 intent.route、agent.plan、plan.validate、tool.plan、tools.execute、domain_agent.step、answer.generate、generation.llm、critic.evaluate_answer 等 span；每个工具 step 下都有 `policy.check`，semantic memory step 下还有 memory.semantic_retrieve 和 retrieval.attempt_* 诊断；generation.llm 挂在 answer.generate 下，generation_context artifact 只记录 EvidencePack 派生上下文；SQLite 里还会落 trace_steps、trace_observations、trace_evidence、trace_verifications，能直接查每个 Agent step、observation、证据和 critic 结论；citation.validate、tool_citation.validate、grader.score、critic.verify、replanner.plan 和 decision 作为 Critic 子检查保留兼容。只有调用长期语义记忆时才会落 retrieval_candidates 表，记录 dense/BM25/RRF/rerank/final rank 和 forced/dropped 原因。这样排查坏 case 时，不只能看到最后答案，还能解释每个证据为什么被加入、丢弃、跳过或引用。

## 当前边界

- 这仍然是 deterministic weighted router，不是训练好的意图分类模型。
- `confidence` 是路由内部得分占比，不是统计校准后的概率。
- Trace 已支持 JSON、JSONL、SQLite 查询存储和浏览器 dashboard；dashboard 目前是本地演示版，不是多用户观测平台。
- Qdrant trace 当前记录最终候选和基础阶段信息；本地 HybridRetriever trace 记录 dense/BM25/RRF/forced/rerank/diversify 的完整候选诊断。
- LLM 生成 trace 保存 generation context 的 hash/preview；HTTP retry 的每次底层请求还没有拆成 child span。
- 尚未接入 LangSmith、OpenTelemetry 或 MLflow。
- 后续可以把当前 `signals` 作为特征，叠加少量人工标注 query 做校准分类器，或者引入 LLM router 作为候选信号之一。
