# Source-Preserving Rebuild Workflow

Use when the goal is high-fidelity reverse engineering of an existing Figma presentation deck.

## Preconditions

- Original Figma file is preserved.
- Editable duplicate or working file is available.
- Slide order is confirmed from PDF/export or user-provided ordering.
- Output folder has `manifest.json`, `slides/`, `tokens/`, `assets/`, `components/`, `qa/`, and `process/`.
- Figma write lock is assigned to A5 only.

## Steps

1. Map source slide IDs to final order.
2. Capture source screenshots at `1920x1080`.
3. Clone source frames without redrawing or flattening.
4. Rename root and child layers by role.
5. Preserve original text/font metadata unless fonts are confirmed available.
6. Record source/rebuild node IDs in manifest.
7. Export rebuild screenshots.
8. Run visual QA.

## Acceptance Gate

| Check | Required |
|---|---|
| Size | `1920x1080` |
| Structure | no newly introduced full-slide flatten image |
| Fidelity | similarity `>= 0.98` |
| Text | no visible clipping |
| Evidence | source/rebuild screenshots and QA JSON recorded |

## Common Failures

| Failure | Correction |
|---|---|
| Placeholder rebuild looks unlike source | Stop redrawing; clone source layers and structure the clone |
| Figma font unavailable | Preserve source text node; record font risk |
| Source node too large/timeouts | Use targeted child-node probes, not full subtree reads |
| PDF is flattened | Use PDF only for order and visual reference, not editable source |
