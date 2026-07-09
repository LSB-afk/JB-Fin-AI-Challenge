---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Token Notes

## Current Source Of Truth

`presentation-tokens.json`은 초기 flat token 요약으로 남긴다. 실제 rebuild의 우선순위는 다음 machine-readable 파일이다.

1. `token-index.json`
2. `primitives.json`
3. `semantic.json`
4. `typography.json`
5. `effects.json`
6. `components.json`
7. `slides.json`
8. `assets.json`
9. `qa-rules.json`
10. `assetization-backlog.json`
11. `figma-variable-map.json`

## Source Policy

1. 기존 제품/콘솔 토큰은 `08_본선/03_제품/03_ux/tokens/jb-console-tokens.json`을 기준으로 한다.
2. 발표덱 전용 토큰은 `deck.*` prefix를 사용한다.
3. Figma read-only extraction이 가능한 경우 source node id를 token `$extensions`에 기록한다.
4. local JPG export는 visual QA reference이며, editable layer 값은 Figma extraction을 우선한다.

## Reused Base Tokens

| 목적 | 기존 값 | Deck token |
|---|---|---|
| JB brand primary | `#0A31A8` | reference only |
| Brand accent/glow | `#1C56FF` | `deck.bg.blueGlow`, `deck.status.info` |
| Brand navy | `#0B235B` | `deck.bg.brandNavy` |
| White text/surface | `#FFFFFF` | `deck.text.primaryOnDark`, `deck.surface.diagramPanel` |
| Warning | `#F59E0B` | `deck.status.warning` |
| Success | `#10B981` | `deck.status.success` |
| Danger | `#DC2626` | `deck.status.danger` |

## Deck-Specific Choices

- 발표덱의 frame background는 콘솔 UI보다 더 어둡고 무대 조명처럼 보이는 navy gradient가 필요하다.
- 콘솔 카드 radius `24px`는 실제 제품 화면 내부에서 유지하고, 발표덱의 패널/표/카드는 `8-16px` 중심으로 잡는다.
- `01 Summary`의 `JByond`는 logo image가 아니라 editable wordmark text로 관리한다.
- `07 System Flow`의 가장 작은 텍스트는 `15px` 이하로 내려가지 않도록 한다. 발표장과 영상에서 판독 가능한 최소치다.
- `09 User Scenario`의 4개 story card는 이미지 프레임은 raster를 허용하되 caption과 process flow는 editable로 둔다.

## Figma Checks

- `01 Summary`: `Panchang Medium 300px`, `Pretendard 25/40px`, cover gradient를 확인했다.
- `Panchang`: Fontshare `https://www.fontshare.com/?q=Panchang`을 기준 출처로 등록했고, `assets/fonts/panchang/`에 CSS와 `woff2` 5개 weight를 저장했다.
- 2026-07-09 재확인: Figma Plugin runtime의 available font 목록에는 `Panchang`과 `Pretendard`가 없었다. 따라서 componentized rebuild에서도 source text layer를 복제해 보존하고, text/font property mutation은 보류한다.
- Working Figma 기준 노드: `01 Summary=6:198`, `07 데이터 및 활용 기술=6:325`, `09 User Scenario=6:1046`.
- `07`: dense table text `15.5227/16.4294px`, diagram title `28.3158px`, stroke/radius variants를 확인했다.
- `09`: scenario headline `56.1889px`, process node `15px`, story caption `20px`, image fills `CROP`을 확인했다.
- 현재 남은 큰 Figma componentization 작업은 slides `05/06`의 product UI/callout 구조를 smaller child ID 단위로 분리해 재시도하는 것이다.
- 14장 전체의 남은 추출/컴포넌트화/토큰화 작업은 `assetization-backlog.json`에 machine-readable backlog로 등록했다. md 문서는 사람이 읽는 설명이고, 이 JSON은 다음 A1/A3/A4/A5/A6 루프가 직접 참조하는 실행 계약이다.
- Slide `01` componentization loop에서는 `CoverMediaStackExact` `92:1179`, `CoverHeaderExact` `92:1188`, `CoverFooterExact` `92:1189`, `CoverWordmarkExact` `92:1192`를 승격했고, rebuilt slide `93:1179`에서 tolerance-aware similarity `1.0000000000`을 달성했다. exact-pixel comparison은 Figma instance 렌더링의 1-channel quantization 때문에 넓게 잡히지만 `maxChannelDelta=1`이라 시각 QA 기준에서는 pass로 기록한다.
- Slide `02` componentization loop에서는 broad row component `42:17`이 slide QA에서 row geometry drift를 만들었고, exact-geometry component `48:88`로 교체해 similarity `0.9997815394`를 달성했다. 이 패턴은 이후 text-heavy table/card component promotion의 기준으로 삼는다.
- Slide `03` componentization loop에서는 `EvidenceScreenshotExact/VariantSet` `58:175`와 `EvidenceHighlightExact/VariantSet` `58:182`를 승격했고, rebuilt slide `58:183`에서 source와 byte-identical similarity `1.0000000000`을 달성했다. 증빙 캡처는 raster image-fill component로, 파란 highlight는 editable overlay component로 분리한다.
- Slide `04` componentization loop에서는 `SolutionAxisColumnExact/VariantSet` `53:174`와 `SolutionFlowStepExact/VariantSet` `53:184`를 승격했고, rebuilt slide `54:150`에서 similarity `0.9999657600`을 달성했다. 오른쪽 제품 화면은 원본 raster placement를 보존하고, 좌측 축/하단 flow pill만 editable component instance로 관리한다.
- Slide `07` componentization loop에서는 `SystemFlowTableExact/VariantSet` `66:560`과 `EntityPillExact/VariantSet` `66:610`을 승격했고, rebuilt slide `68:508`에서 similarity `0.9995273920`을 달성했다. 오른쪽 표와 하단 entity pill은 component instance로 관리하고, main flow columns/connectors는 endpoint drift 리스크 때문에 별도 루프로 남긴다.
- Slide `08` componentization loop에서는 `OrgRoleNodeCompactExact/VariantSet` `60:372`, `OrgRoleNodeTallExact/VariantSet` `60:505`, `OrgGateNodeExact/VariantSet` `60:550`을 승격했고, rebuilt slide `61:176`에서 similarity `0.9999146412`를 달성했다. connector는 endpoint drift 리스크 때문에 별도 루프로 남긴다.
- Slide `09` componentization loop에서는 `ScenarioProcessNodeExact/VariantSet` `63:520`과 `ScenarioCardExact/VariantSet` `63:537`을 승격했고, rebuilt slide `64:490`에서 source와 byte-identical similarity `1.0000000000`을 달성했다. workflow/branch node와 story card는 component instance로 관리하고, decision diamond와 connectors는 endpoint drift 리스크 때문에 별도 루프로 남긴다.
- Slide `10` componentization loop에서는 `ExperienceNodeExact/VariantSet` `70:659`를 승격했고, rebuilt slide `70:660`에서 similarity `0.9987331211`을 달성했다. TX/AX/UX/EX-PX/CX experience map node는 component instance로 관리하고, ROI/NPV/time-saved value-chain panel은 dense text reflow 리스크 때문에 evidence caveat와 별도 QA loop가 필요하다.
- Slide `11` componentization loop에서는 `MvpChecklistRowExact/VariantSet` `72:661`과 `DemoPlanRowExact/VariantSet` `72:697`을 승격했고, rebuilt slide `74:649`에서 similarity `0.9999122299`를 달성했다. 완료된 MVP rows와 시연 계획 row pairs는 component instance로 관리하고, headline paragraph는 line-break 리스크 때문에 cloned source layer로 둔다.
- Slide `12` componentization loop에서는 `ExperienceBenefitBubbleExact/VariantSet` `75:690`과 `ExpansionStepExact/VariantSet` `75:703`을 승격했고, rebuilt slide `77:678`에서 similarity `0.9999541860`을 달성했다. AX/EX/CX benefit bubbles와 expansion step labels는 component instance로 관리하고, large orbit vector/radius system은 z-order drift 리스크 때문에 별도 QA loop로 남긴다.
- Slide `13` componentization loop에서는 `ReferenceItem2LineExact/VariantSet` `79:736`, `ReferenceItem3LineExact/VariantSet` `79:832`, `VerificationSummaryRowExact/VariantSet` `79:849`를 승격했고, rebuilt slide `80:688`에서 source와 byte-identical similarity `1.0000000000`을 달성했다. 31개 reference row는 Figma variant cap을 피하기 위해 2-line/3-line set으로 분리하고, provenance normalization은 evidence ledger 작업으로 남긴다.
- Slide `14` componentization loop에서는 `GanttDateTickExact/VariantSet` `85:875`, `GanttLaneMetaExact/VariantSet` `86:885`, `GanttTaskBarExact/VariantSet` `88:987`, `GanttMilestoneExact/VariantSet` `89:813`를 승격했고, rebuilt slide `90:777`에서 similarity `0.9997048611`을 달성했다. 50개 반복 Gantt 단위를 component instance로 교체했고, footer evidence/source box는 반복 사용이 확인될 때만 component 승격한다.
- Slide `05`는 2026-07-09 기준 `6:261`과 `28:159`의 Figma subtree read가 반복적으로 `HTTP 504`를 반환했다. 이후 작은 child ID 기반으로 `FeatureCalloutTopExact/VariantSet` `95:1197`과 `FeatureCalloutRightExact/VariantSet` `96:1195`를 승격했고, rebuilt slide `98:1189`에서 source와 byte-identical similarity `1.0000000000`을 달성했다. unresolved `6:285`는 직접 읽지 않고 baseline clone 안에 보존했으며, 직접 편집은 수동 격리 전까지 금지한다.
- Slide `06`도 2026-07-09 기준 `6:286`과 `28:184`의 lightweight child read 및 baseline metadata read가 `HTTP 504`를 반환했다. 이후 selected child ID workflow로 `ApprovalAuditCalloutExact/VariantSet` `101:1205`를 승격했고, rebuilt slide `101:1206`에서 source와 byte-identical similarity `1.0000000000`을 달성했다. timeout-prone `6:304`는 직접 읽지 않고 baseline clone 안에 보존했다.
