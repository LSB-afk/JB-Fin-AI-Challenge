---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 08 AI Org Chart Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/08 데이터 및 활용 기술.jpg` |
| Deck audit node-id | `4939:2710` |
| Pasted working node-id | `6:592` |
| Structured rebuild node-id | `28:211` |
| QA reference | `qa/visual-diff/08-ai-org-structured-v1.json` |
| Figma access | `metadata_ok_large` |

## Message

사람의 판단을 중심에 두고, 위험 신호·근거 탐색·금융 검토·준법·고객 안내·감사 운영을 여러 AI 업무지원 기능/에이전트로 배정하는 조직도형 슬라이드다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Header | `[AI 업무 지원 조직도]` + headline | editable text |
| Main org chart | 다수의 기능 카드와 connector arrow | `OrgRoleNode` + `OrgConnector` |
| Approval owner nodes | RM/준법 최종 승인자 카드 | `HumanGateNode` |
| Operation agents | 우하단 운영 에이전트 3종 | `OpsAgentCard` |
| Background shapes | split dark/white stage and large masked panels | tokenized shapes |

## Key Nodes

- `관리 건 운영 기능`
- `주의 신호 분류`
- `정책금융 후보 검토`
- `근거 수집`
- `서류 체크리스트`
- `사기 유의 신호 확인`
- `준법 검토`
- `전세위험 관리 리드`
- `전세가율 확인 기능`
- `등기상 유의 신호 확인 기능`
- `임차인 자산노출 검토 기능`
- `은행 상담 연결 지원 기능`
- `RM 최종 승인자`
- `준법 최종 승인자`
- `Cost Sentinel · 원가 파수꾼`
- `119 · 사고 승격`
- `Ledger Curator · 감사 원장`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:948` | header group | section label and headline |
| `6:676`-`6:857` | left/middle function cards | repeated cards with title, body, category chip, risk/status chip |
| `6:596`-`6:645` | right housing-risk function cards | repeated cards with larger status chips |
| `6:898`, `6:915`, `6:927` | upper human/coordination nodes | approval and coordination cards |
| `6:939`-`6:946` | connectors | vector arrows/lines |
| `6:954`-`6:982` | operation agents | three compact op-cards |

## Component Model

- `JByond/Deck/OrgRoleNode`
- `JByond/Deck/OrgStatusChip`
- `JByond/Deck/OrgConnector`
- `JByond/Deck/HumanGateNode`
- `JByond/Deck/OpsAgentCard`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:211` |
| Source mapping | `6:592 -> 28:211` |
| QA | `1` changed pixel, similarity `0.9999995177` |
| Scope status | root-structured clone; org-card component promotion completed in v1.0 |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `61:176` |
| Source mapping | `6:592 -> 28:211 -> 61:176` |
| Component sets | compact role cards `60:372`; tall role cards `60:505`; gate cards `60:550` |
| Instance count | `29` org/gate card instances |
| QA | `177` changed pixels, similarity `0.9999146412` |
| Visual diff | `qa/visual-diff/08-ai-org-componentized-v1.0.json` |
| Screenshot | `assets/rebuild-screenshots/08-ai-org-componentized-61-176.png` |

Remaining: connector arrows and bottom-right `운영 에이전트 3종` panel remain cloned source layers. Promote them only after verifying endpoint/spacing drift stays below the current 177-pixel delta.

## QA Risks

- This slide has a very large number of repeated cards; component promotion must be incremental.
- Small chips and connector arrows are the most likely source of visual drift.
- Some card texts are operationally sensitive and should remain source-preserved until product wording is reviewed.
