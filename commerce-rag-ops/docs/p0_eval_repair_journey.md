# P0 Eval Repair Journey

## Scope

本轮按 `CommerceRAG Ops 新版评测后的修复方案` 落地 P0 的可审计闭环：

- 拆分 `humanlike_blind` 为可单轮解析与需要上下文澄清的两个 split。
- 修复 `forbidden_evidence.wrong_product_ids` 中混入目标商品的问题。
- 新增 `clarify` action，并让无上下文指代问题请求用户补充 product/SKU/order。
- 增加 citation repair 后处理，拒答/澄清不保留 citation。
- 用真实 OpenAI-compatible LLM 小样本跑新 split 评测，不使用 template 冒充真实结果。

## Artifacts

- `data/eval/humanlike_single_turn_resolvable.jsonl`: 29 rows
- `data/eval/humanlike_context_required.jsonl`: 171 rows
- `reports/eval_fairness_repair_report.md`
- `reports/humanlike_context_required_report.md`
- `reports/humanlike_single_turn_resolvable_report.md`
- `src/commerce_rag_ops/eval_repair.py`
- `src/commerce_rag_ops/citation_repair.py`

## Data Repairs

Command:

```bash
python -m commerce_rag_ops.cli repair-evalsets
```

Result:

- Source rows: 200
- Resolvable rows: 29
- Context-required rows: 171
- Humanlike forbidden repairs: 12
- Challenge forbidden repairs: 12
- Remaining target-in-forbidden violations: 0

Context-required rows are marked:

- `expected_action = "clarify"`
- `must_cite = false`

## Real LLM Smoke Eval

Commands:

```bash
python -m commerce_rag_ops.cli eval --eval-filename humanlike_context_required.jsonl --generator openai-compatible --reranker-model none --limit 10
python -m commerce_rag_ops.cli eval --eval-filename humanlike_single_turn_resolvable.jsonl --generator openai-compatible --reranker-model none --limit 10
```

Observed `humanlike_context_required` first-10 result:

- LLM model: `deepseek-v4-flash`
- Oracle sources: `False`
- Reranker model: `none`
- `action_accuracy`: 1.0
- `citation_leak_rate`: 0.0
- `citation_schema_ok`: 1.0

Observed `humanlike_single_turn_resolvable` first-10 result:

- `exact_recall@5`: 0.3
- `acceptable_recall@5`: 0.3
- `entity_accuracy@5`: 0.3
- `forbidden_rate@5`: 0.0
- `citation_schema_ok`: 0.1

Interpretation:

- P0 action/citation handling for context-required cases is now working on the real API smoke set.
- Resolvable rows still need P1 retrieval/entity-candidate work; this is expected because the current smoke eval uses `local-token-cosine` and no reranker.

## Verification

Passed:

```bash
python -m compileall src
pytest -q tests/test_core.py::test_citation_repair_appends_doc_and_strips_non_answer_citations tests/test_core.py::test_context_required_reference_clarifies_without_citation tests/test_core.py::test_eval_row_repair_removes_target_from_forbidden_products
pytest -q
python -m commerce_rag_ops.cli llm-check
python -m commerce_rag_ops.cli refusal-eval --generator openai-compatible --reranker-model none --min-pass-rate 0.90
```

LLM check result:

- Endpoint: `https://opencode.ai/zen/go/v1/...`
- Model: `deepseek-v4-flash`
- Answer preview: `OK`

Full regression:

- `43 passed`
- Runtime: about 5m03s

Refusal/safety eval after the action split:

- `n`: 48
- `pass_rate`: 1.0
- `citation_leak_rate`: 0.0
- `action_counts`: `refuse=44`, `clarify=4`

The 4 clarify cases are insufficient-context or ambiguous-product rows whose correct behavior under the new four-action router is to ask for the missing product/order context instead of refusing.

## Strong Retrieval Baseline Status

Environment check:

- `sentence_transformers`: available
- `qdrant_client`: available
- `torch`: available
- CUDA: available, `NVIDIA GeForce RTX 5080`

Planned command for the Qdrant+BGE index:

```bash
python -m commerce_rag_ops.cli qdrant-index --embedding-backend sentence-transformers --embedding-model BAAI/bge-large-en-v1.5 --embedding-device cuda --embedding-batch-size 64
```

Executed index build:

- Collection: `commerce_rag_chunks`
- Points: 42,737
- Embedding model: `BAAI/bge-large-en-v1.5`
- Embedding dimensions: 1024
- Path: `.qdrant`

The CLI Qdrant backend now passes `--reranker-model` into `QdrantBackend`, so the reported reranker model matches the actual retriever configuration.

Smoke baseline commands:

```bash
python -m commerce_rag_ops.cli eval --eval-filename humanlike_single_turn_resolvable.jsonl --backend qdrant --embedding-backend auto --generator openai-compatible --reranker-model BAAI/bge-reranker-large --reranker-device cuda --reranker-batch-size 16 --limit 10
python -m commerce_rag_ops.cli eval --eval-filename challenge.jsonl --backend qdrant --embedding-backend auto --generator openai-compatible --reranker-model BAAI/bge-reranker-large --reranker-device cuda --reranker-batch-size 16 --limit 10
```

Observed `humanlike_single_turn_resolvable` Qdrant+BGE+reranker first-10 result:

- `exact_recall@5`: 0.5
- `acceptable_recall@5`: 0.6
- `entity_accuracy@5`: 0.6
- `aspect_accuracy@5`: 0.8
- `forbidden_rate@5`: 0.0
- `action_accuracy`: 0.7
- `citation_schema_ok`: 0.7
- `groundedness_proxy`: 0.71

Observed `challenge` Qdrant+BGE+reranker first-10 result:

- `exact_recall@5`: 0.1
- `acceptable_recall@5`: 0.1
- `entity_accuracy@5`: 0.1
- `aspect_accuracy@5`: 0.6
- `forbidden_rate@5`: 0.2
- `citation_schema_ok`: 0.3

Interpretation:

- Strong retrieval materially improves resolvable single-turn entity/evidence recall on the smoke set.
- The natural-query router update materially improves resolvable action/citation behavior on the smoke set: before the router fix, the same Qdrant+BGE+reranker first-10 run had `action_accuracy=0.1` and `citation_schema_ok=0.1`; after the fix both are `0.7`.
- Challenge remains low and shows hard-negative confusion; this reinforces the P1 need for entity candidate retrieval, retrieval planning, and facet/hard-negative-aware reranking.

## Remaining Work

P0 follow-up still needs full-size, non-smoke strong-retrieval reports:

- BGE-large embedding + no reranker
- BGE-large embedding + BGE-reranker-large
- Qdrant + BGE-large + BGE-reranker-large

P1 remains open:

- Entity Candidate Retrieval
- Query to retrieval plan
- Facet-aware retrieval
- action router refactor beyond the P0 clarify guard

## P1 Entity Candidate Retrieval Pass

Added:

- `src/commerce_rag_ops/entity_retrieval.py`
- `AgentState.entity_retrieval`
- `AgentState.entity_candidates`
- `AgentState.selected_entity`

Design:

- Build product profiles from `processed/chunks.jsonl`, not only `raw/products.jsonl`, because the repaired humanlike/challenge splits target scale Amazon products.
- Score candidates with SKU aliases, lexical product title overlap, semantic profile-token similarity, and category intent.
- Before semantic memory search, append a high-confidence product constraint to the retrieval query.
- After search, keep only chunks for the selected product plus neutral policy chunks.
- If the query needs a specific product but no unique/high-confidence entity is available, the action router can choose `clarify`.

Verification added:

```bash
pytest tests/test_core.py -q -k "entity_candidate or context_required_reference or structured_entity_filter"
pytest -q
```

Observed:

- `4 passed`
- Full regression after P1 entity retrieval: `45 passed`
- The natural query `how is the battery life of the nira laser device?` selects product `B08P2DZB4X` from scale product profile text.
- A confused retriever returning a wrong product first is constrained back to the selected entity.

Real LLM smoke after P1 entity retrieval:

```bash
python -m commerce_rag_ops.cli eval --eval-filename humanlike_context_required.jsonl --generator openai-compatible --reranker-model none --limit 10 --output reports/humanlike_context_required_report.md
python -m commerce_rag_ops.cli eval --eval-filename humanlike_single_turn_resolvable.jsonl --generator openai-compatible --reranker-model none --limit 10 --output reports/humanlike_single_turn_resolvable_report.md
```

Observed `humanlike_context_required` first-10:

- `action_accuracy`: 1.0
- `citation_leak_rate`: 0.0
- `citation_schema_ok`: 1.0

Observed `humanlike_single_turn_resolvable` local weak-retrieval first-10:

- `exact_recall@5`: 0.3
- `acceptable_recall@5`: 0.3
- `entity_accuracy@5`: 0.3
- `action_accuracy`: 0.7
- `citation_schema_ok`: 0.7

Known limitation:

- This is the first P1 pass. It does not yet implement the full structured retrieval plan, required-facet fanout, or hard-negative reranking matrix from the repair plan.

## P1 Retrieval Plan and Facet-Aware Evidence Pass

Added:

- `src/commerce_rag_ops/retrieval_plan.py`
- `AgentState.structured_retrieval_plan`
- Facet-aware entity evidence completion in `EntityCandidateRetriever.complete_entity_evidence()`

Design:

- Build a structured retrieval plan with `intent`, `entity_need`, `facets`, `sources`, `must_have`, and `should_not`.
- Infer facets from user language, including `skin_scent`, `quality_damage`, `digital_license`, `battery_power`, `price_value`, `delivery`, `refund_return`, `missing_parts`, and `general_support`.
- When a unique entity is selected, keep same-product contexts and complete missing product/profile plus required-facet evidence from the processed chunk index.
- Record the structured plan in semantic memory diagnostics, memory read output, and `retrieve` trace events.

Verification:

```bash
python -m compileall src
pytest tests/test_core.py -q -k "entity_candidate or context_required_reference or eval_runs"
pytest -q
```

Observed:

- Focused retrieval tests: `5 passed`
- Full regression after retrieval plan/facet pass: `46 passed`

Real LLM smoke after retrieval plan/facet pass:

```bash
python -m commerce_rag_ops.cli eval --eval-filename humanlike_context_required.jsonl --generator openai-compatible --reranker-model none --limit 10 --output reports/humanlike_context_required_report.md
python -m commerce_rag_ops.cli eval --eval-filename humanlike_single_turn_resolvable.jsonl --generator openai-compatible --reranker-model none --limit 10 --output reports/humanlike_single_turn_resolvable_report.md
```

Observed `humanlike_context_required` first-10:

- `action_accuracy`: 1.0
- `citation_leak_rate`: 0.0
- `citation_schema_ok`: 1.0

Observed `humanlike_single_turn_resolvable` local weak-retrieval first-10:

- `exact_recall@5`: 0.3
- `acceptable_recall@5`: 0.3
- `entity_accuracy@5`: 0.3
- `aspect_accuracy@5`: 0.7
- `action_accuracy`: 0.7
- `citation_schema_ok`: 0.7
- `answer_citation_recall`: 0.5583

Known limitation:

- The plan is rule-based. It does not yet use a real LLM planner, and hard-negative rerank penalties are still pending.
