# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: humanlike_blind
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_blind.jsonl
- Oracle sources: False

## 摘要

- 样本数: 200
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 0.043
- Recall@5: 0.0526
- MRR: 0.0836
- NDCG@5: 0.0563
- exact_recall@5: 0.06
- acceptable_recall@5: 0.125
- entity_accuracy@5: 0.13
- aspect_accuracy@5: 0.65
- forbidden_rate@5: 0.05
- 引用率: 0.28
- Citation schema OK: 0.175
- Answer citation precision/recall: 0.175 / 0.1338
- Citation grounded rate: 0.28
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.34
- 延迟 p50/p95: 45 ms / 45457 ms
- Embedding 模型: local-token-cosine
- Reranker 模型: none
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 98 | 0.0571 | 0.0643 | 0.1068 | 0.0724 | 0.3469 | 0.2041 | 0.2041 / 0.1633 | 1.0 |
| recommendation | 51 | 0.0118 | 0.0294 | 0.0392 | 0.0272 | 0.1961 | 0.1569 | 0.1569 / 0.1225 | 1.0 |
| support | 51 | 0.0471 | 0.0534 | 0.0833 | 0.0547 | 0.2353 | 0.1373 | 0.1373 / 0.0882 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 200 | 0.043 | 0.0526 | 0.0836 | 0.0563 | 0.28 | 0.175 | 0.175 / 0.1338 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 427 | 43 |
| dense | 415 | 23 |
| forced_fallback | 200 | 0 |
| policy_fallback | 29 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | bm25: 28, dense: 17 |
| recommendation | bm25: 3, dense: 2 |
| support | bm25: 12, dense: 4 |

## Agentic 证据诊断

- 重试率: 0.86

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 50, escalate: 6, refuse: 144 |
| 尝试次数 | 1: 28, 2: 172 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_policy | 10 |
| missing_product | 1 |
| missing_review | 11 |
| missing_structured_entity | 18 |
| no_context | 1 |
| unknown_intent | 131 |
| unsafe_commitment | 2 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 165 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_policy: 5, missing_product: 1, missing_review: 6, missing_structured_entity: 8, no_context: 1, unknown_intent: 60, unsafe_commitment: 2 |
| recommendation | missing_review: 3, missing_structured_entity: 8, unknown_intent: 33 |
| support | missing_policy: 5, missing_review: 2, missing_structured_entity: 2, unknown_intent: 38 |

## 原始 JSON

```json
{
  "suite": "humanlike_blind",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\humanlike_blind.jsonl",
  "use_oracle_sources": false,
  "n": 200,
  "retrieval_backend": "local",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "local-token-cosine",
    "embedding_backend": "local",
    "reranker_model": "none",
    "llm_model": "deepseek-v4-flash"
  },
  "retrieval": {
    "precision@5": 0.043,
    "recall@5": 0.0526,
    "mrr": 0.0836,
    "ndcg@5": 0.0563,
    "exact_recall@5": 0.06,
    "acceptable_recall@5": 0.125,
    "entity_accuracy@5": 0.13,
    "aspect_accuracy@5": 0.65,
    "forbidden_rate@5": 0.05
  },
  "support_quality": {
    "citation_ok": 0.28,
    "citation_schema_ok": 0.175,
    "answer_citation_precision": 0.175,
    "answer_citation_recall": 0.1338,
    "citation_grounded_rate": 0.28,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.34
  },
  "latency": {
    "p50_ms": 45,
    "p95_ms": 45457
  },
  "by_intent": {
    "customer_ops": {
      "n": 98,
      "retrieval": {
        "precision@5": 0.0571,
        "recall@5": 0.0643,
        "mrr": 0.1068,
        "ndcg@5": 0.0724
      },
      "support_quality": {
        "citation_ok": 0.3469,
        "citation_schema_ok": 0.2041,
        "answer_citation_precision": 0.2041,
        "answer_citation_recall": 0.1633,
        "citation_grounded_rate": 0.3469,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.3776
      }
    },
    "recommendation": {
      "n": 51,
      "retrieval": {
        "precision@5": 0.0118,
        "recall@5": 0.0294,
        "mrr": 0.0392,
        "ndcg@5": 0.0272
      },
      "support_quality": {
        "citation_ok": 0.1961,
        "citation_schema_ok": 0.1569,
        "answer_citation_precision": 0.1569,
        "answer_citation_recall": 0.1225,
        "citation_grounded_rate": 0.1961,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.3529
      }
    },
    "support": {
      "n": 51,
      "retrieval": {
        "precision@5": 0.0471,
        "recall@5": 0.0534,
        "mrr": 0.0833,
        "ndcg@5": 0.0547
      },
      "support_quality": {
        "citation_ok": 0.2353,
        "citation_schema_ok": 0.1373,
        "answer_citation_precision": 0.1373,
        "answer_citation_recall": 0.0882,
        "citation_grounded_rate": 0.2353,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.2549
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 200,
      "retrieval": {
        "precision@5": 0.043,
        "recall@5": 0.0526,
        "mrr": 0.0836,
        "ndcg@5": 0.0563
      },
      "support_quality": {
        "citation_ok": 0.28,
        "citation_schema_ok": 0.175,
        "answer_citation_precision": 0.175,
        "answer_citation_recall": 0.1338,
        "citation_grounded_rate": 0.28,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.34
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 427,
      "dense": 415,
      "forced_fallback": 200,
      "policy_fallback": 29
    },
    "relevant_hit_signal_counts": {
      "bm25": 43,
      "dense": 23
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "bm25": 28,
        "dense": 17
      },
      "recommendation": {
        "bm25": 3,
        "dense": 2
      },
      "support": {
        "bm25": 12,
        "dense": 4
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 50,
      "escalate": 6,
      "refuse": 144
    },
    "attempt_counts": {
      "1": 28,
      "2": 172
    },
    "retry_rate": 0.86,
    "evidence_gap_counts": {
      "missing_policy": 10,
      "missing_product": 1,
      "missing_review": 11,
      "missing_structured_entity": 18,
      "no_context": 1,
      "unknown_intent": 131,
      "unsafe_commitment": 2
    },
    "citation_failure_counts": {
      "missing_answer_citation": 165
    },
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "missing_policy": 5,
        "missing_product": 1,
        "missing_review": 6,
        "missing_structured_entity": 8,
        "no_context": 1,
        "unknown_intent": 60,
        "unsafe_commitment": 2
      },
      "recommendation": {
        "missing_review": 3,
        "missing_structured_entity": 8,
        "unknown_intent": 33
      },
      "support": {
        "missing_policy": 5,
        "missing_review": 2,
        "missing_structured_entity": 2,
        "unknown_intent": 38
      }
    }
  },
  "retrieval_rows": [
    {
      "query_id": "H-0001",
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
        "ticket:T-006",
        "kb:KB001_return_refund_policy"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0002",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B0916ZRQDG",
        "review:AS-Baby_Products-B0BN714TVL-price_value",
        "review:RV-AMZREV-Baby_Products-01067",
        "product:PP-Software-B006GWE5PM",
        "ticket:FAQ-Baby_Products-0002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
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
          "doc_id": "review:AS-Baby_Products-B0BN714TVL-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01067",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B006GWE5PM",
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
          "doc_id": "ticket:FAQ-Baby_Products-0002",
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
      "query_id": "H-0003",
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
        "product:PP-All_Beauty-B07GDBN9LB",
        "product:PP-Software-B005SE8IFW",
        "product:PP-Software-B07BKPFXTJ",
        "product:PP-Software-B00BYJ6BUO",
        "review:RV-AMZREV-Software-00176"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07GDBN9LB",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B005SE8IFW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B07BKPFXTJ",
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
          "doc_id": "product:PP-Software-B00BYJ6BUO",
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
          "doc_id": "review:RV-AMZREV-Software-00176",
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
      "query_id": "H-0004",
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
        "review:R-011",
        "ticket:T-006",
        "product:P-SOFT-001",
        "product:P-BABY-002"
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
      "query_id": "H-0005",
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
        "product:PP-Baby_Products-B09N6J7BQ4",
        "product:PP-Software-B0000C66VY",
        "product:PP-Baby_Products-B085L8TDCM",
        "review:RV-AMZREV-Baby_Products-00966",
        "ticket:FAQ-Software-0056"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B09N6J7BQ4",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B0000C66VY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B085L8TDCM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00966",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0056",
          "doc_type": "faq_case",
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
      "query_id": "H-0006",
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
        "product:PP-All_Beauty-B01DUYNJL4",
        "product:PP-All_Beauty-B073TBC4TS",
        "review:RV-AMZREV-All_Beauty-00963",
        "review:RV-AMZREV-All_Beauty-04304",
        "review:RV-AMZREV-All_Beauty-04440"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B01DUYNJL4",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B073TBC4TS",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00963",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04440",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0007",
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
        "review:AS-Baby_Products-B08W7VYTH2-delivery",
        "review:RV-AMZREV-All_Beauty-00247",
        "kb:KB004_shipping_delivery_policy",
        "kb:KB001_return_refund_policy",
        "product:PP-Software-B00658U5HE"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B08W7VYTH2-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00247",
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
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 4,
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
          "rank": 5,
          "doc_id": "product:PP-Software-B00658U5HE",
          "doc_type": "product_profile",
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
      "query_id": "H-0008",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-Baby_Products-B0C3FG4HSV",
        "review:RV-AMZREV-Baby_Products-01132",
        "review:RV-AMZREV-Baby_Products-03252",
        "review:AS-Baby_Products-B0C5RW5SMK-price_value",
        "ticket:FAQ-Software-0158"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0C3FG4HSV",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-01132",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-03252",
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
          "doc_id": "review:AS-Baby_Products-B0C5RW5SMK-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0158",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0009",
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
        "ticket:T-003",
        "product:P-SOFT-001",
        "kb:KB004_shipping_delivery_policy"
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
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 26,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0010",
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
        "product:PP-All_Beauty-B08KGVBW41",
        "review:AS-All_Beauty-B07CDYN5W8-skin_scent",
        "review:RV-AMZREV-All_Beauty-01062",
        "product:PP-Software-B07GBYBWFG",
        "review:RV-AMZREV-All_Beauty-00895"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B08KGVBW41",
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
          "doc_id": "review:AS-All_Beauty-B07CDYN5W8-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01062",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B07GBYBWFG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00895",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0011",
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
        "review:R-005",
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
      "query_id": "H-0012",
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
        "ticket:T-004",
        "ticket:T-001"
      ],
      "signals": [
        {
          "rank": 1,
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
      "query_id": "H-0013",
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
        "ticket:T-004",
        "ticket:T-001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-004",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 25,
          "signals": [
            "bm25"
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
      "query_id": "H-0014",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 0.5,
      "ndcg@5": 0.21398626473452756,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-All_Beauty-B003NTFDFM-quality_damage",
        "product:PP-Baby_Products-B0BWJHQDZJ",
        "product:PP-Baby_Products-B0B2R9NTXV",
        "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
        "review:RV-AMZREV-Baby_Products-03869"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B003NTFDFM-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BWJHQDZJ",
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
          "doc_id": "product:PP-Baby_Products-B0B2R9NTXV",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-03869",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0015",
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
        "review:AS-All_Beauty-B07HHZBH4X-skin_scent",
        "review:RV-AMZREV-Software-00715",
        "product:PP-All_Beauty-B00KXFD75M",
        "product:PP-All_Beauty-B01LY4FP5K",
        "kb:KB003_payment_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07HHZBH4X-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-00715",
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00KXFD75M",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B01LY4FP5K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB003_payment_refund_policy",
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
      "query_id": "H-0016",
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
        "review:AS-All_Beauty-B07M9D3WYW-skin_scent",
        "product:PP-All_Beauty-B07WRVM3Z2",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "product:PP-All_Beauty-B0B8F6MWFJ",
        "review:RV-AMZREV-Baby_Products-02331"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07M9D3WYW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07WRVM3Z2",
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
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0B8F6MWFJ",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-02331",
          "doc_type": "review_evidence",
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
      "query_id": "H-0017",
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
        "review:R-011",
        "ticket:T-001",
        "product:P-BEAUTY-001",
        "product:P-BABY-002"
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
      "query_id": "H-0018",
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
        "product:PP-Software-B0000C66VY",
        "review:AS-Software-B003VUNYIG-digital_license",
        "review:RV-AMZREV-All_Beauty-04440",
        "product:PP-Software-B005ZKC3YG",
        "review:RV-AMZREV-All_Beauty-00378"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B0000C66VY",
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
          "doc_id": "review:AS-Software-B003VUNYIG-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04440",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 24,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005ZKC3YG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00378",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0019",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-All_Beauty-B000067E30-price_value",
        "review:RV-AMZREV-All_Beauty-02755",
        "product:PP-All_Beauty-B01MA3LXIL",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B000067E30-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02755",
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
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B01MA3LXIL",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0020",
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
      "query_id": "H-0021",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:AS-Baby_Products-B096LKKG3C-price_value",
        "review:RV-AMZREV-Software-04491",
        "product:PP-Software-B01N0IG90U",
        "product:PP-Software-B07QFVSHQB",
        "review:RV-AMZREV-All_Beauty-00092"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B096LKKG3C-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-04491",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B01N0IG90U",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B07QFVSHQB",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00092",
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
      "query_id": "H-0022",
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
        "review:AS-All_Beauty-B07T92WSTX-skin_scent",
        "review:RV-AMZREV-Baby_Products-04629",
        "product:PP-Software-B005ZTFPFQ",
        "review:AS-All_Beauty-B012Q9NGE4-skin_scent",
        "review:AS-All_Beauty-B084JGNSST-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07T92WSTX-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-04629",
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
          "doc_id": "product:PP-Software-B005ZTFPFQ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B012Q9NGE4-skin_scent",
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
          "doc_id": "review:AS-All_Beauty-B084JGNSST-skin_scent",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0023",
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
        "review:RV-AMZREV-Baby_Products-01515",
        "product:PP-Baby_Products-B0BRJWF9B2",
        "review:RV-AMZREV-All_Beauty-03005",
        "review:RV-AMZREV-Baby_Products-03926",
        "review:RV-AMZREV-Baby_Products-00194"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-01515",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BRJWF9B2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03005",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-03926",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-00194",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0024",
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
        "review:RV-AMZREV-Software-01771",
        "review:RV-AMZREV-Software-03637",
        "review:RV-AMZREV-Software-01394",
        "review:RV-AMZREV-Software-02607",
        "review:AS-Software-B018IOV40E-refund_return"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-01771",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-03637",
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
          "doc_id": "review:RV-AMZREV-Software-01394",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-02607",
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
          "doc_id": "review:AS-Software-B018IOV40E-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0025",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.6,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B08DHTJ25J",
        "ticket:FAQ-All_Beauty-0003",
        "review:RV-AMZREV-All_Beauty-00008",
        "product:PP-All_Beauty-B07FPS2VFK",
        "review:AS-All_Beauty-B0B1MBRVDS-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B08DHTJ25J",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:FAQ-All_Beauty-0003",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00008",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B07FPS2VFK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B0B1MBRVDS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0026",
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
        "ticket:T-006"
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
      "query_id": "H-0027",
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
        "product:PP-Software-B00A8ECU24",
        "product:PP-Software-B07FY5BD28",
        "review:RV-AMZREV-Software-01504",
        "product:PP-Software-B005SE8IFW",
        "review:AS-All_Beauty-B01AWXGD3M-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00A8ECU24",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B07FY5BD28",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-01504",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005SE8IFW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B01AWXGD3M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0028",
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
      "query_id": "H-0029",
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
        "product:PP-Baby_Products-B07LFY4JLZ",
        "product:PP-Baby_Products-B09JFYSGSC",
        "product:PP-Baby_Products-B07258QRSV",
        "product:PP-Baby_Products-B001QC3CKG",
        "review:RV-AMZREV-All_Beauty-01674"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B07LFY4JLZ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B09JFYSGSC",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B07258QRSV",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B001QC3CKG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01674",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0030",
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
        "product:PP-All_Beauty-B01JIVO8GS",
        "review:RV-AMZREV-Software-00266",
        "product:PP-Software-B00EEDJHXA",
        "product:PP-Baby_Products-B0BVR8RCY8",
        "product:PP-Software-B00MDWUIAK"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B01JIVO8GS",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-00266",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B00EEDJHXA",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0BVR8RCY8",
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
          "doc_id": "product:PP-Software-B00MDWUIAK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0031",
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
        "review:R-002",
        "ticket:T-001",
        "product:P-BEAUTY-002",
        "product:P-BEAUTY-001"
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
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
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
          "rank": 4,
          "doc_id": "product:P-BEAUTY-001",
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
      "query_id": "H-0032",
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
      "forbidden_rate@5": 0.6,
      "retrieved": [
        "product:PP-Baby_Products-B0BXTNL2NY",
        "review:RV-AMZREV-Baby_Products-00947",
        "review:RV-AMZREV-Baby_Products-02299",
        "review:AS-Baby_Products-B0BXTNL2NY-skin_scent",
        "ticket:FAQ-Software-0158"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0BXTNL2NY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00947",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02299",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B0BXTNL2NY-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0158",
          "doc_type": "faq_case",
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
      "query_id": "H-0033",
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
      "query_id": "H-0034",
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
        "review:RV-AMZREV-All_Beauty-03182",
        "review:RV-AMZREV-All_Beauty-00841",
        "review:RV-AMZREV-All_Beauty-03660",
        "review:RV-AMZREV-All_Beauty-04304",
        "kb:KB002_warranty_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03182",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00841",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03660",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB002_warranty_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0035",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B0916ZRQDG",
        "review:AS-Baby_Products-B0B2CBQGSS-price_value",
        "review:RV-AMZREV-Baby_Products-01791",
        "product:PP-All_Beauty-B01F99RQQW",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0B2CBQGSS-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01791",
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
          "doc_id": "product:PP-All_Beauty-B01F99RQQW",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0036",
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
        "review:AS-Baby_Products-B075QQ8VZW-refund_return",
        "review:RV-AMZREV-Software-02057",
        "product:PP-Baby_Products-B09ZY4DZQF",
        "review:AS-Software-B00FAPF5U0-refund_return",
        "ticket:FAQ-Software-0076"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B075QQ8VZW-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-02057",
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
          "doc_id": "product:PP-Baby_Products-B09ZY4DZQF",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B00FAPF5U0-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0076",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0037",
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
      "query_id": "H-0038",
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
      "query_id": "H-0039",
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
        "review:R-007",
        "review:R-009"
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
      "query_id": "H-0040",
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
        "review:R-011",
        "ticket:T-006",
        "product:P-SOFT-001",
        "product:P-BABY-002"
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
      "query_id": "H-0041",
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
        "product:P-SOFT-001"
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
          "doc_id": "product:P-SOFT-001",
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
      "query_id": "H-0042",
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
        "review:R-006"
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
      "query_id": "H-0043",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B09BR43CS5",
        "review:RV-AMZREV-All_Beauty-00740",
        "review:RV-AMZREV-All_Beauty-01090",
        "product:PP-All_Beauty-B073WQHFXB",
        "ticket:FAQ-All_Beauty-0036"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B09BR43CS5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01090",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B073WQHFXB",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0036",
          "doc_type": "faq_case",
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
      "query_id": "H-0044",
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
        "review:R-007",
        "ticket:T-004",
        "product:P-SOFT-002",
        "review:R-008"
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
      "query_id": "H-0045",
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
        "review:R-002",
        "ticket:T-001",
        "product:P-BEAUTY-001",
        "ticket:T-006"
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
      "query_id": "H-0046",
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
        "product:PP-Baby_Products-B08J2KDQ1G",
        "product:PP-Baby_Products-B0C2ZC67GD",
        "product:PP-Baby_Products-B00G4EPD12",
        "product:PP-All_Beauty-B09571TNVG",
        "review:RV-AMZREV-All_Beauty-04304"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B08J2KDQ1G",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0C2ZC67GD",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B00G4EPD12",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B09571TNVG",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
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
      "query_id": "H-0047",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-02299",
        "review:RV-AMZREV-Baby_Products-00947",
        "review:RV-AMZREV-Baby_Products-01102",
        "review:RV-AMZREV-Baby_Products-01571",
        "review:AS-Baby_Products-B0BXTNL2NY-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-02299",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00947",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-01102",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01571",
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
          "doc_id": "review:AS-Baby_Products-B0BXTNL2NY-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0048",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Software-00004",
        "product:PP-Software-B00CWY76CC",
        "review:RV-AMZREV-Software-00055",
        "review:RV-AMZREV-Software-02162",
        "review:RV-AMZREV-Software-01139"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-00004",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00CWY76CC",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 25,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00055",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-02162",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-01139",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0049",
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
      "query_id": "H-0050",
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
        "ticket:FAQ-All_Beauty-0070",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-04510",
        "review:AS-All_Beauty-B01BEYRHBA-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0070",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04510",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B01BEYRHBA-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
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
      "query_id": "H-0051",
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
      "query_id": "H-0052",
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
        "review:RV-AMZREV-Baby_Products-00778",
        "product:PP-Baby_Products-B074YD5Q3T",
        "review:AS-All_Beauty-B002E4VK40-quality_damage",
        "product:PP-All_Beauty-B07CSL21J8",
        "ticket:FAQ-All_Beauty-0062"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-00778",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B074YD5Q3T",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B002E4VK40-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
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
          "doc_id": "ticket:FAQ-All_Beauty-0062",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0053",
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
        "review:RV-AMZREV-Baby_Products-04383",
        "product:PP-Baby_Products-B07PWMXJDK",
        "product:PP-Baby_Products-B09BCM58RX",
        "product:PP-Baby_Products-B08HH4STTH",
        "product:PP-Baby_Products-B0BW7CVB9K"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-04383",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B07PWMXJDK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B09BCM58RX",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B08HH4STTH",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B0BW7CVB9K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0054",
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
      "query_id": "H-0055",
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
        "review:AS-All_Beauty-B07PCGSFGQ-price_value",
        "review:RV-AMZREV-All_Beauty-04440",
        "product:PP-Baby_Products-B000RHJT6C",
        "product:PP-Software-B09DTFRPF4",
        "review:AS-All_Beauty-B07PCGSFGQ-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07PCGSFGQ-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04440",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B000RHJT6C",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B09DTFRPF4",
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
          "doc_id": "review:AS-All_Beauty-B07PCGSFGQ-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0056",
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
        "ticket:T-006",
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
        }
      ]
    },
    {
      "query_id": "H-0057",
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
        "review:R-006",
        "ticket:T-005",
        "product:P-BABY-001",
        "review:R-010"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-006",
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
          "doc_id": "ticket:T-005",
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
          "rank": 4,
          "doc_id": "review:R-010",
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
      "query_id": "H-0058",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 0.9558295932317544,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B08BBQ29N5",
        "review:RV-AMZREV-All_Beauty-03336",
        "ticket:FAQ-All_Beauty-0001",
        "review:RV-AMZREV-All_Beauty-00005",
        "review:RV-AMZREV-All_Beauty-02240"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B08BBQ29N5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03336",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-All_Beauty-0001",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02240",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0059",
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
        "review:RV-AMZREV-Software-02381",
        "product:PP-Software-B00820STKI",
        "review:AS-Software-B018IOV40E-refund_return",
        "review:RV-AMZREV-Software-01556",
        "product:PP-All_Beauty-B07GV9VGLD"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-02381",
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
          "doc_id": "product:PP-Software-B00820STKI",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Software-B018IOV40E-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-01556",
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
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B07GV9VGLD",
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
      "query_id": "H-0060",
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
        "product:PP-Software-B005ZKAXBG",
        "review:RV-AMZREV-Software-02219",
        "product:PP-Baby_Products-B08MY6543N",
        "product:PP-Software-B005M4T8L6",
        "product:PP-Baby_Products-B001E2DGKO"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B005ZKAXBG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-02219",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B08MY6543N",
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
          "doc_id": "product:PP-Software-B005M4T8L6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B001E2DGKO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0061",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.48522855511632257,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0006",
        "review:AS-All_Beauty-B08KFKKPBB-skin_scent",
        "review:AS-All_Beauty-B089RZ67T7-skin_scent",
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
        "review:RV-AMZREV-Baby_Products-04406"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0006",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B08KFKKPBB-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B089RZ67T7-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-04406",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0062",
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
        "review:R-009",
        "ticket:T-005"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-009",
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
          "doc_id": "ticket:T-005",
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
      "query_id": "H-0063",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0054",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-Software-00176",
        "review:AS-Software-B071KV3X66-digital_license",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0054",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00176",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B071KV3X66-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
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
      "query_id": "H-0064",
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
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-All_Beauty-B07PCGSFGQ-price_value",
        "review:RV-AMZREV-All_Beauty-00674",
        "product:PP-Software-B00HGJ18C2",
        "ticket:FAQ-Software-0088"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07PCGSFGQ-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00674",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00HGJ18C2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0088",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0065",
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
        "review:RV-AMZREV-Baby_Products-02422",
        "product:PP-Baby_Products-B0010P5Q7Q",
        "review:AS-Baby_Products-B09Y5T9VL7-delivery",
        "review:R-010",
        "review:RV-AMZREV-Baby_Products-03598"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-02422",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0010P5Q7Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B09Y5T9VL7-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-010",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-03598",
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
      "query_id": "H-0066",
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
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-Software-B003VUNYIG-digital_license",
        "review:RV-AMZREV-All_Beauty-03978",
        "product:PP-Software-B005ZKC3YG",
        "review:CL-All_Beauty-battery_power"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B003VUNYIG-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 24,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03978",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005ZKC3YG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-All_Beauty-battery_power",
          "doc_type": "complaint_cluster",
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
      "query_id": "H-0067",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.14285714285714285,
      "mrr": 0.2,
      "ndcg@5": 0.13120507751234178,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02778",
        "review:RV-AMZREV-Baby_Products-04979",
        "review:RV-AMZREV-All_Beauty-00198",
        "review:RV-AMZREV-All_Beauty-00674",
        "product:PP-All_Beauty-B081TJ8YS3"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02778",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-04979",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00198",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00674",
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
          "doc_id": "product:PP-All_Beauty-B081TJ8YS3",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0068",
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
      "query_id": "H-0069",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-Software-B005ZKC3YG",
        "review:AS-Baby_Products-B09B8LCT53-price_value",
        "review:RV-AMZREV-All_Beauty-00674",
        "product:PP-All_Beauty-B003NTFDFM",
        "ticket:FAQ-Software-0158"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B005ZKC3YG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 27,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B09B8LCT53-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 17,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00674",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B003NTFDFM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0158",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0070",
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
      "query_id": "H-0071",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.5531464700081437,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:FAQ-Baby_Products-0002",
        "product:PP-Baby_Products-B0BWJHQDZJ",
        "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
        "review:RV-AMZREV-All_Beauty-03307",
        "product:PP-Baby_Products-B07CCG2VSY"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-Baby_Products-0002",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BWJHQDZJ",
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
          "doc_id": "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03307",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B07CCG2VSY",
          "doc_type": "product_profile",
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
      "query_id": "H-0072",
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
        "review:RV-AMZREV-Baby_Products-04385",
        "product:PP-Software-B0144NYGJY",
        "review:RV-AMZREV-Baby_Products-02245",
        "review:RV-AMZREV-Software-01785",
        "review:RV-AMZREV-Baby_Products-02267"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-04385",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B0144NYGJY",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-02245",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-01785",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02267",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0073",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 0.25,
      "ndcg@5": 0.27727342735504823,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00091",
        "product:PP-All_Beauty-B098GMKW8D",
        "product:PP-All_Beauty-B01MA3LXIL",
        "review:RV-AMZREV-All_Beauty-01157",
        "ticket:FAQ-All_Beauty-0007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00091",
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
          "doc_id": "product:PP-All_Beauty-B098GMKW8D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 26,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B01MA3LXIL",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01157",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
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
      "query_id": "H-0074",
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
      "query_id": "H-0075",
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
        "ticket:T-003",
        "ticket:T-002"
      ],
      "signals": [
        {
          "rank": 1,
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
      "query_id": "H-0076",
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
        "product:PP-Baby_Products-B082RPF719",
        "review:RV-AMZREV-Software-01246",
        "product:PP-Baby_Products-B00GJY6EPG",
        "product:PP-Software-B0000C66VY",
        "product:PP-Software-B00N1HONIO"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B082RPF719",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-01246",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B00GJY6EPG",
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
          "doc_id": "product:PP-Software-B0000C66VY",
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
          "doc_id": "product:PP-Software-B00N1HONIO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0077",
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
      "query_id": "H-0078",
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
        "product:PP-Software-B01BPPA75Q",
        "product:PP-Software-B00JRAYXIE",
        "product:PP-Software-B000EZYEB2",
        "product:PP-Software-B000053F9D",
        "review:RV-AMZREV-Baby_Products-04449"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B01BPPA75Q",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00JRAYXIE",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B000EZYEB2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B000053F9D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-04449",
          "doc_type": "review_evidence",
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
      "query_id": "H-0079",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.6,
      "recall@5": 0.42857142857142855,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B08P2DZB4X",
        "review:AS-All_Beauty-B08P2DZB4X-battery_power",
        "review:RV-AMZREV-All_Beauty-03160",
        "review:RV-AMZREV-Software-00266",
        "ticket:FAQ-All_Beauty-0002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B08P2DZB4X",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 24,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B08P2DZB4X-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-00266",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0002",
          "doc_type": "faq_case",
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
      "query_id": "H-0080",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 0.2,
      "ndcg@5": 0.13120507751234178,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:AS-All_Beauty-B000067E30-price_value",
        "review:RV-AMZREV-All_Beauty-00172",
        "review:RV-AMZREV-Baby_Products-00958",
        "review:RV-AMZREV-All_Beauty-04748",
        "product:PP-Baby_Products-B08WBJSYKH"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B000067E30-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00172",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00958",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04748",
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
          "doc_id": "product:PP-Baby_Products-B08WBJSYKH",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0081",
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
        "review:R-002",
        "ticket:T-001",
        "review:R-012",
        "ticket:T-006"
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
      "query_id": "H-0082",
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
        "review:RV-AMZREV-All_Beauty-01293",
        "review:RV-AMZREV-All_Beauty-00963",
        "review:RV-AMZREV-Baby_Products-02497",
        "review:RV-AMZREV-Baby_Products-00966",
        "review:AS-Baby_Products-B0BW8SNCF2-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01293",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00963",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02497",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00966",
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
          "doc_id": "review:AS-Baby_Products-B0BW8SNCF2-price_value",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0083",
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
      "query_id": "H-0084",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00828",
        "review:AS-All_Beauty-B085BB7B1M-skin_scent",
        "review:RV-AMZREV-Baby_Products-04463",
        "review:RV-AMZREV-Software-01856",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00828",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B085BB7B1M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04463",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-01856",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0085",
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
        "review:RV-AMZREV-Baby_Products-00864",
        "review:RV-AMZREV-All_Beauty-04304",
        "product:PP-Baby_Products-B001QC3CKG",
        "review:RV-AMZREV-Baby_Products-01009",
        "review:AS-Baby_Products-B09NKBDYQS-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-00864",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 27,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B001QC3CKG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01009",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B09NKBDYQS-price_value",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0086",
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
      "query_id": "H-0087",
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
        "product:PP-Software-B00CKOYVG8",
        "product:PP-Software-B00BYJ6BUO",
        "review:RV-AMZREV-Software-02615",
        "product:PP-All_Beauty-B07N8JMJGY",
        "review:AS-Software-B0094BB4TW-digital_license"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00CKOYVG8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B00BYJ6BUO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-02615",
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
          "doc_id": "product:PP-All_Beauty-B07N8JMJGY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B0094BB4TW-digital_license",
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
      "query_id": "H-0088",
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
        "product:PP-All_Beauty-B07WVVXZG9",
        "review:AS-All_Beauty-B08SG2MBRY-skin_scent",
        "review:RV-AMZREV-All_Beauty-01312",
        "product:PP-Baby_Products-B0BR9R2Q3D",
        "product:PP-Baby_Products-B077TQCPGP"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07WVVXZG9",
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
          "doc_id": "review:AS-All_Beauty-B08SG2MBRY-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01312",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B0BR9R2Q3D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B077TQCPGP",
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
      "query_id": "H-0089",
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
        "review:R-009"
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
      "query_id": "H-0090",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.5,
      "mrr": 0.5,
      "ndcg@5": 0.38685280723454163,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B079573LDT",
        "product:PP-Software-B00004UFGD",
        "product:PP-Baby_Products-B0B14XF7Q3",
        "product:PP-Baby_Products-B08QFZY27L",
        "review:RV-AMZREV-Software-00334"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B079573LDT",
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
          "doc_id": "product:PP-Software-B00004UFGD",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B0B14XF7Q3",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B08QFZY27L",
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
          "doc_id": "review:RV-AMZREV-Software-00334",
          "doc_type": "review_evidence",
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
      "query_id": "H-0091",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B07CDYN5W8",
        "review:AS-All_Beauty-B07CDYN5W8-skin_scent",
        "review:RV-AMZREV-All_Beauty-04280",
        "product:PP-Software-B005ZKC3YG",
        "review:RV-AMZREV-All_Beauty-01046"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CDYN5W8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 27,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07CDYN5W8-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04280",
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
          "rank": 4,
          "doc_id": "product:PP-Software-B005ZKC3YG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01046",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0092",
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
      "forbidden_rate@5": 0.6,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-04979",
        "review:RV-AMZREV-All_Beauty-00740",
        "review:RV-AMZREV-Baby_Products-02299",
        "review:RV-AMZREV-Baby_Products-00947",
        "review:AS-Baby_Products-B07RRDX26B-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-04979",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02299",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00947",
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
          "doc_id": "review:AS-Baby_Products-B07RRDX26B-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0093",
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
        "review:AS-Software-B00FAPF5U0-price_value",
        "review:RV-AMZREV-All_Beauty-04002",
        "product:PP-Baby_Products-B01E5E703G",
        "review:AS-All_Beauty-B000067E30-price_value",
        "product:PP-Baby_Products-B0B2CBQGSS"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Software-B00FAPF5U0-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04002",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B01E5E703G",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B000067E30-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B0B2CBQGSS",
          "doc_type": "product_profile",
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
      "query_id": "H-0094",
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
        "review:RV-AMZREV-All_Beauty-01029",
        "product:PP-All_Beauty-B076DGMQTM",
        "product:PP-All_Beauty-B07FPS2VFK",
        "review:RV-AMZREV-All_Beauty-00986",
        "review:AS-All_Beauty-B076DGMQTM-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01029",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B076DGMQTM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07FPS2VFK",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00986",
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
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B076DGMQTM-skin_scent",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0095",
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
        "product:PP-Baby_Products-B0925YB2SX",
        "review:RV-AMZREV-All_Beauty-03371",
        "product:PP-Baby_Products-B07KGT8NQC",
        "product:PP-Baby_Products-B01E5E703G",
        "product:PP-All_Beauty-B072JX8LV5"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0925YB2SX",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03371",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B07KGT8NQC",
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
          "doc_id": "product:PP-Baby_Products-B01E5E703G",
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
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0096",
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
        "review:RV-AMZREV-Software-01222",
        "product:PP-Software-B000053F9D",
        "review:AS-Software-B00AFY7UJA-digital_license",
        "review:RV-AMZREV-Software-03735",
        "review:RV-AMZREV-Software-03685"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-01222",
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
          "doc_id": "product:PP-Software-B000053F9D",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Software-B00AFY7UJA-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03735",
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
          "doc_id": "review:RV-AMZREV-Software-03685",
          "doc_type": "review_evidence",
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
      "query_id": "H-0097",
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
        "product:P-BABY-002",
        "review:R-012"
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
          "bm25_rank": 15,
          "signals": [
            "bm25"
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
      "query_id": "H-0098",
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
        "ticket:T-005",
        "review:R-009"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-005",
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
      "query_id": "H-0099",
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
        "review:RV-AMZREV-Software-02615",
        "product:PP-Software-B0093BM38O",
        "product:PP-Software-B01LXOU5PM",
        "product:PP-All_Beauty-B07GDBN9LB",
        "review:AS-Software-B006C4JHT8-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-02615",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B0093BM38O",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B01LXOU5PM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B07GDBN9LB",
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
          "doc_id": "review:AS-Software-B006C4JHT8-quality_damage",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0100",
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
        "review:AS-Baby_Products-B0BC2VLLRH-price_value",
        "review:RV-AMZREV-Baby_Products-00778",
        "review:AS-All_Beauty-B09X9BG4FC-skin_scent",
        "review:AS-Baby_Products-B0C54J5D2B-battery_power",
        "product:PP-Baby_Products-B014D4HQ5U"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B0BC2VLLRH-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00778",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B09X9BG4FC-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B0C54J5D2B-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B014D4HQ5U",
          "doc_type": "product_profile",
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
      "query_id": "H-0101",
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
        "product:PP-All_Beauty-B0B4JPGX8P",
        "review:AS-Software-B09415CZLY-price_value",
        "review:RV-AMZREV-All_Beauty-00977",
        "product:PP-Baby_Products-B08C2GL1G5",
        "product:PP-All_Beauty-B08B1PR9C7"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B0B4JPGX8P",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B09415CZLY-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00977",
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
          "doc_id": "product:PP-Baby_Products-B08C2GL1G5",
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
          "doc_id": "product:PP-All_Beauty-B08B1PR9C7",
          "doc_type": "product_profile",
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
      "query_id": "H-0102",
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
        "review:RV-AMZREV-Software-04924",
        "product:PP-All_Beauty-B08N9RT9YD",
        "review:AS-Baby_Products-B00GUN3Z1W-delivery",
        "product:PP-Software-B0062AI84W",
        "review:RV-AMZREV-Baby_Products-01791"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-04924",
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
          "doc_id": "product:PP-All_Beauty-B08N9RT9YD",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B00GUN3Z1W-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B0062AI84W",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-01791",
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
      "query_id": "H-0103",
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
        "product:P-BABY-002",
        "product:P-BEAUTY-001",
        "product:P-BABY-001",
        "product:P-SOFT-001",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-002",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:P-BEAUTY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:P-BABY-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:P-SOFT-001",
          "doc_type": "product",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0104",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-02150",
        "product:PP-Baby_Products-B07J5DS8SN",
        "review:AS-All_Beauty-B07MN1KJ15-skin_scent",
        "product:PP-Software-B01LXOU5PM",
        "review:CL-Baby_Products-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-02150",
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
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B07J5DS8SN",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07MN1KJ15-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B01LXOU5PM",
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
          "doc_id": "review:CL-Baby_Products-quality_damage",
          "doc_type": "complaint_cluster",
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
      "query_id": "H-0105",
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
      "query_id": "H-0106",
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
        "product:PP-All_Beauty-B0046BPTI2",
        "review:RV-AMZREV-All_Beauty-01227",
        "review:RV-AMZREV-Baby_Products-04069",
        "product:PP-All_Beauty-B08LPJT4MT",
        "review:AS-All_Beauty-B07YR837T2-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B0046BPTI2",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01227",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04069",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B08LPJT4MT",
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
          "doc_id": "review:AS-All_Beauty-B07YR837T2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0107",
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
        "product:P-SOFT-001",
        "review:R-006"
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
      "query_id": "H-0108",
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
        "product:PP-All_Beauty-B07VDCD17L",
        "review:AS-All_Beauty-B078W6XC3C-skin_scent",
        "review:RV-AMZREV-Baby_Products-03807",
        "product:PP-All_Beauty-B0046BPTI2",
        "ticket:FAQ-Baby_Products-0002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07VDCD17L",
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
          "doc_id": "review:AS-All_Beauty-B078W6XC3C-skin_scent",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-03807",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0046BPTI2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0002",
          "doc_type": "faq_case",
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
      "query_id": "H-0109",
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
        "product:PP-All_Beauty-B07Z5BW8WL",
        "review:AS-Software-B07PRDNNGY-digital_license",
        "review:RV-AMZREV-Baby_Products-01139",
        "product:PP-All_Beauty-B01LY4FP5K",
        "review:CL-All_Beauty-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07Z5BW8WL",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B07PRDNNGY-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01139",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B01LY4FP5K",
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
          "doc_id": "review:CL-All_Beauty-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0110",
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
        "product:PP-All_Beauty-B00J7QCNDU",
        "review:AS-All_Beauty-B07S5GYK14-skin_scent",
        "review:RV-AMZREV-All_Beauty-02122",
        "product:PP-All_Beauty-B0844X4D53",
        "review:CL-Baby_Products-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B00J7QCNDU",
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
          "doc_id": "review:AS-All_Beauty-B07S5GYK14-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02122",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0844X4D53",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-Baby_Products-skin_scent",
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
      "query_id": "H-0111",
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
        "ticket:T-006",
        "kb:KB001_return_refund_policy"
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0112",
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
        "review:RV-AMZREV-All_Beauty-03182",
        "product:PP-All_Beauty-B00OP8NZV4",
        "review:AS-All_Beauty-B08P7PSMRR-skin_scent",
        "product:PP-All_Beauty-B017XD9GP6",
        "ticket:FAQ-Software-0056"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03182",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00OP8NZV4",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08P7PSMRR-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B017XD9GP6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0056",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0113",
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
        "review:R-011",
        "ticket:T-006",
        "product:P-BABY-002",
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
      "query_id": "H-0114",
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
        "product:PP-Software-B07QFVSHQB",
        "review:AS-All_Beauty-B07PCGSFGQ-price_value",
        "review:RV-AMZREV-Software-01246",
        "product:PP-All_Beauty-B0B2L218H2",
        "product:PP-Software-B0097K21YW"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B07QFVSHQB",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07PCGSFGQ-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-01246",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0B2L218H2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Software-B0097K21YW",
          "doc_type": "product_profile",
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
      "query_id": "H-0115",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:AS-All_Beauty-B07S5GYK14-skin_scent",
        "review:RV-AMZREV-All_Beauty-00198",
        "review:RV-AMZREV-Baby_Products-04979",
        "review:RV-AMZREV-Baby_Products-02909",
        "review:RV-AMZREV-All_Beauty-03909"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07S5GYK14-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00198",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04979",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-02909",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03909",
          "doc_type": "review_evidence",
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
      "query_id": "H-0116",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "product:PP-Baby_Products-B0B2LYJ3TY",
        "review:RV-AMZREV-Software-01238",
        "product:PP-Software-B007BTVS0O",
        "review:RV-AMZREV-Baby_Products-04812",
        "review:CL-All_Beauty-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0B2LYJ3TY",
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
          "doc_id": "review:RV-AMZREV-Software-01238",
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
          "rank": 3,
          "doc_id": "product:PP-Software-B007BTVS0O",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-04812",
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
          "doc_id": "review:CL-All_Beauty-delivery",
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
      "query_id": "H-0117",
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
        "product:PP-All_Beauty-B07GV9VGLD",
        "review:AS-Baby_Products-B0BC2VLLRH-price_value",
        "review:RV-AMZREV-All_Beauty-04645",
        "product:PP-All_Beauty-B0916ZRQDG",
        "product:PP-All_Beauty-B08B1PR9C7"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07GV9VGLD",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BC2VLLRH-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04645",
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
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B08B1PR9C7",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0118",
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
        "review:RV-AMZREV-All_Beauty-03862",
        "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
        "review:RV-AMZREV-All_Beauty-04395",
        "review:RV-AMZREV-All_Beauty-00002",
        "product:PP-All_Beauty-B0916ZRQDG"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03862",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04395",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00002",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
          "doc_type": "product_profile",
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
      "query_id": "H-0119",
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
      "query_id": "H-0120",
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
      "query_id": "H-0121",
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
        "product:P-BEAUTY-001"
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
          "doc_id": "product:P-BEAUTY-001",
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
      "query_id": "H-0122",
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
        "kb:KB001_return_refund_policy"
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0123",
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
        "review:CL-All_Beauty-general_complaint",
        "review:R-002",
        "ticket:T-001",
        "review:R-003"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-general_complaint",
          "doc_type": "complaint_cluster",
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
      "query_id": "H-0124",
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
        "review:R-011",
        "ticket:T-006",
        "product:P-BABY-002",
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
      "query_id": "H-0125",
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
        "review:R-011",
        "ticket:T-006"
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
      "query_id": "H-0126",
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
        "product:PP-Software-B00I4MMX7E",
        "review:RV-AMZREV-All_Beauty-00963",
        "product:PP-Software-B01LDIQ97K",
        "product:PP-Software-B008JK6W5K",
        "product:PP-All_Beauty-B0841S3FRB"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00I4MMX7E",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00963",
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
          "rank": 3,
          "doc_id": "product:PP-Software-B01LDIQ97K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B008JK6W5K",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B0841S3FRB",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0127",
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
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-All_Beauty-B00KCTER3U-skin_scent",
        "review:RV-AMZREV-All_Beauty-02755",
        "review:RV-AMZREV-All_Beauty-00740",
        "review:RV-AMZREV-All_Beauty-03909"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B00KCTER3U-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02755",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03909",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0128",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B01MA3LXIL",
        "review:AS-All_Beauty-B074TG7CVH-skin_scent",
        "review:RV-AMZREV-All_Beauty-02755",
        "product:PP-Software-B00MPBBI2G",
        "ticket:FAQ-Software-0158"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B01MA3LXIL",
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
          "doc_id": "review:AS-All_Beauty-B074TG7CVH-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02755",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00MPBBI2G",
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
          "doc_id": "ticket:FAQ-Software-0158",
          "doc_type": "faq_case",
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
      "query_id": "H-0129",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B09NCJHDX3",
        "review:RV-AMZREV-All_Beauty-00740",
        "product:PP-Software-B00HGJ18C2",
        "review:RV-AMZREV-All_Beauty-00894",
        "ticket:FAQ-Software-0088"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B09NCJHDX3",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B00HGJ18C2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00894",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0088",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0130",
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
        "review:AS-All_Beauty-B08GFLMGN2-skin_scent",
        "product:PP-All_Beauty-B08GFLMGN2",
        "review:RV-AMZREV-All_Beauty-01155",
        "review:RV-AMZREV-All_Beauty-03217",
        "review:RV-AMZREV-All_Beauty-02128"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08GFLMGN2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08GFLMGN2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01155",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03217",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02128",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0131",
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
        "review:R-011",
        "ticket:T-006"
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
      "query_id": "H-0132",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.3333333333333333,
      "mrr": 1.0,
      "ndcg@5": 0.46927872602275644,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B00ASMHGWU",
        "review:RV-AMZREV-Software-00822",
        "product:PP-Software-B00CGK71B8",
        "product:PP-Software-B00HGJ18C2",
        "review:AS-All_Beauty-B08LPC1G23-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00ASMHGWU",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-00822",
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
          "doc_id": "product:PP-Software-B00CGK71B8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 25,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00HGJ18C2",
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
          "doc_id": "review:AS-All_Beauty-B08LPC1G23-skin_scent",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0133",
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
        "review:R-006"
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
      "query_id": "H-0134",
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
        "review:RV-AMZREV-Baby_Products-04807",
        "product:PP-Baby_Products-B09XGQ8YJ7",
        "review:RV-AMZREV-Baby_Products-00896",
        "review:AS-Baby_Products-B0BJKYW5T7-delivery",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-04807",
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
          "doc_id": "product:PP-Baby_Products-B09XGQ8YJ7",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00896",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B0BJKYW5T7-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
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
      "query_id": "H-0135",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:AS-Baby_Products-B07PXV2688-quality_damage",
        "review:RV-AMZREV-Software-02279",
        "product:PP-All_Beauty-B08C24Q6LB",
        "review:RV-AMZREV-Baby_Products-00813",
        "review:CL-Software-general_complaint"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B07PXV2688-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-02279",
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
          "doc_id": "product:PP-All_Beauty-B08C24Q6LB",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-00813",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-Software-general_complaint",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0136",
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
        "review:R-002",
        "ticket:T-002",
        "product:P-BEAUTY-001",
        "product:P-BEAUTY-002"
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
          "doc_id": "product:P-BEAUTY-002",
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
      "query_id": "H-0137",
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
        "review:AS-Baby_Products-B0C5B1WSGJ-quality_damage",
        "review:RV-AMZREV-All_Beauty-00342",
        "product:PP-Software-B007TKT2SK",
        "review:AS-All_Beauty-B08JH8NGKN-skin_scent",
        "review:RV-AMZREV-Software-01142"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B0C5B1WSGJ-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00342",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B007TKT2SK",
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
          "doc_id": "review:AS-All_Beauty-B08JH8NGKN-skin_scent",
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
          "doc_id": "review:RV-AMZREV-Software-01142",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0138",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6131471927654584,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B00005Q5NT",
        "product:PP-Software-B005ZKDC32",
        "product:PP-Software-B006WBKPGA",
        "product:PP-Software-B07HRJG52T",
        "review:RV-AMZREV-All_Beauty-04547"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00005Q5NT",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B005ZKDC32",
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
          "rank": 3,
          "doc_id": "product:PP-Software-B006WBKPGA",
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
          "doc_id": "product:PP-Software-B07HRJG52T",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04547",
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
      "query_id": "H-0139",
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
      "forbidden_rate@5": 0.6,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00826",
        "review:RV-AMZREV-Baby_Products-00864",
        "review:RV-AMZREV-All_Beauty-00829",
        "review:RV-AMZREV-All_Beauty-04304",
        "review:AS-Baby_Products-B0BC2VLLRH-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00826",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00864",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00829",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04304",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B0BC2VLLRH-price_value",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0140",
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
        "review:AS-Software-B007ZGO7EM-price_value",
        "review:RV-AMZREV-All_Beauty-00737",
        "kb:KB001_return_refund_policy",
        "kb:KB004_shipping_delivery_policy",
        "product:PP-Software-B07LCQMJVN"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Software-B007ZGO7EM-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00737",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
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
          "doc_id": "kb:KB004_shipping_delivery_policy",
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
          "rank": 5,
          "doc_id": "product:PP-Software-B07LCQMJVN",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0141",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:RV-AMZREV-Software-00404",
        "review:RV-AMZREV-Baby_Products-00958",
        "review:RV-AMZREV-All_Beauty-04748",
        "review:RV-AMZREV-All_Beauty-00113",
        "review:AS-Software-B007ZGO7EM-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Software-00404",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00958",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04748",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00113",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B007ZGO7EM-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0142",
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
        "product:P-BABY-002",
        "review:R-002"
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
          "doc_id": "review:R-002",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0143",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6131471927654584,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B08KWSBN3X",
        "product:PP-Baby_Products-B0BJCBN3C8",
        "product:PP-Baby_Products-B09VFX2XXV",
        "review:RV-AMZREV-Baby_Products-00890",
        "product:PP-Baby_Products-B01N1QJ5R7"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B08KWSBN3X",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BJCBN3C8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B09VFX2XXV",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00890",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B01N1QJ5R7",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0144",
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
      "query_id": "H-0145",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 0.5,
      "ndcg@5": 0.38356636737133565,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "kb:KB001_return_refund_policy",
        "product:PP-All_Beauty-B083BDVS36",
        "ticket:FAQ-All_Beauty-0013",
        "review:AS-All_Beauty-B01M1OFZOG-refund_return",
        "review:RV-AMZREV-All_Beauty-02283"
      ],
      "signals": [
        {
          "rank": 1,
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-All_Beauty-0013",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B01M1OFZOG-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 19,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02283",
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
      "query_id": "H-0146",
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
        "ticket:T-006",
        "kb:KB001_return_refund_policy"
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0147",
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
        "product:PP-Software-B00BYJ6BUO",
        "product:PP-Software-B007W34AZO",
        "product:PP-Software-B01LXOU5PM",
        "product:PP-Software-B00A4EZ3QS",
        "review:RV-AMZREV-Software-03824"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00BYJ6BUO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B007W34AZO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B01LXOU5PM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 28,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00A4EZ3QS",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-03824",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0148",
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
          "bm25_rank": 19,
          "signals": [
            "bm25"
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
      "query_id": "H-0149",
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
        "review:R-011"
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
      "query_id": "H-0150",
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
        "product:PP-Software-B00005Q5NQ",
        "review:AS-Software-B01617VVCQ-missing_parts",
        "review:RV-AMZREV-Baby_Products-03872",
        "product:PP-Software-B005ZXRSNY",
        "ticket:FAQ-Software-0071"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00005Q5NQ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B01617VVCQ-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-03872",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005ZXRSNY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 26,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0071",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0151",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B01MA3LXIL",
        "review:AS-All_Beauty-B07SHHXSPL-price_value",
        "review:RV-AMZREV-Baby_Products-01791",
        "product:PP-All_Beauty-B0916ZRQDG",
        "product:PP-All_Beauty-B083TLNBJJ"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B01MA3LXIL",
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
          "doc_id": "review:AS-All_Beauty-B07SHHXSPL-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 17,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01791",
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
          "doc_id": "product:PP-All_Beauty-B0916ZRQDG",
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
          "doc_id": "product:PP-All_Beauty-B083TLNBJJ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0152",
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
        "ticket:T-006",
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
        }
      ]
    },
    {
      "query_id": "H-0153",
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
        "ticket:T-006",
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
        }
      ]
    },
    {
      "query_id": "H-0154",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.6,
      "recall@5": 0.6,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0006",
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
        "product:PP-All_Beauty-B08M3C6LVS",
        "product:PP-All_Beauty-B083BDVS36",
        "review:RV-AMZREV-All_Beauty-00027"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0006",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08M3C6LVS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00027",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0155",
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
        "product:PP-Baby_Products-B07GD6447J",
        "review:RV-AMZREV-All_Beauty-02758",
        "product:PP-Baby_Products-B09TKKRXTM",
        "product:PP-Baby_Products-B09T74WZF7",
        "product:PP-Baby_Products-B0B4BPCTMZ"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B07GD6447J",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02758",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B09TKKRXTM",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B09T74WZF7",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Baby_Products-B0B4BPCTMZ",
          "doc_type": "product_profile",
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
      "query_id": "H-0156",
      "intent": "customer_ops",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B007MB4YW0",
        "review:RV-AMZREV-All_Beauty-02347",
        "review:RV-AMZREV-All_Beauty-01504",
        "review:RV-AMZREV-All_Beauty-04524",
        "ticket:FAQ-Software-0005"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B007MB4YW0",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02347",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01504",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04524",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0005",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0157",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.125,
      "mrr": 0.5,
      "ndcg@5": 0.21398626473452756,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-All_Beauty-B09FP8PP2K-price_value",
        "ticket:FAQ-All_Beauty-0014",
        "review:AS-All_Beauty-B01EKSKUL6-price_value",
        "product:PP-Baby_Products-B08KWSBN3X",
        "review:RV-AMZREV-All_Beauty-01847"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:FAQ-All_Beauty-0014",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B01EKSKUL6-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B08KWSBN3X",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01847",
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
      "query_id": "H-0158",
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "kb:KB001_return_refund_policy",
        "kb:KB006_return_status_matrix",
        "review:RV-AMZREV-All_Beauty-03612",
        "product:PP-Baby_Products-B09B3FT1W8",
        "review:AS-All_Beauty-B00YQ6X8EO-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03612",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B09B3FT1W8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-delivery",
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
      "query_id": "H-0159",
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
        "ticket:T-006",
        "kb:KB001_return_refund_policy"
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0160",
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
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-All_Beauty-B07VGBBNTH-skin_scent",
        "review:RV-AMZREV-All_Beauty-02328",
        "review:RV-AMZREV-All_Beauty-04951",
        "review:RV-AMZREV-All_Beauty-00740"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 22,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07VGBBNTH-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02328",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04951",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0161",
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
        "review:RV-AMZREV-Baby_Products-01791",
        "product:PP-Software-B005ZKC3YG",
        "review:RV-AMZREV-All_Beauty-03256",
        "review:RV-AMZREV-All_Beauty-00703",
        "review:RV-AMZREV-All_Beauty-00182"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-01791",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B005ZKC3YG",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03256",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00703",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00182",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0162",
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
        "review:RV-AMZREV-All_Beauty-00830",
        "product:PP-Baby_Products-B09B3FT1W8",
        "review:RV-AMZREV-All_Beauty-02429",
        "review:RV-AMZREV-All_Beauty-03115",
        "review:RV-AMZREV-All_Beauty-03182"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00830",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B09B3FT1W8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02429",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03115",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03182",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0163",
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
      "query_id": "H-0164",
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
        "product:PP-Software-B009L9Z6G4",
        "review:AS-All_Beauty-B07H281V4V-price_value",
        "review:RV-AMZREV-All_Beauty-02755",
        "product:PP-All_Beauty-B00L5HZCPU",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B009L9Z6G4",
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
          "doc_id": "review:AS-All_Beauty-B07H281V4V-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02755",
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
          "doc_id": "product:PP-All_Beauty-B00L5HZCPU",
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0165",
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
        "review:RV-AMZREV-Baby_Products-01161",
        "review:RV-AMZREV-All_Beauty-00740",
        "review:RV-AMZREV-All_Beauty-00674",
        "review:RV-AMZREV-Software-04924",
        "product:PP-All_Beauty-B07CSL21J8"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-01161",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00674",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-04924",
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
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0166",
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
      "query_id": "H-0167",
      "intent": "customer_ops",
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
        "product:PP-All_Beauty-B072JX8LV5",
        "review:AS-Baby_Products-B0BM5NFFF3-quality_damage",
        "review:RV-AMZREV-All_Beauty-00198",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "ticket:FAQ-Baby_Products-0004"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BM5NFFF3-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00198",
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
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 30,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0004",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0168",
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
        "review:RV-AMZREV-Baby_Products-04016",
        "review:RV-AMZREV-All_Beauty-04933",
        "review:RV-AMZREV-Baby_Products-00139",
        "review:RV-AMZREV-Baby_Products-00141",
        "review:AS-Software-B017250D16-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-04016",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04933",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-00139",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-00141",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B017250D16-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0169",
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
        "product:P-SOFT-001",
        "product:P-BEAUTY-001"
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
          "doc_id": "product:P-BEAUTY-001",
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
      "query_id": "H-0170",
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
        "ticket:T-006",
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
        }
      ]
    },
    {
      "query_id": "H-0171",
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
        "review:AS-All_Beauty-B083TLNBJJ-skin_scent",
        "review:RV-AMZREV-All_Beauty-00686",
        "product:PP-All_Beauty-B08DX9P6V1",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B083TLNBJJ-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00686",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-All_Beauty-B08DX9P6V1",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0172",
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
        "review:RV-AMZREV-All_Beauty-02523",
        "review:RV-AMZREV-Baby_Products-02383",
        "review:RV-AMZREV-Baby_Products-03790",
        "review:RV-AMZREV-All_Beauty-01351",
        "review:AS-All_Beauty-B08K2HC58L-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02523",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-02383",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-03790",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01351",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B08K2HC58L-price_value",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0173",
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
      "query_id": "H-0174",
      "intent": "recommendation",
      "expected_action": "answer",
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
        "review:RV-AMZREV-All_Beauty-00740",
        "review:RV-AMZREV-Software-01240",
        "review:RV-AMZREV-All_Beauty-00674",
        "review:RV-AMZREV-Baby_Products-04319",
        "review:AS-Software-B004SIIBGU-refund_return"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-01240",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00674",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-04319",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B004SIIBGU-refund_return",
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
      "query_id": "H-0175",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 0.3333333333333333,
      "ndcg@5": 0.16958010263680806,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:AS-All_Beauty-B08KWN77LW-skin_scent",
        "review:RV-AMZREV-All_Beauty-03256",
        "ticket:FAQ-All_Beauty-0006",
        "review:AS-All_Beauty-B089RZ67T7-skin_scent",
        "product:PP-All_Beauty-B083BDVS36"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08KWN77LW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03256",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-All_Beauty-0006",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B089RZ67T7-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0176",
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
      "query_id": "H-0177",
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
        "product:PP-Software-B009ZZDNT6",
        "product:PP-Software-B07LCQMJVN",
        "product:PP-Software-B00ABXA1HI",
        "product:PP-Software-B01N0BP507",
        "review:AS-Software-B018IOV40E-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B009ZZDNT6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B07LCQMJVN",
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
          "doc_id": "product:PP-Software-B00ABXA1HI",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B01N0BP507",
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
          "doc_id": "review:AS-Software-B018IOV40E-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0178",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.5855700749881525,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B07KG1TWP5",
        "review:RV-AMZREV-All_Beauty-03222",
        "review:RV-AMZREV-All_Beauty-00015",
        "review:RV-AMZREV-All_Beauty-01375",
        "review:AS-All_Beauty-B07KG1TWP5-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07KG1TWP5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03222",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00015",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01375",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
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
      "query_id": "H-0179",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:AS-Baby_Products-B0873X984F-delivery",
        "review:RV-AMZREV-Software-04924",
        "product:PP-All_Beauty-B081ZN3TD5",
        "review:AS-All_Beauty-B0149YNDP6-delivery",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B0873X984F-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-04924",
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
          "doc_id": "product:PP-All_Beauty-B081ZN3TD5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0149YNDP6-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 4,
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
          "bm25_rank": 12,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "H-0180",
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
        "kb:KB007_carrier_exception_notice",
        "product:PP-Software-B01N0BP507",
        "product:PP-Software-B01923M8T6",
        "product:PP-All_Beauty-B07VDCD17L",
        "review:AS-All_Beauty-B07VDCD17L-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "kb:KB007_carrier_exception_notice",
          "doc_type": "text_notice",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B01N0BP507",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B01923M8T6",
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
          "doc_id": "product:PP-All_Beauty-B07VDCD17L",
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
          "doc_id": "review:AS-All_Beauty-B07VDCD17L-skin_scent",
          "doc_type": "review_aspect_summary",
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
      "query_id": "H-0181",
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
      "query_id": "H-0182",
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
      "query_id": "H-0183",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.2,
      "mrr": 0.5,
      "ndcg@5": 0.21398626473452756,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-Baby_Products-B0C9SY2V2H-quality_damage",
        "review:RV-AMZREV-Software-00035",
        "product:PP-Baby_Products-B00Q65V72S",
        "review:AS-All_Beauty-B07WRF6KMW-skin_scent",
        "review:CL-Software-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B0C9SY2V2H-quality_damage",
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
          "doc_id": "review:RV-AMZREV-Software-00035",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B00Q65V72S",
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
          "doc_id": "review:AS-All_Beauty-B07WRF6KMW-skin_scent",
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
          "doc_id": "review:CL-Software-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0184",
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
      "query_id": "H-0185",
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
        "product:PP-Baby_Products-B0BM8555XB",
        "product:PP-Baby_Products-B0BXTNL2NY",
        "product:PP-Baby_Products-B07X8QYG66",
        "product:PP-Baby_Products-B099RZ14B8",
        "review:AS-Baby_Products-B005GXXLYS-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B0BM8555XB",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BXTNL2NY",
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
          "doc_id": "product:PP-Baby_Products-B07X8QYG66",
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
          "doc_id": "product:PP-Baby_Products-B099RZ14B8",
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
          "doc_id": "review:AS-Baby_Products-B005GXXLYS-skin_scent",
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
      "query_id": "H-0186",
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
        "product:PP-Software-B00LG25894",
        "review:AS-Baby_Products-B0B5DR7K5K-missing_parts",
        "review:RV-AMZREV-Baby_Products-00932",
        "product:PP-Baby_Products-B09JKZV63T",
        "product:PP-Software-B0000C66VY"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00LG25894",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0B5DR7K5K-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00932",
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
          "doc_id": "product:PP-Baby_Products-B09JKZV63T",
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
          "doc_id": "product:PP-Software-B0000C66VY",
          "doc_type": "product_profile",
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
      "query_id": "H-0187",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.8,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B07KG1TWP5",
        "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
        "review:RV-AMZREV-All_Beauty-00015",
        "review:RV-AMZREV-All_Beauty-00552",
        "review:RV-AMZREV-All_Beauty-01497"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07KG1TWP5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00015",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 26,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00552",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01497",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0188",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:AS-All_Beauty-B07D1B499B-price_value",
        "product:PP-Software-B004DPIEF6",
        "review:RV-AMZREV-Baby_Products-00958",
        "review:RV-AMZREV-Baby_Products-00993",
        "review:RV-AMZREV-All_Beauty-00172"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07D1B499B-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Software-B004DPIEF6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 23,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00958",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00993",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00172",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0189",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 0.2,
      "recall@5": 0.16666666666666666,
      "mrr": 0.3333333333333333,
      "ndcg@5": 0.16958010263680806,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-All_Beauty-B07CSL21J8",
        "review:RV-AMZREV-Baby_Products-00879",
        "ticket:FAQ-Software-0011",
        "ticket:FAQ-All_Beauty-0088",
        "ticket:FAQ-All_Beauty-0089"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-00879",
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
          "doc_id": "ticket:FAQ-Software-0011",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "ticket:FAQ-All_Beauty-0088",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0089",
          "doc_type": "faq_case",
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
      "query_id": "H-0190",
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
        "product:P-BABY-001",
        "ticket:T-005"
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
          "doc_id": "ticket:T-005",
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
      "query_id": "H-0191",
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
        "product:P-BABY-002",
        "ticket:T-006"
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
      "query_id": "H-0192",
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
        "product:P-BEAUTY-001",
        "review:R-002",
        "review:R-001",
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
      "query_id": "H-0193",
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
        "product:PP-All_Beauty-B01LY4FP5K",
        "review:AS-All_Beauty-B08NPBQR9L-skin_scent",
        "review:RV-AMZREV-All_Beauty-02670",
        "product:PP-All_Beauty-B07N8JMJGY",
        "review:CL-All_Beauty-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B01LY4FP5K",
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
          "doc_id": "review:AS-All_Beauty-B08NPBQR9L-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02670",
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
          "doc_id": "product:PP-All_Beauty-B07N8JMJGY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-All_Beauty-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        }
      ]
    },
    {
      "query_id": "H-0194",
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
        "ticket:T-006",
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
        }
      ]
    },
    {
      "query_id": "H-0195",
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
        "product:PP-Software-B00CTQ6SIG",
        "review:AS-Software-B009L9Z6G4-refund_return",
        "review:RV-AMZREV-Software-00813",
        "product:PP-Software-B00CKOYVG8",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00CTQ6SIG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B009L9Z6G4-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 23,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00813",
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
          "rank": 4,
          "doc_id": "product:PP-Software-B00CKOYVG8",
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
          "doc_id": "kb:KB001_return_refund_policy",
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
      "query_id": "H-0196",
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
        "review:AS-All_Beauty-B01MA3LXIL-skin_scent",
        "review:RV-AMZREV-Baby_Products-01791",
        "product:PP-Baby_Products-B00ZPR8KW8",
        "review:AS-Baby_Products-B00GUN3Z1W-delivery",
        "review:AS-Software-B005AAWYR2-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B01MA3LXIL-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-01791",
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
          "doc_id": "product:PP-Baby_Products-B00ZPR8KW8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B00GUN3Z1W-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B005AAWYR2-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0197",
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
        "review:R-012",
        "ticket:T-006",
        "product:P-SOFT-002",
        "review:R-011"
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
      "query_id": "H-0198",
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
        "product:PP-All_Beauty-B017XD9GP6",
        "review:AS-All_Beauty-B000067E30-price_value",
        "review:RV-AMZREV-Baby_Products-01596",
        "product:PP-Software-B019FW1MGY",
        "review:RV-AMZREV-Baby_Products-03932"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B017XD9GP6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B000067E30-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01596",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B019FW1MGY",
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
          "doc_id": "review:RV-AMZREV-Baby_Products-03932",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25"
          ]
        }
      ]
    },
    {
      "query_id": "H-0199",
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
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00419",
        "review:RV-AMZREV-All_Beauty-00740",
        "review:AS-All_Beauty-B088X67C26-skin_scent",
        "review:RV-AMZREV-All_Beauty-01367",
        "ticket:FAQ-All_Beauty-0137"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00419",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 1,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00740",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B088X67C26-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01367",
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
          "doc_id": "ticket:FAQ-All_Beauty-0137",
          "doc_type": "faq_case",
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
      "query_id": "H-0200",
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "product:PP-All_Beauty-B07CSL21J8",
        "review:AS-All_Beauty-B07PCGSFGQ-price_value",
        "review:RV-AMZREV-All_Beauty-01062",
        "product:PP-Software-B005ZKC3YG",
        "ticket:FAQ-Software-0158"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B07CSL21J8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07PCGSFGQ-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01062",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B005ZKC3YG",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0158",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25"
          ]
        }
      ]
    }
  ],
  "support_rows": [
    {
      "query_id": "H-0001",
      "expected_intent": "support",
      "intent": "support",
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
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB001_return_refund_policy",
          "chunk_id": "ee79e051ef7a427c",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for reaching out. I understand the item you purchased was too small, and I’m here to help explain your options.\n\n**Your Options Under Our Policy**  \nOur Return and Refund Policy [doc:kb:KB001_return_refund_policy] states that cust"
    },
    {
      "query_id": "H-0002",
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
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
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
      "answer_preview": "Based on the information I have access to, I cannot determine whether the product you're asking about is worth the price or whether its size is appropriate for a toddler. The only product record retrieved is **HydraGlow Vitamin C Serum** (P"
    },
    {
      "query_id": "H-0003",
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
      "query_id": "H-0004",
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
      "query_id": "H-0005",
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
      "query_id": "H-0006",
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
      "query_id": "H-0007",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
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
          "source": "kb",
          "doc_id": "KB004_shipping_delivery_policy",
          "chunk_id": "71d755fa30c11a8e",
          "rank": 1,
          "doc_type": "policy_markdown"
        },
        {
          "source": "kb",
          "doc_id": "KB001_return_refund_policy",
          "chunk_id": "ee79e051ef7a427c",
          "rank": 2,
          "doc_type": "policy_markdown"
        },
        {
          "source": "ticket",
          "doc_id": "FAQ-All_Beauty-0110",
          "chunk_id": "a1015630f69537fd",
          "rank": 3,
          "doc_type": "faq_case"
        },
        {
          "source": "kb",
          "doc_id": "scanned_damage_claim",
          "chunk_id": "b574afb70eabbf5a",
          "rank": 4,
          "doc_type": "ocr_image"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided information, complaints about the shipping condition of items upon arrival include:\n\n- **Damaged items**: customers have reported items arriving with leaking bottles and broken pumps. For example, a damage claim form d"
    },
    {
      "query_id": "H-0008",
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
      "answer_preview": "Customers have generally positive impressions of the **NightView Baby Monitor**, which holds an **average rating of 4.4 / 5** based on 932 ratings [doc:product:P-BABY-001#b5c4f3e2496ef945]. However, one recent verified review gave a **2‑sta"
    },
    {
      "query_id": "H-0009",
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
      "citation_count": 4,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "R-005",
          "chunk_id": "2a1a90c64b8a0e30",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-SOFT-001",
          "chunk_id": "379d92ed1d5b4648",
          "rank": 2,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-007",
          "chunk_id": "78076c5983e8c9cd",
          "rank": 3,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-SOFT-002",
          "chunk_id": "cc2f8e67d7bf53ec",
          "rank": 4,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the product and review information available, the most relevant complaints about license activation and content access involve email delivery for a license key and unexpected subscription renewal timing.  \n\n- A review for **PDF Stu"
    },
    {
      "query_id": "H-0010",
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
      "query_id": "H-0011",
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
      "query_id": "H-0012",
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
      "answer_preview": "Based on the provided information, the complete refund policy document is not available. However, from previous ticket resolutions and similar case records, we can share the following specific guidelines that have been applied:\n\n- **Damaged"
    },
    {
      "query_id": "H-0013",
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
      "answer_citation_count": 6,
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
      "answer_preview": "{\n  \"answer\": \"Thank you for reaching out. Our return and refund policy varies based on the product and the reason for return. From similar cases, damaged items reported within 30 days can be refunded or replaced after validation [doc:ticke"
    },
    {
      "query_id": "H-0014",
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
      "query_id": "H-0015",
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
      "query_id": "H-0016",
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
      "query_id": "H-0017",
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
      "query_id": "H-0018",
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
      "query_id": "H-0019",
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
      "query_id": "H-0020",
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
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
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
      "answer_preview": "Based on the available customer feedback for the baby products in context, a problem has been reported with the **NightView Baby Monitor**. One verified purchaser gave it a 2-star rating and highlighted that **the battery drained overnight*"
    },
    {
      "query_id": "H-0021",
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
      "query_id": "H-0022",
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
      "query_id": "H-0023",
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
      "query_id": "H-0024",
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
      "query_id": "H-0025",
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
      "query_id": "H-0026",
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
      "query_id": "H-0027",
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
      "query_id": "H-0028",
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
      "query_id": "H-0029",
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
      "query_id": "H-0030",
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
      "query_id": "H-0031",
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
          "source": "review",
          "doc_id": "R-003",
          "chunk_id": "b1f9d8d8d461916a",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
          "rank": 2,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information I have, I cannot provide a precise count of customers who reported issues with the Ionic Compact Hair Dryer. \n\nThe only direct customer report available is one review (rating: 2) that states the dryer stopped workin"
    },
    {
      "query_id": "H-0032",
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
      "answer_preview": "I cannot find any customer feedback regarding the smell of the baby item (NightView Baby Monitor) in the provided information. The product description [doc:product:P-BABY-001#b5c4f3e2496ef945] and the single available customer review [doc:r"
    },
    {
      "query_id": "H-0033",
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
      "query_id": "H-0034",
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
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03182",
          "chunk_id": "609f0f01aabfb1e8",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00841",
          "chunk_id": "3320e3d1f6b8848a",
          "rank": 2,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03660",
          "chunk_id": "76dc8a5621df095d",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-04304",
          "chunk_id": "d073717b9fecc0f8",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I’m unable to answer how this beauty item is powered based on the information provided. The product search returned no results, and none of the included reviews or context mention any power source. Please provide more details about the spec"
    },
    {
      "query_id": "H-0035",
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
      "query_id": "H-0036",
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
      "query_id": "H-0037",
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
      "answer_preview": "The HydraGlow Vitamin C Serum is described as **fragrance‑free**, meaning it is formulated without added scents and should not have a strong or noticeable smell [doc:product:P-BEAUTY-001#8dcd5d4642a6ec23]."
    },
    {
      "query_id": "H-0038",
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
      "query_id": "H-0039",
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
      "query_id": "H-0040",
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
      "query_id": "H-0041",
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
      "answer_citation_count": 6,
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the current catalog and reviews, it looks like you're asking about the **NightView Baby Monitor**. Here is the full breakdown:\n\n**Features**\nThe NightView Baby Monitor is designed specifically for nursery use. It includes **night v"
    },
    {
      "query_id": "H-0042",
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
      "query_id": "H-0043",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unsafe_commitment",
        "no_context"
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
      "query_id": "H-0044",
      "expected_intent": "customer_ops",
      "intent": "sku_order",
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
      "citation_count": 1,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "P-SOFT-002",
          "chunk_id": "cc2f8e67d7bf53ec",
          "rank": 1,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the information available, I cannot provide details about the price or customer reviews of a mattress protector. The retrieved data only references a **Cloud Backup Family Plan (software subscription)** priced at $79.00 with an ave"
    },
    {
      "query_id": "H-0045",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "unsafe_commitment",
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
      "query_id": "H-0046",
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
      "query_id": "H-0047",
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
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
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
      "answer_preview": "Based on the available reviews and summaries for the NightView Baby Monitor, there is **no mention of smell** in any of the provided data. The reviews discuss battery life, delivery, night vision, two-way audio, and temperature alerts, but "
    },
    {
      "query_id": "H-0048",
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
      "query_id": "H-0049",
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
          "doc_id": "R-004",
          "chunk_id": "490e079c4c5a7f26",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I don’t have shipping or delivery time information in the available data. The product details I found (for the **HydraGlow Vitamin C Serum** and the **Ionic Compact Hair Dryer**) include descriptions, prices, and stock, but no estimates for"
    },
    {
      "query_id": "H-0050",
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
      "query_id": "H-0051",
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
      "query_id": "H-0052",
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
      "query_id": "H-0053",
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
      "query_id": "H-0054",
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
      "query_id": "H-0055",
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
      "query_id": "H-0056",
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
      "query_id": "H-0057",
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
      "query_id": "H-0058",
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
      "query_id": "H-0059",
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
      "query_id": "H-0060",
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
      "query_id": "H-0061",
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
      "query_id": "H-0062",
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
      "answer_preview": "I’m sorry your item arrived defective. Based on similar cases, we can help you get a replacement and track its shipping once we have the necessary information.\n\n**Getting a replacement**:  \nTo start the replacement process, please provide:\n"
    },
    {
      "query_id": "H-0063",
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
      "query_id": "H-0064",
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
      "query_id": "H-0065",
      "expected_intent": "recommendation",
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
      "answer_preview": "The **NightView Baby Monitor** has an average rating of **4.4 out of 5**, based on **932 reviews**.[doc:product:P-BABY-001#b5c4f3e2496ef945][tool:sql.product_search]"
    },
    {
      "query_id": "H-0066",
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
      "query_id": "H-0067",
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
      "query_id": "H-0068",
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
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry, but I don’t have any information about washcloths in the provided data. The product search and reviews available are for a serum and a hair dryer, and none of the documents describe washcloths or their suitability for sensitive s"
    },
    {
      "query_id": "H-0069",
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
      "query_id": "H-0070",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_product"
      ],
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
          "doc_id": "R-001",
          "chunk_id": "c248dad601bafaf8",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for your interest in our beauty products! Based on the information I have, I can see the **HydraGlow Vitamin C Serum** is a popular item priced at $24.99 with a 4.5‑star rating [doc:product:P-BEAUTY-001#8dcd5d4642a6ec23]. I also f"
    },
    {
      "query_id": "H-0071",
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
      "query_id": "H-0072",
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
      "query_id": "H-0073",
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
      "query_id": "H-0074",
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
      "query_id": "H-0075",
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
      "query_id": "H-0076",
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
      "query_id": "H-0077",
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
      "query_id": "H-0078",
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
      "query_id": "H-0079",
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
      "query_id": "H-0080",
      "expected_intent": "customer_ops",
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
      "answer_preview": "I'm sorry, but the information I have access to does not include any data about a diaper balm. The product and customer feedback you see in the retrieved context is for an **Ionic Compact Hair Dryer** (SKU: BEAUTY-DRYER-02, price $39.50, ra"
    },
    {
      "query_id": "H-0081",
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
      "answer_preview": "I don't have information about a TV service in the provided materials. The available records cover refund and return policies for products like baby monitors, vitamin C serum, software licenses, and baby bottles, but nothing related to a TV"
    },
    {
      "query_id": "H-0082",
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
      "query_id": "H-0083",
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
      "query_id": "H-0084",
      "expected_intent": "customer_ops",
      "intent": "support",
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
          "source": "ticket",
          "doc_id": "T-002",
          "chunk_id": "c2cbb38083f73a1b",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB001_return_refund_policy",
          "chunk_id": "ee79e051ef7a427c",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context and tool results, **no review text is included**. The materials contain a ticket about a warranty question and a general return/refund policy document, but neither is a customer review that could be checked for"
    },
    {
      "query_id": "H-0085",
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
      "query_id": "H-0086",
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
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I understand you're saying a baby item is too short, but from the information I have I can't tell which product you're referring to or how it's too short. The baby products currently available are:\n\n- **NightView Baby Monitor** – a nursery "
    },
    {
      "query_id": "H-0087",
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
      "query_id": "H-0088",
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry, but I couldn't find any product in our catalog that matches your description—something used under a pet water bowl with raised edges and good ratings. The product search returned items in the baby, beauty, and software categories"
    },
    {
      "query_id": "H-0089",
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
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the baby products available in our catalog, I do not see an item that provides extra absorbency for overnight use and comes in a large quantity. The baby products we currently carry are:\n\n- **NightView Baby Monitor** – A monitor wi"
    },
    {
      "query_id": "H-0090",
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
      "query_id": "H-0091",
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
      "query_id": "H-0092",
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
      "query_id": "H-0093",
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
      "query_id": "H-0094",
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
      "query_id": "H-0095",
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
      "query_id": "H-0096",
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry, but I cannot answer your question from the available information. The provided documents and tool results contain details about a baby monitor product and its review, as well as several unrelated products and a general review sum"
    },
    {
      "query_id": "H-0097",
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
      "query_id": "H-0098",
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
      "answer_preview": "Based on the information available, the adhesive stickers not sticking on your disposable toilet seat covers would be considered a quality defect. In similar cases where a product arrives damaged or has a functional defect, we typically req"
    },
    {
      "query_id": "H-0099",
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
      "query_id": "H-0100",
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
      "query_id": "H-0101",
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
      "query_id": "H-0102",
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
      "query_id": "H-0103",
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
      "query_id": "H-0104",
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
      "query_id": "H-0105",
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
      "query_id": "H-0106",
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
      "query_id": "H-0107",
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
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Thank you for your question. I searched our product catalog for items matching your description of \"easy to put on and take off\" and \"machine washable,\" but unfortunately, none of the available products (which include baby bottles, a serum,"
    },
    {
      "query_id": "H-0108",
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
      "query_id": "H-0109",
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
      "query_id": "H-0110",
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
      "query_id": "H-0111",
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
      "query_id": "H-0112",
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
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-003",
          "chunk_id": "b1f9d8d8d461916a",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, I cannot identify which specific beauty item you are referring to because the retrieved documents describe two different products: the **HydraGlow Vitamin C Serum** (P‑BEAUTY‑001) and the **Ionic Compact "
    },
    {
      "query_id": "H-0113",
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
      "query_id": "H-0114",
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
      "query_id": "H-0115",
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
      "query_id": "H-0116",
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
      "query_id": "H-0117",
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
      "query_id": "H-0118",
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
      "citation_count": 4,
      "answer_citation_count": 4,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03862",
          "chunk_id": "450c0e191a347ccd",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B081TJ8YS3-skin_scent",
          "chunk_id": "ba84a50ce3bd530d",
          "rank": 2,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-04395",
          "chunk_id": "b978389591e14146",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00002",
          "chunk_id": "bc65a88042312693",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm not sure which beauty item you're referring to in your question. Could you please provide the product name or SKU? That way I can give you the right information about its scent.\n\nBased on the reviews I have, here's what customers have s"
    },
    {
      "query_id": "H-0119",
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
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available product and review information, I can find **no mention of washcloths**, nor any reference to a scent that might affect sensitive skin. The provided data only includes a HydraGlow Vitamin C Serum (fragrance‑free and n"
    },
    {
      "query_id": "H-0120",
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
      "answer_preview": "Based on the available information, I cannot provide a review that meets your request. The only review in the provided context is for the **NightView Baby Monitor** ([doc:product:P-BABY-001#b5c4f3e2496ef945]), and it is negative – reporting"
    },
    {
      "query_id": "H-0121",
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
      "answer_preview": "I can't confirm whether you can still get a refund because the provided information does not include any return policy, eligibility details, or order records for that beauty item. Without these details, I'm unable to assess your situation. "
    },
    {
      "query_id": "H-0122",
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
      "query_id": "H-0123",
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
      "query_id": "H-0124",
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
      "query_id": "H-0125",
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
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the product information available, I do not have any details about spare parts, their compatibility with the main device, or recommended replacement intervals for either the NightView Baby Monitor or the Anti-Colic Glass Bottle Set"
    },
    {
      "query_id": "H-0126",
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
      "query_id": "H-0127",
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
      "query_id": "H-0128",
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
      "query_id": "H-0129",
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
      "query_id": "H-0130",
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
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
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
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the product catalog and review information available, there is **no brush product** referenced in the provided data. The only products listed are a **HydraGlow Vitamin C Serum** ([doc:product:P-BEAUTY-001#8dcd5d4642a6ec23]) and an "
    },
    {
      "query_id": "H-0131",
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
      "citation_count": 2,
      "answer_citation_count": 0,
      "citation_failures": [
        "missing_answer_citation"
      ],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "R-011",
          "chunk_id": "23590fb96a887844",
          "rank": 1,
          "doc_type": "review"
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
      "answer_preview": "I'm unable to find any edge protectors in our current product listings or any reviews that match your request. The products returned from the search are for baby bottles, baby monitors, a vitamin C serum, and a software plan — none are edge"
    },
    {
      "query_id": "H-0132",
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
      "query_id": "H-0133",
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
      "query_id": "H-0134",
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
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 3,
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
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
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
      "answer_preview": "I don’t have specific information about shipping options for the baby item you are asking about. The available documents and tool results include two baby products (NightView Baby Monitor and Anti-Colic Glass Bottle Set) and cover warranty "
    },
    {
      "query_id": "H-0135",
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
      "query_id": "H-0136",
      "expected_intent": "recommendation",
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
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "R-003",
          "chunk_id": "b1f9d8d8d461916a",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 2,
          "doc_type": "product"
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
      "answer_preview": "Based on the product information, the beauty item is the **HydraGlow Vitamin C Serum** (product ID P-BEAUTY-001).  \n\n- **Average customer rating:** 4.5 out of 5 [doc:product:P-BEAUTY-001#8dcd5d4642a6ec23].  \n- **Active ingredients:** vitami"
    },
    {
      "query_id": "H-0137",
      "expected_intent": "recommendation",
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
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 2,
          "doc_type": "product"
        },
        {
          "source": "product",
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 3,
          "doc_type": "product"
        },
        {
          "source": "product",
          "doc_id": "P-BABY-002",
          "chunk_id": "f16c5ecbec43cadb",
          "rank": 4,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, here are a few products we have, along with their average ratings and any common issues mentioned in customer reviews.\n\n- **NightView Baby Monitor**  \n  Average rating: **4.4** (out of 5) [doc:product:P-B"
    },
    {
      "query_id": "H-0138",
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
      "query_id": "H-0139",
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
      "query_id": "H-0140",
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
      "answer_citation_recall": 1.0,
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
      "answer_preview": "I don’t have enough context to identify exactly which “item” you’re referring to. Based on the records available, I can share shipping‑related complaints that were handled for several different products:\n\n*   **Baby Monitor** – late deliver"
    },
    {
      "query_id": "H-0141",
      "expected_intent": "customer_ops",
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
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
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
      "answer_preview": "I'm sorry, but I cannot answer your question about reviews for \"this app.\" The information I have access to does not include any reviews, price‑value comments, or any reference to an app. The only product context provided is for an Ionic Co"
    },
    {
      "query_id": "H-0142",
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
      "query_id": "H-0143",
      "expected_intent": "customer_ops",
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
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
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
      "answer_preview": "I don't have any information in the provided context about a \"baby memory book.\" The available details only cover a **NightView Baby Monitor** (P‑BABY‑001) and a ticket about a missing bottle cap. Without any data on the memory book’s price"
    },
    {
      "query_id": "H-0144",
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
      "query_id": "H-0145",
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
      "answer_preview": "I’m sorry to hear the gold eye mask didn’t meet your expectations. Unfortunately, I’m unable to find a matching product or a specific return policy for dissatisfaction in the information available to me.\n\n- A search of our product catalog d"
    },
    {
      "query_id": "H-0146",
      "expected_intent": "support",
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
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 2,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "{\n  \"answer\": \"I'm sorry, but I cannot find any information about a baby playpen with gate in the provided context or tool results. The product search returned only a baby monitor and a bottle set, neither of which is a playpen. I recommend"
    },
    {
      "query_id": "H-0147",
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
      "query_id": "H-0148",
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
      "query_id": "H-0149",
      "expected_intent": "recommendation",
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
      "answer_preview": "The baby item is the **NightView Baby Monitor** [tool:sql.product_search]. Based on the product information, its key features are:\n\n- **Night Vision**\n- **Two-Way Audio**\n- **Temperature Sensor**\n- **Long Battery Life**\n- **Price:** $89.99\n"
    },
    {
      "query_id": "H-0150",
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
      "query_id": "H-0151",
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
      "query_id": "H-0152",
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
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "product",
          "doc_id": "P-BABY-001",
          "chunk_id": "b5c4f3e2496ef945",
          "rank": 2,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, the only review for the NightView Baby Monitor (a baby monitor with night vision, audio, and temperature alerts) mentions two complaints: **late delivery** and the **battery draining overnight**[doc:revie"
    },
    {
      "query_id": "H-0153",
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
      "query_id": "H-0154",
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
      "query_id": "H-0155",
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
      "query_id": "H-0156",
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
      "query_id": "H-0157",
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
      "query_id": "H-0158",
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
      "query_id": "H-0159",
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
      "query_id": "H-0160",
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
      "query_id": "H-0161",
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
      "query_id": "H-0162",
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
      "query_id": "H-0163",
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
          "doc_id": "R-001",
          "chunk_id": "c248dad601bafaf8",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The HydraGlow Vitamin C Serum is fragrance-free, as noted in its product description [doc:product:P-BEAUTY-001#8dcd5d4642a6ec23]. No specific fragrance is added to this beauty item."
    },
    {
      "query_id": "H-0164",
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
      "query_id": "H-0165",
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
      "answer_preview": "I am unable to answer your question about user reviews on refunds and returns for a streaming service. The available context and tool results contain only information about physical products (such as baby monitors, vitamin C serum, baby bot"
    },
    {
      "query_id": "H-0166",
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
          "doc_id": "P-BEAUTY-001",
          "chunk_id": "8dcd5d4642a6ec23",
          "rank": 1,
          "doc_type": "product"
        },
        {
          "source": "review",
          "doc_id": "R-003",
          "chunk_id": "b1f9d8d8d461916a",
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
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I am unable to answer this question because the provided context and tool results do not contain any information about a hair straightener. The products referenced are a **HydraGlow Vitamin C Serum** [doc:product:P-BEAUTY-001#8dcd5d4642a6ec"
    },
    {
      "query_id": "H-0167",
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
      "query_id": "H-0168",
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
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
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
      "answer_preview": "Based on the available context and tool results, I cannot find a review that explicitly states a \"better alternative\" for a product that is \"not recommended.\"\n\nHere is what the provided information shows:\n\n- **One review with a low rating:*"
    },
    {
      "query_id": "H-0169",
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
      "query_id": "H-0170",
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
      "query_id": "H-0171",
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
      "query_id": "H-0172",
      "expected_intent": "recommendation",
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
          "source": "review",
          "doc_id": "R-009",
          "chunk_id": "f214a7e5ff92c052",
          "rank": 1,
          "doc_type": "review"
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
      "answer_preview": "I see you're interested in an accessory and whether reviews mention it being flimsy or not worth the cost. Based on the information I have, I need a bit more detail to give you a useful answer.\n\nThere are a few products returned by our sear"
    },
    {
      "query_id": "H-0173",
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
      "query_id": "H-0174",
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
      "query_id": "H-0175",
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
      "query_id": "H-0176",
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
      "query_id": "H-0177",
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
      "query_id": "H-0178",
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
      "query_id": "H-0179",
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
      "answer_preview": "The provided context does **not include any product reviews** (the review summaries field is empty), so I cannot directly answer from reviews.  \n\nHowever, based on similar customer support tickets that mention shipping‑related issues, the f"
    },
    {
      "query_id": "H-0180",
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
      "query_id": "H-0181",
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
      "query_id": "H-0182",
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
      "query_id": "H-0183",
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
      "query_id": "H-0184",
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
      "query_id": "H-0185",
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
      "query_id": "H-0186",
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
      "query_id": "H-0187",
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
      "query_id": "H-0188",
      "expected_intent": "customer_ops",
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
          "doc_id": "P-BEAUTY-002",
          "chunk_id": "30d1e2ed70dffd07",
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
      "answer_preview": "I'm unable to answer your question about a playmat because the provided context and tool results do not contain any information about a playmat. The available data only describes an **Ionic Compact Hair Dryer** (product ID P‑BEAUTY‑002) wit"
    },
    {
      "query_id": "H-0189",
      "expected_intent": "customer_ops",
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
      "answer_preview": "{\n  \"answer\": \"Based on the available information, the Anti-Colic Glass Bottle Set is priced at $28.00 and holds an average rating of 4.6 out of 5. However, there are no specific user comments about its price or value in the provided contex"
    },
    {
      "query_id": "H-0190",
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
      "query_id": "H-0191",
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
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available product information and reviews, there is no mention of a \"baby gate\" product in your store records. The products currently on file are:\n\n- NightView Baby Monitor ([doc:product:P-BABY-001#b5c4f3e2496ef945])\n- Anti-Col"
    },
    {
      "query_id": "H-0192",
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
      "query_id": "H-0193",
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
      "query_id": "H-0194",
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
      "query_id": "H-0195",
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
      "query_id": "H-0196",
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
      "query_id": "H-0197",
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
      "query_id": "H-0198",
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
      "query_id": "H-0199",
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
      "query_id": "H-0200",
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
    }
  ]
}
```
