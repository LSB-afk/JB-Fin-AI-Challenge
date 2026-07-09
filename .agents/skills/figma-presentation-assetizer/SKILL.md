---
name: figma-presentation-assetizer
description: Use when a user asks to reverse engineer, assetize, tokenize, componentize, rebuild, visually QA, blind-rebuild, or hand off a Figma presentation deck or slide system.
---

# Figma Presentation Assetizer

## Core Principle

Treat a finished deck as a production asset system, not a screenshot pile. Preserve the source, extract structure, build tokens/components, rebuild in Figma, verify visually, and package handoff evidence.

## Required Companion Skills

- **REQUIRED for Figma tool calls:** load and follow `figma-use`.
- **REQUIRED for new skill edits:** follow `skill-creator` and `writing-skills`.

## Modes

| Mode | Use when | Key restriction |
|---|---|---|
| Source-preserving rebuild | Need high-fidelity editable copy from source | clone/structure before redrawing |
| Componentized rebuild | Repeated elements should become reusable components | promote one family, then QA |
| Blind rebuild | Need proof docs/assets/tokens can recreate a slide | do not inspect source/final frame during build |
| Handoff packaging | Team or AI must reuse the result | produce index, runbook, archive, QA links |

## Non-Negotiables

- Do not mutate the original Figma file.
- Only A5 Figma Slide Builder may write to Figma.
- Do not use a full-slide flattened image as rebuild content.
- Do not mark pass without visual evidence.
- Preserve source text/font metadata when required fonts are unavailable.
- Record assets, tokens, components, prompts, risks, and QA drift.

## Workflow

1. Read package state: `README.md`, `INDEX.md`, `manifest.json`, and `deck-definition.md` if present.
2. Select mode from the table above.
3. Read only the relevant reference:
   - `references/workflow.md`
   - `references/agent-model.md`
   - `references/figma-write-lock.md`
   - `references/qa-rules.md`
   - `references/package-schema.md`
   - `references/operator-knowhow.md`
4. Use `.codex/presentation-assetization/` scripts/templates when present.
5. Finish with validation and a concise handoff.

## Red Flags

Stop and correct course if you are about to:

- rebuild from a screenshot because it is faster
- let multiple agents write to Figma
- skip visual diff after component promotion
- call a prompt-only generation “proved” without blind rebuild QA
- overwrite the source or accepted final page
