---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# 09 User Scenario Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `assets/source-screenshots/09-user-scenario.jpg` |
| Deck audit node-id | `4915:2636` |
| Provided URL candidate | `5053:12685` |
| Pasted working node-id | `6:1046` |
| Pasted working screenshot | `assets/pasted-working-screenshots/09-user-scenario-6-1046.png` |
| Figma access | `working_source_available_in_h6RkEn7fGbTwZbzuwaHsWi` |

## Message

AI가 근거를 정리하고, 관련 RM이 실행 전 마지막 안전선을 확인하는 업무 흐름을 4컷 시나리오로 보여준다. 히어로 케이스는 `CCL-0001 전주 중앙로 카페 운전자금`이다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | 딥 네이비 gradient | tokenized fill |
| Badge | 중앙 상단 `User Scenario` pill | `ScenarioBadge` component |
| Headline | 중앙 2줄 대형 문장, `실행 전 마지막 안전선` 강조 | editable rich text |
| Process flow | 작은 rounded nodes + decision diamond + branching | vector/text components |
| Use case label | 좌하단 `[Use Case] 전주 중앙로 카페 운전자금 케이스 사례` | editable text |
| Story cards | 4개 white image cards + captions | `ScenarioCard` component |
| Page number | 우하단 `9` | editable text |

## Process Flow

1. `로그인·역할 진입`
2. `케이스보드 칸반`
3. `케이스 생성 CCL-0001`
4. `상세·서류/근거 확인`
5. `에이전트 실행뷰 판단->초안->검증`
6. `승인대기함`
7. `여신 감독 결정`
8. Branch:
   - `고객 회신 발송 큐`
   - `초안 수정 -> 발송 큐`
   - `차단·재작업`
9. `감사 로그 봉인`

## Story Cards

| # | Visual | Caption |
|---:|---|---|
| 1 | RM이 위험 케이스 목록을 확인하는 일러스트 | 카드매출 둔화와 비용 증가로 운전자금 위험 신호가 감지된 소상공인 케이스를 전북은행 RM이 확인한다. |
| 2 | AI Agent가 판단기록/근거를 수집하는 화면 | AI Agent는 고객 맥락, 매출 흐름, 서류 상태, 정책금융 가능성, 준법 체크 포인트를 정리한다. |
| 3 | 하나로 모인 자료/evidence packet UI | RM은 근거 패키지를 바탕으로 판단한다. 판단할 자료가 하나로 정리된다. |
| 4 | 최종 승인 화면과 RM/준법 담당자 승인 말풍선 | 고객 대상 조치는 RM 및 관련 담당자의 승인 후에만 실행된다. 모든 판단, 승인 기록은 Audit Ledger에 남는다. |

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `26:2` |
| 위치 | `x=32628`, `y=1220`, `1920x1080.0001` |
| Source mapping | `6:1046 -> 26:2`, 주요 하위 레이어는 role naming과 `jbyond` metadata로 연결 |
| Source screenshot | `assets/rebuild-screenshots/09-user-scenario-source-6-1046.png` |
| Rebuild screenshot | `assets/rebuild-screenshots/09-user-scenario-structured-26-2.png` |
| Pixel diff | `0 / 2,073,600` changed pixels, similarity `1.0000000000` |
| QA status | `pass_pixel_identical` |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `64:490` |
| Rebuild name | `S09/UserScenario/Componentized Rebuild v1.0` |
| Source baseline | pasted source `6:1046`; structured baseline `26:2` |
| Component sets | `JByond/Deck/ScenarioProcessNodeExact/VariantSet` `63:520`; `JByond/Deck/ScenarioCardExact/VariantSet` `63:537` |
| Instance count | `14` total: 10 process/branch nodes + 4 scenario cards |
| Rebuild screenshot | `assets/rebuild-screenshots/09-user-scenario-componentized-64-490.png` |
| Component evidence | `assets/components/scenario-process-node-exact-variant-set-63-520.png`; `assets/components/scenario-card-exact-variant-set-63-537.png` |
| Pixel diff | `0 / 2,073,600` changed pixels, similarity `1.0000000000` |
| QA record | `qa/visual-diff/09-user-scenario-componentized-v1.0.json` |
| QA status | `pass_pixel_identical_componentized` |

Componentized v1.0 replaces the reusable process/branch nodes and story cards with component instances while preserving the decision diamond, connector lines, background, headline, and use-case label as cloned source layers. This is intentional: the promoted component families are the repeated elements, and the one-off connector geometry stays source-preserving until a separate connector promotion loop can verify endpoint drift.

## Pasted Source Layer Inventory

| Source node | Structured node | Role name | Notes |
|---|---|---|---|
| `6:1047` | `26:3` | `S09/UserScenario/Background/Image/DeepNavyGradient` | full-slide background image fill |
| `6:1048` | `26:4` | `S09/UserScenario/Header` | badge and headline group |
| `6:1053` | `26:9` | `S09/UserScenario/Flow/Node/Step01-LoginRole` | process node |
| `6:1055` | `26:11` | `S09/UserScenario/Flow/Node/Step02-CaseBoardKanban` | process node; source text uses `칸반` |
| `6:1065` | `26:21` | `S09/UserScenario/Flow/Decision/SupervisorDecision` | decision diamond group |
| `6:1069` | `26:25` | `S09/UserScenario/Flow/Branch/CustomerReplyQueue` | top branch |
| `6:1071` | `26:27` | `S09/UserScenario/Flow/Branch/EditDraftToQueue` | middle branch |
| `6:1073` | `26:29` | `S09/UserScenario/Flow/Branch/BlockAndRework` | bottom branch |
| `6:1077` | `26:33` | `S09/UserScenario/Cards/ScenarioCards` | four card container |
| `6:1079` | `26:35` | `S09/UserScenario/Cards/ScenarioCard/Step01/Image/Illustration` | raster-allowed card image |
| `6:1082` | `26:38` | `S09/UserScenario/Cards/ScenarioCard/Step02/Image/Illustration` | raster-allowed card image |
| `6:1085` | `26:41` | `S09/UserScenario/Cards/ScenarioCard/Step03/Image/Illustration` | raster-allowed card image |
| `6:1088` | `26:44` | `S09/UserScenario/Cards/ScenarioCard/Step04/Image/Illustration` | raster-allowed card image |
| `6:1090`-`6:1104` | `26:46`-`26:60` | `S09/UserScenario/Flow/Connectors/*` | connector arrows and branch lines |
| `6:1105` | `26:61` | `S09/UserScenario/UseCase` | use case label/value group |

## Component Model

- `JByond/Deck/ScenarioBadge`
- `JByond/Deck/HeadlineBlock`
- `JByond/Deck/ProcessNode`
- `JByond/Deck/ScenarioProcessNodeExact/VariantSet` (`63:520`, promoted v1.0 exact geometry)
- `JByond/Deck/DecisionDiamond`
- `JByond/Deck/BranchGroup`
- `JByond/Deck/ScenarioCard`
- `JByond/Deck/ScenarioCardExact/VariantSet` (`63:537`, promoted v1.0 exact geometry)
- `JByond/Deck/CardCaption`

## Rebuild Notes

- Story card 내부 일러스트는 pilot에서는 image frame으로 보존하고, 카드 frame/caption/text는 editable로 분리한다. Working source image nodes are `6:1079`, `6:1082`, `6:1085`, `6:1088`.
- Process flow는 반드시 vector/text로 재구성한다. 발표 수정 때 branch label만 바꿀 수 있어야 한다.
- pasted Figma source는 `케이스보드 칸반`으로 확인됐다. 이전 `간반` 표기는 stale interpretation으로 본다.

## QA Risks

- Process flow가 작아 텍스트 선명도와 connector alignment가 중요하다.
- Story card 4개는 같은 width/height/baseline을 유지해야 한다.
- 내부 일러스트 원본이 분리되어 있지 않으면 Figma duplicate에서 imageHash를 추출해야 한다.
- "Enter" 버튼이 시연 현실과 충돌한 정합성 플래그가 있으므로 재사용본에서는 발표 맥락에 맞게 유지/완화 선택이 필요하다.
