# 电商/客服/客户运营 RAG Agent 简历项目最终蓝图

生成时间：2026-07-04  
目标：从低热度 GitHub 项目中优中选优，组合成一个真实可信、数据来源清楚、清洗/切片/评估链路完整、能支撑面试深挖的简历项目。

## 0. 最终结论

建议不要再做“20 个项目横向罗列”，而是保留 6 个源码已检查的项目，组合包装成一个完整项目：

**CommerceRAG Ops：面向电商客服与客户运营的可评测 RAG Agent 平台**

一句话定位：

> 面向电商售前推荐、售后客服、退换货政策问答和客户运营洞察的 RAG Agent 系统，基于真实 Amazon 商品/评论数据、客服工单和知识库构建多源检索，支持混合召回、重排序、自反思校验、拒答与引用质量门，并用 RAGAS、IR 指标和线上延迟指标做端到端评测。

为什么这个方向适合简历：

- 不是 coding agent，面向电商/客服/客户运营，业务垂直度更高。
- 数据来源可以说清楚：Amazon Reviews 2023、STaRK E-Commerce、商品库、知识库、客服工单、黄金评测集。
- 工程链路完整：ETL、清洗、切片、索引、混合检索、Agent 编排、LLM 生成、评测、trace、质量门。
- 项目热度低但代码真实，适合包装成“参考多个开源项目后自研复现/增强”的求职项目。
- 面试可深挖点多：chunk 策略、召回融合、RAGAS 指标、citation/refusal gate、数据清洗、线上观测、延迟优化。

## 1. 最终保留项目

> 星标数通过 `gh api repos/<owner>/<repo>` 在 2026-07-04 认证查询。GitHub 未认证 REST 请求当时返回 403，因此使用本机已登录的 `gh` token 复核。

| 档位 | 项目 | Stars | 为什么保留 | 在最终项目中的角色 |
|---|---:|---:|---|---|
| A1 | [PranayM-235/ecommerce-rag-eval](https://github.com/PranayM-235/ecommerce-rag-eval) | 0 | 电商客服 RAG 小而完整，有 KB、ticket、SKU DB、golden dataset、IR 评测和 RAGAS-style 评测 | 客服知识库/工单 RAG、黄金集、基础评测骨架 |
| A1 | [ShivamBwaj/Ecommerce-RAG-Chatbot](https://github.com/ShivamBwaj/Ecommerce-RAG-Chatbot) | 2 | 商品 RAG 使用 Qdrant hybrid search、BM25+dense RRF、LangSmith trace、RAGAS 评测，有真实 eval 结果 | 商品检索、混合召回、ID-based context precision/recall、trace |
| A1 | [polarbear333/rag-llm-based-recommender](https://github.com/polarbear333/rag-llm-based-recommender) | 16 | Amazon Reviews 2023 数据工程最完整，有 PySpark ETL、字段清洗、review/meta join、BigQuery VECTOR_SEARCH | 真实数据来源、清洗、商品/评论推荐检索 |
| A1 | [tep00018/ECommerceRAG](https://github.com/tep00018/ECommerceRAG) | 1 | 基于 STaRK E-Commerce 的 benchmark 型项目，有 TextPreprocessor、FAISS/HNSW、reranker、Hit@K/Recall/MRR/NDCG | 大规模电商检索 benchmark、严格 IR 指标 |
| A2 | [chiragmandal/llm-support-agent-mlops](https://github.com/chiragmandal/llm-support-agent-mlops) | 0 | 客服 RAG 的 MLOps 形态清楚，有 sentence-aware chunk、稳定 chunk id、Qdrant score threshold、citation/refusal/latency gate | 质量门、拒答、引用率、MLOps/CI 评测 |
| A2 | [jackson-neymar/agentic-customer-support](https://github.com/jackson-neymar/agentic-customer-support) | 2 | 客服 Agentic RAG 形态完整，有 hybrid retriever、CrossEncoder rerank、LLM grader、自反思循环、query expansion | Agent 编排、自反思、中文/英文客服检索、兜底策略 |

不建议继续保留更多项目的原因：

- 简历项目不是文献综述，面试官更关心你能否把一条链路讲穿。
- 超过 6 个来源会让“借鉴/组合”的边界变模糊，反而降低可信度。
- 这 6 个已经覆盖数据、清洗、切片、检索、Agent、评测、trace、MLOps，不需要再堆项目数量。

## 2. 组合后的项目名称与定位

推荐项目名：

**CommerceRAG Ops**

备选项目名：

- **RetailCare RAG Agent**
- **EcomSupport Copilot**
- **CustomerOps RAG Agent**

推荐中文名：

**面向电商客服与客户运营的可评测 RAG Agent 平台**

简历一句话：

> 构建面向电商客服和客户运营的 RAG Agent 平台，整合商品库、评论、知识库和客服工单，使用混合检索、CrossEncoder 重排序、自反思校验和可观测 trace，并基于 RAGAS、Hit@K/MRR/NDCG、引用率、拒答正确率和延迟指标建立离线评测与上线质量门。

这个包装的核心不是“我做了一个聊天机器人”，而是：

- 我做了一个有真实数据来源的电商知识系统。
- 我处理了电商数据很脏的问题。
- 我知道 RAG 不是只接一个 vector DB，要评估召回、生成、引用、拒答和延迟。
- 我知道客服场景要可控：不能编政策、不能乱承诺退款、不能推荐不存在的商品。

## 3. 源项目深度拆解

### 3.1 PranayM-235/ecommerce-rag-eval

本地源码：

- [ingest.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/ingest.py)
- [eval_retrieval.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/eval_retrieval.py)
- [eval_ragas.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/eval_ragas.py)
- [rag_chain.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/rag_chain.py)
- [golden_dataset.json](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/eval/golden_dataset.json)

已确认实现：

- `ingest.py` 同时加载 KB markdown、support tickets JSON、SQLite 商品库。
- KB 与 tickets 分开切片、分开 Chroma collection。
- KB 使用 `chunk_size=512, chunk_overlap=50`。
- tickets 使用 `chunk_size=256, chunk_overlap=30`。
- chunk id 使用 `doc_id_chunk_index` 结构，便于回溯。
- `eval_retrieval.py` 计算 Precision@K、Recall@K、F1@K、MRR、NDCG@K。
- `eval_ragas.py` 做 Faithfulness、Answer Relevancy、Context Recall 这类 LLM-as-judge 评估。
- README/Streamlit 中有指标展示：Precision@5 0.35、Recall@5 0.91、MRR 0.97、NDCG@5 0.87、Faithfulness 1.00、Context Recall 0.70。

适合借鉴的点：

- 把客服 KB、历史工单、商品 SKU 拆成不同数据源，而不是全部塞进一个向量库。
- 用黄金集把每个问题对应到 `relevant_doc_ids`，便于做召回评测。
- 面试时可以说：“我把政策类问题、历史工单类问题、SKU 查询类问题做了路由，减少单一路径误召回。”

局限：

- 数据量偏小，适合作为骨架，不适合作为最终项目的数据规模主来源。
- Chroma 适合本地 demo，生产包装里建议替换或补充 Qdrant/BigQuery/FAISS。
- 部分路径写死在本机路径，说明这是课程/个人项目风格，包装时应重构成配置化。

### 3.2 ShivamBwaj/Ecommerce-RAG-Chatbot

本地源码：

- [retrieval_generation.py](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/apps/api/src/api/agents/retrieval_generation.py)
- [eval_retriever.py](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/apps/api/evals/eval_retriever.py)
- [eval_retriever2.py](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/apps/api/evals/eval_retriever2.py)
- [eval_results.md](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/eval_results.md)

已确认实现：

- `retrieval_generation.py` 使用 Qdrant `query_points`。
- dense 检索使用 `sentence-transformers/all-MiniLM-L6-v2`。
- keyword 检索使用 Qdrant BM25 `Document(text=query, model="qdrant/bm25")`。
- 两路召回通过 `FusionQuery(fusion="rrf")` 做 Reciprocal Rank Fusion。
- top_k 之前 dense 和 BM25 各取 20 个候选，再融合返回。
- 使用 LangSmith `@traceable` 标注 embedding、retriever、prompt、LLM generation、RAG pipeline。
- 生成结果使用 Pydantic/instructor 约束输出结构：`answer` 和 `references`。
- `eval_retriever.py`/`eval_retriever2.py` 使用 RAGAS 的 Faithfulness、ResponseRelevancy、IDBasedContextPrecision、IDBasedContextRecall。
- `eval_results.md` 给出结果：Context Precision 0.217、Context Recall 0.957、Faithfulness 0.881、Response Relevancy 0.841、Latency P50 31.52、Total Tokens 49,502。

适合借鉴的点：

- 商品检索场景里，纯向量检索容易漏掉具体型号、品牌、SKU、属性词；BM25 能补关键词精确匹配。
- RRF 是很好讲的融合策略：不需要校准两路分数，只使用排名位置做融合，鲁棒且工程上简单。
- IDBasedContextRecall 很适合电商商品检索，因为商品有 `parent_asin`/SKU 这类稳定 ID。
- LangSmith trace 可以直接支撑“可观测性”表述，不只是打印日志。

局限：

- Context Precision 0.217 偏低，可以包装成你改进项目的切入点：增加 reranker、metadata filter、意图路由后优化 precision。
- 生成模型与 API 依赖较多，复现成本比 Pranay 项目高。

### 3.3 polarbear333/rag-llm-based-recommender

本地源码：

- [etl_full.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/etl_full.py)
- [search_engine.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/backend/app/core/search_engine.py)
- [rag_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/backend/app/core/rag_pipeline.py)
- [test_rag_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/backend/tests/test_rag_pipeline.py)

已确认实现：

- 数据源来自 HuggingFace `McAuley-Lab/Amazon-Reviews-2023`。
- 处理的类目包括 `All_Beauty`、`Software`、`Baby_products`。
- 使用 PySpark 做 ETL，配置了 driver/executor memory、shuffle partitions、adaptive execution、checkpoint。
- review 数据字段包括 rating、title、text、asin、parent_asin、user_id、timestamp、helpful_vote、verified_purchase。
- metadata 字段包括 main_category、title、average_rating、rating_number、features、description、price、store、categories、details、parent_asin。
- 清洗包括删除 images/videos/author 等字段、numpy 类型转换、空文本处理、换行和 tab 清洗。
- review 和 metadata 通过 asin/parent_asin join。
- 输出写到 GCS Parquet，并按 `main_category` 分区。
- `search_engine.py` 使用 BigQuery `VECTOR_SEARCH` 对 product embeddings 和 review embeddings 检索。
- 商品综合分：`0.7 product_similarity + 0.2 avg_review_similarity + 0.1 avg_rating/5`。
- `rag_pipeline.py` 会按商品列表分批做 LLM 分析，避免 prompt 过长，并在 structured output 解析失败时降级为单商品 fallback。
- tests 覆盖 batching、fallback、key_specs 等逻辑。

适合借鉴的点：

- 这是最终项目“真实数据工程”的主来源。
- 简历里可以具体写 Amazon Reviews 2023，而不是笼统写“电商数据集”。
- 可以把 review 和 product metadata 分开建索引：product index 用于商品召回，review index 用于口碑/痛点/推荐理由补充。
- 客户运营方向可以从评论中抽取 pain points、selling points、best_for、sentiment highlights。

局限：

- 更偏推荐系统/RAG 推荐，不是客服 Agent 本体。
- BigQuery/GCS 依赖较重，个人复现可先用 DuckDB/Parquet/Qdrant 替代。

### 3.4 tep00018/ECommerceRAG

本地源码：

- [preprocessing.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/src/utils/preprocessing.py)
- [metrics.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/src/evaluation/metrics.py)
- [run_evaluation.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/scripts/run_evaluation.py)
- [frmr_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/src/pipeline/frmr_pipeline.py)

已确认实现：

- README 声称基于 Amazon STaRK Semi-structured Knowledge Base / STaRK E-Commerce。
- `preprocessing.py` 有完整 `TextPreprocessor`，支持 lowercase、special chars、punctuation、stopwords、contractions、digits、lemmatization、stemming、min token length 等。
- preprocessing 还包含面向电商字段的处理函数，例如 price、rank、category、review、features、combined text 等。
- `metrics.py` 实现 Hit@1/5/10/20/30/50/75/100、Recall@20/30/50/75/100、MRR、Precision@K、NDCG@K。
- `run_evaluation.py` 读取配置、校验 node/query/result 路径、跑 validation/evaluation_filtered/evaluation_full 并保存 CSV。
- `frmr_pipeline.py` 方向是 E5-large embedding、FAISS HNSW、MS MARCO MiniLM cross-encoder reranker。
- README 报告了 Hit@1、MRR 等 benchmark 结果，例如 Hit@1 54.75%、MRR 0.6403 等。

适合借鉴的点：

- 用它支撑“我不只会 RAGAS，也会传统信息检索指标”。
- STaRK E-Commerce 可以作为大规模 benchmark 数据来源，适合讲“离线召回评测”。
- TextPreprocessor 可以转化成你项目里的 `preprocess_products.py`，强调电商字段归一化。
- CrossEncoder reranker 可以作为解决 Shivam 项目 precision 偏低的改进模块。

局限：

- 更偏检索 pipeline benchmark，不是完整客服业务应用。
- 数据集准备门槛较高，包装时适合说“使用 STaRK 风格 query-product relevance 标注构造离线 benchmark”，不要夸大成线上真实业务数据。

### 3.5 chiragmandal/llm-support-agent-mlops

本地源码：

- [ingest.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/apps/ingestor/ingest.py)
- [rag.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/common/rag.py)
- [eval.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/apps/evaluator/eval.py)
- [eval_metrics.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/common/eval_metrics.py)
- [zenml_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/pipelines/zenml_pipeline.py)
- [eval_report.json](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/eval_report.json)

已确认实现：

- ingestor 做 sentence-aware chunking。
- chunk id 使用稳定 SHA256 派生 UUID，利于重复 ingest、追踪和评测。
- ingest 时会删除/重建 collection，避免旧 chunk 残留。
- Qdrant upsert 写入向量。
- `rag.py` 在 Qdrant 层使用 `score_threshold`，弱召回时 prompt 收到 no context，并要求模型基于上下文回答和引用 `[doc:source#chunk_id]`。
- `eval.py` 对 `data/eval_set/eval.jsonl` 跑评测。
- 指标包括 citation_rate、refusal_correctness、groundedness_proxy、keyword_coverage、latency_p50_ms、latency_p95_ms。
- `eval_report.json` 结果：n=4、citation_rate=1.0、refusal_correctness=1.0、groundedness_avg 约 0.6146、keyword_coverage_avg 0.75、latency_p50 10338ms、latency_p95 15906ms。
- `zenml_pipeline.py` 有质量门配置，例如 citation_rate_min 等，并将 run config/metrics 记录到 MLflow。

适合借鉴的点：

- 客服场景需要“拒答正确率”，这个比普通 QA 更贴近真实业务。
- 引用率、弱召回拒答、latency p50/p95 是面试中很好讲的生产化指标。
- 稳定 chunk id 是非常实用的小细节：可以解释每个回答引用来自哪个文档和哪个 chunk。

局限：

- eval 样本数只有 4，不能直接包装成大规模评测。
- 更像 MLOps template，需要结合电商数据和客服业务补足数据丰富度。

### 3.6 jackson-neymar/agentic-customer-support

本地源码：

- [hybrid_retriever.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/hybrid_retriever.py)
- [reflection_loop.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/reflection_loop.py)
- [llm_grader.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/llm_grader.py)
- [chunkenizer.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/vectorizer/app/vectordb/chunkenizer.py)

已确认实现：

- `hybrid_retriever.py` 同时支持 BM25、Qdrant vector、hybrid、hybrid+rerank。
- BM25 使用 `rank_bm25.BM25Okapi`。
- 中文分词优先使用 jieba，fallback 使用 regex tokenization。
- 文档加载支持 file/directory，并通过 `SimpleTextSplitter(chunk_size=500, chunk_overlap=100)` 分块。
- reranker 使用 `sentence_transformers.CrossEncoder`。
- `reflection_loop.py` 实现 SelfReflectionLoop。
- 阈值：hallucination score > 0.3 触发重试，relevance score < 0.7 触发重试，最多重试 2 次。
- 反思流程：初始回答评估 -> query enhancement -> 重新检索 -> 重新生成 -> 再评估 -> web search fallback。
- query enhancement 的 HyDE/expanded_queries/sub_queries 只作为补充召回信号，不替代原始问题。
- `llm_grader.py` 使用结构化评分，包括幻觉和相关性。

适合借鉴的点：

- 这是“Agentic RAG”包装的主来源。
- 适合客服场景：回答前后都要检查相关性和幻觉，不通过就重试或升级。
- query expansion、HyDE、decomposition 都可以说是“扩大候选召回”，但不改变用户原始问题，避免把假设内容当事实。

局限：

- 项目范围较大，部分路径和模型加载较本地化，包装时要抽象成可配置模块。
- web search fallback 在真实客服场景要谨慎，最好包装成“外部知识兜底/人工升级”，不要说随意查网页回答退款政策。

## 4. 最终项目架构

推荐包装架构：

```text
commerce-rag-ops/
  data/
    raw/
      amazon_reviews_2023/
      stark_ecommerce/
      support_tickets/
      kb_articles/
      products.sqlite
    processed/
      products.parquet
      reviews.parquet
      kb_chunks.parquet
      ticket_chunks.parquet
      eval_golden.jsonl
  src/
    etl/
      load_amazon_reviews.py
      clean_products.py
      clean_reviews.py
      build_customer_kb.py
    indexing/
      chunker.py
      embedder.py
      qdrant_indexer.py
      bm25_indexer.py
    retrieval/
      hybrid_retriever.py
      reranker.py
      product_sql_tool.py
      routing.py
    agents/
      support_agent.py
      recommendation_agent.py
      customer_ops_agent.py
      reflection_loop.py
      graders.py
    evaluation/
      retrieval_eval.py
      ragas_eval.py
      support_quality_eval.py
      latency_eval.py
    observability/
      langsmith_tracing.py
      mlflow_logger.py
    api/
      app.py
      schemas.py
  tests/
    test_chunker.py
    test_retriever.py
    test_quality_gate.py
  reports/
    eval_report.md
    error_analysis.md
    data_card.md
```

核心链路：

```text
Amazon Reviews / STaRK / KB / Tickets / SKU DB
        |
        v
Data Cleaning & Normalization
        |
        v
Chunking with stable chunk_id
        |
        v
Dense Index + BM25 Index + SQL Product Tool
        |
        v
Intent Router
  |-- policy/support question -> KB + ticket retrieval
  |-- product recommendation -> product/review retrieval
  |-- SKU/order lookup -> SQL/tool call
  |-- weak retrieval -> refusal / human escalation
        |
        v
Hybrid Retrieval + RRF + CrossEncoder Rerank
        |
        v
LLM Answer with citations
        |
        v
Self Reflection / Grader
        |
        v
Trace + Metrics + Quality Gate
```

## 5. Agentic RAG 设计

这里需要明确：最终包装不是“单轮 query -> retrieve -> generate”的普通 RAG，而是 **Agentic RAG**。它的核心体现在 5 个动作上：

- **Plan**：先判断用户意图和风险级别，再决定查哪些数据源。
- **Route**：在 KB、历史工单、商品/评论索引、SQL 商品库之间动态路由。
- **Act**：调用检索器、reranker、SQL/tool、客户运营分析器等工具。
- **Reflect**：用 grader 检查回答是否幻觉、是否相关、是否缺引用。
- **Control**：根据评分选择直接回答、改写查询重试、拒答或升级人工。

### 5.1 为什么这是 Agentic RAG

普通 RAG 的流程通常是：

```text
User Query -> Retriever -> LLM -> Answer
```

本项目的 Agentic RAG 流程是：

```text
User Query
  |
  v
Intent + Risk Router
  |-- 售后/政策: KB + Tickets + citation required
  |-- 商品推荐: Product Index + Review Index + rating/features
  |-- 订单/SKU: SQL/Product Tool + policy KB
  |-- 客户运营: Review Mining + complaint/sentiment summary
  |
  v
Retrieval Planner
  |
  v
Dense Retrieval + BM25 Retrieval + Metadata Filter
  |
  v
RRF Fusion + CrossEncoder Rerank
  |
  v
Answer Generator with citations
  |
  v
LLM Grader / Rule-based Quality Gate
  |-- pass -> return answer
  |-- low relevance -> query expansion / HyDE / sub-query retry
  |-- weak evidence -> refuse or ask clarification
  |-- high-risk support issue -> human escalation
```

所以它的 Agentic 点不是“用了某个 Agent 框架”，而是系统会基于状态做决策：检索哪里、是否调用工具、是否重试、是否拒答、是否升级人工。

### 5.2 Agent 状态设计

建议在最终实现里维护一个 `AgentState`：

```text
AgentState
  query: 原始用户问题
  intent: support | recommendation | customer_ops | sku_order | unknown
  risk_level: low | medium | high
  retrieval_plan: 需要访问的数据源和工具
  retrieved_contexts: 召回 chunk / 商品 / 评论 / 工单
  reranked_contexts: 精排后的上下文
  tool_results: SQL/SKU/库存/订单等结构化结果
  answer: 当前生成答案
  citations: 引用的 source#chunk_id 或 product_id
  grader_scores: hallucination / relevance / groundedness
  action: answer | retry | refuse | escalate
  trace_id: LangSmith/MLflow run id
```

这个状态设计方便面试时解释“Agent 为什么可控”：每次决策都有输入、输出、评分和 trace。

### 5.3 Agentic RAG 来源映射

| Agentic 能力 | 在最终项目里的表现 | 来源项目 |
|---|---|---|
| Intent routing | support/recommendation/customer ops/SKU query 分流 | PranayM + 最终包装设计 |
| Retrieval planning | 根据意图选择 KB、tickets、products、reviews、SQL | PranayM / polarbear333 / Shivam |
| Tool use | 商品 SKU、库存、价格、订单状态走 SQL/tool | PranayM |
| Hybrid retrieval action | dense + BM25 + RRF + rerank | Shivam / jackson-neymar / tep00018 |
| Query expansion / HyDE | 初次回答不过关时补充召回信号 | jackson-neymar |
| Self-reflection | hallucination/relevance grader 后决定 retry/fallback | jackson-neymar |
| Refusal control | 弱召回时拒答，不编造政策 | chiragmandal |
| Citation control | 高风险客服答案必须引用 doc/chunk | chiragmandal |
| Trace and observability | 每轮 retrieve/generate/eval 可追踪 | Shivam / chiragmandal |

### 5.4 三类 Agent 的职责

| Agent | 触发场景 | 使用工具 | 输出 |
|---|---|---|---|
| Support Agent | 退款、退货、物流、保修、售后投诉 | KB retriever、ticket retriever、SQL tool、refusal gate | 带政策引用的客服答复，必要时升级人工 |
| Recommendation Agent | 商品推荐、对比、预算/偏好筛选 | product retriever、review retriever、reranker、rating scorer | 推荐列表、推荐理由、评论证据 |
| Customer Ops Agent | 差评分析、用户痛点、运营建议 | review mining、sentiment/pain point extraction、category filter | 痛点摘要、改进建议、引用样例评论 |

Support Agent 是最适合体现 Agentic RAG 的部分，因为它不是只生成答案，而是要做风险判断：

- 涉及退款/赔付/保修时，必须有政策 chunk 引用。
- 用户缺少订单号或 SKU 时，先追问，不直接承诺处理结果。
- 召回分低或上下文冲突时，拒答或转人工。
- 初次回答被 grader 判定相关性低时，执行 query expansion 后重新检索。

### 5.5 Agentic RAG 面试说法

可以这样说：

> 我这里的 Agentic RAG 不是简单套一个 agent 框架，而是把 RAG 拆成可决策的多步流程。系统先识别意图和风险，再规划要查 KB、工单、商品评论还是 SQL 工具；检索后用 RRF 和 reranker 选上下文；生成答案后再用 grader 检查幻觉、相关性和引用。如果分数不过，会改写查询重新检索；如果证据不足，会拒答或升级人工。这样比普通 RAG 更适合客服，因为客服不能在低证据情况下编退款、保修、赔付结论。

这一段建议放进 README 的项目亮点里，标题可以叫：

**Agentic RAG workflow with retrieval planning, self-reflection and refusal control**

## 6. 模块来源映射

### 6.1 数据来源

最终项目建议使用四类数据：

| 数据 | 用途 | 来源项目 | 真实实现依据 |
|---|---|---|---|
| Amazon Reviews 2023 | 商品评论、评分、用户反馈、客户运营洞察 | polarbear333 | `etl_full.py` 调用 `McAuley-Lab/Amazon-Reviews-2023` |
| STaRK E-Commerce | query-product relevance benchmark | tep00018 | README 和 evaluation pipeline 围绕 STaRK E-Commerce |
| KB articles | 退换货、配送、保修、支付、会员政策 | PranayM | `ingest.py` 加载 markdown KB |
| Support tickets | 历史客服问题和解决方案 | PranayM / chiragmandal | `tickets.json`、`eval.jsonl`、support agent eval |
| Product SQLite/metadata | SKU、库存、价格、类目、评分 | PranayM / polarbear333 | `products.db` 校验、Amazon metadata fields |

包装建议：

- 数据卡里明确写：公开数据使用 Amazon Reviews 2023 和 STaRK E-Commerce；客服工单和 KB 为模拟电商客服数据，但结构参考真实工单字段。
- 如果担心“模拟工单”不够真实，可以从 Amazon Reviews 中抽取负面评论和物流/质量/退款相关评论，自动改写为客服 ticket。
- 商品维度以 `asin` 或 `parent_asin` 作为稳定商品 ID；客服文档以 `source#chunk_id` 作为引用 ID。

### 6.1.1 数据真实性口径

简历和面试里建议把数据分成三层说，边界要清楚：

| 数据层 | 能不能说真实 | 推荐说法 | 不建议说法 | 证据来源 |
|---|---|---|---|---|
| 商品与评论数据 | 可以说真实公开数据 | 使用 UCSD McAuley Lab 的 Amazon Reviews 2023 公开数据集，包含真实商品 metadata、用户评论、评分、时间戳、verified_purchase 等字段 | 使用某公司真实交易/用户数据 | polarbear333 `README.md`、`etl_full.py` |
| 电商检索 benchmark | 可以说公开 benchmark | 使用 STaRK E-Commerce / Amazon STaRK 作为 query-product relevance benchmark，用于检索指标评测 | 线上业务真实 query log | tep00018 `README.md`、`scripts/download_data.py` |
| 客服 KB / ticket | 不能直接说企业真实 | 按电商客服业务结构构造的模拟知识库和历史工单；字段、类别和评测方式参考真实客服系统；也可由公开评论中的投诉/售后问题衍生生成 | 使用真实企业客服聊天记录 | PranayM `data/kb_articles`、`tickets.json` |
| 商品 SKU/库存/价格 | 可以说结构真实、数据模拟 | 构造 SQLite 商品表模拟 SKU、价格、类目、库存等结构化业务数据，用于 tool call 和 grounding | 真实库存/订单库 | PranayM `products.db` |
| 黄金评测集 | 可以说人工标注/规则构造 | 构造 query -> relevant_doc_ids / relevant_product_ids 的 golden set，用于 Recall@K、MRR、NDCG 和 RAGAS 评测 | 大规模真实线上标注集 | PranayM `eval/golden_dataset.json` |

最稳的总口径：

> 数据层采用“公开真实电商数据 + 业务结构化模拟数据”的组合。商品和评论来自 Amazon Reviews 2023，属于公开真实用户评论与商品元数据；检索评测参考 STaRK E-Commerce benchmark；客服知识库、历史工单、SKU/订单状态为按真实客服系统字段构造的模拟业务数据，并通过 source、doc_id、chunk_id、product_id 建立可追踪引用。

这样说的好处是：

- “真实”落在公开商品评论和 benchmark 上，有来源可查。
- “客服/订单”不冒充企业私有数据，避免面试官追问合规和隐私时翻车。
- 仍然能体现业务真实感，因为字段、流程、评测、引用和拒答机制都按真实客服系统设计。

### 6.1.2 数据来源在 README 里怎么写

建议最终项目 README 放一个 `Data Sources` 表：

| Source | Type | Usage | Fields | Note |
|---|---|---|---|---|
| Amazon Reviews 2023 | Public real-world ecommerce dataset | 商品推荐、评论洞察、商品/评论 RAG | `asin`, `parent_asin`, `rating`, `text`, `timestamp`, `verified_purchase`, `title`, `features`, `categories`, `average_rating` | 公开数据，按类目抽样 |
| STaRK E-Commerce / Amazon STaRK | Public benchmark | 离线检索评测、Hit@K/MRR/NDCG | query, product node, relevance labels | benchmark 数据，不是线上业务日志 |
| Synthetic Support KB | Simulated business KB | 退换货、保修、物流、支付政策问答 | `doc_id`, `title`, `policy_type`, `content`, `updated_at` | 按电商客服政策结构编写 |
| Synthetic Support Tickets | Simulated support tickets | 历史问题召回、客服答案参考 | `ticket_id`, `category`, `sku`, `customer_query`, `resolution`, `status`, `date` | 可由 Amazon 评论中的投诉问题衍生 |
| Product SQL DB | Simulated structured business DB | SKU/价格/库存/订单工具查询 | `sku`, `product_name`, `category`, `price`, `stock`, `status` | 用于演示 tool grounding |

### 6.1.3 面试中怎么回答“数据是真的吗”

推荐回答：

> 分两部分。商品和评论侧是真实公开数据，我用的是 Amazon Reviews 2023，里面有商品 metadata、用户评论、评分、时间戳、verified_purchase 等字段，所以推荐和评论洞察不是手写样例。检索评测侧参考 STaRK E-Commerce 这种公开 benchmark。客服 KB、ticket 和订单库我没有说成企业真实私有数据，而是按真实电商客服字段结构构造的模拟业务数据，并且可以从公开评论里抽取投诉、物流、质量、退款类问题改写成 ticket。这样既保证数据来源合规，又能覆盖真实客服系统会遇到的流程。

如果面试官继续追问“为什么不用真实客服聊天记录”：

> 真实客服聊天记录通常涉及个人信息、订单号、地址、手机号、支付和售后隐私，不适合作为公开简历项目数据。我选择公开评论数据承载真实用户表达，用模拟 KB/ticket 承载业务流程，再用引用、拒答、人工升级和评测指标保证系统行为接近真实客服场景。

### 6.1.4 怎么让模拟客服数据看起来真实

不要只手写 20 条问答，建议这样生成和整理：

1. 从 Amazon Reviews 2023 里筛选低评分评论，例如 `rating <= 2`。
2. 用关键词筛出售后场景：`refund`、`return`、`broken`、`delivery`、`warranty`、`missing`、`wrong item`、`not working`。
3. 把评论改写成 `customer_query`，保留 `asin`/`parent_asin` 作为商品关联。
4. 根据 KB policy 生成 `resolution`，例如退货窗口、保修条件、退款路径、人工升级。
5. 给每条 ticket 加上 `category`、`sku/asin`、`status`、`date`、`priority`、`expected_policy_doc`。
6. 人工抽样检查，形成 `eval_golden.jsonl`，标注 relevant KB chunk、ticket id 和 expected keywords。

这样可以说：

> 客服工单不是凭空编的，而是从公开真实评论中抽取售后/投诉意图，再映射到模拟客服处理流程和政策库，既有真实用户表达，又规避了私有客服数据的隐私问题。

### 6.2 数据清洗

| 清洗项 | 项目中怎么做 | 来源 |
|---|---|---|
| 删除无用大字段 | 删除 images、videos、author、subtitle、bought_together | polarbear333 `etl_full.py` |
| numpy/list/dict 类型规整 | `convert_all_numpy` 递归转换 | polarbear333 `etl_full.py` |
| review 文本清洗 | 去换行、tab、strip、空值转空串 | polarbear333 `etl_full.py` |
| 商品描述拼接 | title + description + features -> item_description | polarbear333 `etl_full.py` |
| review/meta join | reviews 和 metadata 基于 asin/parent_asin join | polarbear333 `etl_full.py` |
| 电商文本标准化 | lowercase、特殊符号、标点、停用词、词形还原 | tep00018 `preprocessing.py` |
| 电商字段处理 | price、rank、category、review、features、combined text | tep00018 `preprocessing.py` |
| 分区存储 | 按 main_category 写 Parquet | polarbear333 `etl_full.py` |

最终项目可以这样写：

> 对 Amazon Reviews 2023 的 review 与 metadata 进行字段裁剪、类型规整、文本清洗和 asin/parent_asin 对齐，将商品标题、描述、features 拼接为商品语义字段，并保留评分、评论数、verified_purchase、类目等结构化字段；对客服 KB 与历史工单生成稳定 chunk_id，统一写入 Parquet/Qdrant，支持后续召回评测和引用追踪。

### 6.3 切片策略

| 文档类型 | 推荐 chunk 策略 | 来源 |
|---|---|---|
| 政策/KB 文档 | 512 chars/tokens 左右，overlap 50，按段落/句子优先 | PranayM |
| 历史客服工单 | 256 左右，overlap 30，保留 query + resolution | PranayM |
| 长客服文档 | sentence-aware chunk，稳定 SHA256 chunk id | chiragmandal |
| 中文/英文混合客服资料 | 500 chunk size，100 overlap，jieba/BM25 友好 | jackson-neymar |
| 商品描述 | title + features + description 作为独立 item document | polarbear333 / Shivam |
| 评论聚合 | 每个商品聚合 top reviews 或按 sentiment/pain point 分块 | polarbear333 |

包装建议：

- 不要只说“用了 RecursiveCharacterTextSplitter”，要说不同数据源使用不同切片策略。
- 面试可讲：政策文档需要保留上下文，所以 overlap 稍大；客服工单短而结构化，所以 chunk 更小；评论数据按商品聚合，避免单条短评论语义太稀疏。
- 引用 ID 设计为：`{source}:{doc_id}#{chunk_id}`，例如 `kb:return_policy#003`。

### 6.4 检索与排序

| 能力 | 组合方案 | 来源 |
|---|---|---|
| Dense vector retrieval | all-MiniLM-L6-v2 / E5-large embeddings | Shivam / tep00018 |
| Keyword retrieval | BM25 / Qdrant BM25 / rank_bm25 | Shivam / jackson-neymar |
| Fusion | RRF 融合 dense 与 BM25 候选 | Shivam |
| Rerank | MS MARCO MiniLM CrossEncoder | tep00018 / jackson-neymar |
| Product SQL tool | SKU、库存、价格、订单状态查询 | PranayM |
| Review-aware scoring | product similarity + review similarity + rating | polarbear333 |
| Score threshold | 弱召回时触发拒答 | chiragmandal |

最终推荐检索流程：

1. 意图识别：判断用户问题是商品推荐、政策问答、售后问题、订单/SKU 查询、客户运营分析。
2. 多路召回：对 query 同时执行 dense retrieval、BM25 retrieval、metadata filter。
3. RRF 融合：合并 dense 与 BM25 排名，保留 top 50 候选。
4. CrossEncoder rerank：重排到 top 5/top 8。
5. 工具补强：如果涉及价格、库存、订单状态，用 SQL/tool call 查结构化数据。
6. score threshold：如果最高分低于阈值或 reranker 判断低相关，触发拒答或人工升级。

面试讲法：

> 电商客服里有大量品牌、型号、SKU、物流单号、政策关键词，纯向量检索对这些 token 不稳定；所以我用了 dense + BM25 的混合召回，RRF 解决两路分数不可比的问题，再用 CrossEncoder 做精排。对商品推荐还融合评论相似度和评分，避免只按商品描述推荐。

### 6.5 Agent 编排

最终项目建议包装成 3 个 Agent：

| Agent | 负责内容 | 来源 |
|---|---|---|
| Support Agent | 退换货、保修、配送、支付、订单售后 | PranayM / chiragmandal / jackson-neymar |
| Recommendation Agent | 商品推荐、对比、评论总结、适合人群 | polarbear333 / Shivam |
| Customer Ops Agent | 评论洞察、差评聚类、用户痛点、运营建议 | polarbear333 |

统一 Orchestrator：

- `intent_router` 判断任务类型。
- `retrieval_planner` 选择 KB/ticket/product/review/SQL。
- `answer_generator` 生成带引用答案。
- `reflection_loop` 校验幻觉和相关性。
- `quality_gate` 判断是否返回、重试、拒答或升级人工。

关键设计来源：

- SelfReflectionLoop 来自 jackson-neymar。
- weak retrieval refusal 来自 chiragmandal。
- product RAG + references 来自 Shivam。
- SKU/SQLite lookup 来自 PranayM。
- review/product intelligence 来自 polarbear333。

### 6.6 评测体系

最终项目不要只写一个“准确率”，建议分四层：

#### 第一层：检索评测

指标：

- Precision@K
- Recall@K
- F1@K
- MRR
- NDCG@K
- Hit@K

来源：

- PranayM `eval_retrieval.py`
- tep00018 `metrics.py`

适用问题：

- 给定 query 和 relevant_doc_ids，系统是否把正确政策/商品/工单召回到 top K？
- 商品推荐是否找到了标注相关的 parent_asin？

#### 第二层：生成评测

指标：

- Faithfulness
- Response Relevancy
- Context Recall
- IDBasedContextPrecision
- IDBasedContextRecall

来源：

- Shivam `eval_retriever.py` / `eval_retriever2.py`
- PranayM `eval_ragas.py`

适用问题：

- 回答是否基于检索上下文？
- 是否引用了正确商品 ID 或政策 chunk？
- 是否回答了用户真正的问题？

#### 第三层：客服安全与质量门

指标：

- citation_rate
- refusal_correctness
- groundedness_proxy
- keyword_coverage
- weak retrieval refusal rate
- human escalation rate

来源：

- chiragmandal `eval.py`
- chiragmandal `eval_metrics.py`
- jackson-neymar `reflection_loop.py`

适用问题：

- 找不到依据时是否拒答？
- 涉及退款、保修、赔付时是否引用政策？
- 回答是否覆盖应包含的关键词？

#### 第四层：线上体验与成本

指标：

- latency_p50_ms
- latency_p95_ms
- total_tokens
- input_tokens
- output_tokens
- cost per 100 conversations
- retry rate

来源：

- Shivam `eval_results.md`
- chiragmandal `eval_report.json`
- Shivam/Jackson 的 trace 设计

最终项目的报告可以这样写：

| 指标组 | 指标 | 目标门槛 |
|---|---|---:|
| Retrieval | Recall@5 | >= 0.85 |
| Retrieval | MRR | >= 0.75 |
| Retrieval | NDCG@5 | >= 0.75 |
| Generation | Faithfulness | >= 0.85 |
| Generation | Response Relevancy | >= 0.80 |
| Support Safety | Citation Rate | >= 0.90 |
| Support Safety | Refusal Correctness | >= 0.85 |
| Performance | Latency P50 | <= 5s |
| Performance | Latency P95 | <= 12s |

注意：这些是你最终项目可以设定的质量门，不要把它们说成已经在所有开源来源项目中同时达到。

## 7. 可直接写进简历的版本

### 简历项目标题

**CommerceRAG Ops：面向电商客服与客户运营的可评测 RAG Agent 平台**

### 简历 bullet 版本

- 基于 Amazon Reviews 2023、STaRK E-Commerce、商品 SKU、客服知识库和历史工单构建多源电商 RAG 数据层，完成 review/meta join、字段清洗、商品描述拼接、类目分区存储和稳定 chunk_id 生成。
- 设计客服/推荐/运营三类 Agent：支持退换货政策问答、售后问题处理、商品推荐、评论洞察和客户痛点总结，并通过 intent router 动态选择 KB、ticket、product、review 和 SQL 工具。
- 实现 dense + BM25 混合召回、RRF 融合、CrossEncoder 重排序和 score threshold 拒答机制，解决 SKU/品牌/型号等关键词问题和纯向量召回误匹配问题。
- 建立端到端评测体系，覆盖 Precision@K、Recall@K、MRR、NDCG、RAGAS Faithfulness/Response Relevancy/Context Recall、citation rate、refusal correctness 和 latency p50/p95。
- 接入 LangSmith/MLflow 记录 query、retrieval context、rerank score、LLM answer、token usage 和评测指标，形成可复现 trace 与质量门，用于回归测试和上线前验收。

### 面试 3 分钟讲法

我做的是一个面向电商客服和客户运营的 RAG Agent，不是普通聊天机器人。数据层用了公开 Amazon Reviews 2023 和 STaRK E-Commerce，同时构造了商品库、客服知识库和历史工单。清洗阶段会把 review 和商品 metadata 对齐，处理 asin/parent_asin、评分、features、评论文本等字段；客服文档会按来源生成稳定 chunk id，保证回答能追踪到具体 chunk。

检索层我没有只用向量库，而是 dense + BM25 混合召回，因为电商里 SKU、品牌、型号、政策关键词很多，纯向量容易漏。两路召回后用 RRF 融合，再用 CrossEncoder rerank。Agent 会根据意图选择政策问答、商品推荐、订单/SKU 工具或客户运营分析。如果召回分数低，会拒答或转人工，避免编造退款政策。

评测上我做了两套：一套是检索指标，比如 Recall@K、MRR、NDCG；另一套是生成和客服质量，比如 RAGAS Faithfulness、Response Relevancy、Context Recall、引用率、拒答正确率和延迟 p50/p95。所有 query、context、answer、token 和评分都接入 trace，方便做错误分析和回归。

### 面试 10 分钟深挖讲法

可以按下面顺序讲：

1. 业务问题：电商客服不是开放问答，错答退款/保修政策有风险；客户运营也需要基于真实评论和商品数据，而不是凭模型记忆。
2. 数据设计：商品 metadata、review、KB、ticket、SKU DB 分开建模，不同数据源有不同 chunk 策略和索引策略。
3. 清洗细节：Amazon Reviews 2023 中 review 和 metadata 字段很多且类型复杂，需要裁剪 images/videos、转换 numpy/list/dict、清洗文本、基于 asin/parent_asin join。
4. 检索策略：dense 解决语义匹配，BM25 解决 SKU/品牌/政策词，RRF 做排名融合，CrossEncoder 做精排。
5. Agent 编排：intent router 决定走 support、recommendation、customer ops 或 SQL tool；self-reflection 检查幻觉和相关性。
6. 安全控制：低分召回不回答，政策类回答必须引用 chunk，弱上下文触发拒答或人工升级。
7. 评测体系：golden dataset 做 retrieval eval，RAGAS 做 generation eval，citation/refusal/latency 做 production gate。
8. 观测与迭代：LangSmith 看单条 trace，MLflow 记录每次实验指标，对低 precision case 做 error analysis。

## 8. 面试可能追问与回答

### Q1：为什么不用纯向量检索？

电商客服里有很多精确 token，比如 SKU、品牌、型号、订单状态、物流词、政策名称。纯向量对语义相近的问题表现不错，但对这些精确 token 不稳定。我的方案是 dense + BM25 双路召回，BM25 保证关键词和 SKU 不丢，dense 负责语义改写后的问题，最后用 RRF 融合排名。

来源：

- Shivam 的 Qdrant dense + BM25 + RRF。
- jackson-neymar 的 BM25 + vector + rerank。

### Q2：RRF 为什么适合这里？

因为 dense similarity 和 BM25 score 不在同一个分布里，直接加权需要调分数归一化。RRF 只依赖排名位置，把不同检索器的候选按 rank 融合，工程实现简单，而且在多路召回时鲁棒。

来源：

- Shivam `retrieval_generation.py` 中 `FusionQuery(fusion="rrf")`。

### Q3：你怎么证明 RAG 有效果？

我分检索和生成两层证明。检索层用 golden dataset 标注 query 到 relevant_doc_ids，计算 Recall@K、MRR、NDCG。生成层用 RAGAS/LLM-as-judge 评估 Faithfulness、Response Relevancy、Context Recall。客服场景还额外评估 citation_rate 和 refusal_correctness，因为答不出来时拒答比胡编更重要。

来源：

- PranayM `eval_retrieval.py`、`eval_ragas.py`。
- tep00018 `metrics.py`。
- Shivam `eval_retriever.py`。
- chiragmandal `eval.py`。

### Q4：你怎么做数据清洗？

商品数据来自 Amazon Reviews 2023，review 和 metadata 分开加载。清洗时删除 image/video/author 等无用字段，转换 numpy/list/dict 类型，清洗 review text 的换行和 tab，拼接 title、description、features 作为商品语义字段，再用 asin/parent_asin 对齐评论和商品 metadata。客服 KB 和 ticket 则保留 source、category、sku、status、date，并生成稳定 chunk id。

来源：

- polarbear333 `etl_full.py`。
- PranayM `ingest.py`。
- chiragmandal `ingest.py`。

### Q5：chunk size 怎么选？

不是一个 chunk size 打天下。政策 KB 通常段落较长，需要保留上下文，所以用 512/50；客服 ticket 是短问答结构，用 256/30；长文档用 sentence-aware chunk，避免切断句子；中文/英文混合客服文档可以用 500/100 并配合 jieba/BM25。商品评论则更适合按商品聚合或按 pain point 聚合，否则单条评论太短，召回噪音大。

来源：

- PranayM `ingest.py`。
- chiragmandal `ingest.py`。
- jackson-neymar `hybrid_retriever.py`。
- polarbear333 `rag_pipeline.py`。

### Q6：低召回或没有上下文时怎么办？

不让模型自由发挥。检索层设置 score threshold，如果没有 chunk 达到阈值，prompt 中明确 no context retrieved，模型需要拒答；如果是高风险售后问题，则转人工或要求用户补充订单信息。这个策略会被 refusal_correctness 指标评估。

来源：

- chiragmandal `rag.py` 和 `eval.py`。

### Q7：自反思循环怎么防止越改越错？

关键是 query enhancement 只作为补充召回信号，不替代原始用户问题。HyDE、query expansion、sub queries 只是扩大候选集，最终生成和评估仍以原始 query 为准。这样可以避免 hypothetical document 里的假设内容污染答案。

来源：

- jackson-neymar `reflection_loop.py`。

### Q8：为什么 Context Precision 可能低？

混合召回为了提高 recall，可能会带入一些不相关候选，尤其商品检索里同类商品很多。解决方法是增加 metadata filter、类目约束、CrossEncoder rerank，以及把 top_k 生成上下文控制得更严格。Shivam 项目的 eval 里 Context Recall 很高但 Precision 较低，正好说明这个 trade-off。

来源：

- Shivam `eval_results.md`。
- tep00018 reranker pipeline。

## 9. 最小可实现版本

如果要快速把项目做出来，建议分三期，不要一开始就做很大。

### Phase 1：可信 Demo

目标：两周内做出能演示的客服 RAG。

范围：

- 使用 PranayM 的 KB/ticket/product DB 思路。
- 用 Chroma 或 Qdrant 建两个 collection：KB 和 tickets。
- 实现 basic retriever + answer with citations。
- 建 golden dataset，跑 Precision@5、Recall@5、MRR、Faithfulness。

简历可写：

- “完成多源客服知识库 RAG 和离线评测闭环。”

### Phase 2：电商真实数据增强

目标：加入真实商品和评论数据。

范围：

- 使用 Amazon Reviews 2023 选 1-3 个类目。
- 做 review/meta join 和清洗。
- 商品描述与评论分开建索引。
- 加入 product recommendation agent。
- 评测商品 ID recall 和 response relevancy。

简历可写：

- “基于真实 Amazon review 数据实现商品推荐和评论洞察。”

### Phase 3：生产化与面试加分

目标：加 trace、质量门、自反思、拒答。

范围：

- Qdrant hybrid search + BM25 + RRF。
- CrossEncoder rerank。
- score threshold + refusal。
- LangSmith trace + MLflow metrics。
- RAGAS + IR + latency report。
- error analysis 文档。

简历可写：

- “建立可观测、可评测、可回归的 RAG Agent 工程体系。”

## 10. 最终文档/仓库建议补齐材料

为了“足够应付面试”，你的最终仓库至少要有这些文档：

| 文档 | 内容 |
|---|---|
| `README.md` | 项目背景、架构图、快速启动、demo 截图、指标表 |
| `docs/data_card.md` | 数据来源、字段说明、清洗规则、隐私/模拟数据说明 |
| `docs/chunking_strategy.md` | 不同数据源 chunk size、overlap、chunk_id 设计 |
| `docs/retrieval_design.md` | dense/BM25/RRF/rerank/filter/threshold 设计 |
| `docs/evaluation_report.md` | IR、RAGAS、客服质量、延迟、成本指标 |
| `docs/error_analysis.md` | 典型失败案例、原因、修复策略 |
| `docs/interview_notes.md` | 项目讲法、Q&A、trade-off |

评测报告最好包含这些表：

- 数据规模：商品数、评论数、KB 文档数、ticket 数、chunk 数。
- 检索指标：Precision@K、Recall@K、MRR、NDCG。
- 生成指标：Faithfulness、Response Relevancy、Context Recall。
- 客服指标：citation rate、refusal correctness、human escalation rate。
- 性能指标：latency p50/p95、token usage、cost。
- 消融实验：dense only、BM25 only、hybrid、hybrid+rerank。

## 11. 组合包装时的来源标注

下面是最终项目每个模块对应的学习来源，后续深入学习可以按这个顺序读源码。

| 你的模块 | 主要来源 | 必读文件 |
|---|---|---|
| 数据 ETL | polarbear333 | [etl_full.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/etl_full.py) |
| 商品/评论检索 | polarbear333 | [search_engine.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/backend/app/core/search_engine.py) |
| 商品 RAG 输出 | polarbear333 | [rag_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/polarbear333__rag-llm-based-recommender/backend/app/core/rag_pipeline.py) |
| KB/ticket ingest | PranayM | [ingest.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/ingest.py) |
| 黄金集与 IR 评测 | PranayM | [eval_retrieval.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/eval_retrieval.py) |
| RAGAS-style 评测 | PranayM | [eval_ragas.py](E:/code/agent/deepsearch/.repo-inspect/PranayM-235__ecommerce-rag-eval/notebooks/eval_ragas.py) |
| Qdrant hybrid + RRF | Shivam | [retrieval_generation.py](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/apps/api/src/api/agents/retrieval_generation.py) |
| LangSmith/RAGAS eval | Shivam | [eval_retriever.py](E:/code/agent/deepsearch/.repo-inspect/ShivamBwaj__Ecommerce-RAG-Chatbot/apps/api/evals/eval_retriever.py) |
| 电商文本预处理 | tep00018 | [preprocessing.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/src/utils/preprocessing.py) |
| 标准 IR 指标 | tep00018 | [metrics.py](E:/code/agent/deepsearch/.repo-inspect/tep00018__ECommerceRAG/src/evaluation/metrics.py) |
| 质量门/MLOps | chiragmandal | [zenml_pipeline.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/pipelines/zenml_pipeline.py) |
| 引用/拒答评测 | chiragmandal | [eval.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/apps/evaluator/eval.py) |
| score threshold RAG | chiragmandal | [rag.py](E:/code/agent/deepsearch/.repo-inspect/chiragmandal__llm-support-agent-mlops/src/common/rag.py) |
| Agentic hybrid retriever | jackson-neymar | [hybrid_retriever.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/hybrid_retriever.py) |
| 自反思循环 | jackson-neymar | [reflection_loop.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/reflection_loop.py) |
| LLM grader | jackson-neymar | [llm_grader.py](E:/code/agent/deepsearch/.repo-inspect/jackson-neymar__agentic-customer-support/customer_support_chat/app/services/rag/llm_grader.py) |

## 12. 最终推荐学习顺序

1. 先读 PranayM 的 `ingest.py`、`eval_retrieval.py`、`eval_ragas.py`，理解一个最小电商客服 RAG 闭环。
2. 再读 Shivam 的 `retrieval_generation.py`，理解 Qdrant hybrid、BM25、RRF、LangSmith trace。
3. 然后读 polarbear333 的 `etl_full.py`，补齐真实 Amazon 数据清洗和 join。
4. 读 tep00018 的 `metrics.py` 和 `preprocessing.py`，把评测指标和文本预处理讲扎实。
5. 读 chiragmandal 的 `rag.py`、`eval.py`、`zenml_pipeline.py`，学习拒答、引用率和质量门。
6. 最后读 jackson-neymar 的 `hybrid_retriever.py`、`reflection_loop.py`，把项目升级成 Agentic RAG。

这个顺序能保证面试时从“能跑”讲到“数据真实”，再讲到“可评测”和“生产化”。

## 13. 最可信的最终故事线

不要说“我从零原创了全部模块”。更可信的说法是：

> 我参考了多个低热度开源电商/客服 RAG 项目的实现，重新组合并工程化为一个面向电商客服和客户运营的 RAG Agent。我的主要工作是统一数据 schema、补齐 Amazon Reviews 数据清洗、设计多源 chunk 和索引、实现 hybrid retrieval + rerank、加入拒答和自反思质量门，并把评测从单一 RAGAS 扩展到 IR 指标、客服安全指标和线上延迟指标。

这句话最稳，因为：

- 承认参考开源，不会被问到每一行是不是原创时露怯。
- 强调你做的是组合、重构、工程化、评测体系。
- 所有模块都有源码来源可以深入学习。
- 项目仍然足够像真实工作，而不是 toy chatbot。

## 14. 可以继续深化的差异化方向

如果后续要继续增强，建议从下面选 2 个，不要全做：

1. **消融实验**：dense only vs BM25 only vs hybrid vs hybrid+rerank，展示 Recall@5、MRR、latency 的 trade-off。
2. **客服风险分级**：退款、赔付、保修为高风险，必须引用政策；普通推荐为低风险，可引用商品/评论。
3. **评论洞察 Agent**：从 review 中抽取 pain points、top complaints、feature requests，输出运营建议。
4. **多轮对话状态**：保留用户偏好、预算、尺码、品牌限制，推荐时做 context-aware retrieval。
5. **数据漂移监控**：监控 top failed intents、low score retrieval rate、refusal rate、category distribution shift。
6. **主动学习闭环**：把人工客服纠正记录加入 hard negative 或 golden dataset，定期回归评测。

最推荐优先做：

- 消融实验。
- 客服风险分级。
- 评论洞察 Agent。

这三个最容易在面试中体现工程判断。

## 15. 需要避免的包装风险

- 不要说所有数据都是企业真实数据，除非确实有授权；应该说公开数据 + 模拟客服工单。
- 不要把开源项目的指标直接说成你最终项目指标，除非你自己复跑过。
- 不要只展示 demo UI，要展示 `data_card`、`eval_report`、`error_analysis`。
- 不要过度强调 LangGraph/Agent 框架名，业务和评测更重要。
- 不要把 web search fallback 用在退款政策这类高风险场景，建议包装成人工升级或内部知识库兜底。

## 16. 最终选择一句话

如果只能保留一个核心参考：

- 数据工程选 polarbear333。
- RAG/eval 骨架选 PranayM。
- 混合检索和 trace 选 Shivam。
- 指标严谨性选 tep00018。
- MLOps/质量门选 chiragmandal。
- Agentic 编排选 jackson-neymar。

最终项目就是把这 6 个方向组合成一个可信的电商客服/客户运营 RAG Agent。
