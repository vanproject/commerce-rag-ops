# 检索消融报告

本报告比较 dense-only、BM25-only、hybrid RRF、以及带 rerank 的 hybrid RRF。

| 模式 | Precision@5 | Recall@5 | MRR | NDCG@5 |
|---|---:|---:|---:|---:|
| dense | 0.4333 | 0.9583 | 1.0 | 0.9512 |
| bm25 | 0.4333 | 0.9583 | 1.0 | 0.9192 |
| hybrid | 0.4333 | 0.9583 | 1.0 | 0.9512 |
| hybrid_rerank | 0.4333 | 0.9583 | 1.0 | 0.9515 |

## 原始 JSON

```json
{
  "n": 6,
  "modes": {
    "dense": {
      "summary": {
        "precision@5": 0.4333,
        "recall@5": 0.9583,
        "mrr": 1.0,
        "ndcg@5": 0.9512
      },
      "rows": [
        {
          "query_id": "Q-001",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-001",
            "kb:KB001_return_refund_policy",
            "ticket:T-004",
            "ticket:T-006",
            "kb:KB004_shipping_delivery_policy"
          ]
        },
        {
          "query_id": "Q-002",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-002",
            "kb:KB002_warranty_policy",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        },
        {
          "query_id": "Q-003",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-BABY-001",
            "review:R-010",
            "review:R-004",
            "review:R-009",
            "review:R-011"
          ]
        },
        {
          "query_id": "Q-004",
          "precision@5": 0.6,
          "recall@5": 0.75,
          "mrr": 1.0,
          "ndcg@5": 0.787702056960637,
          "retrieved": [
            "review:R-009",
            "ticket:T-005",
            "review:R-010",
            "review:R-011",
            "review:R-012"
          ]
        },
        {
          "query_id": "Q-005",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "kb:KB004_shipping_delivery_policy",
            "product:P-SOFT-001",
            "kb:KB001_return_refund_policy",
            "kb:KB001_return_refund_policy",
            "product:P-BEAUTY-002"
          ]
        },
        {
          "query_id": "Q-006",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 0.9197207891481876,
          "retrieved": [
            "ticket:T-004",
            "ticket:T-001",
            "kb:KB003_payment_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        }
      ]
    },
    "bm25": {
      "summary": {
        "precision@5": 0.4333,
        "recall@5": 0.9583,
        "mrr": 1.0,
        "ndcg@5": 0.9192
      },
      "rows": [
        {
          "query_id": "Q-001",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-001",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "ticket:T-004",
            "kb:KB003_payment_refund_policy"
          ]
        },
        {
          "query_id": "Q-002",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-002",
            "kb:KB002_warranty_policy",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        },
        {
          "query_id": "Q-003",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-BABY-001",
            "review:R-010",
            "product:P-BABY-002",
            "review:R-004",
            "review:R-002"
          ]
        },
        {
          "query_id": "Q-004",
          "precision@5": 0.6,
          "recall@5": 0.75,
          "mrr": 1.0,
          "ndcg@5": 0.787702056960637,
          "retrieved": [
            "ticket:T-005",
            "review:R-009",
            "review:R-010",
            "review:R-011",
            "review:R-012"
          ]
        },
        {
          "query_id": "Q-005",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 0.8503449055347546,
          "retrieved": [
            "product:P-SOFT-001",
            "kb:KB001_return_refund_policy",
            "kb:KB005_missing_parts_policy",
            "kb:KB001_return_refund_policy",
            "kb:KB004_shipping_delivery_policy"
          ]
        },
        {
          "query_id": "Q-006",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 0.8772153153380493,
          "retrieved": [
            "ticket:T-004",
            "ticket:T-001",
            "ticket:T-006",
            "kb:KB003_payment_refund_policy",
            "kb:KB001_return_refund_policy"
          ]
        }
      ]
    },
    "hybrid": {
      "summary": {
        "precision@5": 0.4333,
        "recall@5": 0.9583,
        "mrr": 1.0,
        "ndcg@5": 0.9512
      },
      "rows": [
        {
          "query_id": "Q-001",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-001",
            "kb:KB001_return_refund_policy",
            "ticket:T-004",
            "ticket:T-006",
            "kb:KB003_payment_refund_policy"
          ]
        },
        {
          "query_id": "Q-002",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-002",
            "kb:KB002_warranty_policy",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        },
        {
          "query_id": "Q-003",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-BABY-001",
            "review:R-010",
            "review:R-004",
            "product:P-BABY-002",
            "review:R-009"
          ]
        },
        {
          "query_id": "Q-004",
          "precision@5": 0.6,
          "recall@5": 0.75,
          "mrr": 1.0,
          "ndcg@5": 0.787702056960637,
          "retrieved": [
            "review:R-009",
            "ticket:T-005",
            "review:R-010",
            "review:R-011",
            "review:R-012"
          ]
        },
        {
          "query_id": "Q-005",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-SOFT-001",
            "kb:KB004_shipping_delivery_policy",
            "kb:KB001_return_refund_policy",
            "kb:KB001_return_refund_policy",
            "kb:KB005_missing_parts_policy"
          ]
        },
        {
          "query_id": "Q-006",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 0.9197207891481876,
          "retrieved": [
            "ticket:T-004",
            "ticket:T-001",
            "kb:KB003_payment_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        }
      ]
    },
    "hybrid_rerank": {
      "summary": {
        "precision@5": 0.4333,
        "recall@5": 0.9583,
        "mrr": 1.0,
        "ndcg@5": 0.9515
      },
      "rows": [
        {
          "query_id": "Q-001",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-001",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "ticket:T-004",
            "kb:KB004_shipping_delivery_policy"
          ]
        },
        {
          "query_id": "Q-002",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "ticket:T-002",
            "kb:KB002_warranty_policy",
            "kb:KB001_return_refund_policy",
            "ticket:T-006",
            "kb:KB001_return_refund_policy"
          ]
        },
        {
          "query_id": "Q-003",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-BABY-001",
            "review:R-010",
            "product:P-BABY-002",
            "review:R-002",
            "review:R-004"
          ]
        },
        {
          "query_id": "Q-004",
          "precision@5": 0.6,
          "recall@5": 0.75,
          "mrr": 1.0,
          "ndcg@5": 0.8318724637288826,
          "retrieved": [
            "review:R-009",
            "review:R-012",
            "ticket:T-005",
            "review:R-010",
            "review:R-011"
          ]
        },
        {
          "query_id": "Q-005",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 1.0,
          "retrieved": [
            "product:P-SOFT-001",
            "kb:KB004_shipping_delivery_policy",
            "kb:KB001_return_refund_policy",
            "kb:KB001_return_refund_policy",
            "kb:KB005_missing_parts_policy"
          ]
        },
        {
          "query_id": "Q-006",
          "precision@5": 0.4,
          "recall@5": 1.0,
          "mrr": 1.0,
          "ndcg@5": 0.8772153153380493,
          "retrieved": [
            "ticket:T-004",
            "ticket:T-001",
            "ticket:T-006",
            "kb:KB003_payment_refund_policy",
            "kb:KB001_return_refund_policy"
          ]
        }
      ]
    }
  }
}
```
