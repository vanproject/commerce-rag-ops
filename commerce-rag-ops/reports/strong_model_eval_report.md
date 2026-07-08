# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

## 摘要

- 样本数: 30
- 检索后端: qdrant
- 检索模式: hybrid_rerank
- Precision@5: 0.9333
- Recall@5: 0.8778
- MRR: 0.9333
- NDCG@5: 0.9333
- 引用率: 1.0
- 关键词覆盖率: 0.9556
- groundedness 代理指标: 0.9618
- 延迟 p50/p95: 685 ms / 882 ms
- Embedding 模型: BAAI/bge-large-en-v1.5
- Reranker 模型: BAAI/bge-reranker-large
- LLM 模型: template

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |
| recommendation | 25 | 1.0 | 0.9333 | 1.0 | 1.0 | 1.0 | 1.0 |
| sku_order | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.6667 |
| support | 3 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| medium | 24 | 1.0 | 0.9306 | 1.0 | 1.0 | 1.0 | 1.0 |
| unknown | 6 | 0.6667 | 0.6667 | 0.6667 | 0.6667 | 1.0 | 0.7778 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 119 | 112 |
| dense | 119 | 112 |
| entity_match | 104 | 104 |
| policy_fallback | 3 | 3 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| recommendation | bm25: 106, dense: 106, entity_match: 104 |
| support | bm25: 6, dense: 6, policy_fallback: 3 |

## Agentic 证据诊断

- 重试率: 0.0667

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 30 |
| 尝试次数 | 1: 28, 2: 2 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| none | 0 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| none | none |

## 原始 JSON

```json
{
  "n": 30,
  "retrieval_backend": "qdrant",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "BAAI/bge-large-en-v1.5",
    "embedding_backend": "sentence-transformers",
    "reranker_model": "BAAI/bge-reranker-large",
    "llm_model": "template"
  },
  "retrieval": {
    "precision@5": 0.9333,
    "recall@5": 0.8778,
    "mrr": 0.9333,
    "ndcg@5": 0.9333
  },
  "support_quality": {
    "citation_ok": 1.0,
    "keyword_coverage": 0.9556,
    "groundedness_proxy": 0.9618
  },
  "latency": {
    "p50_ms": 685,
    "p95_ms": 882
  },
  "by_intent": {
    "customer_ops": {
      "n": 1,
      "retrieval": {
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.0,
        "groundedness_proxy": 0.4642
      }
    },
    "recommendation": {
      "n": 25,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9333,
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
        "precision@5": 0.0,
        "recall@5": 0.0,
        "mrr": 0.0,
        "ndcg@5": 0.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.6667,
        "groundedness_proxy": 0.3908
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
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    }
  },
  "by_difficulty": {
    "medium": {
      "n": 24,
      "retrieval": {
        "precision@5": 1.0,
        "recall@5": 0.9306,
        "mrr": 1.0,
        "ndcg@5": 1.0
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    },
    "unknown": {
      "n": 6,
      "retrieval": {
        "precision@5": 0.6667,
        "recall@5": 0.6667,
        "mrr": 0.6667,
        "ndcg@5": 0.6667
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.7778,
        "groundedness_proxy": 0.8092
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 119,
      "dense": 119,
      "entity_match": 104,
      "policy_fallback": 3
    },
    "relevant_hit_signal_counts": {
      "bm25": 112,
      "dense": 112,
      "entity_match": 104,
      "policy_fallback": 3
    },
    "relevant_hit_signals_by_intent": {
      "recommendation": {
        "bm25": 106,
        "dense": 106,
        "entity_match": 104
      },
      "support": {
        "bm25": 6,
        "dense": 6,
        "policy_fallback": 3
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 30
    },
    "attempt_counts": {
      "1": 28,
      "2": 2
    },
    "retry_rate": 0.0667,
    "evidence_gap_counts": {},
    "evidence_gaps_by_intent": {}
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
          "dense_rank": 2,
          "bm25_rank": 2,
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
          "dense_rank": 7,
          "bm25_rank": 33,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:R-010",
          "doc_type": "review",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 38,
          "signals": [
            "dense",
            "bm25"
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
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "retrieved": [
        "review:CL-Baby_Products-quality_damage",
        "review:AS-Baby_Products-B0BB84JXS9-missing_parts",
        "review:RV-AMZREV-Baby_Products-01255",
        "review:RV-AMZREV-Baby_Products-00358",
        "ticket:FAQ-Software-0043"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 12,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BB84JXS9-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 36,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01255",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 21,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-00358",
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
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0043",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25"
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
      "precision@5": 0.0,
      "recall@5": 0.0,
      "mrr": 0.0,
      "ndcg@5": 0.0,
      "retrieved": [
        "product:PP-Software-B008XME36E",
        "product:PP-Software-B00Q7T7NZ8"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B008XME36E",
          "doc_type": "product_profile",
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
          "doc_id": "product:PP-Software-B00Q7T7NZ8",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
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
          "dense_rank": 1,
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
          "dense_rank": 3,
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
      "query_id": "QS-0001",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00511",
        "product:PP-All_Beauty-B000067E30",
        "review:AS-All_Beauty-B000067E30-price_value",
        "review:RV-AMZREV-All_Beauty-04225",
        "review:RV-AMZREV-All_Beauty-03366"
      ],
      "signals": [
        {
          "rank": 1,
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000067E30",
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
        "review:RV-AMZREV-All_Beauty-04062",
        "product:PP-All_Beauty-B000068PBJ",
        "review:AS-All_Beauty-B000068PBJ-battery_power",
        "review:RV-AMZREV-All_Beauty-03549",
        "review:RV-AMZREV-All_Beauty-00821"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04062",
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
          "doc_id": "product:PP-All_Beauty-B000068PBJ",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 43,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000068PBJ-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 63,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03549",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00821",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-02207",
        "review:RV-AMZREV-All_Beauty-02030"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00033",
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
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02207",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02030",
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
      "query_id": "QS-0004",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00708",
        "product:PP-All_Beauty-B0002M5JNY",
        "review:AS-All_Beauty-B0002M5JNY-battery_power",
        "review:RV-AMZREV-All_Beauty-02372",
        "review:RV-AMZREV-All_Beauty-02426"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00708",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02372",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02426",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-02960",
        "review:AS-All_Beauty-B000CSH3YG-skin_scent",
        "review:RV-AMZREV-All_Beauty-04313",
        "review:RV-AMZREV-All_Beauty-01974",
        "review:RV-AMZREV-All_Beauty-02126"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02960",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B000CSH3YG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 62,
          "bm25_rank": 86,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04313",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 75,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01974",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 87,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02126",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 55,
          "bm25_rank": 88,
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
      "query_id": "QS-0007",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04052",
        "product:PP-All_Beauty-B000GBID0M",
        "review:AS-All_Beauty-B000GBID0M-battery_power",
        "review:RV-AMZREV-All_Beauty-04121",
        "review:RV-AMZREV-All_Beauty-04937"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04052",
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
          "doc_id": "product:PP-All_Beauty-B000GBID0M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 15,
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
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04121",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04937",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-03554",
        "product:PP-All_Beauty-B000I1CFC2",
        "review:AS-All_Beauty-B000I1CFC2-price_value",
        "review:RV-AMZREV-All_Beauty-02308",
        "review:RV-AMZREV-All_Beauty-02648"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03554",
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
          "doc_id": "product:PP-All_Beauty-B000I1CFC2",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000I1CFC2-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02308",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02648",
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
        "review:RV-AMZREV-All_Beauty-02148"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04380",
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
          "doc_id": "product:PP-All_Beauty-B000NHZSKC",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 1,
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
          "bm25_rank": 27,
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
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02148",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
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
        "review:RV-AMZREV-All_Beauty-04920",
        "product:PP-All_Beauty-B000NIZYIW",
        "review:RV-AMZREV-All_Beauty-03825",
        "review:RV-AMZREV-All_Beauty-03769",
        "review:RV-AMZREV-All_Beauty-00647"
      ],
      "signals": [
        {
          "rank": 1,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03769",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00647",
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
      "query_id": "QS-0012",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03580",
        "product:PP-All_Beauty-B000OQFVLS",
        "review:AS-All_Beauty-B000OQFVLS-quality_damage",
        "review:RV-AMZREV-All_Beauty-01189",
        "review:RV-AMZREV-All_Beauty-00055"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03580",
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
          "dense_rank": 24,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01189",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
          "doc_type": "review_evidence",
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
      "query_id": "QS-0013",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04029",
        "product:PP-All_Beauty-B000PKKAGO",
        "review:AS-All_Beauty-B000PKKAGO-skin_scent",
        "review:RV-AMZREV-All_Beauty-03934",
        "review:RV-AMZREV-All_Beauty-02129"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04029",
          "doc_type": "review_evidence",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000PKKAGO",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000PKKAGO-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03934",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02129",
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
      "query_id": "QS-0014",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04436",
        "product:PP-All_Beauty-B000X20Y4C",
        "review:AS-All_Beauty-B000X20Y4C-quality_damage",
        "review:RV-AMZREV-All_Beauty-04055",
        "review:RV-AMZREV-All_Beauty-02418"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04436",
          "doc_type": "review_evidence",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B000X20Y4C",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B000X20Y4C-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 43,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04055",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02418",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 25,
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
        "review:RV-AMZREV-All_Beauty-03046",
        "review:RV-AMZREV-All_Beauty-04319"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02206",
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
          "doc_id": "product:PP-All_Beauty-B001281404",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B001281404-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03046",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04319",
          "doc_type": "review_evidence",
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
        "review:RV-AMZREV-All_Beauty-00534",
        "product:PP-All_Beauty-B001V9V71U",
        "review:AS-All_Beauty-B001V9V71U-delivery",
        "review:RV-AMZREV-All_Beauty-00580",
        "review:RV-AMZREV-All_Beauty-04318"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00534",
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
          "doc_id": "product:PP-All_Beauty-B001V9V71U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B001V9V71U-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 24,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00580",
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
        "review:RV-AMZREV-All_Beauty-02050",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-00032",
        "review:RV-AMZREV-All_Beauty-04255"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02050",
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
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-04778",
        "review:RV-AMZREV-All_Beauty-00828"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04526",
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
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04778",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00828",
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
        "review:RV-AMZREV-All_Beauty-01633",
        "product:PP-All_Beauty-B003NTFDFM",
        "review:AS-All_Beauty-B003NTFDFM-skin_scent",
        "review:RV-AMZREV-All_Beauty-02150",
        "review:RV-AMZREV-All_Beauty-01643"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01633",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B003NTFDFM",
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
          "doc_id": "review:AS-All_Beauty-B003NTFDFM-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02150",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01643",
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
          "bm25_rank": 2,
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
          "bm25_rank": 1,
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
          "dense_rank": 23,
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
      "query_id": "QS-0024",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01034",
        "product:PP-All_Beauty-B0046BPTI2",
        "review:AS-All_Beauty-B0046BPTI2-price_value",
        "review:RV-AMZREV-All_Beauty-00321",
        "review:RV-AMZREV-All_Beauty-00744"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01034",
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
          "doc_id": "product:PP-All_Beauty-B0046BPTI2",
          "doc_type": "product_profile",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0046BPTI2-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00321",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 9,
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
      "attempts": 2,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 0.4642,
      "answer_preview": "Customer ops summary should focus on repeated review/ticket themes: complaint cluster for category baby_products and aspect refund_return. cluster size 68 from public review subset, average rating 1.794.; complaint cluster for category baby",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "Q-005",
      "expected_intent": "sku_order",
      "intent": "sku_order",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.3908,
      "answer_preview": "SKU SOFT-PDF-01 maps to PDF Studio Pro License. Current demo inventory is 100 units at $59.0. Supporting context: [doc:product:PP-Software-B008XME36E#c36b4e293b554a0b], [doc:ticket:FAQ-All_Beauty-0065#87768eeb1835a658], [doc:ticket:FAQ-Soft",
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
    }
  ]
}
```
