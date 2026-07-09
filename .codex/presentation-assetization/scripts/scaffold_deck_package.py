#!/usr/bin/env python3
"""Scaffold a new presentation assetization package."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


ROOT_FILES = {
    "README.md": "# {{deck_name}} Presentation Assetization\n\nStart with `INDEX.md`, `deck-definition.md`, and `manifest.json`.\n",
    "INDEX.md": """# Presentation Assets Index

| Category | Index |
|---|---|
| Overview | [indexes/01-overview.md](indexes/01-overview.md) |
| Slides | [indexes/02-slides.md](indexes/02-slides.md) |
| Design System | [indexes/03-design-system.md](indexes/03-design-system.md) |
| Assets | [indexes/04-assets.md](indexes/04-assets.md) |
| QA | [indexes/05-qa.md](indexes/05-qa.md) |
| Process | [indexes/06-process.md](indexes/06-process.md) |
| Handoff | [indexes/07-handoff.md](indexes/07-handoff.md) |
""",
    "deck-definition.md": "# {{deck_name}} Deck Definition\n\nDescribe thesis, narrative arc, design philosophy, visual grammar, and quality gates.\n",
}

DIRS = [
    "slides",
    "tokens",
    "components",
    "assets",
    "assets/source-screenshots",
    "assets/rebuild-screenshots",
    "assets/images",
    "assets/components",
    "assets/fonts",
    "qa",
    "qa/visual-diff",
    "process",
    "handoff",
    "indexes",
]

TOKEN_JSON_FILES = [
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

HANDOFF_FILES = {
    "README.md": "# Handoff\n\nUse this folder to package team-facing reuse instructions.\n",
    "team-quickstart.md": "# Team Quickstart\n\nSummarize the first reading path for designers, PMs, builders, and QA.\n",
    "ai-reuse-runbook.md": "# AI Reuse Runbook\n\nDescribe source inputs, token usage, component rules, and QA loop.\n",
    "figma-usage-guide.md": "# Figma Usage Guide\n\nRecord working file URLs, source pages, rebuild pages, and write-lock rules.\n",
    "share-checklist.md": "# Share Checklist\n\n- [ ] Source preserved\n- [ ] Tokens documented\n- [ ] QA completed\n",
}

INDEX_FILES = {
    "01-overview.md": "# Overview Index\n\n- [../README.md](../README.md)\n- [../deck-definition.md](../deck-definition.md)\n- [../manifest.json](../manifest.json)\n",
    "02-slides.md": "# Slides Index\n\n- [../slides/01-placeholder-source-analysis.md](../slides/01-placeholder-source-analysis.md)\n",
    "03-design-system.md": "# Design System Index\n\n- [../tokens/README.md](../tokens/README.md)\n- [../components/component-catalog.md](../components/component-catalog.md)\n",
    "04-assets.md": "# Assets Index\n\n- [../assets/asset-ledger.md](../assets/asset-ledger.md)\n",
    "05-qa.md": "# QA Index\n\n- [../qa/rebuild-diff.md](../qa/rebuild-diff.md)\n- [../qa/pdf-order-check.md](../qa/pdf-order-check.md)\n",
    "06-process.md": "# Process Index\n\n- [../process/ai-build-log.md](../process/ai-build-log.md)\n- [../process/rebuild-prompts.md](../process/rebuild-prompts.md)\n- [../process/parallel-agent-operating-model.md](../process/parallel-agent-operating-model.md)\n",
    "07-handoff.md": "# Handoff Index\n\n- [../handoff/README.md](../handoff/README.md)\n- [../handoff/team-quickstart.md](../handoff/team-quickstart.md)\n- [../handoff/ai-reuse-runbook.md](../handoff/ai-reuse-runbook.md)\n- [../handoff/figma-usage-guide.md](../handoff/figma-usage-guide.md)\n- [../handoff/share-checklist.md](../handoff/share-checklist.md)\n",
}


def write(path: Path, text: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True)
    parser.add_argument("--deck-name", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    for rel in DIRS:
        (root / rel).mkdir(parents=True, exist_ok=True)

    mapping = {"{{deck_name}}": args.deck_name, "YYYY-MM-DD": date.today().isoformat()}
    for rel, text in ROOT_FILES.items():
        for key, value in mapping.items():
            text = text.replace(key, value)
        write(root / rel, text, args.force)

    manifest = {
        "project": f"{args.deck_name} presentation deck assetization",
        "version": f"assetization-{date.today().isoformat()}",
        "status": "initialized",
        "sourceReferences": {
            "documentIndex": "INDEX.md",
            "categoryIndexes": [f"indexes/{name}" for name in INDEX_FILES],
            "deckDefinition": "deck-definition.md",
            "handoffPackage": {
                "entry": "handoff/README.md",
                "quickstart": "handoff/team-quickstart.md",
                "aiReuseRunbook": "handoff/ai-reuse-runbook.md",
                "figmaUsageGuide": "handoff/figma-usage-guide.md",
                "shareChecklist": "handoff/share-checklist.md",
            },
        },
        "codexSkillPack": {
            "version": "0.1.0",
            "portableRoot": ".codex/presentation-assetization",
            "runtimeSkill": ".agents/skills/figma-presentation-assetizer/SKILL.md",
            "recommendedInvocation": "$figma-presentation-assetizer",
            "references": {
                "operatorKnowhow": ".codex/presentation-assetization/references/operator-knowhow.md",
                "reusePlaybook": ".codex/presentation-assetization/references/reuse-playbook.md",
            },
        },
        "tokenSystem": {
            "status": "initialized_placeholders",
            "index": "tokens/token-index.json",
            "sourceOfTruth": [f"tokens/{name}" for name in TOKEN_JSON_FILES if name != "token-index.json"],
            "humanReadable": ["tokens/README.md", "tokens/token-notes.md"],
        },
        "qualityGates": {
            "frameSize": "1920x1080",
            "minSimilarity": 0.98,
            "noFullSlideFlatten": True,
            "visualQaRequired": True,
        },
        "slides": [],
    }
    write(root / "manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", args.force)
    write(
        root / "slides" / "01-placeholder-source-analysis.md",
        "# 01 Placeholder Source Analysis\n\nReplace this file with real source analysis after ingestion.\n",
        args.force,
    )
    for name in TOKEN_JSON_FILES:
        payload = {
            "status": "initialized_placeholder",
            "deckName": args.deck_name,
            "replaceBeforeBuild": True,
        }
        if name == "token-index.json":
            payload["files"] = [f"tokens/{item}" for item in TOKEN_JSON_FILES if item != "token-index.json"]
        write(root / "tokens" / name, json.dumps(payload, ensure_ascii=False, indent=2) + "\n", args.force)
    write(root / "tokens" / "README.md", "# Token System\n\nReplace placeholders with extracted deck tokens.\n", args.force)
    write(root / "tokens" / "token-notes.md", "# Token Notes\n\n", args.force)
    write(root / "components" / "component-catalog.md", "# Component Catalog\n\n", args.force)
    write(root / "assets" / "asset-ledger.md", "# Asset Ledger\n\n", args.force)
    write(root / "qa" / "rebuild-diff.md", "# Rebuild Diff And QA Loop\n\n", args.force)
    write(root / "qa" / "pdf-order-check.md", "# PDF Order Check\n\n", args.force)
    write(root / "process" / "ai-build-log.md", "# AI Build Log\n\n", args.force)
    write(root / "process" / "rebuild-prompts.md", "# Rebuild Prompts\n\n", args.force)
    write(root / "process" / "parallel-agent-operating-model.md", "# Parallel Agent Operating Model\n\n", args.force)
    for name, text in HANDOFF_FILES.items():
        write(root / "handoff" / name, text, args.force)
    for name, text in INDEX_FILES.items():
        write(root / "indexes" / name, text, args.force)
    print(f"Scaffolded: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
