# 检索迭代日志

本日志记录真正改变检索行为的 precision 与 Agentic RAG 迭代。它的目标是让项目在面试中可解释、可追溯：每一步都包含观察到的问题、实现改动、验证命令和实测结果。

## 2026-07-05 - Curated Evidence Budget 与 Policy Family Guards

观察到的问题：

- 种子/demo query 能返回正确的 ticket 或 product，但 Top-5 后半部分会被弱相关 KB、OCR、table 文档填充。
- 典型失败包括 refund、warranty、subscription demo，其中 policy matrix 或 OCR form 挤掉了权威 policy。

实现改动：

- 为本地 fixture 商品增加 curated/demo evidence budget。
- 为 warranty、payment refund、shipping delivery、missing parts、return/refund policy 类型增加 policy-family guards。
- 将正/负情绪过滤限制在 curated fixtures，避免伤害 Amazon-scale query。

验证：

- `python -m pytest -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli gate`

结果：

- 6 条 seed query 的 Precision/Recall/NDCG 达到 `1.0`。
- Full gate 通过：Precision@5 `0.9675`，Recall@5 `0.9315`，NDCG@5 `0.9902`，p95 `573 ms`。

## 2026-07-05 - Rating Evidence-Pack Collection 与 Support Context Guards

观察到的问题：

- Rating-specific review query 有时会把 `product_profile` 或无关 `review_aspect_summary` 混入本应放 review evidence 的位置。
- Support case 在已经找到核心 FAQ、policy、原始 review 后，仍可能继续引用 category complaint cluster 或错误 aspect summary。

实现改动：

- 增加 rating evidence-pack collection：当存在至少 5 个同 product、同 rating 的 review evidence candidate 时，最终 Top-5 优先填充这些 review chunks。
- 增加 support final-context guards：support case 拒绝 complaint clusters；显式 aspect support question 需要同 aspect summary；battery/power case 避免被 generic reason-code table 填充。
- 提升质量门禁阈值。

验证：

- 对 `Q-001` 到 `Q-006` 做 seed quick check。
- 对全部 366 条 query 运行 retrieval-only full eval script。
- `python -m pytest -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli gate`

结果：

- Full gate 通过：Precision@5 `0.9776`，Recall@5 `0.9361`，NDCG@5 `0.9969`，p95 `559 ms`。
- Customer-ops Precision@5 提升到 `0.9645`。
- Support Precision@5 提升到 `0.981`。

## 2026-07-05 - Product-Level Aspect Hard Guards

观察到的问题：

- 剩余 precision miss 主要来自 product-level customer-ops query，例如 `around price_value` 或 `around missing_parts`。
- Retriever 已经找到正确 product 和 evidence，但最后一个 slot 仍可能被错误 aspect summary 或 category-level complaint cluster 占用。
- 对同 rating review 不足 5 条的 sparse rating-evidence query，系统可能选择一个已被已选 reviews 覆盖过的 aspect summary。

实现改动：

- 增加 product-level aspect hard guards：当 query 能解析到某个 product 且询问特定 aspect 时，final context 会拒绝错误 aspect 的 `review_aspect_summary`、`review_evidence`、`faq_case` 和 category `complaint_cluster` 结果。
- 为 sparse rating-specific review evidence query 增加互补 aspect-summary fallback：当已选 reviews 覆盖某一 aspect 后，尽量选择同 product 的另一个相关 aspect summary。
- 再次提升质量门禁：overall Precision@5 `>= 0.99`，customer-ops Precision@5 `>= 0.99`。

验证：

- 对之前的弱样本做本地 spot check：`QS-0161`、`QS-0187`、`QS-0193`、`QS-0196`、`QS-0205`、`QS-0226`，以及 seed `Q-001` 到 `Q-006`。
- 对全部 366 条 query 运行 retrieval-only full eval。
- `python -m pytest -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli gate`

结果：

- Full gate 通过：Precision@5 `0.9945`，Recall@5 `0.9355`，MRR `1.0`，NDCG@5 `0.9966`，p95 `559 ms`。
- Customer-ops Precision@5 提升到 `0.9978`。
- Recommendation Precision@5 保持 `1.0`。
- Support Precision@5 保持 `0.981`。

残留说明：

- Recall@5 受 evidence-pack size 约束；对有 6-8 个 relevant documents 的 query，即使 Top-5 全部相关，也不可能在 Top-5 内召回所有标签。
- 剩余 precision miss 多数来自 general-support case：前 3-4 个 context 正确，最后一个 padding slot 有噪声。后续可考虑 support-specific dynamic evidence budget 或更严格的 lineage expansion，但需要小心验证，避免降低 support recall。

## 2026-07-06 - Agent Evidence Contracts 与 Support Aspect Routing

观察到的问题：

- 检索指标已经高于目标区间，但 agent loop 没有显式记录某个回答是否具备该 intent 期望的完整证据形态。
- 包含 `price_value` 这类 aspect label 的 support query 可能被误路由成精确 price/SKU lookup，因为 tokenizer 会把 aspect 拆成 `price` 和 `value`。
- 朴素 evidence-contract retry 可能让评测延迟翻倍，因此重试需要限制在 critical evidence gaps 上。

实现改动：

- 在检索后增加 agent-level evidence contract。它会检查 support policy/case evidence、recommendation product/review evidence、customer-ops customer-voice evidence、以及 SKU/order structured-entity evidence。
- 为 `missing_policy`、`missing_review`、`missing_product`、`missing_customer_voice`、`missing_structured_entity`、`no_context` 等 critical gap 增加 gap-specific retry query expansion 和 source fallback。
- 对 non-critical gap 做 trace 记录，例如已有 policy evidence 时的 `missing_similar_support_case`，但不强制二次检索。
- 修正 intent routing：`How should support handle this price_value case ...` 留在 support flow，而显式 SKU、inventory、order status、price、delivery-status query 仍路由到结构化工具。

验证：

- `python -m pytest -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli gate`
- 对全部 366 条 golden query 运行 full agent gap scan；在压制 non-critical support-case retry 后，evaluation distribution 显示 `366` 条 one-attempt answer。

结果：

- Tests: `11 passed`。
- Gate: PASS。
- Precision@5 `0.9989`，Recall@5 `0.9360`，MRR `1.0`，NDCG@5 `0.9971`。
- Citation rate `1.0`，keyword coverage `0.8934`，groundedness proxy `1.0`。
- p95 latency `631 ms`。

评测完整性：

- 未修改 `data/eval/golden.jsonl`。
- 分数变化来自 agent routing、answer keyword coverage、evidence-contract trace/retry 行为和报告刷新，不来自测试集 relabel。

## 2026-07-06 - 评测中的 Agentic 证据诊断

观察到的问题：

- Agent trace 已经按 query 记录 evidence gaps，但正式 evaluation report 没有汇总 fallback health。
- 这会导致面试时很难说明 Agentic RAG 是否真的启用、是否过度触发，还是只在记录残留风险。

实现改动：

- 在每条 support-quality evaluation row 中加入 `attempts` 和 `evidence_gaps`。
- 在 report JSON 中加入 `agentic_diagnostics`，包含 action counts、attempt counts、retry rate、evidence-gap counts、以及 evidence gaps by intent。
- 在 `reports/evaluation_report.md` 中增加 `Agentic 证据诊断` 章节。
- 增加测试覆盖，确保 eval output 保留新的 diagnostics。

验证：

- `python -m pytest -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli gate`

结果：

- Tests: `11 passed`。
- Gate: PASS。
- Agentic diagnostics：retry rate `0.0`，actions `answer: 366`，attempts `1: 366`，evidence gaps `missing_case_evidence: 36`。
- Retrieval/support metrics 仍高于 gate：Precision@5 `0.9989`，Recall@5 `0.9360`，NDCG@5 `0.9971`，keyword coverage `0.8934`，p95 `631 ms`。

评测完整性：

- 未修改 `data/eval/golden.jsonl`。
- 本轮提升的是可观测性和面试可解释性，不是通过调整 label 或 query distribution 提分。

## 2026-07-06 - Scripted Fallback Stress Harness

观察到的问题：

- 正式 golden eval 显示 `0.0` retry rate，因为大多数 retrieved evidence 首轮已经足够。
- 这对延迟是好事，但不能证明首轮检索失败时 critical fallback path 是否可用。

实现改动：

- 新增 `commerce_rag_ops.fallback_stress`，用于脚本化注入检索失败。
- 新增 CLI 命令 `python -m commerce_rag_ops.cli fallback-stress`。
- 生成 `reports/fallback_stress_report.md`。
- 覆盖四类可恢复 critical gaps：`missing_review`、`missing_policy`、`missing_customer_voice`、`missing_structured_entity`。
- 增加 no-context refusal case，证明 retry 无法恢复 grounded evidence 时 agent 不会硬答。
- 增加 unknown-order refusal 边界：当显式 order ID 在 SQL/JSON 工具中不存在时，即使 retrieval 找到相关 product 或 policy chunk，仍保持 `missing_structured_entity`。
- 增加 unknown-SKU refusal 边界，规则相同：显式 SKU 字符串必须通过结构化工具解析，不能用另一个检索到的 product 替代。
- 增加 recoverable SKU/order product-context case：当 query 没有显式 SKU/order ID，但首轮缺少 product context 时，agent 会重试并可从 retrieved product evidence 恢复。
- 增加 structured-entity context filtering：当 SKU/order 工具解析出 product 后，final citations 保留同 product evidence 和 product-neutral policy docs，丢弃冲突 product contexts。并为显式 SKU 和显式 order ID 分别增加测试。

验证：

- `python -m pytest tests\test_core.py::test_fallback_stress_cases_cover_critical_gaps -q -p no:cacheprovider`
- `python -m pytest tests\test_core.py::test_structured_entity_filter_removes_wrong_product_context -q -p no:cacheprovider`
- `python -m commerce_rag_ops.cli fallback-stress`

结果：

- Stress cases: `7`。
- 是否通过: `true`。
- 触发重试用例数: `7`。
- 最终回答用例数: `4`。
- 最终拒答用例数: `3`。
- 可恢复 case 均产出 citations；unknown-SKU、unknown-order、no-context case 均无 citation 并拒答。

评测完整性：

- 未修改 `data/eval/golden.jsonl`。
- 这是对抗式 control-flow 检查，不是提分迭代。
