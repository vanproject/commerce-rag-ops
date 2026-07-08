# Frozen Heldout Eval Summary

This report summarizes the current frozen/designed heldout artifacts already written under `reports/`.
All referenced eval reports were generated with real `openai-compatible` LLM calls; no template generator is used for heldout results.

## Retrieval / Support Eval

| Split | Scope | N | backend | embedding | reranker | llm | exact@5 | acceptable@5 | entity@5 | aspect@5 | forbidden@5 | action_acc | citation_schema | Report |
|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| humanlike_blind | historical-full | 200 | local | local-token-cosine | none | deepseek-v4-flash | 0.06 | 0.125 | 0.13 | 0.65 | 0.05 | n/a | 0.175 | `reports/humanlike_blind_report.md` |
| humanlike_single_turn_resolvable | smoke | 10 | local | local-token-cosine | none | deepseek-v4-flash | 0.3 | 0.3 | 0.3 | 0.7 | 0.0 | 0.7 | 0.7 | `reports/humanlike_single_turn_resolvable_report.md` |
| humanlike_context_required | smoke | 10 | local | local-token-cosine | none | deepseek-v4-flash | 0.0 | 0.0 | 0.0 | 0.8 | 0.04 | 1.0 | 1.0 | `reports/humanlike_context_required_report.md` |
| challenge | full | 100 | local | local-token-cosine | none | deepseek-v4-flash | 0.05 | 0.08 | 0.08 | 0.48 | 0.0185 | n/a | 0.46 | `reports/challenge_report.md` |

## Strong Retrieval Smoke Matrix

These rows are smoke runs, not full heldout runs; they are kept separate until the full matrix is regenerated.

| Split | Profile | Scope | N | backend | embedding | reranker | llm | exact@5 | acceptable@5 | entity@5 | aspect@5 | forbidden@5 | action_acc | citation_schema | Report |
|---|---|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| humanlike_single_turn_resolvable | qdrant+bge+reranker | smoke | 10 | qdrant | BAAI/bge-large-en-v1.5 | BAAI/bge-reranker-large | deepseek-v4-flash | 0.5 | 0.6 | 0.6 | 0.8 | 0.0 | 0.7 | 0.7 | `reports/humanlike_single_turn_resolvable_qdrant_bge_reranker_report.md` |
| challenge | qdrant+bge+reranker | smoke | 10 | qdrant | BAAI/bge-large-en-v1.5 | BAAI/bge-reranker-large | deepseek-v4-flash | 0.1 | 0.1 | 0.1 | 0.6 | 0.2 | 0.1 | 0.3 | `reports/challenge_qdrant_bge_reranker_report.md` |

## Answer Groundedness

| Split | N | Judge model | Business QA Pass | final_groundedness | claim_support | unsupported_claim | citation_schema | required_facet | Report |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| humanlike_blind | 200 | deepseek-v4-flash | 0.005 | 0.005 | 0.9155 | 0.0279 | 0.205 | 0.495 | `reports/humanlike_blind_groundedness_report.md` |
| challenge | 100 | deepseek-v4-flash | 0.09 | 0.11 | 0.87 | 0.0443 | 0.52 | 0.53 | `reports/challenge_groundedness_report.md` |

## Safety / Memory

| Split | N | Key metrics | Report |
|---|---:|---|---|
| refusal_safety_heldout | 50 | pass_rate=1.0, refusal_rate=1.0, citation_leak_rate=0.0 | `reports/refusal_eval_report.md` |
| multiturn_memory_heldout | 50 | carryover=0.8000, wrong_entity_leak=0.0000, privacy_block=1.0000, success=0.8400 | `reports/memory_eval_report.md` |

## Notes

- `humanlike_blind` remains in this table for historical comparability; post-repair primary single-turn quality should focus on `humanlike_single_turn_resolvable` and `humanlike_context_required`.
- Strong retrieval rows currently present are smoke runs. Full local/BGE/BGE+reranker/Qdrant matrix regeneration remains open.
- Groundedness rows are older full heldout judge runs and still show the remaining citation/facet/action-contract gap.
