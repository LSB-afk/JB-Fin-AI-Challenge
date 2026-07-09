---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 04 Solution Overview Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/04 솔루션 개요.jpg` |
| Deck audit node-id | `4815:12466` |
| Pasted working node-id | `6:210` |
| Structured rebuild node-id | `28:108` |
| QA reference | `qa/visual-diff/04-solution-structured-v1.json` |
| Figma access | `metadata_partial_ok` |

## Message

JByond는 금융 업무를 `계열사 x 역할 x 케이스` 구조로 재구성하고, AI Agent가 근거와 위험 신호를 정리한 뒤 사람이 최종 판단과 고객 감각에 집중하게 한다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Left header | `Solution Overview` + 설명문 | editable text |
| Structure table | 기관/역할/케이스 3열 예시 | editable table/card pattern |
| Flow rail | 기관 -> 역할 -> 케이스 -> AI Agent 정리 -> 담당자 확인 -> 다음 역할 전달 | `SolutionAxisFlow` |
| Keyboard control note | `키보드 기반 화면 제어` block | editable info panel |
| Right product shot | large console screenshot | raster allowed as product UI screenshot |

## Text Inventory

- `Solution Overview`
- `본 솔루션은 금융 업무를 계열사 x 역할 x 케이스 구조로 재구성한다. AI Agent가 근거와 위험 신호를 먼저 정리하고, 사람은 최종 판단과 고객 감각에 집중합니다.`
- `계열사 x 역할 x 케이스 구조`
- Institution examples: `전북은행`, `JB 우리캐피탈`
- Role examples: `여신`, `전세 담당`, `이상거래 담당`
- Case examples: `대출 상담, 사후 관리`, `전세사기 위험 검토`, `보이스피싱, 이상거래 탐지`
- Flow: `기관`, `역할`, `케이스`, `AI Agent 정리`, `담당자 확인`, `다음 역할 전달`
- `키보드 기반 화면 제어`
- `Enter 목적은 사용자의 감각을 불필요한 탐색과 조작에 쓰지 않게 하고, 사람이 더 잘해야 하는 감각 중심 판단에 집중시키는 것이다...`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:211`-`6:213` | header and message | left text stack |
| `6:214` | structure table group | institution/role/case examples |
| `6:257` | keyboard control note | title + body paragraph |
| `6:240`-`6:256` | flow rail | text nodes and polygon arrows |
| `6:260` | product screenshot | image fills `6e735ee...`, `145c4d...`, `1213x935`, scale `CROP` |

Observed Figma summary: `24` text nodes, `1` image fill node, `2` polygon arrow nodes, dominant fonts `Pretendard Regular`, `SemiBold`, `Medium`, `Bold`.

## Component Model

- `JByond/Deck/SolutionAxisFlow`
- `JByond/Deck/StructureTable`
- `JByond/Deck/UICalloutPanel`
- `JByond/Deck/KeyboardControlNote`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:108` |
| Source mapping | `6:210 -> 28:108` |
| QA | `10` changed pixels, similarity `0.9999951775` |
| Scope status | structured baseline preserved; componentized baseline accepted as `54:150` |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `54:150` |
| Source mapping | `6:210 -> 28:108 -> 54:150` |
| Component sets | `SolutionAxisColumnExact=53:174`, `SolutionFlowStepExact=53:184` |
| QA | `71` changed pixels, similarity `0.9999657600` |
| Screenshot | `assets/rebuild-screenshots/04-solution-componentized-54-150.png` |
| Visual diff | `qa/visual-diff/04-solution-componentized-v1.0.json` |

Promoted exact-geometry components:

- `JByond/Deck/SolutionAxisColumnExact/VariantSet` (`53:174`): `기관`, `역할`, `케이스` columns from structured nodes `28:116`, `28:123`, `28:130`
- `JByond/Deck/SolutionFlowStepExact/VariantSet` (`53:184`): `AI Agent 정리`, `담당자 확인`, `다음 역할 전달` pills from structured nodes `28:147`, `28:149`, `28:151`

## QA Risks

- Right screenshot is raster-allowed but must be ledgered with image hash/source node.
- Flow rail is small; arrow alignment and label baseline are the main visual risks.
- `Enter` narrative has product-demonstration implications and should stay tied to the demo behavior.
