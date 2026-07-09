# Agent Model Reference

Use A0-A8 roles for deck assetization.

| Agent | Role | Writes |
|---|---|---|
| A0 | Orchestrator | README, INDEX, manifest, integrated QA |
| A1 | Figma Reverse Engineer | slides analysis, source screenshots |
| A2 | Token Cartographer | tokens |
| A3 | Component Architect | components |
| A4 | Asset Harvester | assets and ledger |
| A5 | Figma Slide Builder | Figma only |
| A6 | Visual QA Judge | QA reports and diff records |
| A7 | AI Process Librarian | prompts and build logs |
| A8 | Evidence Recorder | append-only evidence |

## Handoff Format

Each agent returns:

1. Task
2. Inputs
3. Output
4. Assumptions
5. Open risks
6. Next action

## Conflict Prevention

- A5 is the only Figma writer.
- A0 owns manifest updates.
- Other agents propose manifest changes through handoff blocks.
- Parallel agents write separate owned files only.
