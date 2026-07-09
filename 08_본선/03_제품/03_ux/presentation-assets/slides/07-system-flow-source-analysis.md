---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# 07 System Flow Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `assets/source-screenshots/07-system-flow.jpg` |
| Deck audit node-id | `4877:1440` |
| Provided URL candidate | `5053:11964` |
| Pasted working node-id | `6:325` |
| Pasted working screenshot | `assets/pasted-working-screenshots/07-system-flow-6-325.png` |
| Figma access | `working_source_available_in_h6RkEn7fGbTwZbzuwaHsWi` |

## Message

은행 내부 데이터와 공공/외부 데이터를 `Case` 단위로 연결하고, Agent, RAG, Policy Engine을 통해 금융 업무에 안전하게 활용한다는 아키텍처 설명 슬라이드다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Header | 좌상단 섹션 라벨 + 2줄 메시지 | editable text |
| Left diagram card | 큰 흰색 rounded panel, 6단 시스템 플로우 | componentized flowchart |
| Right data table | dark background 위 thin-line table | editable table rows |
| Right tech table | 하단 기술 설명 table | editable table rows |
| Page number | 우하단 `7` | editable text |

## Flowchart Inventory

Top flow stages:

1. `사용자 신호`
2. `반입 / 보안`
3. `Case Hub`
4. `AI 업무지원`
5. `사람승인`
6. `통계 실행`

Important nodes:

- `RM·감독자·관리자`
- `내부 금융 신호`
- `외부·공공신호`
- `반입 게이트`
- `토큰화·DLP`
- `은행 보안 경계`
- `Zero-PII Case Hub`
- `오케스트레이터`
- `근거 패킷`
- `탐지 분류`, `판단·평가`, `행동 초안`, `준법 검증`
- `모델·도구 레이어`
- `Approval Gate`
- `정책·책무 통제`
- `반려·재검토 루프`
- `승인 후 실행`, `고객·업무 시스템`, `폴백`

Bottom entities:

- `Case`
- `AgentRun`
- `Agent`
- `Skill`
- `Evidence`
- `Approval`
- `Audit`

## Table Inventory

Data table rows in pasted Figma source `6:326`:

- `은행 내부 데이터`: CRM, 여신, 상담이력, 사후관리 기록, FDS, 문서 관리 시스템
- `공공·외부 데이터`: 한국은행 ECOS, 공공데이터포털, 국토부 실거래가, HUG 전세보증, 금융위·금감원 경보, 지역 뉴스
- `감사 데이터`: 데이터 접근, 모델 실행, Agent 판단, 사람 승인·반려 이력

Technology rows:

- `CaseOps Engine`
- `Bank Data Connector`
- `Evidence Graph RAG`
- `Agent / Skill / Model Router`
- `Policy Engine`
- `Human Gate`
- `PII 비반출 모델 라우팅`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `25:2` |
| 위치 | `x=30388`, `y=1220`, `1920x1080` |
| Source mapping | `6:325 -> 25:2`, 주요 하위 레이어는 role naming과 `jbyond` metadata로 연결 |
| Source screenshot | `assets/rebuild-screenshots/07-system-flow-source-6-325.png` |
| Rebuild screenshot | `assets/rebuild-screenshots/07-system-flow-structured-25-2.png` |
| Pixel diff | `512 / 2,073,600` changed pixels, similarity `0.9997530864` |
| QA status | `pass_above_98_percent` |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `68:508` |
| Rebuild name | `S07/SystemFlow/Componentized Rebuild v1.0` |
| Source baseline | pasted source `6:325`; structured baseline `25:2` |
| Component sets | `JByond/Deck/SystemFlowTableExact/VariantSet` `66:560`; `JByond/Deck/EntityPillExact/VariantSet` `66:610` |
| Instance count | `9` total: 2 right-side tables + 7 entity pills |
| Rebuild screenshot | `assets/rebuild-screenshots/07-system-flow-componentized-68-508.png` |
| Component evidence | `assets/components/system-flow-table-exact-variant-set-66-560.png`; `assets/components/entity-pill-exact-variant-set-66-610.png` |
| Pixel diff | `980 / 2,073,600` changed pixels, similarity `0.9995273920` |
| QA record | `qa/visual-diff/07-system-flow-componentized-v1.0.json` |
| QA status | `pass_above_99_percent_componentized` |

Componentized v1.0 replaces the two right-side table groups and seven bottom entity pills with exact component instances. The main 6-stage flow columns, flow nodes, and connectors remain cloned source layers for now because connector endpoints are sensitive and should be promoted in a separate loop.

## Pasted Source Layer Inventory

| Source node | Structured node | Role name | Notes |
|---|---|---|---|
| `6:326` | `25:3` | `S07/SystemFlow/Tables` | right-side data and technology tables |
| `6:327` | `25:4` | `S07/SystemFlow/Tables/DataSources/Table` | source/data usage table |
| `6:345` | `25:22` | `S07/SystemFlow/Tables/Technology/Table` | technology table |
| `6:379` | `25:56` | `S07/SystemFlow/Header` | section label and headline |
| `6:382` | `25:59` | `S07/SystemFlow/Diagram/Panel` | white system-flow panel |
| `6:383` | `25:60` | `S07/SystemFlow/Diagram/Text/Title` | diagram title |
| `6:384` | `25:61` | `S07/SystemFlow/Diagram/FlowGroup` | main 6-stage flowchart |
| `6:538` | `25:215` | `S07/SystemFlow/Diagram/EntityRail` | bottom entity rail |
| `6:589` | `25:266` | `S07/SystemFlow/Diagram/Legend/SecurityRisk` | 개인정보 / 보안 / 환각 예방 legend |

## Component Model

- `JByond/Deck/SystemFlowPanel`
- `JByond/Deck/FlowStageHeader`
- `JByond/Deck/FlowNode`
- `JByond/Deck/FlowConnector`
- `JByond/Deck/EntityPill`
- `JByond/Deck/EntityPillExact/VariantSet` (`66:610`, promoted v1.0 exact geometry)
- `JByond/Deck/DarkTable`
- `JByond/Deck/SystemFlowTableExact/VariantSet` (`66:560`, promoted v1.0 exact geometry)
- `JByond/Deck/TableRow`

## Rebuild Notes

- 이 슬라이드는 모든 요소를 editable text/vector로 복제해야 한다. 단일 이미지로 쓰면 pilot 목적을 충족하지 못한다.
- 왼쪽 diagram은 먼저 stage grid를 만든 뒤 node를 배치한다. absolute coordinates만 쓰면 텍스트 수정 시 쉽게 무너진다.
- 오른쪽 table은 Figma table component 또는 auto-layout row stack으로 만든다.
- `[제휴 TBD]` 문구는 원본 보존 항목으로 남기되, 최종 발표용 재사용본에서는 검토 플래그를 달아야 한다.

## QA Risks

- 가장 작은 텍스트가 많아 line-height clipping 위험이 크다.
- Flow connector가 도형 뒤에 깔리거나 서로 겹칠 수 있다.
- 오른쪽 표의 dotted divider와 opacity 차이가 원본 품질을 좌우한다.
- pasted Figma source의 6번째 flow stage는 `통계 실행`으로 표시된다. 재사용본에서는 `통제 실행`이 의도였는지 검토해야 한다.
- `정책·책무 통제`는 source에서 그대로 보존한다.
- `07` structured rebuild v1은 98% 기준을 통과했지만 오른쪽 표 영역에 512 pixel render delta가 남아 zero-diff polish 후보로 기록한다.
