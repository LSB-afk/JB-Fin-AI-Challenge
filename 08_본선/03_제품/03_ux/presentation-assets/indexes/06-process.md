---
tags:
  - area/product
  - type/index
  - status/active
date: 2026-07-09
up: "[[Presentation Assets Index]]"
---

# Process Index

이 색인은 AI build 과정, prompt, Figma build ledger, 병렬 에이전트 운영 문서를 정리한다.

## Process Documents

| 문서 | 역할 |
|---|---|
| [`../process/ai-build-log.md`](../process/ai-build-log.md) | 날짜별 작업, decision, input/output, known issue 기록 |
| [`../process/rebuild-prompts.md`](../process/rebuild-prompts.md) | A5 Builder/A6 QA prompt와 slide별 componentized rebuild prompt |
| [`../process/parallel-agent-operating-model.md`](../process/parallel-agent-operating-model.md) | A0-A8 병렬 에이전트 역할, wave, ownership, handoff |
| [`../process/figma-build-ledger.json`](../process/figma-build-ledger.json) | Figma build 작업의 machine-readable ledger |

## Recommended Process Reading

| 상황 | 읽는 순서 |
|---|---|
| 이 작업이 어떻게 진행됐는지 회고 | `ai-build-log.md` -> `rebuild-prompts.md` |
| 후속 AI 에이전트를 돌릴 때 | `parallel-agent-operating-model.md` -> `rebuild-prompts.md` -> `figma-build-ledger.json` |
| Figma에 새 rebuild를 만들 때 | `deck-definition.md` -> `manifest.json` -> `rebuild-prompts.md` -> slide source-analysis -> token files |
| 실패 원인 분석 | `ai-build-log.md` -> `qa/rebuild-diff.md` -> relevant `qa/visual-diff/*.json` |

## Open Process Gap

`deck-definition.md`에서 별도 필요 문서로 지정한 다음 항목은 아직 생성되지 않았다.

| 문서 | 목적 |
|---|---|
| `blind-rebuild-runbook.md` | 원본 frame 없이 문서/토큰/자산만으로 재생성하는 절차 |
| `blind-rebuild-eval.md` | blind rebuild 결과와 diff/failure log |
| `layout-grammar.json` | zone, grid, anchor, z-order를 기계적으로 읽는 schema |
| `font-install-runbook.md` | Panchang/Pretendard 설치/enable 절차 |
| `component-maturity-matrix.md` | Exact/Flexible/One-off component 성숙도 판단 |
| `copy-system.md` | headline, eyebrow, caption, label 문체 규칙 |
| `export-package-checklist.md` | Figma final page -> PDF/PPT export 검수 |
