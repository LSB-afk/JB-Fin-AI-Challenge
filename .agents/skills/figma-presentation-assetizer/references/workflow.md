# Workflow Reference

## Source-Preserving Rebuild

1. Confirm source file, editable duplicate, slide order, output folder, and write lock.
2. Capture source screenshots at `1920x1080`.
3. Clone source frames without redrawing.
4. Add role-based names and metadata to the clone.
5. Export rebuild screenshots and run visual diff.
6. Record source/rebuild node IDs and QA result.

## Component Promotion

1. Start only after source-preserving QA passes.
2. Promote one repeated family at a time.
3. Prefer exact-geometry components when fonts or dense text make reflow risky.
4. Replace source layers with component instances in a new candidate frame.
5. Rerun full-slide QA before accepting.

## Blind Rebuild

Build without inspecting or cloning source/final frames. Use only:

- `deck-definition.md`
- `INDEX.md`
- `manifest.json` for identity and QA references
- target `slides/*-source-analysis.md`
- `tokens/*`
- `components/component-catalog.md`
- `assets/asset-ledger.md`
- `process/rebuild-prompts.md`

Compare against accepted final only after build.

## Handoff Packaging

Required handoff docs:

- `handoff/README.md`
- `handoff/team-quickstart.md`
- `handoff/ai-reuse-runbook.md`
- `handoff/figma-usage-guide.md`
- `handoff/share-checklist.md`

Create a zip excluding `.DS_Store` and verify it with `unzip -t`.
