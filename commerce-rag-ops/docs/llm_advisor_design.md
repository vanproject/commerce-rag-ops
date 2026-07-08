# LLM Advisor 与规则兜底设计

本文记录本轮把系统从“规则工作流”升级为“LLM 参与决策建议，规则和策略最终兜底”的实现。核心口径是：

> LLM proposes, rules/policy disposes。

LLM 不再只参与最后总结，而是在 Agent 的三个关键阶段给出建议：

1. 初始意图识别建议。
2. Agent 执行计划建议，其中包括是否 direct answer、是否追问、是否调用结构化工具、是否调用长期语义记忆，以及具体 tool_calls。
3. 最终动作建议。

但 LLM 的输出永远不是最终执行结果。`CommerceRAGAgent` 会把 LLM 建议与 deterministic router、ToolPolicy、evidence gate、citation validator 合并，安全边界和事实边界不可被覆盖。

## 运行链路

当前主链路可以概括为：

```text
query
  -> deterministic weighted router
  -> llm.intent_advice
  -> route merge with hard safety boundaries
  -> risk assessment
  -> agent.plan / llm plan advice
  -> DomainAgent.next_step consumes plan tool_calls + heuristic suggestions
  -> ToolPolicy / ToolExecutor per step
  -> optional memory.semantic_retrieve
  -> generation
  -> citation/tool citation validation
  -> deterministic grader/evidence gaps
  -> llm action advice
  -> final action merge
  -> answer / retry / refuse / escalate
```

这个设计保留了规则系统的可复现性，同时让 LLM 可以参与更开放的判断。例如用户说“退款太麻烦了，帮我处理一下”，规则可能只识别到 support；LLM 可以在 `agent.plan.tool_calls` 中建议补充 `ops.refund_request_draft` 或 `ops.escalate_ticket`，也可以决定是否需要调用 `memory.semantic_retrieve` 查政策/相似案例。但 DomainAgent 只会消费允许 domain 内的 step，ToolPolicy 会要求用户确认，且大额退款会被直接阻断。

## 四阶段职责

| 阶段 | LLM 参与点 | LLM 可以建议 | 不可绕过的兜底 |
|---|---|---|---|
| Intent routing | `advise_route()` | 在规则信号不足或业务语义更强时建议 `support`、`recommendation`、`customer_ops`、`sku_order`、`unknown` | `safety_boundary`、`safety_domain` 不可覆盖；低置信度或非法 intent 被忽略 |
| Agent planning | `advise_plan()` | 建议 `direct_answer`、`ask_user`、`call_tools`、`retrieve_memory`、`decide_action`；决定 RAG/语义记忆是否需要调用；通过 `tool_calls` 建议订单、退货资格、评论摘要、相似工单、人工升级、退款申请草稿等工具 | 计划会经过 validation；隐私/安全边界会移除 `retrieve_memory` 和 `call_tools`；非法工具和非法 source 会被丢弃；DomainAgent 和 ToolPolicy 再次兜底 |
| Final action | `advise_action()` | 建议 `answer`、`retry`、`refuse`、`escalate`，尤其是高风险客服场景升级人工 | unknown、隐私、提示注入、不安全承诺、弱证据拒答不可覆盖；规则判定 retry/refuse 时 LLM 不能强行 answer |

`advise_tools()` 接口暂时保留，供旧实验脚本或外部集成兼容；主链路不再单独调用它。工具选择已经内联到 `agent.plan`，再由 `DomainAgent.next_step()` 按 observation、预算和 allowed tools 逐步消费。

## RAG 的新定位

RAG 现在被降级为长期语义记忆工具：

- 工具名：`memory.semantic_retrieve`
- 输入：`query`、`sources`、`top_k`、`reason`
- 输出：`memory_type=semantic_long_term`、retrieved contexts、doc citations、dense/BM25/RRF/rerank diagnostics

因此 `Check order ORD-1003 status.` 这类强结构化问题可以只调用 `sql.order_by_id` 和 `sql.order_items_by_order_id`，不触发向量检索。退款政策、客户投诉趋势、推荐理由、相似 FAQ case 等需要外部知识的问题，才由 Agent plan 调用 `memory.semantic_retrieve`。

## 工具与退款边界

当前写操作工具包括：

- `ops.escalate_ticket`：生成人工升级工单草稿，不直接创建真实工单。
- `ops.refund_request_draft`：生成退款申请草稿，不直接批准退款。

写工具都声明 `requires_confirmation=True`。因此即使 LLM 建议调用这些工具，系统返回的也是 `requires_user_confirmation`，由用户决定是否提交。

退款金额还有额外策略：

- `refund_amount <= 100`：仍然只是确认草稿，不自动退款。
- `refund_amount > 100`：ToolPolicy 返回 `blocked/refund_amount_exceeds_limit`。

也就是说，LLM 可以帮用户整理退款申请信息，但不能批准大额退款，也不能绕过用户确认。

## 规则兜底

不可覆盖的边界包括：

- 隐私和越权：`all customer orders`、`payment details`、`emails`、`address` 等。
- 提示注入和系统信息：`system prompt`、`api key` 等。
- 结构化事实：显式 SKU、订单号、订单明细、库存、退货资格必须由 SQL/工具确认。
- 证据不足：缺少 policy、review、ticket、product context 时先 retry；仍不足则拒答。
- 引用一致性：doc citation 和 tool citation 必须来自本轮检索或工具调用。

这些规则由 `_route_intent_decision()`、`_merge_route_decision()`、`_validated_agent_plan()`、`DomainAgent.next_step()`、`ToolPolicy.check()`、`_evidence_gaps()`、`_merge_action_decision()` 和 citation validators 共同保证。

## Trace 观察点

轻量 event trace 会记录：

- `intent_route.llm_advice`
- `intent_route.selected_by`
- `agent_plan.merged_plan`
- `memory_semantic_retrieve`
- `memory_skip`
- `tool_use.llm_advice`，现在指向从 `agent.plan.tool_calls` 消费的建议
- `decision.rule_action`
- `decision.llm_advice`
- `finish.final_action`

Span trace 额外包含：

- `llm.intent_advice`
- `agent.plan`
- `plan.validate`
- `tool.plan`
- `tools.execute`
- `answer.generate`
- `memory.semantic_retrieve` 或 `memory.skip`
- `retrieval.attempt`，仅当 semantic memory 被调用时出现
- `generation.llm`
- `citation.validate`
- `tool_citation.validate`
- `decision`

因此面试或排障时可以回答：

> 我能看到规则路由原本怎么判、LLM 建议了什么、最后为什么采纳或拒绝。比如隐私 query 里，LLM 即使建议 support，trace 会显示 `llm_merge_reason=rule_safety_boundary_not_overridable`，最终仍然 unknown/refuse。

## 配置方式

`.env.example` 提供 OpenAI-compatible 配置：

```text
COMMERCE_RAG_LLM_ENDPOINT=https://opencode.ai/zen/go/v1
COMMERCE_RAG_LLM_MODEL=deepseek-v4-flash
COMMERCE_RAG_LLM_API_KEY=
```

CLI 和 API 支持：

```powershell
python -m commerce_rag_ops.cli ask "My serum arrived broken. Can you help with a refund?" --advisor auto
python -m commerce_rag_ops.cli qdrant-ask "Draft a refund request for order ORD-1001." --advisor auto
```

`--advisor auto` 会在 `COMMERCE_RAG_LLM_API_KEY` 存在时启用真实 LLM advisor，否则回退到 rule-only。离线测试可以显式使用 `--advisor rule`。

## 面试讲法

可以这样说：

> 我没有把 Agent 做成纯规则工作流。现在 LLM 参与三个决策点：先给意图路由建议，再给执行计划建议，决定是否 direct answer、追问、调用结构化工具、调用长期语义记忆，最后给 answer/retry/refuse/escalate 动作建议。但系统采用 LLM proposes, policy disposes：隐私、安全、写操作确认、大额退款、结构化事实和 citation contract 都由确定性规则最终兜底。这样既保留了 LLM 对自然语言业务语义的理解，也避免它直接越权执行退款或编造政策。

如果被追问“LLM 除了总结还做了什么”，可以答：

> 它是 planner/advisor，不是 executor。LLM 会读取规则路由、记忆上下文、可用工具、evidence gaps 和工具结果，提出 intent/plan/action 建议。工具调用建议已经内联在 plan 的 `tool_calls` 里，由 DomainAgent 逐步消费：能决定是否调用 `memory.semantic_retrieve`，能补充低风险工具，也能建议升级人工；但不能绕过 ToolPolicy 和 evidence gate。

## 当前边界

- LLM advisor 走 OpenAI-compatible JSON 输出，不是函数调用协议；非法 JSON 会自动退回规则链路。
- 当前没有让 LLM 直接执行工具，所有工具调用都必须转成 `ToolCall` 后进入 ToolPolicy。
- `advise_tools()` 仍保留为兼容接口，但主链路工具选择已经合并进 `advise_plan()`。
- `memory.semantic_retrieve` 是 Agent 内部处理的特殊只读语义记忆工具，复用现有 retriever/Qdrant/dense+BM25+RRF+rerank，不重建向量库。
- 大额退款阈值目前是 demo 配置 `100.0`，真实业务应从策略中心或配置服务读取。
- `ops.refund_request_draft` 和 `ops.escalate_ticket` 只是确认草稿，不连接真实工单系统。
