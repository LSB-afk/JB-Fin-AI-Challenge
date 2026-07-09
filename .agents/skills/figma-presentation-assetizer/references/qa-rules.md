# QA Rules

## Slide Gate

- frame size `1920x1080`
- no full-slide flattened rebuild image
- no visible text clipping
- no incoherent overlap
- visual similarity `>= 0.98` unless exception is documented

## Token Gate

Core color, typography, spacing, surface, effect, and component rules should map to token files when available.

## Component Gate

Repeated elements need one of:

- Figma component instance
- documented reusable pattern
- documented one-off exception

## Asset Gate

Every raster asset records:

- source slide
- source node or origin
- use slide
- path
- raster policy
- crop/hash when available

## QA Output

Record:

- source and rebuild node IDs
- screenshot paths
- changed pixels and similarity when available
- drift region or reason
- pass/fail decision
