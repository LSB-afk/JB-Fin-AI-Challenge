# Figma Write Lock

## Rule

Only A5 mutates Figma. Everyone else is read-only.

## Before Any Figma Write

1. Load `figma-use`.
2. Confirm target is an editable duplicate/workspace, not the original.
3. Confirm the mode: source-preserving, componentized, blind, or derivative.
4. Confirm the frame/page name to create.
5. Return created or mutated node IDs.

## Forbidden

- Mutating the original source file.
- Overwriting source, baseline, or accepted final frames.
- Creating a full-slide image as the rebuild.
- Running parallel Figma write agents.
- Retyping large text blocks while required fonts are missing.

## Font Policy

If a required font is unavailable in Figma runtime:

- preserve source text layers when possible
- clone instead of retyping
- record font risk in tokens and QA
