# Agent Runtime 重构记录

本文记录本轮把项目从“固定 workflow + 多个 advisor”推进到 **RootRouterAgent + DomainAgent + AgentLoop + EvidencePack + CriticVerifier + Replanner** 的重构状态。

## 重构目标

原来的主链路虽然已经支持 LLM advisor、工具调用和按需 RAG，但控制权仍分散在多个环节：

- deterministic route
- LLM route advice
- agent plan
- tool plan
- LLM tool advice
- semantic memory 特判
- grader
- decision

本轮开始收敛为：

```text
Request
  -> structured ContextResolution
  -> RootRouterAgent
  -> DomainAgent plan / next_step
  -> AgentLoop step budget
  -> tool / semantic memory observations
  -> EvidencePackBuilder
  -> CriticVerifier
  -> Replanner
  -> FinalAnswer
  -> answer / repair_budget / refuse / escalate
```

当前是兼容式落地：保留 `CommerceRAGAgent` 对外入口和现有 CLI/API/test，但内部已经开始使用新的 runtime 对象，避免一次性推倒导致评测失真。

## 已完成

### 1. Structured ContextResolution

新增 `memory.context_resolver`：

- `ContextResolution`
- `ResolvedEntity`
- `EntityCandidate`
- `ContextResolver`

`EntityResolver` 现在不再把记忆实体拼成自然语言 suffix。旧行为：

```text
Can I get a refund for that? Context from conversation memory: order ORD-1003.
```

新行为：

```json
{
  "original_query": "Can I get a refund for that?",
  "is_followup": true,
  "referenced_entities": [
    {
      "entity_type": "order_id",
      "entity_value": "ORD-1003",
      "source": "entity_memory",
      "confidence": 0.92,
      "requires_tool_confirmation": true
    }
  ],
  "resolution_source": "memory"
}
```

CLI/API 仍返回兼容字段 `resolved_query`，但内部不再依赖字符串拼接；`ToolSuggester` 会直接读取 `state.resolved_entities`。

### 2. RootRouterAgent

新增 `agents.root_router.RootRouterAgent`，把 weighted routing 信号和 legacy intent 映射收敛到 router 层：

| legacy intent | domain |
|---|---|
| support | support |
| recommendation | recommendation |
| customer_ops | customer_ops |
| sku_order | order |
| unknown / safety boundary | refusal |

RootRouter 只负责领域分派和安全边界，不做工具计划、检索计划或最终动作。

当前 `_route_intent_decision()` 仍作为 `CommerceRAGAgent` 的兼容方法保留，但实现已经委托给 `RootRouterAgent.decide_intent()`。也就是说，query token、结构化实体、业务短语、类目 hint 和 safety boundary 的加权打分不再由 `CommerceRAGAgent.run()` 所属类直接维护；`CommerceRAGAgent` 只消费 router 输出并进入 DomainAgent。

### 3. DomainAgents

新增：

- `SupportAgent`
- `RecommendationAgent`
- `CustomerOpsAgent`
- `OrderAgent`
- `RefusalAgent`

每个 DomainAgent 定义：

- `name`
- `allowed_tools`
- `evidence_contract`
- `plan()`
- `next_step()`

当前 `plan()` 是规则式可复现版本，输出兼容 `agent_plan`；`next_step()` 已接入 `AgentLoop`，会读取 `RunState.observations`、`action_suggestions` 和 `semantic_memory_request` 动态选择下一步 action。工具候选来自 `ToolSuggester` 和 `agent.plan.tool_calls`；主链路不再单独调用旧的 `advise_tools()`，LLM 对工具的建议被并入 `advise_plan()` 输出，再由 DomainAgent 跳过已执行过的 step，在结构化工具之后按需读取长期语义记忆。

### 4. Runtime Types

新增 `runtime` 包：

- `RunState`
- `BudgetState`
- `AgentStep`
- `AgentStepRecord`
- `Observation`
- `AgentLoop`
- `AgentStepExecutor`

当前工具和 semantic memory 调用已经通过 `AgentLoop.run_agent()` 执行，并消耗 `max_steps`、`max_tool_calls`、`max_retrieval_calls`、`max_write_tool_drafts` 预算；`AgentState.runtime_state` 会记录 steps、observations 和 budgets。外层不再是固定 `for attempt in range(max_retries + 1)`，而是由 `CriticVerifier` 判断是否需要 repair，再由 `Replanner` 生成补证据 step。`max_retries` 仅作为 CLI/API 兼容参数，内部解释为 `max_repair_rounds`。

`AgentStepExecutor` 已从 `CommerceRAGAgent._run_domain_step_loop()` 中抽到 runtime 层，负责 `domain_agent.step` span、`policy.check` span、工具执行、retrieval observation 和结构化工具结果同步；`CommerceRAGAgent` 只保留 semantic memory 的业务回调。

### 5. EvidencePackBuilder

新增 `evidence.EvidencePackBuilder`，把工具和语义记忆结果归一为：

- `structured_facts`
- `policy_evidence`
- `product_evidence`
- `review_evidence`
- `ticket_evidence`
- `unresolved_conflicts`
- `missing_requirements`

这一步开始替代旧的散落字段，例如 `tool_results`、`retrieved_contexts`、`structured_context_filter` 和 `_evidence_gaps`。

生成前会先执行 `evidence_pack.prepare_answer`，把已验证工具结果和检索证据归一成回答上下文。`TemplateAnswerGenerator` 和 `OpenAICompatibleGenerator` 都通过 `build_answer_context()` 读取 EvidencePack；OpenAI-compatible prompt 不再包含 raw `tool_results`、raw retrieved `contexts` 或 `retrieval_plan`。

### 5.1 FinalAnswerBuilder

新增 `runtime.FinalAnswerBuilder`，把最终回答生成从 `CommerceRAGAgent.run()` 中抽离出来。它只负责：

- 根据当前 evidence 状态选择允许的 doc citations。
- 构造 EvidencePack-only 的 generation artifact。
- 调用配置的 `AnswerGenerator`。
- 记录 `answer.generate -> generation.llm` span。

因此主链路可以更明确地表达为 `CriticVerifier / Replanner -> FinalAnswer`，而不是在 `CommerceRAGAgent.run()` 中直接拼 generation span。`generation_context` artifact 的 `prompt_policy` 现在是 `evidence_pack_only`，不再把 raw contexts 或 raw tool_results 放进生成阶段 trace。

### 6. CriticVerifier

新增 `evidence.CriticVerifier`，统一输出：

- `passed`
- `action`
- `missing_evidence`
- `citation_errors`
- `tool_fact_errors`
- `safety_errors`
- `repair_hints`

新增 `evidence.EvidenceGapAnalyzer`，把原先散落在 `CommerceRAGAgent._evidence_gaps()` 和 `_safety_gaps()` 里的缺口分析迁移到 evidence 层。当前主流程中：

- `EvidenceGapAnalyzer.gaps()` 负责产出 missing requirements / safety gaps。
- `CriticVerifier.verify()` 负责合并 citation/tool citation 校验和 evidence contract。
- `CriticVerifier.decide_action()` 负责产出 `answer | retry | refuse | escalate | ask_user`。
- `CommerceRAGAgent._grade()` 仍保留为 relevance/groundedness proxy 指标，不再是最终动作决策主控。

### 7. Replanner

新增 `evidence.Replanner`：

- 输入：`VerificationResult`、query、domain。
- 输出：`RepairPlan`，包含需要补证据的 `AgentStep`。
- 当前规则：`missing_policy` 补 KB policy retrieve；`missing_review` / `missing_customer_voice` 补 review/ticket retrieve；`missing_product_context` 补 product/kb retrieve。
- Trace：新增 `replanner.plan` span 和 `replanner_plan` event。

当 action 为 retry 时，下一轮 repair 会优先使用 Replanner 生成的 repair query/sources，而不是只依赖旧的 `_enhance_query()`。Trace 会记录 `repair_budget_start`、每轮 `repair_round`、`max_repair_rounds`，`runtime_state.repair_budget` 会记录当前补证据预算。

### 8. Semantic Memory Tool

`memory.semantic_retrieve` 已注册为只读 `ToolSpec`，由 Agent plan 决定是否调用：

- 输入：`query`、`sources`、`top_k`、`candidate_k`、`reason`。
- 输出：`memory_type=semantic_long_term`、contexts、doc citations、diagnostics。
- 执行：在 `DomainAgent.next_step()` 中作为普通 `tool_call` step 选择，通过 `ToolExecutor` 和 `ToolPolicy`，隐私边界、domain/action 权限不能被 LLM 绕过；返回后在 `Observation.kind` 中标记为 `retrieval`。
- Trace：保留 `memory.semantic_retrieve` span，并把原来的 dense/BM25/RRF/rerank diagnostics 挂在该 memory 调用下。

普通 SQL/订单/库存/工单工具先确认结构化事实；semantic memory 在需要政策、评论、FAQ、相似工单等长期知识时才被调用。订单状态这类强结构化问题会进入 `memory.skip`。

## 当前运行链路

当前兼容链路为：

```text
CommerceRAGAgent.run
  -> memory.load
  -> intent.route
  -> router.select_domain
  -> DomainAgent.plan
  -> tool.plan / agent.plan tool_calls / ToolSuggester action_suggestions
  -> domain_agent.loop
       -> domain_agent.step
       -> policy.check
       -> tools.execute / memory.semantic_retrieve as ToolSpec
  -> context.structured_filter
  -> evidence_pack.prepare_answer
  -> answer.generate
       -> generation.llm
  -> critic.evaluate_answer
       -> citation.validate / tool_citation.validate
       -> evidence_pack.build
       -> critic.verify
       -> replanner.plan
       -> critic decision
  -> repair round if critic_action == retry and repair budget remains
```

也就是说，外部 API 还没有变，但 trace 中已经能看到：

- `router.select_domain`
- `agent.plan`
- `plan.validate`
- `domain_agent.loop`
- `domain_agent.step`
- `policy.check`
- `memory.semantic_retrieve` 或 `memory.skip`
- `evidence_pack.prepare_answer`
- `answer.generate`
- `generation.llm`
- `critic.evaluate_answer`
- `evidence_pack.build`
- `critic.verify`
- `replanner.plan`
- `action_decision.critic_action`
- `action_decision.repair_round`
- `runtime_state.repair_budget`

`TraceSQLiteStore` 也开始从 span-only 过渡到目标 schema：除了 `trace_runs`、`trace_spans`、`trace_artifacts`、`retrieval_candidates`，现在会额外写入 `trace_steps`、`trace_observations`、`trace_evidence`、`trace_verifications`。这些表从 `runtime_state`、`EvidencePack` 和 `CriticVerifier` 输出派生，方便直接查询“DomainAgent 做了哪些 step、每步产生了什么 observation、最终 evidence pack 里有哪些结构化事实/文档证据、critic 给了什么 verification”。

## 行为验证

新增/更新测试覆盖：

- follow-up 不再拼接 query，但能从 `context_resolution.referenced_entities` 调用订单工具。
- `RootRouterAgent` 负责 weighted intent signals，并选择 `order` / `refusal` domain。
- `DomainAgent` 计划进入 `state.agent_plan`。
- `AgentLoop` 记录 `runtime_state.steps`、`runtime_state.observations` 和 budget 使用。
- `direct_answer` 计划不会被强行插入结构化工具或语义记忆调用。
- 订单状态查询可跳过 semantic memory。
- support/recommendation/customer ops 需要语义证据时调用 `memory.semantic_retrieve`。
- `EvidencePackBuilder` 生成结构化事实。
- `AnswerGenerator` 只消费 EvidencePack 派生的 answer context，不直接读取 raw retrieved contexts 或 raw tool results。
- `FinalAnswerBuilder` 生成 EvidencePack-only artifact，并把 `generation.llm` 挂到 `answer.generate` 下。
- `TraceSQLiteStore` 可查询 `steps()`、`observations()`、`evidence()`、`verification()`，并落到 `trace_steps`、`trace_observations`、`trace_evidence`、`trace_verifications` 表。
- `EvidenceGapAnalyzer` 产出缺口；`CriticVerifier` 记录通过/拒答/repair 信息并决定最终动作。
- `Replanner` 在缺证据时产出 repair step，下一轮 retry 优先使用 repair query/sources。
- 固定 `max_retries + 1` 循环已替换为 Critic/Replanner 驱动的 repair budget loop；无 repair 预算时不会额外检索，有预算且 Critic 判断缺证据时才进入下一轮。

当前验证：

```text
pytest -q: 36 passed
fallback-stress: 7/7 passed
tool-eval --reranker-model none: pass_rate 1.0
```

## 尚未完成的拆分

后续还需要继续做：

1. 继续缩小 `CommerceRAGAgent.run()`，把 planning、evidence build、critic/replanner 迁到更薄的 runtime orchestration 层。
2. 将 `_grade()` 的 proxy 指标迁移为 CriticVerifier 的 metrics 输出，减少 `grader.score` 兼容层。
3. 将 event trace 从 span/step/observation trace 派生，减少双轨维护；SQLite 已经有 `trace_steps` / `trace_observations` / `trace_evidence` / `trace_verifications` 派生表，但 span trace 仍是主事实源。
4. 继续增强 `DomainAgent.next_step()` 的 LLM/rule 混合选择能力，让它不只消费候选动作，还能基于 observation quality 主动提出补充动作。

## 面试说法

可以这样讲：

> 我把原先的固定 Agentic workflow 重构成 Router + Domain Agents + AgentLoop + EvidencePack + Critic + Replanner + FinalAnswer 的形态。RootRouter 只负责安全边界和领域分派；Support/Recommendation/CustomerOps/Order/Refusal 各自拥有工具权限和证据契约；DomainAgent.next_step 通过 AgentLoop 执行工具和长期语义记忆 step，并记录 observation 和预算；每个工具 step 都先落 `policy.check`，再执行工具或 semantic memory；RAG 被降级为只读长期语义记忆工具 `memory.semantic_retrieve`，只有计划需要政策、评论、FAQ 或相似工单时才调用；多轮指代不再通过 query suffix 拼接，而是结构化 ContextResolution；工具和语义检索结果会进入 EvidencePack；最终回答由 `FinalAnswerBuilder` 只读取 EvidencePack 派生的 answer context，不直接读 raw contexts/tool_results；EvidenceGapAnalyzer 负责缺口识别，CriticVerifier 判断证据是否足够、引用是否有效、安全边界是否通过并产出最终动作；不通过时 Replanner 只补缺失证据。当前为了兼容已有 CLI/API，参数名仍保留 `max_retries`，但内部已解释为 `max_repair_rounds`，只有 Critic 要求 retry 且预算允许时才进入 repair round。Trace 能看到 router.select_domain、agent.plan、domain_agent.loop、domain_agent.step、policy.check、memory.skip / memory.semantic_retrieve、evidence_pack.prepare_answer、answer.generate、generation.llm、critic.evaluate_answer、critic.verify、replanner.plan、action_decision.critic_action 和 repair_budget。
