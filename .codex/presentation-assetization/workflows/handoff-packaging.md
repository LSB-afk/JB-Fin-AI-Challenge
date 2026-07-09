# Handoff Packaging Workflow

Use when a deck assetization package is ready to share with teammates.

## Required Documents

- `README.md`
- `INDEX.md`
- `deck-definition.md`
- `manifest.json`
- `handoff/README.md`
- `handoff/team-quickstart.md`
- `handoff/ai-reuse-runbook.md`
- `handoff/figma-usage-guide.md`
- `handoff/share-checklist.md`

## Steps

1. Update `INDEX.md` and category indexes.
2. Ensure manifest links `documentIndex`, `categoryIndexes`, `deckDefinition`, and `handoffPackage`.
3. Run package validator.
4. Create shareable zip, excluding `.DS_Store` and local temp files.
5. Verify zip with `unzip -t`.
6. Record archive path in handoff README and manifest.

## Share Message Shape

Tell teammates:

1. Open Figma final page first.
2. Read `handoff/team-quickstart.md`.
3. Read `deck-definition.md` for design philosophy.
4. Use `handoff/ai-reuse-runbook.md` for AI rebuild/derivative work.
5. Run QA before claiming reuse success.
