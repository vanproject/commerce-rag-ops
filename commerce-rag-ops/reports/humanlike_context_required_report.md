# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: humanlike_context_required
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_context_required.jsonl
- Oracle sources: False

## 摘要

- 样本数: 10
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 0.0
- Recall@5: 0.0
- MRR: 0.0
- NDCG@5: 0.0
- exact_recall@5: 0.0
- acceptable_recall@5: 0.0
- entity_accuracy@5: 0.0
- aspect_accuracy@5: 0.8
- forbidden_rate@5: 0.04
- Action accuracy: 1.0
- 引用率: 1.0
- Citation leak rate(refuse/clarify): 0.0
- Citation schema OK: 1.0
- Answer citation precision/recall: 1.0 / 1.0
- Citation grounded rate: 1.0
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.6
- 延迟 p50/p95: 5499 ms / 17528 ms
- Embedding 模型: local-token-cosine
- Reranker 模型: none
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |
| recommendation | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |
| support | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 10 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 25 | 0 |
| dense | 19 | 0 |
| forced_fallback | 8 | 0 |
| policy_fallback | 3 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|

## Agentic 证据诊断

- 重试率: 0.0

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | clarify: 10 |
| 尝试次数 | 1: 10 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_customer_voice | 1 |
| missing_review | 1 |
| missing_structured_entity | 1 |
| no_context | 1 |
| unknown_intent | 3 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| none | 0 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_customer_voice: 1, no_context: 1, unknown_intent: 1 |
| recommendation | missing_review: 1, unknown_intent: 1 |
| support | missing_structured_entity: 1, unknown_intent: 1 |

## 原始 JSON

```json
{
  "suite": "humanlike_context_required",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\humanlike_context_required.jsonl",
  "use_oracle_sources": false,
  "n": 10,
  "retrieval_backend": "local",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "local-token-cosine",
    "embedding_backend": "local",
    "reranker_model": "none",
    "llm_model": "deepseek-v4-flash"
  },
  "retrieval": {
    "precision@5": 0.0,
    "recall@5": 0.0,
    "mrr": 0.0,
    "ndcg@5": 0.0,
    "exact_recall@5": 0.0,
    "acceptable_recall@5": 0.0,
    "entity_accuracy@5": 0.0,
    "aspect_accuracy@5": 0.8,
    "forbidden_rate@5": 0.04
  },
  "support_quality": {
    "action_accuracy": 1.0,
    "citation_ok": 1.0,
    "citation_leak_rate": 0.0,
    "citation_schema_ok": 1.0,
    "answer_citation_precision": 1.0,
    "answer_citation_recall": 1.0,
    "citation_grounded_rate": 1.0,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.6
  },
  "latency": {
    "p50_ms": 5499,
    "p95_ms": 17528
  },
  "by_intent": {
    "customer_ops": {
      "n": 4,
      "retrieval": {
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.5
      }
    },
    "recommendation": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.6667
      }
    },
    "support": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.6667
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 10,
      "retrieval": {
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.6
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 25,
      "dense": 19,
      "forced_fallback": 8,
      "policy_fallback": 3
    },
    "relevant_hit_signal_counts": {},
    "relevant_hit_signals_by_intent": {}
  },
  "agentic_diagnostics": {
    "action_counts": {
      "clarify": 10
    },
    "attempt_counts": {
      "1": 10
    },
    "retry_rate": 0.0,
    "evidence_gap_counts": {
      "missing_customer_voice": 1,
      "missing_review": 1,
      "missing_structured_entity": 1,
      "no_context": 1,
      "unknown_intent": 3
    },
    "citation_failure_counts": {},
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "missing_customer_voice": 1,
        "no_context": 1,
        "unknown_intent": 1
      },
      "recommendation": {
        "missing_review": 1,
        "unknown_intent": 1
      },
      "support": {
        "missing_structured_entity": 1,
        "unknown_intent": 1
      }
    }
  },
  "retrieval_rows": [
    {
      "query_id": "H-0001",
      "intent": "support",
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
      "query_id": "H-0010",
      "intent": "customer_ops",
      "expected_action": "clarify",
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
      "expected_action": "clarify",
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
    }
  ],
  "support_rows": [
    {
      "query_id": "H-0001",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0002",
      "expected_intent": "support",
      "intent": "sku_order",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the order ID, SKU, or product name so I can look up the right item before answering."
    },
    {
      "query_id": "H-0003",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0004",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0005",
      "expected_intent": "recommendation",
      "intent": "unknown",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0006",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "missing_review"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0007",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "missing_customer_voice"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0008",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0010",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "no_context"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "H-0011",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "clarify",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    }
  ]
}
```
