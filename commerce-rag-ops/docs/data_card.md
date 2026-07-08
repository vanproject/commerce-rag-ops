# 数据卡片

本文档记录 CommerceRAG Ops 的数据来源、规模、清洗规则、切片策略、评测集边界和隐私边界。

## 目标

本项目用于展示一个可复现的电商客服/推荐/客户运营 Agentic RAG 工程。仓库内使用安全的合成 seed 数据，规模层兼容公开真实数据 Amazon Reviews 2023。项目不包含真实企业客服工单、真实客户聊天或真实订单。

推荐表述：

> Public-real-data compatible，本地合成 seed 数据可复现运行；规模数据来自 Amazon Reviews 2023 公开数据格式。

避免表述：

> 仓库包含真实企业工单、真实客户聊天、真实订单。

## 数据层

| 层 | 当前实现 | 生产/公开来源 |
|---|---|---|
| Products | `data/raw/products.jsonl` 合成商品目录 | Amazon Reviews 2023 product metadata |
| Reviews | `data/raw/reviews.jsonl` 合成评论式记录 | Amazon Reviews 2023 raw reviews |
| Support KB | `data/raw/kb_articles/*.md` 与 `data/raw/knowledge_assets/*` | 企业政策文档、帮助中心 HTML、CSV 表、PDF、扫描件 |
| Tickets | `data/raw/support_tickets.jsonl` 合成工单 | 匿名化 CRM，或由公开评论生成 |
| Orders | `data/raw/orders.jsonl` 合成订单 | 匿名化订单服务/数据仓库 |
| Customer segments | `data/raw/customer_segments.jsonl` 合成客户运营记录 | CRM/CDP 聚合数据 |
| Golden eval | `data/eval/golden.jsonl` | 多相关文档 evidence pack 标签 |
| Structured SQL | `data/structured/commerce.db` | warehouse/order DB/feature store |

## Amazon 公开数据

项目支持通过命令下载 Amazon Reviews 2023 官方 gzip 文件：

```powershell
python -m commerce_rag_ops.cli download-amazon-full --count-rows
```

当前工作区包含三个简历项目类别的完整 gzip 文件：

| Category | Reviews | Metadata |
|---|---:|---:|
| All_Beauty | 701,528 | 112,590 |
| Software | 4,880,181 | 89,251 |
| Baby_Products | 6,028,884 | 217,724 |

原始文件位于 `data/raw/amazon_reviews_2023/`，manifest 位于 `data/raw/amazon_reviews_2023/manifest.json`。默认不会把 11.6M reviews 全部塞进 SQLite 或 Qdrant，而是构建真实规模子集，保证本地项目轻量可复现。

## 当前数据规模

| 层 | 路径 | 当前内容 |
|---|---|---|
| 原始公开数据 | `data/raw/amazon_reviews_2023/` | Amazon gzip 文件和 manifest |
| 原始 seed 数据 | `data/raw/*.jsonl`, `data/raw/kb_articles/*.md`, `data/raw/knowledge_assets/*` | 商品、评论、工单、订单、客户分群、混合格式 KB |
| RAG/eval 数据 | `data/processed/chunks.jsonl`, `data/eval/golden.jsonl` | 42,737 chunks，366 条主评测 query |
| Refusal eval | `data/eval/refusal.jsonl` | 48 条 unknown/refusal 边界用例 |
| Combined eval | `reports/combined_eval_report.md` | 366 条正常业务问答 + 48 条边界/拒答问答，合计 414 条 |
| Citation schema smoke | `reports/citation_schema_smoke_report.md` | 25 条样本，验证 citation marker、state citations 与 retrieved contexts 一致性 |
| Scale subset | `data/scale/*.jsonl` | 3,000 商品，15,000 评论，19,969 RAG 文档 |
| SQL 数据 | `data/structured/commerce.db` | 结构化实体、eval labels、chunks、Amazon manifest |

SQLite 表覆盖：

| 表 | 行数 | 来源 |
|---|---:|---|
| `products` | 6 | `data/raw/products.jsonl` |
| `reviews` | 12 | `data/raw/reviews.jsonl` |
| `support_tickets` | 6 | `data/raw/support_tickets.jsonl` |
| `orders` | 4 | `data/raw/orders.jsonl` |
| `customer_segments` | 4 | `data/raw/customer_segments.jsonl` |
| `kb_articles` | >= 9 | KB 与 mixed-format assets |
| `scale_products` | 3,000 | `data/scale/products.jsonl` |
| `scale_reviews` | 15,000 | `data/scale/reviews.jsonl` |
| `scale_rag_documents` | 19,969 | `data/scale/rag_documents.jsonl` |
| `golden_eval` | 366 | `data/eval/golden.jsonl` |
| `document_chunks` | 42,737 | `data/processed/chunks.jsonl` |
| `amazon_sample_products` | 20 | `data/raw/products.amazon_sample.jsonl` |
| `amazon_sample_reviews` | 20 | `data/raw/reviews.amazon_sample.jsonl` |
| `public_data_files` | 6 | Amazon manifest |

## 清洗规则

- 标准化空白字符，保留原始 ID。
- 过滤空评论、空标题和不可检索文本。
- 保留结构化字段：`product_id`、`sku`、`review_id`、`ticket_id`、`doc_id`。
- 通过 `parent_asin`/商品 ID 关联评论和商品元数据。
- 解析 Markdown、HTML、TXT、CSV、JSON、可选 PDF 文本、OCR 图片 sidecar。
- 审计不支持文件和空抽取结果。
- 商品文本组合 title、category、description、features、price、rating。
- 工单文本组合 `customer_query` 和 `resolution`。

## 切片规则

| Source | Chunk size | Overlap | 原因 |
|---|---:|---:|---|
| KB | 520 | 60 | 保留完整政策上下文 |
| KB table | 420 | 50 | 表格行保持紧凑 |
| KB OCR image | 360 | 45 | OCR 噪声更高，chunk 更短 |
| Ticket | 280 | 35 | query/resolution 保持紧凑 |
| Product | 480 | 40 | 保留商品特征整体 |
| Review | 360 | 30 | 保留单条客户声音 |

## 文档类型覆盖

| 文档类型 | 数量 | 说明 |
|---|---:|---|
| Markdown policy | 5 | 退货、保修、支付退款、配送、缺件 |
| HTML policy page | 1 | 退货状态矩阵 |
| Text notice | 1 | 承运商异常通知 |
| CSV table | 1 | 退款原因码 |
| OCR image | 1 | 损坏索赔表单，含订单/SKU 证据 |
| Unsupported fixture | 1 skipped | 表格导出边界测试 |

## Scale RAG 文档类型

| Doc type | Count | 用途 |
|---|---:|---|
| `product_profile` | 3,000 | 商品画像，含评分/评论信号 |
| `review_evidence` | 15,000 | 单条评论证据 |
| `review_aspect_summary` | 1,405 | 商品+方面聚合 |
| `complaint_cluster` | 24 | 类目+方面差评趋势 |
| `faq_case` | 540 | 由 actionable reviews 派生的客服 case |

## 评测标签

当前评测集不再是一条 query 只对应一个相关文档，而是多文档 evidence pack：

| Relevant docs/query | Query count |
|---:|---:|
| 1 | 3 |
| 2 | 61 |
| 3 | 41 |
| 4 | 93 |
| 5 | 77 |
| 6 | 52 |
| 7 | 15 |
| 8 | 24 |

平均每条 query 有 4.41 个相关文档，更接近真实 RAG 答案需要商品画像、代表性评论、方面总结、政策文档和 FAQ case 一起支撑的情况。

后续 precision/fallback 迭代没有修改 `data/eval/golden.jsonl` 的相关文档标签，也没有为了分数好看重写标签。最近只补齐早期 6 条 seed query 缺失的 `intent`、`expected_action`、`safety_category` 元数据；366 条主评测 query 保持稳定，指标变化来自检索逻辑、路由、证据契约、fallback/retry/refusal、报告刷新。

当前主评测不再包含缺失标注导致的 `unknown` 桶。真实 unknown/out-of-scope 与安全边界由 `data/eval/refusal.jsonl` 衡量，当前 48 条；合并报告把 366 条正常业务问答和 48 条边界/拒答问答统一展示为 414 条，并按 `intent`、`expected_action`、`safety_category` 分组。

评测还支持规则等价相关性，例如同商品同 rating 的 review evidence 可作为 review-evidence query 的有效替代证据，避免把合理替代证据误判为 false positive。

## Citation Schema 检查

除了 `keyword_coverage`，eval 会对答案引用做 deterministic schema 检查：

- citation marker 必须符合 `[doc:<source>:<doc_id>#<chunk_id>]`。
- state citations 必须能映射到本轮 retrieved contexts。
- answer 文本里的 citation 必须来自 state citations，不能编造 doc id 或 chunk id。
- `must_cite=true` 的样本必须在 answer 正文里实际出现合法 citation。

新增指标包括 `citation_schema_ok`、`answer_citation_precision`、`answer_citation_recall`、`citation_grounded_rate`，并在报告中统计 `missing_answer_citation`、`unknown_answer_citation`、`ungrounded_state_citation` 等失败原因。

## 隐私边界

仓库不包含真实私有客户数据。生产版本应在入库前删除或 hash PII，例如姓名、手机号、地址、订单号、支付信息等。
