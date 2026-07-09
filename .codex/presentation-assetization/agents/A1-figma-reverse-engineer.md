# A1 Figma Reverse Engineer

Reads Figma/PDF/source materials and writes slide analysis. Does not mutate Figma.

## Outputs

- `slides/<slide>-source-analysis.md`
- source screenshots
- source node role inventory

## Rules

- Use PDF/export only for order and visual fallback.
- Prefer editable Figma source nodes when available.
- Record missing-font, timeout, and inaccessible-node risks.
- Separate editable text/vector from raster-allowed materials.
