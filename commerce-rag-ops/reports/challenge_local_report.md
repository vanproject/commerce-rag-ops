# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: challenge
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\challenge.jsonl
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
- aspect_accuracy@5: 0.4
- forbidden_rate@5: 0.02
- Action accuracy: 0.1
- 引用率: 0.3
- Citation leak rate(refuse/clarify): 0.1
- Citation schema OK: 0.3
- Answer citation precision/recall: 0.3 / 0.25
- Citation grounded rate: 0.3
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.6
- 延迟 p50/p95: 9104 ms / 52865 ms
- Embedding 模型: local-token-cosine
- Reranker 模型: none
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.75 | 0.75 | 0.75 / 0.625 | 1.0 |
| recommendation | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 / 0.0 | 1.0 |
| support | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 / 0.0 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 10 | 0.0 | 0.0 | 0.0 | 0.0 | 0.3 | 0.3 | 0.3 / 0.25 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 9 | 0 |
| dense | 11 | 0 |
| forced_fallback | 17 | 0 |
| policy_fallback | 2 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|

## Agentic 证据诊断

- 重试率: 0.2
- hard_negative_hit_rate: 0.0
- hard_negative_penalized_count: 0

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 1, clarify: 7, refuse: 2 |
| 尝试次数 | 1: 8, 2: 2 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_policy | 2 |
| missing_review | 1 |
| missing_structured_entity | 1 |
| no_context | 1 |
| privacy_violation | 1 |
| unknown_intent | 3 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 7 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_review: 1, no_context: 1, privacy_violation: 1 |
| recommendation | missing_policy: 1, missing_structured_entity: 1, unknown_intent: 1 |
| support | missing_policy: 1, unknown_intent: 2 |

## 原始 JSON

```json
{
  "suite": "challenge",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\challenge.jsonl",
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
    "aspect_accuracy@5": 0.4,
    "forbidden_rate@5": 0.02
  },
  "support_quality": {
    "action_accuracy": 0.1,
    "citation_ok": 0.3,
    "citation_leak_rate": 0.1,
    "citation_schema_ok": 0.3,
    "answer_citation_precision": 0.3,
    "answer_citation_recall": 0.25,
    "citation_grounded_rate": 0.3,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.6
  },
  "latency": {
    "p50_ms": 9104,
    "p95_ms": 52865
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
        "citation_leak_rate": 0.25,
        "citation_schema_ok": 0.75,
        "answer_citation_precision": 0.75,
        "answer_citation_recall": 0.625,
        "citation_grounded_rate": 0.75,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.75
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
        "action_accuracy": 0.0,
        "citation_ok": 0.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.0,
        "answer_citation_precision": 0.0,
        "answer_citation_recall": 0.0,
        "citation_grounded_rate": 0.0,
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
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "action_accuracy": 0.1,
        "citation_ok": 0.3,
        "citation_leak_rate": 0.1,
        "citation_schema_ok": 0.3,
        "answer_citation_precision": 0.3,
        "answer_citation_recall": 0.25,
        "citation_grounded_rate": 0.3,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.6
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 9,
      "dense": 11,
      "forced_fallback": 17,
      "policy_fallback": 2
    },
    "relevant_hit_signal_counts": {},
    "relevant_hit_signals_by_intent": {}
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 1,
      "clarify": 7,
      "refuse": 2
    },
    "attempt_counts": {
      "1": 8,
      "2": 2
    },
    "retry_rate": 0.2,
    "hard_negative_hit_rate": 0.0,
    "hard_negative_penalized_count": 0,
    "evidence_gap_counts": {
      "missing_policy": 2,
      "missing_review": 1,
      "missing_structured_entity": 1,
      "no_context": 1,
      "privacy_violation": 1,
      "unknown_intent": 3
    },
    "citation_failure_counts": {
      "missing_answer_citation": 7
    },
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "missing_review": 1,
        "no_context": 1,
        "privacy_violation": 1
      },
      "recommendation": {
        "missing_policy": 1,
        "missing_structured_entity": 1,
        "unknown_intent": 1
      },
      "support": {
        "missing_policy": 1,
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
      "evidence_gaps": [
        "missing_policy"
      ],
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "unknown_intent"
      ],
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "query_id": "C-0007",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "clarify",
      "attempts": 1,
      "evidence_gaps": [
        "missing_review"
      ],
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "query_id": "C-0008",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "refuse",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
      "action_accuracy": 0.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 1.0,
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
          "doc_id": "P-SOFT-001",
          "chunk_id": "379d92ed1d5b4648",
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
      "answer_preview": "I’m unable to answer your question based on the available evidence. The information I have only includes details for one product (PDF Studio Pro License [doc:product:P-SOFT-001#379d92ed1d5b4648]) and does not provide any mapping of package "
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "hard_negative_hit_rate": 0.0,
      "hard_negative_penalized_count": 0,
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
      "groundedness_proxy": 1.0,
      "answer_preview": "Please provide the product name, SKU, or order ID so I can answer about the correct item."
    }
  ]
}
```
