# Agent-first 能力矩阵

本文档对应简历包装时常被追问的 Agent / Agentic RAG 能力点。当前项目主体是电商客服/客户运营 Agent；RAG 是长期语义记忆工具，不是每轮必经主流程。

| 能力 | 状态 | 当前实现 | 主要证据 |
|---|---|---|---|
| Hybrid retrieval action | 已实现 | 本地链路：dense token cosine + BM25 + RRF + rerank；Qdrant 链路：BGE dense candidates + BM25 candidates + RRF + BGE CrossEncoder rerank。 | `src/commerce_rag_ops/retrieval.py`, `src/commerce_rag_ops/retriever_backends.py`, `reports/strong_model_full_llm_eval_report.md` |
| Agent Planner | 已实现 | 每轮先生成 `agent.plan`，决定是否直接依赖结构化工具、是否调用长期语义记忆、是否进入最终动作判断。LLM 可通过 `advise_plan()` 提建议，规则 planner 负责 fallback，计划会记录 accepted/rejected reason。 | `src/commerce_rag_ops/advisor.py`, `CommerceRAGAgent._rule_agent_plan`, `_merge_agent_plan`, `tests/test_core.py::test_agent_first_planner_can_skip_semantic_memory_for_order_status` |
| Router / Domain Agents | 已实现 | 新增 `RootRouterAgent`，weighted intent signals 和 safety boundary 由 `RootRouterAgent.decide_intent()` 生成，再收敛为 support/recommendation/customer_ops/order/refusal domain；新增五个 DomainAgent，分别声明 allowed tools、evidence contract、规则式 plan 和 observation-aware `next_step()`。 | `src/commerce_rag_ops/agents/`, `tests/test_core.py::test_root_router_owns_intent_signals_and_domain_mapping`, `tests/test_core.py::test_router_domain_evidence_pack_and_critic_are_recorded`, `tests/test_core.py::test_domain_agent_selects_next_step_from_observations_and_suggestions`, `docs/agent_runtime_refactor.md` |
| ReAct-style AgentLoop | 已实现 | 通过 `AgentLoop.run_agent()` 调用 `DomainAgent.next_step()`，DomainAgent 基于 `RunState.observations`、`action_suggestions` 和 `semantic_memory_request` 逐步选择 SQL/业务工具和 `memory.semantic_retrieve`；`AgentStepExecutor` 负责 `domain_agent.step`、`policy.check`、工具执行和 observation 记录；runtime_state 记录 steps、observations 和 step/tool/retrieval/write draft budgets。固定 `max_retries + 1` 循环已替换为 Critic/Replanner 驱动的 repair budget loop。 | `src/commerce_rag_ops/runtime/loop.py`, `src/commerce_rag_ops/runtime/executor.py`, `CommerceRAGAgent._run_domain_step_loop`, `tests/test_core.py::test_runtime_step_loop_records_observations_and_budgets`, `tests/test_core.py::test_agentic_evidence_contract_retries_missing_review` |
| EvidencePack / Critic / Replanner | 已实现 | 工具结果和语义记忆结果会归一进 EvidencePack；EvidenceGapAnalyzer 产出缺口；CriticVerifier 输出 passed/action/missing evidence/citation errors/tool fact errors/safety errors/repair hints，并通过 `decide_action()` 产出最终动作；Replanner 将缺口转成 repair steps，只有 Critic 要求 retry 且 repair budget 允许时才进入下一轮补证据。`_grade()` 仍作为 proxy 指标兼容层保留。 | `src/commerce_rag_ops/evidence/`, `CommerceRAGAgent.run`, `docs/agent_runtime_refactor.md` |
| EvidencePack-driven Answer | 已实现 | 生成前先执行 `evidence_pack.prepare_answer`；`FinalAnswerBuilder` 负责 `answer.generate -> generation.llm`，并只构造 EvidencePack-only generation artifact；Template/LLM 生成器通过 `build_answer_context()` 读取 EvidencePack 中的 structured facts、doc evidence、conflicts 和 missing requirements。OpenAI-compatible prompt 不再传 raw `tool_results`、raw retrieved `contexts` 或 `retrieval_plan`。 | `src/commerce_rag_ops/runtime/final_answer.py`, `src/commerce_rag_ops/generator.py`, `CommerceRAGAgent.run`, `tests/test_core.py::test_answer_generation_uses_evidence_pack_context` |
| Semantic Memory Tool | 已实现 | RAG 被封装成只读 ToolSpec `memory.semantic_retrieve`，只在 Agent plan 需要外部知识、政策、评论、FAQ、相似工单时调用；在 ReAct loop 中作为普通 `tool_call` step 由 DomainAgent 选择，执行经过 ToolExecutor/ToolPolicy，返回后以 retrieval observation 记录 `memory_type=semantic_long_term`、doc citations、retrieval diagnostics。明确订单状态等强结构化问题可跳过 RAG。 | `src/commerce_rag_ops/tools/retrieval_tools.py`, `CommerceRAGAgent._execute_semantic_memory`, `AgentState.memory_reads`, `tests/test_core.py::test_agent_first_planner_calls_semantic_memory_when_needed` |
| Tool Registry / Tool Policy | 已实现 | 原 `_run_tools` 硬编码逻辑已重构为 Tool Registry + ToolSuggester + Policy + Executor；`ToolPlanner` 保留为兼容启发式候选来源，不再作为最终主控路径。ToolSpec 声明 `allowed_domains`、legacy `allowed_intents`、read/write、risk、confirmation 和脱敏字段；AgentLoop 执行工具时会把 domain/action/risk 传入 ToolPolicy，并在每个工具 step 下记录 `policy.check` span；跨域工具调用、隐私查询、大额退款和未确认写操作都会被阻断或要求确认。支持商品、订单、订单明细、库存、退货资格、评论摘要、相似工单、人工升级确认占位；工具结果先于检索执行，并反向约束 retrieval query。 | `src/commerce_rag_ops/tools/`, `src/commerce_rag_ops/tool_eval.py`, `data/eval/tool_golden.jsonl`, `reports/tool_eval_report.md`, `docs/tool_refactor_journey.md`, `tests/test_core.py::test_tool_policy_uses_domain_action_and_risk_context` |
| LLM Advisor | 已实现 | 真实 LLM 可参与 intent routing、agent planning、final action 建议；工具选择已经内联到 `advise_plan().tool_calls`，由 `DomainAgent.next_step()` 消费，旧 `advise_tools()` 仅兼容保留。规则路由、ToolPolicy、evidence gate 和 citation validators 最终兜底。LLM 可以建议人工升级或退款申请草稿，但写操作必须用户确认，大额退款会被 ToolPolicy 阻断。 | `src/commerce_rag_ops/advisor.py`, `CommerceRAGAgent._merge_route_decision`, `_merge_agent_plan`, `_merge_tool_plan`, `_merge_action_decision`, `tests/test_core.py::test_llm_advisor_can_steer_intent_tools_and_action_with_policy_guardrails`, `docs/llm_advisor_design.md` |
| Query expansion / HyDE | 部分实现 | 已实现 synonym query expansion 和 retry-time query enhancement；不是完整 HyDE 生成式假设文档。失败/缺证据时会根据 gap 注入 policy/review/product/customer voice 等召回词。 | `src/commerce_rag_ops/text.py`, `CommerceRAGAgent._enhance_query`, `reports/fallback_stress_report.md` |
| Weighted intent routing | 已实现 | 路由不再是单一路径 if/else，而是把结构化实体、业务短语、类目提示、客服关键词和安全边界作为多路信号加权打分，并把 scores/signals/confidence 写入 trace；weighted signals 已迁入 `RootRouterAgent.decide_intent()`，`CommerceRAGAgent._route_intent_decision` 只保留兼容 wrapper；LLM advisor 可作为候选信号覆盖普通业务路由，但不能覆盖 safety boundary。 | `src/commerce_rag_ops/agents/root_router.py`, `CommerceRAGAgent._merge_route_decision`, `docs/intent_trace_design.md`, `docs/llm_advisor_design.md` |
| Conversation / Entity Memory | 已实现 | 新增 conversation-scoped SQLite memory：保存 recent turns 和安全业务实体；ContextResolver 支持 it/that/刚才那个/这个订单 等 follow-up，输出结构化 `ContextResolution.referenced_entities`，不再把实体拼接进 query；显式新 SKU/订单覆盖旧实体；隐私字段不写入记忆。`EntityResolver` 仅作为兼容包装保留。 | `src/commerce_rag_ops/memory/context_resolver.py`, `src/commerce_rag_ops/entity_memory.py`, `data/eval/multiturn_memory.jsonl`, `reports/memory_eval_report.md`, `docs/memory_design.md` |
| Self-reflection | 已实现 | Agent 每轮生成后执行 relevance/groundedness proxy、EvidenceGapAnalyzer、evidence contract、citation schema 检查；CriticVerifier 根据 verification 和缺口决定 answer/retry/refuse/escalate。新增 LLM-as-judge 用真实 API 抽样评估 groundedness/relevance/citation/safety。 | `src/commerce_rag_ops/evidence/gaps.py`, `src/commerce_rag_ops/evidence/critic.py`, `CommerceRAGAgent.run`, `src/commerce_rag_ops/llm_judge.py`, `reports/llm_judge_report.md` |
| Refusal control | 已实现 | 弱召回、未知意图、未知 SKU/订单、隐私/越权/提示注入/不安全承诺会 retry 后拒答；拒答不输出 citation。 | `src/commerce_rag_ops/refusal_eval.py`, `data/eval/refusal.jsonl`, `reports/refusal_eval_report.md`, `reports/combined_eval_report.md` |
| Citation control | 已实现 | 高风险客服答案必须有 doc/chunk citation；citation schema validator 校验 answer citation marker、state citations、retrieved contexts 三者一致；tool citation validator 校验 `[tool:...]` marker 来自本轮工具调用，覆盖价格、库存、订单状态、订单明细、退货资格等结构化事实。 | `src/commerce_rag_ops/citation_quality.py`, `reports/citation_schema_smoke_report.md`, `reports/tool_eval_report.md`, `data/quality_gates.json` |
| Trace and observability | 已实现 | 保留兼容 event trace，同时新增 span trace：trace_run、trace_spans、trace_artifacts、retrieval_candidates；新增 `agent.plan`、`plan.validate`、`domain_agent.loop`、`domain_agent.step`、`policy.check`、`memory.source_defaults`、`memory.semantic_retrieve`、`memory.skip`、`answer.generate`、`critic.evaluate_answer`；`generation.llm` 现在挂在 `answer.generate` 下，generation artifact 使用 EvidencePack-only prompt policy；TraceSQLiteStore 已新增 `trace_steps`、`trace_observations`、`trace_evidence`、`trace_verifications` 派生表；doc/tool citation validation、proxy grader、evidence build、critic verify、replanner 和 final decision 现在挂在 Critic 父 span 下；本地 HybridRetriever 记录 dense/BM25/RRF/forced/rerank/diversify 候选诊断。`retrieval_plan` 仅作为旧报告兼容字段保留，主链路由 `memory.semantic_retrieve` 工具输入决定是否检索。 | `src/commerce_rag_ops/trace.py`, `src/commerce_rag_ops/trace_store.py`, `src/commerce_rag_ops/serialization.py`, `src/commerce_rag_ops/runtime/final_answer.py`, `web/index.html`, `docs/intent_trace_design.md`, `tests/test_core.py::test_trace_store_and_api_builder` |

## LLM-as-Judge

新增命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli judge-eval --backend qdrant --generator openai-compatible --limit 3
```

当前真实 API smoke 结果：

| 指标 | 值 |
|---|---:|
| 样本数 | 3 |
| Judge model | `deepseek-v4-flash` |
| Pass rate | 1.0 |
| Groundedness | 1.0 |
| Relevance | 1.0 |
| Citation support | 1.0 |
| Safety | 1.0 |

报告：`reports/llm_judge_report.md`。

## 口径说明

- `Query expansion / HyDE` 目前是 query expansion + gap-aware retry query enhancement，不是论文式 HyDE。如果面试官严格问 HyDE，应说“没有把 LLM 生成的 hypothetical document 放入检索，只做了轻量 query expansion 和 agentic retry expansion”。
- `Self-reflection` 分两层：默认 deterministic grader/evidence contract 可离线复现；`judge-eval` 是真实 LLM-as-judge 抽样质检。
- `Citation control` 分三层：doc citation 校验 retrieved contexts；tool citation 校验结构化事实来自本轮工具调用；LLM-as-judge 再做语义级 groundedness/citation support 抽样质检。
- `LLM Advisor` 是建议层，不是执行层；所有 LLM 建议都会重新经过规则合并、DomainAgent、ToolPolicy 和 evidence gate。面试时不要说“LLM 直接决定退款/调用工具”，应该说“LLM 在 agent.plan 中建议工具和动作，系统按策略确认或阻断”。
- `Semantic Memory Tool` 是 RAG 的新定位。面试时不要说“整个项目就是 RAG”，应该说“RAG 是长期语义记忆的一种实现，由 Agent 在需要外部知识时调用；订单/SKU 等强事实优先走结构化工具”。
