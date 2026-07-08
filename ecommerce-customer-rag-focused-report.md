# 电商 / 客服 / 客户运营 RAG Agent 聚焦报告

核验时间：2026-07-04  
检索方式：已认证 GitHub CLI：`gh search repos`、`gh repo view`、`gh api repos/{owner}/{repo}/readme`；辅以 GitHub 网页搜索。  
筛选目标：star 不超过 500；聚焦电商、客服、客户运营；优先选择较新的 RAG 技术、数据丰富、评测结果丰富的项目。  

## 1. 筛选结论

这次扩大检索后，真正值得优先看的项目不多。大量 `ecommerce-rag` / `customer-support-rag` 仓库只是基础 Chroma/FAISS demo，没有明确数据来源或评测。更值得看的项目集中在三类：

1. **高级 RAG 客服系统**
   - Hybrid retrieval、rerank、LLM grader、query rewriting、HITL、observability。
   - 代表：`jackson-neymar/agentic-customer-support`、`supportiq`、`customer-support-agentic-rag`。

2. **评测优先的电商/客服 RAG**
   - 有 golden set、Precision/Recall/MRR/NDCG、faithfulness、answer relevancy、context recall。
   - 代表：`PranayM-235/ecommerce-rag-eval`、`genai-support-assistant-rag`、`ShivamBwaj/Ecommerce-RAG-Chatbot`。

3. **数据丰富的电商检索/推荐 RAG**
   - Amazon Reviews、STaRK E-Commerce、BigQuery thelook_ecommerce、真实 CFPB 投诉。
   - 代表：`tep00018/ECommerceRAG`、`polarbear333/rag-llm-based-recommender`、`Kparos000/langgraph-ecommerce-agent`、`nujgnil/support-agent-rag`。

最适合包装成简历项目的方向：

> **Commerce Support RAG Agent：电商客服 + 商品/订单/退款 API + Hybrid RAG + HITL + Evaluation Harness**

建议组合参考：

- 高级 RAG 技术：`jackson-neymar/agentic-customer-support`
- 评测体系：`PranayM-235/ecommerce-rag-eval`
- 数据源：`ShivamBwaj/Ecommerce-RAG-Chatbot` 或 `tep00018/ECommerceRAG`
- 生产化：`chiragmandal/llm-support-agent-mlops` 或 `databricks-solutions/agentic-customer-support`

---

## 2. A 档：最值得优先看的项目

| 排名 | 项目 | stars | 强项 | 数据来源 | 关键 RAG 技术 | 明确指标 / 结果 |
|---:|---|---:|---|---|---|---|
| 1 | [PranayM-235/ecommerce-rag-eval](https://github.com/PranayM-235/ecommerce-rag-eval) | 0 | 电商 RAG 评测最完整 | 产品目录、KB 文章、历史工单、20 Q&A golden dataset | ChromaDB、SQL structured lookup、LLM-as-judge | Precision@5、Recall@5、F1@K、MRR、NDCG@K、Faithfulness、Answer Relevancy、Context Recall；全部通过阈值 |
| 2 | [jackson-neymar/agentic-customer-support](https://github.com/jackson-neymar/agentic-customer-support) | 1 | RAG 技术最先进 | 航旅 + 电商 + FAQ，多源知识库，WooCommerce 商品/订单 | BM25 + Qdrant + RRF + Cross-Encoder、LLM Grader、自反思、Query Rewriting、DuckDuckGo fallback | 召回率提升约 30%、SSE 首字节 P95、P99、QPS、Token、Guardrail 拦截率、LangSmith + Prometheus + Grafana |
| 3 | [ShivamBwaj/Ecommerce-RAG-Chatbot](https://github.com/ShivamBwaj/Ecommerce-RAG-Chatbot) | 2 | 电商商品 RAGAS 评测清楚 | Amazon CDs & Vinyl dataset，约 1.5M products，reviews、ratings、images | Qdrant、hybrid search、product ID grounding、RAGAS | 28 curated queries；Faithfulness 0.881、Context Recall 0.957、Context Precision 0.217、median latency 31.52s，生产估计 2-5s |
| 4 | [tep00018/ECommerceRAG](https://github.com/tep00018/ECommerceRAG) | 1 | 电商检索 benchmark 最强 | Amazon STaRK E-Commerce semi-structured KB，6,380 eval queries / 9,100 full queries | E5 retrieval、FAISS、BM25 + graph augmentation、cross-encoder rerank | Hit@1、Hit@5、Hit@20、Recall@20、MRR；最佳 Hit@1 54.75%、MRR 0.6403；比 published baseline Hit@1 +20.4%、MRR +14.5% |
| 5 | [ashishlandiwal/genai-support-assistant-rag](https://github.com/ashishlandiwal/genai-support-assistant-rag) | 0 | 客服拒答/升级评测清楚 | Nimbus synthetic support KB，15 in-scope + 3 out-of-scope eval set | Agentic routing、hybrid rerank、confidence gating、human escalation | retrieval_hit@4、grounding、escalation recall、out-of-scope handling；README 样例显示 hit@4 和 grounding 100% |
| 6 | [jabbala10-bit/supportiq](https://github.com/jabbala10-bit/supportiq) | 2 | 客服多源 RAG 数据最像生产 | MySQL 订单/账号/账单/库存；ChromaDB + 8,000 PDF KB；DuckDuckGo/Tavily | Router + SQL Agent + RAG Agent + Web Agent、Hybrid retrieval、Corrective RAG | 8s average response、94% retrieval precision、60% workload reduction |
| 7 | [Kparos000/langgraph-ecommerce-agent](https://github.com/Kparos000/langgraph-ecommerce-agent) | 1 | 电商经营分析数据源真实 | BigQuery public dataset：`bigquery-public-data.thelook_ecommerce` | LangGraph、multi-agent BI、SQL validation、LangSmith tracing | SQL validity >99%、响应 <10s、pytest eval、LangSmith trace |
| 8 | [chiragmandal/llm-support-agent-mlops](https://github.com/chiragmandal/llm-support-agent-mlops) | 0 | MLOps / 质量门禁强 | Markdown support KB、eval_set | Qdrant、score_threshold retrieval、ZenML pipeline、MLflow tracking | citation rate、groundedness_proxy、refusal correctness、latency p50/p95、keyword coverage、MLflow quality gate |

---

## 3. A 档项目详解

### 3.1 [PranayM-235/ecommerce-rag-eval](https://github.com/PranayM-235/ecommerce-rag-eval)

**定位**：专门为电商客服构建的 RAG + evaluation harness。这个项目最值得看，因为它不是只做一个聊天 UI，而是把评测作为核心能力。

**数据来源**：

- Product Catalog：20 个 SKU，存 SQLite，包含结构化商品字段。
- Knowledge Base Articles：5 篇，包含 return、warranty、shipping、support 等政策类内容。
- Historical Support Tickets：20 条历史客服工单。
- Golden Dataset：20 条 Q&A，用于评测。

**RAG / Agent 机制**：

- 非结构化政策和历史工单走 RAG。
- 结构化商品事实走 SQLite 查询。
- RAG pipeline 与 SQL lookup 结合，避免把 SKU、价格、保修这类结构化事实全部塞给 LLM。
- 评测结果写入 SQLite `eval_runs` 表，保留 run history。

**明确指标**：

- Retrieval Evaluation：Precision@K、Recall@K、F1@K、MRR、NDCG@K。
- Generation Evaluation：Faithfulness、Answer Relevancy、Context Recall。
- README 示例结果：
  - Precision@5：0.35，阈值 ≥0.30，通过。
  - Recall@5：0.91，通过。
  - Faithfulness：1.00，阈值 ≥0.70，通过。
  - Context Recall：0.70，阈值 ≥0.60，通过。
  - 全部 8 项指标通过。

**为什么适合简历项目**：

它的工程故事非常清楚：电商客服不能只靠“看起来回答不错”，必须有 golden set 和 CI gate。你可以把数据规模扩到 100-200 条 Q&A，并加入订单/退款 API，把它升级成完整 Commerce Support RAG Agent。

**可包装亮点**：

- 构建电商客服 RAG 评测体系，覆盖检索质量、生成忠实度、上下文召回和业务正确性。
- 将政策/历史工单 RAG 与商品 SKU SQL lookup 解耦，降低结构化事实幻觉。
- 将评测结果写入 `eval_runs`，支持版本对比和回归检测。

### 3.2 [jackson-neymar/agentic-customer-support](https://github.com/jackson-neymar/agentic-customer-support)

**定位**：基于 LangGraph 的企业级多智能体 RAG 客服系统，面向航旅 + 电商 + 知识问答。它是本轮技术栈最“新”的项目之一。

**数据来源**：

- 航旅 mock / SQLite 数据源。
- WooCommerce 商品 / 订单查询。
- FAQ 自动同步服务：本地/远程 PDF、DOCX、Markdown。
- 外部 Web search：DuckDuckGo fallback。

**较新 RAG 技术**：

- Hybrid retrieval：BM25 + Qdrant dense vector。
- RRF fusion。
- Cross-Encoder reranking。
- LLM Grader 双维度评分：幻觉 + 相关性。
- Query Rewriting，最多 2 次重检。
- DuckDuckGo fallback。
- Citation tracker：输出来源文件 + 段落。
- Agentic RAG self-reflection loop。

**Agent / 生产化机制**：

- 1 主 + 8 专业助手分层状态机。
- MCP 外部服务热插拔。
- GoHumanLoop / HITL 人工审批。
- Jailbreak guardrail、relevance guardrail、敏感操作审批。
- FastAPI SSE 流式输出。
- LangSmith + Prometheus + Grafana + 结构化日志。

**明确指标 / 结果**：

- README 声称 Hybrid Retrieval 比单一向量检索召回率提升约 30%。
- Prometheus Histogram 监控 SSE 首字节 P95。
- Grafana 面板包含 QPS、P99 延迟、Token、活跃会话、护栏拦截率、SSE 首字节 P95。
- 目前 README 中更偏运行指标和工程指标，离线 golden-set 指标不如 `ecommerce-rag-eval` 完整。

**为什么适合简历项目**：

这是“高级 RAG 技术栈”的最佳参考。适合把它的检索链路拿来用，但你需要补一个可复现实验集：例如 100 条电商客服问题，统计 Recall@5、MRR、rerank 前后变化、query rewrite 成功率、fallback 命中率。

**可包装亮点**：

- 实现 BM25 + dense vector + RRF + Cross-Encoder 三阶段混合检索。
- 通过 LLM Grader 和 query rewriting 构建自反思 RAG，减少低质量检索导致的幻觉。
- 对退款、取消订单等敏感操作接入 HITL 审批，并用 Grafana 展示 P95/P99、Token、guardrail block rate。

### 3.3 [ShivamBwaj/Ecommerce-RAG-Chatbot](https://github.com/ShivamBwaj/Ecommerce-RAG-Chatbot)

**定位**：面向电商商品推荐和问答的生产型 RAG chatbot，使用 FastAPI、Streamlit 和 Qdrant。

**数据来源**：

- Amazon CDs & Vinyl dataset。
- README 描述约 1.5M products。
- 数据包含 product metadata、reviews、ratings、images。
- 评测集：28 curated queries with expected product references。

**RAG 技术**：

- Qdrant vector database。
- Product chunks 带 product IDs、ratings、description、metadata。
- Hybrid search。
- 明确要求回答引用真实 product IDs。
- 通过 product ID 回查 image、price、description。

**明确指标 / 结果**：

- RAGAS 0.4.3 end-to-end evaluation。
- Faithfulness：0.881。
- Context Recall：0.957。
- Context Precision：0.217。
- Median latency：31.52s。README 说明评测时包含 45s artificial delay，生产无 delay 约 2-5s。
- Evaluations run on Groq free tier，cost $0.00。

**为什么适合简历项目**：

数据规模比普通 demo 大得多，而且指标真实：Context Recall 高、Precision 低，这说明项目不是只报喜。你可以围绕“高召回低精度”做 reranker / metadata filter / product intent classifier 改进。

**可包装亮点**：

- 基于 Amazon product dataset 构建商品问答与推荐 RAG，支持产品 ID grounding 和商品详情回查。
- 使用 RAGAS 评估 Faithfulness、Context Recall、Context Precision，并分析高召回低精度的 tradeoff。
- 引入 reranker / category filter / price filter 优化 Context Precision。

### 3.4 [tep00018/ECommerceRAG](https://github.com/tep00018/ECommerceRAG)

**定位**：面向 Amazon STaRK E-Commerce semi-structured KB 的神经检索 + reranker RAG pipelines。它更像电商检索 benchmark，不是客服系统，但数据和指标非常强。

**数据来源**：

- Amazon STaRK dataset，Stanford SNAP。
- `amazon_stark_nodes_processed.csv`，约 8GB。
- query datasets：
  - `validation_queries.csv`
  - `evaluation_queries_filtered.csv`
  - `evaluation_queries_full.csv`，9,100 queries。
- README 提到 Amazon STaRK evaluation dataset 6,380 queries。

**RAG / 检索技术**：

- FRMR：E5 retrieval + Webis Set-Encoder reranker。
- FRWSR：E5 retrieval + Webis Set-Encoder。
- BARMR：BM25 + graph augmentation + cross-encoder。
- Graph augmentation 使用 also-bought / related product 等关系。
- FAISS indices。

**明确指标 / 结果**：

- Hit@1、Hit@5、Hit@20、Recall@20、MRR。
- README 最佳结果：
  - Hit@1：54.75%。
  - MRR：0.6403。
  - 比 published benchmark Hit@1 提升 20.4%。
  - MRR 提升 14.5%。
  - Recall@20 提升 7.8%。

**为什么适合简历项目**：

如果你想做更“算法/检索”导向的电商项目，它是最好的。缺点是它不是客服 agent，但你可以把它作为商品检索层，接到客服/导购 agent 后面。

**可包装亮点**：

- 在 STaRK E-Commerce KB 上实现 neural retriever + reranker + graph augmentation。
- 对比 dense、sparse、graph-enhanced sparse 三类策略，使用 Hit@K、Recall@20、MRR 做离线评测。
- 将检索层接入电商导购 Agent，为商品推荐提供可量化的 retrieval backbone。

### 3.5 [ashishlandiwal/genai-support-assistant-rag](https://github.com/ashishlandiwal/genai-support-assistant-rag)

**定位**：客服 RAG + agentic routing，重点是“何时回答、何时重排、何时升级人工”。

**数据来源**：

- Nimbus synthetic support knowledge base。
- `eval/eval_set.jsonl`。
- 15 个 in-scope 问题 + 3 个 out-of-scope 问题。

**RAG 技术**：

- Top-k retrieval。
- Similarity confidence threshold。
- Borderline query 走 hybrid rerank。
- Out-of-scope / low-confidence 自动升级人工。
- Answer + sources + decision trace。

**明确指标**：

- `retrieval_hit@4`。
- `grounding`。
- escalation recall。
- out-of-scope handling。
- `eval/run_eval.py` 输出 `eval/report.md`。
- README 样例显示 retrieval_hit@4 和 grounding 为 100%。

**为什么适合简历项目**：

客服系统必须能“拒答和升级”，这是很多 RAG demo 没有的。这个项目适合做评测模板，尤其适合测 out-of-scope refusal 和 human handoff。

**可包装亮点**：

- 构建 confidence-based escalation，低置信度或知识库不覆盖时不强行回答。
- 用 eval set 评估 retrieval hit、grounding、out-of-scope handling 和 escalation recall。
- 在客服场景中把“拒答正确率”作为一等指标。

### 3.6 [jabbala10-bit/supportiq](https://github.com/jabbala10-bit/supportiq)

**定位**：on-premise adaptive RAG multi-agent customer support。

**数据来源**：

- MySQL：order status、account info、billing、inventory。
- ChromaDB + 8,000 PDF knowledge base：product specs、return policy、FAQ、manuals。
- DuckDuckGo / Tavily：promotions、breaking updates。

**RAG 技术**：

- Router-based multi-agent architecture。
- SQL Agent。
- RAG Agent。
- Web Agent。
- ChromaDB + BM25 hybrid retrieval。
- Corrective RAG：检索质量差时 relevance grading + query rewrite。
- Qwen3-8B / Ollama，本地部署。

**明确指标 / 结果**：

- 8 second average response time。
- 94% retrieval precision on policy questions。
- 60% reduction in agent workload。

**为什么适合简历项目**：

它的数据源结构非常像真实客服：SQL 处理交易事实，RAG 处理政策文档，Web 处理实时信息。很适合直接当 CommerceOps Agent 的蓝图。

**可包装亮点**：

- 使用 router 将订单/账单/库存、政策文档、实时促销拆给不同 agent。
- 构建 ChromaDB + BM25 混合检索，并通过 Corrective RAG 处理低质量召回。
- 以 retrieval precision、平均响应时间、人工工作量下降作为业务指标。

### 3.7 [Kparos000/langgraph-ecommerce-agent](https://github.com/Kparos000/langgraph-ecommerce-agent)

**定位**：电商经营分析 Agent，用自然语言查询 BigQuery public ecommerce dataset，并生成业务洞察。

**数据来源**：

- Google BigQuery public dataset：`bigquery-public-data.thelook_ecommerce`。
- 主表包括 orders、order_items、products、users、events、distribution_centers。

**RAG / Agent 技术**：

- LangGraph。
- 多 agent：segmentation、trend、geo analytics、product performance。
- Natural language to SQL。
- SQL validation。
- BigQuery execution。
- Report synthesis。
- LangSmith tracing。

**明确指标 / 结果**：

- README 声称 SQL validity >99%。
- Typical response under 10s。
- pytest-based eval / unit tests。
- LangSmith 记录 prompt、sub-agent routing、SQL creation、validation、execution、report synthesis。

**为什么适合简历项目**：

这不是传统文档 RAG，而是“数据分析型 RAG/Agent”。它适合做客户运营：GMV、AOV、用户分群、品类趋势、地区销售、履约表现。

**可包装亮点**：

- 基于真实公开电商数据集构建 NL2SQL + BI Agent。
- 通过 SQL validator 和 LangSmith trace 保证可解释性。
- 自建 50 条业务问题 eval set，评估 table routing accuracy、SQL validity、answer correctness 和 latency。

### 3.8 [chiragmandal/llm-support-agent-mlops](https://github.com/chiragmandal/llm-support-agent-mlops)

**定位**：RAG-based support agent 的端到端 MLOps 项目，强调 ZenML + MLflow + Qdrant + Kubernetes。

**数据来源**：

- Markdown support knowledge base。
- `eval_set/` 小型评测集。

**RAG / MLOps 技术**：

- Qdrant vector DB。
- Sentence-aware chunking。
- Deterministic chunk IDs。
- Score-threshold retrieval。
- ZenML pipeline：ingest -> eval -> register + quality gate。
- MLflow tracking：metrics + artifacts。

**明确指标 / 结果**：

- citation rate。
- groundedness proxy。
- refusal correctness。
- latency p50 / p95。
- keyword coverage。
- `gate_pass = True/False` logged to MLflow。

**为什么适合简历项目**：

这个项目适合补“生产化评测与上线门禁”。你可以把它的 pipeline 接到电商客服 RAG 上，让每次更新知识库/embedding/prompt 都跑评测，指标下降则阻止上线。

**可包装亮点**：

- 构建 RAG CI/CD 质量门禁，自动记录 citation rate、refusal correctness、latency p95。
- 使用 MLflow 保存 run config、eval_report、metrics，实现可复现的 RAG 迭代。
- 通过 score threshold 控制低质量上下文进入 prompt，减少幻觉。

---

## 4. B 档：有价值，但需要补评测或数据

| 项目 | stars | 值得借鉴 | 短板 |
|---|---:|---|---|
| [haoyiyin/basjoo](https://github.com/haoyiyin/basjoo) | 147 | 开源 AI 客服平台，RAG KB、多 provider、embeddable widget、Qdrant、文件上传、human takeover、E2E tests | 平台工程强，但 README 中 RAG 评测指标不够明确 |
| [ro-anderson/multi-agent-rag-customer-support](https://github.com/ro-anderson/multi-agent-rag-customer-support) | 122 | LangGraph 多 Agent 客服，travel DB benchmark、Qdrant、LangSmith；README 规划 Adaptive RAG / Corrective RAG / Self-RAG | Star 较高，项目较早；高级 RAG 多为规划项，评测指标不够完整 |
| [ANI-IN/Multi-Agent-Customer-Support](https://github.com/ANI-IN/Multi-Agent-Customer-Support) | 21 | Chinook digital music store，SQL grounding、identity verification、HITL、long-term memory、28 deterministic tests | 更偏 tool/SQL agent，不是典型 RAG；离线 RAG 指标缺 |
| [nvikou/Ai-support-chat-react-fastapi](https://github.com/nvikou/Ai-support-chat-react-fastapi) | 7 | 支持自动化 70-80% 工单，confidence score、citations、automatic escalation、dashboard | 评测结果更像产品指标声明，缺 golden-set 指标 |
| [nujgnil/support-agent-rag](https://github.com/nujgnil/support-agent-rag) | 0 | 使用真实 CFPB complaint sample 1000，转成 support tickets，FAISS，Streamlit，AzureML | 金融客服而非电商；README 未给明确评测分数 |
| [lingyun1010/ecommerce-rag-agent](https://github.com/lingyun1010/ecommerce-rag-agent) | 1 | Etsy/Shopify-like agent，订单 API + RAG + escalation，清楚地区分 live operational facts 和 RAG 文档 | 没有明确评测结果 |
| [dineschandgr/spring-ai-order-support-agent](https://github.com/dineschandgr/spring-ai-order-support-agent) | 2 | Spring AI + Gemini + MySQL + SSE，订单状态/取消/客户订单工具调用 | RAG 技术较弱，更偏 tool calling；评测不足 |
| [ahmettugur/agentic-customer-support-bot](https://github.com/ahmettugur/agentic-customer-support-bot) | 2 | .NET 10 + MAF，6-agent orchestration、HITL、reasoning trace store、YAML evaluation runner | 不一定是 RAG 强项目，但 agent 工程化很强 |
| [databricks-solutions/agentic-customer-support](https://github.com/databricks-solutions/agentic-customer-support) | 12 | Synthetic telco data、Vector Search、MLflow Tracing、Databricks Agent Evaluation | 绑定 Databricks 生态；不是电商，但客服 LLMOps 很强 |
| [polarbear333/rag-llm-based-recommender](https://github.com/polarbear333/rag-llm-based-recommender) | 16 | Amazon Reviews 2023、GCP/Vertex/BigQuery、MRR/nDCG/latency/cost，电商推荐数据丰富 | 更偏推荐检索，不是客服/客户运营 |
| [Frnn4268/shop-nexus-core](https://github.com/Frnn4268/shop-nexus-core) | 1 | 完整电商微服务，订单事件、推荐服务、RAG service、precision/recall/coverage/hit rate/MRR | RAG 评测较弱，推荐评测强；适合作系统架构参考 |

---

## 5. 不建议首选的项目类型

这次搜索里有大量类似项目，不建议作为主体：

- 只有 Chroma / FAISS + Streamlit 的基础 RAG chatbot，没有数据集和评测。
- 只有“客服 agent”但没有 RAG 或业务数据源。
- 只有平台 UI、ticket CRUD、chat widget，但 RAG 只是“可以上传知识库”。
- 只有产品搜索，没有订单/退款/客服流程，也没有离线指标。
- 只有 README 声称“production-ready”，但没有 eval set、测试或指标。

---

## 6. 简历项目最佳组合方案

### 方案：CommerceRAG Ops Agent

**一句话**：一个面向电商售后和客户运营的多源 RAG Agent，支持商品问答、订单查询、退款政策、人工升级，并内置评测和可观测性。

### 数据来源

- 商品库：Amazon product metadata / 自建 SKU catalog / Shopify mock catalog。
- 订单库：SQLite / MySQL / MongoDB orders。
- 退款记录：refunds / returns table。
- 文档库：return policy、warranty、shipping、FAQ、product manuals。
- 历史工单：support tickets。
- Golden set：100 条 customer queries，覆盖商品、订单、退款、政策、投诉、out-of-scope。

### RAG 技术

- BM25 + dense vector hybrid retrieval。
- RRF fusion。
- Cross-Encoder rerank。
- Metadata filters：category、brand、price、SKU、policy type。
- LLM Grader：relevance + groundedness。
- Query rewrite：最多 2 次。
- CRAG fallback：低质量检索时扩大检索或升级人工。
- Citation tracker：source file、chunk_id、policy section。

### Agent 编排

- Router Agent：判断 Product / Order / Refund / Policy / Escalation。
- Product RAG Agent：商品问答、推荐、对比。
- Order Tool Agent：订单状态、物流、历史订单。
- Refund Policy RAG Agent：退货政策、保修、退款条件。
- Customer Ops Agent：投诉、情绪、SLA、升级建议。
- Human Approval：退款、取消订单、优惠补偿走 HITL。

### 评测指标

**Retrieval**

- Precision@5。
- Recall@5。
- MRR。
- nDCG@5。
- Context Precision。
- Context Recall。

**Generation**

- Faithfulness。
- Answer Relevancy。
- Citation Precision。
- Citation Recall。
- Grounding。

**Agent / 业务**

- Intent routing accuracy。
- Entity F1：order_id、sku、customer_id、refund_id。
- Tool routing accuracy。
- Escalation recall。
- Out-of-scope refusal accuracy。
- Policy compliance。
- Unsafe action block rate。

**性能 / 成本**

- p50 / p95 / p99 latency。
- first token latency。
- token cost / query。
- rerank latency。
- fallback rate。

### 简历 bullet

- 构建面向电商售后的多 Agent RAG 系统，整合商品库、订单 API、退款政策文档和历史工单，实现商品问答、订单查询、退款判断和人工升级。
- 实现 BM25 + Qdrant dense retrieval + RRF + Cross-Encoder rerank 的三阶段检索链路，并通过 LLM Grader 与 query rewriting 构建自反思 RAG。
- 自建 100 条电商客服 golden set，评估 Precision@5、Recall@5、MRR、nDCG@5、Faithfulness、Citation Precision、Escalation Recall。
- 引入 HITL 审批和 policy engine，对取消订单、退款、优惠补偿等敏感操作进行人工确认和审计记录。
- 使用 Prometheus/Grafana/MLflow 记录 p95 latency、token cost、fallback rate、guardrail block rate 和评测回归，形成可复现的 RAG 迭代流程。

---

## 7. 真实性增强候选：重点看数据清洗、切片和评估

这一节专门补充“更像真实项目”的候选。筛选标准更偏工程过程：数据从哪里来、怎么清洗、怎么切片、怎么建索引、怎么评估。很多 RAG demo 只展示聊天效果，但简历项目要讲清楚这些底层环节，才不像套壳。

| 项目 | stars | 真实性来源 | 数据清洗 / 切片 / 索引 | 评估指标 | 适合借鉴 |
|---|---:|---|---|---|---|
| [polarbear333/rag-llm-based-recommender](https://github.com/polarbear333/rag-llm-based-recommender) | 16 | Amazon Reviews 2023，UCSD McAuley Lab | PySpark ETL、清洗、normalization、deduplication、长评论 passage chunking、BigQuery 存储、Vertex AI embeddings | MRR、nDCG@k、Precision/Recall、latency、per-1000-query cost | 真实电商评论 RAG 推荐系统 |
| [PranayM-235/ecommerce-rag-eval](https://github.com/PranayM-235/ecommerce-rag-eval) | 0 | 产品目录、KB 文章、历史工单、20 Q&A golden dataset | 结构化 SKU 进 SQLite，政策/历史工单进 RAG，评测结果写 `eval_runs` | Precision@5、Recall@5、F1@K、MRR、NDCG@K、Faithfulness、Answer Relevancy、Context Recall | 电商客服 eval-first 架构 |
| [ShivamBwaj/Ecommerce-RAG-Chatbot](https://github.com/ShivamBwaj/Ecommerce-RAG-Chatbot) | 2 | Amazon CDs & Vinyl，约 1.5M products，reviews、ratings、images | 商品 chunk 带 product ID、rating、description；Qdrant hybrid search；回答后回查 product detail | 28 curated queries；Faithfulness 0.881、Context Recall 0.957、Context Precision 0.217、latency | 商品推荐 RAG + RAGAS |
| [tep00018/ECommerceRAG](https://github.com/tep00018/ECommerceRAG) | 1 | Amazon STaRK E-Commerce semi-structured KB，6,380 eval queries / 9,100 full queries | STaRK nodes、FAISS indices、E5 embeddings、BM25 tokenized docs、graph augmentation | Hit@1/5/20、Recall@20、MRR；Hit@1 54.75%、MRR 0.6403 | 电商检索 benchmark 背书 |
| [nujgnil/support-agent-rag](https://github.com/nujgnil/support-agent-rag) | 0 | 真实 CFPB complaint sample 1000，转换成 support tickets | raw CFPB CSV -> `support_tickets.csv`；financial support docs -> FAISS index | 有 tests / AzureML 部署线索；指标需补 | 真实客服投诉数据参考 |
| [chiragmandal/llm-support-agent-mlops](https://github.com/chiragmandal/llm-support-agent-mlops) | 0 | Markdown support KB + eval set | sentence-aware chunking、deterministic chunk IDs、Qdrant score threshold、ZenML ingest/eval/register pipeline | citation rate、groundedness_proxy、refusal correctness、latency p50/p95、keyword coverage、MLflow gate | RAG MLOps 和质量门禁 |
| [Frnn4268/shop-nexus-core](https://github.com/Frnn4268/shop-nexus-core) | 1 | 完整电商微服务：商品、订单、推荐、RAG、事件流 | MongoDB 商品/订单；order_created 事件；Chroma RAG service；推荐模型 artifact versioning | 推荐侧 precision、recall、coverage、hit rate、MRR；RAG 侧需补 | 电商系统架构和推荐评测 |
| [Annkkitaaa/Ecommerce-RAG-Chatbot](https://github.com/Annkkitaaa/Ecommerce-RAG-Chatbot) | 12 | `Product_Information_Dataset.csv` + `Order_Data_Dataset.csv` | `preprocess_data.py` 清洗产品/订单，生成 processed products/orders 和 product embeddings | pytest；缺明确 RAG 指标 | 商品 + 订单双数据源 MVP |

### 值得强调的真实工程细节

如果你后面要真正做一个项目，建议把“数据工程”作为第一层亮点写进去：

- **多源数据**：商品 catalog、订单、退款记录、政策文档、商品评论、历史工单、out-of-scope 问题集。
- **清洗与标准化**：去重、空值处理、价格/评分/品牌/category 标准化、SKU 规范化、HTML/Markdown/PDF 文本抽取。
- **元数据抽取**：`product_id`、`sku`、`category`、`brand`、`price_range`、`rating`、`policy_type`、`source_file`、`chunk_id`。
- **切片策略**：政策文档按 section 切；长评论按 passage chunking；FAQ 保留完整问答对；历史工单按 issue/resolution 切。
- **索引策略**：BM25 处理关键词和 SKU；dense vector 处理语义；RRF 融合；Cross-Encoder rerank；metadata filter 控制品类/价格/品牌。
- **评估数据**：手写 golden dataset，覆盖商品推荐、订单状态、退货政策、投诉升级、知识库外问题。
- **回归记录**：每次改 chunk size、top_k、embedding model、reranker、prompt，都生成 eval run 并保存在 SQLite / MLflow。

## 8. 包装升级版：Eval-first Commerce Support RAG Agent

前面的方案可以进一步包装成一个更真实的简历项目：

> **Eval-first Commerce Support RAG Agent：带真实商品评论、订单数据、政策文档和工单评测的电商客服 RAG 系统**

### 项目定位

这个项目不要写成“电商 RAG 聊天机器人”。更好的叙述是：

> 我做了一个 eval-first 的电商客服 RAG Agent，把商品推荐、订单查询、退款政策、历史工单和人工升级放在同一个多源检索与评测框架下，并用 golden set 持续评估检索质量、生成忠实度和客服流程正确性。

### 数据设计

建议至少准备 5 类数据：

| 数据 | 来源 | 用途 | 存储 |
|---|---|---|---|
| 商品 catalog | Amazon Reviews / 自建 SKU catalog | 商品问答、推荐、对比 | SQL + vector metadata |
| 商品评论 | Amazon Reviews 2023 / CDs & Vinyl | 场景化推荐、优缺点总结 | passage chunks |
| 订单数据 | mock Shopify / WooCommerce / SQLite orders | 查订单、查物流、历史订单 | SQL |
| 政策文档 | shipping、return、warranty、FAQ | 退货、保修、配送问答 | vector DB |
| 历史工单 | support tickets / CFPB-like complaints | 相似案例召回、回复草稿 | vector DB |

### 数据流水线

可以把清洗和切片写成独立 pipeline：

1. **Extract**：读取 CSV / JSONL / Markdown / PDF / HTML。
2. **Clean**：去重、统一字段、过滤空文本、清理 HTML、规范价格/评分/category。
3. **Enrich**：生成 `source_type`、`source_file`、`sku`、`category`、`brand`、`policy_type`、`created_at`。
4. **Chunk**：政策按 section，评论按 passage，FAQ 按问答对，工单按 issue/resolution。
5. **Index**：BM25 index + dense vector index + metadata index。
6. **Evaluate**：对每次索引版本跑 golden set，记录指标。

### 检索链路

建议实现四路检索：

- **Keyword / BM25**：适合 SKU、品牌、订单号、政策关键词。
- **Dense Vector**：适合语义问题和场景化推荐。
- **Metadata Filter**：按 category、brand、price_range、rating、policy_type 限定范围。
- **Cross-Encoder Rerank**：对 top-50 候选重排，提升 Precision@5。

RAG 流程可以写成：

```text
query
  -> intent router
  -> entity extractor
  -> BM25 + dense retrieval
  -> RRF fusion
  -> metadata filter
  -> cross-encoder rerank
  -> LLM grader
  -> answer / rewrite / escalate
```

### 评估体系

建议把评估分四层：

| 层级 | 指标 | 解释 |
|---|---|---|
| Retrieval | Precision@5、Recall@5、MRR、nDCG@5 | 检索是否找到了正确商品/政策/工单 |
| Generation | Faithfulness、Answer Relevancy、Context Recall、Citation Precision | 回答是否忠实、是否引用正确 |
| Agent | Intent accuracy、Entity F1、Tool routing accuracy、Escalation recall | 路由、抽取、工具调用和升级是否正确 |
| Product | p95 latency、token cost、fallback rate、human handoff rate | 是否能上线、是否稳定 |

### 对照实验

报告里可以设计 A/B/C 实验，让项目更像研究型工程：

| 实验 | Baseline | Candidate | 预期观察 |
|---|---|---|---|
| Retrieval | dense only | BM25 + dense + RRF | Recall@5 提升 |
| Rerank | no rerank | Cross-Encoder rerank | Precision@5 / MRR 提升 |
| Chunking | fixed 800 chars | section-aware chunking | policy citation 更准确 |
| Filtering | no metadata | category/price/rating filter | 商品推荐更贴近需求 |
| Refusal | always answer | confidence threshold + escalate | out-of-scope 错答下降 |

### 简历 bullet 升级版

- 设计并实现 eval-first 电商客服 RAG Agent，整合商品 catalog、Amazon Reviews 商品评论、订单数据、退款政策文档和历史工单，覆盖商品推荐、订单查询、政策问答和人工升级。
- 构建数据清洗与索引流水线，对商品评论和历史工单做去重、字段标准化、元数据抽取和 passage-level chunking，并将商品/政策/工单分别写入 SQL、BM25 和向量索引。
- 实现 BM25 + dense vector + RRF + Cross-Encoder rerank 的混合检索链路，支持 SKU、category、brand、price、rating、policy_type 等 metadata filters。
- 自建 100 条电商客服 golden set，评估 Precision@5、Recall@5、MRR、nDCG@5、Faithfulness、Context Recall、Citation Precision、Escalation Recall 和 p95 latency。
- 引入 confidence threshold、LLM Grader 和 query rewriting，对低质量检索自动重写查询或升级人工，减少 out-of-scope 和低置信度场景下的幻觉回答。
- 使用 MLflow / SQLite 记录每次 chunking、embedding、top_k、reranker 和 prompt 变更后的评测结果，形成可复现的 RAG 回归测试流程。

## 9. 最终推荐排序

| 排名 | 推荐参考 | 为什么 |
|---:|---|---|
| 1 | `PranayM-235/ecommerce-rag-eval` | 电商 RAG 评测体系最完整，最适合当你项目的 eval harness |
| 2 | `jackson-neymar/agentic-customer-support` | RAG 技术最新最全，适合参考高级检索和 Agentic RAG |
| 3 | `ShivamBwaj/Ecommerce-RAG-Chatbot` | Amazon 商品数据丰富，RAGAS 结果明确 |
| 4 | `tep00018/ECommerceRAG` | STaRK E-Commerce benchmark 强，适合做检索算法背书 |
| 5 | `jabbala10-bit/supportiq` | 多源客服 RAG 架构最接近真实生产 |
| 6 | `ashishlandiwal/genai-support-assistant-rag` | 拒答/升级人工评测清楚，适合客服安全性 |
| 7 | `Kparos000/langgraph-ecommerce-agent` | 真实 BigQuery 电商数据，适合客户运营/BI Agent |
| 8 | `chiragmandal/llm-support-agent-mlops` | MLOps 和质量门禁强，适合补生产化 |
