#!/usr/bin/env python3
"""Compare two images and report simple pixel-diff metrics."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("target")
    parser.add_argument("--output")
    args = parser.parse_args()

    try:
        from PIL import Image, ImageChops
    except ImportError:
        print("ERROR: Pillow is required for visual_diff.py. Install pillow or run QA with another image diff tool.", file=sys.stderr)
        return 2

    source_path = Path(args.source)
    target_path = Path(args.target)
    source = Image.open(source_path).convert("RGBA")
    target = Image.open(target_path).convert("RGBA")
    if source.size != target.size:
        result = {
            "source": str(source_path),
            "target": str(target_path),
            "sameSize": False,
            "sourceSize": source.size,
            "targetSize": target.size,
            "similarity": 0.0,
        }
    else:
        diff = ImageChops.difference(source, target)
        width, height = source.size
        changed = 0
        bbox = diff.getbbox()
        for pixel in diff.getdata():
            if pixel != (0, 0, 0, 0):
                changed += 1
        total = width * height
        result = {
            "source": str(source_path),
            "target": str(target_path),
            "sameSize": True,
            "size": [width, height],
            "changedPixels": changed,
            "totalPixels": total,
            "similarity": 1 - (changed / total),
            "bbox": list(bbox) if bbox else None,
        }
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
