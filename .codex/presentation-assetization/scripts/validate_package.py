#!/usr/bin/env python3
"""Validate a Figma presentation assetization package."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_ROOT_FILES = [
    "README.md",
    "INDEX.md",
    "deck-definition.md",
    "manifest.json",
]

REQUIRED_DIRS = [
    "slides",
    "tokens",
    "components",
    "assets",
    "qa",
    "process",
    "handoff",
]

REQUIRED_TOKEN_FILES = [
    "token-index.json",
    "primitives.json",
    "semantic.json",
    "typography.json",
    "fonts.json",
    "effects.json",
    "surfaces.json",
    "components.json",
    "slides.json",
    "assets.json",
    "qa-rules.json",
]

REQUIRED_HANDOFF_FILES = [
    "README.md",
    "team-quickstart.md",
    "ai-reuse-runbook.md",
    "figma-usage-guide.md",
    "share-checklist.md",
]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        fail(errors, f"Invalid JSON: {path}: {exc}")
        return None


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    if not root.exists():
        return [f"Root does not exist: {root}"]
    if not root.is_dir():
        return [f"Root is not a directory: {root}"]

    for rel in REQUIRED_ROOT_FILES:
        if not (root / rel).is_file():
            fail(errors, f"Missing root file: {rel}")

    for rel in REQUIRED_DIRS:
        if not (root / rel).is_dir():
            fail(errors, f"Missing directory: {rel}/")

    for rel in REQUIRED_TOKEN_FILES:
        if not (root / "tokens" / rel).is_file():
            fail(errors, f"Missing token file: tokens/{rel}")

    for rel in REQUIRED_HANDOFF_FILES:
        if not (root / "handoff" / rel).is_file():
            fail(errors, f"Missing handoff file: handoff/{rel}")

    for json_path in sorted(root.rglob("*.json")):
        load_json(json_path, errors)

    manifest_path = root / "manifest.json"
    manifest = load_json(manifest_path, errors) if manifest_path.exists() else None
    if isinstance(manifest, dict):
        source_refs = manifest.get("sourceReferences", {})
        if not isinstance(source_refs, dict):
            fail(errors, "manifest.sourceReferences must be an object")
        else:
            for key in ["documentIndex", "deckDefinition", "handoffPackage"]:
                if key not in source_refs:
                    fail(errors, f"manifest.sourceReferences.{key} is missing")
            handoff = source_refs.get("handoffPackage")
            if isinstance(handoff, dict):
                for key in ["entry", "quickstart", "aiReuseRunbook", "figmaUsageGuide", "shareChecklist"]:
                    rel = handoff.get(key)
                    if not isinstance(rel, str) or not (root / rel).exists():
                        fail(errors, f"handoffPackage.{key} target missing: {rel}")

        if "qualityGates" not in manifest:
            fail(errors, "manifest.qualityGates is missing")
        if "tokenSystem" not in manifest:
            fail(errors, "manifest.tokenSystem is missing")

    slide_docs = sorted((root / "slides").glob("*-source-analysis.md")) if (root / "slides").exists() else []
    if not slide_docs:
        fail(errors, "No slide source-analysis docs found")

    index_dir = root / "indexes"
    if index_dir.exists():
        for rel in ["01-overview.md", "02-slides.md", "03-design-system.md", "04-assets.md", "05-qa.md", "06-process.md"]:
            if not (index_dir / rel).is_file():
                fail(errors, f"Missing category index: indexes/{rel}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, help="presentation-assets root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Package valid: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
