---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 12 Closing Expansion Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/12 마무리.jpg` |
| Deck audit node-id | `4939:4127` |
| Pasted working node-id | `6:983` |
| Structured rebuild node-id | `29:151` |
| QA reference | `qa/visual-diff/12-expansion-structured-v1.json` |
| Figma access | `metadata_ok` |

## Message

JByond는 JB의 다음을 잇는 금융 AX 운영체계이며, 업무 로그·AI Agent·Case·API가 늘어날수록 RM 노하우와 조직 자산이 쌓이는 확장 구조를 보여준다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Left closing | `감사합니다.` + JByond definition + closing sentence | editable text |
| Left bubbles | AX/EX/CX circles and benefit captions | `ExperienceBenefitBubble` |
| Right orbit/ladder | expanding AX operating system diagram | `ExpansionOrbit` |
| Center mini list | `더 많은 업무 로그`, `더 많은 AI Agent`, `더 많은 Case`, `더 많은 API` | editable list |
| Bottom badge | `Local Guard OS - JByond` | editable badge |

## Text Inventory

- `감사합니다.`
- `JByond — JB의 다음(beyond)을 잇는(bond) 금융 AX 운영체계`
- `JByond는 JB금융이 AX 전환 기반을 갖춘 상태로 나아가게 할 것입니다`
- `AX < 기업 >` / `생산성 향상, 포용금융 강화, 소비자보호 강화`
- `EX < 직원 >` / `검색·문서정리 업무 감소, RM의 판단 집중, 관계형 영업 시간 확보`
- `CX < 고객 >` / `더 빠른 답변, 더 이해되는 설명, 더 안전한 금융`
- `JB 금융 AX 운영체계로 확장`
- `계열사 전반의 AX 업무 표준화`
- `JB금융형 AI Agent 업무 인프라 구축`
- `업무 로그 기반 Agent 스킬 고도화`
- `RM 노하우의 조직 자산화`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:1015` | closing title | left top |
| `6:1017` | definition + closing sentence | left body |
| `6:1020`-`6:1031` | AX/EX/CX benefit bubbles | three circles and captions |
| `6:1009` | growth input list | central list |
| `6:1032` | AX operating expansion diagram | right grouped diagram |
| `6:984`-`6:1007` | large vector orbit shapes | visual expansion motif |

## Component Model

- `JByond/Deck/ClosingStatement`
- `JByond/Deck/ExperienceBenefitBubble`
- `JByond/Deck/ExpansionOrbit`
- `JByond/Deck/ExpansionStep`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `29:151` |
| Source mapping | `6:983 -> 29:151` |
| QA | `2` changed pixels, similarity `0.9999990355` |
| Scope status | root-structured clone; vector orbit/token promotion pending |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `77:678` |
| Component sets | `75:690` `JByond/Deck/ExperienceBenefitBubbleExact/VariantSet`; `75:703` `JByond/Deck/ExpansionStepExact/VariantSet` |
| Replaced source units | AX/EX/CX benefit bubbles `29:188`, `29:191`, `29:194`; expansion steps `29:204`, `29:206`, `29:208`, `29:210` |
| Instance count | `7` component instances |
| Screenshot | `assets/rebuild-screenshots/12-expansion-componentized-77-678.png` |
| Component evidence | `assets/components/experience-benefit-bubble-exact-variant-set-75-690.png`; `assets/components/expansion-step-exact-variant-set-75-703.png` |
| QA | `95` changed pixels, similarity `0.9999541860`; see `qa/visual-diff/12-expansion-componentized-v1.0.json` |
| Scope status | benefit bubbles and step labels componentized; large orbit vectors and closing text remain cloned source layers |

## QA Risks

- Many large decorative vectors overlap; component promotion should preserve z-order.
- The `today` marker is date-sensitive in derivative decks.
