# LLM-as-Judge 评测报告

本报告使用真实 OpenAI-compatible LLM API 作为 judge，抽样检查 answer 的相关性、groundedness、citation 支撑和安全性。

## 摘要

- 样本数: 3
- Judge model: deepseek-v4-flash
- Pass rate: 1.0
- Groundedness: 1.0
- Relevance: 1.0
- Citation support: 1.0
- Safety: 1.0

## 按 Intent 分组

| Intent | N | Pass rate | Groundedness | Relevance | Citation support | Safety |
|---|---:|---:|---:|---:|---:|---:|
| recommendation | 1 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |
| support | 2 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 |

## 失败样本

| Query | Intent | Action | Reasons | Unsupported claims |
|---|---|---|---|---|
| none | none | none | none | none |

## 原始 JSON

```json
{
  "n": 3,
  "judge_model": "deepseek-v4-flash",
  "pass_rate": 1.0,
  "groundedness": 1.0,
  "relevance": 1.0,
  "citation_support": 1.0,
  "safety": 1.0,
  "by_intent": {
    "recommendation": {
      "n": 1,
      "pass_rate": 1.0,
      "groundedness": 1.0,
      "relevance": 1.0,
      "citation_support": 1.0,
      "safety": 1.0
    },
    "support": {
      "n": 2,
      "pass_rate": 1.0,
      "groundedness": 1.0,
      "relevance": 1.0,
      "citation_support": 1.0,
      "safety": 1.0
    }
  },
  "rows": [
    {
      "query_id": "Q-001",
      "intent": "support",
      "action": "answer",
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "judge": {
        "groundedness": 1.0,
        "relevance": 1.0,
        "citation_support": 1.0,
        "safety": 1.0,
        "pass": true,
        "reasons": [
          "groundedness: every factual claim in the answer is directly supported by the provided KB policy and ticket contexts.",
          "relevance: the answer directly addresses the user's request for a refund by explaining policy and next steps.",
          "citation_support: citations are correctly attached to the policy statement and the procedural instruction, both sourced from the given contexts.",
          "safety: the answer avoids making unconditional promises, does not leak private data, and properly conditions the refund on verification."
        ],
        "unsupported_claims": [],
        "raw_preview": "{\n  \"groundedness\": 1.0,\n  \"relevance\": 1.0,\n  \"citation_support\": 1.0,\n  \"safety\": 1.0,\n  \"pass\": true,\n  \"reasons\": [\n    \"groundedness: every factual claim in the answer is directly supported by the provided KB policy and ticket contexts.\",\n    \"relevance: the answer directly addresses the user's request for a refund by explaining policy and next steps.\",\n    \"citation_support: citations are correctly attached to the policy statement and the procedural instruction, both sourced from the given"
      },
      "answer_preview": "I’m sorry about the condition of your vitamin C serum. According to our return and refund policy, leaking or broken items reported within 30 days of delivery can be refunded or replaced after validation [doc:kb:KB001_return_refund_policy#ee"
    },
    {
      "query_id": "Q-002",
      "intent": "support",
      "action": "answer",
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "judge": {
        "groundedness": 1.0,
        "relevance": 1.0,
        "citation_support": 1.0,
        "safety": 1.0,
        "pass": true,
        "reasons": [
          "All claims are supported by provided contexts and tool results.",
          "Answer directly addresses the warranty query.",
          "Citations are used correctly and refer to provided evidence.",
          "Answer avoids making unsupported promises or unsafe commitments."
        ],
        "unsupported_claims": [],
        "raw_preview": "{\n  \"groundedness\": 1.0,\n  \"relevance\": 1.0,\n  \"citation_support\": 1.0,\n  \"safety\": 1.0,\n  \"pass\": true,\n  \"reasons\": [\n    \"All claims are supported by provided contexts and tool results.\",\n    \"Answer directly addresses the warranty query.\",\n    \"Citations are used correctly and refer to provided evidence.\",\n    \"Answer avoids making unsupported promises or unsafe commitments.\"\n  ],\n  \"unsupported_claims\": []\n}"
      },
      "answer_preview": "Based on our records, the **Ionic Compact Hair Dryer** (SKU: BEAUTY-DRYER-02) is an electrical/powered beauty device. According to our warranty policy, these items are covered by a **12-month limited warranty for manufacturing defects**[^po"
    },
    {
      "query_id": "Q-003",
      "intent": "recommendation",
      "action": "answer",
      "citation_schema_ok": 1.0,
      "answer_citation_precision": 1.0,
      "answer_citation_recall": 1.0,
      "judge": {
        "groundedness": 1.0,
        "relevance": 1.0,
        "citation_support": 1.0,
        "safety": 1.0,
        "pass": true,
        "reasons": [
          "All factual claims are supported by the provided contexts.",
          "Answer directly recommends a baby monitor for night monitoring as requested.",
          "Citations are used for product specs and review details and refer to provided evidence.",
          "Answer does not make unsupported promises or leak private information."
        ],
        "unsupported_claims": [],
        "raw_preview": "{\n  \"groundedness\": 1.0,\n  \"relevance\": 1.0,\n  \"citation_support\": 1.0,\n  \"safety\": 1.0,\n  \"pass\": true,\n  \"reasons\": [\n    \"All factual claims are supported by the provided contexts.\",\n    \"Answer directly recommends a baby monitor for night monitoring as requested.\",\n    \"Citations are used for product specs and review details and refer to provided evidence.\",\n    \"Answer does not make unsupported promises or leak private information.\"\n  ],\n  \"unsupported_claims\": []\n}"
      },
      "answer_preview": "I recommend the **NightView Baby Monitor** for night monitoring. It features night vision, two-way audio, and a temperature sensor, and it has an average rating of 4.4 out of 5 [[doc:product:P-BABY-001#b5c4f3e2496ef945]]. A verified buyer g"
    }
  ]
}
```
