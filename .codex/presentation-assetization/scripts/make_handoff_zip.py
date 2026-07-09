#!/usr/bin/env python3
"""Create or verify a shareable handoff zip for a deck asset package."""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from datetime import date
from pathlib import Path


EXCLUDE_NAMES = {".DS_Store"}


def archive_from_manifest(root: Path) -> Path | None:
    manifest_path = root / "manifest.json"
    if not manifest_path.exists():
        return None
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    handoff = manifest.get("sourceReferences", {}).get("handoffPackage", {})
    rel = handoff.get("shareableArchive")
    if isinstance(rel, str) and rel:
        return (root / rel).resolve()
    return None


def default_archive(root: Path) -> Path:
    return root.parent / f"{root.name}-handoff-{date.today().isoformat()}.zip"


def should_include(path: Path) -> bool:
    return path.name not in EXCLUDE_NAMES and not path.name.endswith(".zip")


def create_zip(root: Path, archive: Path) -> None:
    archive.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(root.rglob("*")):
            if not should_include(path):
                continue
            zf.write(path, path.relative_to(root.parent))


def test_zip(archive: Path) -> list[str]:
    if not archive.is_file():
        return [f"Archive not found: {archive}"]
    with zipfile.ZipFile(archive, "r") as zf:
        bad = zf.testzip()
        if bad:
            return [f"Corrupt entry in archive: {bad}"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--output", help="optional archive path")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    archive = Path(args.output).resolve() if args.output else archive_from_manifest(root) or default_archive(root)

    if args.check:
        errors = test_zip(archive)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"Archive valid: {archive}")
        return 0

    create_zip(root, archive)
    errors = test_zip(archive)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Archive written: {archive}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
