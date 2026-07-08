from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .agent import CommerceRAGAgent
from .models import DocumentChunk, SearchResult
from .retrieval import RetrievalMode


@dataclass(frozen=True)
class FallbackStressCase:
    case_id: str
    query: str
    expected_gap: str
    expected_intent: str
    first_results: list[SearchResult]
    second_results: list[SearchResult]
    expected_action: str = "answer"
    expect_gap_cleared: bool = True
    expect_citations: bool = True


class ScriptedFallbackRetriever:
    def __init__(self, cases: list[FallbackStressCase]):
        self.cases = {case.query: case for case in cases}
        self.calls_by_query: dict[str, int] = {}

    def search(
        self,
        query: str,
        *,
        sources: Iterable[str] | None = None,
        top_k: int = 5,
        candidate_k: int = 30,
        mode: RetrievalMode = "hybrid_rerank",
    ) -> list[SearchResult]:
        original_query = self._original_query(query)
        case = self.cases[original_query]
        calls = self.calls_by_query.get(original_query, 0) + 1
        self.calls_by_query[original_query] = calls
        return case.first_results if calls == 1 else case.second_results

    def _original_query(self, query: str) -> str:
        for original in self.cases:
            if query.startswith(original):
                return original
        raise KeyError(f"No scripted fallback case for query: {query}")


def run_fallback_stress(data_dir: Path) -> dict:
    cases = _stress_cases()
    retriever = ScriptedFallbackRetriever(cases)
    agent = CommerceRAGAgent(retriever, data_dir)
    rows = []
    for case in cases:
        state = agent.run(case.query, max_retries=1)
        grade_events = [event for event in state.trace if event.get("event") == "grade"]
        first_gaps = grade_events[0].get("evidence_gaps", []) if grade_events else []
        final_gaps = grade_events[-1].get("evidence_gaps", []) if grade_events else []
        gap_state_ok = case.expected_gap not in final_gaps if case.expect_gap_cleared else case.expected_gap in final_gaps
        citation_state_ok = bool(state.citations) if case.expect_citations else not state.citations
        passed = (
            state.intent == case.expected_intent
            and state.attempts == 2
            and case.expected_gap in first_gaps
            and gap_state_ok
            and state.action == case.expected_action
            and citation_state_ok
        )
        rows.append(
            {
                "case_id": case.case_id,
                "query": case.query,
                "expected_intent": case.expected_intent,
                "actual_intent": state.intent,
                "expected_gap": case.expected_gap,
                "expected_action": case.expected_action,
                "first_gaps": first_gaps,
                "final_gaps": final_gaps,
                "attempts": state.attempts,
                "action": state.action,
                "citations": len(state.citations),
                "passed": passed,
            }
        )
    return {
        "n": len(rows),
        "passed": all(row["passed"] for row in rows),
        "retry_cases": sum(1 for row in rows if row["attempts"] > 1),
        "answered_cases": sum(1 for row in rows if row["action"] == "answer"),
        "refused_cases": sum(1 for row in rows if row["action"] == "refuse"),
        "rows": rows,
    }


def write_fallback_stress_report(report_path: Path, report: dict) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Fallback 压力测试报告",
        "",
        "本报告通过脚本化检索失败来验证关键 Agentic fallback 行为。",
        "该流程不会修改或重新打分 `data/eval/golden.jsonl`。",
        "",
        f"- 用例数: {report['n']}",
        f"- 是否通过: {report['passed']}",
        f"- 触发重试用例数: {report['retry_cases']}",
        f"- 最终回答用例数: {report['answered_cases']}",
        f"- 最终拒答用例数: {report['refused_cases']}",
        "",
        "| 用例 | 意图 | 预期缺口 | 首轮缺口 | 最终缺口 | 尝试次数 | 预期动作 | 实际动作 | 引用数 | 状态 |",
        "|---|---|---|---|---|---:|---|---|---:|---|",
    ]
    for row in report["rows"]:
        status = "PASS" if row["passed"] else "FAIL"
        lines.append(
            "| {case_id} | {actual_intent} | {expected_gap} | {first_gaps} | {final_gaps} | {attempts} | {expected_action} | {action} | {citations} | {status} |".format(
                case_id=row["case_id"],
                actual_intent=row["actual_intent"],
                expected_gap=row["expected_gap"],
                first_gaps=", ".join(row["first_gaps"]) or "none",
                final_gaps=", ".join(row["final_gaps"]) or "none",
                attempts=row["attempts"],
                expected_action=row["expected_action"],
                action=row["action"],
                citations=row["citations"],
                status=status,
            )
        )
    lines.extend(["", "## 原始用例", ""])
    for row in report["rows"]:
        lines.extend(
            [
                f"### {row['case_id']}",
                "",
                f"- Query: {row['query']}",
                f"- 预期关键缺口: `{row['expected_gap']}`",
                f"- 预期动作: `{row['expected_action']}`",
                f"- 首轮缺口: `{', '.join(row['first_gaps']) or 'none'}`",
                f"- 最终缺口: `{', '.join(row['final_gaps']) or 'none'}`",
                "",
            ]
        )
    report_path.write_text("\n".join(lines), encoding="utf-8")


def _stress_cases() -> list[FallbackStressCase]:
    product = _result(
        "product",
        "P-BABY-001",
        "p1",
        "NightView Baby Monitor product profile with clear night vision and in-stock inventory.",
        {"doc_type": "product_profile", "product_id": "P-BABY-001", "title": "NightView Baby Monitor"},
        0.55,
    )
    review = _result(
        "review",
        "R-010",
        "r1",
        "Verified review says the baby monitor has clear night vision and reliable alerts.",
        {"doc_type": "review_evidence", "product_id": "P-BABY-001", "rating": 5},
        0.48,
    )
    ticket = _result(
        "ticket",
        "T-001",
        "t1",
        "Customer query: serum arrived leaking. Resolution: collect photos and route to return policy.",
        {"doc_type": "faq_case", "product_id": "P-BEAUTY-001", "aspect": "refund_return"},
        0.52,
    )
    policy = _result(
        "kb",
        "KB001_return_refund_policy",
        "k1",
        "Damaged items reported within 30 days can be refunded or replaced after validation.",
        {"document_type": "policy_markdown", "policy_type": "return_refund_policy"},
        0.5,
    )
    ops_product = _result(
        "product",
        "P-BABY-002",
        "p2",
        "Anti-Colic Glass Bottle Set product profile.",
        {"doc_type": "product_profile", "product_id": "P-BABY-002"},
        0.5,
    )
    ops_review = _result(
        "review",
        "R-009",
        "r2",
        "Low-rating review: bottle nipple leaked and replacement parts were confusing.",
        {"doc_type": "review_evidence", "product_id": "P-BABY-002", "rating": 2, "aspect": "missing_parts"},
        0.46,
    )
    sku_policy = _result(
        "kb",
        "KB004_shipping_delivery_policy",
        "k2",
        "Shipping and delivery policy for checking carrier status.",
        {"document_type": "policy_markdown", "policy_type": "shipping_delivery_policy"},
        0.5,
    )
    sku_product = _result(
        "product",
        "P-SOFT-001",
        "p3",
        "PDF Studio Pro License product profile. SKU SOFT-PDF-01. Current inventory is available.",
        {"doc_type": "product_profile", "product_id": "P-SOFT-001", "sku": "SOFT-PDF-01"},
        0.53,
    )
    return [
        FallbackStressCase(
            case_id="FS-001",
            query="Recommend a baby monitor with good night vision reviews",
            expected_gap="missing_review",
            expected_intent="recommendation",
            first_results=[product],
            second_results=[product, review],
        ),
        FallbackStressCase(
            case_id="FS-002",
            query="My serum arrived broken. Can I get a refund?",
            expected_gap="missing_policy",
            expected_intent="support",
            first_results=[ticket],
            second_results=[ticket, policy],
        ),
        FallbackStressCase(
            case_id="FS-003",
            query="What customer ops issues appear in baby product complaints?",
            expected_gap="missing_customer_voice",
            expected_intent="customer_ops",
            first_results=[ops_product],
            second_results=[ops_product, ops_review],
        ),
        FallbackStressCase(
            case_id="FS-004",
            query="Check inventory status for the matched item.",
            expected_gap="missing_product_context",
            expected_intent="sku_order",
            first_results=[sku_policy],
            second_results=[sku_product, sku_policy],
        ),
        FallbackStressCase(
            case_id="FS-005",
            query="Check SKU TEMP-404 inventory status.",
            expected_gap="missing_structured_entity",
            expected_intent="sku_order",
            first_results=[sku_policy],
            second_results=[sku_product, sku_policy],
            expected_action="refuse",
            expect_gap_cleared=False,
            expect_citations=False,
        ),
        FallbackStressCase(
            case_id="FS-006",
            query="Check order ORD-404 status.",
            expected_gap="missing_structured_entity",
            expected_intent="sku_order",
            first_results=[sku_policy],
            second_results=[sku_product, sku_policy],
            expected_action="refuse",
            expect_gap_cleared=False,
            expect_citations=False,
        ),
        FallbackStressCase(
            case_id="FS-007",
            query="Can I get a refund for an unknown discontinued item with no order details?",
            expected_gap="no_context",
            expected_intent="support",
            first_results=[],
            second_results=[],
            expected_action="refuse",
            expect_gap_cleared=False,
            expect_citations=False,
        ),
    ]


def _result(
    source: str,
    doc_id: str,
    chunk_id: str,
    text: str,
    metadata: dict,
    rerank_score: float,
) -> SearchResult:
    return SearchResult(
        chunk=DocumentChunk(chunk_id=chunk_id, source=source, doc_id=doc_id, text=text, metadata=metadata),
        score=rerank_score,
        rerank_score=rerank_score,
    )
