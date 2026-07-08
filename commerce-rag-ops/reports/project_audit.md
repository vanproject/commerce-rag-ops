# 项目覆盖审计

## 数据量统计

| 数据 | 数量 |
|---|---:|
| products | 6 |
| reviews | 12 |
| support_tickets | 6 |
| kb_chunks | 14 |
| orders | 4 |
| customer_segments | 4 |
| processed_chunks | 42737 |
| golden_eval_queries | 366 |

## 文档摄取

- 已抽取知识文档: 9
- 跳过文件数: 1

| 文档类型 | 数量 |
|---|---:|
| html_policy_page | 1 |
| ocr_image | 1 |
| policy_markdown | 5 |
| structured_table | 1 |
| text_notice | 1 |

| 抽取方法 | 数量 |
|---|---:|
| csv_dict_reader | 1 |
| html_text_parser | 1 |
| plain_text | 6 |
| sidecar_ocr_text | 1 |

跳过示例:
- `E:\code\agent\deepsearch\commerce-rag-ops\data\raw\knowledge_assets\unsupported_vendor_export.xlsx`: unsupported_suffix

## Amazon 规模化子集

- 商品数: 3000
- 评论数: 15000
- RAG 文档数: 19969
- Golden 评测问题数: 366

| 生成文档类型 | 数量 |
|---|---:|
| product_profile | 3000 |
| review_evidence | 15000 |
| review_aspect_summary | 1405 |
| complaint_cluster | 24 |
| faq_case | 540 |

## 公共数据下载

- Amazon 商品样本存在: True
- Amazon 商品样本行数: 20
- Amazon 评论样本存在: True
- Amazon 评论样本行数: 20
- Amazon 全量 manifest 存在: True
- Amazon 全量分类: All_Beauty, Software, Baby_Products

## 运行时后端

- 本地 Qdrant 路径: E:\code\agent\deepsearch\commerce-rag-ops\.qdrant
- 本地 Qdrant 路径存在: True
- Qdrant embedding 后端: sentence-transformers
- Qdrant embedding 模型: BAAI/bge-large-en-v1.5
- SQLite 结构化库: E:\code\agent\deepsearch\commerce-rag-ops\data\structured\commerce.db
- SQLite 存在: True
- LLM endpoint 已配置: True
- LLM API key 已配置: True
- LLM 模型: deepseek-v4-flash

## 原始 JSON

```json
{
  "data_counts": {
    "products": 6,
    "reviews": 12,
    "support_tickets": 6,
    "kb_chunks": 14,
    "orders": 4,
    "customer_segments": 4,
    "processed_chunks": 42737,
    "golden_eval_queries": 366
  },
  "document_ingestion": {
    "knowledge_documents": 9,
    "document_types": {
      "html_policy_page": 1,
      "ocr_image": 1,
      "policy_markdown": 5,
      "structured_table": 1,
      "text_notice": 1
    },
    "extraction_methods": {
      "csv_dict_reader": 1,
      "html_text_parser": 1,
      "plain_text": 6,
      "sidecar_ocr_text": 1
    },
    "skipped_files": [
      {
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\knowledge_assets\\unsupported_vendor_export.xlsx",
        "reason": "unsupported_suffix",
        "suffix": ".xlsx"
      }
    ]
  },
  "scale_subset": {
    "source": "Amazon Reviews 2023 full gzip subset",
    "categories": [
      {
        "category": "All_Beauty",
        "reviews": 5000,
        "products": 1000,
        "avg_rating": 4.1826
      },
      {
        "category": "Software",
        "reviews": 5000,
        "products": 1000,
        "avg_rating": 3.843
      },
      {
        "category": "Baby_Products",
        "reviews": 5000,
        "products": 1000,
        "avg_rating": 4.3582
      }
    ],
    "reviews_per_category_target": 5000,
    "products_per_category_limit": 1000,
    "products": 3000,
    "reviews": 15000,
    "rag_documents": 19969,
    "golden_eval_queries": 366,
    "document_types": {
      "product_profile": 3000,
      "review_evidence": 15000,
      "review_aspect_summary": 1405,
      "complaint_cluster": 24,
      "faq_case": 540
    }
  },
  "public_data_downloads": {
    "amazon_products_sample_exists": true,
    "amazon_products_sample_rows": 20,
    "amazon_reviews_sample_exists": true,
    "amazon_reviews_sample_rows": 20,
    "amazon_full_manifest_exists": true,
    "amazon_full_manifest_path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\manifest.json",
    "amazon_full_categories": [
      "All_Beauty",
      "Software",
      "Baby_Products"
    ],
    "amazon_full_files": [
      {
        "category": "All_Beauty",
        "kind": "reviews",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/All_Beauty.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\All_Beauty\\reviews.jsonl.gz",
        "bytes": 94441517,
        "rows": 701528
      },
      {
        "category": "All_Beauty",
        "kind": "metadata",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_All_Beauty.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\All_Beauty\\metadata.jsonl.gz",
        "bytes": 39871253,
        "rows": 112590
      },
      {
        "category": "Software",
        "kind": "reviews",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Software.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\Software\\reviews.jsonl.gz",
        "bytes": 496076370,
        "rows": 4880181
      },
      {
        "category": "Software",
        "kind": "metadata",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Software.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\Software\\metadata.jsonl.gz",
        "bytes": 64165835,
        "rows": 89251
      },
      {
        "category": "Baby_Products",
        "kind": "reviews",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Baby_Products.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\Baby_Products\\reviews.jsonl.gz",
        "bytes": 837501465,
        "rows": 6028884
      },
      {
        "category": "Baby_Products",
        "kind": "metadata",
        "url": "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Baby_Products.jsonl.gz",
        "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\raw\\amazon_reviews_2023\\Baby_Products\\metadata.jsonl.gz",
        "bytes": 174842029,
        "rows": 217724
      }
    ],
    "note": "Amazon Reviews 2023 sample is optional and stored separately from curated seed data."
  },
  "qdrant": {
    "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\.qdrant",
    "local_path_exists": true,
    "embedding_config": {
      "embedding_backend": "sentence-transformers",
      "embedding_model": "BAAI/bge-large-en-v1.5",
      "embedding_device": "cuda",
      "embedding_batch_size": 32
    }
  },
  "sqlite": {
    "exists": true,
    "path": "E:\\code\\agent\\deepsearch\\commerce-rag-ops\\data\\structured\\commerce.db",
    "tables": {
      "amazon_sample_products": 20,
      "amazon_sample_reviews": 20,
      "customer_segments": 4,
      "document_chunks": 42737,
      "golden_eval": 366,
      "kb_articles": 9,
      "orders": 4,
      "products": 6,
      "public_data_files": 6,
      "reviews": 12,
      "scale_products": 3000,
      "scale_rag_documents": 19969,
      "scale_reviews": 15000,
      "support_tickets": 6
    },
    "indexes": [
      "idx_chunks_source_doc",
      "idx_orders_customer_id",
      "idx_orders_sku",
      "idx_products_category",
      "idx_products_sku_lower",
      "idx_public_data_files_category",
      "idx_reviews_product_id",
      "idx_reviews_rating",
      "idx_scale_products_category",
      "idx_scale_rag_documents_product_id",
      "idx_scale_rag_documents_type",
      "idx_scale_reviews_category_rating",
      "idx_scale_reviews_product_id",
      "idx_segments_churn_risk",
      "idx_tickets_product_id"
    ]
  },
  "llm": {
    "endpoint_configured": true,
    "api_key_configured": true,
    "model": "deepseek-v4-flash"
  }
}
```

## SQLite 表

| 表 | 行数 |
|---|---:|
| amazon_sample_products | 20 |
| amazon_sample_reviews | 20 |
| customer_segments | 4 |
| document_chunks | 42737 |
| golden_eval | 366 |
| kb_articles | 9 |
| orders | 4 |
| products | 6 |
| public_data_files | 6 |
| reviews | 12 |
| scale_products | 3000 |
| scale_rag_documents | 19969 |
| scale_reviews | 15000 |
| support_tickets | 6 |
