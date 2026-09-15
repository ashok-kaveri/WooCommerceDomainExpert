"""
Generate a QA test-result document (.docx) from a Trello card.

This mirrors the document QA hands over after a release run: a PluginHive
cover page, document-history and testing-details tables, the replicated
problem, and then one section per Trello checklist group with the individual
checklist items as test cases.

Steps, expected results and screenshot slots come from an optional JSON
sidecar so the wording can be edited without touching this file. When no
sidecar is given, each case still gets an empty Steps / Expected / Screenshot
scaffold for the tester to fill in.

Usage:
    python3 scripts/generate_test_document.py SI23TDil \
        --steps data/test_documents/SI23TDil_steps.json \
        --plugin "WooCommerce UPS Shipping Plugin with Print Label" \
        --version 6.6.4

Output: data/test_documents/<Plugin Name> - V<version>.docx
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(REPO_ROOT / ".env")

from pipeline.trello_client import TrelloClient  # noqa: E402

# Palette sampled from the QA team's existing test documents.
HEADING_BLUE = RGBColor(0x07, 0x37, 0x63)
TABLE_HEADER_BG = "6D9EEB"
TABLE_VALUE_BG = "EFEFEF"
RULE_BLUE = "3D85C6"
PLACEHOLDER_GREY = RGBColor(0x88, 0x88, 0x88)

OUTPUT_DIR = REPO_ROOT / "data" / "test_documents"
ASSETS_DIR = REPO_ROOT / "data" / "test_documents" / "assets"
SHOTS_DIR = REPO_ROOT / "data" / "test_documents" / "screenshots"


# ---------------------------------------------------------------------------
# Low-level docx helpers
# ---------------------------------------------------------------------------

def _shade(cell, hex_fill: str) -> None:
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hex_fill)
    cell._tc.get_or_add_tcPr().append(shd)


def _paragraph_rule(paragraph, edge: str, hex_color: str, size: int = 12) -> None:
    """Draw a horizontal rule above or below a paragraph."""
    p_bdr = OxmlElement("w:pBdr")
    border = OxmlElement(f"w:{edge}")
    border.set(qn("w:val"), "single")
    border.set(qn("w:sz"), str(size))
    border.set(qn("w:space"), "1")
    border.set(qn("w:color"), hex_color)
    p_bdr.append(border)
    paragraph._p.get_or_add_pPr().append(p_bdr)


def _page_number_field(paragraph) -> None:
    """Insert a PAGE field. fldSimple is understood by Word, Pages and Docs."""
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    run = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = "1"
    run.append(text)
    fld.append(run)
    paragraph._p.append(fld)


def _restart_page_numbers(section) -> None:
    pg_num = OxmlElement("w:pgNumType")
    pg_num.set(qn("w:start"), "1")
    section._sectPr.append(pg_num)


def _fixed_columns(table, widths: list[float]) -> None:
    """Pin column widths. Word only honours these with a fixed table layout."""
    table.autofit = False
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    table._tbl.tblPr.append(layout)

    # The tblGrid is authoritative for renderers; cell widths alone are ignored.
    grid = table._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        for col, width in zip(grid.findall(qn("w:gridCol")), widths):
            col.set(qn("w:w"), str(int(width * 1440)))

    for row in table.rows:
        for cell, width in zip(row.cells, widths):
            cell.width = Inches(width)


def _row_height(row, inches: float) -> None:
    tr_pr = row._tr.get_or_add_trPr()
    tr_height = OxmlElement("w:trHeight")
    tr_height.set(qn("w:val"), str(int(inches * 1440)))
    tr_height.set(qn("w:hRule"), "atLeast")
    tr_pr.append(tr_height)


# ---------------------------------------------------------------------------
# Building blocks
# ---------------------------------------------------------------------------

def _heading(doc, text: str, size: int = 14, color=HEADING_BLUE, space_before: int = 14):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(space_before)
    para.paragraph_format.space_after = Pt(6)
    run = para.add_run(text)
    run.bold = True
    run.font.size = Pt(size)
    run.font.color.rgb = color
    return para


def _body(doc, text: str, bold: bool = False, size: int = 11, italic: bool = False):
    para = doc.add_paragraph()
    para.paragraph_format.space_after = Pt(6)
    run = para.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    return para


def _evidence(doc, entry, height_in: float = 2.4) -> None:
    """Render one piece of evidence: a captured screenshot, or an empty slot."""
    if isinstance(entry, dict):
        caption, filename = entry.get("caption", ""), entry.get("file")
    else:
        caption, filename = entry, None

    image = (SHOTS_DIR / filename) if filename else None
    if image and image.exists():
        para = doc.add_paragraph()
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.space_after = Pt(2)
        para.add_run().add_picture(str(image), width=Inches(6.3))
        cap = doc.add_paragraph()
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cap.paragraph_format.space_after = Pt(12)
        run = cap.add_run(caption)
        run.italic = True
        run.font.size = Pt(9)
        run.font.color.rgb = PLACEHOLDER_GREY
        return

    _screenshot_slot(doc, caption, height_in)


def _screenshot_slot(doc, caption: str, height_in: float = 2.4) -> None:
    """An empty bordered box for the tester to paste evidence into."""
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    _fixed_columns(table, [6.5])
    cell = table.cell(0, 0)
    _row_height(table.rows[0], height_in)
    para = cell.paragraphs[0]
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(f"[ Screenshot: {caption} ]")
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = PLACEHOLDER_GREY
    doc.add_paragraph()


def _kv_table(doc, rows: list[tuple[str, str]], label_width: float = 1.6) -> None:
    table = doc.add_table(rows=len(rows), cols=2)
    table.style = "Table Grid"
    _fixed_columns(table, [label_width, 6.5 - label_width])
    for idx, (label, value) in enumerate(rows):
        label_cell, value_cell = table.rows[idx].cells
        _shade(label_cell, TABLE_HEADER_BG)
        _shade(value_cell, TABLE_VALUE_BG)
        run = label_cell.paragraphs[0].add_run(label)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        for line_no, line in enumerate(value.split("\n")):
            para = value_cell.paragraphs[0] if line_no == 0 else value_cell.add_paragraph()
            vrun = para.add_run(line)
            vrun.font.size = Pt(10)
    doc.add_paragraph()


def _document_history(doc, author: str, created: str) -> None:
    _heading(doc, "Document History")
    _body(
        doc,
        "The signatures below certify that this document has been reviewed and "
        "accepted, and demonstrates that the signatories are aware of all the "
        "requirements contained herein and are committed to ensuring their provision.",
    )
    table = doc.add_table(rows=4, cols=4)
    table.style = "Table Grid"
    _fixed_columns(table, [1.5, 2.0, 1.5, 1.5])
    headers = ["", "Name", "Signature", "Date"]
    for col, text in enumerate(headers):
        cell = table.cell(0, col)
        _shade(cell, TABLE_HEADER_BG if col else "FFFFFF")
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    rows = [("Created by", author, "Signed", created), ("Reviewed by", "", "", ""), ("Approved by", "", "", "")]
    for r, (label, name, signature, when) in enumerate(rows, start=1):
        cells = table.rows[r].cells
        _shade(cells[0], TABLE_HEADER_BG)
        run = cells[0].paragraphs[0].add_run(label)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        for idx, value in enumerate((name, signature, when), start=1):
            _shade(cells[idx], TABLE_VALUE_BG)
            vrun = cells[idx].paragraphs[0].add_run(value)
            vrun.font.size = Pt(10)
            vrun.bold = idx == 1
            cells[idx].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_paragraph()


def _summary_table(doc, groups: list[dict]) -> None:
    rows = 1 + sum(1 + len(g["items"]) for g in groups)
    table = doc.add_table(rows=rows, cols=3)
    table.style = "Table Grid"
    _fixed_columns(table, [0.7, 4.8, 1.0])
    for col, text in enumerate(("#", "Test Case", "Status")):
        cell = table.cell(0, col)
        _shade(cell, TABLE_HEADER_BG)
        run = cell.paragraphs[0].add_run(text)
        run.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    row_idx = 1
    case_no = 0
    for group in groups:
        cells = table.rows[row_idx].cells
        for cell in cells:
            _shade(cell, TABLE_VALUE_BG)
        run = cells[1].paragraphs[0].add_run(group["name"])
        run.bold = True
        run.font.size = Pt(10)
        row_idx += 1
        for item in group["items"]:
            case_no += 1
            cells = table.rows[row_idx].cells
            cells[0].paragraphs[0].add_run(f"TC-{case_no:02d}").font.size = Pt(10)
            cells[1].paragraphs[0].add_run(item["name"]).font.size = Pt(10)
            status_run = cells[2].paragraphs[0].add_run(item.get("status", ""))
            status_run.font.size = Pt(10)
            status_run.bold = True
            row_idx += 1
    doc.add_paragraph()


# ---------------------------------------------------------------------------
# Document assembly
# ---------------------------------------------------------------------------

def _configure_body_section(section, logo: Path | None) -> None:
    # Unlink from the cover section, otherwise the logo and page number are
    # inherited backwards onto the cover page.
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False

    header_para = section.header.paragraphs[0]
    header_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if logo and logo.exists():
        header_para.add_run().add_picture(str(logo), width=Inches(1.25))
    _paragraph_rule(header_para, "bottom", RULE_BLUE)

    footer_para = section.footer.paragraphs[0]
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    _paragraph_rule(footer_para, "top", RULE_BLUE)
    _page_number_field(footer_para)


def build_document(
    card,
    spec: dict,
    plugin_name: str,
    version: str,
    logo: Path | None,
    author: str,
) -> Document:
    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(11)

    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    title = f"{plugin_name} - V {version}"

    # --- Cover page (no header/footer) ------------------------------------
    for _ in range(10):
        doc.add_paragraph()
    if logo and logo.exists():
        cover = doc.add_paragraph()
        cover.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cover.add_run().add_picture(str(logo), width=Inches(4.2))
    cover_title = doc.add_paragraph()
    cover_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cover_title.add_run(title)
    run.font.size = Pt(15)

    # --- Body section ------------------------------------------------------
    body_section = doc.add_section(WD_SECTION.NEW_PAGE)
    body_section.top_margin = Inches(1)
    body_section.bottom_margin = Inches(1)
    body_section.left_margin = Inches(1)
    body_section.right_margin = Inches(1)
    _configure_body_section(body_section, logo)
    _restart_page_numbers(body_section)

    _document_history(doc, author=author, created=date.today().strftime("%d-%m-%y"))

    _heading(doc, "Testing details")
    _body(doc, "Following information specifies the plugin release details & testing observation.")
    _kv_table(
        doc,
        [
            ("Plugin name", plugin_name),
            ("Version", version),
            ("Changelog", spec.get("changelog", "")),
            ("Release details", spec.get("release_details", "")),
            ("Ticket Details", spec.get("ticket_url", "")),
            ("Trello Card", card.url),
            ("Observation", spec.get("overall_observation", "")),
        ],
    )

    doc.add_page_break()
    _heading(doc, "Details of Replicated")
    _body(doc, spec.get("replicated", ""))
    _evidence(doc, spec.get("replicated_screenshot", "Pre-fix behaviour — commercial invoice generated for the affected order"))

    doc.add_page_break()
    _heading(doc, "Pre-requisites", size=13)
    _kv_table(
        doc,
        [
            ("Store URL", spec.get("store_url", "")),
            ("Plugin under test", f"{plugin_name} v{version}"),
            ("Supporting setup", spec.get("prerequisites", "")),
        ],
        label_width=1.8,
    )
    for entry in spec.get("prerequisite_screenshots", []):
        _evidence(doc, entry)

    doc.add_page_break()
    _heading(doc, "TEST RESULT", size=15)
    _summary_table(doc, spec["groups"])

    case_no = 0
    for group in spec["groups"]:
        doc.add_page_break()
        _heading(doc, group["name"], size=13, color=RGBColor(0, 0, 0))
        for item in group["items"]:
            case_no += 1
            _heading(doc, f"TC-{case_no:02d} — {item['name']}", size=11, color=HEADING_BLUE, space_before=10)

            if item.get("steps"):
                _body(doc, "Steps", bold=True, size=10)
                for step_no, step in enumerate(item["steps"], start=1):
                    para = doc.add_paragraph()
                    para.paragraph_format.left_indent = Inches(0.25)
                    para.paragraph_format.space_after = Pt(2)
                    para.add_run(f"{step_no}. {step}").font.size = Pt(10)

            if item.get("expected"):
                _body(doc, "Expected Result", bold=True, size=10)
                para = doc.add_paragraph()
                para.paragraph_format.left_indent = Inches(0.25)
                para.add_run(item["expected"]).font.size = Pt(10)

            _body(doc, "Evidence", bold=True, size=10)
            for entry in item.get("screenshots") or ["attach evidence"]:
                _evidence(doc, entry)

            obs = doc.add_paragraph()
            obs.paragraph_format.space_after = Pt(14)
            obs_run = obs.add_run("Observation: ")
            obs_run.bold = True
            obs_run.font.size = Pt(10)
            trailing = obs.add_run(item.get("observation", ""))
            trailing.font.size = Pt(10)

    return doc


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _spec_from_card(card, spec: dict) -> dict:
    """Fill any missing group/item structure straight from the Trello checklists."""
    if spec.get("groups"):
        return spec
    spec["groups"] = [
        {"name": cl["name"], "items": [{"name": it["name"]} for it in cl["items"]]}
        for cl in card.checklists
    ]
    return spec


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("card_id", help="Trello card short link, e.g. SI23TDil")
    parser.add_argument("--steps", type=Path, help="JSON sidecar with steps/expected/screenshots")
    parser.add_argument("--plugin", required=True, help="Plugin name as it appears on the cover")
    parser.add_argument("--version", required=True, help="Release version under test")
    parser.add_argument("--author", default="", help="Name for the 'Created by' row")
    parser.add_argument("--logo", type=Path, default=ASSETS_DIR / "pluginhive_logo.png")
    parser.add_argument("--out", type=Path, help="Output .docx path")
    args = parser.parse_args()

    card = TrelloClient().get_card(args.card_id)
    spec = json.loads(args.steps.read_text()) if args.steps else {}
    spec = _spec_from_card(card, spec)

    doc = build_document(
        card=card,
        spec=spec,
        plugin_name=args.plugin,
        version=args.version,
        logo=args.logo,
        author=args.author,
    )

    out = args.out or OUTPUT_DIR / f"{args.plugin} - V{args.version}.docx"
    out.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
