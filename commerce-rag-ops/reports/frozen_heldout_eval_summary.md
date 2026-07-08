# Frozen Heldout Eval Summary

This report summarizes the designed-scale heldout eval run with real OpenAI-compatible LLM calls. Generation, answer production, and LLM-as-Judge used `deepseek-v4-flash`; no template generator was used. Retrieval used the local backend with `--reranker-model none`.

## Retrieval / Support Eval

| Split | N | exact_recall@5 | acceptable_recall@5 | entity_accuracy@5 | aspect_accuracy@5 | forbidden_rate@5 | Report |
|---|---:|---:|---:|---:|---:|---:|---|
| humanlike_blind | 200 | 0.06 | 0.125 | 0.13 | 0.65 | 0.05 | `reports/humanlike_blind_report.md` |
| challenge | 100 | 0.05 | 0.08 | 0.08 | 0.48 | 0.0185 | `reports/challenge_report.md` |

## Answer Groundedness

| Split | N | Judge model | Business QA Pass Rate | final_groundedness_pass_rate | claim_support_rate | unsupported_claim_rate | citation_schema_pass_rate | required_facet_pass_rate | Report |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| humanlike_blind | 200 | deepseek-v4-flash | 0.005 | 0.005 | 0.9155 | 0.0279 | 0.205 | 0.495 | `reports/humanlike_blind_groundedness_report.md` |
| challenge | 100 | deepseek-v4-flash | 0.09 | 0.11 | 0.87 | 0.0443 | 0.52 | 0.53 | `reports/challenge_groundedness_report.md` |

## Safety / Memory

| Split | N | Key metrics | Report |
|---|---:|---|---|
| refusal_safety_heldout | 50 | pass_rate=0.82, refusal_rate=0.82, citation_leak_rate=0.18 | `reports/refusal_eval_report.md` |
| multiturn_memory_heldout | 50 | carryover=1.0, wrong_entity_leak=0.0, privacy_block=1.0, success=0.58 | `reports/memory_heldout_report.md` |

## Artifacts

| Artifact | Path |
|---|---|
| Humanlike retrieval/support report | `reports/humanlike_blind_report.md` |
| Challenge retrieval/support report | `reports/challenge_report.md` |
| Humanlike groundedness report | `reports/humanlike_blind_groundedness_report.md` |
| Challenge groundedness report | `reports/challenge_groundedness_report.md` |
| Humanlike groundedness rows | `reports/humanlike_blind_groundedness_rows.jsonl` |
| Challenge groundedness rows | `reports/challenge_groundedness_rows.jsonl` |
| Refusal/safety report | `reports/refusal_eval_report.md` |
| Multi-turn memory heldout report | `reports/memory_heldout_report.md` |

## Notes

- Groundedness rows were written incrementally so the run could survive API interruptions and resume without using template/mock substitutes.
- Low Business QA Pass is mainly driven by blind retrieval and citation/facet failures. Judge claim support is comparatively high, but citation schema pass and required facet pass are low.
- These heldout results should be treated as the main quality signal; the old scripted regression benchmark remains useful only for engineering regression.
