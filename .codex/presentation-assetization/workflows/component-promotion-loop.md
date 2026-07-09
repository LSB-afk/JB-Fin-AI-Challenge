# Component Promotion Loop

Use after a source-preserving rebuild passes visual QA. Componentization must be a controlled refactor, not a redraw.

## Rule

Promote one repeated family at a time, replace only that family with instances, then rerun full-slide visual QA.

## Steps

1. Pick a repeated family: card, table row, callout, entity pill, process node, Gantt tick, task bar.
2. Create an exact-geometry component or variant set from source-preserving clones.
3. Hide or remove only the corresponding original layers in a new componentized frame.
4. Place component instances at exact source coordinates.
5. Export source and rebuild screenshots.
6. Run visual diff.
7. Accept only if visual drift is within gate and component usage is documented.

## Exact vs Flexible

| Type | Use when | Gate |
|---|---|---|
| `Exact` | pixel fidelity is critical, fonts are missing, dense text might reflow | should match source geometry |
| `Flexible` | future decks need editable variants more than pixel identity | must have separate derivative QA |
| documented one-off | only appears once or connector endpoints are fragile | record why not componentized |

## Rejection Triggers

- Text or arrow geometry shifts visibly.
- Component instance renders with clipped text.
- Similarity drops below the accepted baseline without a documented reason.
- A broad auto-layout component replaces an exact source group before fonts are stable.
