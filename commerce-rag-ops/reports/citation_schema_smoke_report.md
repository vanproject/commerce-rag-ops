# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

## 摘要

- 样本数: 25
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 1.0
- Recall@5: 0.9467
- MRR: 1.0
- NDCG@5: 1.0
- 引用率: 0.8
- Citation schema OK: 0.8
- Answer citation precision/recall: 0.8 / 0.8
- Citation grounded rate: 0.8
- 关键词覆盖率: 0.7867
- groundedness 代理指标: 1.0
- 延迟 p50/p95: 395 ms / 434 ms

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 / 1.0 | 0.6667 |
| recommendation | 20 | 1.0 | 0.9333 | 1.0 | 1.0 | 0.75 | 0.75 | 0.75 / 0.75 | 0.75 |
| sku_order | 1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |
| support | 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 / 1.0 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| medium | 19 | 1.0 | 0.9298 | 1.0 | 1.0 | 0.7368 | 0.7368 | 0.7368 / 0.7368 | 0.7368 |
| unknown | 6 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 / 1.0 | 0.9444 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 90 | 90 |
| dense | 78 | 78 |
| entity_match | 87 | 87 |
| forced_fallback | 10 | 10 |
| policy_fallback | 4 | 4 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | forced_fallback: 4 |
| recommendation | bm25: 84, dense: 71, entity_match: 87, forced_fallback: 5 |
| sku_order | bm25: 1, dense: 2, policy_fallback: 1 |
| support | bm25: 5, dense: 5, forced_fallback: 1, policy_fallback: 3 |

## Agentic 证据诊断

- 重试率: 0.2

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 20, refuse: 5 |
| 尝试次数 | 1: 20, 2: 5 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_product_context | 5 |
| missing_structured_entity | 5 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 5 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| recommendation | missing_product_context: 5, missing_structured_entity: 5 |

## 原始 JSON

```json
{
  "n": 25,
  "retrieval_backend": "local",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {},
  "retrieval": {
    "precision@5": 1.0,
    "recall@5": 0.9467,
    "mrr": 1.0,
    "ndcg@5": 1.0
  },
  "support_quality": {
    "citation_ok": 0.8,
    "citation_schema_ok": 0.8,
    "answer_citation_precision": 0.8,
    "answer_citation_recall": 0.8,
    "citation_grounded_rate": 0.8,
    "keyword_coverage": 0.7867,
    "groundedness_proxy": 1.0
  },
  "latency": {
    "p50_ms": 395,
    "p95_ms": 434
  },
  "by_intent": {
    "customer_ops": {
      "n": 1,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 1.0,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 0.6667,
        "groundedness_proxy": 1.0
      }
    },
    "recommendation": {
      "n": 20,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9333,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 0.75,
        "citation_schema_ok": 0.75,
        "answer_citation_precision": 0.75,
        "answer_citation_recall": 0.75,
        "citation_grounded_rate": 0.75,
        "keyword_coverage": 0.75,
        "groundedness_proxy": 1.0
      }
    },
    "sku_order": {
      "n": 1,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 1.0,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    },
    "support": {
      "n": 3,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 1.0,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    }
  },
  "by_difficulty": {
    "medium": {
      "n": 19,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9298,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 0.7368,
        "citation_schema_ok": 0.7368,
        "answer_citation_precision": 0.7368,
        "answer_citation_recall": 0.7368,
        "citation_grounded_rate": 0.7368,
        "keyword_coverage": 0.7368,
        "groundedness_proxy": 1.0
      }
    },
    "unknown": {
      "n": 6,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 1.0,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 1.0,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 0.9444,
        "groundedness_proxy": 1.0
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 90,
      "dense": 78,
      "entity_match": 87,
      "forced_fallback": 10,
      "policy_fallback": 4
    },
    "relevant_hit_signal_counts": {
      "bm25": 90,
      "dense": 78,
      "entity_match": 87,
      "forced_fallback": 10,
      "policy_fallback": 4
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "forced_fallback": 4
      },
      "recommendation": {
        "bm25": 84,
        "dense": 71,
        "entity_match": 87,
        "forced_fallback": 5
      },
      "sku_order": {
        "bm25": 1,
        "dense": 2,
        "policy_fallback": 1
      },
      "support": {
        "bm25": 5,
        "dense": 5,
        "forced_fallback": 1,
        "policy_fallback": 3
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 20,
      "refuse": 5
    },
    "attempt_counts": {
      "1": 20,
      "2": 5
    },
    "retry_rate": 0.2,
    "evidence_gap_counts": {
      "missing_product_context": 5,
      "missing_structured_entity": 5
    },
    "citation_failure_counts": {
      "missing_answer_citation": 5
    },
    "evidence_gaps_by_intent": {
      "recommendation": {
        "missing_product_context": 5,
        "missing_structured_entity": 5
      }
    }
  },
  "retrieval_rows": [
    {
      "query_id": "Q-001",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:T-001",
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-001",
          "doc_type": "ticket",
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "Q-002",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:T-002",
        "kb:KB002_warranty_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-002",
          "doc_type": "ticket",
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
          "doc_id": "kb:KB002_warranty_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "Q-003",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "product:P-BABY-001",
        "review:R-010"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-BABY-001",
          "doc_type": "product",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-010",
          "doc_type": "review",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "Q-004",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:R-009",
        "ticket:T-005",
        "review:R-012",
        "ticket:T-006"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-009",
          "doc_type": "review",
          "relevant": true,
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
          "relevant": true,
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
          "relevant": true,
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
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "Q-005",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "product:P-SOFT-001",
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:P-SOFT-001",
          "doc_type": "product",
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
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense",
            "policy_fallback"
          ]
        }
      ]
    },
    {
      "query_id": "Q-006",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:T-004",
        "kb:KB003_payment_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:T-004",
          "doc_type": "ticket",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB003_payment_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
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
      "query_id": "QS-0001",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04225",
        "product:PP-All_Beauty-B000067E30",
        "review:AS-All_Beauty-B000067E30-price_value",
        "review:RV-AMZREV-All_Beauty-00511",
        "review:RV-AMZREV-All_Beauty-03366"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04225",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000067E30",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000067E30-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00511",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03366",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0002",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00821",
        "product:PP-All_Beauty-B000068PBJ",
        "review:AS-All_Beauty-B000068PBJ-price_value",
        "review:RV-AMZREV-All_Beauty-04062",
        "review:RV-AMZREV-All_Beauty-03549"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00821",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000068PBJ",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000068PBJ-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04062",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03549",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0003",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00033",
        "product:PP-All_Beauty-B00023J4AW",
        "review:RV-AMZREV-All_Beauty-02567",
        "review:RV-AMZREV-All_Beauty-02030",
        "review:RV-AMZREV-All_Beauty-02207"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00033",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00023J4AW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02567",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02030",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02207",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0004",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02426",
        "product:PP-All_Beauty-B0002M5JNY",
        "review:AS-All_Beauty-B0002M5JNY-battery_power",
        "review:RV-AMZREV-All_Beauty-03989",
        "review:RV-AMZREV-All_Beauty-04067"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02426",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0002M5JNY",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0002M5JNY-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03989",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04067",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0005",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00104",
        "product:PP-All_Beauty-B0008F6QGO",
        "review:RV-AMZREV-All_Beauty-00919"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00104",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0008F6QGO",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00919",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0006",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01974",
        "product:PP-All_Beauty-B000CSH3YG",
        "review:AS-All_Beauty-B000CSH3YG-skin_scent",
        "review:RV-AMZREV-All_Beauty-02960",
        "review:RV-AMZREV-All_Beauty-03517"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01974",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000CSH3YG",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000CSH3YG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02960",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03517",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0007",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04056",
        "product:PP-All_Beauty-B000GBID0M",
        "review:AS-All_Beauty-B000GBID0M-battery_power",
        "review:RV-AMZREV-All_Beauty-04937",
        "review:RV-AMZREV-All_Beauty-04052"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04056",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000GBID0M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000GBID0M-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04937",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04052",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0008",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02795",
        "product:PP-All_Beauty-B000I1CFC2",
        "review:AS-All_Beauty-B000I1CFC2-price_value",
        "review:RV-AMZREV-All_Beauty-03554",
        "review:RV-AMZREV-All_Beauty-03093"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02795",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000I1CFC2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000I1CFC2-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03554",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03093",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0009",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00404",
        "product:PP-All_Beauty-B000LX69SI"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00404",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000LX69SI",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0010",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04380",
        "product:PP-All_Beauty-B000NHZSKC",
        "review:AS-All_Beauty-B000NHZSKC-skin_scent",
        "review:RV-AMZREV-All_Beauty-04216",
        "review:RV-AMZREV-All_Beauty-03834"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04380",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000NHZSKC",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000NHZSKC-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04216",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03834",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0011",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03825",
        "product:PP-All_Beauty-B000NIZYIW",
        "review:RV-AMZREV-All_Beauty-00647",
        "review:RV-AMZREV-All_Beauty-03769",
        "review:RV-AMZREV-All_Beauty-04920"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03825",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000NIZYIW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00647",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03769",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04920",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0012",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01189",
        "product:PP-All_Beauty-B000OQFVLS",
        "review:AS-All_Beauty-B000OQFVLS-quality_damage",
        "review:RV-AMZREV-All_Beauty-03580",
        "review:RV-AMZREV-All_Beauty-00055"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01189",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000OQFVLS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000OQFVLS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03580",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0013",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02341",
        "product:PP-All_Beauty-B000PKKAGO",
        "review:AS-All_Beauty-B000PKKAGO-battery_power",
        "review:RV-AMZREV-All_Beauty-03264",
        "review:RV-AMZREV-All_Beauty-00588"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02341",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000PKKAGO",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000PKKAGO-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03264",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00588",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0014",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01767",
        "product:PP-All_Beauty-B000X20Y4C",
        "review:RV-AMZREV-All_Beauty-01736",
        "review:RV-AMZREV-All_Beauty-01723",
        "review:RV-AMZREV-All_Beauty-04813"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01767",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000X20Y4C",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 21,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01736",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01723",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04813",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0015",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02206",
        "product:PP-All_Beauty-B001281404",
        "review:AS-All_Beauty-B001281404-skin_scent",
        "review:RV-AMZREV-All_Beauty-02367",
        "review:RV-AMZREV-All_Beauty-01848"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02206",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B001281404",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B001281404-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02367",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01848",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0016",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00442",
        "product:PP-All_Beauty-B001ENX2NY"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00442",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B001ENX2NY",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0017",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04318",
        "product:PP-All_Beauty-B001V9V71U",
        "review:AS-All_Beauty-B001V9V71U-delivery",
        "review:RV-AMZREV-All_Beauty-00534",
        "review:RV-AMZREV-All_Beauty-02614"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04318",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B001V9V71U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B001V9V71U-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00534",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02614",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0018",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00032",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-04255",
        "review:RV-AMZREV-All_Beauty-02050"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0020MKBNW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04255",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02050",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    },
    {
      "query_id": "QS-0019",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04526",
        "product:PP-All_Beauty-B002E4VK40",
        "review:AS-All_Beauty-B002E4VK40-quality_damage",
        "review:RV-AMZREV-All_Beauty-00828",
        "review:RV-AMZREV-All_Beauty-04778"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04526",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B002E4VK40",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B002E4VK40-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00828",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04778",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ]
    }
  ],
  "support_rows": [
    {
      "query_id": "Q-001",
      "expected_intent": "support",
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
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
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
          "source": "kb",
          "doc_id": "KB001_return_refund_policy",
          "chunk_id": "ee79e051ef7a427c",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The return/refund path depends on the return window, item condition, and proof of purchase. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-001#d9c7c01c76812a84], [doc:kb:"
    },
    {
      "query_id": "Q-002",
      "expected_intent": "support",
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
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
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
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Warranty cases require product identification, proof of purchase, and a defect description. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-002#c2cbb38083f73a1b], [doc:kb:"
    },
    {
      "query_id": "Q-003",
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
          "doc_id": "R-010",
          "chunk_id": "f365b190b6deaf19",
          "rank": 2,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: NightView Baby Monitor (BABY-MONITOR-01) at $89.99, rating 4.4, stock 17; Anti-Colic Glass Bottle Set (BABY-BOTTLE-02) at $28.0, rating 4.6, stock 55. I used product/review evidence from [doc:product:P-BABY-001#b5c4f3e2"
    },
    {
      "query_id": "Q-004",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
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
          "source": "ticket",
          "doc_id": "T-005",
          "chunk_id": "1f1347dbaadd98b8",
          "rank": 2,
          "doc_type": "ticket"
        },
        {
          "source": "review",
          "doc_id": "R-012",
          "chunk_id": "00becedaf80dda0e",
          "rank": 3,
          "doc_type": "review"
        },
        {
          "source": "ticket",
          "doc_id": "T-006",
          "chunk_id": "04f23fbde0250d69",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review for nightview baby monitor. rating 2. delivery was late and the baby monitor battery drained overnight. i may return it if replacement is not available.. Suggested action: inspec"
    },
    {
      "query_id": "Q-005",
      "expected_intent": "sku_order",
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
      "citation_count": 2,
      "answer_citation_count": 2,
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
          "source": "kb",
          "doc_id": "KB004_shipping_delivery_policy",
          "chunk_id": "71d755fa30c11a8e",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "SKU SOFT-PDF-01 maps to PDF Studio Pro License. Current demo inventory is 100 units at $59.0. Supporting context: [doc:product:P-SOFT-001#379d92ed1d5b4648], [doc:kb:KB004_shipping_delivery_policy#71d755fa30c11a8e]."
    },
    {
      "query_id": "Q-006",
      "expected_intent": "support",
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
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 2,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 1,
          "doc_type": "ticket"
        },
        {
          "source": "kb",
          "doc_id": "KB003_payment_refund_policy",
          "chunk_id": "58aeba54f84fefb9",
          "rank": 2,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-004#d85e1613389da6aa], [doc:k"
    },
    {
      "query_id": "QS-0001",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-04225",
          "chunk_id": "4d17948b232c69e3",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000067E30",
          "chunk_id": "b8f7b95d48805643",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000067E30-price_value",
          "chunk_id": "26927288d77640fb",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00511",
          "chunk_id": "6deb2b622a912cc6",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0002",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-00821",
          "chunk_id": "54a15bec1ade2e16",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000068PBJ",
          "chunk_id": "a226b5cccd4d8a86",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000068PBJ-price_value",
          "chunk_id": "c66568825a2feb33",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-04062",
          "chunk_id": "ec1eeb515e93273e",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0003",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-00033",
          "chunk_id": "7378bda93b1704ce",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B00023J4AW",
          "chunk_id": "31e4e5356ad6761c",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-02567",
          "chunk_id": "18fbef7e60bfd2ba",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-02030",
          "chunk_id": "93991d6af799c931",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0004",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
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
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "QS-0005",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
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
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "QS-0006",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-01974",
          "chunk_id": "9b7b3db37e3b1c03",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000CSH3YG",
          "chunk_id": "e77c709a558ec0d0",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000CSH3YG-skin_scent",
          "chunk_id": "efe493af8ddf0685",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-02960",
          "chunk_id": "2f4fcadd5ff92929",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0007",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
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
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "QS-0008",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-02795",
          "chunk_id": "3669a32512744053",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000I1CFC2",
          "chunk_id": "57b552a0bc9623b5",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000I1CFC2-price_value",
          "chunk_id": "116dfbbd44e7564f",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03554",
          "chunk_id": "f97ad7ca015d7563",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0009",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
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
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "QS-0010",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-04380",
          "chunk_id": "d14eefa25d80a662",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000NHZSKC",
          "chunk_id": "c8c0f014a65acc81",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000NHZSKC-skin_scent",
          "chunk_id": "bca957f3f65e1592",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-04216",
          "chunk_id": "5f5e8bf41eb6a2d3",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0011",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-03825",
          "chunk_id": "7df8896e9b04cd36",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000NIZYIW",
          "chunk_id": "02901e70f2242830",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00647",
          "chunk_id": "f16ce30df47192d0",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03769",
          "chunk_id": "fc2c6602a35f0ec3",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0012",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-01189",
          "chunk_id": "8ce4c6c63b6bc239",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000OQFVLS",
          "chunk_id": "90668ccd7ce759e9",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000OQFVLS-quality_damage",
          "chunk_id": "ddbc8c7879563512",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03580",
          "chunk_id": "2cd14501283d55fb",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0013",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-02341",
          "chunk_id": "48c41a6559cad901",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000PKKAGO",
          "chunk_id": "cfb4dc32feda9ed8",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B000PKKAGO-battery_power",
          "chunk_id": "092644ffdbd14f2c",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03264",
          "chunk_id": "3f445c85d6a3d482",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0014",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-01767",
          "chunk_id": "33823a1291a92e9e",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B000X20Y4C",
          "chunk_id": "dbea9bbec6fca9a7",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-01736",
          "chunk_id": "39bd3f7b248b0d66",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-01723",
          "chunk_id": "11b52e6b70c5d6a3",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0015",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-02206",
          "chunk_id": "2425fe9de181ce9a",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B001281404",
          "chunk_id": "286ef1f34bba8dae",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B001281404-skin_scent",
          "chunk_id": "00a0dadece35e545",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-02367",
          "chunk_id": "9aaa845a92597dd9",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0016",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-00442",
          "chunk_id": "20205d3579dab348",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B001ENX2NY",
          "chunk_id": "7a3009a7f3632055",
          "rank": 2,
          "doc_type": "product_profile"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0017",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-04318",
          "chunk_id": "2edfbf08af94404a",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B001V9V71U",
          "chunk_id": "8ca0d1d7ca2d387e",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B001V9V71U-delivery",
          "chunk_id": "797c5449660a321c",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00534",
          "chunk_id": "c2466505be10c44c",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    },
    {
      "query_id": "QS-0018",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
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
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "QS-0019",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "medium",
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
          "doc_id": "RV-AMZREV-All_Beauty-04526",
          "chunk_id": "3baa528dba4523a4",
          "rank": 1,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-All_Beauty-B002E4VK40",
          "chunk_id": "5105454dafc35b18",
          "rank": 2,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "AS-All_Beauty-B002E4VK40-quality_damage",
          "chunk_id": "39bc4665a54f445e",
          "rank": 3,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00828",
          "chunk_id": "f020dc6f79f2e4f0",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty"
    }
  ]
}
```
