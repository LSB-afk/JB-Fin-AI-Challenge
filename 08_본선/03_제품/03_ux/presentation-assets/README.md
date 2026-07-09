---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[design-system]]"
aliases:
  - JByond 발표덱 자산화
  - presentation-assets
---

# JByond 발표덱 자산화 Pilot

목적은 최종 발표용 Figma 덱을 반복 가능하고 재사용 가능한 디자인 자산으로 바꾸는 것이다. 1차 범위는 3장이었고, 현재는 같은 방식의 source-preserving structured clone을 14장 전체로 확장했다.

먼저 읽을 문서는 `INDEX.md`와 `deck-definition.md`다. `INDEX.md`는 모든 문서의 2계층 색인이고, `deck-definition.md`는 발표덱의 철학, 서사 구조, 시각 문법, 재현 규칙, 문서 누락 리뷰를 한 곳에 묶은 상위 정의서다. 팀원에게 공유할 때는 `handoff/README.md`를 시작점으로 사용한다.

| Pilot | 슬라이드 | 역할 | 기준 파일 |
|---|---|---|---|
| 01 | Summary | 브랜드/히어로 calibration | `6:198`, `assets/rebuild-screenshots/01-summary-source-6-198.png` |
| 07 | 데이터 및 활용 기술 | 시스템 플로우/표/아키텍처 복잡도 검증 | `6:325`, `assets/rebuild-screenshots/07-system-flow-source-6-325.png` |
| 09 | 사용자 시나리오 | 스토리보드/업무 흐름/카드 컴포넌트 검증 | `6:1046`, `assets/rebuild-screenshots/09-user-scenario-source-6-1046.png` |

## 현재 상태

- Local source screenshots: ready
- Final PDF order check: ready
- Repo-side reverse engineering docs: ready
- Figma working workspace: created
- User-pasted editable source slides in working Figma: ready
- `01 Summary` editable rebuild v0: created, but visual QA failed and is retained as an experiment
- `01 Summary` structured rebuild v1: `22:2`, pixel-identical to pasted source `6:198`
- `07 데이터 및 활용 기술` structured rebuild v1: `25:2`, similarity `0.9997530864`
- `09 User Scenario` structured rebuild v1: `26:2`, pixel-identical to pasted source `6:1046`
- Remaining 11 slides source-preserving structured rebuild v1: created, all pass QA target; min similarity `0.9996238426`
- Full-deck QA audit: `qa/visual-diff/full-deck-structured-audit-2026-07-09.json`
- Full 14-slide source-analysis docs: ready under `slides/*-source-analysis.md`
- Machine-readable full-deck assetization backlog: `tokens/assetization-backlog.json`
- First promoted Figma components: `JByond/Deck/ProblemCaseCard` node `36:16`, case-card variant set `39:77`, limitation-row variant set `42:17`, exact-geometry limitation-row set `48:88`
- Slide `01` componentized rebuild v1.0: `93:1179`, using components `92:1179`, `92:1188`, `92:1189`, `92:1192`; tolerance-aware similarity `1.0000000000`, max channel delta `1`
- Slide `02` componentized rebuild v1.2: `49:76`, using component sets `39:77` and `48:88`, similarity `0.9997815394`
- Slide `03` componentized rebuild v1.0: `58:183`, using component sets `58:175` and `58:182`, similarity `1.0000000000`
- Slide `04` componentized rebuild v1.0: `54:150`, using component sets `53:174` and `53:184`, similarity `0.9999657600`
- Slide `05` componentized rebuild v1.0: `98:1189`, using component sets `95:1197` and `96:1195`, similarity `1.0000000000`
- Slide `06` componentized rebuild v1.0: `101:1206`, using component set `101:1205`, similarity `1.0000000000`
- Slide `07` componentized rebuild v1.0: `68:508`, using component sets `66:560`, `66:610`, similarity `0.9995273920`
- Slide `08` componentized rebuild v1.0: `61:176`, using component sets `60:372`, `60:505`, `60:550`, similarity `0.9999146412`
- Slide `09` componentized rebuild v1.0: `64:490`, using component sets `63:520`, `63:537`, similarity `1.0000000000`
- Slide `10` componentized rebuild v1.0: `70:660`, using component set `70:659`, similarity `0.9987331211`
- Slide `11` componentized rebuild v1.0: `74:649`, using component sets `72:661`, `72:697`, similarity `0.9999122299`
- Slide `12` componentized rebuild v1.0: `77:678`, using component sets `75:690`, `75:703`, similarity `0.9999541860`
- Slide `13` componentized rebuild v1.0: `80:688`, using component sets `79:736`, `79:832`, `79:849`, similarity `1.0000000000`
- Slide `14` componentized rebuild v1.0: `90:777`, using component sets `85:875`, `86:885`, `88:987`, `89:813`, similarity `0.9997048611`
- Newly extracted materials: slide `01` cover media/header/footer/wordmark component evidence, slide `03` evidence captures, slide `04` solution composite, slide `05` workbench composite/callout component evidence, slide `06` local product-panel crops and approval/audit callout component evidence, slide `11` checklist/demo row component evidence, slide `12` benefit-bubble/expansion-step component evidence, slide `13` reference-item/verification-row component evidence, slide `14` Gantt date/lane/task/milestone component evidence
- Original Figma file access: restored; metadata and read-only `use_figma` probe succeeded
- Current Figma connector account: `Full` seat on `팀 망상궤도`
- Final visual review page: `99 Final Componentized Deck` page `106:1201` in the working Figma file, containing the 14 accepted componentized rebuild frames in PDF order

원본 Figma는 보존한다. 현재 작업 파일은 처음에는 fresh rebuild workspace였으나, 사용자가 원본 작업 슬라이드를 `Page 1`에 붙여넣었다. 따라서 `6:*` 노드들이 이제 editable reverse-engineering 기준이다. A5 Builder는 이 붙여넣은 원본을 기준으로 구조화/컴포넌트화/토큰화를 진행하고, 기존 `5:2` rebuild는 실패 사례와 QA 비교용으로만 남긴다.

Figma rebuild workspace: `https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`

## Final Figma Page

최종 시각 결과물은 working Figma 파일의 `99 Final Componentized Deck` 페이지에 있다. 14개 componentized rebuild frame을 새 페이지로 이동했고, 기존 node-id는 유지했다. 배치는 `1920x1080` 프레임 기준 2열 x 7행이다.

| Slide | Final node-id | Frame name |
|---|---|---|
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

## Working Figma Source Nodes

| Pilot | 붙여넣은 기준 node-id | 역할 | 로컬 기준 이미지 |
|---|---|---|---|
| 01 Summary | `6:198` | cover calibration, Panchang wordmark, laptop hero | `assets/rebuild-screenshots/01-summary-source-6-198.png` |
| 07 데이터 및 활용 기술 | `6:325` | system flow, table, architecture model | `assets/rebuild-screenshots/07-system-flow-source-6-325.png` |
| 09 User Scenario | `6:1046` | workflow, decision branch, four story cards | `assets/rebuild-screenshots/09-user-scenario-source-6-1046.png` |

Full 14-slide source/rebuild mapping is in `slides/_inventory-14.md` and `manifest.json`.

## Structured Rebuild Nodes

| Pilot | Source | Structured rebuild | QA |
|---|---|---|---|
| 01 Summary | `6:198` | `22:2` / `S01/Summary/Structured Rebuild v1.0`; componentized `93:1179` | structured: `0` changed pixels, similarity `1.0000000000`; componentized: tolerance-aware similarity `1.0000000000`, max delta `1`; see `qa/visual-diff/01-summary-componentized-v1.0.json` |
| 07 데이터 및 활용 기술 | `6:325` | `25:2` / `S07/SystemFlow/Structured Rebuild v1.0` | `512` changed pixels, similarity `0.9997530864`; see `qa/visual-diff/07-system-flow-structured-v1.json` |
| 09 User Scenario | `6:1046` | `26:2` / `S09/UserScenario/Structured Rebuild v1.0` | `0` changed pixels, similarity `1.0000000000`; see `qa/visual-diff/09-user-scenario-structured-v1.json` |

Full-deck expansion nodes:

| Range | Structured rebuild nodes | QA |
|---|---|---|
| 02-06 | `28:2`, `28:95`, `28:108`, `28:159`, `28:184` | Pass; `03`, `05`, `06` are byte-equal full PNG exports; `02`, `04` pass pixel diff |
| 08 | `28:211` | Pass; similarity `0.9999995177` |
| 10-14 | `29:2`, `29:104`, `29:151`, `29:214`, `29:357` | Pass; min similarity `0.9996238426`; `13` is byte-equal full PNG export |

Slide `02` now also has a componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.1 | `46:2` | `39:77`, `42:17` | similarity `0.9938806906`; passed 98% but rejected because row geometry drifted |
| v1.2 | `49:76` | `39:77`, `48:88` | similarity `0.9997815394`; current accepted componentized baseline |

Slide `03` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `58:183` | `58:175`, `58:182` | similarity `1.0000000000`; evidence screenshots and highlight overlays are component instances |

Slide `04` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `54:150` | `53:174`, `53:184` | similarity `0.9999657600`; solution axis columns and flow step pills are component instances |

Slide `05` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `98:1189` | `95:1197`, `96:1195` | similarity `1.0000000000`; top/right callout labels are component instances |

Slide `06` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `101:1206` | `101:1205` | similarity `1.0000000000`; approval/audit callout labels are component instances |

Slide `07` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `68:508` | `66:560`, `66:610` | similarity `0.9995273920`; right-side tables and bottom entity pills are component instances |

Slide `08` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `61:176` | `60:372`, `60:505`, `60:550` | similarity `0.9999146412`; 29 org/gate cards are component instances |

Slide `09` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `64:490` | `63:520`, `63:537` | similarity `1.0000000000`; process nodes and scenario cards are component instances |

Slide `10` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `70:660` | `70:659` | similarity `0.9987331211`; TX/AX/UX/EX-PX/CX experience nodes are component instances |

Slide `11` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `74:649` | `72:661`, `72:697` | similarity `0.9999122299`; MVP checklist rows and demo-plan rows are component instances |

Slide `12` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `77:678` | `75:690`, `75:703` | similarity `0.9999541860`; AX/EX/CX benefit bubbles and right-side expansion steps are component instances |

Slide `13` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `80:688` | `79:736`, `79:832`, `79:849` | similarity `1.0000000000`; 31 reference items and 4 verification rows are component instances |

Slide `14` componentized rebuild loop:

| Version | Node | Component sets | QA |
|---|---|---|---|
| v1.0 | `90:777` | `85:875`, `86:885`, `88:987`, `89:813` | similarity `0.9997048611`; 14 date ticks, 9 lane metadata rows, 21 task bars, and 6 milestone markers are component instances |

Panchang은 Fontshare를 기준 소스로 등록했다. 로컬 폰트 자산은 `assets/fonts/panchang/`에 있고, cover wordmark token은 `Panchang Medium 500`을 사용한다. Figma Plugin API에서는 pasted text nodes가 `Panchang`/`Pretendard` fontName을 보존하지만 `hasMissingFont: true`로 보고된다. 고품질 editable rebuild 전에는 Figma에서 해당 폰트를 enable/install해야 한다.

2026-07-09 재확인에서도 Figma Plugin runtime의 available font 목록에는 `Panchang`과 `Pretendard`가 노출되지 않았다. 따라서 새 텍스트를 재타이핑하지 않고, 원본 text layer를 복제한 뒤 component/metadata를 입히는 방식을 기본 정책으로 둔다.

## Directory

| 경로 | 소유 에이전트 | 내용 |
|---|---|---|
| `manifest.json` | A0 | 슬라이드, node-id, reference asset, QA status |
| `slides/` | A1 | 슬라이드별 원본 분석과 rebuild spec |
| `tokens/` | A2 | 발표덱 전용 design tokens |
| `components/` | A3 | Figma component catalog |
| `assets/` | A4 | source screenshots, 이미지, 그래프, 표, ledger |
| `qa/` | A6 | visual QA, diff, test loop |
| `process/` | A7 | AI build log, prompts, parallel agent model |

## PDF Order Baseline

최종 발표 PDF `08_본선/05_제출/제출본/PPT/JBFinAI_JByond_본선_PPT.pdf`는 14페이지이며, 각 page마다 `1920x1080` JPEG image 1개가 들어 있다. PDF page order는 `PPT/Figma/*.jpg` 14장 export 순서와 일치한다. 자세한 확인 결과는 `qa/pdf-order-check.md`를 기준으로 한다.

## Build Loop

1. Pasted editable source node를 기준으로 source layer inventory를 확정한다.
2. 원본 node를 구조화 복제하고, 원본은 보존한 채 복제본에 role naming과 `jbyond` metadata를 붙인다.
3. source/rebuild screenshot을 `1920x1080`으로 저장하고 pixel diff를 계산한다.
4. pixel baseline이 통과하면 토큰, asset ledger, component catalog에 연결한다.
5. 같은 규칙으로 `07`, `09`를 확장한다.
6. 3장 pilot 통과 후 같은 clone/QA 방식으로 14장 전체 pixel baseline을 만든다.
7. 남은 11장은 baseline을 깨지 않는 범위에서 role taxonomy, asset extraction, component promotion을 순차 진행한다.

## Quality Gates

- Slide: `1920x1080`, editable text, no full-slide flatten image, no visible text clipping
- Token: 주요 color/type/effect/spacing/radius가 `tokens/token-index.json` 아래 machine-readable token files에 등록
- Component: 2회 이상 반복되는 요소는 component 또는 documented pattern
- Asset: 이미지/그래프/표는 출처, 사용 슬라이드, 원본/파생 여부 기록
- QA: 원본 대비 차이, 수정 루프, 남은 오차를 기록

## Next Work

3장 pilot 구조화 복제 loop, 14장 전체 source-preserving clone baseline, 14장 source-analysis 문서화, machine-readable backlog 작성은 통과했다. 모든 14장은 98% visual gate를 넘는 componentized rebuild loop를 보유한다. Slide `02`는 case card와 limitation row, slide `03`은 evidence screenshots/highlight overlays, slide `04`는 solution axis/flow step, slide `05`는 feature callouts, slide `06`은 approval/audit callouts, slide `07`은 right-side tables/entity pills, slide `08`은 조직도 카드/gate node, slide `09`는 process nodes/scenario cards, slide `10`은 experience map nodes, slide `11`은 MVP checklist/demo-plan rows, slide `12`는 AX/EX/CX benefit bubbles와 expansion step labels, slide `13`은 reference items와 verification rows, slide `14`는 Gantt date ticks/lane metadata/task bars/milestones를 component instance로 치환했다. 남은 작업은 slide `07` main flow columns/connectors, slide `08` connector/ops panel, slide `12` large orbit vector/radius system 같은 one-off 영역의 선택적 추가 atomization이다.
