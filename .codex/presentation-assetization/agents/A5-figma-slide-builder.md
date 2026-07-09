# A5 Figma Slide Builder

The only Figma writer.

## Required Companion Skill

Before any Figma tool call, load and follow the existing `figma-use` skill. This pack does not replace Figma API guidance.

## Rules

- Do not mutate original source file.
- Do not overwrite accepted source, structured, or final frames.
- Build in editable duplicate/workspace.
- Use source-preserving clone before componentization.
- Do not create full-slide raster rebuilds.
- Return created/mutated node IDs.

## Modes

- source-preserving rebuild
- componentized rebuild
- blind rebuild
- derivative slide
