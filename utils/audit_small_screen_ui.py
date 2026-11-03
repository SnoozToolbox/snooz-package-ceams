#!/usr/bin/env python3
"""
Audit Qt .ui files for small-screen responsiveness risks.

This script reports likely anti-patterns that can inflate minimum window size
or reduce readability on small displays/high DPI scaling.

With --style, it instead reports styling hardcoded in Qt Designer that blocks
the Snooz theme: inline style sheets setting fonts or colors, and widget fonts
with a hardcoded family or point size. The application already sets the font
(Roboto 12pt) and the theme (stylesheet.qss) for every form; per-widget styling
should use a dynamic property (e.g. role=heading) styled in stylesheet.qss.
Add --strict to exit with code 1 when issues are found (pre-commit / release).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

TEXT_WIDGETS = {"QTextEdit", "QPlainTextEdit"}
# Style sheet declarations that override the application font or theme colors.
THEME_BLOCKING_DECLARATION_RE = re.compile(
    r"(?:^|[;{\s])(font(?:-family|-size|-weight|-style)?|color|background(?:-color)?)\s*:", re.IGNORECASE
)


def _is_ui_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() == ".ui"


def _iter_ui_files(root: Path):
    for path in root.rglob("*.ui"):
        if "/target/" in path.as_posix() or "__pycache__" in path.as_posix():
            continue
        yield path


def _get_text(elem: ET.Element, xpath: str, default: str = "") -> str:
    node = elem.find(xpath)
    return (node.text or default).strip() if node is not None else default


def _to_int(value: str, fallback: int = 0) -> int:
    try:
        return int(value)
    except Exception:
        return fallback


def audit_ui_file(path: Path) -> dict:
    result = {
        "file": str(path),
        "score": 0,
        "issues": [],
    }

    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        result["score"] += 10
        result["issues"].append(f"XML parse error: {exc}")
        return result

    # Root geometry hint that often indicates desktop-first design.
    geom_width = _to_int(_get_text(root, "./widget/property[@name='geometry']/rect/width", "0"))
    geom_height = _to_int(_get_text(root, "./widget/property[@name='geometry']/rect/height", "0"))
    if geom_width > 1200 or geom_height > 900:
        result["score"] += 2
        result["issues"].append(f"Large design geometry hint: {geom_width}x{geom_height}")

    # Scan every widget for risky size policies and content-driven sizing.
    for widget in root.findall(".//widget"):
        cls = widget.attrib.get("class", "")
        name = widget.attrib.get("name", "<unnamed>")

        # Fixed policy can make layouts rigid on small screens.
        sp = widget.find("./property[@name='sizePolicy']/sizepolicy")
        if sp is not None:
            hs = sp.attrib.get("hsizetype", "")
            vs = sp.attrib.get("vsizetype", "")
            if hs == "Fixed":
                result["score"] += 1
                result["issues"].append(f"{name}: hsizetype=Fixed")
            if vs == "Fixed" and cls in TEXT_WIDGETS:
                result["score"] += 2
                result["issues"].append(f"{name}: text widget with vsizetype=Fixed")

        # QTextEdit/QPlainTextEdit: AdjustToContents frequently inflates minimum hints.
        if cls in TEXT_WIDGETS:
            adjust = _get_text(widget, "./property[@name='sizeAdjustPolicy']/enum", "")
            if "AdjustToContents" in adjust:
                result["score"] += 3
                result["issues"].append(f"{name}: sizeAdjustPolicy=AdjustToContents")

            max_h = _to_int(_get_text(widget, "./property[@name='maximumSize']/size/height", "16777215"), 16777215)
            if 0 < max_h < 1000:
                result["score"] += 2
                result["issues"].append(f"{name}: maxHeight={max_h}")

            min_h = _to_int(_get_text(widget, "./property[@name='minimumSize']/size/height", "0"), 0)
            if min_h >= 200:
                result["score"] += 2
                result["issues"].append(f"{name}: minHeight={min_h}")

    return result


def audit_ui_style(path: Path) -> dict:
    """Report styling hardcoded in Qt Designer that overrides the Snooz theme."""
    result = {
        "file": str(path),
        "score": 0,
        "issues": [],
    }

    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        result["score"] += 1
        result["issues"].append(f"XML parse error: {exc}")
        return result

    root_widget = root.find("./widget")
    for widget in root.iter("widget"):
        name = widget.attrib.get("name", "<unnamed>")
        label = f"{name} (root)" if widget is root_widget else name

        sheet = _get_text(widget, "./property[@name='styleSheet']/string", "")
        declarations = sorted({m.lower() for m in THEME_BLOCKING_DECLARATION_RE.findall(sheet)})
        if declarations:
            result["score"] += 3 if widget is root_widget else 1
            result["issues"].append(f"{label}: styleSheet sets {', '.join(declarations)}: {sheet[:60]}")

        family = _get_text(widget, "./property[@name='font']/font/family", "")
        point_size = _get_text(widget, "./property[@name='font']/font/pointsize", "")
        if family or point_size:
            result["score"] += 1
            result["issues"].append(f"{label}: hardcoded font {family} {point_size + 'pt' if point_size else ''}".rstrip())

    return result


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Audit Qt .ui files for small-screen responsiveness risks")
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan")
    parser.add_argument("--min-score", type=int, default=None,
                        help="Show only files with score >= this value (default: 4, or 1 with --style)")
    parser.add_argument("--top", type=int, default=50, help="Maximum number of results to display")
    parser.add_argument("--style", action="store_true",
                        help="Audit hardcoded fonts/colors that block the theme instead of small-screen risks")
    parser.add_argument("--strict", action="store_true",
                        help="Exit with code 1 if any file reaches --min-score (for pre-commit or release checks)")
    args = parser.parse_args(argv)
    if args.min_score is None:
        args.min_score = 1 if args.style else 4

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root does not exist: {root}")
        return 2

    files = [p for p in _iter_ui_files(root) if _is_ui_file(p)]
    audit = audit_ui_style if args.style else audit_ui_file
    audits = [audit(p) for p in files]
    audits.sort(key=lambda x: x["score"], reverse=True)

    shown = 0
    for item in audits:
        if item["score"] < args.min_score:
            continue
        print(f"[{item['score']:>2}] {Path(item['file']).as_posix()}")
        for issue in item["issues"][:8]:
            print(f"     - {issue}")
        if len(item["issues"]) > 8:
            print(f"     - ... {len(item['issues']) - 8} more")
        shown += 1
        if shown >= args.top:
            break

    if shown == 0:
        print("No high-risk files found with current threshold.")
    else:
        flagged = sum(1 for item in audits if item["score"] >= args.min_score)
        print(f"\nReported {shown} of {flagged} file(s) with score >= {args.min_score}.")

    if args.strict and any(item["score"] >= args.min_score for item in audits):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
