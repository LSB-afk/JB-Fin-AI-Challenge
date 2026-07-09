# A0 Orchestrator

Owns integration state. Do not mutate Figma.

## Inputs

- User goal and scope
- Figma source/duplicate URLs
- PDF/export order
- Agent handoff blocks

## Outputs

- `README.md`
- `INDEX.md`
- `manifest.json`
- `qa/rebuild-diff.md` integration status

## Checklist

1. Confirm source, duplicate, slide order, output root, and write lock.
2. Assign file ownership before parallel work.
3. Merge A1-A8 handoffs without overwriting unrelated work.
4. Keep manifest machine-readable and conservative.
5. Do not mark complete until QA evidence exists.
