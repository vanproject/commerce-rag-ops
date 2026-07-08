# Data Notes

This repository ships with small synthetic seed data so the project can run without private company data or large downloads.

The intended production-scale data sources are:

- Amazon Reviews 2023 from UCSD McAuley Lab for public real-world product metadata and review text.
- STaRK E-Commerce / Amazon STaRK for public retrieval benchmark style query-product relevance labels.
- Synthetic support KB, tickets, and SKU tables modeled after ecommerce support systems.

The seed support tickets are not private enterprise records. They are structured examples that mirror realistic ecommerce support fields and can be regenerated from low-rating public product reviews.

Optional importer:

```powershell
python -m commerce_rag_ops.cli import-amazon-sample --categories All_Beauty --review-limit 50 --product-limit 50
```

This requires `pip install -e .[data]` and writes separate `*.amazon_sample.jsonl` files for inspection.
