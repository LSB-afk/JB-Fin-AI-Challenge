# Operator Know-How

This is the practical field guide distilled from the JByond Figma deck assetization run. It is for humans and AI agents who need to repeat the work without rediscovering the same failure modes.

## Core Lesson

A finished presentation deck is not one asset. Treat it as five linked systems:

| System | What to capture | Why it matters |
|---|---|---|
| Narrative | deck thesis, slide role, sequence, emphasis | preserves intent when slides change |
| Visual grammar | layout, typography, color, effects, density | makes rebuilds feel designed, not approximated |
| Source structure | frames, layers, text, images, tables, components | enables editable reconstruction |
| Reuse model | tokens, component candidates, variants, naming | makes the deck extensible |
| Evidence loop | screenshots, diffs, QA notes, prompts, decisions | prevents unverified claims |

## What Worked

- Use the final PDF to confirm slide order before naming or rebuilding frames.
- Work from an editable duplicate or pasted working source, never the original.
- Start with one calibration slide before scaling. The first accepted slide teaches the typography, spacing, image handling, and QA threshold.
- Preserve source images when fidelity matters. Recreate structure around them instead of replacing them with generic approximations.
- Separate source-preserving rebuild from componentized rebuild. First prove the slide can be cloned structurally, then promote components.
- Promote one repeated family at a time. Every promotion changes geometry risk.
- Prefer exact-geometry component variants for dense decks. Flexible components are useful later, but exact variants protect pixel-critical presentation work.
- Keep screenshots as QA/reference assets, not as the rebuild itself.
- Record node IDs immediately. Figma work becomes hard to audit if source/rebuild/final IDs are not captured while fresh.

## What Failed Or Drifted

| Failure mode | Symptom | Correct response |
|---|---|---|
| Prompt-only overclaim | Agent says a prompt can reproduce the deck | require assets, tokens, source analysis, components, and visual QA |
| Placeholder rebuild | Output looks like a generic deck | return to source screenshots, typography, exact crops, and slide-level role |
| Missing fonts | Re-entered text falls back to wrong font | preserve source text or document font risk before retyping |
| Broad component drift | Reusable component changes layout subtly | create exact-geometry variants and re-run full-slide QA |
| Full-slide flatten shortcut | Rebuild is just a screenshot | reject as assetization failure |
| Parallel Figma mutation | Multiple agents edit same file | enforce A5-only Figma write lock |
| Late documentation | Node IDs and decisions are reconstructed from memory | update manifest, QA, and process log during the run |

## Operating Heuristics

| Decision | Default |
|---|---|
| Unsure whether source or final differs from PDF | trust PDF order, then record discrepancy |
| Unsure whether an image should be recreated | preserve/export original image first |
| Unsure whether a repeated element should be a component | document as candidate; promote only after the source-preserving pass |
| Unsure whether a component abstraction is too flexible | choose exact-geometry variant for the pilot, note future flexible version |
| Unsure whether QA passed | fail or mark conditional; do not mark pass without visual evidence |
| Unsure whether to ask multiple agents to write Figma | do not; only A5 writes |

## Tokenization Lessons

Use three layers of tokens:

1. Primitive tokens: raw colors, type sizes, radii, shadows, blur values, spacing.
2. Semantic tokens: deck background, emphasis text, primary stroke, evidence highlight, glass surface, muted caption.
3. Component tokens: card surface, timeline node, flow connector, quote block, table row, cover wordmark.

Do not rely only on `presentation-tokens.json`. Keep split machine-readable files so AI can retrieve exactly what it needs without loading the whole system.

## Component Lessons

Promote components only when the family is real:

- 2+ uses in the deck, or
- one complex object that is likely to recur in derivative slides, or
- a pixel-critical object that needs exact preservation.

Document component status explicitly:

| Status | Meaning |
|---|---|
| `candidate` | repeated or valuable, not yet promoted |
| `promoted_v1` | usable component, may have drift risk |
| `exact_geometry` | source-derived, pixel-critical variant |
| `future_flexible` | should be redesigned after fidelity is proven |

## QA Lessons

Slide QA is not a final screenshot glance. Minimum evidence:

- source screenshot path
- rebuild screenshot path
- pixel or manual diff notes
- text clipping check
- flatten-image check
- token/component usage check
- known drift and accepted risk

Use visual QA after every build step that changes geometry: cloning, component replacement, font substitution, image crop, or final page movement.

## Agent Coordination Lessons

A1-A4 can run in parallel because they read different surfaces. A5 cannot be parallelized because Figma mutation is shared state. A6 should be independent enough to disagree with A5.

Use the six-block handoff after every agent pass:

1. Scope handled
2. Files or Figma nodes touched
3. Evidence produced
4. Decisions made
5. Risks or gaps
6. Next recommended action

## Proof Levels

Be precise about what has been proven.

| Claim | Required proof |
|---|---|
| Source was analyzed | slide source-analysis, assets, token notes |
| Source was preserved | editable clone or source-preserving rebuild with screenshots |
| Componentization works | component catalog, instance usage, QA after promotion |
| AI can reuse the package | blind rebuild from docs/tokens/assets only, then QA |
| Prompt alone is enough | almost never true; requires repeated blind rebuild success without hidden source access |

## Minimum Closeout

Before handoff, run:

```bash
python3 .codex/presentation-assetization/scripts/validate_package.py --root <presentation-assets>
python3 .codex/presentation-assetization/scripts/build_doc_indexes.py --root <presentation-assets> --check
python3 .codex/presentation-assetization/scripts/make_handoff_zip.py --root <presentation-assets> --check
npm run test
```

If any check is skipped, write the reason in the handoff.
