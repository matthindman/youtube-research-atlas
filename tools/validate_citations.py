#!/usr/bin/env python3
"""
validate_citations.py — structural citation validator for the atlas.

This script does NOT verify that a citation's claim is actually
supported by the cited source (that is a human task). It checks
mechanical invariants:

  1. Every quote has a page number ("(p. 12)" or "(pp. 12-14)").
  2. Every source_id referenced in a wiki page exists in
     data/source-registry.yaml.
  3. Every [[wikilink]] resolves to a real page.
  4. Every [NEEDS CITATION] marker is reported.

Writes a human-readable report to stdout and exits non-zero if any
critical errors are found.

Usage:
  python tools/validate_citations.py
  python tools/validate_citations.py --strict   # exit non-zero on warnings too
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None  # handled below


REPO = Path(__file__).resolve().parent.parent
WIKI = REPO / "wiki"
DATA = REPO / "data"

QUOTE_RE = re.compile(r'>\s*"([^"]+)"')
PAGE_CITE_RE = re.compile(r"\((?:pp?\.\s*\d+(?:-\d+)?|§\s*[\w.]+)")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
NEEDS_CITATION_RE = re.compile(r"\[NEEDS CITATION\]")
SOURCE_REF_RE = re.compile(r"\b([a-z][a-z0-9_]*_\d{4}[a-z0-9_]*)\b")


def load_registry() -> set[str]:
    """Return the set of source_ids known to the registry."""
    reg_path = DATA / "source-registry.yaml"
    if not reg_path.exists():
        return set()
    if yaml is None:
        # Fall back to a coarse regex parse so we don't hard-depend on PyYAML.
        text = reg_path.read_text()
        return set(re.findall(r"^\s*-\s+id:\s*(\S+)", text, re.MULTILINE))
    data = yaml.safe_load(reg_path.read_text()) or {}
    sources = data.get("sources") or []
    return {s.get("id") for s in sources if isinstance(s, dict) and s.get("id")}


def collect_pages() -> list[Path]:
    return sorted(p for p in WIKI.rglob("*.md") if p.is_file())


def page_slug(path: Path) -> str:
    return path.stem


CANONICAL_NAME_RE = re.compile(r"^canonical_name:\s*(\S+)\s*$", re.MULTILINE)


def canonical_names_for(path: Path) -> set[str]:
    """Return the set of identifiers that can target this page.

    Always includes the file stem. If the frontmatter contains
    canonical_name, includes that too — theme and dossier pages use
    canonical_name as their wikilink target even when the filename
    is something generic like dossier.md.
    """
    names = {path.stem}
    try:
        text = path.read_text()
    except OSError:
        return names
    m = CANONICAL_NAME_RE.search(text)
    if m:
        names.add(m.group(1).strip().strip('"').strip("'"))
    return names


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                        help="Exit non-zero on warnings as well as errors.")
    args = parser.parse_args()

    pages = collect_pages()
    known_slugs: set[str] = set()
    for p in pages:
        known_slugs.update(canonical_names_for(p))
    known_sources = load_registry()

    errors: list[str] = []
    warnings: list[str] = []
    needs_citation: list[str] = []

    for page in pages:
        rel = page.relative_to(REPO)
        text = page.read_text()

        # 1. Quotes must be followed by a page number (allow up to 80 chars
        #    between the closing quote and the page cite — accommodates
        #    trailing punctuation and verification markers).
        for m in QUOTE_RE.finditer(text):
            start = m.end()
            tail = text[start:start + 80]
            if not PAGE_CITE_RE.search(tail):
                line_no = text.count("\n", 0, m.start()) + 1
                errors.append(
                    f"{rel}:{line_no}: quote without page number: "
                    f"\"{m.group(1)[:60]}...\""
                )

        # 2. Wikilinks must resolve to a known page slug.
        for m in WIKILINK_RE.finditer(text):
            target = m.group(1).strip()
            if target in ("", "TODO"):
                continue
            if target not in known_slugs:
                line_no = text.count("\n", 0, m.start()) + 1
                warnings.append(
                    f"{rel}:{line_no}: broken wikilink [[{target}]]"
                )

        # 3. NEEDS CITATION markers.
        for m in NEEDS_CITATION_RE.finditer(text):
            line_no = text.count("\n", 0, m.start()) + 1
            needs_citation.append(f"{rel}:{line_no}")

        # 4. Source refs — loose heuristic for author_year slugs.
        #    Flag any slug that looks like a source_id but is not in the
        #    registry. This catches typos and unregistered sources but
        #    will also flag legitimate non-source slugs, so it is a warning,
        #    not an error.
        if known_sources:
            for m in SOURCE_REF_RE.finditer(text):
                candidate = m.group(1)
                # Skip canonical_name slugs used for theme/method pages.
                if candidate in known_slugs and candidate not in known_sources:
                    continue
                if candidate not in known_sources and "_" in candidate:
                    # Only warn if the candidate appears inside a citation-ish
                    # context: preceded by "(" or "[[" or "source_id:".
                    start = max(0, m.start() - 12)
                    context = text[start:m.start()]
                    if any(tok in context for tok in ("source_id:", "sources:", "[[")):
                        line_no = text.count("\n", 0, m.start()) + 1
                        warnings.append(
                            f"{rel}:{line_no}: unregistered source_id "
                            f"'{candidate}'"
                        )

    # Report.
    print(f"# Atlas citation validation — {len(pages)} pages scanned")
    print()
    print(f"Errors:            {len(errors)}")
    print(f"Warnings:          {len(warnings)}")
    print(f"[NEEDS CITATION]:  {len(needs_citation)}")
    print()

    if errors:
        print("## Errors")
        for e in errors:
            print(f"- {e}")
        print()
    if warnings:
        print("## Warnings")
        for w in warnings:
            print(f"- {w}")
        print()
    if needs_citation:
        print("## [NEEDS CITATION]")
        for n in needs_citation:
            print(f"- {n}")
        print()

    if errors:
        return 1
    if args.strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
