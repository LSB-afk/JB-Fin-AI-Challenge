---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Component Catalog

Figma component naming은 `JByond/Deck/...`를 사용한다. 제품 UI 캡처 내부를 재구성하는 경우에는 `JByond/ConsoleShot/...`로 분리한다.

## Core Components

| Component | 목적 | Props / variants | Pilot slides |
|---|---|---|---|
| `JByond/Deck/FrameDark` | 1920x1080 navy stage frame | `glow: none/right/center`, `footer: true/false` | 01, 07, 09 |
| `JByond/Deck/FooterMeta` | 대회명, 팀명, page number | `left`, `right`, `page`, `mode: cover/page` | 01, 07, 09 |
| `JByond/Deck/SlideHeader` | eyebrow + headline group | `align: left/center`, `tone: muted/strong` | 01, 07, 09 |
| `JByond/Deck/SectionBadge` | `User Scenario` 같은 pill label | `label`, `align`, `tone` | 09 |
| `JByond/Deck/HeroWordmark` | `JByond` 대형 editable wordmark | `size: cover/section`, `opacity` | 01 |
| `JByond/Deck/ProductShotLaptop` | 노트북/콘솔 hero image | `crop`, `shadow`, `overlay` | 01 |

## System Flow Components

| Component | 목적 | Props / variants | Pilot slides |
|---|---|---|---|
| `JByond/Deck/SystemFlowPanel` | 흰색 시스템 다이어그램 패널 | `density: high`, `title` | 07 |
| `JByond/Deck/FlowStageHeader` | 1-6 단계 헤더 pill | `index`, `label`, `state` | 07 |
| `JByond/Deck/FlowNode` | 단계 내부 업무/통제 노드 | `tone: neutral/security/ai/approval/execution`, `height` | 07 |
| `JByond/Deck/FlowConnector` | flow arrow/line | `direction`, `elbow`, `dashed` | 07, 09 |
| `JByond/Deck/EntityPill` | Case, AgentRun 등 운영계약 객체 | `label`, `subtitle`, `tone` | 07 |
| `JByond/Deck/DarkTable` | dark background 위 데이터/기술 표 | `columns`, `rowCount`, `divider: solid/dotted` | 07 |
| `JByond/Deck/TableRow` | 표 행 | `emphasis`, `muted` | 07 |

## Scenario Components

| Component | 목적 | Props / variants | Pilot slides |
|---|---|---|---|
| `JByond/Deck/ProcessNode` | 작은 workflow step box | `label`, `width`, `tone` | 09 |
| `JByond/Deck/DecisionDiamond` | 의사결정 diamond | `label`, `branches` | 09 |
| `JByond/Deck/BranchGroup` | 3분기 action group | `items`, `layout` | 09 |
| `JByond/Deck/ScenarioCard` | 4컷 시나리오 카드 | `stepNo`, `image`, `caption`, `state` | 09 |
| `JByond/Deck/CardCaption` | 카드 하단 caption | `stepNo`, `text`, `align` | 09 |

## Full Deck Candidate Components

These are candidate patterns from the 14-slide clone baseline. They are not promoted to final Figma components until a component refactor preserves the slide pixel baseline.

| Component candidate | 목적 | Props / variants | Source slides |
|---|---|---|---|
| `JByond/Deck/ComparisonCard` | 문제정의/비교 항목 카드 | `tone`, `title`, `caption`, `evidence` | 02, 03 |
| `JByond/Deck/SolutionAxisFlow` | 솔루션 개요 흐름/축 다이어그램 | `steps`, `axisTone`, `connectorStyle` | 04 |
| `JByond/Deck/UICalloutPanel` | 제품 UI 캡처 + 설명 callout | `screenshot`, `calloutCount`, `state` | 05, 06, 11 |
| `JByond/Deck/OrgRoleNode` | AI 업무 지원 조직도 역할 노드 | `role`, `owner`, `status`, `tone` | 08 |
| `JByond/Deck/MetricBlock` | 기대효과 수치/효과 블록 | `value`, `unit`, `label`, `evidenceLevel` | 10 |
| `JByond/Deck/ExpansionOrbit` | 확장성/마무리 순환 구조 | `items`, `centerLabel`, `tone` | 12 |
| `JByond/Deck/ReferenceGroup` | Appendix 출처 묶음 | `sourceType`, `confidence`, `url`, `note` | 13 |
| `JByond/Deck/GanttLane` | 협업 간트 lane 및 task bar | `owner`, `phase`, `start`, `end`, `status` | 14 |

## Component Promotion Queue

These are the next concrete promotion units. Each promotion must keep the existing source-clone baseline and be followed by the same screenshot diff used in `qa/rebuild-diff.md`.

Promoted v1 component:

| Component | Figma node | Source | Evidence | Notes |
|---|---|---|---|---|
| `JByond/Deck/CoverMediaStackExact` | `92:1179` | slide 01 structured nodes `22:3`, `22:7`, `22:8`, `22:9`, `22:10` | `assets/components/cover-media-stack-exact-92-1179.png` | Exact cover media stack for stage image, laptop product image, hand accent, and bottom veil overlays. Used in slide 01 componentized rebuild `93:1179`. |
| `JByond/Deck/CoverHeaderExact` | `92:1188` | slide 01 structured node `22:4` | `assets/components/cover-header-exact-92-1188.png` | Exact header component. Text was not mutated because Pretendard is unavailable in the plugin runtime; source font metadata is preserved. |
| `JByond/Deck/CoverFooterExact` | `92:1189` | slide 01 structured nodes `22:11`, `22:12` | `assets/components/cover-footer-exact-92-1189.png` | Exact footer component. Text was not mutated because Pretendard is unavailable in the plugin runtime; source font metadata is preserved. |
| `JByond/Deck/CoverWordmarkExact` | `92:1192` | slide 01 structured node `22:13` | `assets/components/cover-wordmark-exact-92-1192.png` | Exact Panchang wordmark component. Used in slide 01 componentized rebuild `93:1179`. |
| `JByond/Deck/ProblemCaseCard` | `36:16` | slide 02 node `6:11` | `assets/components/problem-case-card-36-16.png` | Source-preserving component clone. Future work should add variants for the other slide 02 case-card widths/states without mutating the slide baseline. |
| `JByond/Deck/ProblemCaseCard/VariantSet` | `39:77` | slide 02 nodes `6:11`, `6:55`, `6:69`, `6:25`, `6:39` | `assets/components/problem-case-card-variant-set-39-77.png` | Five variants with `Size=large/small` and `Source=capital/aqua/farm/student`. Original slide baseline remains untouched. |
| `JByond/Deck/LimitationRow/VariantSet` | `42:17` | slide 02 row nodes `6:84`-`6:94` | `assets/components/limitation-row-variant-set-42-17.png` | Three variants with `Approach=chatbot/dashboard/rpa`. Child bounds expanded to avoid text clipping. |
| `JByond/Deck/LimitationRowExact/VariantSet` | `48:88` | slide 02 structured row nodes `28:83`, `28:88`, `28:91`, `28:86`, `28:89`, `28:92`, `28:87`, `28:90`, `28:93` | `assets/components/limitation-row-exact-variant-set-48-88.png` | Exact-geometry variant set for pixel-critical slide rebuilds. It restored slide 02 componentized similarity from `0.9938806906` to `0.9997815394`. |
| `JByond/Deck/EvidenceScreenshotExact/VariantSet` | `58:175` | slide 03 evidence image nodes `6:321`, `6:320` | `assets/components/evidence-screenshot-exact-variant-set-58-175.png` | Exact-source variants for the two evidence screenshots. Used in slide 03 componentized rebuild `58:183`, which is byte-identical to source. |
| `JByond/Deck/EvidenceHighlightExact/VariantSet` | `58:182` | slide 03 highlight nodes `6:322`, `6:323`, `6:324` | `assets/components/evidence-highlight-exact-variant-set-58-182.png` | Exact-source variants for blue evidence highlight overlays. Used in slide 03 componentized rebuild `58:183`. |
| `JByond/Deck/SolutionAxisColumnExact/VariantSet` | `53:174` | slide 04 structured nodes `28:116`, `28:123`, `28:130` | `assets/components/solution-axis-column-exact-variant-set-53-174.png` | Exact-geometry variants for `기관`, `역할`, `케이스` columns. Used in slide 04 componentized rebuild `54:150`. |
| `JByond/Deck/SolutionFlowStepExact/VariantSet` | `53:184` | slide 04 structured nodes `28:147`, `28:149`, `28:151` | `assets/components/solution-flow-step-exact-variant-set-53-184.png` | Exact-geometry variants for flow pills `AI Agent 정리`, `담당자 확인`, `다음 역할 전달`. Used in slide 04 componentized rebuild `54:150`. |
| `JByond/Deck/FeatureCalloutTopExact/VariantSet` | `95:1197` | slide 05 small child nodes `6:271`, `6:274` | `assets/components/feature-callout-top-exact-variant-set-95-1197.png` | Exact variants for `CaseBoard` and `RiskSignal` callout labels. Used in slide 05 componentized rebuild `98:1189`. |
| `JByond/Deck/FeatureCalloutRightExact/VariantSet` | `96:1195` | slide 05 small child text pairs `6:277`, `6:279`, `6:278`, `6:280` | `assets/components/feature-callout-right-exact-variant-set-96-1195.png` | Exact variants for `AgentRun` and `EvidencePack` callout labels. Used in slide 05 componentized rebuild `98:1189`. |
| `JByond/Deck/ApprovalAuditCalloutExact/VariantSet` | `101:1205` | slide 06 selected child nodes `6:309`, `6:305` | `assets/components/approval-audit-callout-exact-variant-set-101-1205.png` | Exact variants for `L0L4Gate` and `AuditLogAgent` callout labels. Used in slide 06 componentized rebuild `101:1206`. |
| `JByond/Deck/SystemFlowTableExact/VariantSet` | `66:560` | slide 07 structured table nodes `25:4`, `25:22` | `assets/components/system-flow-table-exact-variant-set-66-560.png` | Exact-geometry variants for the right-side data and technology tables. Used in slide 07 componentized rebuild `68:508`. |
| `JByond/Deck/EntityPillExact/VariantSet` | `66:610` | slide 07 structured entity pill nodes `25:217`, `25:223`, `25:229`, `25:235`, `25:241`, `25:247`, `25:253` | `assets/components/entity-pill-exact-variant-set-66-610.png` | Seven exact operational contract entity variants. Used in slide 07 componentized rebuild `68:508`. |
| `JByond/Deck/OrgRoleNodeCompactExact/VariantSet` | `60:372` | slide 08 compact card nodes `28:295`-`28:464` | `assets/components/org-role-node-compact-exact-variant-set-60-372.png` | Fourteen exact 256x94 org role card variants. Used in slide 08 componentized rebuild `61:176`. |
| `JByond/Deck/OrgRoleNodeTallExact/VariantSet` | `60:505` | slide 08 tall card nodes `28:215`-`28:507` | `assets/components/org-role-node-tall-exact-variant-set-60-505.png` | Twelve exact 256x117 org role card variants. Used in slide 08 componentized rebuild `61:176`. |
| `JByond/Deck/OrgGateNodeExact/VariantSet` | `60:550` | slide 08 gate nodes `28:517`, `28:534`, `28:546` | `assets/components/org-gate-node-exact-variant-set-60-550.png` | Three exact top approval/coordination variants. Duplicate source titles were disambiguated in variant names. |
| `JByond/Deck/ScenarioProcessNodeExact/VariantSet` | `63:520` | slide 09 process/branch nodes `26:9`, `26:11`, `26:13`, `26:15`, `26:17`, `26:19`, `26:25`, `26:27`, `26:29`, `26:31` | `assets/components/scenario-process-node-exact-variant-set-63-520.png` | Ten exact workflow/branch node variants. Used in slide 09 componentized rebuild `64:490`. |
| `JByond/Deck/ScenarioCardExact/VariantSet` | `63:537` | slide 09 story card nodes `26:34`, `26:37`, `26:40`, `26:43` | `assets/components/scenario-card-exact-variant-set-63-537.png` | Four exact scenario card variants with preserved image fills and editable captions. Used in slide 09 componentized rebuild `64:490`. |
| `JByond/Deck/ExperienceNodeExact/VariantSet` | `70:659` | slide 10 experience map nodes `29:8`, `29:21`, `29:37`, `29:49`, `29:69` | `assets/components/experience-node-exact-variant-set-70-659.png` | Five exact TX/AX/UX/EX-PX/CX node variants. Used in slide 10 componentized rebuild `70:660`. |
| `JByond/Deck/MvpChecklistRowExact/VariantSet` | `72:661` | slide 11 checklist row nodes `29:112`, `29:114`, `29:116`, `29:118` | `assets/components/mvp-checklist-row-exact-variant-set-72-661.png` | Four exact 완료된 MVP row variants. Used in slide 11 componentized rebuild `74:649`. |
| `JByond/Deck/DemoPlanRowExact/VariantSet` | `72:697` | slide 11 demo row nodes `29:121`, `29:127`, `29:133`, `29:139`, `29:145` | `assets/components/demo-plan-row-exact-variant-set-72-697.png` | Five exact 시연 계획 row-pair variants. Used in slide 11 componentized rebuild `74:649`. |
| `JByond/Deck/ExperienceBenefitBubbleExact/VariantSet` | `75:690` | slide 12 benefit bubble nodes `29:188`, `29:191`, `29:194` | `assets/components/experience-benefit-bubble-exact-variant-set-75-690.png` | Three exact AX/EX/CX benefit bubble variants. Used in slide 12 componentized rebuild `77:678`. |
| `JByond/Deck/ExpansionStepExact/VariantSet` | `75:703` | slide 12 expansion step nodes `29:204`, `29:206`, `29:208`, `29:210` | `assets/components/expansion-step-exact-variant-set-75-703.png` | Four exact right-side expansion step label variants. Used in slide 12 componentized rebuild `77:678`. |
| `JByond/Deck/ReferenceItem2LineExact/VariantSet` | `79:736` | slide 13 2-line reference item nodes | `assets/components/reference-item-2line-exact-variant-set-79-736.png` | Twelve exact 2-line reference item variants. Split from the full item family to keep the variant set under the 30-variant cap. Used in slide 13 componentized rebuild `80:688`. |
| `JByond/Deck/ReferenceItem3LineExact/VariantSet` | `79:832` | slide 13 3-line reference item nodes | `assets/components/reference-item-3line-exact-variant-set-79-832.png` | Nineteen exact 3-line reference item variants. Used in slide 13 componentized rebuild `80:688`. |
| `JByond/Deck/VerificationSummaryRowExact/VariantSet` | `79:849` | slide 13 verification rows `29:344`, `29:347`, `29:350`, `29:353` | `assets/components/verification-summary-row-exact-variant-set-79-849.png` | Four exact verification summary row variants. Used in slide 13 componentized rebuild `80:688`. |
| `JByond/Deck/GanttDateTickExact/VariantSet` | `85:875` | slide 14 date labels and grid lines | `assets/components/gantt-date-tick-exact-variant-set-85-875.png` | Fourteen exact date tick variants. Used in slide 14 componentized rebuild `90:777`. |
| `JByond/Deck/GanttLaneMetaExact/VariantSet` | `86:885` | slide 14 lane shells and left-side metadata | `assets/components/gantt-lane-meta-exact-variant-set-86-885.png` | Nine exact lane metadata variants with row shell, track label, progress, human owner line, and AI/model line. Used in slide 14 componentized rebuild `90:777`. |
| `JByond/Deck/GanttTaskBarExact/VariantSet` | `88:987` | slide 14 task bar backgrounds and three internal labels | `assets/components/gantt-task-bar-exact-variant-set-88-987.png` | Twenty-one exact task bar variants. Used in slide 14 componentized rebuild `90:777`. |
| `JByond/Deck/GanttMilestoneExact/VariantSet` | `89:813` | slide 14 milestone vertical lines and bottom labels | `assets/components/gantt-milestone-exact-variant-set-89-813.png` | Six exact milestone marker variants. Used in slide 14 componentized rebuild `90:777`. |

| Priority | Component | Source slides | Promotion input | QA expectation |
|---:|---|---|---|---|
| 0 | `JByond/Deck/CoverMediaStackExact`, `JByond/Deck/CoverHeaderExact`, `JByond/Deck/CoverFooterExact`, `JByond/Deck/CoverWordmarkExact` | 01 | cover media, header, footer, and wordmark | components `92:1179`, `92:1188`, `92:1189`, `92:1192` promoted; slide 01 componentized clone `93:1179` passes tolerance-aware QA with max channel delta `1` |
| 1 | `JByond/Deck/ProblemCaseCard` | 02 | repeated RM/case cards | variant set promoted as node `39:77`; next map into slide clone and rerun slide 02 diff |
| 2 | `JByond/Deck/LimitationRow` | 02 | 기존 접근/한계 rows | broad variant set `42:17` and exact-geometry set `48:88` promoted; slide 02 componentized clone `49:76` passes with similarity `0.9997815394` |
| 3 | `JByond/Deck/EvidenceCapture` | 03 | two regulation/article image fills plus highlights | exact evidence screenshot set `58:175` and highlight set `58:182` promoted; slide 03 componentized clone `58:183` is byte-identical to source |
| 4 | `JByond/Deck/SolutionAxisFlow` | 04 | role/case/AI/human/next-role flow | axis columns `53:174` and flow step pills `53:184` promoted; slide clone `54:150` passes with similarity `0.9999657600` |
| 5 | `JByond/Deck/SystemFlowTableExact`, `JByond/Deck/EntityPillExact` | 07 | right-side tables and bottom entity rail | sets `66:560`, `66:610` promoted; slide 07 componentized clone `68:508` passes with similarity `0.9995273920` |
| 6 | `JByond/Deck/FeatureCallout` / `ApprovalAuditCallout` | 05, 06, 11 | UI screenshot callout labels and leader lines | Slide 05 sets `95:1197`/`96:1195` and slide 06 set `101:1205` are mapped into byte-identical rebuilds `98:1189` and `101:1206` |
| 7 | `JByond/Deck/ProductScreenshotFrame` | 05, 06, 11 | product UI crops and device/panel shadows | Image crop and shadow must be ledgered |
| 8 | `JByond/Deck/OrgRoleNode` | 08 | AI organization role nodes | compact `60:372`, tall `60:505`, and gate `60:550` sets promoted; slide 08 componentized clone `61:176` passes with similarity `0.9999146412` |
| 9 | `JByond/Deck/ScenarioProcessNodeExact`, `JByond/Deck/ScenarioCardExact` | 09 | process nodes and four scenario cards | sets `63:520`, `63:537` promoted; slide 09 componentized clone `64:490` is byte-identical to source |
| 10 | `JByond/Deck/ExperienceNodeExact` | 10 | TX/AX/UX/EX-PX/CX experience map nodes | set `70:659` promoted; slide 10 componentized clone `70:660` passes with similarity `0.9987331211` |
| 11 | `JByond/Deck/MetricBlock` | 10 | ROI/NPV/time-saved value chain blocks | Numeric values remain editable and evidence-linked |
| 12 | `JByond/Deck/MvpChecklistRowExact`, `JByond/Deck/DemoPlanRowExact` | 11 | MVP checklist rows and demo-plan row pairs | sets `72:661`, `72:697` promoted; slide 11 componentized clone `74:649` passes with similarity `0.9999122299` |
| 13 | `JByond/Deck/ExperienceBenefitBubbleExact`, `JByond/Deck/ExpansionStepExact` | 12 | AX/EX/CX benefit bubbles and step labels | sets `75:690`, `75:703` promoted; slide 12 componentized clone `77:678` passes with similarity `0.9999541860` |
| 14 | `JByond/Deck/ExpansionOrbit` | 12 | large orbit vector/radius system | Promote only after z-order drift check against `77:678` |
| 15 | `JByond/Deck/ReferenceItem2LineExact`, `JByond/Deck/ReferenceItem3LineExact`, `JByond/Deck/VerificationSummaryRowExact` | 13 | appendix reference entries and verification rows | sets `79:736`, `79:832`, `79:849` promoted; slide 13 componentized clone `80:688` is byte-identical to source |
| 16 | `JByond/Deck/ReferenceColumn`, `JByond/Deck/EvidenceConfidenceTag` | 13 | column shell and evidence status taxonomy | Link to structured evidence ledger before promoting broader variants |
| 17 | `JByond/Deck/GanttDateTickExact`, `JByond/Deck/GanttLaneMetaExact`, `JByond/Deck/GanttTaskBarExact`, `JByond/Deck/GanttMilestoneExact` | 14 | date ticks, lane metadata, task bars, milestones | sets `85:875`, `86:885`, `88:987`, `89:813` promoted; slide 14 componentized clone `90:777` passes with similarity `0.9997048611` |

## Naming Rules

- Slide frame: `S01/Summary`, `S07/SystemFlow`, `S09/UserScenario`
- Section/layer prefix: `S07/Diagram/...`, `S09/Flow/...`
- Text layers: `Text/<purpose>`, not `Title 1`
- Image layers: `Image/<source-or-role>`
- Component variants: use `tone`, `size`, `align`, `state` only in pilot
- Do not detach instances unless a one-off visual exception is documented in `qa/rebuild-diff.md`.

## Build Order

1. `FrameDark`, `FooterMeta`, `SlideHeader`
2. `HeroWordmark`, `ProductShotLaptop` for `01`
3. System flow atoms (`FlowStageHeader`, `FlowNode`, `FlowConnector`, `EntityPill`) for `07`
4. `DarkTable` and `TableRow` for `07`
5. Scenario atoms (`ProcessNode`, `DecisionDiamond`, `ScenarioCard`) for `09`
6. Full-deck candidates only after source-preserving clone QA is locked
7. Compose slides from component instances

## Component Gate

반복 요소가 2회 이상 나오면 다음 중 하나여야 한다.

- Figma component instance
- documented local pattern with clear reason not to componentize
- image asset only when source is intentionally raster and not expected to be edited
