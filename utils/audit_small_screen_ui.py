#!/usr/bin/env python3
"""
Audit Qt .ui files for small-screen responsiveness risks.

This script reports likely anti-patterns that can inflate minimum window size
or reduce readability on small displays/high DPI scaling.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

TEXT_WIDGETS = {"QTextEdit", "QPlainTextEdit"}


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


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Audit Qt .ui files for small-screen responsiveness risks")
    parser.add_argument("root", nargs="?", default=".", help="Root directory to scan")
    parser.add_argument("--min-score", type=int, default=4, help="Show only files with score >= this value")
    parser.add_argument("--top", type=int, default=50, help="Maximum number of results to display")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Root does not exist: {root}")
        return 2

    files = [p for p in _iter_ui_files(root) if _is_ui_file(p)]
    audits = [audit_ui_file(p) for p in files]
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
        print(f"\nReported {shown} file(s) with score >= {args.min_score}.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
