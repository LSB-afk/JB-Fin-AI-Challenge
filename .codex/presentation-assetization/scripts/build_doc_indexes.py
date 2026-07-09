#!/usr/bin/env python3
"""Create or check two-level markdown indexes for a deck asset package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


CATEGORY_FILES = [
    "01-overview.md",
    "02-slides.md",
    "03-design-system.md",
    "04-assets.md",
    "05-qa.md",
    "06-process.md",
]


def markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def is_external(link: str) -> bool:
    return "://" in link or link.startswith("#") or link.startswith("mailto:")


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    for md in [root / "INDEX.md", *sorted((root / "indexes").glob("*.md"))]:
        if not md.exists():
            errors.append(f"Missing index file: {md.relative_to(root)}")
            continue
        for link in markdown_links(md.read_text(encoding="utf-8")):
            if is_external(link):
                continue
            target = link.split("#", 1)[0]
            if not target:
                continue
            if not (md.parent / target).exists():
                errors.append(f"Broken link in {md.relative_to(root)}: {link}")
    return errors


def render(root: Path) -> dict[Path, str]:
    slide_docs = sorted((root / "slides").glob("*-source-analysis.md"))
    token_docs = sorted((root / "tokens").glob("*"))
    files: dict[Path, str] = {}

    files[root / "INDEX.md"] = """# Presentation Assets Index

| Category | Index |
|---|---|
| Overview | [indexes/01-overview.md](indexes/01-overview.md) |
| Slides | [indexes/02-slides.md](indexes/02-slides.md) |
| Design System | [indexes/03-design-system.md](indexes/03-design-system.md) |
| Assets | [indexes/04-assets.md](indexes/04-assets.md) |
| QA | [indexes/05-qa.md](indexes/05-qa.md) |
| Process | [indexes/06-process.md](indexes/06-process.md) |
"""

    files[root / "indexes" / "01-overview.md"] = """# Overview Index

- [../README.md](../README.md)
- [../deck-definition.md](../deck-definition.md)
- [../manifest.json](../manifest.json)
"""
    slide_lines = "\n".join(f"- [../slides/{p.name}](../slides/{p.name})" for p in slide_docs)
    files[root / "indexes" / "02-slides.md"] = f"# Slides Index\n\n{slide_lines}\n"
    token_lines = "\n".join(
        f"- [../tokens/{p.name}](../tokens/{p.name})" for p in token_docs if p.is_file()
    )
    files[root / "indexes" / "03-design-system.md"] = (
        "# Design System Index\n\n"
        "- [../components/component-catalog.md](../components/component-catalog.md)\n"
        f"{token_lines}\n"
    )
    files[root / "indexes" / "04-assets.md"] = "# Assets Index\n\n- [../assets/asset-ledger.md](../assets/asset-ledger.md)\n"
    files[root / "indexes" / "05-qa.md"] = "# QA Index\n\n- [../qa/rebuild-diff.md](../qa/rebuild-diff.md)\n- [../qa/pdf-order-check.md](../qa/pdf-order-check.md)\n"
    files[root / "indexes" / "06-process.md"] = "# Process Index\n\n- [../process/ai-build-log.md](../process/ai-build-log.md)\n- [../process/rebuild-prompts.md](../process/rebuild-prompts.md)\n- [../process/parallel-agent-operating-model.md](../process/parallel-agent-operating-model.md)\n"
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--check", action="store_true", help="check existing indexes instead of writing")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if args.check:
        errors: list[str] = []
        if not (root / "INDEX.md").is_file():
            errors.append("Missing INDEX.md")
        for rel in CATEGORY_FILES:
            if not (root / "indexes" / rel).is_file():
                errors.append(f"Missing indexes/{rel}")
        errors.extend(check_links(root))
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"Indexes valid: {root}")
        return 0

    files = render(root)
    (root / "indexes").mkdir(parents=True, exist_ok=True)
    for path, text in files.items():
        path.write_text(text, encoding="utf-8")
        print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
