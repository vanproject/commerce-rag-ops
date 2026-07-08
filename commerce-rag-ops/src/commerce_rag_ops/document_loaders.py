from __future__ import annotations

import csv
import json
import re
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from .text import normalize_text


TEXT_SUFFIXES = {".md", ".txt"}
HTML_SUFFIXES = {".html", ".htm"}
TABLE_SUFFIXES = {".csv", ".tsv"}
JSON_SUFFIXES = {".json", ".jsonl"}
PDF_SUFFIXES = {".pdf"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp"}
SIDECAR_SUFFIXES = {".ocr.txt", ".pdf.txt"}


@dataclass(frozen=True)
class KnowledgeDocument:
    doc_id: str
    title: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class DocumentLoadReport:
    documents: list[KnowledgeDocument]
    skipped: list[dict[str, Any]]


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self._skip_depth += 1
        if tag in {"p", "br", "li", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self._skip_depth > 0:
            self._skip_depth -= 1
        if tag in {"p", "li", "tr", "h1", "h2", "h3"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if self._skip_depth == 0:
            self.parts.append(data)

    def text(self) -> str:
        return normalize_text(" ".join(self.parts))


def load_knowledge_documents(data_dir: Path) -> list[KnowledgeDocument]:
    return load_knowledge_documents_with_report(data_dir).documents


def load_knowledge_documents_with_report(data_dir: Path) -> DocumentLoadReport:
    docs: list[KnowledgeDocument] = []
    skipped: list[dict[str, Any]] = []

    kb_dir = data_dir / "raw" / "kb_articles"
    for path in sorted(kb_dir.glob("*.md")):
        docs.append(_load_text_document(path, document_type="policy_markdown", source_dir="kb_articles"))

    assets_dir = data_dir / "raw" / "knowledge_assets"
    if assets_dir.exists():
        for path in sorted(p for p in assets_dir.rglob("*") if p.is_file()):
            if _is_sidecar(path):
                continue
            try:
                extracted = extract_knowledge_document(path)
            except Exception as exc:
                skipped.append({"path": str(path), "reason": "extract_error", "error": str(exc)})
                continue
            if extracted is None:
                skipped.append({"path": str(path), "reason": "unsupported_suffix", "suffix": path.suffix.lower()})
                continue
            if not extracted.text.strip():
                skipped.append({"path": str(path), "reason": "empty_text"})
                continue
            docs.append(extracted)

    return DocumentLoadReport(documents=docs, skipped=skipped)


def extract_knowledge_document(path: Path) -> KnowledgeDocument | None:
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return _load_text_document(path, document_type="text_notice", source_dir=path.parent.name)
    if suffix in HTML_SUFFIXES:
        return _load_html_document(path)
    if suffix in TABLE_SUFFIXES:
        return _load_table_document(path)
    if suffix in JSON_SUFFIXES:
        return _load_json_document(path)
    if suffix in PDF_SUFFIXES:
        return _load_pdf_document(path)
    if suffix in IMAGE_SUFFIXES:
        return _load_image_ocr_document(path)
    return None


def _load_text_document(path: Path, *, document_type: str, source_dir: str) -> KnowledgeDocument:
    text = path.read_text(encoding="utf-8")
    return KnowledgeDocument(
        doc_id=path.stem,
        title=_title_from_text(text, fallback=path.stem),
        text=text,
        metadata={
            "document_type": document_type,
            "filename": path.name,
            "source_dir": source_dir,
            "extraction_method": "plain_text",
        },
    )


def _load_html_document(path: Path) -> KnowledgeDocument:
    parser = _HTMLTextExtractor()
    parser.feed(path.read_text(encoding="utf-8"))
    text = parser.text()
    return KnowledgeDocument(
        doc_id=path.stem,
        title=_title_from_text(text, fallback=path.stem),
        text=text,
        metadata={
            "document_type": "html_policy_page",
            "filename": path.name,
            "source_dir": path.parent.name,
            "extraction_method": "html_text_parser",
        },
    )


def _load_table_document(path: Path) -> KnowledgeDocument:
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter=delimiter))
    fields = rows[0].keys() if rows else []
    lines = [f"Table document {path.stem}. Columns: {', '.join(fields)}."]
    for index, row in enumerate(rows[:100], start=1):
        row_text = "; ".join(f"{key}: {value}" for key, value in row.items())
        lines.append(f"Row {index}. {row_text}.")
    return KnowledgeDocument(
        doc_id=path.stem,
        title=path.stem.replace("_", " ").title(),
        text=" ".join(lines),
        metadata={
            "document_type": "structured_table",
            "filename": path.name,
            "source_dir": path.parent.name,
            "extraction_method": "csv_dict_reader",
            "row_count": len(rows),
        },
    )


def _load_json_document(path: Path) -> KnowledgeDocument:
    rows: list[dict[str, Any]]
    if path.suffix.lower() == ".jsonl":
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    else:
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload if isinstance(payload, list) else [payload]
    lines = [f"JSON document {path.stem}."]
    for index, row in enumerate(rows[:100], start=1):
        lines.append(f"Record {index}. {_flatten_mapping(row)}.")
    return KnowledgeDocument(
        doc_id=path.stem,
        title=path.stem.replace("_", " ").title(),
        text=" ".join(lines),
        metadata={
            "document_type": "json_knowledge",
            "filename": path.name,
            "source_dir": path.parent.name,
            "extraction_method": "json_loader",
            "row_count": len(rows),
        },
    )


def _load_pdf_document(path: Path) -> KnowledgeDocument:
    sidecar = _sidecar_text(path, ".pdf.txt")
    if sidecar:
        text = sidecar.read_text(encoding="utf-8")
        method = "sidecar_pdf_text"
    else:
        try:
            from pypdf import PdfReader  # type: ignore
        except Exception as exc:
            raise RuntimeError("PDF extraction requires pypdf or a .pdf.txt sidecar") from exc
        reader = PdfReader(str(path))
        text = "\n".join((page.extract_text() or "") for page in reader.pages)
        method = "pypdf"
    return KnowledgeDocument(
        doc_id=path.stem,
        title=_title_from_text(text, fallback=path.stem),
        text=text,
        metadata={
            "document_type": "pdf_document",
            "filename": path.name,
            "source_dir": path.parent.name,
            "extraction_method": method,
        },
    )


def _load_image_ocr_document(path: Path) -> KnowledgeDocument:
    sidecar = _sidecar_text(path, ".ocr.txt")
    if sidecar:
        text = sidecar.read_text(encoding="utf-8")
        method = "sidecar_ocr_text"
        confidence = "curated_fixture"
    else:
        try:
            import pytesseract  # type: ignore
            from PIL import Image  # type: ignore
        except Exception as exc:
            raise RuntimeError("OCR extraction requires pytesseract+Pillow or a .ocr.txt sidecar") from exc
        text = pytesseract.image_to_string(Image.open(path))
        method = "pytesseract"
        confidence = "runtime_ocr_unscored"
    return KnowledgeDocument(
        doc_id=path.stem,
        title=_title_from_text(text, fallback=path.stem),
        text=text,
        metadata={
            "document_type": "ocr_image",
            "filename": path.name,
            "source_dir": path.parent.name,
            "extraction_method": method,
            "ocr_confidence": confidence,
        },
    )


def _sidecar_text(path: Path, suffix: str) -> Path | None:
    candidates = [Path(str(path) + suffix), path.with_suffix(suffix)]
    return next((candidate for candidate in candidates if candidate.exists()), None)


def _is_sidecar(path: Path) -> bool:
    lowered = path.name.lower()
    return any(lowered.endswith(suffix) for suffix in SIDECAR_SUFFIXES)


def _title_from_text(text: str, *, fallback: str) -> str:
    for line in text.splitlines():
        clean = line.strip().lstrip("#").strip()
        if clean:
            return clean[:120]
    clean_text = normalize_text(text)
    return clean_text[:120] if clean_text else fallback


def _flatten_mapping(row: dict[str, Any]) -> str:
    parts = []
    for key, value in row.items():
        if isinstance(value, (dict, list)):
            value = json.dumps(value, ensure_ascii=False)
        parts.append(f"{key}: {value}")
    return re.sub(r"\s+", " ", "; ".join(parts))
