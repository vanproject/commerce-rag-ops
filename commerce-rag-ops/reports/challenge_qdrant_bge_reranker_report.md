# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: challenge
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\challenge.jsonl
- Oracle sources: False

## 摘要

- 样本数: 10
- 检索后端: qdrant
- 检索模式: hybrid_rerank
- Precision@5: 0.02
- Recall@5: 0.05
- MRR: 0.025
- NDCG@5: 0.0264
- exact_recall@5: 0.1
- acceptable_recall@5: 0.1
- entity_accuracy@5: 0.1
- aspect_accuracy@5: 0.6
- forbidden_rate@5: 0.2
- Action accuracy: 0.1
- 引用率: 0.3
- Citation leak rate(refuse/clarify): 0.0
- Citation schema OK: 0.3
- Answer citation precision/recall: 0.3 / 0.3
- Citation grounded rate: 0.3
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.289
- 延迟 p50/p95: 150 ms / 76074 ms
- Embedding 模型: BAAI/bge-large-en-v1.5
- Reranker 模型: BAAI/bge-reranker-large
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.75 | 0.75 | 0.75 / 0.75 | 1.0 |
| recommendation | 3 | 0.0667 | 0.1667 | 0.0833 | 0.088 | 0.0 | 0.0 | 0.0 / 0.0 | 1.0 |
| support | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 / 0.0 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 10 | 0.02 | 0.05 | 0.025 | 0.0264 | 0.3 | 0.3 | 0.3 / 0.3 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 47 | 1 |
| dense | 47 | 1 |
| policy_fallback | 1 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| recommendation | bm25: 1, dense: 1 |

## Agentic 证据诊断

- 重试率: 0.3

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | clarify: 7, refuse: 3 |
| 尝试次数 | 1: 7, 2: 3 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_policy | 1 |
| missing_structured_entity | 1 |
| no_context | 1 |
| privacy_violation | 1 |
| unknown_intent | 4 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 7 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | no_context: 1, privacy_violation: 1, unknown_intent: 1 |
| recommendation | missing_policy: 1, missing_structured_entity: 1, unknown_intent: 1 |
| support | unknown_intent: 2 |

## 原始 JSON

```json
{
  "suite": "challenge",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\challenge.jsonl",
  "use_oracle_sources": false,
  "n": 10,
  "retrieval_backend": "qdrant",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "BAAI/bge-large-en-v1.5",
    "embedding_backend": "sentence-transformers",
    "reranker_model": "BAAI/bge-reranker-large",
    "llm_model": "deepseek-v4-flash"
  },
  "retrieval": {
    "precision@5": 0.02,
    "recall@5": 0.05,
    "mrr": 0.025,
    "ndcg@5": 0.0264,
    "exact_recall@5": 0.1,
    "acceptable_recall@5": 0.1,
    "entity_accuracy@5": 0.1,
    "aspect_accuracy@5": 0.6,
    "forbidden_rate@5": 0.2
  },
  "support_quality": {
    "action_accuracy": 0.1,
    "citation_ok": 0.3,
    "citation_leak_rate": 0.0,
    "citation_schema_ok": 0.3,
    "answer_citation_precision": 0.3,
    "answer_citation_recall": 0.3,
    "citation_grounded_rate": 0.3,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.289
  },
  "latency": {
    "p50_ms": 150,
    "p95_ms": 76074
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
        "action_accuracy": 0.25,
        "citation_ok": 0.75,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.75,
        "answer_citation_precision": 0.75,
        "answer_citation_recall": 0.75,
        "citation_grounded_rate": 0.75,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.1621
      }
    },
    "recommendation": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.0667,
        "recall@5": 0.1667,
        "mrr": 0.0833,
        "ndcg@5": 0.088
      },
      "support_quality": {
        "action_accuracy": 0.0,
        "citation_ok": 0.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.0,
        "answer_citation_precision": 0.0,
        "answer_citation_recall": 0.0,
        "citation_grounded_rate": 0.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.414
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
        "action_accuracy": 0.0,
        "citation_ok": 0.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.0,
        "answer_citation_precision": 0.0,
        "answer_citation_recall": 0.0,
        "citation_grounded_rate": 0.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.3333
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 10,
      "retrieval": {
        "precision@5": 0.02,
        "recall@5": 0.05,
        "mrr": 0.025,
        "ndcg@5": 0.0264
      },
      "support_quality": {
        "action_accuracy": 0.1,
        "citation_ok": 0.3,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.3,
        "answer_citation_precision": 0.3,
        "answer_citation_recall": 0.3,
        "citation_grounded_rate": 0.3,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.289
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 47,
      "dense": 47,
      "policy_fallback": 1
    },
    "relevant_hit_signal_counts": {
      "bm25": 1,
      "dense": 1
    },
    "relevant_hit_signals_by_intent": {
      "recommendation": {
        "bm25": 1,
        "dense": 1
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "clarify": 7,
      "refuse": 3
    },
    "attempt_counts": {
      "1": 7,
      "2": 3
    },
    "retry_rate": 0.3,
    "evidence_gap_counts": {
      "missing_policy": 1,
      "missing_structured_entity": 1,
      "no_context": 1,
      "privacy_violation": 1,
      "unknown_intent": 4
    },
    "citation_failure_counts": {
      "missing_answer_citation": 7
    },
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "no_context": 1,
        "privacy_violation": 1,
        "unknown_intent": 1
      },
      "recommendation": {
        "missing_policy": 1,
        "missing_structured_entity": 1,
        "unknown_intent": 1
      },
      "support": {
        "unknown_intent": 2
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
      "forbidden_rate@5": 0.6,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04284",
        "kb:KB001_return_refund_policy",
        "ticket:FAQ-Baby_Products-0007",
        "review:CL-All_Beauty-general_complaint",
        "review:AS-Baby_Products-B0BW7CVB9K-refund_return"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04284",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-Baby_Products-0007",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:CL-All_Beauty-general_complaint",
          "doc_type": "complaint_cluster",
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
          "doc_id": "review:AS-Baby_Products-B0BW7CVB9K-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01483",
        "review:AS-All_Beauty-B005IYYF5E-missing_parts",
        "review:RV-AMZREV-All_Beauty-04791",
        "review:RV-AMZREV-All_Beauty-00497",
        "ticket:FAQ-Baby_Products-0007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01483",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 14,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04791",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 37,
          "bm25_rank": 36,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00497",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 34,
          "bm25_rank": 37,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0007",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 49,
          "bm25_rank": 42,
          "signals": [
            "dense",
            "bm25"
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
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Software-B009HQ9UHC",
        "review:AS-All_Beauty-B07S5GYK14-skin_scent",
        "review:RV-AMZREV-Baby_Products-01935",
        "review:RV-AMZREV-Software-01918",
        "ticket:FAQ-Software-0002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B009HQ9UHC",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 2,
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
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01935",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-01918",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 33,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0002",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 34,
          "bm25_rank": 35,
          "signals": [
            "dense",
            "bm25"
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
        "product:PP-All_Beauty-B072JX8LV5",
        "review:AS-All_Beauty-B0BM4GX6TT-skin_scent",
        "review:RV-AMZREV-All_Beauty-01289",
        "review:RV-AMZREV-All_Beauty-04588",
        "review:RV-AMZREV-All_Beauty-01155"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B072JX8LV5",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B0BM4GX6TT-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 39,
          "bm25_rank": 36,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01289",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 43,
          "bm25_rank": 37,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04588",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 37,
          "bm25_rank": 35,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01155",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 2,
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
      "precision@5": 0.2,
      "recall@5": 0.5,
      "mrr": 0.25,
      "ndcg@5": 0.2640681225725909,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
        "review:RV-AMZREV-Baby_Products-03196",
        "product:PP-Baby_Products-B07CCG2VSY",
        "product:PP-Baby_Products-B000056J9F",
        "ticket:FAQ-Baby_Products-0147"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B07CCG2VSY-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 25,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-03196",
          "doc_type": "review_evidence",
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
          "doc_id": "product:PP-Baby_Products-B07CCG2VSY",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B000056J9F",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0147",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
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
        "review:R-007",
        "ticket:FAQ-Software-0171",
        "ticket:FAQ-Software-0073",
        "review:RV-AMZREV-Software-03853",
        "product:PP-Software-B00N28818A"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-007",
          "doc_type": "review",
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
          "doc_id": "ticket:FAQ-Software-0171",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-Software-0073",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03853",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 16,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "product:PP-Software-B00N28818A",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
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
      "forbidden_rate@5": 0.2,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0155",
        "ticket:FAQ-All_Beauty-0169",
        "ticket:FAQ-Baby_Products-0086",
        "review:RV-AMZREV-Baby_Products-03935",
        "review:AS-Baby_Products-B0BB84JXS9-missing_parts"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0155",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:FAQ-All_Beauty-0169",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 24,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-Baby_Products-0086",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-03935",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B0BB84JXS9-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 23,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25"
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
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "product:PP-All_Beauty-B0B7RBK4NJ",
        "review:AS-All_Beauty-B00YQ6X8EO-delivery",
        "review:RV-AMZREV-Baby_Products-03871",
        "ticket:FAQ-All_Beauty-0044",
        "review:RV-AMZREV-All_Beauty-02334"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-All_Beauty-B0B7RBK4NJ",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-03871",
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
          "rank": 4,
          "doc_id": "ticket:FAQ-All_Beauty-0044",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02334",
          "doc_type": "review_evidence",
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
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "ticket:T-003",
          "doc_type": "ticket",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25"
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
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.4,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01285",
        "review:RV-AMZREV-All_Beauty-00828",
        "review:RV-AMZREV-All_Beauty-04060",
        "review:RV-AMZREV-All_Beauty-04935",
        "review:RV-AMZREV-All_Beauty-02745"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01285",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00828",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04060",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04935",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02745",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 2,
          "signals": [
            "dense",
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
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "C-0002",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "C-0003",
      "expected_intent": "support",
      "intent": "unknown",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
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
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "groundedness_proxy": 0.884,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0006",
      "expected_intent": "recommendation",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "missing_policy"
      ],
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "groundedness_proxy": 0.3579,
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "C-0007",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 0.0,
      "citation_ok": 0.0,
      "citation_leak_rate": 0.0,
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
      "groundedness_proxy": 0.2741,
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    },
    {
      "query_id": "C-0008",
      "expected_intent": "customer_ops",
      "intent": "unknown",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "action_accuracy": 0.0,
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
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "C-0010",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 0.0,
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
      "groundedness_proxy": 0.3744,
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    }
  ]
}
```
