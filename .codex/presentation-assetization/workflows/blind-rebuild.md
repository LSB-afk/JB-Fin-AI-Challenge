# Blind Rebuild Workflow

Use to prove that docs, tokens, assets, and components are enough to recreate a slide without inspecting the original frame during build.

## Hard Rule

During build, do not inspect, clone, or use the original source frame or accepted final frame. Use them only after building, for QA comparison.

## Allowed Inputs

- `deck-definition.md`
- `INDEX.md`
- `manifest.json` only for identity and final QA references
- `slides/<slide>-source-analysis.md`
- `tokens/*`
- `components/component-catalog.md`
- `assets/asset-ledger.md`
- `process/rebuild-prompts.md`

## Steps

1. Create a new Figma page: `Blind Rebuild / S## / YYYY-MM-DD`.
2. Create one frame: `S##/<Role>/Blind Rebuild v0.1`.
3. Build from layout zones, tokens, component catalog, and asset ledger.
4. Export screenshot.
5. Compare against accepted final frame only after build.
6. Record missing tokens, missing assets, ambiguous layout grammar, and drift.

## Output Record

Minimum fields:

- new page/frame node ID
- input docs used
- components used
- assets used
- token files used
- visual diff result
- missing documents or schema gaps

## Success Interpretation

A blind rebuild that fails is still valuable if it identifies missing schema, layout grammar, component variants, or asset provenance. Do not hide failure by using the source frame during build.
