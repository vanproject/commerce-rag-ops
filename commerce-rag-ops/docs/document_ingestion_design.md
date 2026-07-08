# 文档摄取设计

本文档说明 CommerceRAG Ops 如何处理多格式知识文档，并把它们转成可检索的 RAG chunks。

## 目标

电商客服知识库通常不是单一 Markdown 文件，而是混合存在：

- 政策 Markdown
- 帮助中心 HTML
- 运营 CSV 表
- 承运商 TXT 通知
- PDF/扫描件
- 客诉图片或索赔表单

项目使用标准库优先的 loader 设计，默认可离线运行；可选依赖用于 PDF/OCR 增强。

## 当前支持格式

| 格式 | 路径示例 | 抽取方式 | source |
|---|---|---|---|
| Markdown | `data/raw/kb_articles/*.md` | plain text | `kb` |
| HTML | `data/raw/knowledge_assets/KB006_return_status_matrix.html` | 标准库 HTML parser，忽略 script/style | `kb` |
| CSV | `data/raw/knowledge_assets/refund_reason_codes.csv` | `csv.DictReader` 转紧凑文本 | `kb` |
| TXT | `data/raw/knowledge_assets/carrier_exception_notice.txt` | plain text | `kb` |
| PNG/JPG OCR | `data/raw/knowledge_assets/scanned_damage_claim.png` | sidecar `.ocr.txt`，可选 pytesseract | `kb` |
| PDF | 可选 | `pypdf` | `kb` |
| Unsupported | fixture | 记录 skipped，不中断流程 | none |

## 元数据

每个知识文档保留：

- `document_type`
- `filename`
- `source_dir`
- `extraction_method`
- `title`
- `policy_type`
- `chunk_index`
- `total_chunks`

OCR 文档还会保留：

- `sidecar_ocr_text`
- 原始图片文件名
- 订单/SKU 文本证据

## 切片策略

不同类型使用不同 chunk size/overlap：

| 类型 | Chunk size | Overlap | 设计理由 |
|---|---:|---:|---|
| 普通 KB | 520 | 60 | 政策句子不被切断 |
| 表格 KB | 420 | 50 | 表格行信息密度高 |
| OCR 图片 | 360 | 45 | OCR 噪声更高，短 chunk 更稳 |
| Ticket | 280 | 35 | 客户问题和处理结果保持紧凑 |
| Product | 480 | 40 | 商品特征尽量在同一 chunk |
| Review | 360 | 30 | 保留单条客户声音 |

## 边界处理

- 空抽取结果进入 audit，不进入索引。
- 不支持后缀进入 skipped 列表。
- OCR 默认读取 sidecar，保证测试 deterministic。
- 可选 OCR/PDF 依赖缺失时不影响主流程。
- 文档标题从首行或文件名推断。

## 验证

相关测试：

```powershell
python -m pytest tests\test_core.py::test_multiformat_knowledge_documents_and_ocr_fixture_load -q -p no:cacheprovider
```

验证点：

- HTML、CSV、TXT、OCR image 都能加载。
- OCR sidecar 中包含 `ORD-1001`。
- unsupported fixture 会被记录为 skipped。

## 面试讲法

可以这样说明：

> 我没有把知识库简化成纯 Markdown，而是做了文档类型感知的 ingestion。不同格式有不同抽取方式和切片参数，OCR/表格/HTML 都会保留来源元数据，方便后续 citation、debug 和合规审计。
