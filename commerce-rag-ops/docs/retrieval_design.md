# 检索与 Agentic RAG 设计

本文档说明 CommerceRAG Ops 的检索链路、fallback 策略、证据契约和评测结果。

## 总体链路

```text
query
  -> intent/risk routing
  -> source plan: kb / ticket / product / review
  -> BGE dense scoring / local semantic scoring
  -> BM25 keyword scoring
  -> reciprocal rank fusion
  -> BGE CrossEncoder rerank + business heuristic prior
  -> evidence contract
  -> tool-grounded context filtering
  -> answer / retry / refuse
```

## 为什么用 Hybrid Retrieval

电商问题同时包含语义意图和精确实体：

- 语义：`money back` 应该匹配 `refund`
- 精确：SKU、订单号、商品名、policy type、license key

因此系统同时保留：

- BM25：抓 SKU、订单、政策关键词。
- 轻量 semantic：抓同义表达和泛化问题。
- RRF：融合不同 ranking，不依赖分数归一化。
- rerank：生产/面试档使用 `BAAI/bge-reranker-large` CrossEncoder，并保留文档类型、商品、rating、aspect、policy 等业务特征作为弱先验。

## 文档模型

`kb` 不只是 Markdown 政策，而是 typed knowledge source：

| Type | 检索角色 |
|---|---|
| Markdown policy | 权威客服政策 |
| HTML help-center page | 帮助中心页面 |
| CSV reason-code table | 运营规则和 triage code |
| TXT carrier notice | 时效性客服通知 |
| OCR claim image | 扫描附件证据 |

结构化实体放在 SQLite：商品、价格、库存、订单、客户分群、SKU metadata。长文本和模糊证据进入 RAG 检索。

## 当前索引规模

默认不把 11.6M Amazon reviews 全塞进 Qdrant，而是抽样真实规模子集：

| Category | Reviews | Products |
|---|---:|---:|
| All_Beauty | 5,000 | 1,000 |
| Software | 5,000 | 1,000 |
| Baby_Products | 5,000 | 1,000 |

子集生成：

- 19,969 个 RAG 文档
- 42,737 个 chunks
- Qdrant payload 包含 `source`、`doc_type`、`category`、`product_id`、`rating`、`timestamp`、`scale_dataset`

## Doc-type-aware Ranking

本地 hybrid retriever 包含多种生产式保护：

- 按 `(source, doc_id)` 去重，避免一个长文档占满 Top-5。
- typed forced candidates：趋势类注入 `complaint_cluster`，方面类注入 `review_aspect_summary`，推荐类注入 `product_profile`，客服 case 注入 `faq_case`。
- evidence-pack diversification：Top-5 尽量覆盖互补证据，而不是重复 chunk。
- 标题 token 倒排索引：快速定位商品、评论、FAQ、方面文档。
- 标题到 product_id fallback：生成 query 中的商品标题可映射回商品 ID。
- 精确标题优先、数字标题消歧，避免不同规格商品混淆。
- rating/aspect 约束：评论证据必须匹配商品、rating、issue type。
- parent/sibling expansion：aspect summary 或 FAQ 命中后拉取同商品同方面评论。
- support policy fallback：客服 case 必须搭配政策引用。
- curated seed routing：短 demo query 用 SKU 或商品 token 定位本地 seed。
- category guard：趋势/投诉类 query 保持在指定类目。
- adaptive context pruning：商品已确定时不强行用其他商品填满 Top-5。
- rating evidence-pack collection：足够多同商品同 rating 评论时，Top-5 聚焦 review evidence。
- product-level aspect hard guard：`around <aspect>` 是强约束。
- support lineage ordering：FAQ case 的 `derived_from_review_id` 优先拉回原始 review。
- support dynamic evidence budget：证据够用时不填低价值上下文。
- policy-family guard：refund、warranty、shipping、missing parts 等映射到对应政策族。
- structured-entity context filtering：SKU/订单工具确认 product 后，最终 citation 只保留同 `product_id` 上下文和无 product_id 的政策文档。

## Agentic Evidence Contract

Agent 在生成答案前检查证据包是否满足 intent：

| Intent | 期望证据 |
|---|---|
| support | policy + case/review 证据 |
| recommendation | product + review 证据 |
| customer_ops | customer voice / complaint / aspect evidence |
| sku_order | SQL/工具确认的结构化实体 + product/policy 上下文 |

关键缺口会触发 retry：

- `missing_policy`
- `missing_review`
- `missing_customer_voice`
- `missing_product_context`
- `missing_structured_entity`
- `no_context`

无法恢复时拒答，避免低证据硬答。

## 结构化事实优先

SKU 和订单是强结构化事实：

- 显式 SKU 必须由商品工具确认。
- 显式订单号必须由订单工具确认。
- 未知 SKU/订单：retry 一次后仍缺结构化实体则拒答。
- 工具确认 product 后，最终 RAG citations 收敛到同 `product_id`。
- 无 product_id 的政策文档仍可作为补充引用。

这一层解决“工具说 A，但引用混入 B”的 evidence conflict。

## 当前正式 Gate

| Metric | Value |
|---|---:|
| Precision@5 | 0.9989 |
| Recall@5 | 0.9360 |
| MRR | 1.0 |
| NDCG@5 | 0.9971 |
| Keyword coverage | 0.8934 |
| p95 latency | 631 ms |

## 检索诊断

当前 full eval relevant-hit signals：

| Signal | Relevant hits |
|---|---:|
| BM25 | 1,238 |
| Dense | 1,178 |
| Entity match | 1,201 |
| Aspect match | 542 |
| Sibling expansion | 435 |
| Forced fallback | 232 |
| Policy fallback | 187 |

## Agentic 证据诊断

正式评测不仅看 retrieval，还统计 agent loop：

| Signal | Value |
|---|---:|
| Retry rate | 0.0 |
| One-attempt answers | 366 |
| Traced `missing_case_evidence` gaps | 36 |

这 36 个 support gap 表示 policy 证据已足够回答，但没有额外相似 case。系统记录为残余风险，不触发昂贵 retry。

## Fallback Stress

独立脚本化压力测试不修改 `data/eval/golden.jsonl`，用于证明 critical fallback 路径：

| Case | Critical gap | 预期行为 |
|---|---|---|
| Recommendation | `missing_review` | retry，补 review evidence |
| Support | `missing_policy` | retry，补 policy |
| Customer ops | `missing_customer_voice` | retry，补投诉/评论证据 |
| SKU/order recoverable | `missing_product_context` | retry，补商品上下文 |
| Unknown SKU | `missing_structured_entity` | retry 后仍未知则拒答 |
| Unknown order | `missing_structured_entity` | retry 后仍未知则拒答 |
| Low evidence | `no_context` | retry 后仍无证据则拒答 |

当前 stress 结果：`7/7` 通过。4 条恢复并带 citations，3 条安全拒答且无 citations。

## Ablation Modes

CLI 支持：

| Mode | 用途 |
|---|---|
| `dense` | 检查语义扩展 |
| `bm25` | 检查关键词/SKU/policy |
| `hybrid` | 检查 RRF 融合 |
| `hybrid_rerank` | 最终检索器，默认使用 BGE reranker |

运行：

```powershell
python -m commerce_rag_ops.cli ablate
```

## Embedding 与 Reranker

Qdrant 支持两类 embedding backend：

| Backend | 用途 |
|---|---|
| `hash` | 测试/无网络机器的确定性 fallback |
| `sentence-transformers` | 本地 GPU embedding |

生产/面试档默认模型：

| 组件 | 默认模型 | 说明 |
|---|---|---|
| Embedding | `BAAI/bge-large-en-v1.5` | 本地 GPU SentenceTransformer，替换早期 MiniLM demo 索引 |
| Reranker | `BAAI/bge-reranker-large` | CrossEncoder，结合业务 heuristic prior |
| LLM | `deepseek-v4-flash` | OpenAI-compatible API，用于真实生成链路 |

离线测试可以使用 `hash` embedding 和 `--reranker-model none`，但这只用于 smoke test，不作为代表性测评配置。

## 面试讲法

可以这样总结：

> 我把 RAG 检索做成 evidence-pack 级别，而不是单 chunk 相似度。生产档用 BGE large embedding 召回、BM25 补精确实体、RRF 融合，再用 BGE reranker 和业务约束排序。Agent 会检查证据包是否满足 intent，缺关键证据就 retry，恢复不了就拒答。SKU/订单事实必须由 SQL 工具确认，RAG 只做解释性证据。
