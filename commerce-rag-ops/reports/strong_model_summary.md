# 强模型链路验证报告

本报告记录从离线 baseline 切换到更具代表性的生产/面试档链路后的验证结果。真实 API key 只保存在本地 `.env`，未写入仓库。

## 当前强模型配置

| 组件 | 当前配置 |
|---|---|
| Vector DB | 本地 embedded Qdrant，collection `commerce_rag_chunks` |
| Embedding backend | `sentence-transformers` |
| Embedding model | `BAAI/bge-large-en-v1.5` |
| Embedding dimension | 1024 |
| Indexed points | 42,737 |
| Reranker | `BAAI/bge-reranker-large` |
| LLM endpoint | OpenAI-compatible，`https://opencode.ai/zen/go/v1` |
| LLM model | `deepseek-v4-flash` |

模型下载说明：

- 直接访问 Hugging Face 时出现 SSL EOF。
- 已通过 `.env` / `.env.example` 配置 `HF_ENDPOINT=https://hf-mirror.com`。
- `BAAI/bge-large-en-v1.5` 与 `BAAI/bge-reranker-large` 均已成功加载。

## Qdrant 索引

重建命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli qdrant-index `
  --qdrant-path .qdrant `
  --collection commerce_rag_chunks `
  --embedding-backend sentence-transformers `
  --embedding-model BAAI/bge-large-en-v1.5 `
  --embedding-device cuda `
  --embedding-batch-size 32
```

输出摘要：

```json
{
  "collection": "commerce_rag_chunks",
  "points": 42737,
  "embedding_backend": "sentence-transformers",
  "embedding_model": "BAAI/bge-large-en-v1.5",
  "embedding_dimensions": 1024
}
```

## 强检索评测

### 30 条 smoke 评测

评测命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli eval --backend qdrant --limit 30 --generator template
```

结果摘要：

| 指标 | 值 |
|---|---:|
| Precision@5 | 0.9333 |
| Recall@5 | 0.8778 |
| MRR | 0.9333 |
| NDCG@5 | 0.9333 |
| Citation rate | 1.0 |
| Keyword coverage | 0.9556 |
| Groundedness proxy | 0.9618 |
| p95 latency | 882 ms |

完整报告：`reports/strong_model_eval_report.md`

### 366 条全量评测：Qdrant + BGE + template

评测命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli eval --backend qdrant --generator template
```

结果摘要：

| 指标 | 值 |
|---|---:|
| Precision@5 | 0.9536 |
| Recall@5 | 0.8686 |
| MRR | 0.9945 |
| NDCG@5 | 0.9470 |
| Citation rate | 0.9918 |
| Keyword coverage | 0.8871 |
| Groundedness proxy | 0.9803 |
| p50 latency | 577 ms |
| p95 latency | 797 ms |

按 intent 分组：

| Intent | N | Precision@5 | Recall@5 | NDCG@5 |
|---|---:|---:|---:|---:|
| customer_ops | 187 | 0.9904 | 0.9109 | 0.9927 |
| recommendation | 91 | 1.0 | 0.9560 | 1.0 |
| sku_order | 1 | 0.0 | 0.0 | 0.0 |
| support | 87 | 0.8372 | 0.6961 | 0.8041 |

完整报告：`reports/strong_model_full_eval_report.md`

### 366 条真实 LLM 全量评测：Qdrant + BGE + deepseek-v4-flash

评测命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli eval --backend qdrant --generator openai-compatible
```

运行耗时约 7313 秒，使用 `.env` 中的 OpenAI-compatible endpoint 与 API key。该结果是真实 LLM 生成链路的全量评测，不再使用 template generator。

结果摘要：

| 指标 | 值 |
|---|---:|
| Precision@5 | 0.9536 |
| Recall@5 | 0.8686 |
| MRR | 0.9945 |
| NDCG@5 | 0.9470 |
| Citation rate | 0.8743 |
| Keyword coverage | 0.8051 |
| Groundedness proxy | 0.9793 |
| p50 latency | 14,528 ms |
| p95 latency | 41,106 ms |

按 intent 分组：

| Intent | N | Precision@5 | Recall@5 | NDCG@5 | Citation | Keyword |
|---|---:|---:|---:|---:|---:|---:|
| customer_ops | 187 | 0.9904 | 0.9109 | 0.9927 | 1.0000 | 0.9234 |
| recommendation | 91 | 1.0000 | 0.9560 | 1.0000 | 0.7253 | 0.7253 |
| sku_order | 1 | 0.0 | 0.0 | 0.0 | 1.0000 | 1.0000 |
| support | 87 | 0.8372 | 0.6961 | 0.8041 | 0.7586 | 0.6322 |

完整报告：`reports/strong_model_full_llm_eval_report.md`

说明：

- template 全量评测用于快速回归强检索链路；真实 LLM 全量评测用于呈现端到端生成质量和真实延迟。
- 旧 baseline 的 0.99+ 指标来自本地业务规则增强检索，更适合证明工程逻辑；强模型结果更能代表真实向量检索和 rerank 链路。
- 全量结果显示 recommendation 和 customer_ops 表现稳定，support 是主要短板：BGE dense/rerank 能找到 FAQ case，但 policy recall 不如旧规则 fallback，需要增加 policy-aware retrieval 或 filter-first policy expansion。
- 真实 LLM 相比 template 的 citation rate 从 0.9918 降到 0.8743，keyword coverage 从 0.8871 降到 0.8051，p95 latency 从 797 ms 升到 41.1s。这不是坏事，说明评测没有用模板美化结果，也暴露了 citation schema、输出校验和 policy retrieval 的下一轮优化空间。
- 早期 6 条 seed query 已补齐 `intent`、`expected_action`、`safety_category` 元数据，主评测不再把缺失标注统计成 `unknown`。真实 unknown/refusal 覆盖见下一节和合并评测。
- 新版 eval 已加入 citation schema validator。后续重新跑全量 eval 时，报告会额外输出 `citation_schema_ok`、`answer_citation_precision`、`answer_citation_recall` 和 `citation_grounded_rate`，不再只依赖 keyword coverage 或 state 里是否存在 citations。

## Unknown / Refusal 评测

拒答评测命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli refusal-eval --backend qdrant --generator template --min-pass-rate 0.99
```

数据集：`data/eval/refusal.jsonl`，48 条。

覆盖类型：

- out-of-domain
- prompt injection
- unknown SKU
- unknown order
- insufficient context
- privacy
- policy boundary
- ambiguous product
- conflicting entity
- unsafe commitment
- irrelevant chitchat

Qdrant+BGE 链路结果：

| 指标 | 值 |
|---|---:|
| 样本数 | 48 |
| Pass rate | 1.0 |
| Refusal rate | 1.0 |
| Citation leak rate | 0.0 |

完整报告：`reports/refusal_eval_report.md`

## 合并评测：Normal + Boundary

增量真实 LLM 命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli combined-eval `
  --backend qdrant `
  --generator openai-compatible `
  --normal-report reports/strong_model_full_llm_eval_report.md
```

该命令复用 366 条真实 LLM 全量报告，只增量调用真实 LLM 跑 48 条边界/拒答用例。

| 指标 | 值 |
|---|---:|
| 正常业务问答 | 366 |
| 边界/拒答问答 | 48 |
| 合并总量 | 414 |
| 合并 pass rate | 0.8889 |
| 正常 answer pass rate | 0.8743 |
| 边界 refuse pass rate | 1.0 |
| 边界 citation leak rate | 0.0 |

合并报告：`reports/combined_eval_report.md`

## Citation Schema 检查

新增 deterministic citation contract：

- citation 必须符合 `[doc:<source>:<doc_id>#<chunk_id>]`。
- state citations 必须能映射到本轮 retrieved contexts。
- answer 文本里的 citation marker 必须来自 state citations。
- `must_cite=true` 的 answer 必须在正文中实际出现至少一个合法 citation marker。

新增指标：

| 指标 | 含义 |
|---|---|
| `citation_schema_ok` | citation 语法、来源和 answer 使用均通过 |
| `answer_citation_precision` | answer 中 citation 有多少属于本轮合法 citations |
| `answer_citation_recall` | state citations 有多少实际出现在 answer 中 |
| `citation_grounded_rate` | state citations 有多少能映射回 retrieved chunk |

Smoke 报告：`reports/citation_schema_smoke_report.md`，25 条 local/template 样本，`citation_schema_ok=0.8`。低于 1 的原因主要是弱证据/拒答案例不应强行输出 citation，这能暴露旧 `citation_ok` 看不到的 answer-side citation 问题。

## LLM-as-Judge

新增命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli judge-eval --backend qdrant --generator openai-compatible --limit 3
```

该命令使用真实 OpenAI-compatible LLM API 作为 judge，评估：

- groundedness
- relevance
- citation support
- safety

当前真实 API smoke：

| 指标 | 值 |
|---|---:|
| 样本数 | 3 |
| Judge model | `deepseek-v4-flash` |
| Pass rate | 1.0 |
| Groundedness | 1.0 |
| Relevance | 1.0 |
| Citation support | 1.0 |
| Safety | 1.0 |

完整报告：`reports/llm_judge_report.md`。

## 能力矩阵

完整对照见：`docs/capability_matrix.md`。

| 能力 | 状态 |
|---|---|
| Hybrid retrieval action | 已实现 |
| Query expansion / HyDE | 部分实现：query expansion + gap-aware retry expansion，不是完整 HyDE |
| Self-reflection | 已实现：deterministic grader + evidence contract + LLM-as-judge |
| Refusal control | 已实现 |
| Citation control | 已实现 |
| Trace and observability | 已实现 |

## 真实 LLM 生成链路

检查命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli llm-check
```

结果：`ok: true`，模型 `deepseek-v4-flash` 返回 `OK`。

真实生成命令：

```powershell
$env:PYTHONPATH="src"
python -m commerce_rag_ops.cli qdrant-ask `
  "My serum arrived leaking. Can I get a refund?" `
  --qdrant-path .qdrant `
  --collection commerce_rag_chunks `
  --generator openai-compatible
```

结果摘要：

- Intent: `support`
- Action: `answer`
- Citations: 2
- Top rerank score: `1.0988`
- Evidence gap count: `0.0`
- Finish latency: about `12.3s`
- Trace artifact: `reports/strong_model_llm_trace.json`

## 后续代表性增强

- 扩大 LLM-as-judge 样本规模，增加按 intent/safety category 的 judge 稳定性报告。
- 对比 `BAAI/bge-large-en-v1.5`、`intfloat/e5-large-v2`、`BAAI/bge-m3` 等 embedding。
- 对比 `BAAI/bge-reranker-large` 与更强 reranker，记录 latency/accuracy tradeoff。
- 针对 support query 增加 policy-first candidate expansion，并做消融验证。
