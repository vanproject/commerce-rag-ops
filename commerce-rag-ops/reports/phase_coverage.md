# Phase 覆盖报告

本报告基于当前实现状态手工整理，用于说明 3 个阶段的功能是否已经落地，以及面试时可引用的证据文件。

## Phase 1: 可信客服 RAG Demo

状态：已实现并验证。

证据：

- 种子客服知识库：`data/raw/kb_articles/*.md`
- 多格式知识资产：`data/raw/knowledge_assets/*`
- 种子客服工单：`data/raw/support_tickets.jsonl`
- Golden 评测集：`data/eval/golden.jsonl`
- 切片输出：`data/processed/chunks.jsonl`
- 生成切片同步写入 SQL：`data/structured/commerce.db`，表 `document_chunks`
- Agentic 客服流程：`src/commerce_rag_ops/agent.py`
- 验证命令：`python -m pytest -q -p no:cacheprovider`

已实现点：

- KB/工单摄取
- Markdown、HTML、TXT、CSV、OCR 图片知识摄取
- 稳定 chunk ID
- Support intent routing
- 带引用的回答
- 拒答与质量评分
- 检索指标与客服质量指标

## Phase 2: 电商数据增强

状态：已实现，包含人工整理种子数据和已下载的公共样本。

证据：

- 人工商品数据：`data/raw/products.jsonl`
- 人工评论数据：`data/raw/reviews.jsonl`
- 订单数据：`data/raw/orders.jsonl`
- 客户分层数据：`data/raw/customer_segments.jsonl`
- 已下载 Amazon Reviews 2023 商品样本：`data/raw/products.amazon_sample.jsonl`
- 已下载 Amazon Reviews 2023 评论样本：`data/raw/reviews.amazon_sample.jsonl`
- Amazon Reviews 2023 全量原始 gzip 文件：
  - `data/raw/amazon_reviews_2023/All_Beauty/reviews.jsonl.gz`: 701,528 行
  - `data/raw/amazon_reviews_2023/All_Beauty/metadata.jsonl.gz`: 112,590 行
  - `data/raw/amazon_reviews_2023/Software/reviews.jsonl.gz`: 4,880,181 行
  - `data/raw/amazon_reviews_2023/Software/metadata.jsonl.gz`: 89,251 行
  - `data/raw/amazon_reviews_2023/Baby_Products/reviews.jsonl.gz`: 6,028,884 行
  - `data/raw/amazon_reviews_2023/Baby_Products/metadata.jsonl.gz`: 217,724 行
- 订单工具种子数据：`data/raw/orders.jsonl`
- 客户运营种子数据：`data/raw/customer_segments.jsonl`
- SQLite 运营库：`data/structured/commerce.db`
- 导入器：`src/commerce_rag_ops/importers.py`

已实现点：

- 兼容 Amazon Reviews 2023 的 product/review schema
- 官方 Amazon Reviews 2023 gzip fallback importer
- 商品推荐 agent
- 评论/客户运营检索
- Order/SKU 结构化工具
- 订单明细工具 `sql.order_items_by_order_id`，当前 seed 数据从订单派生一行 item，schema 支持一单多商品
- 当 `data/structured/commerce.db` 存在时，Order/SKU 工具走 SQLite 查询
- 用于客户运营分析的客户分层种子数据

边界说明：

- 已下载的 Amazon 样本与人工整理种子数据分开存放，不会自动合并进默认 golden eval。

## Phase 3: 工程化与面试增强项

状态：大部分已实现并验证。

证据：

- 检索消融：`reports/ablation_report.md`
- 质量门禁：`reports/quality_gate_report.md`
- 数据/项目审计：`reports/project_audit.md`
- Trace store：`src/commerce_rag_ops/trace_store.py`
- 浏览器 dashboard：`web/index.html`
- HTTP API：`src/commerce_rag_ops/api.py`
- Qdrant 后端：`src/commerce_rag_ops/retriever_backends.py`
- OpenAI-compatible generator：`src/commerce_rag_ops/generator.py`
- SQLite 构建器：`src/commerce_rag_ops/sql_store.py`

已实现点：

- dense/BM25/hybrid/hybrid-rerank 消融
- 质量门禁 pass/fail 报告
- 本地 JSONL trace store
- HTTP `/ask`、`/metrics`、`/traces`
- 浏览器 dashboard
- 浏览器 Tool Trace 面板：Tool Plan、Tool Calls、Retrieval Constraints、Context Inference
- 本地嵌入式 Qdrant index 与查询路径
- OpenAI-compatible LLM adapter
- SQLite build/summary 命令，以及 SQL-backed order/SKU lookup

LLM 验证：

- OpenCode Go endpoint 已接入并验证。
- `deepseek-v4-flash` 已完成一次带引用的 live RAG answer。
- Trace artifact：`reports/llm_trace.json`

## 当前验证快照

- 测试：`pytest -q`，24 passed。
- Qdrant index：`commerce_rag_chunks`，42,737 points，本地 `.qdrant`
- SQLite store：`data/structured/commerce.db`，新增构建会包含 `order_items` 表和索引；历史本地库未重建时工具会从 `orders` 回退派生 item。
- SQLite 表行数目标：products 6，reviews 12，tickets 6，orders 4，order_items 4，customer segments 4，KB articles >=9，scale products 3,000，scale reviews 15,000，scale RAG docs 19,969，golden eval 366，chunks 42,737，Amazon sample products 20，Amazon sample reviews 20，public manifest files 6
- Scale gate：Precision@5 0.7923，Recall@5 0.9044，MRR 0.9836，NDCG@5 0.9649，keyword coverage 0.8816，p95 latency 651 ms
- Quality gate：PASS
- Amazon Reviews 已下载样本：20 products，20 reviews
- Amazon Reviews 全量原始文件：3 categories，11,610,593 review rows，419,565 metadata rows
- Order/SKU/order-items tool：已用 `ORD-1001`、`ORD-1003` 验证
- LLM live check：PASS with `deepseek-v4-flash`
