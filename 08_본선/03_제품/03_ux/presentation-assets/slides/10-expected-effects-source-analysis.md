---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 10 Expected Effects Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/10 기대효과.jpg` |
| Deck audit node-id | `4852:1918` |
| Pasted working node-id | `6:96` |
| Structured rebuild node-id | `29:2` |
| QA reference | `qa/visual-diff/10-effects-structured-v1.json` |
| Figma access | `metadata_ok` |

## Message

JByond는 단일 앱이 아니라 Case 처리 경험을 중심으로 UX, EX, CX를 연결하는 JB금융형 AX 전략이며, 직원·그룹·고객 관점의 가치 사슬을 만든다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Left header | 기대효과 headline and explanation | editable text |
| Left value chain | 직원/그룹/고객 가치 문장 | `ValueChainPanel` |
| Right TX/AX map | TX, AX, UX, EX/PX, CX hierarchy diagram | `ExperienceMap` |
| Bottom left notes | partner/logo-like pills and supporting elements | material tokens |
| Page number | `10` | editable text |

## Text Inventory

- `기대효과 및 향후 확장성`
- `JByond는 단일 앱이 아니라, Case 처리 경험을 중심으로 UX, EX, CX를 연결하는 JB금융형 AX 전략이다.`
- `JB금융그룹이 얻게 될 3관점 가치 사슬 ( 직원 · 그룹 · 고객 )`
- `직원 - RM 1인당 연 약 66시간 업무 여력 확보 (시나리오 기준)`
- `그룹 - 초기 구축비 3억 원을 가정, 3년 NPV 24.2억 원, ROI 471%, 투자금 회수기간 5.4개월...`
- `고객 - 연구의 운영 시뮬레이션에서는 평균 대기시간이 28.1분에서 3.7분으로 약 87% 감소...`
- Experience map labels: `TX`, `AX`, `UX`, `EX/PX`, `CX`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:183` | header group | section title and main sentence |
| `6:193` | value chain panel | dense text box |
| `6:98` | experience map group | nested TX/AX/UX/EX/PX/CX nodes and connectors |
| `6:186` | bottom-left material group | pill/logo-like elements |
| `6:174`-`6:180` | experience map connectors | vector arrows |

## Component Model

- `JByond/Deck/ExperienceMap`
- `JByond/Deck/ExperienceNode`
- `JByond/Deck/MetricBlock`
- `JByond/Deck/ValueChainPanel`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `29:2` |
| Source mapping | `6:96 -> 29:2` |
| QA | `617` changed pixels, similarity `0.9997024498` |
| Scope status | structured baseline preserved; experience-node componentized baseline accepted as `70:660`; metric/evidence panel remains a separate follow-up |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `70:660` |
| Rebuild name | `S10/ExpectedEffects/Componentized Rebuild v1.0` |
| Source baseline | pasted source `6:96`; structured baseline `29:2` |
| Component set | `JByond/Deck/ExperienceNodeExact/VariantSet` `70:659` |
| Instance count | `5` total: `TX`, `AX`, `UX`, `EX-PX`, `CX` |
| Rebuild screenshot | `assets/rebuild-screenshots/10-effects-componentized-70-660.png` |
| Component evidence | `assets/components/experience-node-exact-variant-set-70-659.png` |
| Pixel diff | `2,627 / 2,073,600` changed pixels, similarity `0.9987331211` |
| QA record | `qa/visual-diff/10-effects-componentized-v1.0.json` |
| QA status | `pass_above_98_percent_componentized` |

Componentized v1.0 replaces the five experience map nodes with exact component instances. The arrows, left headline, bottom-left logo material group, and dense value-chain panel remain cloned source layers. The value-chain panel should be promoted only after a separate drift check because its dense multiline text is easy to clip or reflow.

## QA Risks

- ROI/NPV/time-saved values are scenario assumptions. Do not reuse as external fact without caveat.
- `AI Trasformaion` spelling appears in source metadata; derivative decks should decide whether to correct to `Transformation`.
- Small dense value-chain body can clip after typography changes.
