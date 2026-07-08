# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

## 摘要

- 样本数: 366
- 检索后端: qdrant
- 检索模式: hybrid_rerank
- Precision@5: 0.9536
- Recall@5: 0.8686
- MRR: 0.9945
- NDCG@5: 0.947
- 引用率: 0.8743
- 关键词覆盖率: 0.8051
- groundedness 代理指标: 0.9793
- 延迟 p50/p95: 14528 ms / 41106 ms
- Embedding 模型: BAAI/bge-large-en-v1.5
- Reranker 模型: BAAI/bge-reranker-large
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 187 | 0.9904 | 0.9109 | 0.9947 | 0.9927 | 1.0 | 0.9234 |
| recommendation | 91 | 1.0 | 0.956 | 1.0 | 1.0 | 0.7253 | 0.7253 |
| sku_order | 1 | 0.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| support | 87 | 0.8372 | 0.6961 | 1.0 | 0.8041 | 0.7586 | 0.6322 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|
| easy | 90 | 0.9956 | 0.9181 | 1.0 | 0.9976 | 1.0 | 0.9667 |
| hard | 96 | 0.9958 | 0.9137 | 1.0 | 0.9985 | 1.0 | 0.8924 |
| medium | 174 | 0.9186 | 0.8251 | 1.0 | 0.902 | 0.7356 | 0.6743 |
| unknown | 6 | 0.6667 | 0.6667 | 0.6667 | 0.6667 | 1.0 | 0.7778 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| aspect_match | 561 | 561 |
| bm25 | 1437 | 1361 |
| dense | 1437 | 1361 |
| entity_match | 1292 | 1224 |
| policy_fallback | 25 | 25 |
| sibling_expansion | 454 | 454 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | aspect_match: 358, bm25: 760, dense: 760, entity_match: 653, sibling_expansion: 251 |
| recommendation | bm25: 343, dense: 343, entity_match: 341 |
| support | aspect_match: 203, bm25: 258, dense: 258, entity_match: 230, policy_fallback: 25, sibling_expansion: 203 |

## Agentic 证据诊断

- 重试率: 0.2705

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 320, refuse: 46 |
| 尝试次数 | 1: 267, 2: 99 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_case_evidence | 15 |
| missing_policy | 51 |
| missing_product_context | 3 |
| missing_structured_entity | 43 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| recommendation | missing_structured_entity: 25 |
| support | missing_case_evidence: 15, missing_policy: 51, missing_product_context: 3, missing_structured_entity: 18 |

## 原始 JSON

```json
{
  "n": 366,
  "retrieval_backend": "qdrant",
  "retrieval_mode": "hybrid_rerank",
  "model_config": {
    "embedding_model": "BAAI/bge-large-en-v1.5",
    "embedding_backend": "sentence-transformers",
    "reranker_model": "BAAI/bge-reranker-large",
    "llm_model": "deepseek-v4-flash"
  },
  "retrieval": {
    "precision@5": 0.9536,
    "recall@5": 0.8686,
    "mrr": 0.9945,
    "ndcg@5": 0.947
  },
  "support_quality": {
    "citation_ok": 0.8743,
    "keyword_coverage": 0.8051,
    "groundedness_proxy": 0.9793
  },
  "latency": {
    "p50_ms": 14528,
    "p95_ms": 41106
  },
  "by_intent": {
    "customer_ops": {
      "n": 187,
      "retrieval": {
        "precision@5": 0.9904,
        "recall@5": 0.9109,
        "mrr": 0.9947,
        "ndcg@5": 0.9927
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.9234,
        "groundedness_proxy": 0.9905
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
        "citation_ok": 0.7253,
        "keyword_coverage": 0.7253,
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
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.3908
      }
    },
    "support": {
      "n": 87,
      "retrieval": {
        "precision@5": 0.8372,
        "recall@5": 0.6961,
        "mrr": 1.0,
        "ndcg@5": 0.8041
      },
      "support_quality": {
        "citation_ok": 0.7586,
        "keyword_coverage": 0.6322,
        "groundedness_proxy": 0.9406
      }
    }
  },
  "by_difficulty": {
    "easy": {
      "n": 90,
      "retrieval": {
        "precision@5": 0.9956,
        "recall@5": 0.9181,
        "mrr": 1.0,
        "ndcg@5": 0.9976
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.9667,
        "groundedness_proxy": 1.0
      }
    },
    "hard": {
      "n": 96,
      "retrieval": {
        "precision@5": 0.9958,
        "recall@5": 0.9137,
        "mrr": 1.0,
        "ndcg@5": 0.9985
      },
      "support_quality": {
        "citation_ok": 1.0,
        "keyword_coverage": 0.8924,
        "groundedness_proxy": 0.987
      }
    },
    "medium": {
      "n": 174,
      "retrieval": {
        "precision@5": 0.9186,
        "recall@5": 0.8251,
        "mrr": 1.0,
        "ndcg@5": 0.902
      },
      "support_quality": {
        "citation_ok": 0.7356,
        "keyword_coverage": 0.6743,
        "groundedness_proxy": 0.9703
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
      "aspect_match": 561,
      "bm25": 1437,
      "dense": 1437,
      "entity_match": 1292,
      "policy_fallback": 25,
      "sibling_expansion": 454
    },
    "relevant_hit_signal_counts": {
      "aspect_match": 561,
      "bm25": 1361,
      "dense": 1361,
      "entity_match": 1224,
      "policy_fallback": 25,
      "sibling_expansion": 454
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "aspect_match": 358,
        "bm25": 760,
        "dense": 760,
        "entity_match": 653,
        "sibling_expansion": 251
      },
      "recommendation": {
        "bm25": 343,
        "dense": 343,
        "entity_match": 341
      },
      "support": {
        "aspect_match": 203,
        "bm25": 258,
        "dense": 258,
        "entity_match": 230,
        "policy_fallback": 25,
        "sibling_expansion": 203
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 320,
      "refuse": 46
    },
    "attempt_counts": {
      "1": 267,
      "2": 99
    },
    "retry_rate": 0.2705,
    "evidence_gap_counts": {
      "missing_case_evidence": 15,
      "missing_policy": 51,
      "missing_product_context": 3,
      "missing_structured_entity": 43
    },
    "evidence_gaps_by_intent": {
      "recommendation": {
        "missing_structured_entity": 25
      },
      "support": {
        "missing_case_evidence": 15,
        "missing_policy": 51,
        "missing_product_context": 3,
        "missing_structured_entity": 18
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
          "bm25_rank": 2,
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
        "review:RV-AMZREV-All_Beauty-01474",
        "review:RV-AMZREV-All_Beauty-01381"
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
        },
        {
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-04607",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:AS-All_Beauty-B005IYYF5E-missing_parts",
        "review:RV-AMZREV-All_Beauty-01858",
        "review:RV-AMZREV-All_Beauty-00034"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04607",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 6,
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
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 34,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01858",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00034",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
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
        "review:RV-AMZREV-All_Beauty-03101",
        "product:PP-All_Beauty-B005XSZS92",
        "review:RV-AMZREV-All_Beauty-01814",
        "review:RV-AMZREV-All_Beauty-03412",
        "review:RV-AMZREV-All_Beauty-00591"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03101",
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
          "doc_id": "product:PP-All_Beauty-B005XSZS92",
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
        "review:RV-AMZREV-All_Beauty-03845",
        "product:PP-All_Beauty-B007VXJK6E",
        "review:AS-All_Beauty-B007VXJK6E-battery_power",
        "review:RV-AMZREV-All_Beauty-02761",
        "review:RV-AMZREV-All_Beauty-02750"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03845",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B007VXJK6E",
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
          "doc_id": "review:AS-All_Beauty-B007VXJK6E-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02761",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02750",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
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
      "query_id": "QS-0037",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04594",
        "product:PP-All_Beauty-B008TGMJQA",
        "review:AS-All_Beauty-B008TGMJQA-quality_damage",
        "review:RV-AMZREV-All_Beauty-03773",
        "review:RV-AMZREV-All_Beauty-02525"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04594",
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
          "doc_id": "review:AS-All_Beauty-B008TGMJQA-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 17,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02525",
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
      "query_id": "QS-0038",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03824",
        "product:PP-All_Beauty-B008TGSAFE",
        "review:AS-All_Beauty-B008TGSAFE-price_value",
        "review:RV-AMZREV-All_Beauty-01994",
        "review:RV-AMZREV-All_Beauty-01780"
      ],
      "signals": [
        {
          "rank": 1,
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
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01994",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01780",
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
        "review:RV-AMZREV-All_Beauty-00109",
        "product:PP-All_Beauty-B0093EQX6Y",
        "review:AS-All_Beauty-B0093EQX6Y-skin_scent",
        "review:RV-AMZREV-All_Beauty-02727",
        "review:RV-AMZREV-All_Beauty-04381"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00109",
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
          "doc_id": "product:PP-All_Beauty-B0093EQX6Y",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02727",
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
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-04408",
        "product:PP-All_Beauty-B00946HGLW",
        "review:AS-All_Beauty-B00946HGLW-skin_scent",
        "review:RV-AMZREV-All_Beauty-01766",
        "review:RV-AMZREV-All_Beauty-03339"
      ],
      "signals": [
        {
          "rank": 1,
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
          "dense_rank": 12,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03339",
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
        "review:RV-AMZREV-All_Beauty-03307",
        "product:PP-All_Beauty-B00A0RUGPM",
        "review:AS-All_Beauty-B00A0RUGPM-skin_scent",
        "review:RV-AMZREV-All_Beauty-04894",
        "review:RV-AMZREV-All_Beauty-02417"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03307",
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
          "doc_id": "product:PP-All_Beauty-B00A0RUGPM",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 8,
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
          "dense_rank": 32,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04894",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 6,
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
        "review:RV-AMZREV-All_Beauty-03325"
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
          "bm25_rank": 8,
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
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03325",
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
        "review:RV-AMZREV-All_Beauty-00897",
        "review:RV-AMZREV-All_Beauty-03607",
        "review:RV-AMZREV-All_Beauty-03644"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03189",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03607",
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
        "review:RV-AMZREV-All_Beauty-04783",
        "review:RV-AMZREV-All_Beauty-00844"
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
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04783",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00844",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
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
      "query_id": "QS-0053",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03899",
        "product:PP-All_Beauty-B00CLXXXH6",
        "review:RV-AMZREV-All_Beauty-00917",
        "review:RV-AMZREV-All_Beauty-04671",
        "review:RV-AMZREV-All_Beauty-04554"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03899",
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
          "doc_id": "product:PP-All_Beauty-B00CLXXXH6",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00917",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04671",
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
        "review:RV-AMZREV-All_Beauty-02660",
        "product:PP-All_Beauty-B00EWUFETQ",
        "review:AS-All_Beauty-B00EWUFETQ-missing_parts",
        "review:RV-AMZREV-All_Beauty-03343",
        "review:RV-AMZREV-All_Beauty-04051"
      ],
      "signals": [
        {
          "rank": 1,
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00EWUFETQ",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03343",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04051",
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
          "bm25_rank": 4,
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
        "review:RV-AMZREV-All_Beauty-03741",
        "product:PP-All_Beauty-B00FQD0LNW",
        "review:AS-All_Beauty-B00FQD0LNW-quality_damage",
        "review:RV-AMZREV-All_Beauty-01283",
        "review:RV-AMZREV-All_Beauty-02361"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03741",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00FQD0LNW",
          "doc_type": "product_profile",
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
          "doc_id": "review:AS-All_Beauty-B00FQD0LNW-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01283",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02361",
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
      "query_id": "QS-0063",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00269",
        "product:PP-All_Beauty-B00G7PCKI2",
        "review:AS-All_Beauty-B00G7PCKI2-skin_scent",
        "review:RV-AMZREV-All_Beauty-02347",
        "review:RV-AMZREV-All_Beauty-03671"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00269",
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
          "bm25_rank": 3,
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
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03671",
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
        "review:RV-AMZREV-All_Beauty-04823",
        "review:RV-AMZREV-All_Beauty-01690"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03302",
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
          "doc_id": "product:PP-All_Beauty-B00G7UFXJA",
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
          "doc_id": "review:AS-All_Beauty-B00G7UFXJA-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04823",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01690",
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
        "review:RV-AMZREV-All_Beauty-04379",
        "product:PP-All_Beauty-B00HA72I8S",
        "review:RV-AMZREV-All_Beauty-00388",
        "review:RV-AMZREV-All_Beauty-04348"
      ],
      "signals": [
        {
          "rank": 1,
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
        "review:RV-AMZREV-All_Beauty-03085",
        "review:RV-AMZREV-All_Beauty-00643"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02027",
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
          "doc_id": "product:PP-All_Beauty-B00IUI0QFS",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03085",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00643",
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
      "query_id": "QS-0070",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04090",
        "product:PP-All_Beauty-B00J2R8BP8",
        "review:AS-All_Beauty-B00J2R8BP8-quality_damage",
        "review:RV-AMZREV-All_Beauty-03700",
        "review:RV-AMZREV-All_Beauty-00165"
      ],
      "signals": [
        {
          "rank": 1,
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
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00J2R8BP8",
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
          "doc_id": "review:AS-All_Beauty-B00J2R8BP8-quality_damage",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03700",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00165",
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
        "review:RV-AMZREV-All_Beauty-01743",
        "product:PP-All_Beauty-B00J7QCNDU",
        "review:AS-All_Beauty-B00J7QCNDU-delivery",
        "review:RV-AMZREV-All_Beauty-04362",
        "review:RV-AMZREV-All_Beauty-01796"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01743",
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
          "doc_id": "product:PP-All_Beauty-B00J7QCNDU",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 45,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00J7QCNDU-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 44,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04362",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01796",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
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
          "bm25_rank": 4,
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
          "bm25_rank": 5,
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
          "bm25_rank": 2,
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
        "review:RV-AMZREV-All_Beauty-02554"
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
          "bm25_rank": 5,
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
          "bm25_rank": 6,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02554",
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
      "query_id": "QS-0076",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01683",
        "product:PP-All_Beauty-B00KCTER3U",
        "review:AS-All_Beauty-B00KCTER3U-skin_scent",
        "review:RV-AMZREV-All_Beauty-01804",
        "review:RV-AMZREV-All_Beauty-04765"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01683",
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
          "doc_id": "product:PP-All_Beauty-B00KCTER3U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B00KCTER3U-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 41,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01804",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04765",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
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
      "query_id": "QS-0077",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01071",
        "product:PP-All_Beauty-B00KH8F5GO",
        "review:RV-AMZREV-All_Beauty-02411"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01071",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 2,
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
        "review:RV-AMZREV-All_Beauty-04235",
        "product:PP-All_Beauty-B00KNIECVC",
        "review:AS-All_Beauty-B00KNIECVC-skin_scent",
        "review:RV-AMZREV-All_Beauty-02603",
        "review:RV-AMZREV-All_Beauty-00106"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04235",
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
          "dense_rank": 7,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02603",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00106",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
        "review:RV-AMZREV-All_Beauty-03597"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04024",
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
          "doc_id": "product:PP-All_Beauty-B00KR4AFJU",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 10,
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
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03597",
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
      "query_id": "QS-0081",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04990",
        "product:PP-All_Beauty-B00KXFD75M",
        "review:AS-All_Beauty-B00KXFD75M-skin_scent",
        "review:RV-AMZREV-All_Beauty-00098",
        "review:RV-AMZREV-All_Beauty-03571"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04990",
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
          "doc_id": "product:PP-All_Beauty-B00KXFD75M",
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
          "doc_id": "review:AS-All_Beauty-B00KXFD75M-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00098",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03571",
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
          "bm25_rank": 3,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02722",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00449",
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
      "query_id": "QS-0083",
      "intent": "recommendation",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04101",
        "product:PP-All_Beauty-B00LHZC4GA",
        "review:AS-All_Beauty-B00LHZC4GA-skin_scent",
        "review:RV-AMZREV-All_Beauty-01835",
        "review:RV-AMZREV-All_Beauty-01708"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04101",
          "doc_type": "review_evidence",
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
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01835",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01708",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
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
          "bm25_rank": 5,
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
          "bm25_rank": 1,
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
          "bm25_rank": 11,
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
          "bm25_rank": 3,
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
        "review:AS-All_Beauty-B00N6WHTRG-quality_damage",
        "review:RV-AMZREV-All_Beauty-00102",
        "review:RV-AMZREV-All_Beauty-03848"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03361",
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
          "doc_id": "review:AS-All_Beauty-B00N6WHTRG-quality_damage",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00102",
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
        "review:RV-AMZREV-All_Beauty-03426",
        "review:RV-AMZREV-All_Beauty-02327"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01000",
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
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03426",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02327",
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
        "review:RV-AMZREV-All_Beauty-02870",
        "review:RV-AMZREV-All_Beauty-02926",
        "review:RV-AMZREV-All_Beauty-02918",
        "review:RV-AMZREV-All_Beauty-02868",
        "review:RV-AMZREV-All_Beauty-02913"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02870",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02926",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02918",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02868",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02913",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 20,
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
          "bm25_rank": 3,
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
          "bm25_rank": 1,
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
          "bm25_rank": 3,
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
        "review:RV-AMZREV-All_Beauty-01196",
        "review:RV-AMZREV-All_Beauty-02738"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
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
          "bm25_rank": 5,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02738",
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
          "bm25_rank": 2,
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
        "review:RV-AMZREV-All_Beauty-01586"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01199",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01586",
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
          "bm25_rank": 2,
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
          "bm25_rank": 1,
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
          "dense_rank": 7,
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
          "bm25_rank": 2,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01589",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01207",
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
          "bm25_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-02483",
        "review:RV-AMZREV-All_Beauty-00015",
        "review:RV-AMZREV-All_Beauty-03222",
        "review:RV-AMZREV-All_Beauty-01497",
        "review:RV-AMZREV-All_Beauty-00284"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02483",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03222",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01497",
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
        "review:RV-AMZREV-All_Beauty-00016",
        "product:PP-All_Beauty-B07W397QG4",
        "review:AS-All_Beauty-B07W397QG4-skin_scent",
        "review:RV-AMZREV-All_Beauty-01229"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00016",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01229",
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
      "query_id": "QS-0106",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02588",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02765",
        "review:RV-AMZREV-All_Beauty-02748",
        "review:RV-AMZREV-All_Beauty-00922"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02748",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00922",
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
          "bm25_rank": 3,
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
          "dense_rank": 38,
          "bm25_rank": 9,
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
        "review:RV-AMZREV-All_Beauty-03685",
        "review:RV-AMZREV-All_Beauty-00019",
        "review:RV-AMZREV-All_Beauty-02446"
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
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03685",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 11,
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
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02446",
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
        "review:RV-AMZREV-All_Beauty-00020",
        "review:AS-All_Beauty-B00JMDPK8S-battery_power"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
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
          "dense_rank": 7,
          "bm25_rank": 6,
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
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00020",
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
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-battery_power",
          "doc_type": "review_aspect_summary",
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
        "review:RV-AMZREV-All_Beauty-04682",
        "review:RV-AMZREV-All_Beauty-02496",
        "review:RV-AMZREV-All_Beauty-04079"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02766",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01617",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04682",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02496",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04079",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
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
      "query_id": "QS-0111",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01737",
        "product:PP-All_Beauty-B082QX2HP6",
        "review:AS-All_Beauty-B082QX2HP6-skin_scent",
        "review:RV-AMZREV-All_Beauty-03894",
        "review:RV-AMZREV-All_Beauty-02990"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01737",
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02990",
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
          "bm25_rank": 1,
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
          "bm25_rank": 7,
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
          "bm25_rank": 3,
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
      "query_id": "QS-0117",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03842",
        "review:RV-AMZREV-All_Beauty-04471",
        "review:RV-AMZREV-All_Beauty-04252",
        "review:RV-AMZREV-All_Beauty-01726",
        "review:RV-AMZREV-All_Beauty-04681"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03842",
          "doc_type": "review_evidence",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04471",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04252",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01726",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04681",
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
        "review:RV-AMZREV-All_Beauty-01766",
        "review:RV-AMZREV-All_Beauty-03339",
        "review:RV-AMZREV-All_Beauty-03730",
        "review:RV-AMZREV-All_Beauty-04653",
        "review:RV-AMZREV-All_Beauty-00030"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01766",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03339",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03730",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04653",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00030",
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
        "review:RV-AMZREV-All_Beauty-04255",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-04266",
        "review:RV-AMZREV-All_Beauty-00032"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04255",
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
          "doc_id": "product:PP-All_Beauty-B0020MKBNW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 6,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04266",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
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
        "review:RV-AMZREV-All_Beauty-02944",
        "review:RV-AMZREV-All_Beauty-03658",
        "review:RV-AMZREV-All_Beauty-00034",
        "review:RV-AMZREV-All_Beauty-03661",
        "review:RV-AMZREV-All_Beauty-04357"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-02944",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03658",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00034",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03661",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04357",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
          "doc_id": "product:PP-All_Beauty-B01M5KNSQN",
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
      "query_id": "QS-0125",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 0.9558295932317544,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00036",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:AS-All_Beauty-B07KDNK11M-skin_scent",
        "review:AS-All_Beauty-B07KDNK11M-price_value",
        "review:AS-All_Beauty-B07KDNK11M-missing_parts"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00036",
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
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 37,
          "bm25_rank": 32,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 34,
          "bm25_rank": 29,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 35,
          "bm25_rank": 33,
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
        "review:RV-AMZREV-All_Beauty-00039",
        "review:RV-AMZREV-All_Beauty-02333",
        "review:RV-AMZREV-All_Beauty-04025",
        "review:RV-AMZREV-All_Beauty-04150"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04430",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00039",
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04025",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-03826",
        "review:RV-AMZREV-All_Beauty-02623",
        "review:RV-AMZREV-All_Beauty-00041",
        "review:RV-AMZREV-All_Beauty-04981",
        "review:RV-AMZREV-All_Beauty-03710"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03826",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02623",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00041",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04981",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-00042",
        "product:PP-All_Beauty-B09FF97RHL",
        "review:RV-AMZREV-All_Beauty-02657"
      ],
      "signals": [
        {
          "rank": 1,
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
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B09FF97RHL",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02657",
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
        "review:RV-AMZREV-All_Beauty-03425",
        "review:RV-AMZREV-All_Beauty-03694",
        "review:RV-AMZREV-All_Beauty-01693",
        "review:RV-AMZREV-All_Beauty-04204",
        "review:RV-AMZREV-All_Beauty-02771"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03425",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03694",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01693",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04204",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02771",
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
        "review:RV-AMZREV-All_Beauty-00050",
        "review:RV-AMZREV-All_Beauty-04988"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-01428",
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
          "doc_id": "product:PP-All_Beauty-B0875V791H",
          "doc_type": "product_profile",
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04988",
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
          "bm25_rank": 3,
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
          "bm25_rank": 2,
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
      "query_id": "QS-0143",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01948",
        "product:PP-All_Beauty-B015RR870U",
        "review:AS-All_Beauty-B015RR870U-delivery",
        "review:RV-AMZREV-All_Beauty-00054",
        "review:RV-AMZREV-All_Beauty-02401"
      ],
      "signals": [
        {
          "rank": 1,
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
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B015RR870U",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B015RR870U-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 55,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00054",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02401",
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
          "dense_rank": 5,
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
          "bm25_rank": 1,
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
          "dense_rank": 35,
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
          "doc_id": "product:PP-All_Beauty-B00C0YZBJE",
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
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 58,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00056",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04676",
          "doc_type": "review_evidence",
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
        "review:RV-AMZREV-All_Beauty-04370"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04370",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00410",
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
        "review:RV-AMZREV-All_Beauty-01148",
        "product:PP-All_Beauty-B09KT4RJG6",
        "review:AS-All_Beauty-B09KT4RJG6-skin_scent",
        "review:RV-AMZREV-All_Beauty-00060"
      ],
      "signals": [
        {
          "rank": 1,
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
        },
        {
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B09KT4RJG6",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00060",
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
          "dense_rank": 23,
          "bm25_rank": 21,
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
          "dense_rank": 11,
          "bm25_rank": 3,
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
          "bm25_rank": 3,
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
          "bm25_rank": 4,
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
          "bm25_rank": 8,
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
          "bm25_rank": 6,
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
          "bm25_rank": 3,
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
          "dense_rank": 6,
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
          "bm25_rank": 6,
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
          "bm25_rank": 3,
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
          "dense_rank": 6,
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
      "query_id": "QS-0159",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04940",
        "product:PP-All_Beauty-B08FRQGYDF",
        "review:AS-All_Beauty-B08FRQGYDF-delivery",
        "review:RV-AMZREV-All_Beauty-00070",
        "review:RV-AMZREV-All_Beauty-04516"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04940",
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
          "doc_id": "product:PP-All_Beauty-B08FRQGYDF",
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
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-delivery",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00070",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04516",
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
        "review:RV-AMZREV-All_Beauty-02337"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00071",
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
          "bm25_rank": 7,
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
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02337",
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
      "query_id": "QS-0161",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-04968",
        "product:PP-All_Beauty-B085NYYLQ8",
        "review:AS-All_Beauty-B085NYYLQ8-price_value",
        "review:RV-AMZREV-All_Beauty-00072",
        "review:RV-AMZREV-All_Beauty-01495"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-04968",
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
          "doc_id": "product:PP-All_Beauty-B085NYYLQ8",
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
          "doc_id": "review:AS-All_Beauty-B085NYYLQ8-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 59,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00072",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01495",
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
          "bm25_rank": 2,
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
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
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
        "review:RV-AMZREV-All_Beauty-00075",
        "product:PP-All_Beauty-B087D7MVHB",
        "review:AS-All_Beauty-B087D7MVHB-price_value",
        "review:RV-AMZREV-All_Beauty-02757",
        "review:AS-All_Beauty-B087D7MVHB-skin_scent"
      ],
      "signals": [
        {
          "rank": 1,
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
        },
        {
          "rank": 4,
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
          "rank": 5,
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
          "dense_rank": 10,
          "bm25_rank": 4,
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
          "bm25_rank": 5,
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
          "bm25_rank": 2,
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
      "query_id": "QS-0167",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03385",
        "product:PP-All_Beauty-B082NKQ4ZT",
        "review:AS-All_Beauty-B082NKQ4ZT-skin_scent",
        "review:RV-AMZREV-All_Beauty-00078"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03385",
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
          "dense_rank": 9,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
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
        "review:RV-AMZREV-All_Beauty-01709",
        "product:PP-All_Beauty-B084D86YL8",
        "review:AS-All_Beauty-B084D86YL8-skin_scent",
        "review:RV-AMZREV-All_Beauty-02758",
        "review:RV-AMZREV-All_Beauty-00079"
      ],
      "signals": [
        {
          "rank": 1,
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
          "bm25_rank": 1,
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
          "bm25_rank": 4,
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
          "bm25_rank": 3,
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
        "review:RV-AMZREV-All_Beauty-04294",
        "review:RV-AMZREV-All_Beauty-01335",
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
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04294",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01335",
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
        "review:RV-AMZREV-All_Beauty-00330",
        "review:RV-AMZREV-All_Beauty-01704",
        "review:RV-AMZREV-All_Beauty-04500",
        "review:RV-AMZREV-All_Beauty-02672",
        "review:RV-AMZREV-All_Beauty-01402"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00330",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01704",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04500",
          "doc_type": "review_evidence",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02672",
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
        "review:RV-AMZREV-All_Beauty-03200",
        "product:PP-All_Beauty-B077YR3333",
        "review:AS-All_Beauty-B077YR3333-skin_scent",
        "review:RV-AMZREV-All_Beauty-00087",
        "review:RV-AMZREV-All_Beauty-01576"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03200",
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
          "doc_id": "product:PP-All_Beauty-B077YR3333",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00087",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01576",
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
      "query_id": "QS-0176",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-01403",
        "review:RV-AMZREV-All_Beauty-01259",
        "review:RV-AMZREV-All_Beauty-01649",
        "review:RV-AMZREV-All_Beauty-00088",
        "review:RV-AMZREV-All_Beauty-03316"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01259",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01649",
          "doc_type": "review_evidence",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00088",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03316",
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
      "query_id": "QS-0177",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-00089",
        "product:PP-All_Beauty-B07KV31WDS",
        "review:AS-All_Beauty-B07KV31WDS-skin_scent",
        "review:RV-AMZREV-All_Beauty-04887"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00089",
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
          "doc_id": "product:PP-All_Beauty-B07KV31WDS",
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
          "doc_id": "review:AS-All_Beauty-B07KV31WDS-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
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
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02765",
        "review:RV-AMZREV-All_Beauty-02748",
        "review:RV-AMZREV-All_Beauty-00922"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02748",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00922",
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
      "query_id": "QS-0179",
      "intent": "customer_ops",
      "difficulty": "easy",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-03501",
        "product:PP-All_Beauty-B071R2QPF3",
        "review:AS-All_Beauty-B071R2QPF3-skin_scent",
        "review:RV-AMZREV-All_Beauty-04979",
        "review:RV-AMZREV-All_Beauty-00091"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-03501",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00091",
          "doc_type": "review_evidence",
          "relevant": true,
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
        "review:RV-AMZREV-All_Beauty-01261",
        "review:RV-AMZREV-All_Beauty-01506"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-All_Beauty-00092",
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
          "doc_id": "product:PP-All_Beauty-B01KJPFO9W",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01261",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01506",
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
        "review:RV-AMZREV-All_Beauty-02896"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 53,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02899",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
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
          "dense_rank": 89,
          "bm25_rank": 89,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02922",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 39,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02896",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 67,
          "bm25_rank": 66,
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
      "query_id": "QS-0182",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00YQ6X8EO-price_value",
        "review:RV-AMZREV-All_Beauty-02902",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02897",
        "review:RV-AMZREV-All_Beauty-02892"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 90,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02902",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 30,
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
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 88,
          "bm25_rank": 89,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02897",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 73,
          "bm25_rank": 65,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02892",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
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
        "review:RV-AMZREV-All_Beauty-02922",
        "review:RV-AMZREV-All_Beauty-02886"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 78,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02899",
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
          "dense_rank": 89,
          "bm25_rank": 88,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02922",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 30,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02886",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
      "query_id": "QS-0184",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:RV-AMZREV-All_Beauty-02916",
        "product:PP-All_Beauty-B00YQ6X8EO",
        "review:RV-AMZREV-All_Beauty-02902",
        "review:RV-AMZREV-All_Beauty-02932",
        "review:RV-AMZREV-All_Beauty-02931"
      ],
      "signals": [
        {
          "rank": 1,
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B00YQ6X8EO",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 88,
          "bm25_rank": 88,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02902",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 27,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02932",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 49,
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
          "dense_rank": 78,
          "bm25_rank": 72,
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
        "review:RV-AMZREV-All_Beauty-02259",
        "review:RV-AMZREV-All_Beauty-02887"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 71,
          "bm25_rank": 37,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02904",
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
          "dense_rank": 89,
          "bm25_rank": 90,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02259",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 26,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02887",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 64,
          "bm25_rank": 46,
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
        "review:RV-AMZREV-All_Beauty-02225",
        "product:PP-All_Beauty-B081TJ8YS3",
        "review:RV-AMZREV-All_Beauty-02781",
        "review:RV-AMZREV-All_Beauty-02778"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B081TJ8YS3-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 16,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02781",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02778",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
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
      "query_id": "QS-0187",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08P2DZB4X-battery_power",
        "review:RV-AMZREV-All_Beauty-04952",
        "product:PP-All_Beauty-B08P2DZB4X",
        "review:RV-AMZREV-All_Beauty-03160"
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08P2DZB4X",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
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
        "review:RV-AMZREV-All_Beauty-03160",
        "review:RV-AMZREV-All_Beauty-01196"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08P2DZB4X-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01196",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
      "query_id": "QS-0189",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07RBSLNFR-price_value",
        "review:RV-AMZREV-All_Beauty-01586",
        "product:PP-All_Beauty-B07RBSLNFR",
        "review:RV-AMZREV-All_Beauty-00662"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00662",
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
      "query_id": "QS-0190",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07RBSLNFR-skin_scent",
        "review:RV-AMZREV-All_Beauty-00009",
        "product:PP-All_Beauty-B07RBSLNFR",
        "review:RV-AMZREV-All_Beauty-01199",
        "review:RV-AMZREV-All_Beauty-00662"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00009",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
        "review:RV-AMZREV-All_Beauty-01337",
        "product:PP-All_Beauty-B07SLFWZKN",
        "review:RV-AMZREV-All_Beauty-00010",
        "review:RV-AMZREV-All_Beauty-02391"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
          "doc_type": "review_aspect_summary",
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
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01337",
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
          "doc_id": "product:PP-All_Beauty-B07SLFWZKN",
          "doc_type": "product_profile",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00010",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02391",
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
        "review:RV-AMZREV-All_Beauty-04959",
        "product:PP-All_Beauty-B08GLG6W8T",
        "review:RV-AMZREV-All_Beauty-00012",
        "review:RV-AMZREV-All_Beauty-01589"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08GLG6W8T-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04959",
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
          "doc_id": "product:PP-All_Beauty-B08GLG6W8T",
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
          "rank": 4,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01589",
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
        "review:RV-AMZREV-All_Beauty-02483",
        "product:PP-All_Beauty-B07KG1TWP5",
        "review:RV-AMZREV-All_Beauty-00552"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KG1TWP5-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02483",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-00016",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00016",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01155",
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
      "query_id": "QS-0196",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-missing_parts",
        "review:RV-AMZREV-All_Beauty-03440",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-00090"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-missing_parts",
          "doc_type": "review_aspect_summary",
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
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03440",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 1,
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
      "query_id": "QS-0197",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-quality_damage",
        "review:RV-AMZREV-All_Beauty-02765",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-00090"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
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
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 17,
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
          "dense_rank": 3,
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
      "query_id": "QS-0198",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07GDQPG12-skin_scent",
        "review:RV-AMZREV-All_Beauty-02765",
        "product:PP-All_Beauty-B07GDQPG12",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-00017"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
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
          "doc_id": "product:PP-All_Beauty-B07GDQPG12",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 1,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00017",
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
        "review:RV-AMZREV-All_Beauty-03685",
        "product:PP-All_Beauty-B01M7UMAUG",
        "review:RV-AMZREV-All_Beauty-02100",
        "review:RV-AMZREV-All_Beauty-02446"
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B01M7UMAUG",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02446",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 67,
          "bm25_rank": 54,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00019",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
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
      "query_id": "QS-0201",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B01M7UMAUG-price_value",
        "review:RV-AMZREV-All_Beauty-01297",
        "product:PP-All_Beauty-B01M7UMAUG",
        "review:RV-AMZREV-All_Beauty-03370",
        "review:RV-AMZREV-All_Beauty-00159"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01297",
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
          "doc_id": "product:PP-All_Beauty-B01M7UMAUG",
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
          "rank": 4,
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
        },
        {
          "rank": 5,
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
        "review:RV-AMZREV-All_Beauty-02637",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:RV-AMZREV-All_Beauty-03393"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00JMDPK8S-battery_power",
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
          "rank": 2,
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
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
      "query_id": "QS-0203",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B00JMDPK8S-price_value",
        "review:RV-AMZREV-All_Beauty-02637",
        "product:PP-All_Beauty-B00JMDPK8S",
        "review:RV-AMZREV-All_Beauty-03393"
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B00JMDPK8S",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02496",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 2,
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
          "bm25_rank": 21,
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
        "review:RV-AMZREV-All_Beauty-01628"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07ZJKVVLW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02135",
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
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 21,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01628",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 22,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02135",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01769",
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
          "dense_rank": 31,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04079",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07ZJKVVLW",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 28,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04575",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 20,
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
      "query_id": "QS-0210",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B083BDVS36-delivery",
        "review:RV-AMZREV-All_Beauty-03499",
        "product:PP-All_Beauty-B083BDVS36",
        "review:RV-AMZREV-All_Beauty-03256"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B083BDVS36-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03499",
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
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03256",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
          "doc_id": "product:PP-All_Beauty-B083BDVS36",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 12,
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
      "query_id": "QS-0212",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B09FP8PP2K-price_value",
        "review:RV-AMZREV-All_Beauty-04724",
        "product:PP-All_Beauty-B09FP8PP2K",
        "review:RV-AMZREV-All_Beauty-02557",
        "review:RV-AMZREV-All_Beauty-00028"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04724",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 24,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B09FP8PP2K",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02557",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
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
          "dense_rank": 32,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03842",
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
          "doc_id": "product:PP-All_Beauty-B09FP8PP2K",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 21,
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
        "review:RV-AMZREV-All_Beauty-03767",
        "product:PP-All_Beauty-B09FP8PP2K",
        "review:RV-AMZREV-All_Beauty-01726",
        "review:RV-AMZREV-All_Beauty-03993"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 29,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03767",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 26,
          "bm25_rank": 29,
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
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01726",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03993",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 33,
          "bm25_rank": 26,
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
        "review:RV-AMZREV-All_Beauty-03730"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00946HGLW-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-03339",
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
          "doc_id": "product:PP-All_Beauty-B00946HGLW",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04408",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03730",
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
      "query_id": "QS-0216",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-04255",
        "product:PP-All_Beauty-B0020MKBNW",
        "review:RV-AMZREV-All_Beauty-00032",
        "review:RV-AMZREV-All_Beauty-01976"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0020MKBNW",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00032",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01976",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0217",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B005IYYF5E-missing_parts",
        "review:RV-AMZREV-All_Beauty-02944",
        "product:PP-All_Beauty-B005IYYF5E",
        "review:RV-AMZREV-All_Beauty-02077",
        "review:RV-AMZREV-All_Beauty-01858"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 22,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02944",
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
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02077",
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01858",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 11,
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
        "review:RV-AMZREV-All_Beauty-04357",
        "review:RV-AMZREV-All_Beauty-01829"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 39,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04066",
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
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04357",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01829",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02519",
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
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 8,
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
        "review:RV-AMZREV-All_Beauty-02944",
        "review:RV-AMZREV-All_Beauty-02203"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B005IYYF5E-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 47,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04576",
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B005IYYF5E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 31,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02944",
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02203",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
      "query_id": "QS-0221",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-missing_parts",
        "review:RV-AMZREV-All_Beauty-03109",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-04479",
        "review:RV-AMZREV-All_Beauty-00111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 28,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03109",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 33,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 23,
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
        "review:RV-AMZREV-All_Beauty-03708",
        "review:RV-AMZREV-All_Beauty-00111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-price_value",
          "doc_type": "review_aspect_summary",
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
          "dense_rank": 22,
          "bm25_rank": 33,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03708",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 27,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 23,
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
          "dense_rank": 36,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02728",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 33,
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
          "dense_rank": 30,
          "bm25_rank": 25,
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
      "query_id": "QS-0224",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07KDNK11M-skin_scent",
        "review:RV-AMZREV-All_Beauty-04011",
        "product:PP-All_Beauty-B07KDNK11M",
        "review:RV-AMZREV-All_Beauty-03754",
        "review:RV-AMZREV-All_Beauty-03809"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 29,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04011",
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07KDNK11M",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 32,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03754",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03809",
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
          "dense_rank": 19,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03968",
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
          "doc_id": "product:PP-All_Beauty-B07H281V4V",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 10,
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
          "dense_rank": 22,
          "bm25_rank": 21,
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
      "query_id": "QS-0226",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-missing_parts",
        "review:RV-AMZREV-All_Beauty-01861",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-02007"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01861",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02007",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
      "query_id": "QS-0227",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-price_value",
        "review:RV-AMZREV-All_Beauty-04207",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-00045"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-price_value",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00045",
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
      "query_id": "QS-0228",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07CJWG8SP-quality_damage",
        "review:RV-AMZREV-All_Beauty-01693",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-03525",
        "review:RV-AMZREV-All_Beauty-03425"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-quality_damage",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-01693",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
          "dense_rank": 21,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03525",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 10,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03425",
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
        "review:RV-AMZREV-All_Beauty-01861",
        "product:PP-All_Beauty-B07CJWG8SP",
        "review:RV-AMZREV-All_Beauty-02771"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07CJWG8SP-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01861",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B07CJWG8SP",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 22,
          "bm25_rank": 19,
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
      "query_id": "QS-0230",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0875V791H-skin_scent",
        "review:RV-AMZREV-All_Beauty-02001",
        "product:PP-All_Beauty-B0875V791H",
        "review:RV-AMZREV-All_Beauty-01661",
        "review:RV-AMZREV-All_Beauty-01428"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0875V791H-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0875V791H",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01661",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01428",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
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
      "query_id": "QS-0231",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B07LBK2YQX-skin_scent",
        "review:RV-AMZREV-All_Beauty-00051",
        "product:PP-All_Beauty-B07LBK2YQX",
        "review:RV-AMZREV-All_Beauty-00710"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00051",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00710",
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
          "dense_rank": 19,
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
          "bm25_rank": 3,
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
          "dense_rank": 13,
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
      "query_id": "QS-0233",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B015RR870U-price_value",
        "review:RV-AMZREV-All_Beauty-02401",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-01642",
        "review:RV-AMZREV-All_Beauty-03290"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B015RR870U-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 26,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02401",
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
          "bm25_rank": 3,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03290",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 20,
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
      "query_id": "QS-0234",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B015RR870U-skin_scent",
        "review:RV-AMZREV-All_Beauty-02323",
        "product:PP-All_Beauty-B015RR870U",
        "review:RV-AMZREV-All_Beauty-01642",
        "review:RV-AMZREV-All_Beauty-01948"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B015RR870U-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 39,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02323",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
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
          "dense_rank": 31,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01948",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
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
          "dense_rank": 16,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B000OQFVLS",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02412",
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
        "review:RV-AMZREV-All_Beauty-03035",
        "review:RV-AMZREV-All_Beauty-04783"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B00C0YZBJE-skin_scent",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00844",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
          "doc_id": "product:PP-All_Beauty-B00C0YZBJE",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03035",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 34,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04783",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
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
        "review:RV-AMZREV-All_Beauty-00058",
        "product:PP-All_Beauty-B0B4JP5YD9",
        "review:RV-AMZREV-All_Beauty-00410"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00058",
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
        "review:RV-AMZREV-All_Beauty-00059",
        "product:PP-All_Beauty-B0B4JPGX8P",
        "review:RV-AMZREV-All_Beauty-01549"
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
          "bm25_rank": 2,
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
        "review:RV-AMZREV-All_Beauty-04004"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04004",
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
        "review:RV-AMZREV-All_Beauty-00064",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-02014"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
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
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02014",
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
        "review:RV-AMZREV-All_Beauty-00998",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-01959",
        "review:RV-AMZREV-All_Beauty-03521"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 18,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00998",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 20,
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01959",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03521",
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
      "query_id": "QS-0245",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.625,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B0BTJ6SYKB-skin_scent",
        "review:RV-AMZREV-All_Beauty-03276",
        "product:PP-All_Beauty-B0BTJ6SYKB",
        "review:RV-AMZREV-All_Beauty-01341",
        "review:RV-AMZREV-All_Beauty-00064"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 17,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03276",
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
          "doc_id": "product:PP-All_Beauty-B0BTJ6SYKB",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01341",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00064",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00065",
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
      "query_id": "QS-0247",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-All_Beauty-B08KWN77LW-skin_scent",
        "review:RV-AMZREV-All_Beauty-01421",
        "product:PP-All_Beauty-B08KWN77LW",
        "review:RV-AMZREV-All_Beauty-01594",
        "review:RV-AMZREV-All_Beauty-00941"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08KWN77LW-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 4,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01421",
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
          "doc_id": "product:PP-All_Beauty-B08KWN77LW",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01594",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00941",
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
        "review:RV-AMZREV-All_Beauty-02548",
        "product:PP-All_Beauty-B08HXQ3T9K",
        "review:RV-AMZREV-All_Beauty-00067"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B08HXQ3T9K-skin_scent",
          "doc_type": "review_aspect_summary",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-02548",
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
        "review:RV-AMZREV-All_Beauty-01306",
        "product:PP-All_Beauty-B0B2L218H2",
        "review:RV-AMZREV-All_Beauty-04963",
        "review:RV-AMZREV-All_Beauty-01490"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01306",
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
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B0B2L218H2",
          "doc_type": "product_profile",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04963",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 8,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01490",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
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
        "review:RV-AMZREV-All_Beauty-02337",
        "product:PP-All_Beauty-B08BZ1RHPS",
        "review:RV-AMZREV-All_Beauty-01603"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02337",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01603",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
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
      "query_id": "QS-0253",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-battery_power",
        "review:AS-All_Beauty-B013HR1A92-battery_power",
        "review:RV-AMZREV-All_Beauty-00342",
        "review:RV-AMZREV-All_Beauty-04060",
        "review:AS-All_Beauty-B07H8Y5QT2-battery_power"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B013HR1A92-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 28,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00342",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 60,
          "bm25_rank": 34,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04060",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 67,
          "bm25_rank": 82,
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
          "dense_rank": 59,
          "bm25_rank": 48,
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
      "query_id": "QS-0254",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-delivery",
        "review:AS-All_Beauty-B06Y44MMT6-delivery",
        "review:RV-AMZREV-All_Beauty-01793",
        "review:AS-All_Beauty-B00YQ6X8EO-delivery",
        "review:RV-AMZREV-All_Beauty-00304"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-delivery",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B06Y44MMT6-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01793",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B00YQ6X8EO-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 61,
          "bm25_rank": 33,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00304",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 46,
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
          "dense_rank": 1,
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
        "review:AS-All_Beauty-B07C533XCW-missing_parts",
        "review:RV-AMZREV-All_Beauty-01407",
        "review:AS-All_Beauty-B078Z6MGVW-missing_parts",
        "ticket:FAQ-All_Beauty-0169"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B07C533XCW-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01407",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 58,
          "bm25_rank": 68,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B078Z6MGVW-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 46,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-All_Beauty-0169",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 78,
          "bm25_rank": 83,
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
        "review:AS-All_Beauty-B01BZVADRW-price_value",
        "review:RV-AMZREV-All_Beauty-01538",
        "review:RV-AMZREV-All_Beauty-04992",
        "review:RV-AMZREV-All_Beauty-04457"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-price_value",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01BZVADRW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01538",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 48,
          "bm25_rank": 81,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04992",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 39,
          "bm25_rank": 64,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04457",
          "doc_type": "review_evidence",
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
      "query_id": "QS-0258",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-quality_damage",
        "review:AS-All_Beauty-B01BZVADRW-quality_damage",
        "review:RV-AMZREV-All_Beauty-01379",
        "review:RV-AMZREV-All_Beauty-03752",
        "review:RV-AMZREV-All_Beauty-04188"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B01BZVADRW-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 10,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01379",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 13,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03752",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 21,
          "bm25_rank": 63,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04188",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 48,
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
      "query_id": "QS-0259",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-All_Beauty-refund_return",
        "review:AS-All_Beauty-B013HR1A92-refund_return",
        "review:RV-AMZREV-All_Beauty-04457",
        "review:RV-AMZREV-All_Beauty-03485",
        "review:RV-AMZREV-All_Beauty-04260"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-All_Beauty-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-All_Beauty-B013HR1A92-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04457",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03485",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 50,
          "bm25_rank": 62,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04260",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 70,
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
        "review:AS-All_Beauty-B07VDCD17L-skin_scent",
        "review:RV-AMZREV-All_Beauty-04431",
        "review:RV-AMZREV-All_Beauty-01125",
        "review:RV-AMZREV-All_Beauty-02431",
        "review:RV-AMZREV-All_Beauty-02741"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B07VDCD17L-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 33,
          "bm25_rank": 24,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-04431",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 50,
          "bm25_rank": 76,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01125",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02431",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 57,
          "bm25_rank": 80,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02741",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 12,
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
      "query_id": "QS-0261",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-battery_power",
        "review:AS-Baby_Products-B00HHRH07U-battery_power",
        "review:RV-AMZREV-Baby_Products-02005",
        "review:RV-AMZREV-Baby_Products-01944",
        "review:RV-AMZREV-Baby_Products-03860"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B00HHRH07U-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 45,
          "bm25_rank": 76,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01944",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-03860",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
          "bm25_rank": 35,
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
      "query_id": "QS-0262",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:AS-Baby_Products-B08V1NQ2KY-delivery",
        "review:RV-AMZREV-Baby_Products-00829",
        "review:AS-Baby_Products-B0771VPLSX-delivery",
        "review:AS-Baby_Products-B07SK9SG15-delivery",
        "review:AS-Baby_Products-B08W7VYTH2-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-Baby_Products-B08V1NQ2KY-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 56,
          "bm25_rank": 38,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-00829",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 65,
          "bm25_rank": 62,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:AS-Baby_Products-B0771VPLSX-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 27,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B07SK9SG15-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 41,
          "bm25_rank": 35,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Baby_Products-B08W7VYTH2-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 55,
          "bm25_rank": 40,
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
          "dense_rank": 1,
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
        "review:AS-Baby_Products-B0BB84JXS9-missing_parts",
        "review:RV-AMZREV-Baby_Products-03232",
        "review:RV-AMZREV-Baby_Products-03070",
        "ticket:FAQ-Baby_Products-0119"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 1,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BB84JXS9-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 37,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-03232",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 24,
          "bm25_rank": 57,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-03070",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0119",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 23,
          "bm25_rank": 22,
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
      "query_id": "QS-0265",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-price_value",
        "review:AS-Baby_Products-B0BW7CVB9K-price_value",
        "review:RV-AMZREV-Baby_Products-00273",
        "review:RV-AMZREV-Baby_Products-01756",
        "review:RV-AMZREV-Baby_Products-00228"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-price_value",
          "doc_type": "complaint_cluster",
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
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0BW7CVB9K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 72,
          "bm25_rank": 57,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-00273",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 42,
          "bm25_rank": 73,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01756",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 37,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-00228",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 48,
          "bm25_rank": 77,
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
      "query_id": "QS-0266",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-quality_damage",
        "review:AS-Baby_Products-B000IDSLOG-quality_damage",
        "review:RV-AMZREV-Baby_Products-01255",
        "review:RV-AMZREV-Baby_Products-02041",
        "ticket:FAQ-Baby_Products-0036"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B000IDSLOG-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 32,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01255",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 29,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-02041",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 42,
          "bm25_rank": 68,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0036",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 41,
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
      "query_id": "QS-0267",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-refund_return",
        "review:AS-Baby_Products-B0C9R9WP93-refund_return",
        "review:RV-AMZREV-Baby_Products-01255",
        "review:RV-AMZREV-Baby_Products-02481",
        "ticket:FAQ-Baby_Products-0125"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B0C9R9WP93-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 58,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-01255",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-02481",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 44,
          "bm25_rank": 71,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0125",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 59,
          "bm25_rank": 27,
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
      "query_id": "QS-0268",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Baby_Products-skin_scent",
        "review:AS-Baby_Products-B07S76MGJJ-skin_scent",
        "review:RV-AMZREV-Baby_Products-02363",
        "review:RV-AMZREV-Baby_Products-01823",
        "review:RV-AMZREV-Baby_Products-03005"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Baby_Products-skin_scent",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Baby_Products-B07S76MGJJ-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02363",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 28,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Baby_Products-01823",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
          "bm25_rank": 54,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-03005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 35,
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
      "query_id": "QS-0269",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-battery_power",
        "review:AS-Software-B07T771SPH-battery_power",
        "review:RV-AMZREV-Software-00084",
        "review:RV-AMZREV-Software-03363",
        "review:RV-AMZREV-Software-03596"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-battery_power",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B07T771SPH-battery_power",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00084",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-03363",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Software-03596",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 16,
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
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-delivery",
        "review:AS-Software-B00YHZVOCW-delivery",
        "review:RV-AMZREV-Software-02973",
        "review:AS-Software-B09CDNC28X-delivery",
        "review:AS-Software-B00FAPF5U0-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-delivery",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 36,
          "bm25_rank": 40,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00YHZVOCW-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-02973",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 61,
          "bm25_rank": 52,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B09CDNC28X-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B00FAPF5U0-delivery",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 33,
          "bm25_rank": 25,
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
      "query_id": "QS-0271",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8539316501572937,
      "retrieved": [
        "review:CL-Software-digital_license",
        "review:AS-Software-B0094BB4TW-digital_license",
        "review:RV-AMZREV-Software-03901",
        "review:R-005",
        "review:AS-Software-B008Z2NVGK-digital_license"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-digital_license",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 8,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B0094BB4TW-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-03901",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 34,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 32,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B008Z2NVGK-digital_license",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 21,
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
          "dense_rank": 15,
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
      "query_id": "QS-0273",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-missing_parts",
        "review:AS-Software-B00E5NGYVM-missing_parts",
        "review:RV-AMZREV-Software-04324",
        "review:AS-Software-B004FRX0MY-missing_parts",
        "review:AS-Software-B00IG2DOKM-missing_parts"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-missing_parts",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00E5NGYVM-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-04324",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 2,
          "bm25_rank": 7,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B004FRX0MY-missing_parts",
          "doc_type": "review_aspect_summary",
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
          "rank": 5,
          "doc_id": "review:AS-Software-B00IG2DOKM-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 19,
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
      "query_id": "QS-0274",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-price_value",
        "review:AS-Software-B00XZFCVK4-price_value",
        "review:RV-AMZREV-Software-00731",
        "review:AS-Software-B0094BB4TW-price_value",
        "review:AS-Software-B00992CF6W-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-price_value",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00XZFCVK4-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 11,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00731",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B0094BB4TW-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 12,
          "bm25_rank": 16,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B00992CF6W-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 5,
          "bm25_rank": 6,
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
      "query_id": "QS-0275",
      "intent": "customer_ops",
      "difficulty": "hard",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "review:CL-Software-quality_damage",
        "review:AS-Software-B0094BB4TW-quality_damage",
        "review:RV-AMZREV-Software-00382",
        "review:AS-Software-B0066TUXU6-quality_damage",
        "ticket:FAQ-Software-0107"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-quality_damage",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B0094BB4TW-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-00382",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 35,
          "bm25_rank": 72,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Software-B0066TUXU6-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0107",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 16,
          "bm25_rank": 14,
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
        "review:RV-AMZREV-Software-04344",
        "review:RV-AMZREV-Software-04977",
        "review:AS-Software-B0066TUXU6-refund_return"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:CL-Software-refund_return",
          "doc_type": "complaint_cluster",
          "relevant": true,
          "dense_rank": 15,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:AS-Software-B00YHZVOCW-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Software-04344",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 4,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-Software-04977",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 36,
          "signals": [
            "dense",
            "bm25",
            "aspect_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:AS-Software-B0066TUXU6-refund_return",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 67,
          "bm25_rank": 23,
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
      "query_id": "QS-0277",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0001",
        "review:RV-AMZREV-All_Beauty-00005",
        "review:RV-AMZREV-All_Beauty-02240",
        "review:RV-AMZREV-All_Beauty-03336"
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
          "rank": 3,
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
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03336",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0278",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.5531464700081437,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0002",
        "review:RV-AMZREV-All_Beauty-00006",
        "review:RV-AMZREV-All_Beauty-03160",
        "review:RV-AMZREV-All_Beauty-02738",
        "review:RV-AMZREV-All_Beauty-01196"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00006",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03160",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02738",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01196",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 8,
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
      "query_id": "QS-0279",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0003",
        "review:RV-AMZREV-All_Beauty-00008"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0003",
          "doc_type": "faq_case",
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
          "rank": 2,
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
        "review:RV-AMZREV-All_Beauty-00010",
        "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
        "review:RV-AMZREV-All_Beauty-02391",
        "review:RV-AMZREV-All_Beauty-01337"
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07SLFWZKN-skin_scent",
          "doc_type": "review_aspect_summary",
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
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02391",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01337",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 9,
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
      "query_id": "QS-0281",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0005",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00012",
        "review:RV-AMZREV-All_Beauty-01207",
        "review:RV-AMZREV-All_Beauty-04959"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 20,
          "bm25_rank": 15,
          "signals": [
            "dense",
            "bm25",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01207",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04959",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0282",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0006",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00013",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00424",
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0283",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0007",
        "review:RV-AMZREV-All_Beauty-00018",
        "review:RV-AMZREV-All_Beauty-01546",
        "review:RV-AMZREV-All_Beauty-01555",
        "review:RV-AMZREV-All_Beauty-01157"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01546",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01555",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01157",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0284",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0008",
        "review:RV-AMZREV-All_Beauty-03370",
        "review:AS-All_Beauty-B01M7UMAUG-delivery",
        "review:RV-AMZREV-All_Beauty-00019",
        "review:RV-AMZREV-All_Beauty-00159"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03370",
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
          "doc_id": "review:AS-All_Beauty-B01M7UMAUG-delivery",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00019",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00159",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0285",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0009",
        "review:RV-AMZREV-All_Beauty-00020",
        "review:AS-All_Beauty-B00JMDPK8S-quality_damage",
        "review:RV-AMZREV-All_Beauty-02637",
        "review:RV-AMZREV-All_Beauty-03393"
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02637",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-03393",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
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
      "query_id": "QS-0286",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0010",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00023",
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
      "query_id": "QS-0287",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6666666666666666,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0011",
        "review:RV-AMZREV-All_Beauty-00024",
        "review:RV-AMZREV-All_Beauty-01901"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01901",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0288",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0012",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00026",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04511",
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
      "query_id": "QS-0289",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6,
      "recall@5": 0.6,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0013",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00027",
        "review:RV-AMZREV-All_Beauty-02667",
        "review:RV-AMZREV-All_Beauty-04501"
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
          "dense_rank": 39,
          "bm25_rank": 27,
          "signals": [
            "dense",
            "bm25",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02667",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04501",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 14,
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
      "query_id": "QS-0290",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0014",
        "review:RV-AMZREV-All_Beauty-04724",
        "review:AS-All_Beauty-B09FP8PP2K-price_value",
        "review:RV-AMZREV-All_Beauty-02557",
        "review:RV-AMZREV-All_Beauty-00028"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0014",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 12,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04724",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 31,
          "bm25_rank": 38,
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
          "doc_id": "review:AS-All_Beauty-B09FP8PP2K-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02557",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00028",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 30,
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
      "query_id": "QS-0291",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0015",
        "review:RV-AMZREV-All_Beauty-00029"
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
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0016",
        "review:RV-AMZREV-All_Beauty-00031",
        "review:RV-AMZREV-All_Beauty-02111"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0016",
          "doc_type": "faq_case",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00031",
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
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0017",
        "review:RV-AMZREV-All_Beauty-04255",
        "review:AS-All_Beauty-B0020MKBNW-delivery",
        "review:RV-AMZREV-All_Beauty-00032",
        "review:RV-AMZREV-All_Beauty-04266"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04255",
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
          "doc_id": "review:AS-All_Beauty-B0020MKBNW-delivery",
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
          "rank": 4,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04266",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0294",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0018",
        "review:RV-AMZREV-All_Beauty-00035"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0295",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0019",
        "review:RV-AMZREV-All_Beauty-00036",
        "ticket:FAQ-All_Beauty-0042",
        "review:RV-AMZREV-All_Beauty-00111",
        "review:RV-AMZREV-All_Beauty-01532"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00036",
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00111",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 19,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01532",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0296",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0020",
        "review:RV-AMZREV-All_Beauty-00038"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0297",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0021",
        "review:RV-AMZREV-All_Beauty-00039",
        "review:RV-AMZREV-All_Beauty-04399",
        "review:RV-AMZREV-All_Beauty-02333",
        "review:RV-AMZREV-All_Beauty-04150"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00039",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04399",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 13,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02333",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04150",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0298",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0022",
        "review:RV-AMZREV-All_Beauty-00042",
        "kb:refund_reason_codes",
        "review:RV-AMZREV-All_Beauty-02657"
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
          "rank": 3,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": 69,
          "bm25_rank": 89,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02657",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0299",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0023",
        "review:RV-AMZREV-All_Beauty-00043"
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
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0024",
        "review:RV-AMZREV-All_Beauty-00044",
        "review:RV-AMZREV-All_Beauty-04865"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0024",
          "doc_type": "faq_case",
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
          "rank": 2,
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
          "rank": 3,
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
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0025",
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
      "precision@5": 0.8,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0026",
        "review:RV-AMZREV-All_Beauty-00055",
        "review:AS-All_Beauty-B000OQFVLS-quality_damage",
        "review:RV-AMZREV-All_Beauty-02412",
        "review:RV-AMZREV-All_Beauty-01189"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00055",
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
          "doc_id": "review:AS-All_Beauty-B000OQFVLS-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 9,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02412",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01189",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0303",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.5855700749881525,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0027",
        "review:RV-AMZREV-All_Beauty-02136",
        "kb:refund_reason_codes",
        "review:RV-AMZREV-All_Beauty-03035",
        "review:RV-AMZREV-All_Beauty-04676"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02136",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 21,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": 73,
          "bm25_rank": 86,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03035",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04676",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 24,
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
      "query_id": "QS-0304",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0028",
        "review:RV-AMZREV-All_Beauty-00064",
        "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
        "review:RV-AMZREV-All_Beauty-02014",
        "review:RV-AMZREV-All_Beauty-01496"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00064",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 14,
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B0BTJ6SYKB-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 15,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-02014",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01496",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
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
      "query_id": "QS-0305",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0029",
        "review:RV-AMZREV-All_Beauty-04516",
        "review:AS-All_Beauty-B08FRQGYDF-delivery",
        "review:RV-AMZREV-All_Beauty-00070",
        "review:RV-AMZREV-All_Beauty-04940"
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
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08FRQGYDF-delivery",
          "doc_type": "review_aspect_summary",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00070",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04940",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0306",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0030",
        "kb:KB005_missing_parts_policy",
        "review:RV-AMZREV-All_Beauty-00074",
        "kb:refund_reason_codes",
        "review:RV-AMZREV-All_Beauty-01674"
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
          "dense_rank": 8,
          "bm25_rank": 10,
          "signals": [
            "dense",
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
          "dense_rank": 76,
          "bm25_rank": 88,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01674",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0307",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0031",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00079",
        "kb:refund_reason_codes",
        "review:RV-AMZREV-All_Beauty-01709"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 33,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
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
          "dense_rank": 66,
          "bm25_rank": 86,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01709",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0308",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0032",
        "review:RV-AMZREV-All_Beauty-03200",
        "review:AS-All_Beauty-B077YR3333-skin_scent",
        "review:RV-AMZREV-All_Beauty-01503",
        "review:RV-AMZREV-All_Beauty-00087"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03200",
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
          "rank": 3,
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
          "rank": 4,
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
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00087",
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0309",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0033",
        "review:RV-AMZREV-All_Beauty-03440",
        "review:AS-All_Beauty-B07GDQPG12-missing_parts",
        "review:RV-AMZREV-All_Beauty-00090",
        "review:RV-AMZREV-All_Beauty-02765"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03440",
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
        },
        {
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07GDQPG12-missing_parts",
          "doc_type": "review_aspect_summary",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00090",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 7,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-02765",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 18,
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
      "query_id": "QS-0310",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0034",
        "review:RV-AMZREV-All_Beauty-00092",
        "review:RV-AMZREV-All_Beauty-01261",
        "review:RV-AMZREV-All_Beauty-03317",
        "review:RV-AMZREV-All_Beauty-01506"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00092",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01261",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03317",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01506",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0311",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0035",
        "review:RV-AMZREV-All_Beauty-00095",
        "kb:refund_reason_codes",
        "review:RV-AMZREV-All_Beauty-01823",
        "review:RV-AMZREV-All_Beauty-04311"
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
          "rank": 3,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": 58,
          "bm25_rank": 64,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01823",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04311",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0312",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.5531464700081437,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0036",
        "review:RV-AMZREV-All_Beauty-00096",
        "review:RV-AMZREV-All_Beauty-03597",
        "review:RV-AMZREV-All_Beauty-02060",
        "review:RV-AMZREV-All_Beauty-04024"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0036",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00096",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03597",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02060",
          "doc_type": "review_evidence",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04024",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0313",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0037",
        "kb:KB001_return_refund_policy",
        "kb:refund_reason_codes"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 32,
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
      "query_id": "QS-0314",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6666666666666666,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0038",
        "review:RV-AMZREV-All_Beauty-00103",
        "review:RV-AMZREV-All_Beauty-04766"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04766",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0315",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0039",
        "review:RV-AMZREV-All_Beauty-03905",
        "review:AS-All_Beauty-B088838886-quality_damage",
        "review:RV-AMZREV-All_Beauty-02241",
        "review:RV-AMZREV-All_Beauty-00107"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0039",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03905",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 15,
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
          "doc_id": "review:AS-All_Beauty-B088838886-quality_damage",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 21,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02241",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00107",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 12,
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
      "query_id": "QS-0316",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0040",
        "review:RV-AMZREV-All_Beauty-00108"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0317",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 0.6,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0041",
        "review:RV-AMZREV-All_Beauty-00109",
        "review:RV-AMZREV-All_Beauty-02727",
        "review:RV-AMZREV-All_Beauty-03057"
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
          "rank": 3,
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
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03057",
          "doc_type": "review_evidence",
          "relevant": false,
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
        "review:RV-AMZREV-All_Beauty-04479",
        "review:AS-All_Beauty-B07KDNK11M-missing_parts",
        "kb:refund_reason_codes"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0042",
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
          "dense_rank": 36,
          "bm25_rank": 36,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04479",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 18,
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
          "rank": 4,
          "doc_id": "review:AS-All_Beauty-B07KDNK11M-missing_parts",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 24,
          "bm25_rank": 28,
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
          "dense_rank": 74,
          "bm25_rank": 89,
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
      "query_id": "QS-0319",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 1.0,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0043",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00113"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 18,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25",
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
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0044",
        "review:RV-AMZREV-All_Beauty-00117",
        "review:AS-All_Beauty-B0B7RBK4NJ-delivery",
        "review:RV-AMZREV-All_Beauty-01551"
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01551",
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
      "query_id": "QS-0321",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0045",
        "review:RV-AMZREV-All_Beauty-02663",
        "review:AS-All_Beauty-B08XJWLLKQ-quality_damage",
        "review:RV-AMZREV-All_Beauty-00120",
        "review:RV-AMZREV-All_Beauty-00416"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02663",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08XJWLLKQ-quality_damage",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00120",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 5,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00416",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0322",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0046",
        "review:RV-AMZREV-All_Beauty-00123",
        "review:AS-All_Beauty-B08N6YHQXT-quality_damage",
        "review:RV-AMZREV-All_Beauty-03663"
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B08N6YHQXT-quality_damage",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03663",
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
      "query_id": "QS-0323",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0047",
        "review:RV-AMZREV-All_Beauty-00125"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0324",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.5531464700081437,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0048",
        "review:RV-AMZREV-All_Beauty-00126",
        "review:RV-AMZREV-All_Beauty-04658",
        "review:RV-AMZREV-All_Beauty-02165",
        "review:RV-AMZREV-All_Beauty-04612"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04658",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02165",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04612",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0325",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0049",
        "review:RV-AMZREV-All_Beauty-00127"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0326",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0050",
        "review:RV-AMZREV-All_Beauty-00128",
        "review:RV-AMZREV-All_Beauty-02799",
        "review:RV-AMZREV-All_Beauty-04496"
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
          "rank": 3,
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
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04496",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0327",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0051",
        "kb:KB001_return_refund_policy",
        "review:RV-AMZREV-All_Beauty-00132",
        "review:RV-AMZREV-All_Beauty-01887",
        "review:RV-AMZREV-All_Beauty-00430"
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
          "doc_id": "kb:KB001_return_refund_policy",
          "doc_type": "policy_markdown",
          "relevant": true,
          "dense_rank": 52,
          "bm25_rank": 31,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00132",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 19,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01887",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-00430",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0328",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6666666666666666,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0052",
        "review:RV-AMZREV-All_Beauty-00133",
        "review:RV-AMZREV-All_Beauty-01374"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01374",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0329",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.8333333333333334,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0053",
        "review:RV-AMZREV-All_Beauty-00136",
        "review:AS-All_Beauty-B07H3S8WTV-battery_power",
        "review:RV-AMZREV-All_Beauty-01413",
        "review:RV-AMZREV-All_Beauty-03368"
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B07H3S8WTV-battery_power",
          "doc_type": "review_aspect_summary",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01413",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03368",
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
      "query_id": "QS-0330",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0054",
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
          "rank": 3,
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
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0055",
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
        "review:RV-AMZREV-All_Beauty-01954",
        "review:AS-All_Beauty-B01M1OFZOG-skin_scent",
        "review:RV-AMZREV-All_Beauty-02257",
        "review:RV-AMZREV-All_Beauty-04672"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01954",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 64,
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B01M1OFZOG-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 44,
          "bm25_rank": 25,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02257",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 65,
          "bm25_rank": 31,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04672",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 11,
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
      "query_id": "QS-0333",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.2,
      "mrr": 1.0,
      "ndcg@5": 0.3391602052736161,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0057"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0334",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 0.6,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0058",
        "review:RV-AMZREV-All_Beauty-00155",
        "review:RV-AMZREV-All_Beauty-01330",
        "review:RV-AMZREV-All_Beauty-01471"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00155",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 30,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-01330",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 17,
          "bm25_rank": 23,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-01471",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 20,
          "bm25_rank": 26,
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
      "precision@5": 0.4,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0059",
        "review:RV-AMZREV-All_Beauty-00157",
        "review:RV-AMZREV-All_Beauty-02666",
        "review:RV-AMZREV-All_Beauty-03324",
        "review:RV-AMZREV-All_Beauty-01830"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00157",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-02666",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 11,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03324",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01830",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0336",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0060",
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
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0061",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00162",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03415",
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
      "query_id": "QS-0338",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.7142857142857143,
      "mrr": 1.0,
      "ndcg@5": 1.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0062",
        "review:RV-AMZREV-All_Beauty-04885",
        "review:AS-All_Beauty-B085BB7B1M-price_value",
        "review:RV-AMZREV-All_Beauty-01850",
        "review:RV-AMZREV-All_Beauty-03423"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04885",
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
          "rank": 3,
          "doc_id": "review:AS-All_Beauty-B085BB7B1M-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": true,
          "dense_rank": 81,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01850",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 63,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03423",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 34,
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
      "query_id": "QS-0339",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0063",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00164",
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
      "query_id": "QS-0340",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0064",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00167",
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
      "query_id": "QS-0341",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.75,
      "recall@5": 0.75,
      "mrr": 1.0,
      "ndcg@5": 0.8318724637288826,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0065",
        "review:RV-AMZREV-All_Beauty-00168",
        "review:RV-AMZREV-All_Beauty-03535",
        "review:RV-AMZREV-All_Beauty-04111"
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
          "rank": 3,
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
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04111",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0342",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0066",
        "review:RV-AMZREV-All_Beauty-00169"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0343",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0067",
        "review:RV-AMZREV-All_Beauty-00170",
        "review:AS-All_Beauty-B09ZKWV5MK-delivery",
        "review:RV-AMZREV-All_Beauty-03676",
        "review:RV-AMZREV-All_Beauty-04168"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00170",
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
          "rank": 3,
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03676",
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-04168",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0344",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6,
      "recall@5": 0.6,
      "mrr": 1.0,
      "ndcg@5": 0.7227265726449519,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0068",
        "review:RV-AMZREV-All_Beauty-00171",
        "ticket:FAQ-All_Beauty-0178",
        "review:RV-AMZREV-All_Beauty-00411",
        "review:RV-AMZREV-All_Beauty-01556"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0068",
          "doc_type": "faq_case",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00171",
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
          "rank": 3,
          "doc_id": "ticket:FAQ-All_Beauty-0178",
          "doc_type": "faq_case",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00411",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01556",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0345",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6666666666666666,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0069",
        "review:RV-AMZREV-All_Beauty-00172",
        "review:RV-AMZREV-All_Beauty-03461"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0069",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-03461",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0346",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.8,
      "recall@5": 0.8,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0070",
        "review:RV-AMZREV-All_Beauty-03527",
        "review:AS-All_Beauty-B0B5X48DZR-skin_scent",
        "review:RV-AMZREV-All_Beauty-00173",
        "review:RV-AMZREV-All_Beauty-01964"
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
        },
        {
          "rank": 3,
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
          "rank": 4,
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
          "rank": 5,
          "doc_id": "review:RV-AMZREV-All_Beauty-01964",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0347",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.8687949224876582,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0071",
        "review:RV-AMZREV-All_Beauty-00174",
        "review:AS-All_Beauty-B08N5NDVGH-price_value",
        "review:RV-AMZREV-All_Beauty-04971"
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00174",
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
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-04971",
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
      "query_id": "QS-0348",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0072",
        "review:RV-AMZREV-All_Beauty-00175"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0349",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.4,
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0073",
        "review:RV-AMZREV-All_Beauty-00176",
        "review:RV-AMZREV-All_Beauty-04950",
        "review:RV-AMZREV-All_Beauty-03096",
        "review:RV-AMZREV-All_Beauty-04678"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-04950",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 3,
          "signals": [
            "dense",
            "bm25",
            "entity_match"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-03096",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04678",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0350",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0074",
        "review:RV-AMZREV-All_Beauty-00180"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0351",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.5,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0075",
        "review:RV-AMZREV-All_Beauty-00181",
        "review:RV-AMZREV-All_Beauty-02274",
        "review:RV-AMZREV-All_Beauty-03133"
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-02274",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-03133",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0352",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 1.0,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0076",
        "review:RV-AMZREV-All_Beauty-00182"
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
        "kb:refund_reason_codes"
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
          "dense_rank": 7,
          "bm25_rank": 15,
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
          "dense_rank": 67,
          "bm25_rank": 84,
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
        "review:RV-AMZREV-All_Beauty-00184"
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
          "dense_rank": 28,
          "bm25_rank": 12,
          "signals": [
            "dense",
            "bm25",
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
      "recall@5": 0.6666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.7653606369886217,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0079",
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
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0080",
        "review:RV-AMZREV-All_Beauty-00186"
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
        }
      ],
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0357",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.6666666666666666,
      "recall@5": 0.5,
      "mrr": 1.0,
      "ndcg@5": 0.6366824387328317,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0081",
        "review:RV-AMZREV-All_Beauty-00189",
        "review:RV-AMZREV-All_Beauty-00848"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0081",
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
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00848",
          "doc_type": "review_evidence",
          "relevant": false,
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
      "query_id": "QS-0358",
      "intent": "support",
      "difficulty": "medium",
      "precision@5": 0.5,
      "recall@5": 0.4,
      "mrr": 1.0,
      "ndcg@5": 0.5531464700081437,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0082",
        "review:RV-AMZREV-All_Beauty-00191",
        "review:RV-AMZREV-All_Beauty-01149",
        "review:RV-AMZREV-All_Beauty-04944"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0082",
          "doc_type": "faq_case",
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
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00191",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-01149",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "doc_id": "review:RV-AMZREV-All_Beauty-04944",
          "doc_type": "review_evidence",
          "relevant": false,
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
          "dense_rank": 49,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
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
          "doc_id": "kb:refund_reason_codes",
          "doc_type": "structured_table",
          "relevant": true,
          "dense_rank": 70,
          "bm25_rank": 73,
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
        "kb:refund_reason_codes"
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
          "dense_rank": 9,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-All_Beauty-00195",
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
          "dense_rank": 57,
          "bm25_rank": 86,
          "signals": [
            "dense",
            "bm25",
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
      "answer_preview": "I’m sorry to hear about the leaking serum and broken pump. According to our return and refund policy, you may request a refund or replacement for items that arrive damaged, defective, or incorrect, as long as you report it within 30 days of",
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
      "answer_preview": "Yes, your Ionic Compact Hair Dryer (SKU: BEAUTY-DRYER-02) is eligible for warranty support. Electrical and powered beauty devices come with a **12‑month limited warranty** that covers manufacturing defects. However, to proceed we need to ve",
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
      "answer_preview": "Based on the available product information and reviews, I recommend the **NightView Baby Monitor** for night monitoring.\n\nThis monitor is specifically designed for nursery use and includes **night vision**, two-way audio, and temperature al",
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
      "answer_preview": "From the provided complaint clusters, the customer operations issues appearing in negative reviews for baby products are:\n\n- **Refund/Return problems** (cluster size 68, average rating 1.794) [doc:review:CL-Baby_Products-refund_return#f4d37",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.3908,
      "answer_preview": "The product database lists SKU **SOFT‑PDF‑01** as “PDF Studio Pro License” with a price of **$59.00**. For delivery context, the product is a digital software license, so standard digital delivery applies. The support knowledge base for sof",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Yes, you can cancel your backup plan from your account page. However, whether you’re eligible for a refund depends on factors such as the renewal date, your usage after the renewal, and local policy. I’ll need to check your account details ",
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
      "answer_preview": "The Crest Whitestrips Dental Whitening System (56 strips) is a popular at-home whitening treatment coated with enamel-safe hydrogen peroxide gel. According to the product profile, it has a catalog rating of **3.6 out of 5** (based on 80 pub",
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
      "answer_preview": "The **Norelco 8894XL** electric shaver in All_Beauty currently holds an average rating of **4.0 out of 5** based on 154 public ratings, with a subset of reviews averaging **4.4**. Key features include cord/cordless operation, 9 sensitivity ",
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
      "answer_preview": "Based on customer reviews and product information, the **Premium Life Rain Hat with Full Visor** is highly rated and praised for its practicality and convenience. \n\nWith a public rating of **4.5 out of 5 stars** (from 614 ratings), this cle",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0004",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0005",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the provided customer reviews, the **Salux Nylon Japanese Beauty Skin Bath Wash Cloth Towel Yellow** has excellent ratings and is strongly recommended.\n\n### Summary of Review Signals\n- **Rating Score:** All available review evidenc",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0007",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the rating and review signals, the **boot tray** (SKU B000I1CFC2) in All_Beauty is a well‑received product. It holds a public rating of **3.9 out of 5** (from 207 ratings) and a slightly higher average of **4.231** from a subset of",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0009",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on available rating and review evidence, the **tea tree lemon sage thickening liter duo set** receives strong overall positive feedback in the All_Beauty category. The product holds a catalog rating of **4.7 out of 5** from 1,924 publ",
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
      "answer_preview": "{\n  \"answer\": \"Based on the rating and review signals for the Soft 'n Style Applicator Bottle, 6 oz in All_Beauty, here is a summary and recommendation.\\n\\n**Overview:**\\nThe product holds a strong catalog rating of **4.6 out of 5** stars b",
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
      "answer_preview": "**Onox Foot Solution Spray, 4 oz (All_Beauty) – Summary & Recommendation**\n\nThe Onox Foot Solution Spray earns a **strong average rating of 4.4 out of 5** (based on 151 public ratings, with a subset of 6 reviews averaging 4.33)[doc:product:",
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
      "answer_preview": "Based on the available product profile and customer reviews, here is a summary of the **Philips Norelco Arcitec 1090 Men’s Shaving System** in the All_Beauty category.\n\n**Product Profile**\n- The shaver features flex & pivot action with thre",
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
      "answer_preview": "The **soft 'n style butterfly clamps, assorted colors, 1 dozen** are highly rated in All_Beauty, with a **4.5 average rating** based on over 2,000 public ratings and a **4.42 average** from a subset of 38 reviews[doc:product:PP-All_Beauty-B",
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
      "answer_preview": "Based on the provided rating and review signals, here is a summary and recommendation for the **Raines Rain Bonnet with Visor, Adult, Colors May Vary** in the All_Beauty category.\n\n**Rating & Overall Signal:**  \nThe product enjoys a strong ",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary of the **face cradle cover - appearus massage fitted headrest covers (6 count/bd1005x6)** in All_Beauty:\n\n- **Product rating:** The catalog shows an average rating of **3.9",
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
      "answer_preview": "Based on available rating and review signals, **Muro 128 5% Solution 15 mL** in All_Beauty is a well-rated product with strong positive feedback from verified purchasers, though there is a minor delivery concern to note.\n\n### Summary of Rat",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0018",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, the **Rose Crystal Organic Rosewater Hydrating Facial Toner with essential oils, pomegranate, and rose quartz gem elixir by Angel Face Botanicals** receives positive feedback from verified p",
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
      "answer_preview": "Based on the available evidence, here is a summary of the product:\n\nThe **IQ Natural Premium Mineral Beauty Powder Natural Touch Bronzer Large 5g** has an overall catalog rating of **4.6 out of 5** from 16 public ratings, indicating general",
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
      "answer_preview": "Based on the available ratings and review signals, the **papier poudre oil blotting papers - rachel 1 booklet (65 sheets)** in **All_Beauty** has a strong positive reputation. \n\n- **Average rating:** 5.0 out of 5 (from 3 catalog ratings; 1 ",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary of the **Super Detox Organic Deep Pore Facial Cleanser with Activated Charcoal, Green Tea, and Argan Oil** in All_Beauty:\n\n- **Overall catalog rating:** 3.5 out of 5 stars ",
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
      "answer_preview": "Based on the available rating and review signals, the **drtulz free nail polish remover - 4 oz** in All_Beauty earns a strong recommendation. \n\n**Summary of signals:**\n- The product profile shows an average rating of **4.5 out of 5** from 1",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0024",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0025",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0026",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0027",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0028",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the provided rating and review signals, here is a summary of the **Besame Cosmetics Forever Red Lipstick (1925)**:\n\n- **Overall Rating:** The product has a strong **4.4 out of 5** from 56 public ratings on the catalog, and the subs",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0030",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, I can provide a recommendation and summary for the **Naramax XL Shower Cap** (blue dot pattern, vinyl, elastic band, extra large/large) in the All_Beauty category. This product has a strong ",
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
      "answer_preview": "Based on the provided rating and review signals for the **Altaire Paris Anti Aging Intensive Youth Day Cream (1.7 oz)** in All_Beauty:\n\n**Summary:**\nThis product is marketed as an intensive anti-aging treatment for tired and stressed skin, ",
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
      "answer_preview": "Based on the available information, here's a summary and recommendation for the **Dermasilk Anti-Aging Skin Care Cream** in the _All_Beauty_ category.\n\n**Summary**\nDermasilk Flawless is a cream developed with advanced optics technology that",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary and recommendation for the **Armani Acqua di Gio Pour Homme 33.8 oz / 1000 ml Shower Gel** in All_Beauty.\n\n**Product Summary**  \n- **Product:** Armani Acqua di Gio Pour Hom",
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
      "answer_preview": "**Product Summary – Lovatic Flawless Eyebrow Hair Remover**  \nBased on the available product profile and customer reviews for the *Lovatic Flawless Eyebrow Hair Remover* (SKU B007MB4YW0) in the All_Beauty category:\n\n- **Overall Rating & Sig",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0036",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary and recommendation for the **Beenle Electric Heat Beard Straightener** from the All_Beauty category.\n\n**Product Summary**\nThis product is a multifunctional beard and hair s",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0038",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals for the \"Cleopatra\" fair trade wooden hair pins (set of four) in the All_Beauty category, the product receives a moderate overall rating but with a notable practical drawback.\n\n**Summary**  \n",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0040",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, the **1/8 inch snap on rollers 8 pack (pink)** is a strong recommendation for its specific use case of styling short or fine hair. Here is a summary of the product feedback:\n\n**Overall Ratin",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0042",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available data, the **moon tattoo stickers 19style totem temporary tattoos star tattoo stickers** in All_Beauty has a solid overall rating: **4.1 out of 5 from 151 public ratings** [doc:product:PP-All_Beauty-B009WFVG66#d9850155",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0044",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "The \"Samy Fat Hair 0 Calories Amplifying Mousse\" (7 oz) is a styling product in the All_Beauty category designed to add volume and hold. Based on available rating and review signals:\n\n- **Ratings**: The product has a catalog average rating ",
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
      "answer_preview": "Based on the provided data, I cannot provide a reliable recommendation or summary for the product **long dual magnetic false eyelashes**. The available review signals are inconsistent with the product title and description. All review texts",
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
      "answer_preview": "Based on the available signals, the **set of 6 fashion headbands fabric wrapped plastic hair bands (#44108)** in All_Beauty receives a positive recommendation. A verified purchaser rated it 5 stars, noting: \"these bands are great! … great c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0048",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the customer rating and review signals available in our records, the **2 pack of 6\"–7\" Natural Ocean Real Sea Sponge by The Sponge Company** (in All_Beauty) is **strongly recommended**.\n\nThe product profile shows that although the ",
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
      "answer_preview": "Based on the available rating and review signals, the **Versace Yellow Diamond Perfumed Deodorant Stick 50ml/1.7oz** in All_Beauty has a mixed picture.  \n\n- The product profile shows a catalog average rating of **4.0 out of 16 public rating",
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
      "answer_preview": "Based on the available rating and review signals, the **Kleancolor Nail Polish Lacquer #20 Neon Pink Manicure + Free Earring Gift** is a well-regarded product in All_Beauty. It holds a **catalog rating of 4.6 out of 5** from 12 public ratin",
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
      "answer_preview": "Based on the provided rating and review signals, **Salerm Color Reverse** (SKU B00C0YZBJE) in All_Beauty receives a mixed reception. It has a catalog rating of **4.0**, though a subset of 8 reviews averages **3.375** [doc:product:PP-All_Bea",
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
      "answer_preview": "Based on the product profile and customer reviews, the **Fuji Premium Crystal Apple Shaped Glass Dappen Dish with Lid** is highly recommended for use as a nail accessory, small jewelry holder, or decorative piece. It has a catalog rating of",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0054",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the provided context, here is a summary and recommendation for the **\"this season's colors tie dye no crease stretch elastic headband hair ties. set of 5\"** (SKU: B00DR75MOM) in the All_Beauty category, using the provided rating an",
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
      "answer_preview": "Based on the available rating and review signals for the **Josie Maran Argan Creamy Concealer Crayon (Fair 1)** in All_Beauty:\n\n- **Overall rating**: The product has a strong **average rating of 4.5 out of 5** from **64 public ratings**, in",
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
      "answer_preview": "Based on available rating and review signals, I can summarize the product **crystal glass, genuine czech 5 inch nail file in green hard case** in the All_Beauty category:\n\n- **Overall catalog rating**: 3.8 out of 5 from 24 public ratings.  ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0058",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals for the **2pairs gel bunion big toe separator spreader eases foot pain foot hallux valgus guard cushion,big toe spreader** (SKU B00EWUFETQ) in All_Beauty, here is a summary:\n\n**Rating Signals",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0060",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Here is a summary of the **SimpleMe Hair Repair Treatment Oil** in the All_Beauty category based on the available rating and review signals:\n\n**Product Profile Summary**\nThe SimpleMe Hair Repair Treatment Oil is designed to deeply condition",
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
      "answer_preview": "Based on rating and review signals, here is a summary of the **Agptek Handmade Natural Fashion Long False Eyelashes (10 pairs)** in All_Beauty:\n\n- **Overall Rating:** The product holds an average rating of **3.5 out of 5 stars** from 640 pu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0063",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "The **Karma Organic Natural Nail Polish Remover (soybean and lavender oil based formula)** is a well‑rated product in the All_Beauty category. It holds a catalog rating of **4.3 out of 5** from 131 public ratings, with an average of **4.5**",
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
      "answer_preview": "Based on the available rating and review signals, the **Neutrogena Visibly Clear Blackhead Eliminating 7 Day Rescue Triple Action Cleanser** (SKU B00GUTPV4A) has an overall catalog rating of **3.6 out of 5** from 14 public ratings [doc:prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0066",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, the **Gold Bond No Mess Powder Spray in Classic Scent (7 oz, 3 pack)** is a top‑performing product in the All_Beauty category. The product profile shows a solid average rating of **4.0 out o",
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
      "answer_preview": "Based on the rating and review signals, the **sun luck whole mung bean sprouts 15oz (4 pack)** shows a positive profile. The product has a catalog rating of **4.5 out of 5** (from two public ratings) and an average of **4 out of 5** from th",
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
      "answer_preview": "Based on available reviews and rating data, here is a summary of the **Sensationail LED Lamp** in All_Beauty:\n\n- **Overall Rating:** The product has an average rating of **4.1 out of 5** from 52 public ratings, with the subset of reviews av",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0070",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review signals, **Tresemme Climate Control Shampoo (32 oz)** in **All_Beauty** receives positive feedback. The product profile shows a strong average rating of **4.5 out of 5** from four public ratings, and",
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
      "answer_preview": "The **dmso cream with aloe vera, 4 oz – rose scented skin moisturizer for adults, whole body pain relief** (SKU B00J7QCNDU) in All_Beauty is highly rated.\n- **Overall rating**: 4.4 out of 5 based on 2,946 public ratings, and 4.333 out of 5 ",
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
      "answer_preview": "Based on the available product and review data, here is a summary of the **sannysis(tm) 1pc useful storage case box holder container pills jewelry nail art tips (15grids)** in **All_Beauty**:\n\n- The product is a storage container suitable f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0074",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the available rating and review data, here is a summary for **Mistiq Instant Facelift Rapid Lifting & Tightening Spritz** in the **All_Beauty** category.\n\n- **Product Overview**: This face mist claims to diminish fine lines, tighte",
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
      "answer_preview": "Based on the provided rating and review signals, here is a summary and recommendation for the **retinol face moisturizer cream natural facial moisturizing cream 1.76 oz** in All_Beauty:\n\n**Summary:**\n- **Product Profile:** This age-defying ",
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
      "answer_preview": "Based on available reviews and product data, the **Dorco Shai Eyebrow Razor for Women** is a highly rated option in All_Beauty (4.3 stars from 34 public ratings, and both subset reviews are perfect 5-stars). Verified purchasers consistently",
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
      "answer_preview": "Based on the available rating and review data, the **Theorie Helichrysum Nourishing Shampoo & Conditioner, 27 fl.oz. set** in All_Beauty is a well‑rated product with a catalog rating of **4.5 out of 5** (from 14 public ratings) and an avera",
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
      "answer_preview": "Based on the available information, here is a summary of the product \"fiber with d3 adult gummies assorted flavors 75 gummies\" in the All_Beauty category using its rating and review signals:\n\n- **Rating:** The product has a perfect 5.0 out ",
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
      "answer_preview": "Based on available rating and review signals, here is a summary and recommendation for the **Silky Smooth Foot Peeling Exfoliating Mask** (1 pair) in the **All_Beauty** category.\n\n**Product Summary**\n\n- **Overall Rating:** 3.5 out of 5 star",
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
      "answer_preview": "Based on the rating and review signals available, the **Protege Flawless Scar Gel Cream** shows mixed feedback. The product profile reports a moderate overall catalog rating of **3.4 out of 5** from 344 ratings, with a small subset of 6 rev",
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
      "answer_preview": "Based on the provided rating and review signals, here is a summary and recommendation for **The Original Ouchless, Snagless Instaloc Loose Hair Tool for Dreadlock Maintenance by Lccessories** in the All_Beauty category.\n\n**Summary:**\n- **Pr",
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
      "answer_preview": "Based on rating and review signals for the **eb5 Collagen Boosting Serum, 1 fl.oz.** in the **All_Beauty** category, the product is generally well-received:\n\n- **Rating**: The product has an overall catalog rating of **4.2 out of 5** from 1",
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
      "answer_preview": "Based on the available rating and review signals, the **Star Wars Rebel Alliance Travel Kit** in the All_Beauty category is a well-regarded product. \n\n- The product holds a **catalog rating of 4.7 out of 5** from 13 public ratings, and the ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0085",
      "expected_intent": "recommendation",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "Based on the provided product profile and customer reviews, here is a summary and recommendation for the **2 pack e.l.f. essential all over color stick blush 3101 pink lemonade** in All_Beauty.\n\n### Summary\n\n- **Product & Ratings:** The pro",
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
      "answer_preview": "Based on the available rating and review information, here is a summary and recommendation for **pure rosehip seed oil certified organic large 4 ounce bottle (120 ml) by Jarosa Beauty** in All_Beauty:\n\n**Summary**  \n- The product is a cold-",
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
      "answer_preview": "Based on the available data, the **best sleep mask set - super soft silk eye mask for traveling insomnia and meditation + ear plugs and pouch** (SKU B00NNKWDI6) has a moderate public rating of **3.5 out of 5** from 70 ratings. The single re",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary of the **Argan Magic 100% Pure Argan Oil** in the All_Beauty category.\n\n### Overall Rating\nThe product has an average rating of **4.1 out of 5** from 77 public ratings on t",
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
      "answer_preview": "Based on the available rating and review signals, here is a summary of the product **organic monoi de tahiti tiare butter 100% natural / 100% pure botanicals / unscented** in the All_Beauty category:\n\nThis product, by Botanical Beauty, is a",
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
      "answer_preview": "Based on the review evidence, customers who gave a 5-star rating for the **Herbivore Natural Sea Mist Texturizing Salt Spray (Coconut, 8 oz)** highlight the following feedback:\n\n- **Scent:** Multiple reviews praise the fragrance. One custom",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence, the product **\"all natural vegan dry shampoo powder - eco friendly, root touch up | hair powder volumizer | for brown hair, brunette and dark hair (Two Goats Apothecary)\"** has received a **rating of ",
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
      "answer_preview": "Based on the available review evidence, the China Glaze Nail Polish in shade Wanderlust 1381 (SKU B00R8DXL44) received a rating of **4 out of 5**. The customer feedback describes the polish as \"pretty color\" but notes that the formula is qu",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Here is the review evidence for the **disposable facial cotton tissue / 100pcs cotton towels face cleansing wipes** for sensitive skin (SKU B099DRHW5V) [doc:review:RV-AMZREV-All_Beauty-00004#592478957d55d1e7].\n\n**Rating:** 5 out of 5  \n**Ve",
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
      "answer_preview": "**Review Evidence**  \nFor the product *niseyo new faux locs 24 inch crochet hair 6 packs 120 strands long soft ombre natural crochet braids (24'' 6pcs t27)*, there is one 3‑star review from a verified purchaser. The review title is “meh” an",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence, there are three 5‑star ratings for the **Nira Skincare Laser & Serum Bundle** (anti‑aging laser + hyaluronic acid serum, FDA‑cleared). \n\n- One customer describes it as “perfect for between salon visits” and not",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence provided, the **Caroline Keller Keratin Shampoo** (formulated for dry and damaged hair and scalp with argan oil, avocado oil, keratin, and vitamins) received a **5-star rating**. The customer feedback is reflect",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, a single customer review exists for the **orange peel nature's cleanse facial scrub - by visage pure - usda organic - physician formulated** product (SKU B08DHTJ25J). The review gave a rating of **3 ou",
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
      "answer_preview": "Based on the available review evidence, the **Ogana Cell Peptide Concentrating Amazing Lotion (2.03 fl.oz., 650 ppm peptide)** has received multiple **5‑star ratings** with consistently positive customer feedback.\n\n- One reviewer states: “t",
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
      "answer_preview": "Based on the available review evidence, the Keratin Secrets Do It Yourself Home Keratin System received a rating of **3** from a customer who described it as **“just ok.”** The customer mentioned that they usually get professional keratin t",
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
      "answer_preview": "Based on the provided review evidence, the **hanhoo red pomegranate 6pcs skin care set** has received **5‑star ratings** with the following customer feedback:\n\n- **Comprehensive skin care regimen** – The set includes six brightening product",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on a 3‑star review for this product, the customer feedback is clear:\n\n> **“didn’t do much and difficult to place and maintain on your face.”**  \n\nThe reviewer found the under‑eye patches **ineffective** (no noticeable reduction of dar",
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
      "answer_preview": "{\n  \"answer\": \"The review evidence for the Bellezza Versa Styler 1-inch titanium plates flat iron (sku B07GHPCT6T) with a rating of 5 shows positive customer feedback. The customer stated that it is a \\\"great hair straightener\\\" that \\\"heat",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Here is the review evidence for the **organic bamboo cotton ear swabs by Bali Boo** (200 count, natural wooden qtips) specifically for **5-star ratings**, along with an explanation of the customer feedback.\n\n**Review Evidence (Rating 5):**\n",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We identified two 5‑star reviews for the **iryasa night indulge cream**:\n\n1. **“wonderful overnight cream!”** – The customer says *“to be honest, i rarely have used an overnight cream,”* indicating that even though they don’t normally use s",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found **four reviews** with a **rating of 5** for the **spa grade jade roller for face with gua sha** (SKU B07GDQPG12). All are from unverified purchases. Here is a summary of the customer feedback from those reviews:\n\n- **Review title “",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, here is the customer feedback for the **manicure and pedicure nail clipper from powergrooming** (1 pack) for rating 5:\n\n- **Review 1:** Titled *\"nice manicure set for men or women\"*, the customer wrote",
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
      "answer_preview": "Based on the provided review evidence, there are multiple 5‑star ratings for the **Philips Sonicare Essence+ Gum Health & Airfloss Rechargeable Electric Flosser Bundle Value Pack (HX8218/02, SKU B01M7UMAUG)**. The customer feedback highligh",
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
      "answer_preview": "Based on the review evidence, there are two reviews with a rating of 3 for the Panasonic EW‑DL82 sonic vibration rechargeable electric toothbrush (white). Their feedback is as follows:\n\n*   **Review 1** (title: *great brush, some drawbacks*",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence for the **4 point eyebrow pen / micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips (SKU B07ZJKVVLW)**, all four available reviews are 5‑star ratings from verified purchasers. The customer feed",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found three verified‑purchase reviews with a rating of 5 for the **2 pieces hair brush cleaner cleaning tool comb cleaner hair brush cleaner comb brushes mini hair dirt remover brush with metal wire rake wooden handle for home and salon ",
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
      "answer_preview": "The review evidence for the original detangler hair brush (rating 3) comes from a verified purchase. The customer described the brush as “just ok” and stated: “its ok not as good as the original wet brush just a knock off.” This feedback in",
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
      "answer_preview": "The review evidence for the charcoal konjac face sponge 3‑pk (SKU B01AKTGHFW) includes a **1‑star rating** from a verified purchaser. The review title is *“not what it claims to do”* and the customer text reads: *“nothing special unfortunat",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "I found a 5‑star review for the **Yellow Brick Road 1lb Shea Butter / 1lb Cocoa Butter combo** (SKU: B079SMVSYW) in the All Beauty category. The customer verified the purchase and titled the review “moisturizing and cost efficient.”  \n\n**Cu",
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
      "answer_preview": "The review for Bromley's 7 Blade Classic Razor (SKU B07K8VTT6M) has a rating of 2. The customer feedback explains that the razor is difficult to hold because it is made of hard, slick plastic with no grippers, and it does not shave as well ",
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
      "answer_preview": "The provided context includes one rating‑2 review for the adofect 31‑pair gold eye mask.  \n\n**Rating‑2 review (verified purchase)** – Title: \"ineffective\"  \n> *Customer text:* \"a total waste of money. i get better results using a tea bag to",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Found **4 five-star reviews** for the Yeshan bow headbands (SKU B09FP8PP2K). Customers consistently praise the product for its quality, softness, and style.  \n\n- “Very pleased with the quality of the headbands super soft and good colors!” –",
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
      "answer_preview": "Based on the provided review evidence, the product **\"halo hair extensions thick invisible wire hair extension with transparent headband...\" (SKU B0BFR5WF1R)** received a **rating of 1 (one star)** from a verified purchase [[doc:review:RV-A",
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
      "answer_preview": "Based on the available review evidence for the **1/8 inch snap on rollers 8 pack (pink)** (SKU B00946HGLW), there are several **rating 5** reviews that highlight positive customer experiences. Here is a summary of the feedback:\n\n| Review Ti",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "**Review Evidence for Replacement Discs (Rating 3)**  \n\nWe located a verified 3‑star review for the replacement discs of the Bellasonic 4‑in‑1 rechargeable electric nail file set. The review is titled “replacement filing discs.”  \n\n**Custom",
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
      "answer_preview": "Here are the 5-star review findings and a summary of customer feedback for the **Wet-Nap Moist Towelette (case of 1000)** in the All Beauty category.\n\n**Review Evidence (Rating 5, Verified Purchases):**\n\n- **Customer 1:** \"i'm a big wet nap",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "I found two 5‑star reviews for the premium life rain hat with full visor (SKU B00023J4AW). Both are verified purchases:\n\n- “Works fine. My wife carries one in her purse.” – customers find it functional and easy to stash in a bag. [doc:revie",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the four 4‑star verified reviews for the shower cap (SKU B005IYYF5E), customers generally find the product satisfactory but have mixed opinions about the fit.\n\n- One reviewer calls it a “nice cap” but states it “runs very large” an",
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
      "answer_preview": "Based on the review evidence, the **NYX Eyebrow Shaper, 1 count** received a **rating of 1**. The customer feedback explains that while the reviewer normally likes NYX products, this particular item was disappointing. The customer reports t",
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
      "answer_preview": "**Review Evidence for Rating 2 (Chialstar 2‑Pack Shampoo Brush)**\n\nThe only review with a rating of **2** for the \"chialstar (2 pack) shampoo brush | hair scalp massager, soft silicone scalp care brush [wet & dry] perfect for men, women, ki",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence, there is one verified purchase review for the **Zynery 10 Pack Button Headbands for Nurses/Doctors** (SKU B08DLGCYK8) with a rating of **4 out of 5**.\n\nThe customer feedback (title: \"great headbands\")",
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
      "answer_preview": "Based on the available review evidence for the product **bow hair band lovely rabbit ears soft carol fleece bowknot makeup cosmetic shower elastic hairlace headband** (SKU B081GCFHPG, pink variant), the following feedback was provided by a ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found **4 verified 5‑star reviews** for the \"alice false eyelashes natural wispy lashes 5 pairs multipack\" (SKU B07H8Z3SMK). All customers praised the lashes for being natural-looking, lightweight, and comfortable.\n\n**Customer feedback s",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found review evidence for the **6 pack 50ml/1.7oz travel plastic clear keychain bottles, leakproof refillable empty bottles** (SKU B08C9LZQN4) in the All Beauty category. \n\n- **Rating:** 5 out of 5  \n- **Customer feedback (excerpt):** *\"",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found four verified 5‑star reviews for the Zoya All Snuggled Up Quad (4‑count, pack of 1). Below is a summary of the customer feedback, which is consistently positive:\n\n- **Colors and finish** – Customers describe the shades as “fantasti",
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
      "answer_preview": "Based on the available review evidence, there are two 1‑star ratings for this product:\n\n- One customer described the stencil as a “waste of money” and explained that the “plastic does not bend for matching your brows and will not lay agains",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found review evidence for **rhinestones bobby pins silver plated words letter crystal hair pins metal hair clips hair barrettes sparkly hair accessories 3pcs (sku B07XYXSYCD)** in **All_Beauty** with a rating of **4 out of 5**. The verif",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, a customer left a **3‑star rating** for the *foot peel mask exfoliating (3 pairs) – foot peeling mask (2 pairs) & moisturizing foot mask (1 pairs)* product (SKU B07NSR3CKR). The review is from a verified ",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence found, here is a summary of customer feedback for the **kenz laurenz cotton headbands 6-pack** (SKU: B07CJWG8SP), all of which have a **rating of 5**.\n\n**Customer Feedback Summary:**\n\n- **Overall Satisfaction**:",
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
      "answer_preview": "We found a verified purchase review for **Merit Advanced Eye Serum** (SKU B018F28B1Y) with a rating of **5 out of 5**. The customer described the product as “great for sensitive skin!” and shared their positive experience: *“I'm loving this",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, here is the feedback for the **5-star rating** on the rhinestones for acrylic nails product (SKU B095SC4J8T):\n\nThe review is titled **\"absolutely beautiful\"**. The customer stated that the rhinestones ",
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
      "answer_preview": "Based on the available review and case records, here is the evidence and explanation for the sonic facial cleansing brush (SKU B09CQ4PXLN) in the All Beauty category:\n\n- **Rating:** 2 out of 5 (unverified purchase).\n- **Customer feedback:**",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The only review found for the “3d mask bracket – internal support holder frame nose breathing smoothly – protect lipstick lips – diy face mask accessories – 5pcs (l-adult)” (SKU B08DXDLR3P) has a rating of **4**. The customer feedback state",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, here is a summary of customer feedback for the **magic hair curlers spiral curls styling kit, 20 pcs no heat wave hair curlers** (all rated 4 out of 5):\n\n- **No instructions included**: One reviewer no",
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
      "answer_preview": "Based on the provided review evidence, the **Schick Bare by Schick Dermaplaning Tool** (which includes 2 dermaplaning razors and 1 cleaning brush) has received a **rating of 4** from a verified (though marked as not verified purchase) custo",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "We located **three 4‑star reviews** for the product **“pore strips, blackhead remover charcoal nose strips deep cleansing 24 strips” (SKU B07FX94GYX)**. Below is a summary of the feedback from each review.\n\n---\n\n### Review 1: “works great”\n",
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
      "answer_preview": "Based on the available review evidence, the **Sailor Moon x ColourPop Collection - From the Moon - Pressed Powder Blush** (SKU B08CXFDDV8) received a **5‑star rating** from a **verified purchase**. The customer’s feedback is summarised in t",
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
      "answer_preview": "Here are the 5‑star review findings for the **Herbivore Natural Sea Mist Texturizing Salt Spray (Coconut, Travel Size 2 oz)** and a summary of the customer feedback:\n\n| Source | Rating | Verified Purchase | Review Summary |\n|--------|------",
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
      "answer_preview": "Based on the provided review evidence, there is a single **rating 4** review for the **Onox Foot Solution Spray, 4 oz** (SKU B000OQFVLS). The customer feedback centers on a safety concern:\n\n- **Customer feedback:** The reviewer originally p",
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
      "answer_preview": "## Review Evidence for Salerm Color Reverse (Rating 5)\n\nBased on the provided review data, I identified three verified 5‑star reviews for **Salerm Color Reverse** (SKU B00C0YZBJE) in All_Beauty. The customer feedback is summarised below.\n\n#",
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
      "answer_preview": "Based on the review evidence for the **Frankies Bikinis Lip Butter Gloss** (also described as a sleeping vegan lip mask, moisturizing lip plumper, etc., SKU B0B8DZ7H5F), we have three reviews that all carry a **rating of 4**. Below is a sum",
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
      "answer_preview": "We found two 5‑star reviews for the **elli k essential sincerity from az time reverse cream – made in usa – anti‑aging face moisturizer** (SKU B0B4JP5YD9). Here is a summary of the customer feedback from these reviews:\n\n- One reviewer (revi",
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
      "answer_preview": "We have two customer reviews for this product, each with a rating of **4 out of 5**. Neither purchase was verified.\n\n**Review 1** (title: *good but strongly scented*) indicates the product works well but has a noticeable scent.  \n\n**Review ",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence for the **Simply Dana Rivitastore Neck Firming Cream** (SKU B09KT4RJG6), here is a summary of the customer feedback specifically for **rating 4**:\n\n**1. Realistic Effectiveness**\nOne customer gave the p",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence for the Apivita Queen Bee Holistic Age Defense Night Cream (1.69 fl. oz., intensive night treatment), a rating‑4 review states:\n\n> “This night cream has a good, thick consistency.”[doc:review:RV-AMZREV",
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
      "answer_preview": "**Review Evidence for Dose of Colors Cold Pressed Booster Multi-Use Oil 1oz (Rating 5)**  \n\nA customer who gave a **5‑star rating** wrote:  \n> “I really like this face oil by Dose of Colors. It is fragrance free, but it has a light, pleasan",
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
      "answer_preview": "**Review Evidence Found**  \nFor the product **Little Moon Essentials Tropical Bath & Shower Sugar Exfoliant, Beach All You Want, 2 oz.**, a review with a rating of **4** was retrieved[doc:review:RV-AMZREV-All_Beauty-00063#68a05d3d70358f6d].",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence (all rating 4), here is a summary of customer feedback for the **Shakira Dance for Women – Long Lasting, Feminine, Charming and Modern Perfume** (SKU B0BTJ6SYKB):\n\n- **Scent profile** – Customers descr",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, there are two customer reviews with a rating of **4 out of 5** for the **More di Croatia Eye Cream – Dubrovnik Gold Anti Aging Eye Cream for Wrinkles**.\n\n**Customer feedback highlights:**\n\n*   The prod",
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
      "answer_preview": "Based on the review evidence for the **Genskin Generation Skin Hydrating Marine Algae Eye Patches** (30 pairs, SKU B08KWN77LW), customers who gave a rating of **4** offer positive feedback focused on the product’s refreshing and relaxing qu",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found two reviews with a rating of 4 for the **invisibobble sprunchie spiral hair ring - true black - scrunchie stylish bracelet**.  \n\n- One reviewer titled their feedback “my first scrunchie!” and wrote “this is my first scrunchie.” Add",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence, there are three reviews with a rating of 4 for the **Pinrose Perfumes Bold Soul - Eau de Parfum Petals (fragrance towelettes)**, which are described as vegan, cruelty-free, and hypoallergenic. Here is a summary",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence for **Pinrose Perfumes Bold Soul – Eau de Parfum Petals (Fragrance Towelettes) – Vegan**, there are three individual reviews with a rating of **4**. Their feedback highlights the following:\n\n- **Portabi",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence, the Serovital Super Saturated Restoring Cleansing Cloths have received several 5-star ratings. Customer feedback highlights the following:\n\n- **Positive impressions**: Customers describe these as “some of the b",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence for the **MD Complete Bright & Healthy Vitamin C+ Vitalizing Face Serum (with Vitamin C, Vitamin E, and Herbal Extracts)**, there are three customer reviews with a rating of **4**. The customer feedback is as fo",
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
      "answer_preview": "We found four pieces of review evidence for the **Caudalie Favorites Set** (SKU B085NYYLQ8) that all carry a **rating of 4**. The customer feedback centers on the set’s travel convenience, product variety, and value for sampling premium ski",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence available, the **Senvenski gel nail polish set (6 colors, SKU B085WTCBLG)** received a **rating of 4**. The customer feedback highlighted the product's color selection: *“This set of gel nail polishes comes in a",
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
      "answer_preview": "Based on the provided review evidence, there are two **4-star customer reviews** for the **mainbasics headband with buttons for face masks (gray)**. Their feedback includes practical experiences as well as a mention of missing parts in a re",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence, here is a summary of customer feedback for the **2-pack Puretize 16.9 oz Hand Sanitizing Gel with Pump Tops (Extra Strength 70% Ethyl Alcohol)** with a rating of **4**:\n\n- **Overall impression**: Customers are ",
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
      "answer_preview": "Based on review evidence from two customer reviews with a rating of 4, the feedback for the **Lua Skincare Clarity Calming Face Oil, 1 fl oz** highlights both a positive effect on skin softness and a critique about a greasy feel. Additional",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence, here are two **rating‑4** customer reviews for the **be plain vitamin ampoule 1.01 fl oz. – Korean multi‑vitamin serum for face** (SKU B083TLNBJJ) and an explanation of the feedback.\n\n### Rating‑4 Rev",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "We found two rating‑4 reviews and one aspect summary for the **6‑pack soft headband (beoffer coral fleece, B082NKQ4ZT)**.  \n\n**Customer feedback highlights:**  \n- The headbands are very **soft** and **cute** (one reviewer says “so soft, so ",
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
      "answer_preview": "Based on the review evidence, the **MD Complete Bright & Healthy Citrus-C Refresh Retinol + Vitamin C Multitasking Treatment** has received **rating-3 reviews** with three main themes of customer feedback:\n\n- **Not effective enough:** One r",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence for the **serum by Merlot (Resveratrol, natural anti-aging, damage corrector, boost collagen, 1 fl oz, dark circle corrector, SKU B07WNBZQGT)**, there is a review with a **rating of 4**. The customer feedback ex",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence, a customer who gave the product a **rating of 4** provided the following feedback:\n\n- **Texture and absorption**: The lotion is described as thinner than some other lotions, but it absorbs quickly. Th",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, a review for the **Kerotin Hairspray - Flexible Hold & Volume with Provitamin B5 - Heat Protectant** (SKU b07jdd2l3m) has a rating of **4 stars**. The review title is **\"huge bottle!\"**, and the custom",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review evidence, there are two verified customer reviews with a rating of **4** for the **\"Wow the Crowd\" eyelash growth serum** (natural formula, 7ml). Both reviews highlight that the product is easy to apply and does",
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
      "answer_preview": "Here are the 5‑star reviews for the **13.5 fl. oz. Goat Milk Facial Cleanser** (SKU B07NPWK167), along with an explanation of the customer feedback.\n\n**Review Evidence (Rating 5)**\n\n1. **“gentle!”** – *“this goat milk cleanser is very gentl",
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
      "answer_preview": "Based on the available review evidence, customers who gave a **5-star rating** to the **C.O. Bigelow No. 007 Dr. Hiosous Quince Hand Lotion, 4 ounces** consistently praised its moisturizing performance, texture, and scent. Here is a summary",
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
      "answer_preview": "Based on the review evidence for the anti-aging hydrating serum (SKU B077YR3333), there are three reviews with a rating of **3 out of 5**. The customer feedback for these neutral ratings highlights the following points:\n\n- **Odd texture**: ",
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
      "answer_preview": "We found three rating‑4 reviews for **QuickBooks Desktop Pro 2019 with Enhanced Payroll (PC Disc)**. Below is a summary of the customer feedback from those reviews.\n\n**Overall Sentiment**  \nCustomers are generally satisfied with the product",
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
      "answer_preview": "{\n  \"answer\": \"Based on the provided review evidence for the **3 pack hair towel wrap turban microfiber drying bath shower head towel with buttons** (SKU B07KV31WDS), the 5-star customer feedback is highly positive and focuses on the follow",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence, I found **4 customer reviews** with a rating of **5** for the product **\"spa grade jade roller for face with gua sha\"** (SKU B07GDQPG12). Here is a summary of the customer feedback from these reviews:\n\n1. **Rev",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review evidence provided, the **aurotrends makeup remover towel (2-pack)** has several 5-star ratings with positive customer feedback. The key takeaways from verified purchasers and reviewers are:\n\n- **Effectiveness and ease of",
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
      "answer_preview": "Based on the review evidence, there are three reviews with a rating of 4 for the **lagunamoon gel nail polish, soak off uv led nail manicure color gel polish varnish set 6pcs 8ml - love spectrum**. Below is a summary of the customer feedbac",
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
      "answer_preview": "Based on the available review data, the main customer ops issue related to delivery for this product is that **items sometimes arrive damaged**.\n\n- A customer reported that their item **arrived broken** even though it was double-bagged, whi",
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
      "answer_preview": "Based on review evidence, the following customer operations issues related to **price_value** appear for this product:\n\n- **Cost not matched by performance** – A verified one-star review states the product is “expensive and doesn’t do anyth",
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
      "answer_preview": "Based on the review evidence, customers of **herbivore - natural sea mist texturizing salt spray (coconut, 8 oz)** report several quality‑related damage issues:\n\n*   **Arriving broken during shipping** – One verified purchase states the “it",
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
      "answer_preview": "Based on the provided review evidence, customer ops issues related to refund/return for the **herbivore - natural sea mist texturizing salt spray (coconut, 8 oz)** include:\n\n- **Product arrived broken and unusable, with the customer questio",
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
      "answer_preview": "Based on the provided reviews, the customer ops issues around the **skin_scent** aspect of Herbivore - Natural Sea Mist Texturizing Salt Spray (Coconut, 8 oz) are not about the scent being unpleasant, but rather that while the scent is gene",
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
      "answer_preview": "Based on the available customer reviews, a customer operations issue related to the scent of the product is that several users find the fragrance off‑putting. The review aspect summary for *skin_scent* shows that out of 11 matched reviews, ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context and tool results, **no customer operations issues related to battery power** are reported for the Nira Skincare Laser & Serum Bundle.\n\n- The review aspect summary for `battery_power` explicitly reports **0 low-",
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
      "answer_preview": "Based on the provided review data, there are no customer operations issues related to **skin_scent** for the Nira Skincare Laser & Serum Bundle. The review aspect summary shows 4 matched reviews with zero low-rating reviews [doc:review:AS-A",
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
      "answer_preview": "Based on the available review data, there are **no customer ops issues** reported around the price/value of the **Ogana Cell Peptide Concentrating Amazing Lotion**. \n\n- The aspect summary for `price_value` shows **2 matched reviews** and **",
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
      "answer_preview": "Based on the provided context, **no customer ops issues or negative feedback appear for the skin_scent aspect** of the Ogana Cell Peptide Concentrating Amazing Lotion 2.03 fl.oz. (60ml) - 650ppm Peptide.\n\nThe aspect summary for skin_scent m",
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
      "answer_preview": "Based on the provided context, the following customer operations issues have been identified for the **Keratin Secrets Do It Yourself Home Keratin System** regarding the aspect **skin_scent**:\n\n1. **Negative feedback on product odor:** The ",
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
      "answer_preview": "Based on the provided review data, there are **no customer operations issues** reported for the **skin_scent** aspect of the Hanhoo Red Pomegranate 6pcs Skin Care Set (6pcs/set).\n\n- The aspect summary for skin_scent shows 3 reviews with **0",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review and ticket data for the **24k gold under eye mask– 20 pairs‑ under eye patches with face massager roller** (SKU B08M3C6LVS), the following customer operations issues related to the **skin_scent** aspect have ap",
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
      "answer_preview": "Based on the review data, the primary customer operations issue related to **quality_damage** for the organic bamboo cotton ear swabs is that some units **fall apart**—the cotton tip comes off the wooden stick. One customer reported that *\"",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided data, a recurring customer operations issue for **iryasa night indulge cream** concerns its skin scent. Multiple customers have reported that the cream smells strongly like furniture polish and find it piercingly unple",
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
      "answer_preview": "Based on the available data, customer ops issues regarding missing parts for the spa grade jade roller for face with gua sha appear primarily as customer inquiries and review mentions. The review aspect summary reports 2 reviews tagged with",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, the main customer operations issue regarding **quality/damage** for the “spa grade jade roller for face with gua sha / jade face roller massager” (ASIN B07GDQPG12) is that there have been **quality/damage",
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
      "answer_preview": "Based on the available review data for the skin_scent aspect of the \"spa grade jade roller for face with gua sha\" (product B07GDQPG12), there are **no clear customer ops issues** reported.\n\n- A review aspect summary for skin_scent indicates",
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
      "answer_preview": "Based on the available review data for the **Philips Sonicare Essence+ Gum Health & AirFloss Rechargeable Electric Flosser, Bundle Value Pack, HX8218/02**, no customer operations issues related to **battery power** were identified. All thre",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided reviews and ticket data, **no specific customer operations issues related to delivery are identified** for this product.\n\nHere is the breakdown of what the retrieved information shows:\n\n- **Positive Delivery Feedback**",
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
      "answer_preview": "Based on the available review data, there are **no customer ops issues** reported for the Philips Sonicare Essence+ Gum Health & Airfloss rechargeable electric flosser, bundle value pack, specifically regarding **price_value**. \n\nThe review",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review data for the Panasonic EW-DL82 Sonic Vibration Rechargeable Electric Toothbrush (White) and specifically the “battery_power” aspect, the available context does not contain any customer‑operations issues directly",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on customer reviews, the main customer operations issues related to **price_value** for the Panasonic EW-DL82 toothbrush are:\n\n- **High initial cost** – One reviewer stated that due to the cost they could not give the product five sta",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available context, there is **one moderate customer concern** related to quality/damage for the Panasonic EW-DL82 toothbrush. The chief point of dissatisfaction is that the toothbrush is **smaller and more lightweight than expe",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available customer reviews, there are **no reported customer operations issues related to delivery** for the \"4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips\" (product ID B07ZJKVVLW). ",
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
      "answer_preview": "Based on the provided review data, there are **no negative customer ops issues reported specifically regarding the price_value**  for the 4 point eyebrow pen.  \n- The review aspect summary for price_value shows 5 matched reviews and zero lo",
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
      "answer_preview": "Based on the available review data for the **4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips**, no customer operations issues related to refund or return are identified:\n\n- The review aspect summar",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review summaries and tool results for the **4 point eyebrow pen, micro ink tat brow pen waterproof eyebrow pencil with micro-fork tips** (SKU B07ZJKVVLW), **no customer operations issues related to the `skin_scent` asp",
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
      "answer_preview": "Based on the reviews for the “2 pieces hair brush cleaner” in the aspect **skin_scent**, one customer ops issue is reported: the small wire teeth of the tool bend easily during use, which may reduce its effectiveness. This issue is describe",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available reviews for delivery of the adofect 31 pairs gold eye mask, the primary customer operations issue is a report of a change in product quality:\n\n- One verified buyer who had purchased the product multiple times reported",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review information, there are **no customer operations issues** reported for the “adofect 31 pairs gold eye mask collagen eye gel pads under eye mask for puffiness and dark circle” related to **price_value**. \n\n- The ",
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
      "answer_preview": "Based on the available reviews and a related customer service ticket, there are **no negative customer ops issues reported** regarding the price value of the **yeshan bow headbands for women non slip stretchy hair bands elastic headwraps kn",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, **no customer operations issues related to quality or damage are reported** for the Yeshan bow headbands. The two reviews that mention `quality_damage` are both 5‑star and express full satisfaction with t",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the customer reviews provided for the Yeshan bow headbands (SKU B09FP8PP2K), the following customer operations issue related to **skin_scent** has been reported:\n\n- **Unpleasant odor:** A verified customer gave a 3-star rating and ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review data, there are **no customer operations issues** reported for the 1/8 inch snap on rollers 8 pack (pink) related to the \"skin_scent\" aspect. The aspect summary shows 4 matched reviews with 0 low‑rating reviews,",
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
      "answer_preview": "Based on the provided reviews and FAQ, there are no customer operations issues reported for delivery of the wet‑nap moist towelette (case of 1000). The delivery‑focused reviews are all positive and no low ratings were found[doc:review:AS-Al",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review data for the **shower cap – blue dot pattern, vinyl material, elastic band, extra large, large** (SKU B005IYYF5E), the customer operations issues tagged under the **missing_parts** aspect are primarily related to **size ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review evidence for the shower cap (blue dot pattern, vinyl, extra large/large), the primary customer operations issue related to price_value is a **strong plastic smell** reported by some customers. Although the prod",
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
      "answer_preview": "Based on the review data available, the **shower cap (blue dot pattern, vinyl, elastic band, extra large/large)** shows mixed customer‑ops issues around **quality_damage**:\n\n- **Negative experience**: A verified buyer reported that the elas",
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
      "answer_preview": "Based on the provided review data, there are **no customer operations issues explicitly related to *skin_scent*** for this shower cap (blue dot pattern, vinyl material, elastic band, extra large/large).  \n\nThe reviews tagged with the *skin_",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the customer operations issue appearing for the **chialstar (2 pack) shampoo brush** regarding **missing_parts** is a **customer inquiry/FAQ**. \n\nA specific support ticket was logged where a customer asked abo",
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
      "answer_preview": "Based on the provided customer review data for the **chialstar (2 pack) shampoo brush** (ASIN B07KDNK11M), there are **no customer operations issues** (such as complaints, negative feedback, price disputes, or refund/return requests) relate",
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
      "answer_preview": "Based on the available reviews, there are **no customer ops issues related to quality or damage** for the chialstar (2 pack) shampoo brush. The review summary shows zero negative ratings for the quality/damage aspect, and customer feedback ",
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
      "answer_preview": "Based on the provided review data for the Chialstar shampoo brush’s **skin_scent** aspect, there are **12 reviews total**, with **1 low‑rating review** [doc:review:AS-All_Beauty-B07KDNK11M-skin_scent#9e4fdd336cb4c941].  \n\nHowever, the speci",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, there are no customer operations issues related to **price_value** for **zoya all snuggled up quad,4 count (pack of 1)**. The aspect summary shows 2 matched reviews and **0 low rating reviews** for this a",
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
      "answer_preview": "Based on the review data for **cotton headbands 6 pack (B07CJWG8SP)** tagged with the aspect **missing_parts**, the following customer ops issues appear:\n\n1. **Color / appearance discrepancy** – One verified 2‑star review complains that the",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on customer reviews, the primary customer operations issue related to price_value for the cotton headbands is a durability concern: one customer reported that a headband developed a small tear after only two wears, despite being satis",
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
      "answer_preview": "Based on the review data for the **cotton headbands 6 pack (B07CJWG8SP)**, the main customer operations issue related to **quality/damage** is a reported problem with the headbands being **too tight**, causing discomfort.\n\n- A 1-star verifi",
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
      "answer_preview": "Based on the provided review data, there are **no customer ops issues** reported for the cotton headbands 6‑pack (Kenz Laurenz) related to the **skin_scent** aspect. \n\n- The aspect summary shows that of the two reviews tagged for skin_scent",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the customer reviews provided, several customer operations issues are evident for the **magic hair curlers spiral curls styling kit, 20 pcs no heat wave hair curlers**, particularly regarding usability and product expectations. The",
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
      "answer_preview": "Based on the available review data for the Schick Bare dermaplaning tool (product B07LBK2YQX), there is evidence of a customer‑operations issue related to **skin_scent**. One low‑rating review (1 star, tagged with the aspect `skin_scent`) i",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on customer reviews, the main customer operations issues around delivery for **herbivore - natural sea mist texturizing salt spray (coconut, travel size 2 oz)** are:\n\n- **Leakage and spillage** – The bottle arrived with the top loose,",
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
      "answer_preview": "Based on customer reviews, the price_value concerns for the **Herbivore Natural Sea Mist Texturizing Salt Spray (Coconut, Travel Size 2 oz)** revolve around the product being perceived as too expensive for the quantity received, especially ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review context, the primary customer operations issue related to the **skin_scent** aspect of the Herbivore Natural Sea Mist Texturizing Salt Spray is a **product delivery damage / leakage incident**.\n\nA verified custo",
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
      "answer_preview": "Based on the available reviews and FAQ case, one customer ops issue related to “quality_damage” for the **Onox Foot Solution Spray, 4 oz** is that the product’s labeling warns against use on cracked or damaged skin, which has raised concern",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on customer reviews for Salerm Color Reverse, the main customer operations issue related to \"skin_scent\" is a strong, unpleasant odor that many users find offensive. Complaints describe the smell as \"disgusting,\" \"worse than a perm sm",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, **no customer operations issues are reported** for the \"Frankies Bikinis Lip Butter Gloss...\" product regarding the *skin_scent* aspect. The two reviews we have are both positive (4 stars) and describe th",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided reviews and aspect summary, **no customer operations issues are reported for the elli k essential sincerity from az time reverse cream regarding skin scent**. The two available reviews are both 5-star and contain only ",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data, there are no significant customer operations issues (such as complaints, returns, or negative feedback) related to the **skin_scent** of the Elli K Essential Sincerity from AZ Time Reverse Double Ampoule.",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review data for the **Simply Dana RivitaStore Neck Firming Cream** (specifically for the *skin_scent* aspect), **no customer operations issues are reported**. The aspect summary includes two reviews, both with a ratin",
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
      "answer_preview": "{\n  \"answer\": \"Based on customer reviews, the main customer ops issue related to skin_scent for the Apivita Queen Bee night cream is a strong, lingering scent that some users find unpleasant. One reviewer described it as a \\\"strong chemical",
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
      "answer_preview": "Based on the provided review data and tool results, **no customer ops issues appear** for the Dose of Colors Cold Pressed Booster Multi-Use Oil 1oz regarding the **skin_scent** aspect.\n\nThe review aspect summary explicitly reports **0 low-r",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, there are indications of customer operations issues related to “missing_parts” for the Shkaira perfumes “Dance for Women” product, but the evidence is limited and does not specify the exact nature of a missing",
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
      "answer_preview": "Based on the available review and database data for the Shakira Dance perfume, **no customer operations issues appear regarding the *price_value* aspect.**\n\nThe review analysis specifically for the **price_value** category shows **0 low-rat",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the customer reviews for the \"Shakira Dance for Women\" perfume (focused on the **skin_scent** aspect), the following customer operations issues appear:\n\n1. **Poor longevity / “long lasting” claim not met** – Several reviews state t",
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
      "answer_preview": "Based on the available review data for the **more di croatia eye cream - dubrovnik gold anti aging eye cream**, no customer ops issues are reported for the **skin_scent** aspect. The two reviews that mention the scent describe it as minimal",
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
      "answer_preview": "Based on the available review data for the **genskin generation skin hydrating marine algae eye patches** (product B08KWN77LW), no customer operations issues have been identified specifically related to the **skin_scent** aspect.  \n\n- The a",
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
      "answer_preview": "Based on the available review data, **no customer operations issues** (such as complaints, returns, or defects) are documented for the **skin_scent** aspect of the invisibobble sprunchie spiral hair ring – true black.\n\nThe review aspect sum",
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
      "answer_preview": "Based on the available reviews for **pinrose perfumes bold soul - eau de parfum petals (fragrance towelettes) – vegan**, the only customer-related feedback around the **skin_scent** aspect is a mixed reception of the fragrance itself. No di",
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
      "answer_preview": "Based on the provided context and tool results, **no specific customer ops issues related to delivery** appear for the Serovital Super Saturated Restoring Cleansing Cloths.\n\nThe review aspect summary for delivery reports **0 low-rating revi",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on customer reviews, the main customer operations issue related to **price_value** for the **Serovital Super Saturated Restoring Cleansing Cloths** is a perception of high cost for the quantity received.  \n\n- A review aspect summary n",
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
      "answer_preview": "Based on the available review data for *md complete bright & healthy vitamin c+ vitalizing face serum*, there are **no reported customer operations issues related to quality/damage**.\n\n- The review aspect summary for quality/damage indicate",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "A negative review trend exists in the **All_Beauty** category specifically regarding **battery power** complaints. A complaint cluster of 36 reviews shows an average rating of **2.278 out of 5**, indicating significant customer dissatisfact",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The negative review trend in All_Beauty for delivery complaints is a cluster of 63 reviews with an average rating of 2.032, indicating significant dissatisfaction with delivery. [doc:review:CL-All_Beauty-delivery#94b6d44733ad17d4]",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the complaint cluster data for **All_Beauty** under the general_complaint aspect, there is a significant negative trend: **403 reviews** form this cluster with an **average rating of only 2.154 out of 5**, indicating that general c",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the complaint cluster analysis, reviews in the All_Beauty category that mention missing parts have an average rating of 2.263 out of 5, which is notably low. The cluster comprises 76 reviews, indicating a recurring negative trend w",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the complaint cluster data, a significant negative trend in the **All_Beauty** category concerns **price_value**. A cluster of 200 reviews, with an average rating of 2.32, indicates widespread customer dissatisfaction with the perc",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "In All_Beauty, a negative trend appears in complaints about quality damage: a cluster of 100 reviews from the public subset has an average rating of 2.08, signaling widespread dissatisfaction with damaged or poor-quality items. [doc:review:",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "There is a notable negative review trend in the **All_Beauty** category specifically for **refund/return** complaints. The data shows a complaint cluster of **109 reviews** from the public review subset, with an extremely low average rating",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "{\n  \"answer\": \"The negative review trend in All_Beauty for skin_scent complaints involves consistently low product ratings (1–2 stars) and user dissatisfaction with product smell. The aggregated aspect summary explicitly recommends an opera",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The negative review trend for battery_power complaints in Baby_Products is a complaint cluster of **33 reviews** with an **average rating of only 2.424 out of 5**, indicating widespread dissatisfaction with battery performance in the catego",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0262",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "difficulty": "hard",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.6959,
      "answer_preview": "Based on the provided context, there is no information about delivery complaints for Baby\\_Products. The available complaint clusters cover refund/return issues, quality/damage issues, and general complaints, but none of these specifically ",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available review analysis, the negative review trend for **Baby_Products** under the aspect **general_complaint** is represented by a review cluster containing **440 public reviews** with a very low **average rating of 2.207**.",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided data, there is a notable negative trend in the **Baby_Products** category specifically regarding **missing parts** complaints. A complaint cluster of **73 reviews** (from a public subset) has an average rating of **2.3",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review analysis, a negative trend for **price_value complaints** in the **Baby_Products** category is identified by a complaint cluster containing **170 reviews** with a low average rating of **2.418**. This indicates that cust",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided review data, a negative review trend exists in the Baby_Products category centered on **quality_damage** complaints. This trend is captured by a specific complaint cluster containing **74 reviews** with a very low aver",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review data, a significant negative trend exists for refund/return complaints in the **Baby_Products** category. A complaint cluster of **68 reviews** focusing on the **refund_return** aspect has an extremely low average rating",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "A complaint cluster for skin_scent in Baby_Products includes 93 reviews and has an average rating of 2.269, indicating a clear negative trend of dissatisfaction related to skin scent concerns [doc:review:CL-Baby_Products-skin_scent#d661068f",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The negative review trend in the Software category for **battery_power** complaints is captured by a complaint cluster of 46 reviews with an average rating of **1.913** (very low). The representative complaint illustrates the kind of dissat",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.3726,
      "answer_preview": "Based on the provided review analysis, a negative review trend for delivery complaints appears in the **Software** category. This trend is identified by a complaint cluster containing **38 reviews** with a very low average rating of **1.895",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the complaint cluster for **Software** and aspect **digital_license**, the negative review trend is that customers frequently feel the content or value provided by the license does **not justify the cost**. The cluster’s representa",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The negative review trend for the `general_complaint` aspect in the Software category centers on severe usability and stability problems. The complaint cluster comprises 1,176 reviews with a very low average rating of 1.913, indicating wide",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the review cluster for the **Software** category and **missing_parts** aspect, the negative trend consists of **low average ratings (1.787)** across 47 reviews. The representative complaint indicates that while the app is considere",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.7726,
      "answer_preview": "The complaint cluster for Software products regarding price_value shows a clear negative trend: customers express dissatisfaction with the value they receive for the price paid. The cluster contains 116 reviews with an average rating of onl",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.9089,
      "answer_preview": "The negative review trend in the Software category for `quality_damage` complaints is a cluster of **36 reviews** with an average rating of **2.056** (out of 5), indicating a high level of dissatisfaction due to quality or damage issues. Af",
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
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the complaint cluster data, the negative review trend for **Software** regarding **refund/return** complaints is that customers strongly express that the products are not worth the money, advising others to avoid specific software ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0277",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.6018,
      "answer_preview": "Based on the return and refund policy `[doc:kb:KB001_return_refund_policy#ee79e051ef7a427c]`, support must first verify the customer's order, product SKU, delivery date, item condition, and proof (such as photos) before processing any retur",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0278",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 0.5049,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0279",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available FAQ case, this product is built around natural orange peel, which gives it a fresh, citrus-like scent. The support team can handle the **skin_scent** inquiry by:\n\n- Referring to the product’s description as an **orang",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0280",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, the ticket [doc:ticket:FAQ-All_Beauty-0004#192ef047cfe7f857] contains only the customer's question about the skin_scent of the Keratin Secrets Do It Yourself Home Keratin System. The handling steps or FAQ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0281",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.4807,
      "answer_preview": "Based on the provided return status matrix policy, for delivery-related cases (such as late delivery), support agents should classify the request by examining the delivery date and evidence. Specifically, **carrier scan evidence is required",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0282",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available context, the only relevant record is an FAQ case ([doc:ticket:FAQ-All_Beauty-0006#bb05e3577024a970]) for the **24k gold under eye mask** with the aspect `skin_scent` and a rating of 3. However, the provided text does ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0283",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available context, the **manicure and pedicure nail clipper from powergrooming** has an associated FAQ entry regarding its price value, which received a 5‑star rating. Support can handle this case by using the FAQ reference to ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0284",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "To handle this delivery case for the **Philips Sonicare Essence+ Gum Health & Airfloss Rechargeable Electric Flosser, Bundle Value Pack, HX8218/02**, the support agent should proceed with caution, as the specific nature of the delivery issu",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0285",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0286",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.9763,
      "answer_preview": "Based on the available information, the knowledge base provides a **general return and refund policy** ( [doc:kb:KB001_return_refund_policy#ee79e051ef7a427c] ) that applies to any product requested within 30 days of delivery for damaged, de",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0287",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.8158,
      "answer_preview": "Based on the available policy documents, support should handle this case by first verifying the order details, product SKU, delivery date, item condition, and requesting photographic proof before any refund or replacement is offered. The Re",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0288",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the case details, the customer is dissatisfied with the **bromley's 7 blade classic razor** because it is difficult to hold (hard, slick plastic with no grip) and does not shave as well as their usual 5‑blade razor[doc:ticket:FAQ-A",
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
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the **Return and Refund Policy**, the support team may offer a replacement or refund after validation [doc:kb:KB001_return_refund_policy#96522358b4eef486]. However, since no order details (order ID, SKU, or delivery date) are curre",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0290",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, I cannot provide a specific handling procedure for this price_value case.\n\nThe retrieved ticket [doc:ticket:FAQ-All_Beauty-0014#0301cad88ee7e4c2] shows only that an FAQ case exists for the **yeshan bow he",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0291",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the only information available is a customer inquiry about the price_value of the halo hair extensions product, where the customer expressed strong dissatisfaction (calling it “garbage”). The context does not ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0292",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0293",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0294",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the **nyx eyebrow shaper, 1 count** was previously the subject of a price‑value question (FAQ‑All_Beauty‑0018) where a customer felt the product was “not worth it” because of the way it affected their eyebrows",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0295",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, there is insufficient detail to determine a specific handling procedure for this general_support case. The only document referencing a general_support scenario for this product [sic: chialstar shampoo bru",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0296",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.792,
      "answer_preview": "Based on the provided context and tool results, I can outline the general policy but must note that the specific evidence for this case is insufficient to proceed without additional information.\n\nAccording to the **Return and Refund Policy*",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0297",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the FAQ case [doc:ticket:FAQ-All\\_Beauty-0021#3379871a035c0bb3] documents a customer who initially praises the product as “very natural, light weight and good quality” but then asks about quality damage. The t",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, support should handle this missing parts case for the eyebrow stencil kit as follows:\n\n- **Required evidence**: Request from the customer a **package photo** and a **description of the missing part**.\n- *",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0299",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.6809,
      "answer_preview": "To handle this delivery case for the rhinestones bobby pins, the support team should follow the standard process defined in the policy documents, as the backend system did not return any matching order or product SKU for this specific item.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0300",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, the support team should handle this general support case by first identifying the customer’s specific concern. If the issue involves a return, refund, or a defective/damaged item, the team must follow the",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0301",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The provided context contains only an FAQ case documenting a negative rating (2) for the **skin_scent** aspect of the sonic facial cleansing brush. No specific handling procedures, policies, or escalation paths are included.  \n\nGiven insuff",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the FAQ case for onox foot solution spray, 4 oz, the customer's concern involves a quality/damage issue related to the product warning about not using it on cracked or hurt feet due to potential stinging [doc:ticket:FAQ-All_Beauty-",
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
      "answer_preview": "To handle the missing_parts case for the **salerm color reverse** product, support should follow the process defined in the refund reason codes knowledge base:\n\n1. **Request the required evidence** from the customer: a **package photo** and",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0304",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "To handle the missing_parts case for **Shakira Perfumes – Dance for Women – long lasting – feminine, charming and modern** (1.7 fl oz), support should follow the **Missing Parts Policy** and the **Refund Reason Codes** guidance, while notin",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0305",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the context available for the **serovital super saturated restoring cleansing cloths** [doc:ticket:FAQ-All_Beauty-0029] (which is classified as a delivery case), support agents should follow the standard resolution procedures outli",
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
      "answer_preview": "To handle this missing parts case for the **mainbasics headband with buttons for face masks (gray)**, support should follow the standard Missing Parts Policy and the **missing_part** refund reason code guidelines.\n\nThe recommended steps are",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0307",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0308",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0309",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "For **missing parts** cases (like a missing component in the spa grade jade roller), support should:\n\n1. **Request evidence** – a package photo and a description of the missing part ([doc:kb:refund_reason_codes#63d8b47e24b444c9]).  \n2. **Sh",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, support should handle the missing parts case for the lagunamoon gel nail polish set by first consulting the FAQ case specifically created for this product and missing parts scenario ([[doc:ticket:FAQ-All_",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "The provided context references a delivery FAQ case for the specific product (Vebelle Anti Aging anti-wrinkle eye cream) [doc:ticket:FAQ-All_Beauty-0035#f17feb00ba5fe0dc] and a Refund Reason Codes policy [doc:kb:refund_reason_codes#1dd31190",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0312",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "To handle this **price_value** case for the **silky smooth foot peeling exfoliating mask - 1 pair**, support should reference the product-specific FAQ case [doc:ticket:FAQ-All_Beauty-0036#59e50999dbfe51e4], which covers this product and not",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0313",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0314",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0315",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided FAQ case (citation), the product is associated with a quality damage issue, but the case does not include any specific handling instructions or resolution steps. Support should gather additional details from the custom",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0316",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available context, the customer is questioning the price\\_value of the product after reporting quality issues (“cheap stuff… bumpy surface, paint is chipping off after one use”). The provided FAQ case does not contain specific ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0317",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "To handle this missing parts case for the **chialstar (2 pack) shampoo brush**, support should follow the **Missing Parts Policy** and the **Missing Part reason code**:\n\n1. **Confirm the report is within 14 days of delivery** (as per policy",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0319",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0320",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0321",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "For this **quality/damage** case involving the **John Frieda Detox and Repair Shampoo and Conditioner Set**, support should follow the standard return/refund policy outlined in the knowledge base. The customer has reported a damage issue af",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0322",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided policy and context, here is how support should handle this quality_damage case for the **heyedrate activated charcoal soap bar and face wash**.\n\nThe **Return and Refund Policy** ([doc:kb:KB001_return_refund_policy#ee79",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0323",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "To handle the quality damage case for the Metluck 3 Pack Hair Wrap Towels, support should follow the standard return and refund policy:\n\n1. **Verify the order and product** – check the customer’s order ID, product SKU, delivery date, and co",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0324",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context [doc:ticket:FAQ-All_Beauty-0048#6971a68f426a4869], this is identified as a **quality_damage FAQ case** for the product *\"3 barrel curling iron, milantia 3/4 inch mini travel curling wand hair for small curly, d",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0325",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "For the \"missing_parts\" case involving the **pink wigs for women short bob pink wig with bangs shoulder length pastel curly wavy cosplay wig synthetic daily costume colorful wigs (14 inch)**, support should follow the standard missing‑parts",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0326",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0327",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided missing parts policy, support should handle this case as follows:\n\n1. **Verify reporting timeframe**: Confirm with the customer that they are reporting the missing part within 14 days of delivery, as required by the po",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0328",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, support should handle this quality damage case for the \"Eternal Matte Lovers Collection\" by following the standard return and refund policy.  \n\n- First, verify the customer's order details (order ID, prod",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0329",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 0.2713,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided product profile and reviews, support should handle this general support case by first listening to the specific complaint, as customers have reported missing pieces, poor seller communication, slow shipping, and diffic",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0331",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0332",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the only available information is a FAQ case that records a customer question about “skin_scent” for the Bed Head Curve Check Curling Wand, along with a comment that the wand is difficult to use on shoulder‑le",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0333",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided policies and the related FAQ ticket, support should handle this delivery case for the Ultimate Essentials Kit by treating it as a potential product defect claim. The customer’s report of hair loss suggests the item may",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0334",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0335",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, support should handle this quality/damage case by following the standard return and refund procedure. According to policy, customers may request a return within 30 days of delivery for damaged or defectiv",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0336",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "For this general support inquiry about the stretch mask & scar removal cream, the support team should first consult the relevant FAQ case [doc:ticket:FAQ-All_Beauty-0060#7138fd1c22fb01a3]. This FAQ indicates that the product is formulated f",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0337",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information from the FAQ case [doc:ticket:FAQ-All_Beauty-0061#6596f215cdf651db], the customer has asked about the skin_scent of the eos delicate petals & blackberry nectar gift set, pack of 1. However, the provided co",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0338",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the customer's inquiry for the **salux nylon japanese beauty skin bath wash cloth/towel (3) blue yellow and pink** ([doc:ticket:FAQ-All_Beauty-0062#e7393095736bf07f]) is a **price_value** complaint. The custom",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0339",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "To handle this general support case for the dgd hand sanitizer bottles (leak proof keychain/holder), the support team should follow the standard return and refund policy for leaking or defective items:\n\n1. **Verify the issue and order detai",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0340",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "The general support case for the 10 pairs 3D faux mink hair false eyelashes should be handled by referring to the corresponding FAQ case documented in ticket **FAQ-All_Beauty-0064**[doc:ticket:FAQ-All_Beauty-0064#1ad5bea54b024f36]. This tic",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0341",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The provided context contains only a faq case entry for the nail buffer block (product ID B07KZQDM8Y) with the aspect **general_support** and a rating of 3. The entry describes the product as a “4 way nail art shiner 4 step buffing – file, ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0342",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available context, only a brief FAQ case identifier is provided for this product’s **price_value** aspect (with a rating of 3) [doc:ticket:FAQ-All_Beauty-0066#e03e9087648e421b]. No specific handling instructions or resolution s",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0343",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 0.8615,
      "answer_preview": "Based on the available return and refund policy, support should follow these steps for delivery cases involving items like the 6‑piece silk hair scrunchies:\n\n1. **Verify the order and product details** – confirm the order ID, product SKU, d",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0344",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the `[doc:ticket:FAQ-All_Beauty-0068#3c89ede3903d50a5]` context, the customer's `price_value` complaint stems from a clear mismatch between the product image and the received item. The customer stated: “the photo on amazon must be ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0345",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided policy and reason‑code details, here is how support should handle this missing‑parts case for the **so’bio étic baby soothing diaper cream**:\n\n1. **Collect the required information** – Ask the customer for:\n   - Order ",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0346",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided ticket context, this is an FAQ case for the hateli pet comb with the aspect \"skin_scent\" and a rating of 3 (neutral). The ticket serves as a reference for handling customer inquiries about the product’s scent, but does",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0347",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0348",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity",
        "missing_product_context"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 0.2074,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0349",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0350",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 0.3204,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0351",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided context, the bath bombs gift set is not an electronic or powered beauty device, so the warranty policy in [doc:kb:KB002_warranty_policy#59391347ce77614f] does not apply. The FAQ ticket [doc:ticket:FAQ-All_Beauty-0075#6",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0352",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 0.3224,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
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
      "answer_preview": "For this missing_parts case concerning the heart shaped makeup sponge set with holder (blue, yellow, 3 pieces), support should follow the established **missing parts policy**:\n\n1. **Verify the delivery timeframe** – Ensure the customer repo",
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
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the knowledge base article on missing parts policy, support should handle this case by first collecting the necessary information from the customer: the order number, the SKU of the product, a photo of the package, and a detailed d",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0355",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, there is a documented FAQ case for the **blaister animal print headbands for women** (product ID B092M1WFTR) under the aspect **skin_scent** with a rating of **2**[doc:ticket:FAQ-All_Beauty-0079#83eba799c",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0356",
      "expected_intent": "support",
      "intent": "sku_order",
      "difficulty": "medium",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_structured_entity"
      ],
      "citation_ok": 0.0,
      "keyword_coverage": 0.3333333333333333,
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist.",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0357",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 0.6666666666666666,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, support should handle this “price_value” case by first asking the customer for the missing order details (order ID, SKU, and delivery date) to validate the complaint. The [return/refund policy]([doc:kb:KB",
      "expected_action": "answer",
      "safety_category": "normal"
    },
    {
      "query_id": "QS-0358",
      "expected_intent": "support",
      "intent": "support",
      "difficulty": "medium",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy"
      ],
      "citation_ok": 1.0,
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available information, there is an existing FAQ case (FAQ‑All_Beauty‑0082) that covers the **price_value** aspect for the product “makeup brushes 12pcs‑ clowii professional premium birch handle makeup brush foundation concealer",
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
      "answer_preview": "For this **missing_parts** case regarding the shower cap (2 pcs large, 15 inch extra large for women), support should follow the standard missing parts policy:\n\n1. **Confirm timing** – Ensure the customer reports the issue within **14 days ",
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
      "answer_preview": "Based on the provided policies, support should handle this missing parts case as follows:\n\n- Verify that the customer reports the missing part within **14 days of delivery**.\n- Collect the following from the customer:\n  - **Order number**\n ",
      "expected_action": "answer",
      "safety_category": "normal"
    }
  ]
}
```
