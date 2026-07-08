# 评测报告

本报告由 `python -m commerce_rag_ops.cli eval` 生成。

- Suite: humanlike_single_turn_resolvable
- Eval path: E:\code\agent\deepsearch\commerce-rag-ops\data\eval\humanlike_single_turn_resolvable.jsonl
- Oracle sources: False

## 摘要

- 样本数: 10
- 检索后端: local
- 检索模式: hybrid_rerank
- Precision@5: 0.18
- Recall@5: 0.24
- MRR: 0.225
- NDCG@5: 0.2233
- exact_recall@5: 0.3
- acceptable_recall@5: 0.3
- entity_accuracy@5: 0.3
- aspect_accuracy@5: 0.7
- forbidden_rate@5: 0.0
- Action accuracy: 0.7
- 引用率: 0.7
- Citation leak rate(refuse/clarify): 0.0
- Citation schema OK: 0.7
- Answer citation precision/recall: 0.7 / 0.4833
- Citation grounded rate: 0.7
- 关键词覆盖率: 1.0
- groundedness 代理指标: 0.9
- 延迟 p50/p95: 24814 ms / 45374 ms
- Embedding 模型: local-token-cosine
- Reranker 模型: none
- LLM 模型: deepseek-v4-flash

## 按意图分组

| 意图 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| customer_ops | 4 | 0.2 | 0.25 | 0.25 | 0.239 | 1.0 | 1.0 | 1.0 / 0.6458 | 1.0 |
| recommendation | 3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.3333 | 0.3333 | 0.3333 / 0.0833 | 1.0 |
| support | 3 | 0.3333 | 0.4667 | 0.4167 | 0.4258 | 0.6667 | 0.6667 | 0.6667 / 0.6667 | 1.0 |

## 按难度分组

| 难度 | N | Precision@5 | Recall@5 | MRR | NDCG@5 | 引用 | Citation schema | Answer citation P/R | 关键词 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| unknown | 10 | 0.18 | 0.24 | 0.225 | 0.2233 | 0.7 | 0.7 | 0.7 / 0.4833 | 1.0 |

## 检索诊断

| 信号 | 返回次数 | 命中相关次数 |
|---|---:|---:|
| bm25 | 22 | 9 |
| dense | 23 | 7 |
| forced_fallback | 11 | 0 |
| policy_fallback | 1 | 0 |

### 按意图统计的相关命中信号

| 意图 | 信号计数 |
|---|---|
| customer_ops | bm25: 4, dense: 4 |
| support | bm25: 5, dense: 3 |

## Agentic 证据诊断

- 重试率: 0.9

### 动作与尝试次数

| 类型 | 计数 |
|---|---|
| 动作 | answer: 7, refuse: 3 |
| 尝试次数 | 1: 1, 2: 9 |

### 证据缺口

| 缺口 | 次数 |
|---|---:|
| missing_case_evidence | 3 |
| missing_policy | 4 |
| missing_review | 1 |
| missing_structured_entity | 2 |
| no_context | 1 |

### Citation schema 失败原因

| 原因 | 次数 |
|---|---:|
| missing_answer_citation | 3 |

### 按意图统计的证据缺口

| 意图 | 缺口计数 |
|---|---|
| customer_ops | missing_case_evidence: 1, missing_policy: 1 |
| recommendation | missing_review: 1, missing_structured_entity: 2 |
| support | missing_case_evidence: 2, missing_policy: 3, no_context: 1 |

## 原始 JSON

```json
{
  "suite": "humanlike_single_turn_resolvable",
  "eval_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\eval\\humanlike_single_turn_resolvable.jsonl",
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
    "precision@5": 0.18,
    "recall@5": 0.24,
    "mrr": 0.225,
    "ndcg@5": 0.2233,
    "exact_recall@5": 0.3,
    "acceptable_recall@5": 0.3,
    "entity_accuracy@5": 0.3,
    "aspect_accuracy@5": 0.7,
    "forbidden_rate@5": 0.0
  },
  "support_quality": {
    "action_accuracy": 0.7,
    "citation_ok": 0.7,
    "citation_leak_rate": 0.0,
    "citation_schema_ok": 0.7,
    "answer_citation_precision": 0.7,
    "answer_citation_recall": 0.4833,
    "citation_grounded_rate": 0.7,
    "keyword_coverage": 1.0,
    "groundedness_proxy": 0.9
  },
  "latency": {
    "p50_ms": 24814,
    "p95_ms": 45374
  },
  "by_intent": {
    "customer_ops": {
      "n": 4,
      "retrieval": {
        "precision@5": 0.2,
        "recall@5": 0.25,
        "mrr": 0.25,
        "ndcg@5": 0.239
      },
      "support_quality": {
        "action_accuracy": 1.0,
        "citation_ok": 1.0,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 1.0,
        "answer_citation_precision": 1.0,
        "answer_citation_recall": 0.6458,
        "citation_grounded_rate": 1.0,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
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
        "action_accuracy": 0.3333,
        "citation_ok": 0.3333,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.3333,
        "answer_citation_precision": 0.3333,
        "answer_citation_recall": 0.0833,
        "citation_grounded_rate": 0.3333,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 1.0
      }
    },
    "support": {
      "n": 3,
      "retrieval": {
        "precision@5": 0.3333,
        "recall@5": 0.4667,
        "mrr": 0.4167,
        "ndcg@5": 0.4258
      },
      "support_quality": {
        "action_accuracy": 0.6667,
        "citation_ok": 0.6667,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.6667,
        "answer_citation_precision": 0.6667,
        "answer_citation_recall": 0.6667,
        "citation_grounded_rate": 0.6667,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.6667
      }
    }
  },
  "by_difficulty": {
    "unknown": {
      "n": 10,
      "retrieval": {
        "precision@5": 0.18,
        "recall@5": 0.24,
        "mrr": 0.225,
        "ndcg@5": 0.2233
      },
      "support_quality": {
        "action_accuracy": 0.7,
        "citation_ok": 0.7,
        "citation_leak_rate": 0.0,
        "citation_schema_ok": 0.7,
        "answer_citation_precision": 0.7,
        "answer_citation_recall": 0.4833,
        "citation_grounded_rate": 0.7,
        "keyword_coverage": 1.0,
        "groundedness_proxy": 0.9
      }
    }
  },
  "retrieval_diagnostics": {
    "returned_signal_counts": {
      "bm25": 22,
      "dense": 23,
      "forced_fallback": 11,
      "policy_fallback": 1
    },
    "relevant_hit_signal_counts": {
      "bm25": 9,
      "dense": 7
    },
    "relevant_hit_signals_by_intent": {
      "customer_ops": {
        "bm25": 4,
        "dense": 4
      },
      "support": {
        "bm25": 5,
        "dense": 3
      }
    }
  },
  "agentic_diagnostics": {
    "action_counts": {
      "answer": 7,
      "refuse": 3
    },
    "attempt_counts": {
      "1": 1,
      "2": 9
    },
    "retry_rate": 0.9,
    "evidence_gap_counts": {
      "missing_case_evidence": 3,
      "missing_policy": 4,
      "missing_review": 1,
      "missing_structured_entity": 2,
      "no_context": 1
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
        "missing_case_evidence": 2,
        "missing_policy": 3,
        "no_context": 1
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
      "citation_count": 4,
      "answer_citation_count": 4,
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
        },
        {
          "source": "review",
          "doc_id": "R-007",
          "chunk_id": "78076c5983e8c9cd",
          "rank": 3,
          "doc_type": "review"
        },
        {
          "source": "ticket",
          "doc_id": "T-004",
          "chunk_id": "d85e1613389da6aa",
          "rank": 4,
          "doc_type": "ticket"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available evidence, the common complaints related to license activation and content access are: - **Not receiving the license key email**: A customer reported that they never received the license key email for the PDF Studio Pr"
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
      "groundedness_proxy": 1.0,
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
        "no_context"
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
          "source": "review",
          "doc_id": "R-002",
          "chunk_id": "406fae475bd443e7",
          "rank": 4,
          "doc_type": "review"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "The **Anti-Colic Glass Bottle Set** is the item designed for feeding and intended to help reduce colic. [doc:review:R-012#00becedaf80dda0e]"
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
        "missing_policy",
        "missing_case_evidence"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 1,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 1,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot provide a complete answer because the available evidence does not include a policy that addresses “incomplete orders” for a streaming plan. The only policy provided is the Warranty Policy, which applies to electronics and powered b"
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
      "answer_citation_recall": 0.3333,
      "citation_grounded_rate": 1.0,
      "citation_count": 3,
      "answer_citation_count": 1,
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
        },
        {
          "source": "product",
          "doc_id": "P-SOFT-001",
          "chunk_id": "379d92ed1d5b4648",
          "rank": 3,
          "doc_type": "product"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I'm sorry, but I cannot answer your question about whether the faux locs run small. The evidence pack provided for this query contains only information about a software product (PDF Studio Pro License), including a review and a support tick"
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
      "answer_citation_recall": 0.25,
      "citation_grounded_rate": 1.0,
      "citation_count": 4,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "product",
          "doc_id": "PP-Software-B005ZKAXBG",
          "chunk_id": "ab45b8e31f8af498",
          "rank": 1,
          "doc_type": "product_profile"
        },
        {
          "source": "review",
          "doc_id": "RV-AMZREV-Software-02219",
          "chunk_id": "c1f316583a9ef405",
          "rank": 2,
          "doc_type": "review_evidence"
        },
        {
          "source": "product",
          "doc_id": "PP-Baby_Products-B08MY6543N",
          "chunk_id": "365ec74803c7b1c1",
          "rank": 3,
          "doc_type": "product_profile"
        },
        {
          "source": "product",
          "doc_id": "PP-Software-B005M4T8L6",
          "chunk_id": "191eb298609c2e13",
          "rank": 4,
          "doc_type": "product_profile"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "Based on the available evidence, I cannot identify a product that allows you to \"see the voice anytime.\" The only voice‑related item in the evidence pack is the **Simple Voice Changer** ([doc:product:PP-Software-B005M4T8L6#191eb298609c2e13]"
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
        "missing_policy",
        "missing_case_evidence"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 1,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 1,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I cannot answer your question because the provided evidence does not contain any information about washcloths, baby skin sensitivity, or product scents. The only product data available is for a vitamin C serum and a hair dryer, and the only"
    },
    {
      "query_id": "H-0073",
      "expected_intent": "support",
      "intent": "support",
      "expected_action": "answer",
      "safety_category": "normal",
      "difficulty": "unknown",
      "action": "answer",
      "attempts": 2,
      "evidence_gaps": [
        "missing_policy",
        "missing_case_evidence"
      ],
      "action_accuracy": 1.0,
      "citation_ok": 1.0,
      "citation_leak_rate": 0.0,
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "citation_grounded_rate": 1.0,
      "citation_count": 1,
      "answer_citation_count": 1,
      "citation_failures": [],
      "citation_payload": [
        {
          "source": "kb",
          "doc_id": "KB002_warranty_policy",
          "chunk_id": "59391347ce77614f",
          "rank": 1,
          "doc_type": "policy_markdown"
        }
      ],
      "keyword_coverage": 1.0,
      "groundedness_proxy": 1.0,
      "answer_preview": "I could not find any information about the \"powergrooming nail clipper set\" in the provided evidence pack. The available product data includes only an \"Anti-Colic Glass Bottle Set\" and a \"PDF Studio Pro License,\" with no mention of the nail"
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
      "groundedness_proxy": 1.0,
      "answer_preview": "I do not have enough grounded context to answer this safely. Please provide the SKU, order detail, or let me escalate this to a human support specialist."
    }
  ]
}
```
