---
tags:
  - area/product
  - type/handoff
  - status/active
date: 2026-07-09
up: "[[JByond Presentation Assetization Handoff]]"
---

# Figma Usage Guide

이 문서는 팀원이 Figma 작업 파일에서 무엇을 보고, 무엇을 건드리면 안 되는지 정리한다.

## Figma File

Working Figma file:

`https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`

최종 발표덱 검토 페이지:

`99 Final Componentized Deck`

## Page Meaning

| Page / Area | 의미 | 주의 |
|---|---|---|
| `Page 1` | 사용자가 붙여 넣은 원본 working source frames와 작업 중간 산출물이 있음 | 원본 source frame을 덮어쓰지 않는다 |
| `99 Final Componentized Deck` | 최종 14장 componentized rebuild frame | 팀 공유/검토의 기본 위치 |
| Component sets | `JByond/Deck/*` component family | 수정 전 QA 영향 범위를 확인한다 |

## Final Frame Map

| Slide | Frame node | Frame name |
|---:|---|---|
| 01 | `93:1179` | `S01/Summary/Final Componentized` |
| 02 | `49:76` | `S02/Problem Definition/Final Componentized` |
| 03 | `58:183` | `S03/Fragmentation/Final Componentized` |
| 04 | `54:150` | `S04/Solution Overview/Final Componentized` |
| 05 | `98:1189` | `S05/Key Feature UI/Final Componentized` |
| 06 | `101:1206` | `S06/Key Feature Approval/Final Componentized` |
| 07 | `68:508` | `S07/System Flow/Final Componentized` |
| 08 | `61:176` | `S08/AI Loop/Final Componentized` |
| 09 | `64:490` | `S09/User Scenario/Final Componentized` |
| 10 | `70:660` | `S10/Business Model/Final Componentized` |
| 11 | `74:649` | `S11/Roadmap/Final Componentized` |
| 12 | `77:678` | `S12/Competition Strategy/Final Componentized` |
| 13 | `80:688` | `S13/Impact/Final Componentized` |
| 14 | `90:777` | `S14/Closing/Final Componentized` |

## Safe Workflow

1. 새 작업은 새 page 또는 새 frame에서 시작한다.
2. 원본 source frame, structured baseline, accepted final frame은 보존한다.
3. component를 수정할 때는 영향을 받는 slide를 먼저 확인한다.
4. 수정 후 full-slide screenshot diff를 돌린다.
5. 결과를 QA 문서에 기록한다.

## Font Caveat

Panchang과 Pretendard는 원본 Figma text layer에 metadata로 남아 있지만, Figma Plugin runtime에서는 missing으로 관측된 적이 있다.

정책:

- 새 텍스트를 대량 재입력하기 전 폰트 설치/enable 상태를 확인한다.
- font가 불안정하면 source text layer를 보존하거나 clone한다.
- 자동화로 fontName을 강제로 바꾸지 않는다.

## Do Not

- `99 Final Componentized Deck`의 accepted frame을 실험용으로 직접 덮어쓰지 않는다.
- 전체 슬라이드를 이미지 한 장으로 flatten하지 않는다.
- component instance를 detach한 뒤 QA 없이 accepted로 표시하지 않는다.
- 원본 source frame과 final frame을 같은 이름으로 혼동하지 않는다.

## New Work Naming

| 작업 | 권장 이름 |
|---|---|
| Blind rebuild page | `Blind Rebuild / S09 / 2026-07-09` |
| Blind rebuild frame | `S09/UserScenario/Blind Rebuild v0.1` |
| New derivative slide | `SXX/<Role>/Derivative v0.1` |
| QA candidate | `SXX/<Role>/QA Candidate v0.1` |
| Component experiment | `JByond/Deck/<ComponentName>/Experiment v0.1` |
