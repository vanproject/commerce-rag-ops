# RAG / Agentic RAG 项目候选：数据来源与明确指标版

核验时间：2026-07-04  
检索方式：使用已认证的 GitHub CLI：`gh search repos`、`gh repo view`、`gh api repos/{owner}/{repo}/readme`。  
筛选口径：star 不超过 500；优先选择 RAG / Agentic RAG / RAG 评测项目；必须能说清楚数据来源和指标。继续排除 coding agent / SWE agent / 自动修代码方向。

## 结论

如果目标是做求职简历项目，我建议优先考虑三条路线：

1. **金融 RAG Agent**
   - 最强参考：`RAGAS-FINANCE`、`Financial-Analyst-Agent-RAG-LangGraph`。
   - 数据来源清楚：SEC / EDGAR / Apple 10-K / companyfacts / yfinance。
   - 指标清楚：faithfulness、context_precision、citation traceability、latency、token cost、table/cell 命中。

2. **电商/客服 RAG Agent**
   - 最强参考：`genai-support-assistant-rag`、`langgraph-ecommerce-agent`、`supportiq`、`agentic-customer-support`。
   - 数据来源清楚：thelook_ecommerce、客服知识库、产品/退货 PDF、订单数据库、synthetic telecom data。
   - 指标清楚：retrieval_hit@k、grounding、escalation recall、SQL validity、latency、RAGAS、MLflow Agent Evaluation。

3. **RAG Eval Harness + 业务 Agent**
   - 最强参考：`SagnikKK1/rag-eval-harness`、`apoorva-01/rag-eval-harness`、`Akash-1512/rag-eval-harness`、`weijia-89/oncology-rag-lab`。
   - 数据来源清楚：公开评论、arXiv papers、AI/ML papers、合成临床 notes、MS MARCO、Kubernetes docs。
   - 指标清楚：Recall@k、MRR、nDCG、citation precision/recall、RAGAS、DeepEval、regression gate、drift。

---

## 最推荐主候选

| 优先级 | 项目 | stars | 领域 | 数据来源 | 明确指标 | 适合包装方向 |
|---:|---|---:|---|---|---|---|
| 1 | [zhenjun-avatar/RAGAS-FINANCE](https://github.com/zhenjun-avatar/RAGAS-FINANCE) | 7 | 金融 RAG Agent | SEC-style filings、Apple CIK 320193、EDGAR HTML、companyfacts JSON、Apple narrative questions 100 条 | `faithfulness`、`context_precision`、平均 latency、平均 token、Langfuse traces | 金融投研 RAG Agent，带 RAGAS 评测和 trace |
| 2 | [denis7-jean/Financial-Analyst-Agent-RAG-LangGraph](https://github.com/denis7-jean/Financial-Analyst-Agent-RAG-LangGraph) | 4 | 金融 SEC Filing Agent | Apple 2024 Form 10-K、yfinance 实时市场数据 | 8 case eval：Route、Retrieval、Cell、Answer；`retrieval_support_present` 6/8；100% citation traceability | SEC filing table-aware RAG Agent |
| 3 | [ashishlandiwal/genai-support-assistant-rag](https://github.com/ashishlandiwal/genai-support-assistant-rag) | 0 | 客服 RAG Agent | Nimbus synthetic support KB、`eval/eval_set.jsonl`，15 条 in-scope + 3 条 out-of-scope | `retrieval_hit@4`、`grounding`、escalation recall、out-of-scope handling | 可评测客服 RAG Agent，适合直接做简历 demo |
| 4 | [Kparos000/langgraph-ecommerce-agent](https://github.com/Kparos000/langgraph-ecommerce-agent) | 1 | 电商经营分析 Agent | Google BigQuery public dataset：`bigquery-public-data.thelook_ecommerce` | LangSmith trace、pytest eval、SQL validity >99%、响应 <10s | 自然语言到电商 BI 分析 Agent |
| 5 | [SagnikKK1/rag-eval-harness](https://github.com/SagnikKK1/rag-eval-harness) | 0 | Agentic RAG Eval | Motorola Edge 50 Fusion 公开 YouTube/Reddit 评论，20 answerable + 6 not-in-corpus golden set | `recall@1/3/5/10`、MRR、refusal_acc、CI regression gate、RAGAS pending | 带 CRAG / rerank / refusal 的 RAG 评测底座 |
| 6 | [Akash-1512/rag-eval-harness](https://github.com/Akash-1512/rag-eval-harness) | 1 | RAG Eval + Red Team Agent | 20 篇 AI/ML research papers，10 组真实 Q&A | RAGAS 5 指标、DeepEval G-Eval、red-team agent、MLflow tracking | 生产级 RAG 评测与红队平台 |
| 7 | [apoorva-01/rag-eval-harness](https://github.com/apoorva-01/rag-eval-harness) | 3 | 研究论文 RAG | 15 篇 retrieval/RAG/embedding arXiv papers，50 个问题 | NDCG@5、Recall@5、MRR、faithfulness、answer relevance、context precision/recall、citation precision/recall | 论文 RAG + citation faithfulness |
| 8 | [weijia-89/oncology-rag-lab](https://github.com/weijia-89/oncology-rag-lab) | 0 | 医疗/肿瘤 RAG Lab | 8 条 base synthetic clinical notes、12 条 adversarial edge-case notes、gold_standard CSV | DeepEval pass rate、>5% regression gate、A/B drift、contextual precision/recall、Phoenix traces | 结构化临床实体抽取 RAG 评测 |
| 9 | [jabbala10-bit/supportiq](https://github.com/jabbala10-bit/supportiq) | 2 | 客服 Multi-Agent RAG | MySQL 订单/账号/账单/库存、ChromaDB + 8,000 PDF KB、DuckDuckGo/Tavily Web | 8s average response、94% retrieval precision、60% workload reduction | On-prem 客服 RAG Agent |
| 10 | [databricks-solutions/agentic-customer-support](https://github.com/databricks-solutions/agentic-customer-support) | 12 | Telco 客服 Agent | synthetic telecom customer data、profiles、subscriptions、KB articles、support tickets | MLflow Tracing、Databricks Agent Evaluation、Unity Catalog lifecycle | 企业客服多 Agent + RAG observability |

---

# 1. 金融 RAG Agent

## 1.1 [zhenjun-avatar/RAGAS-FINANCE](https://github.com/zhenjun-avatar/RAGAS-FINANCE)

**为什么值得看**：这是本轮最符合“RAG + 数据来源 + 指标”的金融候选。它不是普通金融聊天机器人，而是面向 SEC-style filings 的 node-centric RAG 系统，包含 ingestion、hybrid retrieval、rerank、Langfuse trace 和 RAGAS evaluation。

**数据来源**：

- SEC / EDGAR style HTML filings。
- Apple CIK `320193`。
- `CIK0000320193.json` companyfacts。
- `apple_narrative_questions_100.json`：100 个 Apple narrative questions，按 topic group A-J 组织。

**RAG 机制**：

- 把 EDGAR HTML 解析成 multi-level section tree，leaf 作为 chunk。
- Dense retrieval：Qdrant。
- Sparse retrieval：Postgres full-text 或 OpenSearch。
- Fusion：RRF。
- 可选 rerank。
- Langfuse trace 记录查询与评测。

**明确指标**：

- RAGAS：`faithfulness`、`context_precision`。
- README 样例：100 个问题，`faithfulness` 平均约 0.90。
- 平均端到端 latency：约 10.9s / question。
- 平均 token：约 1.9K / question。

**简历包装建议**：

可以做成 **FinTrace RAG Agent**：SEC 文件 ingestion、section-tree retrieval、RAGAS batch evaluation、Langfuse trace dashboard。面试时重点讲：为什么金融 RAG 需要 section tree、为什么要 dense+sparse fusion、怎么用 RAGAS 防止幻觉。

## 1.2 [denis7-jean/Financial-Analyst-Agent-RAG-LangGraph](https://github.com/denis7-jean/Financial-Analyst-Agent-RAG-LangGraph)

**为什么值得看**：这个项目解决金融 RAG 的具体痛点：财报表格错位、引用不可追溯、LLM 算术错误。它用 LangGraph 显式路由，在 RAG、市场数据、calculator tool 之间切换。

**数据来源**：

- Apple 2024 Form 10-K。
- yfinance 实时市场数据。
- SEC filing 的 narrative section、table cell、risk factors。

**RAG 机制**：

- Hi-res document parsing 保留表格结构。
- Hybrid retrieval：BM25 + vector + RRF。
- `cell_plan_node` 先定位 exact table cells，再让 LLM 读取。
- `calculator` tool 做确定性数学计算。
- `narrative_audit_node` 做叙述类问题引用审计。
- LangSmith observability。

**明确指标**：

- README 给出 Test Run 11：8 个 Apple 10-K case。
- 维度：Route、Retrieval、Cell、Answer。
- `retrieval_support_present`：6/8，75%。
- 明确追踪 table/cell 命中、citation mismatch、row mismatch、year mismatch。

**简历包装建议**：

可以做成 **SEC Filing Analyst Agent**。关键亮点是“表格级证据选择”：每个答案不仅有 source page，还能定位 row/column/cell。评测集可以扩到 50 条财报问题，指标包括 answer exactness、citation correctness、calculation correctness、cell hit rate。

## 1.3 [AtharshKrishnamoorthy/Enterprise-RAG](https://github.com/AtharshKrishnamoorthy/Enterprise-RAG)

**为什么值得看**：偏企业金融 RAG pipeline，围绕 earnings call transcripts 做 ingestion、retrieval 和 evaluation API。

**数据来源**：

- `Transcripts` 目录下的公司 earnings call transcripts。
- 示例公司包括 AAPL、AMD、AMZN。

**RAG 机制**：

- Transcript ingestion。
- Chunk + embedding。
- FAISS vector database。
- FastAPI 暴露 ingestion、retrieval、evaluation endpoints。

**明确指标**：

- Answer Relevancy。
- Faithfulness。
- Contextual Precision。
- Overall average score。
- 返回每个 metric 的 reasoning。

**简历包装建议**：

适合做 **Earnings Call RAG Analyst**：把财报电话会 transcript、10-K、行情数据整合起来，回答“管理层对毛利率/需求/风险的表述如何变化”。指标可继承它的 answer relevancy、faithfulness、contextual precision。

## 1.4 [gmespinozar15/financial-analyst-agent](https://github.com/gmespinozar15/financial-analyst-agent)

**为什么列入补充**：它不是最强 RAG 项目，但适合把金融工具调用与 RAG 评测结合。已有 yfinance、VaR、CVaR、Sharpe、比较分析等工具。

**数据来源**：

- yfinance 实时行情和历史价格。
- 公司基本面数据。

**现有指标**：

- VaR / CVaR。
- Volatility。
- Drawdown。
- Sharpe / risk-adjusted return。

**需要补的 RAG 指标**：

- 给它加 SEC filing RAG 后，补 citation correctness、faithfulness、context precision。

**简历包装建议**：

作为金融 RAG Agent 的工具层参考：RAG 负责财报证据，工具负责行情与风险计算。

---

# 2. 电商 / 客服 / 客户运营 RAG Agent

## 2.1 [ashishlandiwal/genai-support-assistant-rag](https://github.com/ashishlandiwal/genai-support-assistant-rag)

**为什么值得看**：这是客服 RAG 里最适合直接借鉴的 eval-first 项目。它不仅有 RAG，还有 agentic routing：回答、重排、升级人工，都由 agent 根据 retrieval confidence 和 coverage 决策。

**数据来源**：

- Nimbus synthetic support knowledge base。
- `eval/eval_set.jsonl`。
- 15 个 in-scope query + 3 个 out-of-scope query。

**RAG / Agent 机制**：

- Top-k retrieval。
- 根据 top similarity score 决定回答或升级。
- Borderline query 走 hybrid rerank。
- 对 high similarity 但 unsupported term 的问题做 human escalation。
- 输出 sources + decision trace。

**明确指标**：

- `retrieval_hit@4`：labelled source 是否在 top-4。
- `grounding`：answer content words 是否出现在 retrieved context。
- escalation recall。
- out-of-scope handling。
- `eval/run_eval.py` 输出 `eval/report.md`。

**简历包装建议**：

做 **Support RAG Agent with Escalation Eval**。面试时讲：不是所有问题都回答；低置信度和知识库未覆盖问题必须升级人工。指标可以直接写 retrieval_hit@4、grounding、escalation recall。

## 2.2 [Kparos000/langgraph-ecommerce-agent](https://github.com/Kparos000/langgraph-ecommerce-agent)

**为什么值得看**：电商经营分析方向很适合简历，因为数据源真实、查询任务多样、业务指标明确。它用 LangGraph 做多 agent 编排，把自然语言转成 BigQuery SQL，并输出业务报告。

**数据来源**：

- Google BigQuery public dataset：`bigquery-public-data.thelook_ecommerce`。
- 主表包括 orders、order_items、products、users、events、distribution centers。

**RAG / Agent 机制**：

- Schema/context helper。
- Intent reasoning。
- Sub-agents：segmentation、trends、geo analytics、product performance。
- SQL generation。
- SQL validation。
- BigQuery execution。
- Synthesis report。
- LangSmith trace。

**明确指标**：

- SQL validity >99%。
- Typical response <10s。
- pytest eval / unit tests。
- LangSmith trace: prompt、routing、SQL、validation、execution、synthesis 全链路可查。

**简历包装建议**：

做 **E-commerce BI Agent**：自然语言问 GMV、AOV、品类、地区、退货、用户分群。重点加 evaluation set：50 条业务问题，每条带 expected SQL pattern、expected source table、answer checker。

## 2.3 [jabbala10-bit/supportiq](https://github.com/jabbala10-bit/supportiq)

**为什么值得看**：它是 on-premise 客服 RAG 多 Agent，数据源非常清楚：SQL、Docs、Web 三路。适合包装成“企业内网客服 Agent”。

**数据来源**：

- MySQL：order status、account info、billing、inventory。
- ChromaDB + 8,000 PDF knowledge base：product specs、return policy、FAQ、manuals。
- DuckDuckGo / Tavily：live promotions、breaking updates。

**RAG / Agent 机制**：

- Adaptive Router。
- SQL Agent。
- RAG Agent。
- Web Agent。
- Hybrid retrieval：ChromaDB + BM25。
- Corrective RAG：质量差时 grade relevance 并 rewrite query。

**明确指标**：

- 8 秒 average response time。
- 94% retrieval precision on policy questions。
- 60% reduction in agent workload。

**简历包装建议**：

做 **On-prem Customer Support RAG**。强调本地部署、隐私、MySQL read-only、PDF policy RAG、Prometheus metrics。面试时可以讲“SQL 数据和政策文档为什么要分 agent”。

## 2.4 [databricks-solutions/agentic-customer-support](https://github.com/databricks-solutions/agentic-customer-support)

**为什么值得看**：这是企业级客服多 Agent 参考，虽然绑定 Databricks，但生产化思路强：Vector Search、tool-calling agents、MLflow Tracing、Agent Evaluation、Unity Catalog lifecycle。

**数据来源**：

- Synthetic telecom customer data。
- Customer profiles。
- Subscriptions。
- Knowledge base articles。
- Support tickets。

**RAG / Agent 机制**：

- Supervisor agent 编排 specialist agents。
- Account agent、billing agent、tech support agent、product agent。
- Vector Search 处理 unstructured KB。
- Tool-calling agents 处理 structured data retrieval。

**明确指标 / 评测体系**：

- Databricks Agent Evaluation。
- MLflow Tracing。
- Agent lifecycle tracked with MLflow and Unity Catalog。
- Unit tests + evaluation framework。

**简历包装建议**：

适合参考 **RAG Agent LLMOps**：把你的客服 Agent 接 MLflow traces，记录每次检索、工具调用、最终答案和评测分数。

## 2.5 [younus-alsaadi/Agentic-customer-support-copilot](https://github.com/younus-alsaadi/Agentic-customer-support-copilot)

**为什么值得看**：它做的是邮件客服，而不是网页聊天。业务闭环清楚：读邮件、查信息、生成草稿、人工审核、最终回复。

**数据来源**：

- Customer emails。
- Drafts / Messages outbound。
- PostgreSQL 业务状态。
- 示例 LangSmith traces 和 email screenshots。

**RAG / Agent 机制**：

- End-to-end email handling。
- Human-in-the-loop review。
- Provider-agnostic LLM。
- 支持本地 Hugging Face model。

**明确指标**：

- Ragas：answer correctness / faithfulness。
- API / agent latency。
- Tool duration。
- End-to-end case duration。
- Error rate。
- PostgreSQL metrics。
- p50 / p95 / p99 latency。
- README 目标：API p95 latency < 2s。

**简历包装建议**：

做 **Customer Email RAG Copilot**。加一个 labeled email set：订单咨询、退款、投诉、缺少验证信息。指标写 response faithfulness、draft acceptance rate、p95 latency、tool error rate。

## 2.6 [gsathishkumar/E-Commerce-MultiAgent-WithoutMCP](https://github.com/gsathishkumar/E-Commerce-MultiAgent-WithoutMCP)

**为什么值得看**：数据源边界特别清晰，适合做电商 RAG 架构参考。它由 orchestrator + 四个 backend 服务组成。

**数据来源**：

- Product catalog PDFs -> Product RAG。
- Refund / returns policy PDFs -> Refund Policy RAG。
- MongoDB orders -> Orders DB agent。
- MongoDB return/refund records -> Refunds DB agent。

**RAG / Agent 机制**：

- LangGraph workflow。
- LLM classifier 路由到四类 agent。
- Product catalog RAG。
- Refund policy RAG。
- Orders DB。
- Refunds DB。
- Synthesizer 输出最终回复。

**明确指标**：

- README 没有给出强数值指标，因此不列为最强 eval 候选。
- 但它返回 routing metadata，天然适合补 tool routing accuracy、policy citation correctness、refund API correctness。

**简历包装建议**：

如果你要做 CommerceOps Agent，可直接借它的数据源分层，但必须补评测：intent accuracy、entity F1、routing accuracy、policy citation correctness、API success rate。

## 2.7 [RafedAftab/agentic-customer-support-assistant](https://github.com/RafedAftab/agentic-customer-support-assistant)

**为什么值得看**：portfolio-ready MVP，业务材料完整，有 fake company、sample support docs、sample tickets、source citations、ticket dashboard。

**数据来源**：

- SwiftCart Electronics fake company docs。
- Markdown / text support documents。
- `sample_tickets/`。
- ChromaDB。

**RAG / Agent 机制**：

- Support docs chunking。
- Retrieval。
- Source-cited answer。
- Ticket triage。
- Category / priority / sentiment。
- Escalation decision。
- Draft reply。

**明确指标**：

- README 暂未给出硬指标。
- 但有 screenshots 和 sample tickets，适合作为 demo shell。

**简历包装建议**：

如果用它做参考，一定要补 eval dashboard：ticket category accuracy、priority accuracy、escalation recall、citation correctness、groundedness。

---

# 3. RAG Eval Harness：适合给你的业务 Agent 补指标

这些项目有些不是完整业务 agent，但非常适合借评测体系。真正做简历项目时，可以把它们的 eval harness 接到你的金融/客服/运维 Agent 上。

## 3.1 [SagnikKK1/rag-eval-harness](https://github.com/SagnikKK1/rag-eval-harness)

**数据来源**：

- Motorola Edge 50 Fusion user reviews。
- public scraped YouTube / Reddit corpus。
- Golden set：20 answerable + 6 not-in-corpus。

**机制**：

- Dense / sparse / hybrid retrieval。
- Cross-encoder rerank。
- Corrective RAG with LangGraph。
- Agent mode：LLM 决定调用 `search_corpus(query, k)` 和 `calculator(expression)`。
- 返回 tool-call trace + gathered chunks。

**明确指标**：

- `recall@1`、`recall@3`、`recall@5`、`recall@10`。
- MRR。
- refusal_acc。
- A/B comparison。
- CI regression gate。

**README 结果亮点**：

- Cross-encoder reranker：`recall@1` 0.45 -> 0.70。
- MRR 0.59 -> 0.76。
- Hybrid retrieval：`recall@3` 0.70 -> 0.90。
- CRAG 处理 not-in-corpus refusal。

**可借鉴点**：

用它给你的电商/金融 RAG 加 not-in-corpus 拒答评测。很多 RAG 项目只测能答的问题，拒答能力才是生产环境的坑。

## 3.2 [apoorva-01/rag-eval-harness](https://github.com/apoorva-01/rag-eval-harness)

**数据来源**：

- 15 篇 retrieval / RAG / embeddings arXiv papers。
- 50 个问题。
- exact page / section citations。

**机制**：

- Chat with research papers。
- Retrieval strategy matrix。
- Chunk x embedding config comparison。
- DeepEval。
- 自定义 citation-faithfulness metric。

**明确指标**：

- NDCG@5。
- Recall@5。
- MRR。
- Faithfulness。
- Answer relevance。
- Context precision。
- Context recall。
- Citation precision。
- Citation recall。

**README 结果亮点**：

- Naive dense -> hybrid + rerank：NDCG@5 0.33 -> 0.62。
- Recall@5 0.44 -> 0.76。

**可借鉴点**：

Citation precision / recall 很适合金融、法律、医疗 RAG。简历里能讲“不是只看答案对不对，还看引用是否真的支撑答案”。

## 3.3 [Akash-1512/rag-eval-harness](https://github.com/Akash-1512/rag-eval-harness)

**数据来源**：

- 20 篇 foundational AI/ML research papers。
- 10 个真实 Q&A pairs。

**机制**：

- RAGAS。
- DeepEval G-Eval。
- LangGraph adversarial red-team agent。
- MLflow tracking。
- PDF corpus upload。

**明确指标**：

- Faithfulness：0.933。
- Context Precision：0.778。
- Context Recall：1.000。
- Answer Relevancy：0.914。
- Answer Correctness：0.735。
- DeepEval faithfulness pass rate：0.667。
- DeepEval answer relevancy pass rate：1.000。

**可借鉴点**：

它最好的点是 red-team agent：能发现 RAGAS / DeepEval 不一定能发现的问题，例如时间版本攻击。适合给金融 RAG 加“过期信息/旧财报误用”测试。

## 3.4 [weijia-89/oncology-rag-lab](https://github.com/weijia-89/oncology-rag-lab)

**数据来源**：

- 8 条 base synthetic oncology notes。
- 12 条 adversarial edge-case notes。
- `data/gold_standard.csv`。
- `data/gold_standard_edge_cases.csv`。
- 可生成 100 / 500 条 synthetic notes 做 scale stress。

**机制**：

- LlamaIndex + Chroma。
- Ollama inference。
- Structured clinical entity extraction：cancer type、AJCC stage、regimen、ECOG。
- Arize Phoenix traces。
- DeepEval suite。

**明确指标**：

- Pass rate。
- Regression gate：pass rate drop >5% 失败。
- A/B model drift。
- top-1 chunk id drift。
- Ragas-style：faithfulness、answer relevancy、contextual precision、contextual recall。
- Stress eval latency / pass summary。

**可借鉴点**：

这是“高风险领域 RAG 如何做安全评测”的好模板。即使你不做医疗，也可以借它的 edge-case gold、drift compare、regression gate。

## 3.5 [jorgemosquera/llm-rag-evaluation-harness](https://github.com/jorgemosquera/llm-rag-evaluation-harness)

**数据来源**：

- MS MARCO v1.1 validation split from HuggingFace。
- 默认取前 500 queries with valid passages and answers。

**机制**：

- FAISS retrieval。
- GPT-4o-mini reranking。
- GPT-4o-mini generation。
- GPT-4o-mini faithfulness judge。

**明确指标**：

- Precision@5。
- Recall@5。
- MRR。
- NDCG@5。
- Lexical Token-Overlap F1。
- Faithfulness。
- Cost estimate by query count。

**可借鉴点**：

MS MARCO 是标准检索数据源，适合做你的 retriever baseline。尤其适合证明你不是只在自造小数据上跑通。

## 3.6 [Suraj370/rag-evaluation-harness](https://github.com/Suraj370/rag-evaluation-harness)

**数据来源**：

- 1,599 个 Kubernetes documentation pages。
- 50 个 human-curated questions。
- reference answers and source citations。

**机制**：

- Official documentation corpus ingestion。
- Chunking strategy comparison。
- Dense retrieval baseline。
- Metadata filtering。
- Reranking。
- Citation-aware grading。
- Failure analysis notebooks。

**明确指标**：

- Hit@5。
- MRR。
- Relevance。
- Citation correctness。
- Answer relevance。

**可借鉴点**：

如果你做运维/SRE RAG Agent，这是比金融/客服更贴近的评测参考。可以把 Kubernetes docs 换成 Linux runbook、Nginx docs、Prometheus docs。

## 3.7 [wzltmp/rag-eval-harness](https://github.com/wzltmp/rag-eval-harness)

**数据来源**：

- 28 篇 Paul Graham essays。
- 695 chunks。
- 30 hand-written Q&A pairs。

**机制**：

- pgvector。
- Vector search。
- Cross-encoder rerank。
- Claude Haiku LLM-as-judge。
- A/B/C eval。

**明确指标**：

- Accuracy。
- A/B/C config comparison。
- Judge variance discussion。

**README 结论亮点**：

- Rerank 在这个 corpus 上没帮上忙。
- 原因分析：小 corpus 中 top-20 vector search 已经包含 gold chunk，reranker 可修正空间小。

**可借鉴点**：

它的价值在于“报告诚实”：不是所有高级组件都有提升。简历项目里能写出失败分析，比只贴高分更像真实工程。

## 3.8 [pk1wastaken/glassbox-rag-evaluation-harness](https://github.com/pk1wastaken/glassbox-rag-evaluation-harness)

**数据来源**：

- 20 technical PDFs。
- 469+ benchmark questions。
- Bundled seed corpus。
- Benchmark CSVs。

**机制**：

- FAISS。
- Metadata-aware chunking。
- Adaptive retrieval depth。
- Optional reranking。
- Citation-rich answer generation。
- Streamlit exploration。

**明确指标**：

- Core benchmark。
- Semantic-collision benchmark。
- Cross-domain stress tests。
- Preferred chunk profile：800 / 200 over 900 / 250。
- Evaluation runner: `evaluate.py --csv_path ... --k ...`。

**可借鉴点**：

适合做“glass-box RAG”：让检索行为、chunking、latency、benchmark 结果都可视化，而不是藏在后端。

## 3.9 [phillipkaraya/rag-eval-harness](https://github.com/phillipkaraya/rag-eval-harness)

**数据来源**：

- Fictional B2B SaaS knowledge base。
- `data/corpus/*.md`。
- 20 support-style questions。
- `data/eval/questions.jsonl`，带 labeled relevant documents。

**机制**：

- BM25。
- TF-IDF。
- Dense embeddings optional。
- Hybrid RRF。
- Passage-level retrieval collapsed to doc-level scoring。

**明确指标**：

- recall@k。
- precision@k。
- MRR@k。
- nDCG@k。

**README 结论亮点**：

- Dense embeddings 在 semantic query 上明显胜出。
- Hybrid 是稳健默认，但不一定超过 dense。

**可借鉴点**：

非常适合给客服 RAG 做最小可复现 retrieval benchmark。没有 LLM 依赖，跑起来快，适合 CI。

## 3.10 [sophie-nguyenthuthuy/rag-eval-harness](https://github.com/sophie-nguyenthuthuy/rag-eval-harness)

**数据来源**：

- VN bank QA sample dataset。
- `data/corpus.jsonl`。
- `data/questions.jsonl`。

**机制**：

- OSS-only judge。
- FakeJudge for CI。
- OllamaJudge for local judge。
- A/B compare。
- Regression gate。
- Per-stage latency logging。

**明确指标**：

- Retrieval：recall@k、precision@k、MRR、nDCG@k、context_precision@k。
- Generation：faithfulness、answer_relevance、answer_correctness。
- Latency：retrieve_ms、generate_ms、ttft_ms、total_ms、p50/p95/p99。

**可借鉴点**：

如果你想强调“本地可跑、无 API 也能 CI”，这是很好的参考。

## 3.11 [darrshangovender/rag-eval-harness](https://github.com/darrshangovender/rag-eval-harness)

**数据来源**：

- `data/golden.yml` labelled question set。
- baseline toy RAG pipeline。

**机制**：

- Pipeline contract。
- Faithfulness judge。
- Retrieval recall@k。
- Regression report。
- CI workflow。

**明确指标**：

- Faithfulness target ≥ 0.90，README 示例 0.94。
- Answer relevance target ≥ 0.85，README 示例 0.91。
- Retrieval recall@5 target ≥ 0.80，README 示例 0.87。
- Latency p50 / p95。
- Cost per question。

**可借鉴点**：

适合直接借“阈值门禁”写法：PR 改了 prompt、chunking、embedding，如果指标下降就 fail。

## 3.12 [Akshitha024/rag-quality-evaluator](https://github.com/Akshitha024/rag-quality-evaluator)

**数据来源**：

- JSONL samples：`qid, question, answer, contexts, gold, citations`。
- tests fixtures synthetic JSONL。

**机制**：

- Heuristic judge。
- LLM judge。
- Drift detection。
- Welch's t-test。
- Six chart types。

**明确指标**：

- Faithfulness。
- Answer relevance。
- Citation grounding。
- Context precision。
- Context recall。
- Answer correctness。
- Drift detection metric deltas。

**可借鉴点**：

适合做 RAG eval dashboard：不仅输出表格，还输出分布图、漂移图、校准散点图。

---

# 4. 建议你怎么包装成简历项目

## 方案 A：FinRAG Audit Agent

**定位**：面向 SEC filings 的金融投研 RAG Agent，强调证据可追溯和指标评测。

**数据来源**：

- SEC EDGAR 10-K / 10-Q。
- Apple / Microsoft / Nvidia filings。
- companyfacts JSON。
- yfinance 行情。

**核心模块**：

- Filing ingestion：HTML/PDF -> section tree -> table cell chunks。
- Hybrid retrieval：BM25 + dense vector + RRF。
- Evidence selector：定位 section / page / table row / cell。
- Calculator tool：同比、环比、margin、P/S、growth。
- Memo generator：bull/base/bear case + risk factors + citations。
- RAGAS / custom eval：faithfulness、context_precision、citation precision、cell hit rate。

**指标**：

- Retrieval Recall@5。
- Context Precision。
- Faithfulness。
- Citation Precision / Recall。
- Cell Hit Rate。
- Calculation Accuracy。
- p95 latency。
- token cost per memo。

## 方案 B：Commerce Support RAG Agent

**定位**：电商客服/售后 RAG Agent，回答订单、退款、政策、商品问题，并能升级人工。

**数据来源**：

- Product catalog PDFs。
- Refund / returns policy PDFs。
- Orders API / MySQL。
- Refund API / MongoDB。
- Sample tickets。
- Out-of-scope query set。

**核心模块**：

- Intent router。
- Entity extractor。
- SQL/DB agent。
- Product RAG agent。
- Refund policy RAG agent。
- Human escalation agent。
- PII-safe trace logger。
- Evaluation harness。

**指标**：

- Intent accuracy。
- Entity F1。
- Retrieval hit@4。
- Grounding。
- Policy citation correctness。
- Escalation recall。
- Out-of-scope refusal accuracy。
- API success rate。
- p95 latency。

## 方案 C：Ops Knowledge RAG Agent

**定位**：面向 Linux/SRE runbook 和官方文档的运维知识 RAG Agent，用于故障排查建议与 runbook 推荐。

**数据来源**：

- Kubernetes docs。
- Nginx docs。
- Prometheus docs。
- Linux man pages。
- 自建 incident/runbook corpus。
- Docker chaos scenario reports。

**核心模块**：

- Docs ingestion。
- Runbook retrieval。
- Incident query rewriting。
- Tool recommendation。
- RCA report generator。
- Evaluation harness。

**指标**：

- Hit@5。
- MRR。
- nDCG@5。
- Runbook match accuracy。
- RCA citation correctness。
- unsafe suggestion rate。
- p95 latency。

---

# 5. 最终推荐排序

| 排名 | 推荐项目方向 | 参考项目 | 理由 |
|---:|---|---|---|
| 1 | 金融 SEC RAG Agent | `RAGAS-FINANCE` + `Financial-Analyst-Agent-RAG-LangGraph` | 数据来源权威，指标清楚，业务含金量高 |
| 2 | 电商客服 RAG Agent | `genai-support-assistant-rag` + `supportiq` + `E-Commerce-MultiAgent` | 最容易做成完整前后端 demo，业务流程好讲 |
| 3 | 电商 BI Agent | `langgraph-ecommerce-agent` | BigQuery public dataset 真实，SQL validity/latency/trace 都能讲 |
| 4 | RAG Eval Platform | `SagnikKK1` + `apoorva-01` + `Akash-1512` | 可以作为任何 RAG Agent 的评测底座 |
| 5 | 医疗/高风险 RAG Lab | `oncology-rag-lab` | 安全、回归、漂移、合成 gold set 的工程意识很强 |

