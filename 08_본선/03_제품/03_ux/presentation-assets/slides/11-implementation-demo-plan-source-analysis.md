---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 11 Implementation Demo Plan Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/11 실제 구현 흐름 및 시연 계획.jpg` |
| Deck audit node-id | `4960:1054` |
| Pasted working node-id | `6:1108` |
| Structured rebuild node-id | `29:104` |
| QA reference | `qa/visual-diff/11-demo-plan-structured-v1.json` |
| Figma access | `metadata_ok` |

## Message

본선 시연은 AI가 어디까지 근거를 정리하고, 사람이 어디서 판단하며, 승인과 감사 기록이 어떻게 남는지를 보여주는 데 초점을 둔다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | deep navy scenario background | image/gradient stage |
| Header | centered pill `본선 구현 결과 / 시연 계획` + headline paragraph | editable text |
| Left column | `완료된 MVP` checklist | `MvpChecklist` |
| Right column | `시연 계획` step pairs | `DemoPlanStep` row pair |

## Text Inventory

Completed MVP:

- `Case 관리 - 신규 위험 케이스를 목록으로 확인하고, 우선순위에 따라 검토할 수 있음`
- `AI Agent 근거 정리 - 고객 정보, 매출 흐름, 정책금융 가능성, 준법 체크 포인트를 Agent가 정리`
- `승인 구조 - 고객 대상 조치는 담당자의 승인 이후에만 실행되는 구조 설계`
- `Audit Log - 판단, 승인, 실행 기록이 남아 사후 검토와 내부 통제에 활용 가능`

Demo plan:

- `RM이 신규 위험 케이스 확인` -> `Case가 업무 단위로 들어오고 우선순위가 보임`
- `AI Agent 실행` -> `여러 Agent가 고객 · 매출 · 서류 · 준법 근거를 정리`
- `근거 패키지 확인` -> `사람이 AI 결과를 검토하는 구조`
- `준법 승인` -> `최종 판단은 RM이 수행`
- `Audit Log 확인` -> `누가, 언제, 어떤 근거로 판단했는지 기록되는 구조`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:1109` | background image/gradient | full-slide background |
| `6:1110` | header group | pill and large paragraph |
| `6:1115`-`6:1123` | MVP checklist | four rows |
| `6:1124`-`6:1154` | demo plan | five row pairs |

## Component Model

- `JByond/Deck/MvpChecklist`
- `JByond/Deck/MvpChecklistRow`
- `JByond/Deck/DemoPlanStep`
- `JByond/Deck/TwoColumnPlan`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `29:104` |
| Source mapping | `6:1108 -> 29:104` |
| QA | `356` changed pixels, similarity `0.9998283179` |
| Scope status | structured baseline preserved; checklist/demo-plan componentized baseline accepted as `74:649` |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `74:649` |
| Rebuild name | `S11/ImplementationDemoPlan/Componentized Rebuild v1.0` |
| Source baseline | pasted source `6:1108`; structured baseline `29:104` |
| Component sets | `JByond/Deck/MvpChecklistRowExact/VariantSet` `72:661`; `JByond/Deck/DemoPlanRowExact/VariantSet` `72:697` |
| Instance count | `9` total: 4 MVP checklist rows, 5 demo-plan row pairs |
| Rebuild screenshot | `assets/rebuild-screenshots/11-demo-plan-componentized-74-649.png` |
| Component evidence | `assets/components/mvp-checklist-row-exact-variant-set-72-661.png`; `assets/components/demo-plan-row-exact-variant-set-72-697.png` |
| Pixel diff | `182 / 2,073,600` changed pixels, similarity `0.9999122299` |
| QA record | `qa/visual-diff/11-demo-plan-componentized-v1.0.json` |
| QA status | `pass_above_99_99_percent_componentized` |

Componentized v1.0 replaces the four completed-MVP checklist rows and five demo-plan row pairs with exact component instances. Background, header badge, headline paragraph, and column titles remain cloned source layers. The header paragraph should remain cloned until Pretendard is available in the Figma runtime because the line breaks are presentation-critical.

## QA Risks

- Header paragraph is wide and can reflow if font availability changes.
- MVP/demonstration wording should stay synchronized with actual app capability and demo route.
