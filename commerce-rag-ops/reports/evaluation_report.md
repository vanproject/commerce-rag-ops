# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

## 摘要

- 样本数: 366
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 0.9989
- Recall@5: 0.936
- MRR: 1.0
- NDCG@5: 0.9971
- 引用率: 1.0
- 关键词覆盖率: 0.8934
- groundedness 代理指标: 1.0
- 延迟 p50/p95: 422 ms / 631 ms

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 187 | 0.9979 | 0.9127 | 1.0 | 0.9957 | 1.0 | 0.8734 |
| recommendation | 91 | 1.0 | 0.956 | 1.0 | 1.0 | 1.0 | 1.0 |
| sku_order | 1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| support | 87 | 1.0 | 0.9645 | 1.0 | 0.997 | 1.0 | 0.8238 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| easy | 90 | 0.9978 | 0.9107 | 1.0 | 0.9926 | 1.0 | 0.8296 |
| hard | 96 | 0.9979 | 0.9137 | 1.0 | 0.9986 | 1.0 | 0.9167 |
| medium | 174 | 1.0 | 0.9593 | 1.0 | 0.9985 | 1.0 | 0.9119 |
| unknown | 6 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.9444 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| aspect_match | 542 | 542 |
| bm25 | 1243 | 1241 |
| dense | 1182 | 1180 |
| entity_match | 1203 | 1201 |
| forced_fallback | 228 | 228 |
| policy_fallback | 187 | 187 |
| sibling_expansion | 435 | 435 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | aspect_match: 358, bm25: 687, dense: 653, entity_match: 650, forced_fallback: 43, sibling_expansion: 251 |
| recommendation | bm25: 336, dense: 312, entity_match: 341, forced_fallback: 6 |
| sku_order | bm25: 1, dense: 2, policy_fallback: 1 |
| support | aspect_match: 184, bm25: 217, dense: 213, entity_match: 210, forced_fallback: 179, policy_fallback: 186, sibling_expansion: 184 |

## Agentic 证据诊断

- 重试率: 0.0

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 366 |
| 尝试次数 | 1: 366 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_case_evidence | 36 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| support | missing_case_evidence: 36 |

## 原始 JSON

```json
{
  "n": 366,
  "retrieval_mode": "hybrid_rerank",
  "retrieval": {
    "precision@5": 0.9989,
    "recall@5": 0.936,
    "mrr": 1.0,
    "ndcg@5": 0.9971
  },
  "support_quality": {
    "citation_ok": 1.0,
    "keyword_coverage": 0.8934,
    "groundedness_proxy": 1.0
  },
  "latency": {
    "p50_ms": 422,
    "p95_ms": 631
  },
  "by_intent": {
    "customer_ops": {
      "n": 187,
      "retrieval": {
        "precision@5": 0.9979,
        "recall@5": 0.9127,
        "mrr": 1.0,
        "ndcg@5": 0.9957
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.8734,
        "groundedness_proxy": 1.0
      }
    },
    "recommendation": {
      "n": 91,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.956,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 1.0,
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
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    },
    "support": {
      "n": 87,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9645,
        "mrr": 1.0,
        "ndcg@5": 0.997
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.8238,
        "groundedness_proxy": 1.0
      }
    }
  },
  "by_difficulty": {
    "easy": {
      "n": 90,
      "retrieval": {
        "precision@5": 0.9978,
        "recall@5": 0.9107,
        "mrr": 1.0,
        "ndcg@5": 0.9926
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.8296,
        "groundedness_proxy": 1.0
      }
    },
    "hard": {
      "n": 96,
      "retrieval": {
        "precision@5": 0.9979,
        "recall@5": 0.9137,
        "mrr": 1.0,
        "ndcg@5": 0.9986
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.9167,
        "groundedness_proxy": 1.0
      }
    },
    "medium": {
      "n": 174,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9593,
        "mrr": 1.0,
        "ndcg@5": 0.9985
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.9119,
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
        "keyword_coverage": 0.9444,
        "groundedness_proxy": 1.0
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "aspect_match": 542,
      "bm25": 1243,
      "dense": 1182,
      "entity_match": 1203,
      "forced_fallback": 228,
      "policy_fallback": 187,
      "sibling_expansion": 435
    },
    "relevant_hit_signal_counts": {
      "aspect_match": 542,
      "bm25": 1241,
      "dense": 1180,
      "entity_match": 1201,
      "forced_fallback": 228,
      "policy_fallback": 187,
      "sibling_expansion": 435
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "aspect_match": 358,
        "bm25": 687,
        "dense": 653,
        "entity_match": 650,
        "forced_fallback": 43,
        "sibling_expansion": 251
      },
      "recommendation": {
        "bm25": 336,
        "dense": 312,
        "entity_match": 341,
        "forced_fallback": 6
      },
      "sku_order": {
        "bm25": 1,
        "dense": 2,
        "policy_fallback": 1
      },
      "support": {
        "aspect_match": 184,
        "bm25": 217,
        "dense": 213,
        "entity_match": 210,
        "forced_fallback": 179,
        "policy_fallback": 186,
        "sibling_expansion": 184
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 366
    },
    "attempt_counts": {
      "1": 366
    },
    "retry_rate": 0.0,
    "evidence_gap_counts": {
      "missing_case_evidence": 36
    },
    "evidence_gaps_by_intent": {
      "support": {
        "missing_case_evidence": 36
      }
    }
  },
  "retrieval_rows": [
    {
      "query_id": "Q-001",
      "intent": "support",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-002",
      "intent": "support",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-003",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-004",
      "intent": "customer_ops",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-005",
      "intent": "sku_order",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-006",
      "intent": "support",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0001",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0002",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0003",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0004",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0005",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0006",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0007",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0008",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0009",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0010",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0011",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0012",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0013",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0014",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0015",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0016",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0017",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0018",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0019",
      "intent": "recommendation",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0020",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00631",
        "product:PP-All_Beauty-B002MYXUO0"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00631",
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
          "doc_id": "product:PP-All_Beauty-B002MYXUO0",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0021",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00593",
        "product:PP-All_Beauty-B003DLQNI6"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00593",
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
          "doc_id": "product:PP-All_Beauty-B003DLQNI6",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0022",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02150",
        "product:PP-All_Beauty-B003NTFDFM",
        "review:AS-All_Beauty-B003NTFDFM-price_value",
        "review:RV-AMZREV-All_Beauty-01643",
        "review:RV-AMZREV-All_Beauty-01633"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02150",
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
          "doc_id": "product:PP-All_Beauty-B003NTFDFM",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B003NTFDFM-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01643",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01633",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0023",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00114",
        "product:PP-All_Beauty-B003USID1C",
        "review:RV-AMZREV-All_Beauty-04236"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00114",
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
          "doc_id": "product:PP-All_Beauty-B003USID1C",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04236",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0024",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01710",
        "product:PP-All_Beauty-B0046BPTI2",
        "review:AS-All_Beauty-B0046BPTI2-price_value",
        "review:RV-AMZREV-All_Beauty-01034",
        "review:RV-AMZREV-All_Beauty-00744"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01710",
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
          "doc_id": "product:PP-All_Beauty-B0046BPTI2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0046BPTI2-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01034",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00744",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0025",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00887",
        "product:PP-All_Beauty-B0047V7MAY"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00887",
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
          "doc_id": "product:PP-All_Beauty-B0047V7MAY",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0026",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03428",
        "product:PP-All_Beauty-B00487JRXC",
        "review:RV-AMZREV-All_Beauty-01093"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03428",
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
          "doc_id": "product:PP-All_Beauty-B00487JRXC",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01093",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0027",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00476",
        "product:PP-All_Beauty-B004FK48DG",
        "review:AS-All_Beauty-B004FK48DG-skin_scent",
        "review:RV-AMZREV-All_Beauty-01627"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00476",
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
          "doc_id": "product:PP-All_Beauty-B004FK48DG",
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
          "doc_id": "review:AS-All_Beauty-B004FK48DG-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01627",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0028",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00459",
        "product:PP-All_Beauty-B004X8JLN2",
        "review:RV-AMZREV-All_Beauty-03367"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00459",
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
          "doc_id": "product:PP-All_Beauty-B004X8JLN2",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03367",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0029",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01120",
        "product:PP-All_Beauty-B005AL5H9S",
        "review:AS-All_Beauty-B005AL5H9S-battery_power",
        "review:RV-AMZREV-All_Beauty-01381",
        "review:RV-AMZREV-All_Beauty-01474"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01120",
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
          "doc_id": "product:PP-All_Beauty-B005AL5H9S",
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
          "doc_id": "review:AS-All_Beauty-B005AL5H9S-battery_power",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01381",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01474",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0030",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00512",
        "product:PP-All_Beauty-B005FLNLM8"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00512",
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
          "doc_id": "product:PP-All_Beauty-B005FLNLM8",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0031",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03658",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-03808",
        "review:RV-AMZREV-All_Beauty-01947",
        "review:RV-AMZREV-All_Beauty-03277"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03658",
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
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": null,
          "signals": [
            "dense",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03808",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01947",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03277",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0032",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00632",
        "product:PP-All_Beauty-B005LFNUF6"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00632",
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
          "doc_id": "product:PP-All_Beauty-B005LFNUF6",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0033",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01814",
        "product:PP-All_Beauty-B005XSZS92",
        "review:RV-AMZREV-All_Beauty-03101",
        "review:RV-AMZREV-All_Beauty-03412",
        "review:RV-AMZREV-All_Beauty-00591"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01814",
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
          "doc_id": "product:PP-All_Beauty-B005XSZS92",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03101",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03412",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00591",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0034",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01117",
        "product:PP-All_Beauty-B00695VZHM"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01117",
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
          "doc_id": "product:PP-All_Beauty-B00695VZHM",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0035",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00385",
        "product:PP-All_Beauty-B007MB4YW0",
        "review:RV-AMZREV-All_Beauty-02772"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00385",
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
          "doc_id": "product:PP-All_Beauty-B007MB4YW0",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02772",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0036",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02761",
        "product:PP-All_Beauty-B007VXJK6E",
        "review:AS-All_Beauty-B007VXJK6E-battery_power",
        "review:RV-AMZREV-All_Beauty-02044",
        "review:RV-AMZREV-All_Beauty-03845"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02761",
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
          "doc_id": "product:PP-All_Beauty-B007VXJK6E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B007VXJK6E-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02044",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03845",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0037",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02102",
        "product:PP-All_Beauty-B008TGMJQA",
        "review:AS-All_Beauty-B008TGMJQA-price_value",
        "review:RV-AMZREV-All_Beauty-03773",
        "review:RV-AMZREV-All_Beauty-04624"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02102",
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
          "doc_id": "product:PP-All_Beauty-B008TGMJQA",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B008TGMJQA-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03773",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04624",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0038",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01994",
        "product:PP-All_Beauty-B008TGSAFE",
        "review:AS-All_Beauty-B008TGSAFE-price_value",
        "review:RV-AMZREV-All_Beauty-01795",
        "review:RV-AMZREV-All_Beauty-03824"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01994",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B008TGSAFE",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B008TGSAFE-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01795",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03824",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0039",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00889",
        "product:PP-All_Beauty-B00915QNQU"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00889",
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
          "doc_id": "product:PP-All_Beauty-B00915QNQU",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0040",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02727",
        "product:PP-All_Beauty-B0093EQX6Y",
        "review:AS-All_Beauty-B0093EQX6Y-skin_scent",
        "review:RV-AMZREV-All_Beauty-04381",
        "review:RV-AMZREV-All_Beauty-00109"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02727",
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
          "doc_id": "product:PP-All_Beauty-B0093EQX6Y",
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
          "doc_id": "review:AS-All_Beauty-B0093EQX6Y-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04381",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00109",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0041",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04653",
        "product:PP-All_Beauty-B00946HGLW",
        "review:AS-All_Beauty-B00946HGLW-skin_scent",
        "review:RV-AMZREV-All_Beauty-04408",
        "review:RV-AMZREV-All_Beauty-01766"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04653",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00946HGLW",
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
          "doc_id": "review:AS-All_Beauty-B00946HGLW-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04408",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01766",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0042",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00400",
        "product:PP-All_Beauty-B009SNONTO"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00400",
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
          "doc_id": "product:PP-All_Beauty-B009SNONTO",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0043",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00717",
        "product:PP-All_Beauty-B009WFVG66"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00717",
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
          "doc_id": "product:PP-All_Beauty-B009WFVG66",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0044",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04894",
        "product:PP-All_Beauty-B00A0RUGPM",
        "review:AS-All_Beauty-B00A0RUGPM-skin_scent",
        "review:RV-AMZREV-All_Beauty-03307",
        "review:RV-AMZREV-All_Beauty-02417"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04894",
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
          "doc_id": "product:PP-All_Beauty-B00A0RUGPM",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00A0RUGPM-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 27,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03307",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02417",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0045",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00472",
        "product:PP-All_Beauty-B00ALUWUBQ"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00472",
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
          "doc_id": "product:PP-All_Beauty-B00ALUWUBQ",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0046",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03022",
        "product:PP-All_Beauty-B00AXXHCLY",
        "review:AS-All_Beauty-B00AXXHCLY-skin_scent",
        "review:RV-AMZREV-All_Beauty-00888",
        "review:RV-AMZREV-All_Beauty-03961"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03022",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00AXXHCLY",
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
          "doc_id": "review:AS-All_Beauty-B00AXXHCLY-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00888",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03961",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0047",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00836",
        "product:PP-All_Beauty-B00B0UGRKG"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00836",
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
          "doc_id": "product:PP-All_Beauty-B00B0UGRKG",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0048",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00636",
        "product:PP-All_Beauty-B00B5WMP8M"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00636",
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
          "doc_id": "product:PP-All_Beauty-B00B5WMP8M",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0049",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03189",
        "product:PP-All_Beauty-B00BGB3C8O",
        "review:RV-AMZREV-All_Beauty-03607",
        "review:RV-AMZREV-All_Beauty-00897",
        "review:RV-AMZREV-All_Beauty-03644"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03189",
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
          "doc_id": "product:PP-All_Beauty-B00BGB3C8O",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03607",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00897",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03644",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0050",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00336",
        "product:PP-All_Beauty-B00BNARG9O"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00336",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00BNARG9O",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0051",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00646",
        "product:PP-All_Beauty-B00BS473N4"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00646",
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
          "doc_id": "product:PP-All_Beauty-B00BS473N4",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0052",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02136",
        "product:PP-All_Beauty-B00C0YZBJE",
        "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
        "review:RV-AMZREV-All_Beauty-04851",
        "review:RV-AMZREV-All_Beauty-00056"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02136",
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
          "doc_id": "product:PP-All_Beauty-B00C0YZBJE",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04851",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00056",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0053",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00917",
        "product:PP-All_Beauty-B00CLXXXH6",
        "review:RV-AMZREV-All_Beauty-04554",
        "review:RV-AMZREV-All_Beauty-03899",
        "review:RV-AMZREV-All_Beauty-04671"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00917",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00CLXXXH6",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04554",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03899",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04671",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0054",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00612",
        "product:PP-All_Beauty-B00CXK679S"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00612",
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
          "doc_id": "product:PP-All_Beauty-B00CXK679S",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0055",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03919",
        "product:PP-All_Beauty-B00DR75MOM",
        "review:AS-All_Beauty-B00DR75MOM-skin_scent",
        "review:RV-AMZREV-All_Beauty-00403"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03919",
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
          "doc_id": "product:PP-All_Beauty-B00DR75MOM",
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
          "doc_id": "review:AS-All_Beauty-B00DR75MOM-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00403",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0056",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00521",
        "product:PP-All_Beauty-B00E2S00ME"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00521",
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
          "doc_id": "product:PP-All_Beauty-B00E2S00ME",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0057",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00648",
        "product:PP-All_Beauty-B00E2SF6Q4",
        "review:RV-AMZREV-All_Beauty-04591"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00648",
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
          "doc_id": "product:PP-All_Beauty-B00E2SF6Q4",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04591",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0058",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00113",
        "product:PP-All_Beauty-B00EIL38WO"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00113",
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
          "doc_id": "product:PP-All_Beauty-B00EIL38WO",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0059",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03776",
        "product:PP-All_Beauty-B00EWUFETQ",
        "review:AS-All_Beauty-B00EWUFETQ-missing_parts",
        "review:RV-AMZREV-All_Beauty-02660",
        "review:RV-AMZREV-All_Beauty-00550"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03776",
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
          "doc_id": "product:PP-All_Beauty-B00EWUFETQ",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00EWUFETQ-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02660",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00550",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0060",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00254",
        "product:PP-All_Beauty-B00F22YKOS"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00254",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00F22YKOS",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0061",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00587",
        "product:PP-All_Beauty-B00FEHM8HM"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00587",
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
          "doc_id": "product:PP-All_Beauty-B00FEHM8HM",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0062",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01392",
        "product:PP-All_Beauty-B00FQD0LNW",
        "review:AS-All_Beauty-B00FQD0LNW-missing_parts",
        "review:RV-AMZREV-All_Beauty-03741",
        "review:RV-AMZREV-All_Beauty-03123"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01392",
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
          "doc_id": "product:PP-All_Beauty-B00FQD0LNW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00FQD0LNW-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03741",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03123",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0063",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03671",
        "product:PP-All_Beauty-B00G7PCKI2",
        "review:AS-All_Beauty-B00G7PCKI2-skin_scent",
        "review:RV-AMZREV-All_Beauty-02347",
        "review:RV-AMZREV-All_Beauty-00269"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03671",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00G7PCKI2",
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
          "doc_id": "review:AS-All_Beauty-B00G7PCKI2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02347",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00269",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0064",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03302",
        "product:PP-All_Beauty-B00G7UFXJA",
        "review:AS-All_Beauty-B00G7UFXJA-skin_scent",
        "review:RV-AMZREV-All_Beauty-00116",
        "review:RV-AMZREV-All_Beauty-04823"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03302",
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
          "doc_id": "product:PP-All_Beauty-B00G7UFXJA",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00G7UFXJA-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00116",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04823",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0065",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00094",
        "product:PP-All_Beauty-B00GUTPV4A"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00094",
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
          "doc_id": "product:PP-All_Beauty-B00GUTPV4A",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0066",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00520",
        "product:PP-All_Beauty-B00H78IR6W",
        "review:RV-AMZREV-All_Beauty-02237",
        "review:RV-AMZREV-All_Beauty-02452"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00520",
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
          "doc_id": "product:PP-All_Beauty-B00H78IR6W",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02237",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02452",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0067",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00388",
        "product:PP-All_Beauty-B00HA72I8S",
        "review:RV-AMZREV-All_Beauty-04379",
        "review:RV-AMZREV-All_Beauty-04348"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00388",
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
          "doc_id": "product:PP-All_Beauty-B00HA72I8S",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04379",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04348",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0068",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00637",
        "product:PP-All_Beauty-B00I58M2Q4"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00637",
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
          "doc_id": "product:PP-All_Beauty-B00I58M2Q4",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0069",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02027",
        "product:PP-All_Beauty-B00IUI0QFS",
        "review:RV-AMZREV-All_Beauty-00643",
        "review:RV-AMZREV-All_Beauty-03085"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02027",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00IUI0QFS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00643",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03085",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0070",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00165",
        "product:PP-All_Beauty-B00J2R8BP8",
        "review:AS-All_Beauty-B00J2R8BP8-price_value",
        "review:RV-AMZREV-All_Beauty-03805",
        "review:RV-AMZREV-All_Beauty-04090"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00165",
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
          "doc_id": "product:PP-All_Beauty-B00J2R8BP8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00J2R8BP8-price_value",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03805",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0071",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00604",
        "product:PP-All_Beauty-B00J4YYA86"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00604",
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
          "doc_id": "product:PP-All_Beauty-B00J4YYA86",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0072",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04946",
        "product:PP-All_Beauty-B00J7QCNDU",
        "review:AS-All_Beauty-B00J7QCNDU-delivery",
        "review:RV-AMZREV-All_Beauty-01796",
        "review:RV-AMZREV-All_Beauty-04362"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04946",
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
          "doc_id": "product:PP-All_Beauty-B00J7QCNDU",
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
          "doc_id": "review:AS-All_Beauty-B00J7QCNDU-delivery",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01796",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04362",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0073",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00110",
        "product:PP-All_Beauty-B00JM1BZUW"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00110",
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
          "doc_id": "product:PP-All_Beauty-B00JM1BZUW",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0074",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02637",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
        "review:RV-AMZREV-All_Beauty-03393",
        "review:RV-AMZREV-All_Beauty-00020"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
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
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00020",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0075",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00791",
        "product:PP-All_Beauty-B00K9E0SG8",
        "review:AS-All_Beauty-B00K9E0SG8-skin_scent",
        "review:RV-AMZREV-All_Beauty-04802",
        "review:RV-AMZREV-All_Beauty-03306"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00791",
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
          "doc_id": "product:PP-All_Beauty-B00K9E0SG8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00K9E0SG8-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04802",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03306",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0076",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03120",
        "product:PP-All_Beauty-B00KCTER3U",
        "review:AS-All_Beauty-B00KCTER3U-quality_damage",
        "review:RV-AMZREV-All_Beauty-01683",
        "review:RV-AMZREV-All_Beauty-04602"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03120",
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
          "doc_id": "product:PP-All_Beauty-B00KCTER3U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 28,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00KCTER3U-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01683",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04602",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0077",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02411",
        "product:PP-All_Beauty-B00KH8F5GO",
        "review:RV-AMZREV-All_Beauty-01071"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02411",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00KH8F5GO",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01071",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0078",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02603",
        "product:PP-All_Beauty-B00KNIECVC",
        "review:AS-All_Beauty-B00KNIECVC-skin_scent",
        "review:RV-AMZREV-All_Beauty-04235",
        "review:RV-AMZREV-All_Beauty-00106"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02603",
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
          "doc_id": "product:PP-All_Beauty-B00KNIECVC",
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
          "doc_id": "review:AS-All_Beauty-B00KNIECVC-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04235",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00106",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0079",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00456",
        "product:PP-All_Beauty-B00KOCJEJC"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00456",
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
          "doc_id": "product:PP-All_Beauty-B00KOCJEJC",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0080",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04024",
        "product:PP-All_Beauty-B00KR4AFJU",
        "review:AS-All_Beauty-B00KR4AFJU-skin_scent",
        "review:RV-AMZREV-All_Beauty-00096",
        "review:RV-AMZREV-All_Beauty-02060"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04024",
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
          "doc_id": "product:PP-All_Beauty-B00KR4AFJU",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00KR4AFJU-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00096",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02060",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0081",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00098",
        "product:PP-All_Beauty-B00KXFD75M",
        "review:AS-All_Beauty-B00KXFD75M-skin_scent",
        "review:RV-AMZREV-All_Beauty-04990",
        "review:RV-AMZREV-All_Beauty-03571"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00098",
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
          "doc_id": "product:PP-All_Beauty-B00KXFD75M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00KXFD75M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04990",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03571",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0082",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04809",
        "product:PP-All_Beauty-B00L5HZCPU",
        "review:AS-All_Beauty-B00L5HZCPU-skin_scent",
        "review:RV-AMZREV-All_Beauty-02722",
        "review:RV-AMZREV-All_Beauty-00449"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04809",
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
          "doc_id": "product:PP-All_Beauty-B00L5HZCPU",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00L5HZCPU-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02722",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00449",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0083",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00779",
        "product:PP-All_Beauty-B00LHZC4GA",
        "review:AS-All_Beauty-B00LHZC4GA-skin_scent",
        "review:RV-AMZREV-All_Beauty-03332",
        "review:RV-AMZREV-All_Beauty-02176"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00779",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00LHZC4GA",
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
          "doc_id": "review:AS-All_Beauty-B00LHZC4GA-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03332",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02176",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0084",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00461",
        "product:PP-All_Beauty-B00LIAZ8OO"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00461",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00LIAZ8OO",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0085",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00100",
        "product:PP-All_Beauty-B00MDKICPK"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00100",
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
          "doc_id": "product:PP-All_Beauty-B00MDKICPK",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0086",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04356",
        "product:PP-All_Beauty-B00MNAE3KS",
        "review:AS-All_Beauty-B00MNAE3KS-skin_scent",
        "review:RV-AMZREV-All_Beauty-04829",
        "review:RV-AMZREV-All_Beauty-00899"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04356",
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
          "doc_id": "product:PP-All_Beauty-B00MNAE3KS",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00MNAE3KS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04829",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00899",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0087",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03361",
        "product:PP-All_Beauty-B00N6WHTRG",
        "review:AS-All_Beauty-B00N6WHTRG-skin_scent",
        "review:RV-AMZREV-All_Beauty-01393",
        "review:RV-AMZREV-All_Beauty-03848"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03361",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00N6WHTRG",
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
          "doc_id": "review:AS-All_Beauty-B00N6WHTRG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01393",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03848",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0088",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00101",
        "product:PP-All_Beauty-B00NNKWDI6"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00101",
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
          "doc_id": "product:PP-All_Beauty-B00NNKWDI6",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0089",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01000",
        "product:PP-All_Beauty-B00O2FGBJS",
        "review:AS-All_Beauty-B00O2FGBJS-skin_scent",
        "review:RV-AMZREV-All_Beauty-01700",
        "review:RV-AMZREV-All_Beauty-03426"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01000",
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
          "doc_id": "product:PP-All_Beauty-B00O2FGBJS",
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
          "doc_id": "review:AS-All_Beauty-B00O2FGBJS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01700",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03426",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0090",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00278",
        "product:PP-All_Beauty-B00OP8NZV4"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00278",
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
          "doc_id": "product:PP-All_Beauty-B00OP8NZV4",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0091",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02868",
        "review:RV-AMZREV-All_Beauty-02870",
        "review:RV-AMZREV-All_Beauty-02913",
        "review:RV-AMZREV-All_Beauty-02935",
        "review:RV-AMZREV-All_Beauty-02938"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02868",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02870",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02913",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02935",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02938",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0092",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02779",
        "product:PP-All_Beauty-B081TJ8YS3",
        "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
        "review:RV-AMZREV-All_Beauty-00002"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02779",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B081TJ8YS3",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00002",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0093",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00003",
        "product:PP-All_Beauty-B00R8DXL44"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00003",
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
          "doc_id": "product:PP-All_Beauty-B00R8DXL44",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0094",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00004",
        "product:PP-All_Beauty-B099DRHW5V"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00004",
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
          "doc_id": "product:PP-All_Beauty-B099DRHW5V",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0095",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00005",
        "product:PP-All_Beauty-B08BBQ29N5"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08BBQ29N5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0096",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00006",
        "product:PP-All_Beauty-B08P2DZB4X",
        "review:AS-All_Beauty-B08P2DZB4X-battery_power",
        "review:RV-AMZREV-All_Beauty-02738",
        "review:RV-AMZREV-All_Beauty-01196"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08P2DZB4X",
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
          "doc_id": "review:AS-All_Beauty-B08P2DZB4X-battery_power",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02738",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01196",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0097",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00007",
        "product:PP-All_Beauty-B086QY6T7N"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00007",
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
          "doc_id": "product:PP-All_Beauty-B086QY6T7N",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0098",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00008",
        "product:PP-All_Beauty-B08DHTJ25J"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00008",
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
          "doc_id": "product:PP-All_Beauty-B08DHTJ25J",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0099",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01199",
        "product:PP-All_Beauty-B07RBSLNFR",
        "review:AS-All_Beauty-B07RBSLNFR-price_value",
        "review:RV-AMZREV-All_Beauty-00009",
        "review:RV-AMZREV-All_Beauty-00662"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01199",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07RBSLNFR",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07RBSLNFR-price_value",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00009",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00662",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0100",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00010",
        "product:PP-All_Beauty-B07SLFWZKN",
        "review:AS-All_Beauty-B07SLFWZKN-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00010",
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
          "doc_id": "product:PP-All_Beauty-B07SLFWZKN",
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
          "doc_id": "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0101",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00012",
        "product:PP-All_Beauty-B08GLG6W8T",
        "review:AS-All_Beauty-B08GLG6W8T-skin_scent",
        "review:RV-AMZREV-All_Beauty-01589",
        "review:RV-AMZREV-All_Beauty-01207"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00012",
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
          "doc_id": "product:PP-All_Beauty-B08GLG6W8T",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08GLG6W8T-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01589",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01207",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0102",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00013",
        "product:PP-All_Beauty-B08M3C6LVS",
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00013",
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
          "doc_id": "product:PP-All_Beauty-B08M3C6LVS",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0103",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00014",
        "product:PP-All_Beauty-B07GHPCT6T"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00014",
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
          "doc_id": "product:PP-All_Beauty-B07GHPCT6T",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0104",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00015",
        "review:RV-AMZREV-All_Beauty-02483",
        "review:RV-AMZREV-All_Beauty-03222",
        "review:RV-AMZREV-All_Beauty-01497",
        "review:RV-AMZREV-All_Beauty-00284"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00015",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02483",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03222",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01497",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00284",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0105",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01229",
        "product:PP-All_Beauty-B07W397QG4",
        "review:AS-All_Beauty-B07W397QG4-skin_scent",
        "review:RV-AMZREV-All_Beauty-00016"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01229",
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
          "doc_id": "product:PP-All_Beauty-B07W397QG4",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07W397QG4-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00016",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0106",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02588",
        "review:RV-AMZREV-All_Beauty-02765",
        "review:RV-AMZREV-All_Beauty-00922",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02748"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02588",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00922",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02748",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0107",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00018",
        "product:PP-All_Beauty-B07J3GH1W1",
        "review:RV-AMZREV-All_Beauty-01157"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00018",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07J3GH1W1",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01157",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0108",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00159",
        "review:RV-AMZREV-All_Beauty-02100",
        "review:RV-AMZREV-All_Beauty-02446",
        "review:RV-AMZREV-All_Beauty-00019",
        "review:RV-AMZREV-All_Beauty-03685"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00159",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02100",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02446",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00019",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03685",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0109",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.830419897363192,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03393",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
        "review:AS-All_Beauty-B00JMDPK8S-battery_power",
        "review:AS-All_Beauty-B00JMDPK8S-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
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
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-battery_power",
          "doc_type": "review_aspect_summary",
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
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0110",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02766",
        "review:RV-AMZREV-All_Beauty-01617",
        "review:RV-AMZREV-All_Beauty-02615",
        "review:RV-AMZREV-All_Beauty-03860",
        "review:RV-AMZREV-All_Beauty-02413"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02766",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01617",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02615",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03860",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02413",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0111",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00022",
        "product:PP-All_Beauty-B082QX2HP6",
        "review:AS-All_Beauty-B082QX2HP6-skin_scent",
        "review:RV-AMZREV-All_Beauty-01737",
        "review:RV-AMZREV-All_Beauty-03894"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00022",
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
          "doc_id": "product:PP-All_Beauty-B082QX2HP6",
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
          "doc_id": "review:AS-All_Beauty-B082QX2HP6-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01737",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03894",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0112",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00023",
        "product:PP-All_Beauty-B077SRDVG9"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00023",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B077SRDVG9",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0113",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00024",
        "product:PP-All_Beauty-B01AKTGHFW"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00024",
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
          "doc_id": "product:PP-All_Beauty-B01AKTGHFW",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0114",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00025",
        "product:PP-All_Beauty-B079SMVSYW"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00025",
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
          "doc_id": "product:PP-All_Beauty-B079SMVSYW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0115",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00026",
        "product:PP-All_Beauty-B07K8VTT6M"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00026",
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
          "doc_id": "product:PP-All_Beauty-B07K8VTT6M",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0116",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00027",
        "product:PP-All_Beauty-B083BDVS36",
        "review:AS-All_Beauty-B083BDVS36-delivery",
        "review:AS-All_Beauty-B083BDVS36-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00027",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B083BDVS36-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B083BDVS36-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0117",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04471",
        "review:RV-AMZREV-All_Beauty-01726",
        "review:RV-AMZREV-All_Beauty-04681",
        "review:RV-AMZREV-All_Beauty-03842",
        "review:RV-AMZREV-All_Beauty-02405"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04471",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01726",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04681",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03842",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02405",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0118",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00029",
        "product:PP-All_Beauty-B0BFR5WF1R"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00029",
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
          "doc_id": "product:PP-All_Beauty-B0BFR5WF1R",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0119",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04653",
        "review:RV-AMZREV-All_Beauty-01766",
        "review:RV-AMZREV-All_Beauty-03730",
        "review:RV-AMZREV-All_Beauty-03339",
        "review:RV-AMZREV-All_Beauty-00030"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04653",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01766",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03730",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03339",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00030",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0120",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00031",
        "product:PP-All_Beauty-B082FLP15V"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00031",
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
          "doc_id": "product:PP-All_Beauty-B082FLP15V",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0121",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00032",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-04255",
        "review:RV-AMZREV-All_Beauty-04266"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
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
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 7,
          "signals": [
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04266",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0122",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02567",
        "product:PP-All_Beauty-B00023J4AW",
        "review:RV-AMZREV-All_Beauty-00033"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02567",
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
          "doc_id": "product:PP-All_Beauty-B00023J4AW",
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0123",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03658",
        "review:RV-AMZREV-All_Beauty-02944",
        "review:RV-AMZREV-All_Beauty-04357",
        "review:RV-AMZREV-All_Beauty-03661",
        "review:RV-AMZREV-All_Beauty-00034"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03658",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02944",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04357",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": null,
          "signals": [
            "dense",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03661",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00034",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0124",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00035",
        "product:PP-All_Beauty-B01M5KNSQN"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00035",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B01M5KNSQN",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0125",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00036",
        "product:PP-All_Beauty-B07KDNK11M"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00036",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0126",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00037",
        "product:PP-All_Beauty-B08DLGCYK8"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00037",
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
          "doc_id": "product:PP-All_Beauty-B08DLGCYK8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0127",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00038",
        "product:PP-All_Beauty-B081GCFHPG"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00038",
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
          "doc_id": "product:PP-All_Beauty-B081GCFHPG",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0128",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04430",
        "review:RV-AMZREV-All_Beauty-02333",
        "review:RV-AMZREV-All_Beauty-00039",
        "review:RV-AMZREV-All_Beauty-04150",
        "review:RV-AMZREV-All_Beauty-04025"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04430",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02333",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00039",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04150",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04025",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0129",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00040",
        "product:PP-All_Beauty-B08C9LZQN4"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00040",
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
          "doc_id": "product:PP-All_Beauty-B08C9LZQN4",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0130",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01819",
        "review:RV-AMZREV-All_Beauty-03710",
        "review:RV-AMZREV-All_Beauty-03968",
        "review:RV-AMZREV-All_Beauty-02080",
        "review:RV-AMZREV-All_Beauty-00041"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01819",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03710",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03968",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02080",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00041",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0131",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02657",
        "product:PP-All_Beauty-B09FF97RHL",
        "review:RV-AMZREV-All_Beauty-00042"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02657",
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
          "doc_id": "product:PP-All_Beauty-B09FF97RHL",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00042",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0132",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00043",
        "product:PP-All_Beauty-B07XYXSYCD"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00043",
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
          "doc_id": "product:PP-All_Beauty-B07XYXSYCD",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0133",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00044",
        "product:PP-All_Beauty-B07NSR3CKR"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00044",
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
          "doc_id": "product:PP-All_Beauty-B07NSR3CKR",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0134",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03694",
        "review:RV-AMZREV-All_Beauty-03425",
        "review:RV-AMZREV-All_Beauty-04204",
        "review:RV-AMZREV-All_Beauty-02771",
        "review:RV-AMZREV-All_Beauty-01693"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03694",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03425",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04204",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02771",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01693",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0135",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00046",
        "product:PP-All_Beauty-B018F28B1Y"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00046",
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
          "doc_id": "product:PP-All_Beauty-B018F28B1Y",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0136",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00047",
        "product:PP-All_Beauty-B095SC4J8T"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00047",
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
          "doc_id": "product:PP-All_Beauty-B095SC4J8T",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0137",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00048",
        "product:PP-All_Beauty-B09CQ4PXLN"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00048",
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
          "doc_id": "product:PP-All_Beauty-B09CQ4PXLN",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0138",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00049",
        "product:PP-All_Beauty-B08DXDLR3P"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00049",
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
          "doc_id": "product:PP-All_Beauty-B08DXDLR3P",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0139",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01428",
        "product:PP-All_Beauty-B0875V791H",
        "review:AS-All_Beauty-B0875V791H-skin_scent",
        "review:RV-AMZREV-All_Beauty-04988",
        "review:RV-AMZREV-All_Beauty-00050"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01428",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B0875V791H",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0875V791H-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04988",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00050",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0140",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00051",
        "product:PP-All_Beauty-B07LBK2YQX",
        "review:AS-All_Beauty-B07LBK2YQX-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00051",
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
          "doc_id": "product:PP-All_Beauty-B07LBK2YQX",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07LBK2YQX-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0141",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01301",
        "product:PP-All_Beauty-B07FX94GYX",
        "review:RV-AMZREV-All_Beauty-00052",
        "review:RV-AMZREV-All_Beauty-03318"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01301",
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
          "doc_id": "product:PP-All_Beauty-B07FX94GYX",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00052",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03318",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0142",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00053",
        "product:PP-All_Beauty-B08CXFDDV8"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00053",
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
          "doc_id": "product:PP-All_Beauty-B08CXFDDV8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0143",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00054",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-02401",
        "review:RV-AMZREV-All_Beauty-01948"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00054",
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
          "doc_id": "product:PP-All_Beauty-B015RR870U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02401",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01948",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0144",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00055",
        "product:PP-All_Beauty-B000OQFVLS",
        "review:AS-All_Beauty-B000OQFVLS-quality_damage"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
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
          "bm25_rank": 2,
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
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0145",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02136",
        "product:PP-All_Beauty-B00C0YZBJE",
        "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
        "review:RV-AMZREV-All_Beauty-00056",
        "review:RV-AMZREV-All_Beauty-04676"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02136",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00C0YZBJE",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00056",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04676",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0146",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00057",
        "product:PP-All_Beauty-B0B8DZ7H5F",
        "review:AS-All_Beauty-B0B8DZ7H5F-skin_scent",
        "review:RV-AMZREV-All_Beauty-02669",
        "review:RV-AMZREV-All_Beauty-01565"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00057",
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
          "doc_id": "product:PP-All_Beauty-B0B8DZ7H5F",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0B8DZ7H5F-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02669",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01565",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0147",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00058",
        "product:PP-All_Beauty-B0B4JP5YD9",
        "review:AS-All_Beauty-B0B4JP5YD9-skin_scent",
        "review:RV-AMZREV-All_Beauty-00410"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00058",
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
          "doc_id": "product:PP-All_Beauty-B0B4JP5YD9",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0B4JP5YD9-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00410",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0148",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01549",
        "product:PP-All_Beauty-B0B4JPGX8P",
        "review:AS-All_Beauty-B0B4JPGX8P-skin_scent",
        "review:RV-AMZREV-All_Beauty-00059"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01549",
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
          "doc_id": "product:PP-All_Beauty-B0B4JPGX8P",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0B4JPGX8P-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00059",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0149",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00060",
        "product:PP-All_Beauty-B09KT4RJG6",
        "review:AS-All_Beauty-B09KT4RJG6-skin_scent",
        "review:RV-AMZREV-All_Beauty-01148"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00060",
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
          "doc_id": "product:PP-All_Beauty-B09KT4RJG6",
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
          "doc_id": "review:AS-All_Beauty-B09KT4RJG6-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01148",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0150",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00061",
        "product:PP-All_Beauty-B07KQ32Z8C",
        "review:AS-All_Beauty-B07KQ32Z8C-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00061",
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
          "doc_id": "product:PP-All_Beauty-B07KQ32Z8C",
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
          "doc_id": "review:AS-All_Beauty-B07KQ32Z8C-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0151",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00062",
        "product:PP-All_Beauty-B08PQ6YXSH",
        "review:AS-All_Beauty-B08PQ6YXSH-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00062",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08PQ6YXSH",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08PQ6YXSH-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0152",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00063",
        "product:PP-All_Beauty-B07W6H8CGT"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00063",
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
          "doc_id": "product:PP-All_Beauty-B07W6H8CGT",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0153",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02014",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:AS-All_Beauty-B0BTJ6SYKB-price_value",
        "review:RV-AMZREV-All_Beauty-00064",
        "review:RV-AMZREV-All_Beauty-01805"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02014",
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
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 21,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00064",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01805",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0154",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00926",
        "product:PP-All_Beauty-B08KYLTK5H",
        "review:AS-All_Beauty-B08KYLTK5H-skin_scent",
        "review:RV-AMZREV-All_Beauty-00065"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00926",
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
          "doc_id": "product:PP-All_Beauty-B08KYLTK5H",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08KYLTK5H-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00065",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0155",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00066",
        "product:PP-All_Beauty-B08KWN77LW",
        "review:AS-All_Beauty-B08KWN77LW-skin_scent",
        "review:RV-AMZREV-All_Beauty-01209"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00066",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08KWN77LW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08KWN77LW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01209",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0156",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00067",
        "product:PP-All_Beauty-B08HXQ3T9K",
        "review:AS-All_Beauty-B08HXQ3T9K-skin_scent",
        "review:RV-AMZREV-All_Beauty-01140"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00067",
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
          "doc_id": "product:PP-All_Beauty-B08HXQ3T9K",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08HXQ3T9K-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01140",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0157",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00068",
        "product:PP-All_Beauty-B0B2L218H2",
        "review:AS-All_Beauty-B0B2L218H2-skin_scent",
        "review:RV-AMZREV-All_Beauty-01306",
        "review:RV-AMZREV-All_Beauty-00069"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00068",
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
          "doc_id": "product:PP-All_Beauty-B0B2L218H2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0B2L218H2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01306",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00069",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0158",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00068",
        "product:PP-All_Beauty-B0B2L218H2",
        "review:AS-All_Beauty-B0B2L218H2-skin_scent",
        "review:RV-AMZREV-All_Beauty-01306",
        "review:RV-AMZREV-All_Beauty-00069"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00068",
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
          "doc_id": "product:PP-All_Beauty-B0B2L218H2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0B2L218H2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01306",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00069",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0159",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04516",
        "product:PP-All_Beauty-B08FRQGYDF",
        "review:AS-All_Beauty-B08FRQGYDF-price_value",
        "review:RV-AMZREV-All_Beauty-04940",
        "review:RV-AMZREV-All_Beauty-00070"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04516",
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
          "doc_id": "product:PP-All_Beauty-B08FRQGYDF",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04940",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00070",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0160",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00071",
        "product:PP-All_Beauty-B08BZ1RHPS",
        "review:AS-All_Beauty-B08BZ1RHPS-quality_damage",
        "review:RV-AMZREV-All_Beauty-01603",
        "review:RV-AMZREV-All_Beauty-02969"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00071",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B08BZ1RHPS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08BZ1RHPS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01603",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02969",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0161",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00072",
        "product:PP-All_Beauty-B085NYYLQ8",
        "review:AS-All_Beauty-B085NYYLQ8-price_value",
        "review:RV-AMZREV-All_Beauty-04968",
        "review:RV-AMZREV-All_Beauty-01495"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00072",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B085NYYLQ8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B085NYYLQ8-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04968",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01495",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0162",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00073",
        "product:PP-All_Beauty-B085WTCBLG"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00073",
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
          "doc_id": "product:PP-All_Beauty-B085WTCBLG",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0163",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01662",
        "product:PP-All_Beauty-B088FBNQXW",
        "review:RV-AMZREV-All_Beauty-00074"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01662",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B088FBNQXW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00074",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0164",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02757",
        "product:PP-All_Beauty-B087D7MVHB",
        "review:AS-All_Beauty-B087D7MVHB-skin_scent",
        "review:RV-AMZREV-All_Beauty-00075",
        "review:AS-All_Beauty-B087D7MVHB-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02757",
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
          "doc_id": "product:PP-All_Beauty-B087D7MVHB",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B087D7MVHB-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00075",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B087D7MVHB-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0165",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00076",
        "product:PP-All_Beauty-B07PRDZ2BH",
        "review:AS-All_Beauty-B07PRDZ2BH-skin_scent",
        "review:RV-AMZREV-All_Beauty-01016"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00076",
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
          "doc_id": "product:PP-All_Beauty-B07PRDZ2BH",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07PRDZ2BH-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01016",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0166",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01156",
        "product:PP-All_Beauty-B083TLNBJJ",
        "review:AS-All_Beauty-B083TLNBJJ-skin_scent",
        "review:RV-AMZREV-All_Beauty-00077"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01156",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B083TLNBJJ",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B083TLNBJJ-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00077",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0167",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00078",
        "product:PP-All_Beauty-B082NKQ4ZT",
        "review:AS-All_Beauty-B082NKQ4ZT-skin_scent",
        "review:RV-AMZREV-All_Beauty-03385"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00078",
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
          "doc_id": "product:PP-All_Beauty-B082NKQ4ZT",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B082NKQ4ZT-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03385",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0168",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02758",
        "product:PP-All_Beauty-B084D86YL8",
        "review:AS-All_Beauty-B084D86YL8-skin_scent",
        "review:RV-AMZREV-All_Beauty-01709",
        "review:RV-AMZREV-All_Beauty-00079"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02758",
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
          "doc_id": "product:PP-All_Beauty-B084D86YL8",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B084D86YL8-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01709",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00079",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0169",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00080",
        "product:PP-All_Beauty-B07WNBZQGT",
        "review:AS-All_Beauty-B07WNBZQGT-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00080",
          "doc_type": "review_evidence",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07WNBZQGT",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07WNBZQGT-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0170",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00081",
        "product:PP-All_Beauty-B07SW7D6ZR",
        "review:AS-All_Beauty-B07SW7D6ZR-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00081",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07SW7D6ZR",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07SW7D6ZR-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0171",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00082",
        "product:PP-All_Beauty-B07JDD2L3M"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00082",
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
          "doc_id": "product:PP-All_Beauty-B07JDD2L3M",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0172",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00883",
        "product:PP-All_Beauty-B082MTTFZD",
        "review:AS-All_Beauty-B082MTTFZD-skin_scent",
        "review:RV-AMZREV-All_Beauty-00083"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00883",
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
          "doc_id": "product:PP-All_Beauty-B082MTTFZD",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B082MTTFZD-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00083",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0173",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00084",
        "review:RV-AMZREV-All_Beauty-04872",
        "review:RV-AMZREV-All_Beauty-01335",
        "review:RV-AMZREV-All_Beauty-04294",
        "review:RV-AMZREV-All_Beauty-00327"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00084",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04872",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01335",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04294",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00327",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0174",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01402",
        "review:RV-AMZREV-All_Beauty-01704",
        "review:RV-AMZREV-All_Beauty-00330",
        "review:RV-AMZREV-All_Beauty-00085",
        "review:RV-AMZREV-All_Beauty-02672"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01402",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01704",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00330",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00085",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02672",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0175",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00087",
        "product:PP-All_Beauty-B077YR3333",
        "review:AS-All_Beauty-B077YR3333-skin_scent",
        "review:RV-AMZREV-All_Beauty-03200",
        "review:RV-AMZREV-All_Beauty-01576"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00087",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B077YR3333",
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
          "doc_id": "review:AS-All_Beauty-B077YR3333-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03200",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01576",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0176",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01403",
        "review:RV-AMZREV-All_Beauty-03316",
        "review:RV-AMZREV-All_Beauty-01649",
        "review:RV-AMZREV-All_Beauty-01259",
        "review:RV-AMZREV-All_Beauty-00088"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01403",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03316",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01649",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01259",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00088",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0177",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04887",
        "product:PP-All_Beauty-B07KV31WDS",
        "review:AS-All_Beauty-B07KV31WDS-skin_scent",
        "review:RV-AMZREV-All_Beauty-00089"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04887",
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
          "doc_id": "product:PP-All_Beauty-B07KV31WDS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07KV31WDS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00089",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0178",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02588",
        "review:RV-AMZREV-All_Beauty-02765",
        "review:RV-AMZREV-All_Beauty-00922",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02748"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02588",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00922",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02748",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0179",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04979",
        "product:PP-All_Beauty-B071R2QPF3",
        "review:AS-All_Beauty-B071R2QPF3-skin_scent",
        "review:RV-AMZREV-All_Beauty-00091",
        "review:RV-AMZREV-All_Beauty-03501"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04979",
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
          "doc_id": "product:PP-All_Beauty-B071R2QPF3",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B071R2QPF3-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00091",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03501",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0180",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00092",
        "product:PP-All_Beauty-B01KJPFO9W",
        "review:RV-AMZREV-All_Beauty-01506",
        "review:RV-AMZREV-All_Beauty-01261"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00092",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B01KJPFO9W",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01506",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01261",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0181",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-delivery",
        "review:RV-AMZREV-All_Beauty-02899",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02922",
        "review:RV-AMZREV-All_Beauty-02931"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02899",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02922",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 28,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02931",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0182",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-price_value",
        "review:RV-AMZREV-All_Beauty-02907",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02934",
        "review:RV-AMZREV-All_Beauty-02897"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02907",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02934",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02897",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0183",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-quality_damage",
        "review:RV-AMZREV-All_Beauty-02899",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02886",
        "review:RV-AMZREV-All_Beauty-02916"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02899",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02886",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02916",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0184",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-refund_return",
        "review:RV-AMZREV-All_Beauty-02916",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02932",
        "review:RV-AMZREV-All_Beauty-02931"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02916",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02932",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02931",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0185",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-skin_scent",
        "review:RV-AMZREV-All_Beauty-02904",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02888",
        "review:RV-AMZREV-All_Beauty-02889"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02904",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02888",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02889",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0186",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
        "review:RV-AMZREV-All_Beauty-02786",
        "product:PP-All_Beauty-B081TJ8YS3",
        "review:RV-AMZREV-All_Beauty-02777",
        "review:RV-AMZREV-All_Beauty-02225"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02786",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B081TJ8YS3",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02777",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02225",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0187",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08P2DZB4X-battery_power",
        "review:RV-AMZREV-All_Beauty-03160",
        "product:PP-All_Beauty-B08P2DZB4X",
        "review:RV-AMZREV-All_Beauty-04952"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08P2DZB4X-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08P2DZB4X",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04952",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0188",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08P2DZB4X-skin_scent",
        "review:RV-AMZREV-All_Beauty-00006",
        "product:PP-All_Beauty-B08P2DZB4X",
        "review:RV-AMZREV-All_Beauty-01196",
        "review:RV-AMZREV-All_Beauty-03160"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08P2DZB4X-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08P2DZB4X",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01196",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0189",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07RBSLNFR-price_value",
        "review:RV-AMZREV-All_Beauty-00662",
        "product:PP-All_Beauty-B07RBSLNFR",
        "review:RV-AMZREV-All_Beauty-01586"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07RBSLNFR-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00662",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07RBSLNFR",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01586",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0190",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07RBSLNFR-skin_scent",
        "review:RV-AMZREV-All_Beauty-00662",
        "product:PP-All_Beauty-B07RBSLNFR",
        "review:RV-AMZREV-All_Beauty-01199",
        "review:RV-AMZREV-All_Beauty-01586"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07RBSLNFR-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00662",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07RBSLNFR",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01199",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01586",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0191",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
        "review:RV-AMZREV-All_Beauty-00010",
        "product:PP-All_Beauty-B07SLFWZKN",
        "review:RV-AMZREV-All_Beauty-01541",
        "review:RV-AMZREV-All_Beauty-01337"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00010",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07SLFWZKN",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01541",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01337",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0192",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08GLG6W8T-skin_scent",
        "review:RV-AMZREV-All_Beauty-00012",
        "product:PP-All_Beauty-B08GLG6W8T",
        "review:RV-AMZREV-All_Beauty-01589",
        "review:RV-AMZREV-All_Beauty-04959"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08GLG6W8T-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00012",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08GLG6W8T",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01589",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04959",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0193",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
        "review:RV-AMZREV-All_Beauty-00013",
        "product:PP-All_Beauty-B08M3C6LVS",
        "review:RV-AMZREV-All_Beauty-00424"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00013",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08M3C6LVS",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00424",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0194",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
        "review:RV-AMZREV-All_Beauty-00552",
        "product:PP-All_Beauty-B07KG1TWP5",
        "review:RV-AMZREV-All_Beauty-02483"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00552",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KG1TWP5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02483",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0195",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07W397QG4-skin_scent",
        "review:RV-AMZREV-All_Beauty-00287",
        "product:PP-All_Beauty-B07W397QG4",
        "review:RV-AMZREV-All_Beauty-01014",
        "review:RV-AMZREV-All_Beauty-01155"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07W397QG4-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00287",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07W397QG4",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01014",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01155",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0196",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-missing_parts",
        "review:RV-AMZREV-All_Beauty-00090",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-03440"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03440",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0197",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-quality_damage",
        "review:RV-AMZREV-All_Beauty-00090",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-02765"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0198",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-skin_scent",
        "review:RV-AMZREV-All_Beauty-00553",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02765"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00553",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0199",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B01M7UMAUG-battery_power",
        "review:RV-AMZREV-All_Beauty-02100",
        "product:PP-All_Beauty-B01M7UMAUG",
        "review:RV-AMZREV-All_Beauty-02446",
        "review:RV-AMZREV-All_Beauty-03685"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B01M7UMAUG-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02100",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B01M7UMAUG",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02446",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03685",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0200",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B01M7UMAUG-delivery",
        "review:RV-AMZREV-All_Beauty-03370",
        "product:PP-All_Beauty-B01M7UMAUG",
        "review:RV-AMZREV-All_Beauty-00019"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B01M7UMAUG-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03370",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B01M7UMAUG",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00019",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0201",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B01M7UMAUG-price_value",
        "review:RV-AMZREV-All_Beauty-00159",
        "product:PP-All_Beauty-B01M7UMAUG",
        "review:RV-AMZREV-All_Beauty-01297",
        "review:RV-AMZREV-All_Beauty-03370"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B01M7UMAUG-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00159",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B01M7UMAUG",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01297",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03370",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0202",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00JMDPK8S-battery_power",
        "review:RV-AMZREV-All_Beauty-03393",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:RV-AMZREV-All_Beauty-02637"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0203",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00JMDPK8S-price_value",
        "review:RV-AMZREV-All_Beauty-03393",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:RV-AMZREV-All_Beauty-02637"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0204",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
        "review:RV-AMZREV-All_Beauty-00020",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:RV-AMZREV-All_Beauty-02637"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00020",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0205",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07ZJKVVLW-delivery",
        "review:RV-AMZREV-All_Beauty-02496",
        "product:PP-All_Beauty-B07ZJKVVLW",
        "review:RV-AMZREV-All_Beauty-04456"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 30,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02496",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04456",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0206",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07ZJKVVLW-price_value",
        "review:RV-AMZREV-All_Beauty-02135",
        "product:PP-All_Beauty-B07ZJKVVLW",
        "review:RV-AMZREV-All_Beauty-03835",
        "review:RV-AMZREV-All_Beauty-04456"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 30,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02135",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03835",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04456",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0207",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07ZJKVVLW-refund_return",
        "review:RV-AMZREV-All_Beauty-02135",
        "product:PP-All_Beauty-B07ZJKVVLW",
        "review:RV-AMZREV-All_Beauty-01769"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02135",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 27,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01769",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0208",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07ZJKVVLW-skin_scent",
        "review:RV-AMZREV-All_Beauty-04079",
        "product:PP-All_Beauty-B07ZJKVVLW",
        "review:RV-AMZREV-All_Beauty-04456",
        "review:RV-AMZREV-All_Beauty-04575"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 30,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04079",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04456",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04575",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0209",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B082QX2HP6-skin_scent",
        "review:RV-AMZREV-All_Beauty-03596",
        "product:PP-All_Beauty-B082QX2HP6",
        "review:RV-AMZREV-All_Beauty-01737"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B082QX2HP6-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03596",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B082QX2HP6",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01737",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0210",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B083BDVS36-delivery",
        "review:RV-AMZREV-All_Beauty-03256",
        "product:PP-All_Beauty-B083BDVS36",
        "review:RV-AMZREV-All_Beauty-03499"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B083BDVS36-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03256",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03499",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0211",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B083BDVS36-price_value",
        "review:RV-AMZREV-All_Beauty-03499",
        "product:PP-All_Beauty-B083BDVS36",
        "review:RV-AMZREV-All_Beauty-03261"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B083BDVS36-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03499",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03261",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0212",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B09FP8PP2K-price_value",
        "review:RV-AMZREV-All_Beauty-02557",
        "product:PP-All_Beauty-B09FP8PP2K",
        "review:RV-AMZREV-All_Beauty-04440",
        "review:RV-AMZREV-All_Beauty-00028"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02557",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B09FP8PP2K",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04440",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0213",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B09FP8PP2K-quality_damage",
        "review:RV-AMZREV-All_Beauty-03842",
        "product:PP-All_Beauty-B09FP8PP2K",
        "review:RV-AMZREV-All_Beauty-00028"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03842",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B09FP8PP2K",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0214",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B09FP8PP2K-skin_scent",
        "review:RV-AMZREV-All_Beauty-01726",
        "product:PP-All_Beauty-B09FP8PP2K",
        "review:RV-AMZREV-All_Beauty-03767",
        "review:RV-AMZREV-All_Beauty-03993"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": null,
          "signals": [
            "dense",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01726",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B09FP8PP2K",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03767",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 26,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03993",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 24,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0215",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00946HGLW-skin_scent",
        "review:RV-AMZREV-All_Beauty-03339",
        "product:PP-All_Beauty-B00946HGLW",
        "review:RV-AMZREV-All_Beauty-04408",
        "review:RV-AMZREV-All_Beauty-00030"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00946HGLW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03339",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00946HGLW",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04408",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00030",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0216",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-00032",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:RV-AMZREV-All_Beauty-04255",
        "review:RV-AMZREV-All_Beauty-01976"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0020MKBNW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
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
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01976",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0217",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B005IYYF5E-missing_parts",
        "review:RV-AMZREV-All_Beauty-02077",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-02203",
        "review:RV-AMZREV-All_Beauty-03658"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02077",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02203",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03658",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0218",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B005IYYF5E-price_value",
        "review:RV-AMZREV-All_Beauty-04066",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-03658",
        "review:RV-AMZREV-All_Beauty-04244"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04066",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03658",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04244",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0219",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B005IYYF5E-quality_damage",
        "review:RV-AMZREV-All_Beauty-02519",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-04295"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02519",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04295",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0220",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B005IYYF5E-skin_scent",
        "review:RV-AMZREV-All_Beauty-04576",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-01986",
        "review:RV-AMZREV-All_Beauty-02203"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04576",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": null,
          "signals": [
            "dense",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01986",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02203",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0221",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-missing_parts",
        "review:RV-AMZREV-All_Beauty-04479",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-03109",
        "review:RV-AMZREV-All_Beauty-00111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04479",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03109",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 24,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0222",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-price_value",
        "review:RV-AMZREV-All_Beauty-04239",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-00111",
        "review:RV-AMZREV-All_Beauty-03708"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 27,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04239",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03708",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0223",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-quality_damage",
        "review:RV-AMZREV-All_Beauty-02728",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-01855"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02728",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01855",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 27,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0224",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-skin_scent",
        "review:RV-AMZREV-All_Beauty-03754",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-01727",
        "review:RV-AMZREV-All_Beauty-03809"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 27,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03754",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01727",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 26,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03809",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0225",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07H281V4V-price_value",
        "review:RV-AMZREV-All_Beauty-03968",
        "product:PP-All_Beauty-B07H281V4V",
        "review:RV-AMZREV-All_Beauty-02644"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07H281V4V-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03968",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07H281V4V",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02644",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 22,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0226",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-missing_parts",
        "review:RV-AMZREV-All_Beauty-02007",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-01861"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02007",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01861",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0227",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-price_value",
        "review:RV-AMZREV-All_Beauty-00045",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-04207"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00045",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04207",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0228",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-quality_damage",
        "review:RV-AMZREV-All_Beauty-03525",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-01693",
        "review:RV-AMZREV-All_Beauty-03425"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03525",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01693",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03425",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0229",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-skin_scent",
        "review:RV-AMZREV-All_Beauty-02771",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-01861"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02771",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01861",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0230",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0875V791H-skin_scent",
        "review:RV-AMZREV-All_Beauty-04428",
        "product:PP-All_Beauty-B0875V791H",
        "review:RV-AMZREV-All_Beauty-01661",
        "review:RV-AMZREV-All_Beauty-02001"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0875V791H-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04428",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0875V791H",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01661",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02001",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0231",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07LBK2YQX-skin_scent",
        "review:RV-AMZREV-All_Beauty-00710",
        "product:PP-All_Beauty-B07LBK2YQX",
        "review:RV-AMZREV-All_Beauty-00051"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07LBK2YQX-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00710",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07LBK2YQX",
          "doc_type": "product_profile",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00051",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0232",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B015RR870U-delivery",
        "review:RV-AMZREV-All_Beauty-02403",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-01642"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B015RR870U-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02403",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B015RR870U",
          "doc_type": "product_profile",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01642",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0233",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B015RR870U-price_value",
        "review:RV-AMZREV-All_Beauty-01642",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-02401",
        "review:RV-AMZREV-All_Beauty-03290"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B015RR870U-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": null,
          "signals": [
            "dense",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01642",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B015RR870U",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02401",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03290",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0234",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B015RR870U-skin_scent",
        "review:RV-AMZREV-All_Beauty-03573",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-01642",
        "review:RV-AMZREV-All_Beauty-02323"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B015RR870U-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03573",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B015RR870U",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01642",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02323",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0235",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B000OQFVLS-quality_damage",
        "review:RV-AMZREV-All_Beauty-00055",
        "product:PP-All_Beauty-B000OQFVLS",
        "review:RV-AMZREV-All_Beauty-02412"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B000OQFVLS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B000OQFVLS",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02412",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0236",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
        "review:RV-AMZREV-All_Beauty-00844",
        "product:PP-All_Beauty-B00C0YZBJE",
        "review:RV-AMZREV-All_Beauty-04783",
        "review:RV-AMZREV-All_Beauty-04851"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00844",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00C0YZBJE",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04783",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04851",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0237",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0B8DZ7H5F-skin_scent",
        "review:RV-AMZREV-All_Beauty-02669",
        "product:PP-All_Beauty-B0B8DZ7H5F",
        "review:RV-AMZREV-All_Beauty-04370"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0B8DZ7H5F-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02669",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0B8DZ7H5F",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04370",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0238",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0B4JP5YD9-skin_scent",
        "review:RV-AMZREV-All_Beauty-00410",
        "product:PP-All_Beauty-B0B4JP5YD9",
        "review:RV-AMZREV-All_Beauty-00058"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0B4JP5YD9-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00410",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0B4JP5YD9",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00058",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0239",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0B4JPGX8P-skin_scent",
        "review:RV-AMZREV-All_Beauty-01549",
        "product:PP-All_Beauty-B0B4JPGX8P",
        "review:RV-AMZREV-All_Beauty-00059"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0B4JPGX8P-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01549",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0B4JPGX8P",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00059",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0240",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B09KT4RJG6-skin_scent",
        "review:RV-AMZREV-All_Beauty-01148",
        "product:PP-All_Beauty-B09KT4RJG6",
        "review:RV-AMZREV-All_Beauty-00060"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09KT4RJG6-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01148",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B09KT4RJG6",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00060",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0241",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KQ32Z8C-skin_scent",
        "review:RV-AMZREV-All_Beauty-00595",
        "product:PP-All_Beauty-B07KQ32Z8C",
        "review:RV-AMZREV-All_Beauty-00061",
        "review:RV-AMZREV-All_Beauty-01193"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KQ32Z8C-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00595",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KQ32Z8C",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00061",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01193",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0242",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08PQ6YXSH-skin_scent",
        "review:RV-AMZREV-All_Beauty-03159",
        "product:PP-All_Beauty-B08PQ6YXSH",
        "review:RV-AMZREV-All_Beauty-00062"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08PQ6YXSH-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03159",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08PQ6YXSH",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00062",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0243",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
        "review:RV-AMZREV-All_Beauty-02014",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-00064"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02014",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00064",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0244",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0BTJ6SYKB-price_value",
        "review:RV-AMZREV-All_Beauty-01959",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-03521",
        "review:RV-AMZREV-All_Beauty-00998"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01959",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03521",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00998",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0245",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0BTJ6SYKB-skin_scent",
        "review:RV-AMZREV-All_Beauty-01341",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-01439",
        "review:RV-AMZREV-All_Beauty-03276"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01341",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01439",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03276",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0246",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08KYLTK5H-skin_scent",
        "review:RV-AMZREV-All_Beauty-00926",
        "product:PP-All_Beauty-B08KYLTK5H",
        "review:RV-AMZREV-All_Beauty-00065"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08KYLTK5H-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00926",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08KYLTK5H",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00065",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0247",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08KWN77LW-skin_scent",
        "review:RV-AMZREV-All_Beauty-03163",
        "product:PP-All_Beauty-B08KWN77LW",
        "review:RV-AMZREV-All_Beauty-01421",
        "review:RV-AMZREV-All_Beauty-00941"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08KWN77LW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03163",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08KWN77LW",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01421",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00941",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0248",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08HXQ3T9K-skin_scent",
        "review:RV-AMZREV-All_Beauty-00067",
        "product:PP-All_Beauty-B08HXQ3T9K",
        "review:RV-AMZREV-All_Beauty-02548"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08HXQ3T9K-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00067",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08HXQ3T9K",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02548",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0249",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0B2L218H2-skin_scent",
        "review:RV-AMZREV-All_Beauty-01490",
        "product:PP-All_Beauty-B0B2L218H2",
        "review:RV-AMZREV-All_Beauty-00068",
        "review:RV-AMZREV-All_Beauty-01389"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0B2L218H2-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01490",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0B2L218H2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00068",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01389",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0250",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08FRQGYDF-delivery",
        "review:RV-AMZREV-All_Beauty-00070",
        "product:PP-All_Beauty-B08FRQGYDF",
        "review:RV-AMZREV-All_Beauty-04516"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00070",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08FRQGYDF",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04516",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0251",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08FRQGYDF-price_value",
        "review:RV-AMZREV-All_Beauty-04940",
        "product:PP-All_Beauty-B08FRQGYDF",
        "review:RV-AMZREV-All_Beauty-04516"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04940",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08FRQGYDF",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04516",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0252",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08BZ1RHPS-quality_damage",
        "review:RV-AMZREV-All_Beauty-01603",
        "product:PP-All_Beauty-B08BZ1RHPS",
        "review:RV-AMZREV-All_Beauty-02337"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08BZ1RHPS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01603",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08BZ1RHPS",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02337",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0253",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-battery_power",
        "review:AS-All_Beauty-B07LCHCD6Q-battery_power",
        "review:RV-AMZREV-All_Beauty-00351",
        "review:RV-AMZREV-All_Beauty-02441",
        "review:AS-All_Beauty-B07H8Y5QT2-battery_power"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07LCHCD6Q-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00351",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02441",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07H8Y5QT2-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0254",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-delivery",
        "review:AS-All_Beauty-B01695MZ9S-delivery",
        "review:RV-AMZREV-All_Beauty-03667",
        "review:RV-AMZREV-All_Beauty-00522",
        "review:RV-AMZREV-All_Beauty-02717"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-delivery",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01695MZ9S-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03667",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00522",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02717",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0255",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-general_complaint"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-general_complaint",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0256",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-missing_parts",
        "review:AS-All_Beauty-B000X20Y4C-missing_parts",
        "review:RV-AMZREV-All_Beauty-04671",
        "review:RV-AMZREV-All_Beauty-04717",
        "review:RV-AMZREV-All_Beauty-03692"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B000X20Y4C-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04671",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04717",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03692",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 25,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0257",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-price_value",
        "review:AS-All_Beauty-B07TK6647L-price_value",
        "review:RV-AMZREV-All_Beauty-01634",
        "review:RV-AMZREV-All_Beauty-03653",
        "ticket:FAQ-All_Beauty-0085"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-price_value",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07TK6647L-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01634",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03653",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0085",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0258",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-quality_damage",
        "review:AS-All_Beauty-B088838886-quality_damage",
        "review:RV-AMZREV-All_Beauty-02543",
        "review:RV-AMZREV-All_Beauty-04006",
        "review:RV-AMZREV-All_Beauty-02082"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 25,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B088838886-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02543",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04006",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02082",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0259",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-refund_return",
        "review:AS-All_Beauty-B00J7QCNDU-refund_return",
        "review:RV-AMZREV-All_Beauty-04883",
        "review:RV-AMZREV-All_Beauty-04243",
        "review:RV-AMZREV-All_Beauty-00024"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B00J7QCNDU-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04883",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04243",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00024",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0260",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-skin_scent",
        "review:AS-All_Beauty-B01FS5PJNE-skin_scent",
        "review:RV-AMZREV-All_Beauty-00613",
        "review:RV-AMZREV-All_Beauty-04243",
        "review:RV-AMZREV-All_Beauty-03321"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01FS5PJNE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 16,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00613",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04243",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03321",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0261",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-battery_power",
        "review:AS-Baby_Products-B073F7FPN8-battery_power",
        "review:RV-AMZREV-Baby_Products-01944",
        "review:RV-AMZREV-Baby_Products-03693",
        "review:RV-AMZREV-Baby_Products-02803"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B073F7FPN8-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01944",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-03693",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 3,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02803",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0262",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-delivery",
        "review:AS-Baby_Products-B00GUN3Z1W-delivery",
        "review:RV-AMZREV-Baby_Products-00644",
        "review:RV-AMZREV-Baby_Products-02346",
        "review:RV-AMZREV-Baby_Products-02699"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-delivery",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B00GUN3Z1W-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00644",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-02346",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02699",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0263",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-general_complaint"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-general_complaint",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0264",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-missing_parts",
        "review:AS-Baby_Products-B0BW7CVB9K-missing_parts",
        "review:RV-AMZREV-Baby_Products-04335",
        "review:AS-Baby_Products-B0B2CBQGSS-missing_parts",
        "ticket:FAQ-Baby_Products-0094"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 9,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BW7CVB9K-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-04335",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B0B2CBQGSS-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0094",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0265",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-price_value",
        "review:AS-Baby_Products-B09RHW5WGX-price_value",
        "review:RV-AMZREV-Baby_Products-01920",
        "review:RV-AMZREV-Baby_Products-04587",
        "review:RV-AMZREV-Baby_Products-02655"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-price_value",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B09RHW5WGX-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01920",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-04587",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02655",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0266",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-quality_damage",
        "review:AS-Baby_Products-B0BFHP8JPG-quality_damage",
        "review:RV-AMZREV-Baby_Products-00649",
        "review:RV-AMZREV-Baby_Products-03395",
        "review:RV-AMZREV-Baby_Products-04838"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 23,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BFHP8JPG-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 6,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00649",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-03395",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-04838",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0267",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-refund_return",
        "review:AS-Baby_Products-B07H53Y3LL-refund_return",
        "review:RV-AMZREV-Baby_Products-00174",
        "review:RV-AMZREV-Baby_Products-01255",
        "ticket:FAQ-Baby_Products-0159"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B07H53Y3LL-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00174",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 25,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01255",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0159",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 5,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0268",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-skin_scent",
        "review:AS-Baby_Products-B09RW4YR1W-skin_scent",
        "review:RV-AMZREV-Baby_Products-00847",
        "review:RV-AMZREV-Baby_Products-00935",
        "review:RV-AMZREV-Baby_Products-02909"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B09RW4YR1W-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00847",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00935",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02909",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0269",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-battery_power",
        "review:AS-Software-B00658U5HE-battery_power",
        "review:RV-AMZREV-Software-04615",
        "review:RV-AMZREV-Software-04049",
        "review:RV-AMZREV-Software-00772"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00658U5HE-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 14,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-04615",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-04049",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-00772",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0270",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "review:CL-Software-delivery",
        "review:AS-Software-B005ZKC3YG-delivery",
        "review:RV-AMZREV-Software-03210",
        "review:RV-AMZREV-Software-03221"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-delivery",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B005ZKC3YG-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 12,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-03210",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03221",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0271",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-digital_license",
        "review:AS-Software-B0094BB4TW-digital_license",
        "review:RV-AMZREV-Software-02422",
        "review:RV-AMZREV-Software-03210",
        "review:RV-AMZREV-Software-03025"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-digital_license",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B0094BB4TW-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-02422",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03210",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-03025",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0272",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-general_complaint"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-general_complaint",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0273",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-missing_parts",
        "review:AS-Software-B004FRX0MY-missing_parts",
        "review:RV-AMZREV-Software-03036",
        "review:AS-Software-B00E5NGYVM-missing_parts",
        "review:RV-AMZREV-Software-02434"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B004FRX0MY-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-03036",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B00E5NGYVM-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 8,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-02434",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0274",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-price_value",
        "review:AS-Software-B07T771SPH-price_value",
        "review:RV-AMZREV-Software-02396",
        "review:RV-AMZREV-Software-00806",
        "review:RV-AMZREV-Software-04050"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-price_value",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B07T771SPH-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 11,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-02396",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-00806",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-04050",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0275",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-quality_damage",
        "review:RV-AMZREV-Software-00218",
        "review:RV-AMZREV-Software-03912",
        "review:RV-AMZREV-Software-02938",
        "review:RV-AMZREV-Software-02428"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-00218",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-03912",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-02938",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-02428",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 1,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0276",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-refund_return",
        "review:AS-Software-B00YHZVOCW-refund_return",
        "review:RV-AMZREV-Software-03945",
        "review:RV-AMZREV-Software-00305",
        "review:RV-AMZREV-Software-04414"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00YHZVOCW-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 4,
          "signals": [
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-03945",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-00305",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-04414",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": null,
          "signals": [
            "dense",
            "aspect_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0277",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0001",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00005",
        "review:RV-AMZREV-All_Beauty-02240"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0001",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02240",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0278",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0002",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00006",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0002",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0279",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0003",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00008"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0003",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00008",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0280",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0004",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00010",
        "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
        "review:RV-AMZREV-All_Beauty-01541"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0004",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00010",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01541",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0281",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0005",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00012",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0005",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00012",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0282",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0006",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00013",
        "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
        "review:RV-AMZREV-All_Beauty-00424"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0006",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00013",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08M3C6LVS-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00424",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0283",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0007",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00018",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0007",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00018",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0284",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0008",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00019",
        "review:AS-All_Beauty-B01M7UMAUG-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0008",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00019",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B01M7UMAUG-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0285",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0009",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00020",
        "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0009",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00020",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0286",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0010",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00023"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0010",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00023",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0287",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0011",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00024",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0011",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 15,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00024",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0288",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0012",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00026",
        "review:RV-AMZREV-All_Beauty-04511"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0012",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00026",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04511",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0289",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0013",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00027",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0013",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00027",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0290",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0014",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00028",
        "review:AS-All_Beauty-B09FP8PP2K-price_value",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0014",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 26,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0291",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0015",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00029",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0015",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00029",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0292",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0016",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00031",
        "review:RV-AMZREV-All_Beauty-02111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0016",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00031",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02111",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0293",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0017",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00032",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0017",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0294",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0018",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00035",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0018",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00035",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0295",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0019",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00036",
        "ticket:FAQ-All_Beauty-0042",
        "review:RV-AMZREV-All_Beauty-00111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0019",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00036",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "ticket:FAQ-All_Beauty-0042",
          "doc_type": "faq_case",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0296",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0020",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00038",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0020",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00038",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0297",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0021",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00039",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0021",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00039",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0298",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0022",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00042",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0022",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": null,
          "signals": [
            "dense",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00042",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0299",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0023",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00043",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0023",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00043",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0300",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0024",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00044",
        "review:RV-AMZREV-All_Beauty-04865"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0024",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00044",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04865",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0301",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0025",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00048"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0025",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00048",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0302",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0026",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00055",
        "review:AS-All_Beauty-B000OQFVLS-quality_damage",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0026",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B000OQFVLS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0303",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0027",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00056",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0027",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00056",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 10,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0304",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0028",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00064",
        "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0028",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 23,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00064",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0305",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0029",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00070",
        "review:AS-All_Beauty-B08FRQGYDF-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0029",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00070",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0306",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0030",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00074",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0030",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 13,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00074",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0307",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0031",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00079",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0031",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": null,
          "signals": [
            "dense",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00079",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0308",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0032",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00087",
        "review:AS-All_Beauty-B077YR3333-skin_scent",
        "review:RV-AMZREV-All_Beauty-01503"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0032",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00087",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B077YR3333-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01503",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0309",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0033",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:AS-All_Beauty-B07GDQPG12-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0033",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0310",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0034",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00092",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0034",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00092",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0311",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0035",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00095",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0035",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00095",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0312",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0036",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00096",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0036",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00096",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0313",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0037",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00100",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0037",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00100",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 2,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0314",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0038",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00103",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0038",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00103",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0315",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0039",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00107",
        "review:AS-All_Beauty-B088838886-quality_damage",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0039",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00107",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B088838886-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0316",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0040",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00108",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0040",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00108",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0317",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0041",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00109",
        "review:RV-AMZREV-All_Beauty-02727"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0041",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00109",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02727",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0318",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0042",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00111",
        "review:AS-All_Beauty-B07KDNK11M-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0042",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 25,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0319",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0043",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00113",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0043",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00113",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0320",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0044",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00117",
        "review:AS-All_Beauty-B0B7RBK4NJ-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0044",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00117",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0B7RBK4NJ-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0321",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0045",
        "kb:KB002_warranty_policy",
        "review:RV-AMZREV-All_Beauty-00120",
        "review:AS-All_Beauty-B08XJWLLKQ-quality_damage",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0045",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB002_warranty_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00120",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08XJWLLKQ-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0322",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0046",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00123",
        "review:AS-All_Beauty-B08N6YHQXT-quality_damage",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0046",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00123",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08N6YHQXT-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0323",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0047",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00125",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0047",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00125",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0324",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0048",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00126",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0048",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00126",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0325",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0049",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00127",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0049",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00127",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0326",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0050",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00128",
        "review:RV-AMZREV-All_Beauty-02799"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0050",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00128",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02799",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0327",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0051",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00132",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0051",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00132",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0328",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0052",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00133",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0052",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00133",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0329",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0053",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00136",
        "review:AS-All_Beauty-B07H3S8WTV-battery_power",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0053",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00136",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07H3S8WTV-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0330",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0054",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00145",
        "review:RV-AMZREV-All_Beauty-04272"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0054",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00145",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04272",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0331",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0055",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00147"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0055",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00147",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0332",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0056",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00148",
        "review:AS-All_Beauty-B01M1OFZOG-skin_scent",
        "review:RV-AMZREV-All_Beauty-03847"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0056",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00148",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B01M1OFZOG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03847",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0333",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0057",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00151",
        "review:AS-All_Beauty-B09WSVFSGJ-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0057",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 25,
          "bm25_rank": null,
          "signals": [
            "dense",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00151",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B09WSVFSGJ-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 18,
          "signals": [
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0334",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0058",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00155",
        "review:RV-AMZREV-All_Beauty-01330"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0058",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00155",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01330",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0335",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0059",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00157",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0059",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00157",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0336",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0060",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00161"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0060",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00161",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0337",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0061",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00162",
        "review:AS-All_Beauty-B0778WCBMF-skin_scent",
        "review:RV-AMZREV-All_Beauty-03415"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0061",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00162",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0778WCBMF-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03415",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0338",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0062",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00163",
        "review:AS-All_Beauty-B085BB7B1M-price_value",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0062",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00163",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B085BB7B1M-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0339",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0063",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00164"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0063",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00164",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0340",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0064",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00167"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0064",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00167",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0341",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0065",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00168",
        "review:RV-AMZREV-All_Beauty-03535"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0065",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00168",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03535",
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
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0342",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0066",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00169",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0066",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00169",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0343",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0067",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00170",
        "review:AS-All_Beauty-B09ZKWV5MK-delivery",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0067",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00170",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B09ZKWV5MK-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0344",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0068",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00171",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0068",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00171",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0345",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0069",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00172",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0069",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": 18,
          "signals": [
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00172",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0346",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0070",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00173",
        "review:AS-All_Beauty-B0B5X48DZR-skin_scent",
        "review:RV-AMZREV-All_Beauty-03527"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0070",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00173",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B0B5X48DZR-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03527",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0347",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0071",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00174",
        "review:AS-All_Beauty-B08N5NDVGH-price_value",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0071",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00174",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08N5NDVGH-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0348",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0072",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00175",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0072",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00175",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0349",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0073",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00176",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0073",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00176",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0350",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0074",
        "kb:KB004_shipping_delivery_policy",
        "review:RV-AMZREV-All_Beauty-00180",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0074",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00180",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0351",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0075",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00181",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0075",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00181",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0352",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0076",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00182",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0076",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00182",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0353",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0077",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00183",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0077",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00183",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0354",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0078",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00184",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0078",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00184",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0355",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0079",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00185"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0079",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00185",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0356",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0080",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00186",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0080",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00186",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0357",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0081",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00189",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0081",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00189",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0358",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0082",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00191",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0082",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00191",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0359",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0083",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00192",
        "review:AS-All_Beauty-B08Z3THTQT-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0083",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00192",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B08Z3THTQT-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0360",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0084",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00195",
        "kb:refund_reason_codes",
        "kb:KB006_return_status_matrix"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0084",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 2,
          "doc_id": "kb:KB005_missing_parts_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00195",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match",
            "aspect_match",
            "sibling_expansion"
          ]
        },
        {
          "rank": 4,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "kb:KB006_return_status_matrix",
          "doc_type": "html_policy_page",
          "relevant": true,
          "dense_rank": null,
          "bm25_rank": null,
          "signals": [
            "forced_fallback",
            "policy_fallback"
          ]
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    }
  ],
  "support_rows": [
    {
      "query_id": "Q-001",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The return/refund path depends on the return window, item condition, and proof of purchase. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-001#d9c7c01c76812a84], [doc:kb:",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-002",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Warranty cases require product identification, proof of purchase, and a defect description. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-002#c2cbb38083f73a1b], [doc:kb:",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-003",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: NightView Baby Monitor (BABY-MONITOR-01) at $89.99, rating 4.4, stock 17; Anti-Colic Glass Bottle Set (BABY-BOTTLE-02) at $28.0, rating 4.6, stock 55. I used product/review evidence from [doc:product:P-BABY-001#b5c4f3e2",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-004",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review for nightview baby monitor. rating 2. delivery was late and the baby monitor battery drained overnight. i may return it if replacement is not available.. Suggested action: inspec",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-005",
      "expected_intent": "sku_order",
      "intent": "sku_order",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "SKU SOFT-PDF-01 maps to PDF Studio Pro License. Current demo inventory is 100 units at $59.0. Supporting context: [doc:product:P-SOFT-001#379d92ed1d5b4648], [doc:kb:KB004_shipping_delivery_policy#71d755fa30c11a8e].",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-006",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:T-004#d85e1613389da6aa], [doc:k",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0001",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0002",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0003",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0004",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0005",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0006",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0007",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0008",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0009",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0010",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0011",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0012",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0013",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0014",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0015",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0016",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0017",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0018",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0019",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0020",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0021",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0022",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0023",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0024",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0025",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0026",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0027",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0028",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0029",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0030",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0031",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0032",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0033",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0034",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0035",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0036",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0037",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0038",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0039",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0040",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0041",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0042",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0043",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0044",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0045",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0046",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0047",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0048",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0049",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0050",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0051",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0052",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0053",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0054",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0055",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0056",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0057",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0058",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0059",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0060",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0061",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0062",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0063",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0064",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0065",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0066",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0067",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0068",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0069",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0070",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0071",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0072",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0073",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0074",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0075",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0076",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0077",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0078",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0079",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0080",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0081",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0082",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0083",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0084",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0085",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0086",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0087",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0088",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0089",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0090",
      "expected_intent": "recommendation",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0. I used product/review evidence from [doc:review:RV-AMZREV-All_Beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0091",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 5. verified purchase true. review titl",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0092",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for all natural vegan dry shampoo powder - eco friendly, root touch up | hair powder volumizer | for brown hair, brunette and dark hair. (brun + application",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0093",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for china glaze nail polish, wanderlust 1381 sku b00r8dxl44 in category all_beauty. rating 4. verified purchase true. review title: pretty color. customer t",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0094",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for disposable facial cotton tissue, 100pcs cotton towels face cleansing wipes for sensitive skin, makeup remover washcloth dry and wet use sku b099drhw5v i",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0095",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for niseyo new faux locs 24 inch crochet hair 6 packs 120 strands long soft ombre natural crochet braids (24'' 6pcs t27) sku b08bbq29n5 in category all_beau",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0096",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for nira skincare laser & serum bundle - includes anti-aging laser & hyaluronic acid serum - reduces appearance of fine lines & wrinkles - fda cleared sku b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0097",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for caroline keller keratin shampoo for dry and damaged hair and scalp. with argan oil, avocado oil keratin and vitamins. specially formulated for post kera",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0098",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for orange peel nature's cleanse facial scrub - by visage pure - usda organic - physician formulated - research supported - natural exfoliating, refreshing,",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0099",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for ogana cell peptide concentrating amazing lotion 2.03 fl.oz. (60ml) - 650ppm peptide contained mild moisturizing facial lotion, hypoallergenic natural in",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0100",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for keratin secrets do it yourself home keratin system sku b07slfwzkn in category all_beauty. rating 3. verified purchase false. review title: just ok. cust",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0101",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for hanhoo red pomegranate 6pcs skin care set (6pcs/set) sku b08glg6w8t in category all_beauty. rating 5. verified purchase false. review title: great refre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0102",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 24k gold under eye mask– 20 pairs- under eye patches with face massager roller, anti-aging hyaluronic acid collagen eye masks for dark circles and puffi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0103",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for bellezza versa styler 1 inch titanium plates flat iron twisted hair straighteners (blush pink) sku b07ghpct6t in category all_beauty. rating 5. verified",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0104",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for organic bamboo cotton ear swabs by bali boo - 200 - natural wooden qtips cotton swabs for cleaning ears, baby or makeup and nails - sustainable & vegan ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0105",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for iryasa night indulge cream - natural face cream for dry skin - vegan anti aging night cream for women - firming cream for face and neck - organic vitami",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0106",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for spa grade jade roller for face with gua sha | jade face roller massager | jade facial roller | face roller massager | jade rollers | wrinkle roller sku ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0107",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for manicure and pedicure nail clipper from powergrooming - powerful trimmer for thick and thin finger nails and toe nails - included nail file and\"catcher\"",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0108",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for philips sonicare essence+ gum health & airfloss rechargeable electric flosser, bundle value pack, hx8218/02 sku b01m7umaug in category all_beauty. ratin",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0109",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for panasonic ew-dl82 sonic vibration rechargeable electric toothbrush, white sku b00jmdpk8s in category all_beauty. rating 3. verified purchase false. revi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0110",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips for daily natural eye brown makeup (dark brown/ chestnut) sku",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0111",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 2 pieces hair brush cleaner cleaning tool comb cleaner hair brush cleaner comb brushes mini hair dirt remover brush with metal wire rake wooden handle f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0112",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for original detangler hair brush sku b077srdvg9 in category all_beauty. rating 3. verified purchase true. review title: just ok. customer text: its ok not ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0113",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for charcoal konjac face sponge 3 pk | acne, psoriasis, bumpy skin & ingrown hairs sku b01aktghfw in category all_beauty. rating 1. verified pur; faq case for charcoal k",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0114",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for yellow brick road 1lb shea butter/1lb cocoa butter combo sku b079smvsyw in category all_beauty. rating 5. verified purchase true. review title: moisturi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0115",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for bromley's 7 blade classic razor - 1 razor sku b07k8vtt6m in category all_beauty. rating 2. verified purchase true. review title: i'll stick ; faq case for bromley's ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0116",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for adofect 31 pairs gold eye mask collagen eye gel pads under eye mask for puffiness and dark circle under eye patches for women and men, gold ; faq case for adofect 31",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0117",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for yeshan bow headbands for women non slip stretchy hair bands elastic headwraps knotted headband wired rabbit ears turban headbands,pack of 8 sku b09fp8pp",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0118",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for halo hair extensions thick invisible wire hair extension with transparent headband hairpieces 4 types adjustable headwidth size wavy curly l; faq case for halo hair ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0119",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 1/8 inch snap on rollers 8 pack (pink) sku b00946hglw in category all_beauty. rating 5. verified purchase true. review title: good price. customer text:",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0120",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for replacement discs for bellasonic 4-in-1 rechargeable electric nail file set with patented oscillating head – shape, smooth, buff & shine nails | remove ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0121",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for wet-nap moist towelette (case of 1000) sku b0020mkbnw in category all_beauty. rating 5. verified purchase true. review title: they smell good. they are ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0122",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for premium life rain hat with full visor sku b00023j4aw in category all_beauty. rating 5. verified purchase true. review title: rain scarf. customer text: ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0123",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for shower cap - blue dot pattern, vinyl material, elastic band, extra large, large, won’t fall off your head, sku b005iyyf5e in category all_beauty. rating",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0124",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for nyx eyebrow shaper, 1 count sku b01m5knsqn in category all_beauty. rating 1. verified purchase true. review title: don’t bother. customer te; faq case for nyx eyebro",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0125",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, kids and pets (pi; faq case for chialstar ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0126",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for zynery 10 pack button headbands for nurses doctors - non slip knotted elastic twisted head wrap, wide headbands with ear loop holder buttons for women g",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0127",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for bow hair band lovely rabbit ears soft carol fleece bowknot makeup cosmetic shower elastic hairlace headband(pink) sku b081gcfhpg in category all_beauty.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0128",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for alice false eyelashes natural wispy lashes 5 pairs multipack sku b07h8z3smk in category all_beauty. rating 5. verified purchase true. review title: love",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0129",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 6 pack 50ml/1.7oz travel plastic clear keychain bottles, leakproof refillable empty bottles portable squeeze containers with 6pcs carabiner and 2pcs fun",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0130",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for zoya all snuggled up quad,4 count (pack of 1) sku b07h281v4v in category all_beauty. rating 5. verified purchase true. review title: great colors!. cust",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0131",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for 24 eyebrow stencil , meilala eyebrow shaper kit ,reusable eyebrow template eye brown shape kit with eyebrow razor… sku b09ff97rhl in categor; faq case for 24 eyebrow",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0132",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for rhinestones bobby pins silver plated words letter crystal hair pins metal hair clips hair barrettes sparkly hair accessories 3pcs (3pcs) sku b07xyxsycd ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0133",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for foot peel mask exfoliating (3 pairs) - foot peeling mask (2 pairs) & moisturizing foot mask (1 pairs), make your feet baby soft, peel away calluses and ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0134",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for cotton headbands 6 pack stretch elastic yoga soft and stretchy sports fashion headband for teens women girls by kenz laurenz (6 pc 2\" cotton headbands-n",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0135",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for merit advanced eye serum sku b018f28b1y in category all_beauty. rating 5. verified purchase true. review title: great for sensitive skin!. customer text",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0136",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for rhinestones for acrylic nails, nail gems jewels crystals 7660pcs red flatback nail rhinestones mutil shapes sizes for nail art design, non-hotfix rhines",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0137",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for sonic facial cleansing brush, electric silicone face brush and massager, waterproof silicone face scrubber for deep cleansing, exfoliating, ; faq case for sonic faci",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0138",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 3d mask bracket - internal support holder frame nose breathing smoothly - protect lipstick lips - diy face mask accessories - 5pcs (l-adult) sku b08dxdl",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0139",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for magic hair curlers spiral curls styling kit, 20 pcs no heat wave hair curlers with 2 styling hook for long hair most kinds of hairstyles (50cm) sku b087",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0140",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for schick bare by schick dermaplaning tool with 2 dermaplaning razors and 1 cleaning brush, 2 count sku b07lbk2yqx in category all_beauty. rating 4. verifi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0141",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for pore strips, blackhead remover charcoal nose strips deep cleansing 24 strips sku b07fx94gyx in category all_beauty. rating 4. verified purchase false. r",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0142",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for sailor moon x colourpop collection - from the moon - pressed powder blush (from the moon) sku b08cxfddv8 in category all_beauty. rating 5. verified purc",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0143",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, travel size 2 oz) sku b015rr870u in category all_beauty. rating 5. verified purchase true.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0144",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for onox foot solution spray, 4 oz sku b000oqfvls in category all_beauty. rating 4. verified purchase true. review title: not 100% sure how safe it is parti",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0145",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for salerm color reverse sku b00c0yzbje in category all_beauty. rating 5. verified purchase true. review title: great product, although smells gross. custom",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0146",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for frankies bikinis lip butter gloss, sleeping vegan lip mask overnight, moisturizing lip plumper, vitamin e lip balm moisturizer, hydrating lip oil with c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0147",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for elli k essential sincerity from az time reverse cream - made in usa - anti-aging face moisturizer for dry & rough skin – repairing treatment cream – hig",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0148",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for elli k essential sincerity from az time reverse double ampoule – made in usa - double layering serum – repairing & deep hydrating – oil and cream formul",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0149",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for simply dana rivitastore neck firming cream — skin firming cream for tightening neck, jawline, and chest, collagen peptides, and squalane cream for wrink",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0150",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for apivita queen bee holistic age defense night cream 1.69 fl.oz. |intensive night treatment that speeds skin regeneration, smooths wrinkle & increases ski",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0151",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for dose of colors cold pressed booster multi-use oil 1oz sku b08pq6yxsh in category all_beauty. rating 5. verified purchase false. review title: leaves ski",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0152",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for little moon essentials tropical bath & shower sugar exfoliant, beach all you want, 2 oz. sku b07w6h8cgt in category all_beauty. rating 4. verified purch",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0153",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for shakira perfumes - dance for women - long lasting - femenine, charming and modern perfume - fruity floral notes - ideal for day wear - 1.7 fl oz sku b0b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0154",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for more di croatia eye cream - dubrovnik gold anti aging eye cream for wrinkles and fine lines, reduce puffiness and dark circles, hyaluronic acid and immo",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0155",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for genskin generation skin hydrating marine algae eye patches | hydrate, plump, brighten eye area 180g/6.34 oz - 30 pairs sku b08kwn77lw in category all_be",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0156",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for invisibobble sprunchie spiral hair ring - true black - scrunchie stylish bracelet, strong elastic grip coil accessories for women - gentle for girls tee",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0157",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for pinrose perfumes bold soul - eau de parfum petals (fragrance towelettes) - vegan, cruelty-free, and hypoallergenic scent with essential oils - notes of ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0158",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for pinrose perfumes bold soul - eau de parfum petals (fragrance towelettes) - vegan, cruelty-free, and hypoallergenic scent with essential oils - notes of ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0159",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for serovital super saturated restoring cleansing cloths - cleansing face wipes with green tea and hyaluronic acid - makeup remover wipes - 1 pack 15 ct sku",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0160",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for md complete bright & healthy vitamin c+ vitalizing face serum| with vitamin c, vitamin e and herbal extracts | potent antioxidant protection, nourishes,",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0161",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for caudalie favorites set sku b085nyylq8 in category all_beauty. rating 4. verified purchase false. review title: good variety of travel size skincare prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0162",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for senvenski gel nail polish red rose burgundy purple mauve lavender violets lilac white black glitter starrily girlfriend gift soak off uv led manicure ar",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0163",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for mainbasics headband with buttons for face masks (gray) sku b088fbnqxw in category all_beauty. rating 4. verified purchase false. review title: works wel",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0164",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 2-pack puretize 16.9 oz hand sanitizing gel w/pump tops - extra strength 70% ethyl alcohol - moisturizing formula with aloe vera, vitamin e & botanical ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0165",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for lua skincare clarity calming face oil, 1 fz sku b07prdz2bh in category all_beauty. rating 4. verified purchase false. review title: leaves skin feeling ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0166",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for be plain vitamin ampoule 1.01 fl oz. - korean multi vitamin serum for face with vitamin b, vitamin c, vitamin e, hyaluronic acid sku b083tlnbjj in categ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0167",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 6 pack soft headband beoffer coral fleece women makeup spa head bands turban fashion bow bowknot hairlace headwear wash face hair holder elastic top kno",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0168",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for md complete bright & healthy citrus-c refresh retinol + vitamin c multitasking treatment sku b084d86yl8 in category all_beauty. rating 3. verified purch",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0169",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for serum by merlot - resveratrol - natural anti-aging - damage corrector - boost collagen - 1 fl oz. - dark circle corrector - sku b07wnbzqgt in category a",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0170",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for kale firm & smooth body lotion - superfood infused firming body lotion with kale. 6.8 fl.oz, anti-aging moisturizing lotion for all skin types sku b07sw",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0171",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for kerotin hairspray - flexible hold & volume with provitamin b5 - heat protectant, frizz ease, weightless hair spray sku b07jdd2l3m in category all_beauty",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0172",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for wow the crowd eyelash growth serum for full, luscious, long and thick lashes - natural formula (7ml), clinically and dermatologist tested - boost and en",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0173",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 13.5 fl. oz. goat milk facial cleanser, moisturizing face wash for women, hydrating natural face wash, anti-aging face wash, face wash for aging ski sku",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0174",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for c.o. bigelow no. 007 dr hiosous quince hand lotion, 4 ounces sku b07j2qzbtp in category all_beauty. rating 5. verified purchase false. review title: sup",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0175",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for anti-aging hydrating serum with natural mango micro-beads, vitamins e and c, natural and organic plant extracts, paraben-free, 30 ml, made in france, ph",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0176",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for [old version] quickbooks desktop pro 2019 with enhanced payroll [pc disc] sku b07fz5hzlm in category all_beauty. rating 4. verified purchase false. revi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0177",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for 3 pack hair towel wrap turban microfiber drying bath shower head towel with buttons - quick magic dryer dry hair hat wrapped bath cap sku b07kv31wds in ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0178",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for spa grade jade roller for face with gua sha | jade face roller massager | jade facial roller | face roller massager | jade rollers | wrinkle roller sku ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0179",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for aurotrends makeup remover towel,2 pack reusable chemical-free microfiber makeup remover cloths,magically and gently wipe away cosmetics,sunscreen,oil an",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0180",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "easy",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review evidence for lagunamoon gel nail polish, soak off uv led nail manicure color gel polish varnish set 6pcs 8ml - love spectrum sku b01kjpfo9w in category all_beauty. r",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0181",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 1. verified purchase true.; review evidence for her",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0182",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 2. verified purchase true.; review evidence for her",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0183",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 1. verified purchase true.; review evidence for her",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0184",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 1. verified purchase true.; review evidence for her",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0185",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, 8 oz) sku b00yq6x8eo in category all_beauty. rating 2. verified purchase true.; review evidence for her",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0186",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for all natural vegan dry shampoo powder - eco friendly, root touch up | hair powder volumizer | for brown hair, brunette and dark hair. (brun +; review evidence for all",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0187",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for nira skincare laser & serum bundle - includes anti-aging laser & hyaluronic acid serum - reduces appearance of fine lines & wrinkles - fda cleared",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0188",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for nira skincare laser & serum bundle - includes anti-aging laser & hyaluronic acid serum - reduces appearance of fine lines & wrinkles - fda cleared",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0189",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for ogana cell peptide concentrating amazing lotion 2.03 fl.oz. (60ml) - 650ppm peptide contained mild moisturizing facial lotion, hypoallergenic natu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0190",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for ogana cell peptide concentrating amazing lotion 2.03 fl.oz. (60ml) - 650ppm peptide contained mild moisturizing facial lotion, hypoallergenic natu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0191",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for keratin secrets do it yourself home keratin system sku b07slfwzkn in category all_beauty. rating 2. verified purchase false. review title: f. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0192",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for hanhoo red pomegranate 6pcs skin care set (6pcs/set) aspect skin_scent. category all_beauty; matched reviews 3; low rating reviews 0. representati",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0193",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 24k gold under eye mask– 20 pairs- under eye patches with face massager roller, anti-aging hyaluronic acid collagen eye masks for dark circles and",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0194",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for organic bamboo cotton ear swabs by bali boo - 200 - natural wooden qtips cotton swabs for cleaning ears, baby or makeup and nails - sustaina. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0195",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for iryasa night indulge cream - natural face cream for dry skin - vegan anti aging night cream for women - firming cream for face and neck - organic ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0196",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for spa grade jade roller for face with gua sha | jade face roller massager | jade facial roller | face roller massager | jade rollers | wrinkle rolle",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0197",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: arger than this and i found it to be a bit awkward at times. plu | i wasn’t sure what to expect with spa grade jade roller for face with gua sha | jade face roller massager",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0198",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for spa grade jade roller for face with gua sha | jade face roller massager | jade facial roller | face roller massager | jade rollers | wrinkle rolle",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0199",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for philips sonicare essence+ gum health & airfloss rechargeable electric flosser, bundle value pack, hx8218/02 aspect battery_power. category all_bea",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0200",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for philips sonicare essence+ gum health & airfloss rechargeable electric flosser, bundle value pack, hx8218/02 aspect delivery. category all_beauty; ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0201",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for philips sonicare essence+ gum health & airfloss rechargeable electric flosser, bundle value pack, hx8218/02 aspect price_value. category all_beaut",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0202",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for panasonic ew-dl82 sonic vibration rechargeable electric toothbrush, white aspect battery_power. category all_beauty; matched reviews 2; low rating",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0203",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for panasonic ew-dl82 sonic vibration rechargeable electric toothbrush, white aspect price_value. category all_beauty; matched reviews 2; low rating r",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0204",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for panasonic ew-dl82 sonic vibration rechargeable electric toothbrush, white aspect quality_damage. category all_beauty; matched reviews 2; low ratin",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0205",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips for daily natural eye brown makeup (dark brown/ chestnu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0206",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips for daily natural eye brown makeup (dark brown/ chestnu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0207",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips for daily natural eye brown makeup (dark brown/ chestnu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0208",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips for daily natural eye brown makeup (dark brown/ chestnu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0209",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for 2 pieces hair brush cleaner cleaning tool comb cleaner hair brush cleaner comb brushes mini hair dirt remover brush with metal wire rake woo. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0210",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for adofect 31 pairs gold eye mask collagen eye gel pads under eye mask for puffiness and dark circle under eye patches for women and men, gold . Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0211",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for adofect 31 pairs gold eye mask collagen eye gel pads under eye mask for puffiness and dark circle under eye patches for women and men, gold aspect",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0212",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for yeshan bow headbands for women non slip stretchy hair bands elastic headwraps knotted headband wired rabbit ears turban headbands,pack of 8 aspect",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0213",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for yeshan bow headbands for women non slip stretchy hair bands elastic headwraps knotted headband wired rabbit ears turban headbands,pack of 8 aspect",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0214",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for yeshan bow headbands for women non slip stretchy hair bands elastic headwraps knotted headband wired rabbit ears turban headbands,pack of 8 aspect",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0215",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for 1/8 inch snap on rollers 8 pack (pink) aspect skin_scent. category all_beauty; matched reviews 4; low rating reviews 0. representative evidence: i",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0216",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for wet-nap moist towelette (case of 1000) aspect delivery. category all_beauty; matched reviews 2; low rating reviews 0. representative evidence: i'm",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0217",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for shower cap - blue dot pattern, vinyl material, elastic band, extra large, large, won’t fall off your head, sku b005iyyf5e in category all_be. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0218",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for shower cap - blue dot pattern, vinyl material, elastic band, extra large, large, won’t fall off your head, sku b005iyyf5e in category all_be. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0219",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for shower cap - blue dot pattern, vinyl material, elastic band, extra large, large, won’t fall off your head, sku b005iyyf5e in category all_be. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0220",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for shower cap - blue dot pattern, vinyl material, elastic band, extra large, large, won’t fall off your head, aspect skin_scent. category all_beauty;",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0221",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, kids and pets (pink/gre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0222",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, kids and pets (pink/gre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0223",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, kids and pets (pink/gre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0224",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, kids and pets (pink/gre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0225",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for zoya all snuggled up quad,4 count (pack of 1) aspect price_value. category all_beauty; matched reviews 2; low rating reviews 0. representative evi",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0226",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for cotton headbands 6 pack stretch elastic yoga soft and stretchy sports fashion headband for teens women girls by kenz laurenz (6 pc 2\" cotton. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0227",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for cotton headbands 6 pack stretch elastic yoga soft and stretchy sports fashion headband for teens women girls by kenz laurenz (6 pc 2\" cotton headb",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0228",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for cotton headbands 6 pack stretch elastic yoga soft and stretchy sports fashion headband for teens women girls by kenz laurenz (6 pc 2\" cotton. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0229",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for cotton headbands 6 pack stretch elastic yoga soft and stretchy sports fashion headband for teens women girls by kenz laurenz (6 pc 2\" cotton headb",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0230",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for magic hair curlers spiral curls styling kit, 20 pcs no heat wave hair curlers with 2 styling hook for long hair most kinds of hairstyles (50cm) as",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0231",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for schick bare by schick dermaplaning tool with 2 dermaplaning razors and 1 cleaning brush, 2 count sku b07lbk2yqx in category all_beauty. rati. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0232",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, travel size 2 oz) sku b015rr870u in category all_beauty. rating 1. verified pu. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0233",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for herbivore - natural sea mist texturizing salt spray (coconut, travel size 2 oz) aspect price_value. category all_beauty; matched reviews 3; low ra",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0234",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for herbivore - natural sea mist texturizing salt spray (coconut, travel size 2 oz) sku b015rr870u in category all_beauty. rating 2. verified pu. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0235",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for onox foot solution spray, 4 oz aspect quality_damage. category all_beauty; matched reviews 2; low rating reviews 0. representative evidence: had o",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0236",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for salerm color reverse sku b00c0yzbje in category all_beauty. rating 1. verified purchase true. review title: from purple to blue 😡. customer ; review evidence for sal",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0237",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for frankies bikinis lip butter gloss, sleeping vegan lip mask overnight, moisturizing lip plumper, vitamin e lip balm moisturizer, hydrating lip oil ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0238",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for elli k essential sincerity from az time reverse cream - made in usa - anti-aging face moisturizer for dry & rough skin – repairing treatment cream",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0239",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for elli k essential sincerity from az time reverse double ampoule – made in usa - double layering serum – repairing & deep hydrating – oil and cream ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0240",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for simply dana rivitastore neck firming cream — skin firming cream for tightening neck, jawline, and chest, collagen peptides, and squalane cream for",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0241",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for apivita queen bee holistic age defense night cream 1.69 fl.oz. |intensive night treatment that speeds skin regeneration, smooths wrinkle & increas",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0242",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for dose of colors cold pressed booster multi-use oil 1oz aspect skin_scent. category all_beauty; matched reviews 2; low rating reviews 0. representat",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0243",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for shakira perfumes - dance for women - long lasting - femenine, charming and modern perfume - fruity floral notes - ideal for day wear - 1.7 fl oz a",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0244",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for shakira perfumes - dance for women - long lasting - femenine, charming and modern perfume - fruity floral notes - ideal for day wear - 1.7 fl oz a",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0245",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for shakira perfumes - dance for women - long lasting - femenine, charming and modern perfume - fruity floral notes - ideal for day wear - 1.7 fl oz a",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0246",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for more di croatia eye cream - dubrovnik gold anti aging eye cream for wrinkles and fine lines, reduce puffiness and dark circles, hyaluronic acid an",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0247",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for genskin generation skin hydrating marine algae eye patches | hydrate, plump, brighten eye area 180g/6.34 oz - 30 pairs aspect skin_scent. category",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0248",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for invisibobble sprunchie spiral hair ring - true black - scrunchie stylish bracelet, strong elastic grip coil accessories for women - gentle for gir",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0249",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops signals show recurring low-rating issues: review evidence for pinrose perfumes bold soul - eau de parfum petals (fragrance towelettes) - vegan, cruelty-free, and hypoallergenic scent with essential oils. Suggested action: inspe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0250",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for serovital super saturated restoring cleansing cloths - cleansing face wipes with green tea and hyaluronic acid - makeup remover wipes - 1 pack 15 ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0251",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for serovital super saturated restoring cleansing cloths - cleansing face wipes with green tea and hyaluronic acid - makeup remover wipes - 1 pack 15 ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0252",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: review aspect summary for md complete bright & healthy vitamin c+ vitalizing face serum| with vitamin c, vitamin e and herbal extracts | potent antioxidant protection, nour",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0253",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect battery_power. cluster size 36 from public review subset, average rating 2.278.. Citations: [doc:review:CL-All_Beauty-b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0254",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect delivery. cluster size 63 from public review subset, average rating 2.032.. Citations: [doc:review:CL-All_Beauty-delive",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0255",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect general_complaint. cluster size 403 from public review subset, average rating 2.154.. Citations: [doc:review:CL-All_Bea",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0256",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect missing_parts. cluster size 76 from public review subset, average rating 2.263.. Citations: [doc:review:CL-All_Beauty-m",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0257",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect price_value. cluster size 200 from public review subset, average rating 2.32.. Citations: [doc:review:CL-All_Beauty-pri",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0258",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect quality_damage. cluster size 100 from public review subset, average rating 2.08.. Citations: [doc:review:CL-All_Beauty-",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0259",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect refund_return. cluster size 109 from public review subset, average rating 1.523.. Citations: [doc:review:CL-All_Beauty-",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0260",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category all_beauty and aspect skin_scent. cluster size 466 from public review subset, average rating 2.296. affected products include: orange peel na",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0261",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect battery_power. cluster size 33 from public review subset, average rating 2.424.. Citations: [doc:review:CL-Baby_Prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0262",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect delivery. cluster size 52 from public review subset, average rating 2.365. affected products include: similac alimen",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0263",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect general_complaint. cluster size 440 from public review subset, average rating 2.207.. Citations: [doc:review:CL-Baby",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0264",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect missing_parts. cluster size 73 from public review subset, average rating 2.356.. Citations: [doc:review:CL-Baby_Prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0265",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect price_value. cluster size 170 from public review subset, average rating 2.418.. Citations: [doc:review:CL-Baby_Produ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0266",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect quality_damage. cluster size 74 from public review subset, average rating 2.243.. Citations: [doc:review:CL-Baby_Pro",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0267",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect refund_return. cluster size 68 from public review subset, average rating 1.794.. Citations: [doc:review:CL-Baby_Prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0268",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect skin_scent. cluster size 93 from public review subset, average rating 2.269.. Citations: [doc:review:CL-Baby_Product",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0269",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect battery_power. cluster size 46 from public review subset, average rating 1.913. affected products include: starz, philo: ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0270",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: ons of magix music maker, including version 7, 2005, and 10. each has been a steady progression of improvement and capability, so i was quite e | i have never been especial",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0271",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect digital_license. cluster size 94 from public review subset, average rating 1.819. affected products include: discovery+ |",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0272",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect general_complaint. cluster size 1176 from public review subset, average rating 1.913. affected products include: roxio cr",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0273",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect missing_parts. cluster size 47 from public review subset, average rating 1.787. affected products include: frndly tv, gsn",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0274",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect price_value. cluster size 116 from public review subset, average rating 1.922. affected products include: wizard of oz fr",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0275",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect quality_damage. cluster size 36 from public review subset, average rating 2.056. affected products include: white noise, ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0276",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category software and aspect refund_return. cluster size 156 from public review subset, average rating 1.692. affected products include: bitdefender i",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0277",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0278",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The return/refund path depends on the return window, item condition, and proof of purchase. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051ef",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0279",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0280",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0281",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB004_shipping_delivery_policy#71d75",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0282",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0283",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0007#8907dde9046",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0284",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0008#efa50744bbd2",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0285",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0009#5a52eb33af1",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0286",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0287",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The return/refund path depends on the return window, item condition, and proof of purchase. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051ef",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0288",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0012#331bc6d182f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0289",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The return/refund path depends on the return window, item condition, and proof of purchase. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0013#e99aa551a086f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0290",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0291",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0292",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0016#29e68c67f8b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0293",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0017#ea8afb7181ab",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0294",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0018#5cb0bee8702",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0295",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0296",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0297",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0021#3379871a035",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0298",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0022#30d775813d4",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0299",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB004_shipping_delivery_policy#71d75",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0300",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0024#5a72e20c3f8",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0301",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0302",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0026#221a30238ba",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0303",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0027#3f482a348af",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0304",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0028#e312ce51b81",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0305",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0029#efc7494e750f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0306",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0030#5ad63947c32",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0307",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0308",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0309",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0033#759dd1001d6",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0310",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0034#210714d6da2",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0311",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0035#f17feb00ba5f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0312",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0036#ee88a9036cf",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0313",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0037#10b3b9927f01",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0314",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0038#9fe4a111d9c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0315",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0039#c8510056eca",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0316",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0317",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0318",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0319",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0043#a42e6cae76fe",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0320",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0044#cee53e3c2263",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0321",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0045#d81510ee7f0",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0322",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0046#62790af3efb",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0323",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0324",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0325",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0049#e5e2da803be",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0326",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0050#68da0417d4c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0327",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0328",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0052#1709515be8b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0329",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0330",
      "expected_intent": "support",
      "intent": "recommendation",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Recommended options: HydraGlow Vitamin C Serum (BEAUTY-SERUM-01) at $24.99, rating 4.5, stock 42; Ionic Compact Hair Dryer (BEAUTY-DRYER-02) at $39.5, rating 3.9, stock 0; Cloud Backup Family Plan (SOFT-BACKUP-02) at $79.0, rating 4.0, stoc",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0331",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0055#09e26492612",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0332",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0333",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0057#a7e34e751af9",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0334",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0335",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0059#c741d5fee2e",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0336",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0060#7138fd1c22f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0337",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0338",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0339",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0063#0e6839aee3c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0340",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0341",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0065#1f91ec9789d",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0342",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0066#e03e9087648",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0343",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB004_shipping_delivery_policy#71d75",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0344",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0068#cabe63368e1",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0345",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0346",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0347",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0071#3a92122d437",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0348",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0349",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Shipping issues should be checked against the shipping policy and the latest carrier status. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0073#3b3a1f01d6f5",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0350",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB004_shipping_delivery_policy#71d7",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0351",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0075#61c7a30a72e",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0352",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0353",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0077#35456dbd87b",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0354",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0078#b84bc65ce03",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0355",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB001_return_refund_policy#ee79e051",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0356",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0080#74938436a0a",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0357",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0081#4213784b482",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0358",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0082#d58d64e4994",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0359",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:ticket:FAQ-All_Beauty-0083#c3f142f4572",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0360",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The safest support response is to answer from the matching policy and similar ticket history. Based on the retrieved policy/ticket evidence, I would respond with a grounded support answer and cite [doc:kb:KB005_missing_parts_policy#50e5f95b",
      "expected_action": "answer",
      "safety_category": "normal"
    }
  ]
}
```
