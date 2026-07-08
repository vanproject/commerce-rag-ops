from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class StructuredFact:
    fact_type: str
    value: Any
    source_tool: str
    citation: str


@dataclass(frozen=True)
class DocEvidence:
    evidence_type: str
    source: str
    doc_id: str
    chunk_id: str
    citation: str
    preview: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EvidenceConflict:
    conflict_type: str
    details: dict[str, Any]
    resolution: str


@dataclass
class EvidencePack:
    structured_facts: list[StructuredFact] = field(default_factory=list)
    policy_evidence: list[DocEvidence] = field(default_factory=list)
    product_evidence: list[DocEvidence] = field(default_factory=list)
    review_evidence: list[DocEvidence] = field(default_factory=list)
    ticket_evidence: list[DocEvidence] = field(default_factory=list)
    unresolved_conflicts: list[EvidenceConflict] = field(default_factory=list)
    missing_requirements: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "structured_facts": [asdict(item) for item in self.structured_facts],
            "policy_evidence": [asdict(item) for item in self.policy_evidence],
            "product_evidence": [asdict(item) for item in self.product_evidence],
            "review_evidence": [asdict(item) for item in self.review_evidence],
            "ticket_evidence": [asdict(item) for item in self.ticket_evidence],
            "unresolved_conflicts": [asdict(item) for item in self.unresolved_conflicts],
            "missing_requirements": self.missing_requirements,
        }
