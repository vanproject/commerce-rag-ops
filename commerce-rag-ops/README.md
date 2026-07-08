# CommerceRAG Ops

面向电商客服、商品推荐和客户运营的 **评测优先 Agent-first 项目**。

这个仓库实现了一个可以本地运行、适合简历和面试展示的电商 Agent 系统。RAG 不是主流程本身，而是长期语义记忆的一种实现，和 SQL 结构化工具、会话记忆、实体记忆、人工升级/退款草稿工具并列，由 Agent 在需要时调用。项目分成两档运行方式：测试档可完全离线复现，生产/面试档使用本地 GPU embedding、CrossEncoder reranker 和真实 OpenAI-compatible LLM API，展示完整工程闭环：

- 多格式文档抽取：Markdown、HTML、TXT、CSV、可选 PDF 文本、OCR 图片附件。
- 数据清洗、去重、空文本过滤、按文档类型切片，并生成稳定 chunk id。
- Amazon Reviews 2023 规模子集构建：抽样 15,000 条公开评论，关联 3,000 条商品元数据，生成多粒度 RAG 文档。
- 可插拔 Qdrant/Embedding：测试可用确定性 hash embedding，生产/面试档默认 `BAAI/bge-large-en-v1.5`。
- SQLite 结构化数据层：商品、评论、工单、订单、客户分群、KB、评测标签、chunks、公开数据 manifest。
- 长期语义记忆：BGE dense retrieval、BM25、RRF 融合、`BAAI/bge-reranker-large` CrossEncoder rerank，封装为 `memory.semantic_retrieve`。
- Agent-first：RootRouterAgent、DomainAgent 执行计划、ReAct-style AgentLoop、LLM advisor、工具调用、按需语义记忆、EvidencePack、CriticVerifier、Replanner、fallback retry、拒答控制、引用输出。
- Tool Registry：商品、订单、库存、退货资格、评论摘要、相似工单、人工升级工具，带 Tool Policy 和专项评测。
- 多轮记忆：conversation-scoped recent turns、ContextResolution 结构化实体继承、显式实体覆盖、隐私实体拦截。
- 离线/真实评测：Precision@5、Recall@5、MRR、NDCG@5、引用率、citation schema、LLM-as-judge、关键词覆盖、groundedness proxy、延迟。

## 为什么这是 Agent-first

系统不是简单的 `query -> retrieve -> generate`，也不是每轮强制 RAG。它维护显式 `AgentState`，先由 Agent 形成执行计划，再按需调用工具或长期语义记忆：

```text
query -> memory.load -> weighted intent/risk router -> agent.plan
      -> tool planner/policy/executor
      -> optional memory.semantic_retrieve
      -> answer with doc/tool citations
      -> EvidencePackBuilder -> CriticVerifier
      -> answer/retry/refuse/escalate
```

Agent 会决策。生产/面试档中，LLM advisor 会参与意图、执行计划、工具和最终动作建议；deterministic router、ToolPolicy、evidence gate 和 citation validator 仍然最终兜底，即 **LLM proposes, rules/policy disposes**。

- 是否需要长期语义记忆：KB、客服工单、商品、评论。
- 是否调用结构化 SKU/订单工具。
- 是否调用库存、退货资格、评论摘要、相似工单等工具。
- 工具是否符合 intent 权限、隐私边界和写操作确认策略。
- 是否补充人工升级或退款申请草稿，但写操作必须用户确认，大额退款直接阻断。
- 高风险客服问题是否有足够证据。
- 是否 query expansion 后 retry，或者安全拒答。
- SKU/订单这种强结构化事实是否必须由 SQL/工具确认。
- follow-up query 是否可以安全继承上一轮 SKU/order/product。

例如 `Check order ORD-1003 status.` 这类强结构化问题可以只调用 SQL 订单工具并跳过 RAG；而退款政策、评论趋势、客户运营分析等问题会调用 `memory.semantic_retrieve`，再使用 dense/BM25/RRF/rerank 从长期语义记忆中取证据。

最新重构记录见 `docs/agent_runtime_refactor.md`：当前已经接入 `RootRouterAgent`、`Support/Recommendation/CustomerOps/Order/Refusal` DomainAgents、结构化 `ContextResolution`、`AgentLoop`、`EvidencePackBuilder`、`CriticVerifier` 和 `Replanner`；`CommerceRAGAgent` 外壳仍保留以兼容 CLI/API 和已有评测。

## 数据来源与真实性边界

仓库内包含可公开运行的合成 seed 数据，同时支持接入公开真实电商数据。

| 来源 | 类型 | 用途 | 真实性边界 |
|---|---|---|---|
| Amazon Reviews 2023 | 公开真实数据目标 | 商品元数据、评论 ETL、规模 RAG 文档 | 原始 gzip 已下载，默认只抽样构建本地子集 |
| STaRK E-Commerce / Amazon STaRK | 公开 benchmark 目标 | 检索评测设计参考 | 未内置原 benchmark 文件 |
| `data/raw/products.jsonl` | 合成 seed | SKU/商品工具、商品检索 | 结构真实，非企业私有数据 |
| `data/raw/reviews.jsonl` | 合成评论式记录 | 评论检索、客户运营 | 结构真实，非复制评论 |
| `data/raw/kb_articles/*.md` | 合成客服 KB | 政策引用、客服回答 | 模拟电商政策 |
| `data/raw/knowledge_assets/*` | 混合格式知识资产 | HTML、CSV、TXT、OCR 图片 | 模拟企业文档格式 |
| `data/raw/support_tickets.jsonl` | 合成工单 | 相似工单检索、客服评测 | 从评论式投诉模式生成 |
| `data/raw/orders.jsonl` | 合成订单 | 订单/SKU 工具 grounding | 结构真实，非企业订单 |
| `data/raw/customer_segments.jsonl` | 合成客户运营数据 | 客户运营示例 | 聚合式合成记录 |

推荐面试说法：

> 项目使用公开真实数据 schema 和本地合成 seed 数据。规模层基于 Amazon Reviews 2023 公开 gzip 文件抽样构建；客服工单和订单是合成数据，用来规避私有客户数据泄露。

## 快速开始

在本目录运行：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli ingest
python -m commerce_rag_ops.cli build-scale-subset --reviews-per-category 5000 --products-per-category 1000 --eval-size 360
python -m commerce_rag_ops.cli ingest
python -m commerce_rag_ops.cli build-sql
python -m commerce_rag_ops.cli sql-summary
python -m commerce_rag_ops.cli ask "My serum bottle arrived leaking and the pump is broken. Can I get a refund?" --generator template --reranker-model none
python -m commerce_rag_ops.cli eval --reranker-model none
python -m commerce_rag_ops.cli ablate --reranker-model none
python -m commerce_rag_ops.cli gate --reranker-model none
python -m commerce_rag_ops.cli fallback-stress
python -m commerce_rag_ops.cli judge-eval --backend qdrant --generator openai-compatible --limit 3
python -m commerce_rag_ops.cli memory-eval --reranker-model none
python -m commerce_rag_ops.cli tool-eval --reranker-model none
```

主要产物：

- `data/processed/chunks.jsonl`
- `data/structured/commerce.db`
- `reports/evaluation_report.md`
- `reports/ablation_report.md`
- `reports/quality_gate_report.md`
- `reports/fallback_stress_report.md`
- `reports/llm_judge_report.md`
- `reports/memory_eval_report.md`
- `reports/tool_eval_report.md`
- `docs/capability_matrix.md`

## 示例查询

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli ask "Recommend a baby product with good reviews for night monitoring." --generator template --reranker-model none
```

响应包含：

- 路由后的 intent
- intent scores/signals
- risk level
- action
- answer
- citations，例如 `[doc:product:P-BABY-001#...]`
- grader scores
- agent plan、tool trace、semantic memory/retrieval trace

持久化 trace：

```powershell
python -m commerce_rag_ops.cli ask "Check SKU SOFT-PDF-01 price and delivery context." --trace-out reports/sample_trace.json --trace-store reports/traces.jsonl
python -m commerce_rag_ops.cli ask "Check SKU SOFT-PDF-01 price and delivery context." --generator template --reranker-model none --trace-db reports/traces.db
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db list --limit 20
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db tree <trace_id>
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db tools <trace_id>
python -m commerce_rag_ops.cli traces --trace-db reports/traces.db candidates <trace_id> --attempt 1
python -m commerce_rag_ops.cli traces --trace-store reports/traces.jsonl legacy-jsonl
```

新的 span trace 会同时保存 `trace_run`、`trace_spans`、`trace_artifacts` 和 `retrieval_candidates`。其中 retrieval candidates 表记录 dense/BM25/RRF/rerank/final rank、forced reason、selected/dropped reason，用于解释证据为什么进入或离开最终上下文。

多轮记忆演示：

```powershell
python -m commerce_rag_ops.cli ask "Check order ORD-1003 status." --generator template --reranker-model none --conversation-db reports/conversations.db --conversation-id demo-1
python -m commerce_rag_ops.cli ask "Can I get a refund for that?" --generator template --reranker-model none --conversation-db reports/conversations.db --conversation-id demo-1
```

第二轮会把 follow-up query 改写为带 `ORD-1003` 的 resolved query，但订单事实仍会通过 SQL 工具再次确认。

## 真实 LLM 接入

CLI 的生产/面试档默认使用 OpenAI-compatible API。Endpoint 和模型有默认值，API key 只从环境变量读取，不写入仓库：

```powershell
# 编辑本地 .env，填写 COMMERCE_RAG_LLM_API_KEY
python -m commerce_rag_ops.cli llm-check
python -m commerce_rag_ops.cli ask "My serum arrived leaking. Can I get a refund?"
```

本地 `.env` 已被 `.gitignore` 排除；`.env.example` 是可提交的模板。测试或无网络环境可显式使用 `--generator template --advisor rule`。不要把 API Key 写进仓库；当前仓库已做敏感 key 扫描。

LLM advisor 开关：

```powershell
python -m commerce_rag_ops.cli ask "Can you draft a refund request for order ORD-1001?" --advisor auto
python -m commerce_rag_ops.cli qdrant-ask "Can support escalate this broken serum refund case?" --advisor auto
```

`--advisor auto` 会在 `COMMERCE_RAG_LLM_API_KEY` 存在时启用真实 LLM，让模型参与 intent routing、tool planning 和 final action 建议；没有 key 时自动回退规则链路。无论是否启用 LLM，隐私边界、写操作确认、大额退款上限、结构化事实确认和引用校验都不会被绕过。详细设计见 `docs/llm_advisor_design.md`。

## 当前规模

| 项目 | 数量 |
|---|---:|
| Amazon 子集商品 | 3,000 |
| Amazon 子集评论 | 15,000 |
| 商品画像文档 | 3,000 |
| 单条评论证据文档 | 15,000 |
| 商品+方面聚合文档 | 1,405 |
| 差评聚类文档 | 24 |
| FAQ case 文档 | 540 |
| 总 RAG 文档 | 19,969 |
| 总 chunks | 42,737 |
| Golden eval queries | 366，平均 4.41 个相关文档/query |
| Multi-turn memory eval | 5 条 MVP 多轮场景 |
| Tool golden eval | 7 条工具规划/权限/结构化事实/写工具确认场景 |
| Qdrant points | 42,737 |

## 当前正式 Gate

正式 gate 使用多相关文档标签和规则等价相关性。商品、客服、方面分析和趋势类 query 都使用 evidence pack，而不是只标一个目标文档。

当前结果：

| 指标 | 当前值 |
|---|---:|
| Precision@5 | 0.9989 |
| Recall@5 | 0.9360 |
| MRR | 1.0 |
| NDCG@5 | 0.9971 |
| Citation rate | 1.0 |
| Keyword coverage | 0.8934 |
| p95 latency | 631 ms |

`reports/evaluation_report.md` 包含 query 级检索诊断和 agentic evidence diagnostics。当前 relevant hit 信号包括 BM25 `1,238`、dense `1,178`、entity match `1,201`、sibling expansion `435`、forced fallback `232`、policy fallback `187`。

`reports/fallback_stress_report.md` 是独立的脚本化压力测试，不参与 `data/eval/golden.jsonl` 打分，也不修改评测集。它验证：

- 缺 review、policy、customer voice、product context 时会 retry 并恢复回答。
- unknown SKU、unknown order、no context 会 retry 一次后拒答，且不输出 citations。

## 结构化事实优先

SKU 和订单属于强结构化事实，必须由 SQL/工具确认，RAG 只能补充解释和政策证据：

- 显式 SKU 查不到：拒答，不借相似商品硬答。
- 显式订单号查不到：拒答，不借相似订单或商品硬答。
- 订单状态和订单商品明细分别由 `sql.order_by_id` 与 `sql.order_items_by_order_id` 提供；当前 seed 数据是一单一商品，但 SQL schema 已支持 item-level 明细。
- SQL/工具确认 product 后：最终 citations 收敛到同 `product_id` 的上下文和无 `product_id` 的政策文档。
- 价格、库存、订单状态、退货资格等结构化事实会输出 `[tool:...]` citation，并由 `tool_citation.validate` 检查答案侧 marker 是否来自本轮工具调用。
- 无显式 SKU/订单的 follow-up 或 fallback 场景：若检索结果只出现唯一商品画像，可生成 `structured_entity_infer` trace，把该商品作为 context-inferred product 继续回答；多商品或显式实体查不到时不会触发该推断。
- 若检索混入同类目但错误商品，`structured_context_filter` 会移除冲突证据并写入 trace。

## 强模型检索配置

生产/面试档推荐本地 GPU embedding + CrossEncoder rerank。当前 CLI 默认配置：

| 组件 | 默认模型 |
|---|---|
| Embedding | `BAAI/bge-large-en-v1.5` |
| Reranker | `BAAI/bge-reranker-large` |
| LLM | `deepseek-v4-flash` via OpenAI-compatible API |

构建本地 Qdrant：

```powershell
python -m commerce_rag_ops.cli qdrant-index `
  --qdrant-path .qdrant `
  --collection commerce_rag_chunks `
  --embedding-backend sentence-transformers `
  --embedding-model BAAI/bge-large-en-v1.5 `
  --embedding-device cuda `
  --embedding-batch-size 32

python -m commerce_rag_ops.cli qdrant-ask "What negative review trend appears in All_Beauty for delivery complaints?" `
  --qdrant-path .qdrant `
  --collection commerce_rag_chunks
```

CrossEncoder reranker 可通过环境变量覆盖：

```powershell
$env:COMMERCE_RAG_RERANKER_MODEL="BAAI/bge-reranker-large"
$env:COMMERCE_RAG_RERANKER_DEVICE="cuda"
python -m commerce_rag_ops.cli gate
```

如果只想跑离线 smoke test，可以加 `--reranker-model none`，系统会退回文档类型感知的本地启发式 reranker。

## 项目结构

```text
commerce-rag-ops/
  data/
    raw/                 # seed 商品、评论、KB、工单、订单
    eval/golden.jsonl    # query -> relevant ids 评测集
    processed/           # chunks
    structured/          # SQLite 结构化库
    scale/               # Amazon 子集与生成 RAG 文档
  docs/                  # 中文设计文档和面试材料
  reports/               # 评测、gate、stress、迭代日志
  src/commerce_rag_ops/  # agent、retrieval、ETL、CLI
  tests/                 # pytest 测试
```

## 面试讲法

一句话版本：

> 我做的是一个电商客服/推荐/客户运营 Agentic RAG 系统。它不是简单向量库问答，而是把公开评论数据、合成客服/订单数据、SQL 工具、混合检索、证据契约、fallback retry、拒答边界和离线评测串成一个可复现工程。

可以重点讲：

- 数据层：Amazon Reviews 2023 子集、合成工单/订单、混合格式 KB、OCR 附件。
- 切片层：按文档类型设置 chunk size/overlap，保留 metadata。
- 检索层：BGE embedding + BM25 + RRF + BGE CrossEncoder rerank + doc-type fallback。
- Agent 层：weighted intent/risk routing、LLM advisor、Tool Registry/Planner/Policy/Executor、conversation/entity memory、evidence contract、retry/refuse、span trace。
- 评测层：366 query、多相关文档标签、intent/difficulty 维度、citation schema validator、LLM-as-judge、gate、fallback stress、414 条合并报告。
- 可信边界：不改 eval 刷分；SKU/订单事实必须由结构化工具确认；无证据拒答。

## 参考项目

| 模块 | 参考灵感 |
|---|---|
| KB/ticket split、golden retrieval eval | `PranayM-235/ecommerce-rag-eval` |
| Qdrant hybrid/RRF/trace | `ShivamBwaj/Ecommerce-RAG-Chatbot` |
| Amazon Reviews schema 和 ETL | `polarbear333/rag-llm-based-recommender` |
| IR metrics 和 reranker benchmark | `tep00018/ECommerceRAG` |
| citation/refusal quality gate | `chiragmandal/llm-support-agent-mlops` |
| Agentic self-reflection / hybrid support flow | `jackson-neymar/agentic-customer-support` |

## 后续生产化方向

- 扩展 Qdrant dense + BM25 + RRF 的线上级融合策略。
- 对 `BAAI/bge-large-en-v1.5`、`bge-reranker-large` 与更大 embedding/rerank 模型做 ablation。
- 加入 LangSmith/OpenTelemetry/MLflow trace。
- 将 Amazon Reviews 2023 持久化为 Parquet。
- 扩展低证据拒答、OCR 附件、跨文档冲突类评测。
- 已加入 deterministic citation schema validator 和真实 API LLM-as-judge；下一步可扩大 judge 抽样并接入 LangSmith/OpenTelemetry。
