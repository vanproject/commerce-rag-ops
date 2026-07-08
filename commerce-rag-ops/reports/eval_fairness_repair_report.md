# Eval Fairness Repair Report

本报告由 `python -m commerce_rag_ops.cli repair-evalsets` 生成。

- Source rows: 200
- Resolvable rows: 29
- Context-required rows: 171
- Source repairs: 12
- Challenge repairs: 12
- Resolvable output: `E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_single_turn_resolvable.jsonl`
- Context-required output: `E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_context_required.jsonl`

## Forbidden Evidence Repairs

| query_id | changes |
| --- | --- |
| H-0004 | removed_target_from_wrong_product_ids |
| H-0005 | removed_target_from_wrong_product_ids |
| H-0006 | removed_target_from_wrong_product_ids |
| H-0016 | removed_target_from_wrong_product_ids |
| H-0017 | removed_target_from_wrong_product_ids |
| H-0018 | removed_target_from_wrong_product_ids |
| H-0028 | removed_target_from_wrong_product_ids |
| H-0029 | removed_target_from_wrong_product_ids |
| H-0030 | removed_target_from_wrong_product_ids |
| H-0040 | removed_target_from_wrong_product_ids |
| H-0041 | removed_target_from_wrong_product_ids |
| H-0042 | removed_target_from_wrong_product_ids |
| C-0004 | removed_target_from_wrong_product_ids |
| C-0005 | removed_target_from_wrong_product_ids |
| C-0006 | removed_target_from_wrong_product_ids |
| C-0016 | removed_target_from_wrong_product_ids |
| C-0017 | removed_target_from_wrong_product_ids |
| C-0018 | removed_target_from_wrong_product_ids |
| C-0028 | removed_target_from_wrong_product_ids |
| C-0029 | removed_target_from_wrong_product_ids |
| C-0030 | removed_target_from_wrong_product_ids |
| C-0040 | removed_target_from_wrong_product_ids |
| C-0041 | removed_target_from_wrong_product_ids |
| C-0042 | removed_target_from_wrong_product_ids |
