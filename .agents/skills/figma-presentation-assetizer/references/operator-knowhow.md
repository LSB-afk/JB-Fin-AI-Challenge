# Operator Know-How

Use this reference when the user asks how to reuse the process, when quality drifts, or when another AI needs the practical lessons behind the package.

## Canonical Documents

When the repo-local pack is available, read:

- `.codex/presentation-assetization/references/operator-knowhow.md`
- `.codex/presentation-assetization/references/reuse-playbook.md`

Those files contain the full field guide and reuse checklist. This file keeps the essential behavior close to the discoverable skill.

## Essential Rules

| Pressure | Correct behavior |
|---|---|
| "Prompt만으로 똑같이" | Say this is not proven; require assets, tokens, source analysis, components, and QA |
| "여러 agent가 Figma에 쓰기" | Refuse parallel Figma writes; A5 is the only writer |
| "원본 보면서 blind rebuild" | Do not inspect source/final during build; compare only in QA |
| Missing fonts | Preserve source text or record risk; do not silently substitute |
| "스크린샷 깔고 끝" | Reject full-slide flatten as assetization failure |

## Practical Defaults

- Use final PDF to confirm slide order.
- Work only in an editable duplicate or new Figma file.
- Calibrate on one slide before scaling.
- Preserve original images when fidelity matters.
- Promote one component family at a time.
- Prefer exact-geometry variants for dense or pixel-critical decks.
- Record node IDs, screenshots, QA status, prompts, and residual risk during the run.

## Proof Language

Do not overclaim. Use these levels:

| Wording | Meaning |
|---|---|
| "source analyzed" | source-analysis/assets/tokens exist |
| "source-preserving rebuild" | editable clone or structured rebuild has QA evidence |
| "componentized rebuild" | component usage and post-promotion QA exist |
| "AI-reusable" | blind rebuild from package materials has passed QA |
| "prompt-only reproducible" | not proven unless multiple blind rebuilds pass without hidden source access |
