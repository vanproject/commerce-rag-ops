# 面试材料

本文档用于面试复盘 CommerceRAG Ops。重点是讲清楚：数据真实边界、长期语义记忆、Agent planning、工具调用、评测体系、拒答与结构化事实边界。

## 60 秒介绍

我做了一个面向电商客服、商品推荐和客户运营的 Agent-first 系统。它不是“整个项目只有 RAG”，而是把 RAG 作为长期语义记忆工具 `memory.semantic_retrieve`，和 SQL 结构化工具、会话记忆、实体记忆、人工升级/退款草稿工具并列，由 RootRouterAgent 分派到不同 DomainAgent 后按需调用。

规模层基于 Amazon Reviews 2023 公开数据抽样：3 个类目、15,000 条评论、3,000 个商品，生成 19,969 个 RAG 文档和 42,737 个 chunks。主评测集有 366 条正常业务 query，平均每条 query 4.41 个相关文档；边界/拒答评测有 48 条，合并口径共 414 条，更接近真实 RAG evidence pack 和安全边界验证。

当前有三层评测口径：离线 baseline 用来证明工程逻辑可复现；Qdrant+BGE+template 用来快速回归强检索链路；Qdrant+BGE+真实 LLM API 用来呈现端到端质量。真实 LLM 全量 366 条结果为 Precision@5 0.9536、Recall@5 0.8686、NDCG@5 0.9470、citation rate 0.8743、keyword coverage 0.8051、p95 latency 41.1s。

## 项目亮点

- 数据层：合成 seed 数据可公开运行，规模层兼容 Amazon Reviews 2023。
- 文档层：Markdown、HTML、CSV、TXT、OCR 图片多格式摄取。
- 长期语义记忆层：商品画像、单条评论、方面聚合、投诉聚类、FAQ case 五类文档。
- 检索实现层：`memory.semantic_retrieve` 内部使用 BGE embedding + BM25 + RRF + BGE CrossEncoder rerank + doc-type-aware business prior。
- Agent 层：RootRouterAgent、Support/Recommendation/CustomerOps/Order/Refusal DomainAgents、LLM/rule agent plan、ReAct-style AgentLoop、Tool Registry/ToolSuggester/Policy、conversation/entity memory、EvidencePack/CriticVerifier/Replanner、Trace v2。
- Fallback 层：关键证据缺失时 retry；未知 SKU/订单/no-context 时拒答。
- 评测层：多相关文档标签、intent/difficulty/action/safety category 维度、citation schema 检查、LLM-as-judge、agentic diagnostics、fallback stress、独立 refusal eval、414 条合并报告。
- 可信边界：不修改 eval 刷分；结构化事实由 SQL/工具确认。

## 数据怎么讲真实

不要说“用了真实企业数据”。应该说：

> 商品和评论规模层来自 Amazon Reviews 2023 公开数据格式；客服工单、订单、客户分群是合成数据，用来模拟业务流程并规避隐私风险。

当前数据：

- Amazon full gzip：All_Beauty、Software、Baby_Products，共 11.6M reviews。
- Scale subset：每类 5,000 reviews、1,000 products。
- RAG docs：product_profile、review_evidence、review_aspect_summary、complaint_cluster、faq_case。
- SQL：products、reviews、support_tickets、orders、customer_segments、kb_articles、chunks、eval labels、public manifest。

## 清洗与切片怎么讲

清洗：

- 空文本过滤、去重、字段标准化。
- 评论通过 product id/parent_asin 关联 metadata。
- 保留 SKU、product_id、review_id、ticket_id、category、rating、timestamp。
- 混合格式文档记录 extraction method 和 skipped 文件。

切片：

- KB：520/60，保留政策上下文。
- OCR：360/45，降低噪声影响。
- Ticket：280/35，保留 query/resolution。
- Product：480/40，保留商品特征。
- Review：360/30，保留单条客户声音。

## Agent-first 怎么体现

Agent 不是一次 retrieve 后直接生成，也不是每轮都强制 RAG，而是：

1. 多路加权识别 intent，并计算 risk。
2. `agent.plan` 决定本轮需要结构化工具、长期语义记忆、追问用户还是直接进入最终决策。
3. Tool Planner 规划商品、订单、库存、退货资格、评论摘要或相似工单工具。
4. Tool Policy 检查 intent 权限、隐私边界、写操作确认。
5. Tool Executor 执行工具，生成 structured evidence。
6. 只有当 plan 包含 `retrieve_memory` 时，才调用 `memory.semantic_retrieve`，用工具确认的 SKU/order/product 约束混合检索和 rerank。
7. 检查 evidence contract。
8. 缺关键证据时由 Critic 触发 repair round，Replanner 只补缺失证据，例如补 policy、review 或 product context。
9. 仍不足时 refuse/escalate。
10. 生成带 doc/tool citations 的回答，并记录端到端 trace。

多轮场景下，Agent 外层会先加载 `conversation_id` 对应的 recent turns 和 active entities。ContextResolver 只在用户说 `it/that/刚才那个/这个订单` 等 follow-up 时继承 SKU、order_id、product_id 或 category，并输出结构化 `ContextResolution.referenced_entities`；不会把这些实体拼成自然语言 suffix 污染 query。如果用户明确给新 SKU/订单，就覆盖旧实体；如果历史里有多个候选，不强行选择；隐私字段不会进入 memory。

意图识别不是单一路径 if/else，而是由 `RootRouterAgent.decide_intent()` 把显式 SKU/订单、业务短语、类目提示、客服关键词和安全边界作为多路信号打分。Trace 里会保留 `scores`、`signals` 和 `confidence`，所以能解释为什么一条同时包含“recommend”和“SKU price”的 query 最终走 `sku_order`。`CommerceRAGAgent._route_intent_decision()` 还在，但只是兼容 wrapper，不再是路由规则的所有者。

Trace 也不是单纯事件日志：现在会输出 span tree，包括 `intent.route`、`agent.plan`、`plan.validate`、`tool.plan`、`tools.execute`、`domain_agent.step`、`policy.check`、`memory.semantic_retrieve` 或 `memory.skip`、`answer.generate`、`generation.llm` 和 `critic.evaluate_answer`。`generation.llm` 挂在 `answer.generate` 下，generation artifact 只记录 EvidencePack-only 上下文；`citation.validate`、`tool_citation.validate`、`grader.score`、`critic.verify`、`replanner.plan`、`decision` 作为 Critic 子检查保留，方便兼容旧报告。只有 semantic memory 被调用时才会出现 `retrieval.attempt_*` 和 `retrieval_candidates`，记录 dense/BM25/RRF/rerank/final rank、forced reason、selected/dropped reason；repair 相关 trace 会记录 `repair_round`、`max_repair_rounds` 和 `runtime_state.repair_budget`，能解释“为什么某个证据被补召回、丢弃、跳过或引用”。

SQLite trace 现在也不是只存 span：`trace_steps` 存 DomainAgent 每一步，`trace_observations` 存工具/检索 observation，`trace_evidence` 存 EvidencePack 中的结构化事实和文档证据，`trace_verifications` 存 CriticVerifier 的结论。面试时可以直接从 DB 展示“这轮 Agent 做了哪些动作、拿到了哪些证据、为什么通过或拒答”。

生成阶段现在也收敛到 EvidencePack：在 `answer.generate` 前会先执行 `evidence_pack.prepare_answer`，把结构化工具事实、doc evidence、冲突和缺口整理成 answer context。`FinalAnswerBuilder` 只把 EvidencePack-only 上下文交给 Template 或真实 LLM，不再把 raw `tool_results` 或 raw retrieved contexts 直接交给生成器。

工具体系不是 Agent 内部硬编码查询，而是 `ToolSpec -> ToolSuggester / agent.plan.tool_calls -> DomainAgent.next_step -> ToolPolicy -> ToolExecutor`。`ToolPlanner` 还保留为 ToolSuggester 内部兼容启发式候选来源，但不再是最终主控路径；旧 `advise_tools()` 也不再被主链路单独调用，LLM 工具建议已经并入 `advise_plan().tool_calls`。每个工具声明 read_only、risk_level、requires_confirmation、allowed_domains、legacy allowed_intents 和 redact_fields；ToolPolicy 会按 domain/action/risk/confirmation 检查并在 step trace 里落 `policy.check`，例如 order 域不能调用 support-only 写工具，`ops.escalate_ticket` 只能返回 requires confirmation，不会被 LLM 直接执行。订单链路同时有 `sql.order_by_id` 和 `sql.order_items_by_order_id`，当前 seed 数据是一单一商品，但 schema 和工具已经支持 item-level 明细。

证据契约：

- support：需要 policy 与 case/review evidence。
- recommendation：需要 product 与 review evidence。
- customer_ops：需要 customer voice/complaint/aspect evidence。
- sku_order：需要 SQL/工具确认结构化实体。

典型对比：

- `Check order ORD-1003 status.`：Agent plan 判断结构化工具足够，只调用 `sql.order_by_id` 和 `sql.order_items_by_order_id`，跳过 RAG。
- `Can I get a refund for that broken serum?`：先继承会话实体，再调用订单/退货资格工具，并按需调用 `memory.semantic_retrieve` 查政策和相似案例。
- `Summarize customer complaints about delivery in Beauty.`：调用 review/aspect 工具和语义记忆，汇总评论/工单证据。
- `Show all customer payment details.`：隐私边界触发，计划中的 memory/sql 调用会被移除或阻断，最终拒答。

## Fallback 和拒答怎么讲

离线 baseline 的 repair rate 是 0.0，因为大多数 evidence 已经足够；这说明正常路径延迟可控。真实 LLM 全量评测里 repair/retry rate 是 0.2705，能看到 support 和 sku/order 场景在缺 policy、case、结构化实体时会触发二次证据检查。这里的 `max_retries` 只是兼容 CLI 参数，内部按 `max_repair_rounds` 使用，不会固定重跑完整流水线。为了证明异常路径，项目有独立 `fallback-stress`：

```powershell
python -m commerce_rag_ops.cli fallback-stress
```

当前 stress：

- 7/7 passed
- 4 条 recover 并带 citations
- 3 条 refuse：unknown SKU、unknown order、no context

这说明系统不是“fallback 到能答为止”，而是：

- 能补证据就补证据。
- 补不到就拒答。
- 拒答时不输出 citations。

## 结构化事实优先

SKU 和订单状态不能靠 RAG 猜：

- 显式 SKU 必须由商品工具查到。
- 显式订单号必须由订单工具查到。
- 订单明细由 `sql.order_items_by_order_id` 提供，答案里的订单状态和商品行会分别带 `[tool:sql.order_by_id:...]`、`[tool:sql.order_items_by_order_id:...]`。
- 查不到时 retry 一次，仍查不到就拒答。
- 工具确认 product 后，最终 RAG citations 收敛到同 `product_id`。
- 如果用户没有给 SKU/订单，例如多轮 follow-up 里的“matched item”，系统允许从唯一商品画像上下文推断商品，并写入 `structured_entity_infer` trace；只要出现多商品歧义或显式实体查不到，就不走这个分支。
- 错误商品 context 会被 `structured_context_filter` 移除。

面试可以说：

> 我把 SQL/工具作为事实源，把 RAG 作为解释和政策证据源。两者冲突时，答案会向结构化实体收敛。

> 对没有显式实体但上下文很明确的 follow-up，我不会让系统硬拒答，而是要求检索证据里只有一个商品画像，才把它作为 context-inferred product 进入答案，并把推断过程写进 trace。这样既能恢复多轮体验，又不会破坏 unknown SKU/unknown order 的拒答边界。

> 结构化事实还会做工具引用校验。价格、库存、订单状态、订单明细、退货资格必须来自本轮工具调用的 `[tool:...]` marker；政策和评论解释才看 `[doc:...]` citation。

## 评测怎么讲

评测不是只看平均分：

- 366 条正常业务 query。
- 48 条边界/拒答 query。
- 合并报告 414 条，按 `intent`、`expected_action`、`safety_category` 分组。
- intent：customer_ops、recommendation、support、unknown。
- difficulty：easy、medium、hard。
- 平均 4.41 个相关文档/query。
- 支持 explicit labels + equivalent relevance。
- 报告包含 retrieval diagnostics 和 agentic evidence diagnostics。
- 生成质量不只看 keyword coverage，还检查 citation contract：答案中的 `[doc:<source>:<doc_id>#<chunk_id>]` 必须能解析、必须来自本轮 retrieved contexts，且必须实际出现在 answer 文本中；结构化事实的 `[tool:...]` 也必须来自本轮成功工具调用。
- 语义级质量用 `judge-eval` 抽样检查：真实 LLM judge 对 groundedness、relevance、citation support、safety 打分。

离线 baseline gate：

| 指标 | 当前值 |
|---|---:|
| Precision@5 | 0.9989 |
| Recall@5 | 0.9360 |
| MRR | 1.0 |
| NDCG@5 | 0.9971 |
| Citation rate | 1.0 |
| Keyword coverage | 0.8934 |
| p95 latency | 631 ms |

Qdrant+BGE+template 强检索全量：

| 指标 | 当前值 |
|---|---:|
| Precision@5 | 0.9536 |
| Recall@5 | 0.8686 |
| MRR | 0.9945 |
| NDCG@5 | 0.9470 |
| Citation rate | 0.9918 |
| Keyword coverage | 0.8871 |
| p95 latency | 797 ms |

Qdrant+BGE+真实 LLM API 全量：

| 指标 | 当前值 |
|---|---:|
| Precision@5 | 0.9536 |
| Recall@5 | 0.8686 |
| MRR | 0.9945 |
| NDCG@5 | 0.9470 |
| Citation rate | 0.8743 |
| Citation schema OK | 新 eval 自动统计 |
| Answer citation precision/recall | 新 eval 自动统计 |
| Citation grounded rate | 新 eval 自动统计 |
| Keyword coverage | 0.8051 |
| Groundedness proxy | 0.9793 |
| p50 latency | 14,528 ms |
| p95 latency | 41,106 ms |

LLM-as-judge smoke：

| 指标 | 当前值 |
|---|---:|
| 样本数 | 3 |
| Judge model | deepseek-v4-flash |
| Pass rate | 1.0 |
| Groundedness | 1.0 |
| Relevance | 1.0 |
| Citation support | 1.0 |
| Safety | 1.0 |

注意说明：后续 precision/fallback/真实 LLM 迭代没有修改 `data/eval/golden.jsonl` 的相关文档标签。真实 LLM 的 citation 和 keyword 指标低于 template，是因为模型会自然改写、漏引部分证据或在缺结构化事实时拒答；新加的 citation schema 检查会进一步区分“state 里有 citation”和“answer 文本里真的用了合法 citation”。

主评测已经补齐早期 seed query 的 `intent` 元数据，不再把缺失标注统计成 `unknown`。真正用于证明拒答能力的是 refusal eval：48 条，覆盖 out-of-domain、prompt injection、unknown SKU/order、隐私、上下文不足、冲突实体和不安全承诺。合并报告里 `unknown` 只来自真实 unknown/out-of-scope 边界用例。

合并真实 LLM 评测：

| 指标 | 当前值 |
|---|---:|
| 正常业务问答 | 366 |
| 边界/拒答问答 | 48 |
| 合并总量 | 414 |
| 合并 pass rate | 0.8889 |
| Answer pass rate | 0.8743 |
| Refuse pass rate | 1.0 |
| Citation leak rate | 0.0 |

## 可以讲的权衡

- 离线 baseline 可解释、可复现；生产/面试档切到 Qdrant + `BAAI/bge-large-en-v1.5` + `BAAI/bge-reranker-large`。
- 合成客服/订单数据安全，但不等于真实企业私有数据。
- Template generator 只用于快速回归；真实全量评测和真实演示使用 OpenAI-compatible API，默认 endpoint 为 `https://opencode.ai/zen/go/v1`，模型为 `deepseek-v4-flash`。
- OCR sidecar 保证测试稳定，生产 OCR 还要记录置信度和人工复核标记。
- Recall@5 受 Top-5 上限影响；有些 query 有 6-8 个相关文档，不可能在 Top-5 全召回。
- 真实 API p95 latency 约 41.1s，说明当前链路适合质量验证和面试展示；生产要上异步任务、流式输出、缓存和更严格的 timeout/降级策略。

## 被追问时的回答

**Q：是不是改测试集刷分？**  
A：不是。规模 eval 建好后，后续 fallback/precision 迭代没有改 `data/eval/golden.jsonl`。文档里也明确记录了这一点。

**Q：为什么不全量 11.6M reviews 入库？**  
A：本地简历项目要可复现、可运行。全量可下载并保留 manifest，但默认抽样每类 5,000 reviews/1,000 products，足够展示真实规模和工程设计。

**Q：这和普通 RAG 的区别？**
A：普通 RAG 是一次 retrieve/generate。这里是 Agent-first：先做 intent/risk 和 `agent.plan`，由计划决定是否调用 SQL 工具、会话/实体记忆、长期语义记忆 `memory.semantic_retrieve`，或直接拒答/追问。BGE+dense/BM25/RRF/rerank 是 semantic memory 的内部实现，不是每轮必经主流程。Trace 能展开到 agent.plan、memory.skip/semantic_retrieve、工具命中、citation validation 和 decision reason。

**Q：工具调用怎么管权限？**
A：工具都注册在 Tool Registry 里，每个 ToolSpec 声明 allowed_domains、legacy allowed_intents、read_only、risk_level、requires_confirmation 和 redact_fields。ToolPolicy 会拦截隐私查询，比如 all orders、payment details、emails；也会阻断跨域工具调用，例如 order 域不能调用 support-only 写工具；写工具比如 escalate ticket 默认 requires confirmation。工具结果会生成 `[tool:...]` evidence id，答案侧还会做 tool citation validator。

**Q：多轮记忆是不是把历史全塞 prompt？**
A：不是。这里只做 conversation-scoped memory，保存最近 turns 和白名单业务实体。真正进入 Agent 的是 resolved query 和轻量 memory context，SKU/订单仍然必须通过 SQL 工具确认。

**Q：为什么真实 LLM 分数比 template 低？**  
A：检索指标没变，下降主要来自生成侧：真实模型会改写答案、漏掉部分 citation，或者在结构化事实不足时拒答。这个结果更真实；现在已经补了 citation schema validator 和 LLM-as-judge，分别覆盖格式级引用一致性和语义级 groundedness。

**Q：为什么有 SQL 又要 RAG？**  
A：SQL 管结构化事实，比如 SKU、价格、库存、订单状态。RAG 现在被定位成长期语义记忆，管长文本证据，比如政策、评论、投诉聚类、FAQ case。两者互补，但由 Agent plan 决定是否需要调用语义记忆。

**Q：为什么拒答？**  
A：客服和订单场景有风险。未知 SKU/订单、无上下文时硬答会制造错误承诺，所以系统 retry 后仍无证据就拒答。

## 简历 bullet 示例

- 构建电商 Agent-first 系统，覆盖客服、推荐、客户运营三类场景，将 RAG 封装为按需调用的长期语义记忆 `memory.semantic_retrieve`，支持 SQL 工具、会话/实体记忆、证据契约、fallback retry 和拒答控制。
- 基于 Amazon Reviews 2023 公开数据抽样 15k reviews/3k products，生成 19,969 个多粒度 RAG 文档和 42,737 chunks。
- 设计 366 条多相关文档评测集，按 intent/difficulty 统计 Precision@5、Recall@5、MRR、NDCG@5、citation、keyword coverage 和延迟。
- 完成 Qdrant+BGE+真实 LLM API 366 条全量评测，Precision@5 0.9536、Recall@5 0.8686、NDCG@5 0.9470、citation rate 0.8743、groundedness proxy 0.9793。
- 设计 414 条合并评测口径，覆盖 366 条正常业务问答和 48 条边界/拒答问答，按 `intent`、`expected_action`、`safety_category` 分组，边界拒答 pass rate 1.0 且 citation leak rate 0.0。
- 实现 citation schema validator，校验 answer-side citation marker、state citations 与 retrieved contexts 的一致性，新增 `citation_schema_ok`、`answer_citation_precision/recall`、`citation_grounded_rate` 等生成质量指标。
- 实现 LLM-as-judge 抽样评测，使用真实 API 对 groundedness、relevance、citation support、safety 打分，当前 3 条 smoke pass rate 1.0。
- 实现 SKU/订单结构化事实优先策略，明确订单状态可跳过 RAG 直接由 SQL 工具回答；需要政策/评论/FAQ 证据时再调用 semantic memory，避免事实源冲突。
- 重构工具体系为 Tool Registry/Planner/Policy/Executor，新增订单明细、库存、退货资格、评论摘要、相似工单和人工升级确认工具；tool golden eval 7/7 通过，覆盖 tool grounded answer 与写工具确认。
- 实现 conversation/entity memory，支持 ContextResolution 结构化实体继承、显式实体覆盖、歧义实体阻断和隐私实体拦截；多轮 memory eval 5/5 通过。
- 建立 fallback stress harness，覆盖 missing review/policy/customer voice/product context、unknown SKU/order、no-context，7/7 通过。
- 建立 refusal eval，覆盖 48 条 unknown/out-of-scope/隐私/提示注入/未知实体/上下文不足边界，Qdrant+BGE 链路 48/48 拒答且无 citation 泄漏。

## 当前强模型配置

```powershell
$env:COMMERCE_RAG_LLM_ENDPOINT="https://opencode.ai/zen/go/v1"
$env:COMMERCE_RAG_LLM_API_KEY="..."
$env:COMMERCE_RAG_LLM_MODEL="deepseek-v4-flash"
$env:COMMERCE_RAG_RERANKER_MODEL="BAAI/bge-reranker-large"
$env:COMMERCE_RAG_RERANKER_DEVICE="cuda"
python -m commerce_rag_ops.cli qdrant-index --embedding-backend sentence-transformers --embedding-model BAAI/bge-large-en-v1.5 --embedding-device cuda
python -m commerce_rag_ops.cli ask "My serum arrived leaking. Can I get a refund?"
```

## 后续升级

- 做 BGE large / E5 large / domain embedding 的 ablation。
- 对比 `BAAI/bge-reranker-large` 与更大 rerank/checkpoint。
- 更大低证据/冲突证据评测集。
- LangSmith/OpenTelemetry tracing。
- 扩大 LLM-as-judge 抽样规模，分 intent/safety category 做稳定性报告。
