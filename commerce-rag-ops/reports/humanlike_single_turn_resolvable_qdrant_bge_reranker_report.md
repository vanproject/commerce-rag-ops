# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: humanlike_single_turn_resolvable
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_single_turn_resolvable.jsonl
- Oracle sources: False

## 摘要

- 样本数: 10
- 检索后端: qdrant
- 检索模式: hybrid_rerank
- Precision@5: 0.24
- Recall@5: 0.315
- MRR: 0.5
- NDCG@5: 0.328
- exact_recall@5: 0.5
- acceptable_recall@5: 0.6
- entity_accuracy@5: 0.6
- aspect_accuracy@5: 0.8
- forbidden_rate@5: 0.0
- Action accuracy: 0.7
- 引用率: 0.7
- Citation leak rate(refuse/clarify): 0.0
- Citation schema OK: 0.7
- Answer citation precision/recall: 0.7 / 0.3333
- Citation grounded rate: 0.7
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.71
- 延迟 p50/p95: 24212 ms / 72438 ms
- Embedding 模型: BAAI/bge-large-en-v1.5
- Reranker 模型: BAAI/bge-reranker-large
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 4 | 0.3 | 0.3542 | 0.625 | 0.3853 | 1.0 | 1.0 | 1.0 / 0.5625 | 1.0 |
| recommendation | 3 | 0.0667 | 0.1111 | 0.3333 | 0.1564 | 0.3333 | 0.3333 | 0.3333 / 0.0833 | 1.0 |
| support | 3 | 0.3333 | 0.4667 | 0.5 | 0.423 | 0.6667 | 0.6667 | 0.6667 / 0.2778 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 10 | 0.24 | 0.315 | 0.5 | 0.328 | 0.7 | 0.7 | 0.7 / 0.3333 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 45 | 12 |
| dense | 45 | 12 |
| policy_fallback | 2 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | bm25: 6, dense: 6 |
| recommendation | bm25: 1, dense: 1 |
| support | bm25: 5, dense: 5 |

## Agentic 证据诊断

- 重试率: 0.8

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 7, refuse: 3 |
| 尝试次数 | 1: 2, 2: 8 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_case_evidence | 2 |
| missing_policy | 3 |
| missing_review | 1 |
| missing_structured_entity | 2 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 3 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_case_evidence: 1, missing_policy: 1 |
| recommendation | missing_review: 1, missing_structured_entity: 2 |
| support | missing_case_evidence: 1, missing_policy: 2 |

## 原始 JSON

```json
{
  "suite": "humanlike_single_turn_resolvable",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\humanlike_single_turn_resolvable.jsonl",
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
    "precision@5": 0.24,
    "recall@5": 0.315,
    "mrr": 0.5,
    "ndcg@5": 0.328,
    "exact_recall@5": 0.5,
    "acceptable_recall@5": 0.6,
    "entity_accuracy@5": 0.6,
    "aspect_accuracy@5": 0.8,
    "forbidden_rate@5": 0.0
  },
  "support_quality": {
    "action_accuracy": 0.7,
    "citation_ok": 0.7,
    "citation_leak_rate": 0.0,
    "citation_schema_ok": 0.7,
    "answer_citation_precision": 0.7,
    "answer_citation_recall": 0.3333,
    "citation_grounded_rate": 0.7,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.71
  },
  "latency": {
    "p50_ms": 24212,
    "p95_ms": 72438
  },
  "by_intent": {
    "customer_ops": {
      "n": 4,
      "retrieval": {
        "precision@5": 0.3,
        "recall@5": 0.3542,
        "mrr": 0.625,
        "ndcg@5": 0.3853
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 0.5625,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.7074
      }
    },
    "recommendation": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.0667,
        "recall@5": 0.1111,
        "mrr": 0.3333,
        "ndcg@5": 0.1564
      },
      "support_quality": {
        "action_accuracy": 0.3333,
        "citation_ok": 0.3333,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.3333,
        "answer_citation_precision": 0.3333,
        "answer_citation_recall": 0.0833,
        "citation_grounded_rate": 0.3333,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.9189
      }
    },
    "support": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.3333,
        "recall@5": 0.4667,
        "mrr": 0.5,
        "ndcg@5": 0.423
      },
      "support_quality": {
        "action_accuracy": 0.6667,
        "citation_ok": 0.6667,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.6667,
        "answer_citation_precision": 0.6667,
        "answer_citation_recall": 0.2778,
        "citation_grounded_rate": 0.6667,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.5044
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 10,
      "retrieval": {
        "precision@5": 0.24,
        "recall@5": 0.315,
        "mrr": 0.5,
        "ndcg@5": 0.328
      },
      "support_quality": {
        "action_accuracy": 0.7,
        "citation_ok": 0.7,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.7,
        "answer_citation_precision": 0.7,
        "answer_citation_recall": 0.3333,
        "citation_grounded_rate": 0.7,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.71
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 45,
      "dense": 45,
      "policy_fallback": 2
    },
    "relevant_hit_signal_counts": {
      "bm25": 12,
      "dense": 12
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "bm25": 6,
        "dense": 6
      },
      "recommendation": {
        "bm25": 1,
        "dense": 1
      },
      "support": {
        "bm25": 5,
        "dense": 5
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 7,
      "refuse": 3
    },
    "attempt_counts": {
      "1": 2,
      "2": 8
    },
    "retry_rate": 0.8,
    "evidence_gap_counts": {
      "missing_case_evidence": 2,
      "missing_policy": 3,
      "missing_review": 1,
      "missing_structured_entity": 2
    },
    "citation_failure_counts": {
      "missing_answer_citation": 3
    },
    "evidence_gaps_by_intent": {
      "customer_ops": {
        "missing_case_evidence": 1,
        "missing_policy": 1
      },
      "recommendation": {
        "missing_review": 1,
        "missing_structured_entity": 2
      },
      "support": {
        "missing_case_evidence": 1,
        "missing_policy": 2
      }
    }
  },
  "retrieval_rows": [
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
        "kb:KB004_shipping_delivery_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-005",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 4,
          "bm25_rank": 8,
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
          "dense_rank": 24,
          "bm25_rank": 26,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "kb:KB004_shipping_delivery_policy",
          "doc_type": "policy_markdown",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 6,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
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
        "review:AS-All_Beauty-B089R7S73D-price_value",
        "review:RV-AMZREV-Baby_Products-02556",
        "product:PP-Baby_Products-B07CJ3ZGJS",
        "product:PP-Baby_Products-B09BNX78XR",
        "ticket:FAQ-Baby_Products-0157"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:AS-All_Beauty-B089R7S73D-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 9,
          "bm25_rank": 10,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Baby_Products-02556",
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
          "doc_id": "product:PP-Baby_Products-B07CJ3ZGJS",
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
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B09BNX78XR",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Baby_Products-0157",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 28,
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
      "ndcg@5": 0.8854598815714874,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0003",
        "product:PP-Baby_Products-B0BHDLD45H",
        "product:PP-All_Beauty-B08DHTJ25J",
        "review:CL-All_Beauty-skin_scent",
        "review:RV-AMZREV-All_Beauty-00008"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0003",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 7,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B0BHDLD45H",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 34,
          "bm25_rank": 20,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-All_Beauty-B08DHTJ25J",
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
          "rank": 4,
          "doc_id": "review:CL-All_Beauty-skin_scent",
          "doc_type": "complaint_cluster",
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
          "doc_id": "review:RV-AMZREV-All_Beauty-00008",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
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
        "product:PP-Baby_Products-B075GSYNJ7",
        "product:PP-Baby_Products-B00I3WEXPU",
        "product:PP-Baby_Products-B07258QRSV",
        "product:PP-Baby_Products-B00I3WEXX2",
        "review:RV-AMZREV-Baby_Products-02768"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B075GSYNJ7",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 29,
          "bm25_rank": 27,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "product:PP-Baby_Products-B00I3WEXPU",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 26,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B07258QRSV",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 9,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Baby_Products-B00I3WEXX2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 24,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02768",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 17,
          "bm25_rank": 42,
          "signals": [
            "dense",
            "bm25"
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
        "kb:KB001_return_refund_policy"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:R-007",
          "doc_type": "review",
          "relevant": false,
          "dense_rank": 3,
          "bm25_rank": 6,
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
          "dense_rank": 8,
          "bm25_rank": 8,
          "signals": [
            "dense",
            "bm25",
            "policy_fallback"
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
      "precision@5": 0.6,
      "recall@5": 0.75,
      "mrr": 0.5,
      "ndcg@5": 0.5654495432396527,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "ticket:FAQ-All_Beauty-0001",
        "review:RV-AMZREV-All_Beauty-00005",
        "review:RV-AMZREV-Baby_Products-02467",
        "review:RV-AMZREV-All_Beauty-03336",
        "product:PP-All_Beauty-B08BBQ29N5"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "ticket:FAQ-All_Beauty-0001",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 5,
          "bm25_rank": 2,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-All_Beauty-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 6,
          "bm25_rank": 4,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "review:RV-AMZREV-Baby_Products-02467",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 10,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
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
          "rank": 5,
          "doc_id": "product:PP-All_Beauty-B08BBQ29N5",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 3,
          "bm25_rank": 3,
          "signals": [
            "dense",
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
        "product:PP-Software-B018IOV40E",
        "review:RV-AMZREV-Software-00005",
        "product:PP-Baby_Products-B09CFFM49C",
        "product:PP-Software-B0052OSTOS",
        "ticket:FAQ-Software-0157"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B018IOV40E",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 37,
          "bm25_rank": 18,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 2,
          "doc_id": "review:RV-AMZREV-Software-00005",
          "doc_type": "review_evidence",
          "relevant": true,
          "dense_rank": 38,
          "bm25_rank": 5,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B09CFFM49C",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 8,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B0052OSTOS",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 27,
          "bm25_rank": 19,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "ticket:FAQ-Software-0157",
          "doc_type": "faq_case",
          "relevant": false,
          "dense_rank": 49,
          "bm25_rank": 50,
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
      "precision@5": 0.2,
      "recall@5": 0.16666666666666666,
      "mrr": 1.0,
      "ndcg@5": 0.3391602052736161,
      "exact_recall@5": 0.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "product:PP-Baby_Products-B08L25DYPS",
        "review:AS-Baby_Products-B0BQMR9VLK-skin_scent",
        "product:PP-Baby_Products-B08ZM22VF6",
        "review:AS-Baby_Products-B0BMQ3G124-skin_scent",
        "review:RV-AMZREV-Baby_Products-02894"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Baby_Products-B08L25DYPS",
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
          "doc_id": "review:AS-Baby_Products-B0BQMR9VLK-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 2,
          "bm25_rank": 11,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Baby_Products-B08ZM22VF6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 15,
          "bm25_rank": 14,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:AS-Baby_Products-B0BMQ3G124-skin_scent",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 7,
          "bm25_rank": 13,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:RV-AMZREV-Baby_Products-02894",
          "doc_type": "review_evidence",
          "relevant": false,
          "dense_rank": 18,
          "bm25_rank": 21,
          "signals": [
            "dense",
            "bm25"
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
      "mrr": 0.5,
      "ndcg@5": 0.38356636737133565,
      "exact_recall@5": 1.0,
      "acceptable_recall@5": 1.0,
      "entity_accuracy@5": 1.0,
      "aspect_accuracy@5": 1.0,
      "forbidden_rate@5": 0.0,
      "retrieved": [
        "review:RV-AMZREV-Baby_Products-00876",
        "product:PP-All_Beauty-B07J3GH1W1",
        "ticket:FAQ-All_Beauty-0007",
        "review:RV-AMZREV-All_Beauty-00228",
        "review:AS-All_Beauty-B07H281V4V-price_value"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "review:RV-AMZREV-Baby_Products-00876",
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
          "rank": 2,
          "doc_id": "product:PP-All_Beauty-B07J3GH1W1",
          "doc_type": "product_profile",
          "relevant": true,
          "dense_rank": 27,
          "bm25_rank": 17,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "ticket:FAQ-All_Beauty-0007",
          "doc_type": "faq_case",
          "relevant": true,
          "dense_rank": 34,
          "bm25_rank": 22,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "review:RV-AMZREV-All_Beauty-00228",
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
          "rank": 5,
          "doc_id": "review:AS-All_Beauty-B07H281V4V-price_value",
          "doc_type": "review_aspect_summary",
          "relevant": false,
          "dense_rank": 6,
          "bm25_rank": 1,
          "signals": [
            "dense",
            "bm25"
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
        "product:PP-Software-B00004TTHU",
        "product:PP-Software-B0857HM2N6",
        "product:PP-Software-B00I07OWW2",
        "product:PP-Software-B00C9E1UEA",
        "review:CL-Software-delivery"
      ],
      "signals": [
        {
          "rank": 1,
          "doc_id": "product:PP-Software-B00004TTHU",
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
          "doc_id": "product:PP-Software-B0857HM2N6",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 45,
          "bm25_rank": 51,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 3,
          "doc_id": "product:PP-Software-B00I07OWW2",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 24,
          "bm25_rank": 33,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 4,
          "doc_id": "product:PP-Software-B00C9E1UEA",
          "doc_type": "product_profile",
          "relevant": false,
          "dense_rank": 23,
          "bm25_rank": 32,
          "signals": [
            "dense",
            "bm25"
          ]
        },
        {
          "rank": 5,
          "doc_id": "review:CL-Software-delivery",
          "doc_type": "complaint_cluster",
          "relevant": false,
          "dense_rank": 38,
          "bm25_rank": 31,
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
      "query_id": "H-0009",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
          "doc_id": "R-005",
          "chunk_id": "2a1a90c64b8a0e30",
          "rank": 1,
          "doc_type": "review"
        },
        {
          "source": "ticket",
          "doc_id": "T-003",
          "chunk_id": "fd4a83c3beaecf88",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.4597,
      "answer_preview": "Based on the evidence pack, a recurring issue related to license activation is customers not receiving the license key email after purchase. One review for **PDF Studio Pro License** reports receiving a rating of 1 because the license key w"
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
      "groundedness_proxy": 0.8896,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "H-0025",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "refuse",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
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
      "groundedness_proxy": 0.1554,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    },
    {
      "query_id": "H-0029",
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
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "AS-Baby_Products-B00NZF1466-missing_parts",
          "chunk_id": "928c507e91838bfd",
          "rank": 1,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-Baby_Products-02768",
          "chunk_id": "847153639b6ada77",
          "rank": 2,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-Baby_Products-04425",
          "chunk_id": "fbbf148568b4445d",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-Baby_Products-00431",
          "chunk_id": "787284a0950c1688",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "{ \"answer\": \"The item designed for feeding that helps reduce colic is the **Anti-Colic Glass Bottle Set** (Product ID: P-BABY-002, Price: $28.00, Rating: 4.6/5). \", \"citations\": [], \"tool_citations\": [ \"\" ]\n}. [doc:review:AS-Baby_Products-B"
    },
    {
      "query_id": "H-0039",
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
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 1,
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
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.3579,
      "answer_preview": "I cannot answer your question based on the available evidence. The provided records do not contain any information about streaming plans, advertised features, or a policy on incomplete orders. The only tickets in the evidence cover a hair d"
    },
    {
      "query_id": "H-0058",
      "expected_intent": "customer_ops",
      "intent": "customer_ops",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "review",
          "doc_id": "AS-Baby_Products-B07C2HRMRF-refund_return",
          "chunk_id": "1841db9159d1da57",
          "rank": 1,
          "doc_type": "review_aspect_summary"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-00005",
          "chunk_id": "aec017377b8876ed",
          "rank": 2,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-03336",
          "chunk_id": "19186cfd12380494",
          "rank": 3,
          "doc_type": "review_evidence"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-All_Beauty-02240",
          "chunk_id": "23f2dc19a46efda6",
          "rank": 4,
          "doc_type": "review_evidence"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I need to check the provided evidence. The structured facts only mention a software product (PDF Studio Pro License), and all document evidence has been dropped due to product mismatch. There is no information about faux locs or sizing. Sin"
    },
    {
      "query_id": "H-0060",
      "expected_intent": "customer_ops",
      "intent": "recommendation",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
          "doc_id": "PP-Software-B018IOV40E",
          "chunk_id": "223275c6aa43baef",
          "rank": 1,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-Software-00005",
          "chunk_id": "569a0085b9818981",
          "rank": 2,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-Baby_Products-B09CFFM49C",
          "chunk_id": "7e0b7067ea036784",
          "rank": 3,
          "doc_type": "product_profile"
        },
        {
          "source": "product",
          "doc_id": "PP-Software-B0052OSTOS",
          "chunk_id": "1bf9ab7fb02ab68f",
          "rank": 4,
          "doc_type": "product_profile"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the provided evidence, the **NBC** software product allows you to see \"the voice\" anytime, as noted in a customer review. - [doc:product:PP-Software-B018IOV40E#223275c6aa43baef] - [doc:review:RV-AMZREV-Software-00005#569a0085b98189"
    },
    {
      "query_id": "H-0068",
      "expected_intent": "customer_ops",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_case_evidence",
        "missing_policy"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 0.5,
      "citation_grounded_rate": 1.0,
      "citation_count": 2,
      "answer_citation_count": 1,
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
          "source": "ticket",
          "doc_id": "T-001",
          "chunk_id": "d9c7c01c76812a84",
          "rank": 2,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 0.37,
      "answer_preview": "I'm sorry, but I cannot answer your question based on the available information. The evidence pack does not contain any data about washcloths, nor does it include any products described as gentle or free of strong scents for sensitive skin."
    },
    {
      "query_id": "H-0073",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 1,
      "evidence_gaps": [],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
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
          "doc_id": "FAQ-All_Beauty-0007",
          "chunk_id": "2400bf8b5413259d",
          "rank": 1,
          "doc_type": "faq_case"
        },
        {
          "source": "ticket",
          "doc_id": "FAQ-Baby_Products-0047",
          "chunk_id": "c82b6f1ec2556ce3",
          "rank": 2,
          "doc_type": "faq_case"
        },
        {
          "source": "kb",
          "doc_id": "scanned_damage_claim",
          "chunk_id": "b574afb70eabbf5a",
          "rank": 3,
          "doc_type": "ocr_image"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot provide information about the price or value of the “Powergrooming Nail Clipper Set” because it does not appear in the available evidence. The product search results included only an anti‑colic glass bottle set and a PDF software l"
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
      "groundedness_proxy": 0.867,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    }
  ]
}
```
