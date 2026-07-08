# LLM 连通性报告

## 配置

- Endpoint base: `https://opencode.ai/zen/go/v1`
- 归一化 endpoint: `https://opencode.ai/zen/go/v1/chat/completions`
- Model: `deepseek-v4-flash`
- API key: 仅运行时配置，未存入仓库文件

## 在线检查结果

状态：PASS。

证据：

- `python -m commerce_rag_ops.cli llm-check` 返回 `ok: true`
- Answer preview: `OK`
- 使用 `--generator openai-compatible` 的完整 RAG query 已成功
- Trace artifact: `reports/llm_trace.json`

实现说明：

- OpenAI-compatible adapter 会发送 `Authorization: Bearer ...`、`Content-Type: application/json`、`Accept: application/json`、`User-Agent: commerce-rag-ops/0.1`。
- 之前的 403 / error code 1010 已通过补齐 browser-safe request headers 解决。
