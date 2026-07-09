# Reuse Playbook

Use this when starting a new Figma presentation assetization project from the skill pack.

## Inputs

Collect these before building:

| Input | Required | Notes |
|---|---:|---|
| Source Figma URL | yes | read-only is enough for analysis; write access must be duplicate/new file |
| Editable working Figma URL | yes | A5 writes only here |
| Final PDF or exported deck | strongly recommended | confirms order and visual truth |
| Target slide list | yes | start with 1-3 slides for calibration |
| Font sources | yes | record provider, license, local files, fallback risk |
| Output folder | yes | normally `<project>/presentation-assets` |

## First 60 Minutes

1. Scaffold the package.
2. Confirm Figma source, editable duplicate, PDF order, and write lock.
3. Capture source screenshots for target slides.
4. Write slide inventory and manifest node map.
5. Pick one calibration slide.
6. Extract initial tokens and assets for that slide.
7. Build source-preserving clone.
8. Run visual QA before expanding.

## Daily Loop

| Phase | Output |
|---|---|
| Ingest | `slides/*-source-analysis.md`, source screenshots |
| Tokenize | `tokens/*.json`, `tokens/token-notes.md` |
| Harvest | `assets/asset-ledger.md`, images, fonts, tables, graphs |
| Build | Figma node IDs, rebuild screenshots |
| QA | `qa/rebuild-diff.md`, visual diff JSON/images |
| Log | `process/ai-build-log.md`, `process/rebuild-prompts.md` |
| Package | `INDEX.md`, handoff docs, zip |

## Prompt Pattern For AI Builders

```text
Use $figma-presentation-assetizer.

Mode: <source-preserving | componentized | blind-rebuild | handoff-packaging>
Source: <Figma URL or package folder>
Editable target: <Figma duplicate URL, if writing>
Slides: <slide numbers and names>
Constraints:
- original Figma must not be mutated
- A5 is the only Figma writer
- no full-slide flattened rebuild
- preserve fonts/images when fidelity matters
- run visual QA and update manifest/process logs
Expected output:
- updated package docs/assets/tokens/QA
- Figma node IDs if a rebuild is created
- clear pass/fail and residual risks
```

## Review Checklist

Ask these questions before saying the package is reusable:

- Can a new reader find the entry point from `INDEX.md`?
- Can an AI locate source node IDs, final node IDs, and screenshot paths from `manifest.json`?
- Are the fonts and image sources recorded?
- Are tokens split enough for machine use?
- Are repeated elements either components or documented candidates?
- Does QA show before/after evidence, not just assertions?
- Does the handoff say what is proven and what is not proven?
- Is the shareable archive regenerated after document changes?

## Escalation Rules

| Situation | Action |
|---|---|
| Original and PDF disagree | document the discrepancy; use PDF for presentation order |
| Figma access is read-only | do analysis only; wait for duplicate/new editable target before A5 |
| Font missing | preserve source text layers or record risk; do not silently substitute |
| Visual diff is large | fix calibration slide before scaling |
| User asks for prompt-only proof | convert request into blind rebuild QA |
| Multiple agents want to edit Figma | stop; route write work through A5 |
