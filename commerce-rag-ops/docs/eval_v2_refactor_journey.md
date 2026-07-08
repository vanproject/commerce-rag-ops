# CommerceRAG Ops Eval V2 Refactor Journey

## Scope

本次重构按 V2 方案把评测口径拆成两层：

- `scripted_regression`：保留旧 scripted golden，用于索引、检索、rerank、citation schema、agent pipeline 回归。
- `humanlike_blind`：新增主评测口径，query 由真实 OpenAI-compatible LLM API 生成，检索默认不传 oracle sources，并把主指标转向 answer-level factual support。

## Implemented Changes

### Phase 1: Scripted Regression Naming

- 新增 `data/eval/scripted_regression.jsonl`，内容从旧 `golden.jsonl` 迁移。
- `run_evaluation()` 默认优先读取 `scripted_regression.jsonl`，缺失时兼容回落到 `golden.jsonl`。
- `scale_builder` 后续会同时写 `scripted_regression.jsonl` 和 `golden.jsonl`，保留旧 SQL/文档入口兼容。
- `write_eval_report()` 对 scripted report 加注：

```text
This is a scripted regression benchmark, not a production generalization benchmark.
```

### Phase 2: Blind Retrieval Eval

- `run_evaluation()` 新增 `use_oracle_sources: bool = False`，默认不再把 `row["sources"]` 传给 retriever。
- `run_ablation()` 同步新增 `use_oracle_sources: bool = False`。
- CLI 新增 `--use-oracle-sources`，只用于辅助诊断，不是默认主指标。

### Phase 3: Relevance Level Metrics

新增 `RelevanceLevel`：

```python
EXACT = 2
ACCEPTABLE = 1
WRONG = 0
FORBIDDEN = -1
```

报告新增 retrieval V2 指标：

- `exact_recall@5`
- `acceptable_recall@5`
- `entity_accuracy@5`
- `aspect_accuracy@5`
- `forbidden_rate@5`

旧 `relevant_doc_ids` 会自动映射成 exact/wrong，新 `required_evidence` / `forbidden_evidence` schema 会启用 exact/acceptable/forbidden 分层。

### Phase 4: Humanlike Evalset Builder

新增 `src/commerce_rag_ops/humanlike_eval.py` 和 CLI：

```powershell
python -m commerce_rag_ops.cli build-humanlike-eval `
  --input data/scale/rag_documents.jsonl `
  --output data/eval/humanlike_blind.jsonl `
  --n 300
```

该 builder 只使用真实 `OpenAICompatibleGenerator`，不提供 template/mock fallback。输出 schema 包含：

- `suite`
- `source_mode`
- `target_entities`
- `required_evidence.exact_doc_ids`
- `required_evidence.acceptable_doc_ids`
- `required_evidence.required_facets`
- `forbidden_evidence.wrong_product_ids`
- `forbidden_evidence.wrong_aspects`
- `answer_checks.must_not_claim`

### Phase 5: Leakage Audit

新增 CLI：

```powershell
python -m commerce_rag_ops.cli audit-eval-leakage `
  --input data/eval/humanlike_blind.jsonl `
  --docs data/scale/rag_documents.jsonl
```

输出并写入 `reports/humanlike_blind_leakage_report.md`：

- `title_overlap_rate`
- `entity_leak_rate`
- `aspect_leak_rate`
- `category_leak_rate`
- `template_pattern_rate`

### Phase 6: Deterministic Grounding Checks

新增 `src/commerce_rag_ops/grounding_checks.py`：

- citation schema check
- tool citation schema check
- entity consistency check
- numeric consistency check
- policy consistency check
- forbidden claim check
- required facet check

核心入口：

```python
run_deterministic_grounding_checks(...)
```

输出 `deterministic_grounding_pass` 和失败明细。

### Phase 7: Real API LLM-as-Judge

新增 `src/commerce_rag_ops/judge.py`：

- `OpenAICompatibleGroundednessJudge`
- `judge_answer_groundedness(...)`
- `normalize_groundedness_judge_result(...)`

Judge prompt 明确要求：

- 只能根据 retrieved contexts 和 tool results 判断。
- 不使用外部知识。
- 不奖励流畅表达。
- 逐条抽取 claim 并判定 support。
- 政策、订单、退款、价格、库存、权限相关 claim 必须严格检查。

本模块只走真实 OpenAI-compatible API，不支持 template/mock。

### Phase 8: Groundedness Report

新增 `run_groundedness_evaluation()` 和 `write_groundedness_report()`，CLI：

```powershell
python -m commerce_rag_ops.cli groundedness-eval `
  --eval-filename humanlike_blind.jsonl `
  --limit 20 `
  --generator openai-compatible
```

报告写入：

```text
reports/humanlike_blind_groundedness_report.md
```

核心指标：

- `Business QA Pass Rate`
- `final_groundedness_pass_rate`
- `claim_support_rate`
- `unsupported_claim_rate`
- `citation_schema_pass_rate`
- `entity_consistency_pass_rate`
- `numeric_consistency_pass_rate`
- `policy_consistency_pass_rate`
- `forbidden_claim_pass_rate`
- `required_facet_pass_rate`

## Real API Guardrail

以下 CLI 路径会拒绝 `--generator template`：

- `eval`
- `gate`
- `refusal-eval`
- `combined-eval`
- `judge-eval`
- `groundedness-eval`

原因：本轮目标明确要求只允许真实 API，不使用 template。

## Verification Snapshot

- `python -m compileall src` passed.
- Focused pytest passed:

```powershell
pytest -q tests/test_core.py::test_llm_judge_json_parsing_and_thresholds tests/test_core.py::test_citation_contract_validates_answer_markers_and_grounding
```

- Full pytest passed:

```powershell
pytest -q
# 31 passed in 147.90s
```

- CLI discovery passed with `PYTHONPATH=src`:

```powershell
python -m commerce_rag_ops.cli --help
python -m commerce_rag_ops.cli eval --help
python -m commerce_rag_ops.cli groundedness-eval --help
python -m commerce_rag_ops.cli build-humanlike-eval --help
```

- Real API connectivity passed:

```powershell
python -m commerce_rag_ops.cli llm-check
# ok=true, model=deepseek-v4-flash
```

## Remaining Notes

- `golden.jsonl` is intentionally kept for compatibility; V2 code paths use `scripted_regression.jsonl` by default.
- `groundedness_proxy` remains available as a retrieval diagnostic, but should not be presented as answer groundedness.
- Humanlike query generation and judge evaluation require configured `COMMERCE_RAG_LLM_API_KEY` and optional judge endpoint/model env vars.

## Designed Scale Expansion

已按 frozen heldout 设计规模补齐四个评测 split，全部自然语言 query/turns 由真实 OpenAI-compatible API 生成，未使用 template/mock：

| Split | File | Target | Actual |
|---|---|---:|---:|
| humanlike normal | `data/eval/humanlike_blind.jsonl` | 200 | 200 |
| challenge | `data/eval/challenge.jsonl` | 100 | 100 |
| refusal / safety | `data/eval/refusal_safety_heldout.jsonl` | 50 | 50 |
| multi-turn memory | `data/eval/multiturn_memory_heldout.jsonl` | 50 | 50 |

新增 manifest：

```text
data/eval/frozen_heldout_manifest.json
```

Leakage audit 已重算：

| Split | title_overlap_rate | entity_leak_rate | aspect_leak_rate | category_leak_rate | template_pattern_rate |
|---|---:|---:|---:|---:|---:|
| humanlike_blind | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| challenge | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

额外做了 stricter exact-doc title token audit（阈值 0.2），`humanlike_blind` 和 `challenge` 均为 0 个失败样本。第一轮真实 API 生成后有部分品牌/标题词残留，随后只针对泄漏 query 继续用真实 API 重写，未使用 template 兜底。

报告文件：

```text
reports/humanlike_blind_leakage_report.md
reports/challenge_leakage_report.md
```

本轮扩容验证：

```powershell
python -m compileall src
pytest -q
# 31 passed in 234.63s
```
