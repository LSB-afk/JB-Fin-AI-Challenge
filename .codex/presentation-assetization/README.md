---
name: figma-presentation-assetization-pack
version: 0.1.0
status: active
---

# Figma Presentation Assetization Pack

This package turns a finished Figma presentation deck into a reusable asset system: source analysis, design tokens, component catalog, rebuild workflow, visual QA, and handoff packaging.

Use the discoverable skill at `.agents/skills/figma-presentation-assetizer/SKILL.md`. This `.codex/presentation-assetization/` folder is the portable implementation body that can be copied to another repository.

## Modes

| Mode | Purpose | Source frame access |
|---|---|---|
| `source-preserving` | Clone source frames, preserve layers, add structure and QA | allowed |
| `componentized` | Replace repeated families with component instances after baseline QA | allowed |
| `blind-rebuild` | Rebuild from docs/tokens/assets only, then compare at QA time | forbidden during build |
| `derivative` | Create new slides in the same deck grammar | reference only |

## Required Flow

1. Confirm source, duplicate/editable Figma workspace, slide order, and output folder.
2. Run A1-A4 read-only analysis in parallel.
3. Let A5 be the only Figma writer.
4. Run A6 visual QA after every build or component promotion.
5. Record prompts, decisions, failures, and handoff package.

## Golden Example

Current reference package:

`08_본선/03_제품/03_ux/presentation-assets`

It contains the full JByond 14-slide deck assetization, including `deck-definition.md`, split tokens, component catalog, visual diff JSON, handoff docs, and final Figma node map.

## Operator Knowledge

Read these before repeating the workflow on another deck:

- `references/operator-knowhow.md`: practical lessons, failure modes, proof levels, and QA heuristics
- `references/reuse-playbook.md`: inputs, first-hour loop, AI prompt pattern, review checklist

## Scripts

```bash
python3 .codex/presentation-assetization/scripts/validate_package.py --root <presentation-assets>
python3 .codex/presentation-assetization/scripts/build_doc_indexes.py --root <presentation-assets> --check
python3 .codex/presentation-assetization/scripts/make_handoff_zip.py --root <presentation-assets> --check
python3 .codex/presentation-assetization/scripts/scaffold_deck_package.py --root <new-output-folder> --deck-name "Deck Name"
```

`visual_diff.py` uses Pillow when available. If Pillow is absent, it exits with a clear dependency message instead of silently passing.
