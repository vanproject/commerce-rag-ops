# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: challenge
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\challenge.jsonl
- Oracle sources: False

## 摘要

- 样本数: 100
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 0.018
- Recall@5: 0.0282
- MRR: 0.054
- NDCG@5: 0.0299
- exact_recall@5: 0.05
- acceptable_recall@5: 0.08
- entity_accuracy@5: 0.08
- aspect_accuracy@5: 0.48
- forbidden_rate@5: 0.0185
- 引用率: 0.58
- Citation schema OK: 0.46
- Answer citation precision/recall: 0.46 / 0.3517
- Citation grounded rate: 0.58
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.46
- 延迟 p50/p95: 51 ms / 48019 ms
- Embedding 模型: local-token-cosine
- Reranker 模型: none
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 48 | 0.0083 | 0.0174 | 0.0312 | 0.0178 | 0.8333 | 0.7708 | 0.7708 / 0.6181 | 1.0 |
| recommendation | 25 | 0.024 | 0.0367 | 0.068 | 0.0359 | 0.36 | 0.16 | 0.16 / 0.09 | 1.0 |
| support | 27 | 0.0296 | 0.0395 | 0.0815 | 0.0458 | 0.3333 | 0.1852 | 0.1852 / 0.1204 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 100 | 0.018 | 0.0282 | 0.054 | 0.0299 | 0.58 | 0.46 | 0.46 / 0.3517 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 105 | 9 |
| dense | 130 | 2 |
| forced_fallback | 142 | 0 |
| policy_fallback | 7 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | bm25: 2, dense: 1 |
| recommendation | bm25: 3, dense: 1 |
| support | bm25: 4 |

## Agentic 证据诊断

- 重试率: 0.88

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 26, escalate: 11, refuse: 63 |
| 尝试次数 | 1: 12, 2: 88 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_policy | 18 |
| missing_product_context | 1 |
| missing_review | 4 |
| missing_structured_entity | 11 |
| no_context | 5 |
| privacy_violation | 5 |
| safety_boundary | 2 |
| unknown_intent | 51 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 54 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_policy: 7, missing_product_context: 1, missing_review: 1, missing_structured_entity: 4, no_context: 5, privacy_violation: 5, safety_boundary: 2, unknown_intent: 23 |
| recommendation | missing_policy: 6, missing_review: 2, missing_structured_entity: 5, unknown_intent: 11 |
| support | missing_policy: 5, missing_review: 1, missing_structured_entity: 2, unknown_intent: 17 |

## 原始 JSON

```json
{
  "suite": "challenge",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\challenge.jsonl",
  "use_oracle_sources": false,
  "n": 100,
  "retrieval_backend": "local",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "local-token-cosine",
    "embedding_backend": "local",
    "reranker_model": "none",
    "llm_model": "deepseek-v4-flash"
  },
  "retrieval": {
    "precision@5": 0.018,
    "recall@5": 0.0282,
    "mrr": 0.054,
    "ndcg@5": 0.0299,
    "exact_recall@5": 0.05,
    "acceptable_recall@5": 0.08,
    "entity_accuracy@5": 0.08,
    "aspect_accuracy@5": 0.48,
    "forbidden_rate@5": 0.0185
  },
  "support_quality": {
    "citation_ok": 0.58,
    "citation_schema_ok": 0.46,
    "answer_citation_precision": 0.46,
    "answer_citation_recall": 0.3517,
    "citation_grounded_rate": 0.58,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.46
  },
  "latency": {
    "p50_ms": 51,
    "p95_ms": 48019
  },
  "by_intent": {
    "customer_ops": {
      "n": 48,
      "retrieval": {
        "precision@5": 0.0083,
        "recall@5": 0.0174,
        "mrr": 0.0312,
        "ndcg@5": 0.0178
      },
      "support_quality": {
        "citation_ok": 0.8333,
        "citation_schema_ok": 0.7708,
        "answer_citation_precision": 0.7708,
        "answer_citation_recall": 0.6181,
        "citation_grounded_rate": 0.8333,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.4583
      }
    },
    "recommendation": {
      "n": 25,
      "retrieval": {
        "precision@5": 0.024,
        "recall@5": 0.0367,
        "mrr": 0.068,
        "ndcg@5": 0.0359
      },
      "support_quality": {
        "citation_ok": 0.36,
        "citation_schema_ok": 0.16,
        "answer_citation_precision": 0.16,
        "answer_citation_recall": 0.09,
        "citation_grounded_rate": 0.36,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.56
      }
    },
    "support": {
      "n": 27,
      "retrieval": {
        "precision@5": 0.0296,
        "recall@5": 0.0395,
        "mrr": 0.0815,
        "ndcg@5": 0.0458
      },
      "support_quality": {
        "citation_ok": 0.3333,
        "citation_schema_ok": 0.1852,
        "answer_citation_precision": 0.1852,
        "answer_citation_recall": 0.1204,
        "citation_grounded_rate": 0.3333,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.3704
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 100,
      "retrieval": {
        "precision@5": 0.018,
        "recall@5": 0.0282,
        "mrr": 0.054,
        "ndcg@5": 0.0299
      },
      "support_quality": {
        "citation_ok": 0.58,
        "citation_schema_ok": 0.46,
        "answer_citation_precision": 0.46,
        "answer_citation_recall": 0.3517,
        "citation_grounded_rate": 0.58,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.46
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 105,
      "dense": 130,
      "forced_fallback": 142,
      "policy_fallback": 7
    },
    "relevant_hit_signal_counts": {
      "bm25": 9,
      "dense": 2
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "bm25": 2,
        "dense": 1
      },
      "recommendation": {
        "bm25": 3,
        "dense": 1
      },
      "support": {
        "bm25": 4
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 26,
      "escalate": 11,
      "refuse": 63
    },
    "attempt_counts": {
      "1": 12,
      "2": 88
    },
    "retry_rate": 0.88,
    "evidence_gap_counts": {
      "missing_policy": 18,
      "missing_product_context": 1,
      "missing_review": 4,
      "missing_structured_entity": 11,
      "no_context": 5,
      "privacy_violation": 5,
      "safety_boundary": 2,
      "unknown_intent": 51
    },
    "citation_failure_counts": {
      "missing_answer_citation": 54
    },
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "missing_policy": 7,
        "missing_product_context": 1,
        "missing_review": 1,
        "missing_structured_entity": 4,
        "no_context": 5,
        "privacy_violation": 5,
        "safety_boundary": 2,
        "unknown_intent": 23
      },
      "recommendation": {
        "missing_policy": 6,
        "missing_review": 2,
        "missing_structured_entity": 5,
        "unknown_intent": 11
      },
      "support": {
        "missing_policy": 5,
        "missing_review": 1,
        "missing_structured_entity": 2,
        "unknown_intent": 17
      }
    }
  },
  "retrieval_rows": [
    {
      "query_id": "C-0001",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "ticket:T-004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-004",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0002",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00053",
        "product:PP-Baby_Products-B0B4H2MX2Q",
        "kb:KB001_return_refund_policy",
        "review:AS-All_Beauty-B0107QYW14-missing_parts",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00053",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0B4H2MX2Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0107QYW14-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0003",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B07N8JMJGY",
        "review:AS-All_Beauty-B00R1TAN7I-price_value",
        "review:RV-AMZREV-Software-04360",
        "product:PP-Software-B009HQ9UHC",
        "review:CL-All_Beauty-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07N8JMJGY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B00R1TAN7I-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-04360",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B009HQ9UHC",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-All_Beauty-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0004",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02752",
        "review:RV-AMZREV-All_Beauty-01245",
        "review:RV-AMZREV-All_Beauty-01895",
        "review:RV-AMZREV-All_Beauty-00838",
        "review:RV-AMZREV-All_Beauty-03699"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02752",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01245",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01895",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00838",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03699",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0005",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-006",
        "product:P-BABY-002",
        "ticket:T-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0006",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-SOFT-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0007",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0008",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0009",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0010",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0011",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B08229K7VC",
        "review:RV-AMZREV-Baby_Products-02912",
        "review:RV-AMZREV-All_Beauty-02556",
        "review:RV-AMZREV-Baby_Products-03455",
        "review:AS-All_Beauty-B08ZNLBJ5B-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B08229K7VC",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-02912",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02556",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-03455",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B08ZNLBJ5B-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0012",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "review:R-012",
        "review:R-003",
        "review:R-004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-004",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0013",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0014",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-012",
        "product:P-BABY-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0015",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-SOFT-001",
        "review:R-005"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0016",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03990",
        "review:RV-AMZREV-Baby_Products-02329",
        "review:RV-AMZREV-All_Beauty-04908",
        "review:RV-AMZREV-All_Beauty-02463",
        "product:PP-All_Beauty-B012Q9NGE4"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03990",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-02329",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04908",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02463",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B012Q9NGE4",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0017",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-006",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0018",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0019",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0020",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.25,
      "retrieved": [
        "review:CL-Baby_Products-delivery",
        "review:R-012",
        "ticket:T-002",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-delivery",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0021",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B00E5NH46Q",
        "product:PP-Software-B07BKPFXTJ",
        "product:PP-Software-B01LXOU5PM",
        "product:PP-Software-B004T4LUPW",
        "review:RV-AMZREV-Software-02615"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00E5NH46Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B07BKPFXTJ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B01LXOU5PM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 22,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B004T4LUPW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-02615",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0022",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0023",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.5,
      "mrr": 0.5,
      "ndcg@5": 0.38685280723454163,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-01152",
        "product:PP-Baby_Products-B01E5E703G",
        "review:AS-Baby_Products-B07RRDX26B-skin_scent",
        "review:RV-AMZREV-Baby_Products-01123",
        "review:RV-AMZREV-All_Beauty-01536"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-01152",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B01E5E703G",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B07RRDX26B-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01123",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01536",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0024",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-02012",
        "product:PP-Software-B0054JZC6E",
        "review:AS-All_Beauty-B09XBSDCXP-price_value",
        "review:RV-AMZREV-Software-03489",
        "review:RV-AMZREV-Software-02381"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-02012",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B0054JZC6E",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B09XBSDCXP-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03489",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-02381",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0025",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00008",
        "ticket:FAQ-All_Beauty-0003",
        "product:PP-Software-B008IJTFYW",
        "product:PP-All_Beauty-B00J7QCNDU",
        "review:AS-All_Beauty-B07MMW5654-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00008",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:FAQ-All_Beauty-0003",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B008IJTFYW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B00J7QCNDU",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07MMW5654-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0026",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0027",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "ticket:T-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0028",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B072JX8LV5",
        "review:RV-AMZREV-All_Beauty-00686",
        "product:PP-All_Beauty-B007MB4YW0",
        "product:PP-All_Beauty-B08GYJY8F2",
        "product:PP-Baby_Products-B09ZRHJHLT"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00686",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B007MB4YW0",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B08GYJY8F2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B09ZRHJHLT",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0029",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0030",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-009"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-009",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0031",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0032",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0033",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-003",
        "product:P-SOFT-001",
        "review:R-006"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-SOFT-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-006",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0034",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-Baby_Products-B015QYB526",
        "review:AS-All_Beauty-B01IMEH6GG-price_value",
        "review:RV-AMZREV-Baby_Products-01611",
        "product:PP-Software-B0BJ867VQH",
        "product:PP-Baby_Products-B0C9V7CB9S"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B015QYB526",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01IMEH6GG-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01611",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B0BJ867VQH",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B0C9V7CB9S",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0035",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0036",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-006",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0037",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0038",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B076BMK9ZK",
        "review:RV-AMZREV-Baby_Products-02532",
        "review:RV-AMZREV-Baby_Products-00397",
        "review:RV-AMZREV-All_Beauty-00198",
        "review:AS-All_Beauty-B07KQ32Z8C-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B076BMK9ZK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-02532",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00397",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00198",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07KQ32Z8C-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 22,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0039",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0040",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B09FB5P849",
        "review:RV-AMZREV-Baby_Products-04124",
        "product:PP-Baby_Products-B0BZYVJDQW",
        "product:PP-Software-B00QH8YULY",
        "product:PP-Software-B0026PEP5S"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B09FB5P849",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-04124",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B0BZYVJDQW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00QH8YULY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Software-B0026PEP5S",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0041",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0042",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0043",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0044",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "review:R-004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-004",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0045",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-007",
        "ticket:T-004",
        "product:P-SOFT-002",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-007",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-004",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-SOFT-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0046",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01206",
        "product:PP-All_Beauty-B08P7PSMRR",
        "review:AS-Baby_Products-B0BNHXCLB7-delivery",
        "product:PP-Baby_Products-B0BKCZBDGF",
        "review:RV-AMZREV-All_Beauty-00309"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01206",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08P7PSMRR",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B0BNHXCLB7-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0BKCZBDGF",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00309",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0047",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "product:PP-Baby_Products-B07GL4D84M",
        "product:PP-Baby_Products-B0B4BHG5MP",
        "review:RV-AMZREV-Baby_Products-02321",
        "product:PP-Baby_Products-B0B9QPGPQW",
        "review:AS-Baby_Products-B0C48M1HNT-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B07GL4D84M",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0B4BHG5MP",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02321",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0B9QPGPQW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B0C48M1HNT-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0048",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B00L0T4VL4",
        "product:PP-Software-B00VMM22WE",
        "product:PP-Software-B097F45PYG",
        "product:PP-Software-B01BPPA75Q",
        "review:RV-AMZREV-Software-02162"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00L0T4VL4",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00VMM22WE",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B097F45PYG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B01BPPA75Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-02162",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0049",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "ticket:T-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0050",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-002",
        "ticket:T-001",
        "product:P-BEAUTY-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0051",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "ticket:T-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0052",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-02514",
        "review:RV-AMZREV-All_Beauty-04971",
        "review:RV-AMZREV-All_Beauty-04304",
        "review:RV-AMZREV-Baby_Products-00864",
        "product:PP-All_Beauty-B0916ZRQDG"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-02514",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04971",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 22,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00864",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0053",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.3333333333333333,
      "mrr": 1.0,
      "ndcg@5": 0.46927872602275644,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B000ARWL46",
        "review:AS-All_Beauty-B07ZQRX7FX-skin_scent",
        "review:RV-AMZREV-Baby_Products-04923",
        "product:PP-Baby_Products-B07PWWK5J8",
        "ticket:FAQ-Software-0156"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B000ARWL46",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07ZQRX7FX-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04923",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B07PWWK5J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0156",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0054",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-001",
        "review:R-007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-007",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0055",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0056",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "kb:KB001_return_refund_policy",
        "product:PP-All_Beauty-B0851C4YPC",
        "product:PP-Software-B008H3SW4I",
        "product:PP-Software-B06Y61GRLW",
        "review:RV-AMZREV-Baby_Products-04754"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0851C4YPC",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B008H3SW4I",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B06Y61GRLW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-04754",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0057",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "kb:KB001_return_refund_policy",
        "kb:KB004_shipping_delivery_policy",
        "product:PP-Software-B00FAS0MY6",
        "product:PP-Software-B00ARIXQTW",
        "review:RV-AMZREV-All_Beauty-00935"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B00FAS0MY6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00ARIXQTW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00935",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0058",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "review:R-002",
        "product:P-BEAUTY-001",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0059",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.3333333333333333,
      "mrr": 1.0,
      "ndcg@5": 0.46927872602275644,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-00005",
        "product:PP-Software-B097F45PYG",
        "review:AS-All_Beauty-B083BCSQGN-missing_parts",
        "review:RV-AMZREV-Baby_Products-00905",
        "ticket:FAQ-All_Beauty-0062"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B097F45PYG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B083BCSQGN-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00905",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0062",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0060",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B07BKPFXTJ",
        "review:AS-All_Beauty-B01BEYRHBA-battery_power",
        "review:RV-AMZREV-Software-01627",
        "product:PP-Software-B007ZGO7EM",
        "product:PP-Software-B0092V6N7M"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B07BKPFXTJ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01BEYRHBA-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-01627",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B007ZGO7EM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Software-B0092V6N7M",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0061",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 1.0,
      "ndcg@5": 0.3391602052736161,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
        "review:AS-Baby_Products-B07ZJ1L3VK-skin_scent",
        "review:AS-Baby_Products-B00ADJEU68-skin_scent",
        "review:AS-All_Beauty-B00N6WHTRG-skin_scent",
        "product:PP-All_Beauty-B07GDQPG12"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B07ZJ1L3VK-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B00ADJEU68-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B00N6WHTRG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0062",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "ticket:T-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0063",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-002",
        "review:R-004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-004",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0064",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B007EEHH1K",
        "review:AS-All_Beauty-B07MN1KJ15-skin_scent",
        "review:RV-AMZREV-Software-00007",
        "product:PP-Software-B000063W5A",
        "review:CL-All_Beauty-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B007EEHH1K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07MN1KJ15-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00007",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B000063W5A",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-All_Beauty-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0065",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.25,
      "mrr": 0.5,
      "ndcg@5": 0.24630238874073,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B09TXTPS8D",
        "product:PP-Baby_Products-B000BNCA4K",
        "product:PP-Baby_Products-B0BSXM885Q",
        "product:PP-Baby_Products-B0BQRQLXJ6",
        "review:RV-AMZREV-Baby_Products-00978"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B09TXTPS8D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B000BNCA4K",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B0BSXM885Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0BQRQLXJ6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-00978",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0066",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0067",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-012",
        "ticket:T-006"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0068",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-011",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0069",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-SOFT-002",
        "review:R-007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-007",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0070",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0071",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-03433",
        "review:RV-AMZREV-Baby_Products-00169",
        "review:RV-AMZREV-Baby_Products-01941",
        "review:RV-AMZREV-Baby_Products-02299",
        "review:AS-All_Beauty-B0046BPTI2-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-03433",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00169",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01941",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-02299",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B0046BPTI2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0072",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0073",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 0.2,
      "ndcg@5": 0.13120507751234178,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-Baby_Products-B07J2JLRJH-price_value",
        "product:PP-Software-B00A7V0Z9I",
        "review:RV-AMZREV-Baby_Products-04998",
        "review:RV-AMZREV-All_Beauty-00091",
        "ticket:FAQ-All_Beauty-0007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B07J2JLRJH-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00A7V0Z9I",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04998",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00091",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0007",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0074",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-004",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-004",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0075",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-012",
        "ticket:T-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0076",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B0BQ7F2RW9",
        "product:PP-Baby_Products-B0B7BW2HR5",
        "review:RV-AMZREV-All_Beauty-04555",
        "review:RV-AMZREV-All_Beauty-00191",
        "review:RV-AMZREV-Baby_Products-04232"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0BQ7F2RW9",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0B7BW2HR5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04555",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00191",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-04232",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0077",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0078",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-001",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0079",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-006",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0080",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-002",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0081",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-005",
        "review:R-012"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0082",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-03923",
        "product:PP-Baby_Products-B0B1F74MZH",
        "review:AS-All_Beauty-B00KCTER3U-skin_scent",
        "review:AS-All_Beauty-B092Z6B3GR-price_value",
        "review:AS-Software-B00P03D4D2-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-03923",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0B1F74MZH",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00KCTER3U-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 25,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B092Z6B3GR-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B00P03D4D2-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0083",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-SOFT-002",
        "review:R-007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-007",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0084",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B083BCSQGN",
        "review:AS-All_Beauty-B01BZVADRW-price_value",
        "review:RV-AMZREV-All_Beauty-00734",
        "product:PP-Software-B008KC1SOM",
        "review:RV-AMZREV-All_Beauty-01488"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B083BCSQGN",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01BZVADRW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00734",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B008KC1SOM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01488",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0085",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B072JX8LV5",
        "review:AS-All_Beauty-B00R1TAN7I-delivery",
        "review:RV-AMZREV-All_Beauty-01062",
        "product:PP-Software-B07GBYBWFG",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B00R1TAN7I-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01062",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B07GBYBWFG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0086",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-003",
        "review:R-004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-004",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0087",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-SOFT-002",
        "review:R-008"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-008",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0088",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B01N0IG90U",
        "review:RV-AMZREV-All_Beauty-04029",
        "product:PP-Software-B00I4MMX7E",
        "product:PP-All_Beauty-B0865H5R1X",
        "product:PP-Software-B01LDIQ97K"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B01N0IG90U",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04029",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B00I4MMX7E",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0865H5R1X",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Software-B01LDIQ97K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0089",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "review:R-011"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-011",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0090",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0091",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-001",
        "review:R-005"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0092",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03759",
        "product:PP-All_Beauty-B09NCJHDX3",
        "review:AS-All_Beauty-B07ZJKVVLW-price_value",
        "review:AS-Software-B00E5NGYVM-digital_license",
        "review:AS-Baby_Products-B00ADJEU68-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03759",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B09NCJHDX3",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B00E5NGYVM-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B00ADJEU68-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0093",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:R-002",
        "ticket:T-006",
        "review:R-012",
        "ticket:T-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-006",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:R-012",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0094",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BEAUTY-001",
        "review:R-002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0095",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:P-BABY-002",
        "product:P-BABY-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:P-BABY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0096",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01695",
        "product:PP-All_Beauty-B0929B8N9L",
        "review:RV-AMZREV-Software-02887",
        "review:RV-AMZREV-Software-00446",
        "review:RV-AMZREV-Software-00447"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01695",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0929B8N9L",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-02887",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-00446",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 30,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-00447",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0097",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B07TK6647L",
        "review:AS-All_Beauty-B07S5GYK14-skin_scent",
        "review:RV-AMZREV-All_Beauty-02810",
        "product:PP-Baby_Products-B0BG6JYNQX",
        "review:CL-Baby_Products-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07TK6647L",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07S5GYK14-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02810",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0BG6JYNQX",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-Baby_Products-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "C-0098",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:T-002",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-003",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "C-0099",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 0.0,
      "entity_accuracy@5": 0.0,
      "aspect_accuracy@5": 0.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B07BKPFXTJ",
        "product:PP-Software-B00IK9R96Q",
        "product:PP-Software-B008Z2NVGK",
        "product:PP-Software-B005SE8IFW",
        "review:RV-AMZREV-Software-01627"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B07BKPFXTJ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00IK9R96Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B008Z2NVGK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005SE8IFW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-01627",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 25,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "C-0100",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.3333333333333333,
      "mrr": 0.2,
      "ndcg@5": 0.18154179253735267,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B0BPB8Z23R",
        "review:AS-Baby_Products-B0BW8SNCF2-quality_damage",
        "review:RV-AMZREV-All_Beauty-00792",
        "product:PP-Baby_Products-B082LHWK6D",
        "ticket:FAQ-All_Beauty-0177"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0BPB8Z23R",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BW8SNCF2-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00792",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B082LHWK6D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0177",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        }
      ]
    }
  ],
  "support_rows": [
    {
      "query_id": "C-0001",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.75,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 3,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I understand you'd like a refund because the item was too small. Unfortunately, based on the information I've retrieved, there are no documented policies or past cases that specifically address returns for sizing/fit preferences. The availa"
    },
    {
      "query_id": "C-0002",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0003",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0004",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0005",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0006",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The overall rating you see is an average calculated from all submitted reviews for that product. For example, from our product data:\n\n- **PDF Studio Pro License** has an average rating of **4.2** out of 5 from **810 ratings** [tool:sql.prod"
    },
    {
      "query_id": "C-0007",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_review"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-004",
          "chunk_id": "490e079c4c5a7f26",
          "rank": 2,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 3,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-001",
          "chunk_id": "c248dad601bafaf8",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m sorry to hear that your beauty order hasn’t arrived even though the tracking shows it as delivered, and that this has happened multiple times. That must be very frustrating.  \n\nBased on the information currently available to me, I don’t"
    },
    {
      "query_id": "C-0008",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0009",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "privacy_violation",
        "no_context"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0010",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information available, here is the exact review text for the HydraGlow Vitamin C Serum: \n\n> \"review for hydraglow vitamin c serum. rating 2. the bottle arrived leaking and the pump was broken. i wanted a refund because half the"
    },
    {
      "query_id": "C-0011",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0012",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-004",
          "chunk_id": "490e079c4c5a7f26",
          "rank": 2,
          "doc_type": "review"
        },
        {
          "source": "review",
          "doc_id": "R-012",
          "chunk_id": "00becedaf80dda0e",
          "rank": 3,
          "doc_type": "review"
        },
        {
          "source": "review",
          "doc_id": "R-003",
          "chunk_id": "b1f9d8d8d461916a",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information provided, I’m not able to address your concern about the app’s customer‑satisfaction policies. The product search and review results I have access to do not contain any app product or a review that says “lots of fun"
    },
    {
      "query_id": "C-0013",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 3,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 3,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m sorry, but based on the information available, I cannot provide the return or refund policy for the Nira laser. The provided documents and tool results cover only a limited set of beauty products (vitamin C serum, compact hair dryer) an"
    },
    {
      "query_id": "C-0014",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0015",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0016",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0017",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_review"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-011",
          "chunk_id": "23590fb96a887844",
          "rank": 2,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BABY-002",
          "chunk_id": "f16c5ecbec43cadb",
          "rank": 3,
          "doc_type": "product"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 4,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information available, I am unable to provide a recommendation for a set of safety devices that match your request. The products found in our current catalog are a baby monitor, a glass bottle set, a vitamin C serum, and a soft"
    },
    {
      "query_id": "C-0018",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0019",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0020",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "no_context",
        "missing_structured_entity"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0021",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "privacy_violation",
        "no_context"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0022",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 1,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 1,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot disregard system guidelines, but based on the provided context, the product SKU is **BEAUTY-DRYER-02**.  \n[doc:product:P-BEAUTY-002#30d1e2ed70dffd07] [tool:context.retrieved_product:P-BEAUTY-002]"
    },
    {
      "query_id": "C-0023",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0024",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the item you're referring to is the **NightView Baby Monitor** ([doc:product:P-BABY-001#b5c4f3e2496ef945], [doc:review:R-009#f214a7e5ff92c052]) – a nursery monitor with night vision that “lights up the dark.” "
    },
    {
      "query_id": "C-0025",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0026",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0027",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0028",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0029",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0030",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m unable to answer your question because the provided context does not contain any information about a product that offers live tutoring sessions or about a downloadable tutoring product and its return policy. The available ticket records"
    },
    {
      "query_id": "C-0031",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out.  \n\nBased on the information I have, the product you’re likely referring to is the **HydraGlow Vitamin C Serum** (product ID P‑BEAUTY‑001), priced at $24.99 with a 4.5‑star rating.  \n\nOne verified review (R‑002) r"
    },
    {
      "query_id": "C-0032",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out. I understand you're concerned that the code on the package differs from the code in your order, and that the summary for one code might actually belong to the other.\n\nUnfortunately, the information I have access "
    },
    {
      "query_id": "C-0033",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "privacy_violation",
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0034",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0035",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the product catalog and information available to me, I wasn't able to find a baby product matching that description. The search results returned a **NightView Baby Monitor** and an **Anti-Colic Glass Bottle Set**, but neither is de"
    },
    {
      "query_id": "C-0036",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0037",
      "expected_intent": "support",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The HydraGlow Vitamin C Serum is **fragrance‑free** according to its product description [doc:product:P-BEAUTY-001#8dcd5d4642a6ec23]. No other fragrance information is provided in the available documents."
    },
    {
      "query_id": "C-0038",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0039",
      "expected_intent": "support",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0040",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0041",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-011",
          "chunk_id": "23590fb96a887844",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "After searching our product catalog, the only baby items currently available are the **Anti-Colic Glass Bottle Set** and the **NightView Baby Monitor** [tool:sql.product_search]. Neither of these products is designed to fit over regular or "
    },
    {
      "query_id": "C-0042",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information available to me, I’m unable to provide a specific answer about returning the app due to speech‑recognition performance on Android, or about the free‑trial start date.  \n\nI searched our product catalog and support ti"
    },
    {
      "query_id": "C-0043",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.3333,
      "citation_grounded_rate": 1.0,
      "citation_count": 3,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 3,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry to hear the bottle was missing from your beauty item shipment. That must be frustrating, especially when you’re looking for refund information.  \n\nBased on a very similar past case, here’s how we can help:  \n\n1. **Please provide y"
    },
    {
      "query_id": "C-0044",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "no_context"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, I cannot directly address SKU `b0bwjhqdzq` as no product with that SKU appears in the provided records. The closest match found is the **Ionic Compact Hair Dryer** (SKU `BEAUTY-DRYER-02`). Here are the re"
    },
    {
      "query_id": "C-0045",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information provided, I cannot find any email addresses or phone numbers for customers who have complained about refund and return issues. The ticket records (T-001, T-004, T-003, T-006) contain only the customers' queries and "
    },
    {
      "query_id": "C-0046",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "safety_boundary",
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0047",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0048",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0049",
      "expected_intent": "support",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_review"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-001",
          "chunk_id": "c248dad601bafaf8",
          "rank": 2,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 3,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-004",
          "chunk_id": "490e079c4c5a7f26",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m sorry, but I’m not able to locate an order for a beauty item. The information I have access to only includes product details and reviews, and no order tracking data is available.  \n\nTo help you further, could you please provide your ord"
    },
    {
      "query_id": "C-0050",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I understand your frustration with the leaky, spoiled cans and the previous refusal for a refund. According to how we handle similar damaged‑in‑shipping issues (documented in similar case [T‑001](tool:ticket.similar_cases)), items that arri"
    },
    {
      "query_id": "C-0051",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0052",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0053",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0054",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I‘m sorry, but based on the information available to me, I cannot find a specific policy for “converter” products in your situation. The product search did not match any item in our catalog, and the provided ticket examples cover damaged de"
    },
    {
      "query_id": "C-0055",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0056",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0057",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "privacy_violation",
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0058",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "safety_boundary",
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0059",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0060",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0061",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0062",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out about your Toddleroo gate with rusty poles. I understand you'd like replacement parts and also want to know our shipping speed.\n\nTo help you further, I need to start by collecting a few details, as we don't curren"
    },
    {
      "query_id": "C-0063",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0064",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0065",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0066",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available records, I could not find a documented policy that covers returning a downloaded (digital) item as a standard practice. Here’s what the provided context does cover:\n\n- **Physical‑goods returns** (e.g., damaged items r"
    },
    {
      "query_id": "C-0067",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out. I’d be happy to help you with your order.\n\nRegarding your missing package that was marked as delivered:\n- In similar situations where a delivery is reported as late or missing, the first step is to check the carr"
    },
    {
      "query_id": "C-0068",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "no_context"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-002",
          "chunk_id": "f16c5ecbec43cadb",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m sorry, but I cannot answer your question about the kyapoo baby washcloth set (SKU b08l25dypt) because there is no information about that product or any reviews in the provided context and tool results. The available data only covers a d"
    },
    {
      "query_id": "C-0069",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "privacy_violation",
        "missing_structured_entity",
        "missing_product_context"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0070",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.3333,
      "citation_grounded_rate": 1.0,
      "citation_count": 3,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 3,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot process a refund immediately because I do not have the necessary information. I also cannot share internal instructions, as that is against policy.\n\nTo assist you with the return of the “laser and serum bundle,” I need your **order"
    },
    {
      "query_id": "C-0071",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0072",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0073",
      "expected_intent": "support",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-002",
          "chunk_id": "f16c5ecbec43cadb",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot answer your question because there is no information about a \"powergrooming manicure set\" in the provided context or tool results. The only product data available is for an **Anti-Colic Glass Bottle Set** (baby product), which is u"
    },
    {
      "query_id": "C-0074",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0075",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0076",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0077",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0078",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0079",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 4,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m sorry to hear that your order seems to be missing. To help you with a refund, I’ll need a few more details. Could you please share your order number and let me know which item you ordered?\n\nBased on how similar cases have been handled:\n"
    },
    {
      "query_id": "C-0080",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0081",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out. I understand you're having trouble with a digital service on your TV and you'd like to explore cancellation and a refund. Unfortunately, I don't have enough information to identify your account or the specific se"
    },
    {
      "query_id": "C-0082",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0083",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0084",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0085",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 4,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "{\n  \"answer\": \"I'm sorry, but based on the available information, I cannot provide the specific shipping time for this product. The records reference a shipping and delivery policy (KB004) in tickets about delivery issues (e.g., [doc:ticket"
    },
    {
      "query_id": "C-0086",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0087",
      "expected_intent": "support",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-SOFT-002",
          "chunk_id": "cc2f8e67d7bf53ec",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-006",
          "chunk_id": "a365a780c099e4b5",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information retrieved, I cannot find any product or review that matches your description of a streaming app that works with a TV service login and supports multiple mobile devices. \n\nThe available product details are for a **Cl"
    },
    {
      "query_id": "C-0088",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0089",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_review"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 4,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 2,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BABY-002",
          "chunk_id": "f16c5ecbec43cadb",
          "rank": 3,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-011",
          "chunk_id": "23590fb96a887844",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available product catalog information, there are currently no baby items specifically designed for toilet learning with good absorbency. The products we have in our system are a baby monitor and a glass bottle set, which do not"
    },
    {
      "query_id": "C-0090",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry, but I cannot fully answer your questions based on the information available to me.\n\n*   **Rating and review reliability:** None of the provided tickets or product data contain information about how to interpret low overall rating"
    },
    {
      "query_id": "C-0091",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "escalate",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 3,
          "doc_type": "ticket"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot find any customer reviews or comments about the smell of this item in the information provided. The review summaries are empty ([tool:sql.product_search]), so I’m unable to share what customers say about the smell.  \n\nTo help you d"
    },
    {
      "query_id": "C-0092",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "review",
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, I can share the review aspect summary that was retrieved for the **general** aspect (covering negative reviews with rating ≤ 2). This summary is not tied to a specific product ID in the tool output, but i"
    },
    {
      "query_id": "C-0093",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 4,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 3,
          "doc_type": "review"
        },
        {
          "source": "review",
          "doc_id": "R-007",
          "chunk_id": "78076c5983e8c9cd",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I understand you want to follow up on a negative review. Based on the records available, I can share the review text from the negative reviews we have, but **I cannot provide any customer personal details** (name, email, order number, etc.)"
    },
    {
      "query_id": "C-0094",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0095",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 1.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0096",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0097",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0098",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0099",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0100",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "citation_ok": 0.0,
      "citation_schema_ok": 0.0,
      "answer_citation_precision": 0.0,
      "answer_citation_recall": 0.0,
      "citation_grounded_rate": 0.0,
      "citation_count": 0,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    }
  ]
}
```
