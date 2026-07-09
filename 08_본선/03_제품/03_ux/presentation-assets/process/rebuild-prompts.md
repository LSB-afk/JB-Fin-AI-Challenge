---
tags:
  - area/product
  - type/process
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Rebuild Prompts

## A5 Figma Builder Prompt - Setup

```text
You are A5 Figma Slide Builder.
Use only the editable duplicate Figma file. Do not mutate the original source file.
Create a page named "JByond Deck Assets / v1" with sections:
00 Foundations, 01 Components, 02 Pilot Slides, 99 References.
Build tokens and components according to presentation-assets/tokens/token-index.json, the split token files, and components/component-catalog.md.
Return all created node IDs. Do not create full-slide raster rebuilds.
```

## A5 Figma Builder Prompt - 01 Summary

```text
Use pasted editable source node 6:198 in h6RkEn7fGbTwZbzuwaHsWi as the source of truth.
Do not use the failed v0 node 5:2 as a visual target.
Create or update S01/Summary/Structured Rebuild v1.0 by preserving separate source layers, then add role-based names and jbyond shared metadata.
Use tokens/token-index.json, tokens/slides.json, tokens/assets.json, tokens/fonts.json, tokens/surfaces.json, and tokens/effects.json.
Required editable layers:
Asset/CoverStageImage, TextGroup/CoverHeader, Text/CoverEyebrow, Text/CoverStatement, Vector/HandAccent, Asset/ProductLaptopImage, Overlay/BottomVeilBase, Overlay/BottomVeilGradient, Text/FooterEvent, Text/FooterTeam, Text/HeroWordmark.
ProductName/HeroWordmark must remain editable text "JByond", not a raster image.
Return source node ID, rebuilt slide node ID, layer map, and screenshot.
```

## A6 Visual QA Prompt - 01 Summary

```text
Compare rebuilt S01/Summary against pasted editable source node 6:198 and assets/rebuild-screenshots/01-summary-source-6-198.png.
Use assets/source-screenshots/01-summary.jpg and the final PDF only as fallback/order references.
Check: 1920x1080, pixel diff, no full-slide raster, editable main text, layer map completeness, JByond overlap and scale, footer alignment, headline line breaks, laptop placement, no clipping, missing-font risk.
Write findings to qa/rebuild-diff.md with pass/fail and specific fixes.
```

## A5 Figma Builder Prompt - 07 System Flow

```text
Build slide S07/SystemFlow at 1920x1080.
Use pasted editable source node 6:325 as the source of truth. Use the local screenshot only as visual fallback.
The left system flow and right tables must be editable components/text, not one image.
Use components: SystemFlowPanel, FlowStageHeader, FlowNode, FlowConnector, EntityPill, DarkTable, TableRow.
Preserve source content including [제휴 TBD], but mark it as a QA risk.
Return rebuilt slide node ID and screenshot.
```

## A5 Figma Builder Prompt - 07 Componentized Rebuild

```text
Use structured baseline node 25:2 as the non-mutated visual source for slide 07.
Create a separate frame named S07/SystemFlow/Componentized Rebuild v1.x; do not overwrite source 6:325 or baseline 25:2.
Use SystemFlowTableExact/VariantSet 66:560 for the two right-side tables.
Use EntityPillExact/VariantSet 66:610 for the seven bottom entity pills.
Keep the main 6-stage flow columns, flow nodes, and connectors as cloned source layers until a narrower promotion loop verifies connector endpoint drift.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 68:508, similarity 0.9995273920, visual diff qa/visual-diff/07-system-flow-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 09 User Scenario

```text
Build slide S09/UserScenario at 1920x1080.
Use pasted editable source node 6:1046 as the source of truth. Use the local screenshot only as visual fallback.
Process flow must be editable vector/text. Story-card images may be raster fills until original sources are extracted.
Use components: SectionBadge, ProcessNode, DecisionDiamond, BranchGroup, ScenarioCard, FooterMeta.
Return rebuilt slide node ID and screenshot.
```

## A5 Figma Builder Prompt - 09 Componentized Rebuild

```text
Use structured baseline node 26:2 as the non-mutated visual source for slide 09.
Create a separate frame named S09/UserScenario/Componentized Rebuild v1.x; do not overwrite source 6:1046 or baseline 26:2.
Use ScenarioProcessNodeExact/VariantSet 63:520 for the ten workflow and branch nodes.
Use ScenarioCardExact/VariantSet 63:537 for the four story cards.
Keep the decision diamond, connector arrows, headline, background, and use-case label as cloned source layers until a narrower promotion loop verifies connector endpoint drift and text fidelity.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 64:490, similarity 1.0000000000, visual diff qa/visual-diff/09-user-scenario-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - Full Deck Clone Baseline

```text
Use the pasted editable source frames in h6RkEn7fGbTwZbzuwaHsWi Page 1 as the source of truth.
Create source-preserving structured clones for the remaining slides only. Do not redraw, flatten, or mutate text/font properties.
For each clone, set a role-based root name using S##/<Role>/Structured Rebuild v1.0 and return source node ID, rebuilt node ID, placement, size, and child count.
After clone creation, A6 must verify all source/rebuild pairs are 1920x1080, preserve child counts, and pass either full PNG byte-equal export or screenshot pixel diff at >= 0.98 similarity.
Slides 01,02,03,04,07,08,09,10,11,12,13,14 now have accepted componentized rebuilds above the 98% visual gate. Slides 05 and 06 remain source-preserving structured baselines because whole-frame or lightweight subtree reads returned HTTP 504.
```

## A6 Visual QA Prompt - Full Deck Clone Baseline

```text
Compare all 14 pasted source frames with their structured rebuild frames.
Primary gate: source and rebuild are both 1920x1080, same frame type, same child count, no full-slide flattening introduced by the rebuild.
For full PNG byte-equal pairs, record byte count and hash.
For byte-mismatch pairs, download full 1920x1080 screenshots and compute visible pixel diff, similarity, bbox, and screenshot SHA-256.
Write the summary to qa/visual-diff/full-deck-structured-audit-2026-07-09.json and qa/rebuild-diff.md.
```

## A5 Figma Builder Prompt - 02 Componentized Rebuild

```text
Use structured baseline node 28:2 as the non-mutated visual source for slide 02.
Create a separate frame named S02/ProblemDefinition/Componentized Rebuild v1.x; do not overwrite source 6:3 or baseline 28:2.
Replace only one repeated family at a time with component instances, then run full-slide screenshot diff.
Use ProblemCaseCard/VariantSet 39:77 for the five case cards.
Use LimitationRowExact/VariantSet 48:88 for the existing-approach rows when visual fidelity matters; keep broad LimitationRow/VariantSet 42:17 for general reuse/documentation.
Do not mutate text/font properties while Panchang/Pretendard are unavailable in the Figma Plugin runtime.
Accepted current baseline: node 49:76, similarity 0.9997815394, visual diff qa/visual-diff/02-problem-componentized-v1.2.json.
```

## A5 Figma Builder Prompt - 04 Componentized Rebuild

```text
Use structured baseline node 28:108 as the non-mutated visual source for slide 04.
Create a separate frame named S04/SolutionOverview/Componentized Rebuild v1.x; do not overwrite source 6:210 or baseline 28:108.
Keep the right-side product screenshot as the original raster asset at this stage.
Use SolutionAxisColumnExact/VariantSet 53:174 for the three 계열사/역할/케이스 columns.
Use SolutionFlowStepExact/VariantSet 53:184 for the three flow pills: AI Agent 정리, 담당자 확인, 다음 역할 전달.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 54:150, similarity 0.9999657600, visual diff qa/visual-diff/04-solution-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 03 Componentized Rebuild

```text
Use structured baseline node 28:95 as the non-mutated visual source for slide 03.
Create a separate frame named S03/ProblemEvidence/Componentized Rebuild v1.x; do not overwrite source 6:313 or baseline 28:95.
Use EvidenceScreenshotExact/VariantSet 58:175 for the two evidence screenshot image fills.
Use EvidenceHighlightExact/VariantSet 58:182 for the three blue highlight overlay rectangles.
Keep the headline, body text, and Problem Definition badge as cloned editable source text layers.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 58:183, similarity 1.0000000000, visual diff qa/visual-diff/03-problem-evidence-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 08 Componentized Rebuild

```text
Use structured baseline node 28:211 as the non-mutated visual source for slide 08.
Create a separate frame named S08/AIOrgChart/Componentized Rebuild v1.x; do not overwrite source 6:592 or baseline 28:211.
Use OrgRoleNodeCompactExact/VariantSet 60:372 for the fourteen 256x94 organization role cards.
Use OrgRoleNodeTallExact/VariantSet 60:505 for the twelve 256x117 organization role cards.
Use OrgGateNodeExact/VariantSet 60:550 for the three top approval/coordination cards.
Keep connector arrows and the bottom-right 운영 에이전트 panel as cloned source layers until a narrower promotion loop verifies endpoint drift.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 61:176, similarity 0.9999146412, visual diff qa/visual-diff/08-ai-org-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 10 Componentized Rebuild

```text
Use structured baseline node 29:2 as the non-mutated visual source for slide 10.
Create a separate frame named S10/ExpectedEffects/Componentized Rebuild v1.x; do not overwrite source 6:96 or baseline 29:2.
Use ExperienceNodeExact/VariantSet 70:659 for the five TX/AX/UX/EX-PX/CX experience map nodes.
Keep arrows, the left headline, bottom-left material group, and dense value-chain panel as cloned source layers until a narrower promotion loop verifies text reflow and connector drift.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 70:660, similarity 0.9987331211, visual diff qa/visual-diff/10-effects-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 11 Componentized Rebuild

```text
Use structured baseline node 29:104 as the non-mutated visual source for slide 11.
Create a separate frame named S11/ImplementationDemoPlan/Componentized Rebuild v1.x; do not overwrite source 6:1108 or baseline 29:104.
Use MvpChecklistRowExact/VariantSet 72:661 for the four 완료된 MVP rows.
Use DemoPlanRowExact/VariantSet 72:697 for the five 시연 계획 row pairs.
Keep the background, header badge, headline paragraph, and column titles as cloned source layers until a narrower promotion loop verifies text reflow.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 74:649, similarity 0.9999122299, visual diff qa/visual-diff/11-demo-plan-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 12 Componentized Rebuild

```text
Use structured baseline node 29:151 as the non-mutated visual source for slide 12.
Create a separate frame named S12/ClosingExpansion/Componentized Rebuild v1.x; do not overwrite source 6:983 or baseline 29:151.
Use ExperienceBenefitBubbleExact/VariantSet 75:690 for the three AX/EX/CX benefit bubbles.
Use ExpansionStepExact/VariantSet 75:703 for the four right-side expansion step labels.
Keep the large orbit vector system, center list, closing statement, bottom badge, and today arrow as cloned source layers until a narrower loop verifies z-order and text-line drift.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 77:678, similarity 0.9999541860, visual diff qa/visual-diff/12-expansion-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 13 Componentized Rebuild

```text
Use structured baseline node 29:214 as the non-mutated visual source for slide 13.
Create a separate frame named S13/AppendixReferences/Componentized Rebuild v1.x; do not overwrite source 6:1586 or baseline 29:214.
Use ReferenceItem2LineExact/VariantSet 79:736 for the twelve 2-line reference rows.
Use ReferenceItem3LineExact/VariantSet 79:832 for the nineteen 3-line reference rows.
Use VerificationSummaryRowExact/VariantSet 79:849 for the four verification summary rows.
Keep the header, column shells, section labels, caveat note, and verification box shell as cloned source layers.
Split the reference rows by line count because a single 31-row variant set exceeds the 30-variant cap.
Accepted current baseline: node 80:688, similarity 1.0000000000, visual diff qa/visual-diff/13-appendix-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 14 Componentized Rebuild

```text
Use structured baseline node 29:357 as the non-mutated visual source for slide 14.
Create a separate frame named S14/AppendixGantt/Componentized Rebuild v1.x; do not overwrite source 6:1155 or baseline 29:357.
Use GanttDateTickExact/VariantSet 85:875 for the fourteen date labels plus vertical grid-line pairs.
Use GanttLaneMetaExact/VariantSet 86:885 for the nine lane shells and left-side metadata groups.
Use GanttTaskBarExact/VariantSet 88:987 for the twenty-one timeline task bars; each instance contains the rounded bar background and three text rows.
Use GanttMilestoneExact/VariantSet 89:813 for the six colored milestone lines plus bottom labels.
Keep the header note, footer legend, and footer evidence/source box as cloned source layers unless later decks repeat the footer pattern.
Do not mutate text/font properties while Pretendard/Panchang are unavailable in the Figma Plugin runtime.
Accepted current baseline: node 90:777, similarity 0.9997048611, visual diff qa/visual-diff/14-gantt-componentized-v1.0.json.
```

## A5 Figma Builder Prompt - 01 Componentized Rebuild

```text
Use structured baseline node 22:2 as the non-mutated visual source for slide 01.
Create a separate frame named S01/Summary/Componentized Rebuild v1.x; do not overwrite source 6:198 or baseline 22:2.
Use CoverMediaStackExact 92:1179 for the stage image, laptop image, hand accent, and bottom veil overlays.
Use CoverHeaderExact 92:1188 for the eyebrow and headline group.
Use CoverFooterExact 92:1189 for the event/team footer pair.
Use CoverWordmarkExact 92:1192 for the Panchang JByond wordmark.
Do not mutate text/font properties while Pretendard/Panchang are unavailable in the Figma Plugin runtime; preserve cloned source text metadata.
Use tolerance-aware QA for Figma instance rendering quantization: exact-pixel deltas with maxChannelDelta <= 1 are accepted when there is no visible layout drift.
Accepted current baseline: node 93:1179, tolerance-aware similarity 1.0000000000, maxChannelDelta 1, visual diff qa/visual-diff/01-summary-componentized-v1.0.json.
```

## A1/A5 Retry Note - 05 Key Feature UI

```text
Do not retry full subtree reads on slide 05 frame 6:261 or baseline 28:159. On 2026-07-09 these returned HTTP 504 repeatedly, including a minimal direct-child read.
Single-node get_metadata now works for `6:262` through `6:284` except `6:285`; bundled use_figma loops over the same ID range still returned HTTP 504.
Retry only with one-node metadata probes and narrowly scoped write calls. Avoid `6:285` until it can be manually selected or isolated.
Accepted componentized baseline: node `98:1189`, similarity `1.0000000000`, visual diff `qa/visual-diff/05-key-feature-ui-componentized-v1.0.json`.
Promoted components: `FeatureCalloutTopExact/VariantSet` node `95:1197` for `CaseBoard`/`RiskSignal`, and `FeatureCalloutRightExact/VariantSet` node `96:1195` for `AgentRun`/`EvidencePack`.
Only promote additional connector vectors in a separate connector-only loop if reuse value justifies the endpoint-drift risk.
```

## A5 Figma Builder Prompt - 05 Partial Componentized Rebuild

```text
Use known Slide 05 child IDs only. Do not traverse source frame 6:261 or structured baseline 28:159, because full-frame reads repeatedly returned HTTP 504.
Create a separate frame named S05/KeyFeatureUI/Componentized Rebuild v1.x; do not overwrite source 6:261 or baseline 28:159.
Keep the product UI screenshot composite from 6:262 as the raster-allowed product shot.
Use FeatureCalloutTopExact/VariantSet 95:1197 for the CaseBoard and RiskSignal callout labels.
Use FeatureCalloutRightExact/VariantSet 96:1195 for the AgentRun and EvidencePack callout labels.
Preserve connector vectors from 6:269, 6:270, 6:281, 6:282, and 6:283 as exact cloned layers unless promoted in a separate connector-only loop.
Avoid unresolved node 6:285 until it can be manually selected or isolated.
Do not mutate text/font properties while Pretendard is unavailable in the Figma Plugin runtime.
Accepted current baseline: node 98:1189, similarity 1.0000000000, visual diff qa/visual-diff/05-key-feature-ui-componentized-v1.0.json.
```

## A1/A5 Retry Note - 06 Key Feature Approval

```text
Do not retry full subtree reads on slide 06 frame 6:286 or baseline 28:184. On 2026-07-09 a lightweight source+baseline child read and get_metadata on 28:184 returned HTTP 504.
Accepted componentized baseline: node `101:1206`, similarity `1.0000000000`, visual diff `qa/visual-diff/06-key-feature-approval-componentized-v1.0.json`.
Promoted component: `ApprovalAuditCalloutExact/VariantSet` node `101:1205` for `L0L4Gate` and `AuditLogAgent`.
Do not direct-read timeout-prone node `6:304` until it can be manually isolated.
Only promote approval queue/report viewer internals if future decks require those console-shot areas to be editable.
```
