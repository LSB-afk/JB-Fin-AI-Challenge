---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 05 Key Feature UI Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/05 주요기능.jpg` |
| Deck audit node-id | `4852:2316` |
| Pasted working node-id | `6:261` |
| Structured rebuild node-id | `28:159` |
| QA reference | `qa/visual-diff/full-deck-structured-audit-2026-07-09.json` |
| Figma access | `visual_reference_ok_metadata_timeout` |

## Message

위험 신호를 개별 알림이 아니라 하나의 `Case`로 묶고, RM이 케이스 상태와 AI Agent 실행 결과를 한 화면에서 확인하는 업무 콘솔을 보여준다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | deep navy stage with blue product glow | `FrameDark.productShot` |
| Header | `Key Feature 1.` + headline + 2줄 설명 | editable text |
| Large product screenshot | Case Board UI, sidebar, status filters, case cards | raster allowed until UI is rebuilt as product mockup components |
| Callouts | thin connector lines to product areas | `UICalloutLine` |
| Right labels | `Case Board`, `Risk Signal`, `Agent Run`, `Evidence Pack` | editable callout labels |
| Footer page | page number `5` | editable text |

## Text Inventory

- `Key Feature 1.`
- `Case 중심 AI Agent 워크벤치`
- `위험 신호를 개별 알림이 아니라 하나의 Case로 묶고,`
- `RM이 케이스 상태와 AI Agent 실행 결과를 한 화면에서 확인할 수 있는 업무 콘솔이다.`
- `Case Board` / `신규·진행·검토·완료·차단 상태별 케이스 관리`
- `Risk Signal` / `매출 둔화, 상환 부담, 서류 누락 등 위험 신호 연결`
- `Agent Run` / `Case별 Agent가 판단->행동 초안->검증 흐름으로 실행`
- `Evidence Pack` / `고객 정보, 매출 흐름, 서류, 정책 금융 후보를 근거 단위로 정리`

## Visual Layer Model

| Role | Notes |
|---|---|
| `ProductShot/CaseBoard` | large screenshot with rounded browser chrome and bright white content area |
| `ConsoleSidebar` | JB side nav and task categories |
| `CaseCard` | 3 repeated cards with status chips, risk signal, agents, evidence tags, next action |
| `Callout/CaseBoard` | top connector to status filters |
| `Callout/RiskSignal` | top-right connector to case risk area |
| `Callout/AgentRun` | right connector to next action/agent area |
| `Callout/EvidencePack` | right-lower connector to evidence tags |

## Component Model

- `JByond/Deck/UICalloutPanel`
- `JByond/Deck/ProductScreenshotFrame`
- `JByond/Deck/FeatureCalloutLabel`
- `JByond/ConsoleShot/CaseCard`
- `JByond/ConsoleShot/SidebarNav`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:159` |
| Source mapping | `6:261 -> 28:159` |
| QA | full PNG byte-equal export, similarity `1.0000000000` |
| Scope status | root-structured clone; Figma metadata extraction timed out and must be retried by smaller subtree |

## QA Risks

- Product screenshot is visually central. If rebuilt as editable UI later, card spacing and screenshot crop must be checked with full pixel diff.
- Figma metadata extraction for the full source node timed out; next pass should target subtrees under `6:261` instead of the whole slide.
- Connector lines are thin and easy to misalign during component promotion.

## 2026-07-09 Figma Read Issue

Slide `05` still has a valid source-preserving structured baseline, but Figma inspection is currently unstable for this node. The following reads returned `HTTP 504`:

- full subtree `use_figma` candidate extraction for `6:261` / `28:159`
- `get_metadata` on `28:159`
- minimal direct-child `use_figma` read on `28:159`

Next retry should use manually selected child IDs or smaller isolated nodes rather than the full slide frame.

## 2026-07-09 Smaller Child ID Probe

Single-node `get_metadata` calls work for most Slide 05 children. A bundled `use_figma` loop over the same IDs still returned `HTTP 504`, so the safe workflow is one-node metadata probes plus narrowly scoped write calls.

| Source node | Role | Type | x | y | w | h | Status |
|---|---|---|---:|---:|---:|---:|---|
| `6:262` | product screenshot composite | rounded rectangle | 289 | 291 | 1278 | 890 | metadata ok |
| `6:263` | eyebrow `Key Feature 1.` | text | 93 | 73 | 835 | 30 | metadata ok |
| `6:264` | headline | text | 90 | 115 | 784 | 42 | metadata ok |
| `6:265` | product panel/card mask | rounded rectangle | 615 | 408 | 918 | 724 | metadata ok |
| `6:266` | product column mask | rounded rectangle | 635 | 491 | 286 | 724 | metadata ok |
| `6:267` | product column mask | rounded rectangle | 928 | 491 | 290 | 724 | metadata ok |
| `6:268` | product column mask | rounded rectangle | 1226 | 491 | 290 | 724 | metadata ok |
| `6:269` | connector line to `Case Board` | vector | 1048 | 157 | 64 | 251 | metadata ok |
| `6:270` | connector line to `Risk Signal` | vector | 1302 | 241 | 64 | 267 | metadata ok |
| `6:271` | `Case Board` callout group | frame | 1133 | 125 | 337 | 60 | metadata ok; children `6:272`, `6:273` |
| `6:274` | `Risk Signal` callout group | frame | 1387 | 214 | 337 | 60 | metadata ok; children `6:275`, `6:276` |
| `6:277` | `Agent Run` label | text | 1615 | 770 | 337 | 27 | metadata ok |
| `6:278` | `Evidence Pack` label | text | 1615 | 908 | 114 | 27 | metadata ok |
| `6:279` | `Agent Run` description | text | 1615 | 800 | 231 | 60 | metadata ok |
| `6:280` | `Evidence Pack` description | text | 1615 | 938 | 241 | 60 | metadata ok |
| `6:281` | connector spine | vector | 1330 | 252 | 36 | 508 | metadata ok |
| `6:282` | lower-right connector | vector | 1705 | 1009.5 | 273 | 28.5 | metadata ok |
| `6:283` | mid-right connector | vector | 1660 | 759.5 | 247.5 | 28.5 | metadata ok |
| `6:284` | headline body backing rectangle | rounded rectangle | 90 | 208 | 798 | 42 | metadata ok |
| `6:285` | unresolved final child | unknown | - | - | - | - | single-node metadata returned `HTTP 504`; avoid until manually selected |

Componentization target from this map: promote `6:271`/`6:274` plus `6:277-280` into exact callout label components, keep `6:262` as raster product screenshot, and preserve vectors `6:269-270`, `6:281-283` as exact connector components or cloned source layers.

## 2026-07-09 Componentized Rebuild V1.0

Full slide `05` now has an accepted componentized rebuild. The build avoided direct access to unresolved node `6:285` by cloning the verified structured baseline `28:159`, hiding the original callout label layers, and placing promoted callout component instances at the exact source coordinates.

| Component | Figma node | Source nodes | Variants | Evidence |
|---|---|---|---|---|
| `JByond/Deck/FeatureCalloutTopExact/VariantSet` | `95:1197` | `6:271`, `6:274` | `CaseBoard`, `RiskSignal` | `assets/components/feature-callout-top-exact-variant-set-95-1197.png` |
| `JByond/Deck/FeatureCalloutRightExact/VariantSet` | `96:1195` | `6:277`, `6:279`, `6:278`, `6:280` | `AgentRun`, `EvidencePack` | `assets/components/feature-callout-right-exact-variant-set-96-1195.png` |

| 항목 | 값 |
|---|---|
| Componentized rebuild node | `98:1189` |
| Source screenshot | `assets/rebuild-screenshots/05-key-feature-ui-source-6-261.png` |
| Rebuild screenshot | `assets/rebuild-screenshots/05-key-feature-ui-componentized-98-1189.png` |
| Visual diff | `qa/visual-diff/05-key-feature-ui-componentized-v1.0.json` |
| QA | byte-identical screenshot export, similarity `1.0000000000`, changed pixels `0` |
| Component instances | `98:1214`, `98:1217`, `98:1220`, `98:1223` |
| Hidden original callout layers | `98:1199`, `98:1202`, `98:1205`, `98:1206`, `98:1207`, `98:1208` |

Next build rule: do not direct-read `6:285` until manually isolated. If additional reuse is needed, promote connector vectors `6:269`, `6:270`, `6:281`, `6:282`, and `6:283` in a connector-only loop and rerun full-slide screenshot diff.
