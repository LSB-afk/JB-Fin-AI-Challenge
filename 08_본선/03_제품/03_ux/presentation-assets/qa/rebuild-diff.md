---
tags:
  - area/product
  - type/qa
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Rebuild Diff And QA Loop

## Current QA State

| Slide | Source screenshot | Rebuild screenshot | Status | Notes |
|---|---|---|---|---|
| 01 Summary | Pasted editable source `6:198`; `assets/rebuild-screenshots/01-summary-source-6-198.png` | Componentized rebuild `93:1179`; `assets/rebuild-screenshots/01-summary-componentized-93-1179.png` | `componentized_rebuild_v1_pass_tolerance_delta_le_1` | `5:2` remains a failed experiment. `22:2` is the pixel-identical structured baseline. `93:1179` uses four component instances; max channel delta is `1`, tolerance-aware changed pixels `0 / 2,073,600`, similarity `1.0000000000`. |
| 07 System Flow | Pasted editable source `6:325`; `assets/rebuild-screenshots/07-system-flow-source-6-325.png` | Structured rebuild `25:2`; `assets/rebuild-screenshots/07-system-flow-structured-25-2.png` | `structured_rebuild_v1_pass_99_9753_percent_similarity` | Source clone with role-based layer names. Pixel diff: `512 / 2,073,600`, similarity `0.9997530864`. Tiny right-table-region render delta remains as a polish-loop candidate. |
| 09 User Scenario | Pasted editable source `6:1046`; `assets/rebuild-screenshots/09-user-scenario-source-6-1046.png` | Structured rebuild `26:2`; `assets/rebuild-screenshots/09-user-scenario-structured-26-2.png` | `structured_rebuild_v1_pixel_identical_to_pasted_source` | Process nodes, connectors, decision branch, use-case label, four story cards, and captions are preserved as separate editable/raster-allowed layers. Pixel diff: `0 / 2,073,600`, similarity `1.0000000000`. |

## Full Deck Structured Clone Audit

Full audit JSON: `qa/visual-diff/full-deck-structured-audit-2026-07-09.json`

All 14 source-preserving structured clones pass the `>= 0.98` visual gate. Minimum measured similarity is `0.9996238426` on slide `14`.

| Slide | Source | Rebuild | QA method | Changed pixels | Similarity | Status |
|---:|---|---|---|---:|---:|---|
| 01 | `6:198` | `22:2` | full screenshot pixel diff | `0` | `1.0000000000` | pass; deep taxonomy done |
| 02 | `6:3` | `28:2` | full screenshot pixel diff | `41` | `0.9999802276` | pass; deep taxonomy pending |
| 03 | `6:313` | `28:95` | Figma full PNG byte-equal export | `0` | `1.0000000000` | pass; deep taxonomy pending |
| 04 | `6:210` | `28:108` | full screenshot pixel diff | `10` | `0.9999951775` | pass; deep taxonomy pending |
| 05 | `6:261` | `28:159` | Figma full PNG byte-equal export | `0` | `1.0000000000` | pass; deep taxonomy pending |
| 06 | `6:286` | `28:184` | Figma full PNG byte-equal export | `0` | `1.0000000000` | pass; deep taxonomy pending |
| 07 | `6:325` | `25:2` | full screenshot pixel diff | `512` | `0.9997530864` | pass; deep taxonomy done |
| 08 | `6:592` | `28:211` | full screenshot pixel diff | `1` | `0.9999995177` | pass; deep taxonomy pending |
| 09 | `6:1046` | `26:2` | full screenshot pixel diff | `0` | `1.0000000000` | pass; deep taxonomy done |
| 10 | `6:96` | `29:2` | full screenshot pixel diff | `617` | `0.9997024498` | pass; deep taxonomy pending |
| 11 | `6:1108` | `29:104` | full screenshot pixel diff | `356` | `0.9998283179` | pass; deep taxonomy pending |
| 12 | `6:983` | `29:151` | full screenshot pixel diff | `2` | `0.9999990355` | pass; deep taxonomy pending |
| 13 | `6:1586` | `29:214` | Figma full PNG byte-equal export | `0` | `1.0000000000` | pass; deep taxonomy pending |
| 14 | `6:1155` | `29:357` | full screenshot pixel diff | `780` | `0.9996238426` | pass; Gantt componentization done |

Scope note: all 14 slides now have at least one accepted componentized rebuild loop above the 98% visual gate. Some dense one-off regions remain cloned source layers by design; deeper atomization is optional follow-up work, not visual parity work.

## 01 Summary Componentized Rebuild

Slide `01` now has a cover-specific componentized rebuild. The source `6:198` and structured baseline `22:2` were not mutated.

| Version | Figma node | Components | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `93:1179` | `92:1179`, `92:1188`, `92:1189`, `92:1192` | tolerance-aware `0`; exact-pixel `923,512` with max delta `1` | tolerance-aware `1.0000000000` | Accepted as current componentized slide 01 baseline. Exact-pixel drift is a Figma instance rendering quantization artifact, not visible layout drift. |

QA files:

- `qa/visual-diff/01-summary-componentized-v1.0.json`
- `assets/rebuild-screenshots/01-summary-componentized-93-1179.png`
- `assets/components/cover-media-stack-exact-92-1179.png`
- `assets/components/cover-header-exact-92-1188.png`
- `assets/components/cover-footer-exact-92-1189.png`
- `assets/components/cover-wordmark-exact-92-1192.png`

Interpretation: the cover is reusable as a four-instance composition while preserving the source look. Text was cloned without mutation because `Pretendard` is not available to the plugin runtime; install/enable Pretendard before retyping or changing header/footer text through Figma automation.

## 02 Problem Definition Componentized Rebuild

Slide `02` now has a separate componentized rebuild loop. The original source `6:3` and structured baseline `28:2` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.1 | `46:2` | `39:77`, `42:17` | `12,689` | `0.9938806906` | Passed 98% gate, but rejected as final because the broad `LimitationRow` component shifted row text/arrow geometry. |
| v1.2 | `49:76` | `39:77`, `48:88` | `453` | `0.9997815394` | Accepted as current componentized slide 02 baseline. |

QA files:

- `qa/visual-diff/02-problem-componentized-v1.1.json`
- `qa/visual-diff/02-problem-componentized-v1.2.json`
- `assets/rebuild-screenshots/02-problem-componentized-49-76.png`

Interpretation: replacing repeated visual families with component instances is viable, but only when the promoted component preserves exact source geometry. For text-heavy rows, an exact-geometry component can be preferable to a broader auto-layout-friendly component until fonts are available in the Figma runtime.

## 03 Problem Evidence Componentized Rebuild

Slide `03` now has a separate componentized rebuild. The source `6:313` and structured baseline `28:95` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `58:183` | `58:175`, `58:182` | `0` | `1.0000000000` | Accepted as current componentized slide 03 baseline. |

QA files:

- `qa/visual-diff/03-problem-evidence-componentized-v1.0.json`
- `assets/rebuild-screenshots/03-problem-evidence-componentized-58-183.png`
- `assets/components/evidence-screenshot-exact-variant-set-58-175.png`
- `assets/components/evidence-highlight-exact-variant-set-58-182.png`

Interpretation: raster evidence captures can be assetized as exact-source image-fill components while keeping overlay highlights as editable component instances. This preserves source fidelity and still makes the evidence-slide pattern reusable.

## 04 Solution Overview Componentized Rebuild

Slide `04` now has a separate componentized rebuild. The source `6:210` and structured baseline `28:108` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `54:150` | `53:174`, `53:184` | `71` | `0.9999657600` | Accepted as current componentized slide 04 baseline. |

QA files:

- `qa/visual-diff/04-solution-componentized-v1.0.json`
- `assets/rebuild-screenshots/04-solution-componentized-54-150.png`

Interpretation: the axis-column group and flow-step pills can be replaced with exact-geometry component instances without meaningful visual drift. The right-side product screenshot remains the original raster asset, which is intentional for this stage.

## 05 Key Feature UI Componentized Rebuild

Slide `05` now has a full-slide componentized rebuild. The build did not direct-read unresolved node `6:285`; it cloned the verified structured baseline `28:159`, hid the original callout label layers, and placed promoted callout component instances at exact source coordinates.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `98:1189` | `95:1197`, `96:1195` | `0` | `1.0000000000` | Accepted as current componentized slide 05 baseline. |

| Component set | Figma node | Source nodes | Variants | Decision |
|---|---|---|---|---|
| `JByond/Deck/FeatureCalloutTopExact/VariantSet` | `95:1197` | `6:271`, `6:274` | `CaseBoard`, `RiskSignal` | Used in `98:1189`. |
| `JByond/Deck/FeatureCalloutRightExact/VariantSet` | `96:1195` | `6:277`, `6:279`, `6:278`, `6:280` | `AgentRun`, `EvidencePack` | Used in `98:1189`. |

QA files:

- `qa/visual-diff/05-key-feature-ui-componentized-v1.0.json`
- `qa/visual-diff/05-key-feature-ui-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/05-key-feature-ui-source-6-261.png`
- `assets/rebuild-screenshots/05-key-feature-ui-componentized-98-1189.png`
- `assets/components/feature-callout-top-exact-variant-set-95-1197.png`
- `assets/components/feature-callout-right-exact-variant-set-96-1195.png`

Interpretation: the product UI screenshot remains raster-allowed while the four callout labels are component instances. Connector vectors remain cloned source layers; promote them only in a separate connector-only loop if reuse value justifies the endpoint-drift risk.

## 06 Key Feature Approval Componentized Rebuild

Slide `06` now has a full-slide componentized rebuild. The build did not direct-read timeout-prone node `6:304`; it cloned the verified structured baseline `28:184`, hid the original approval/audit callout frames, and placed promoted callout component instances at exact source coordinates.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `101:1206` | `101:1205` | `0` | `1.0000000000` | Accepted as current componentized slide 06 baseline. |

| Component set | Figma node | Source nodes | Variants | Decision |
|---|---|---|---|---|
| `JByond/Deck/ApprovalAuditCalloutExact/VariantSet` | `101:1205` | `6:309`, `6:305` | `L0L4Gate`, `AuditLogAgent` | Used in `101:1206`. |

QA files:

- `qa/visual-diff/06-key-feature-approval-componentized-v1.0.json`
- `qa/visual-diff/06-key-feature-approval-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/06-key-feature-approval-source-6-286.png`
- `assets/rebuild-screenshots/06-key-feature-approval-componentized-101-1206.png`
- `assets/components/approval-audit-callout-exact-variant-set-101-1205.png`

Interpretation: the main approval queue/report viewer UI remains raster-allowed product material while the two explanatory callouts are reusable component instances. Promote internal console-shot cards only if future decks require editing those UI internals.

## 07 System Flow Componentized Rebuild

Slide `07` now has a separate componentized rebuild. The source `6:325` and structured baseline `25:2` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `68:508` | `66:560`, `66:610` | `980` | `0.9995273920` | Accepted as current componentized slide 07 baseline. |

QA files:

- `qa/visual-diff/07-system-flow-componentized-v1.0.json`
- `assets/rebuild-screenshots/07-system-flow-componentized-68-508.png`
- `assets/components/system-flow-table-exact-variant-set-66-560.png`
- `assets/components/entity-pill-exact-variant-set-66-610.png`

Interpretation: the right-side tables and bottom entity rail can be replaced with exact component instances while staying above 99.95% similarity. The main 6-stage flow columns and connectors remain cloned source layers until a narrower endpoint-drift loop promotes them.

## 08 AI Org Chart Componentized Rebuild

Slide `08` now has a separate componentized rebuild. The source `6:592` and structured baseline `28:211` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `61:176` | `60:372`, `60:505`, `60:550` | `177` | `0.9999146412` | Accepted as current componentized slide 08 baseline. |

QA files:

- `qa/visual-diff/08-ai-org-componentized-v1.0.json`
- `assets/rebuild-screenshots/08-ai-org-componentized-61-176.png`
- `assets/components/org-role-node-compact-exact-variant-set-60-372.png`
- `assets/components/org-role-node-tall-exact-variant-set-60-505.png`
- `assets/components/org-gate-node-exact-variant-set-60-550.png`

Interpretation: the main org-card families can be replaced with exact component instances while remaining above 99.99% similarity. Connector arrows and the bottom-right operations panel remain cloned source layers for now.

## 09 User Scenario Componentized Rebuild

Slide `09` now has a separate componentized rebuild. The source `6:1046` and structured baseline `26:2` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `64:490` | `63:520`, `63:537` | `0` | `1.0000000000` | Accepted as current componentized slide 09 baseline. |

QA files:

- `qa/visual-diff/09-user-scenario-componentized-v1.0.json`
- `assets/rebuild-screenshots/09-user-scenario-componentized-64-490.png`
- `assets/components/scenario-process-node-exact-variant-set-63-520.png`
- `assets/components/scenario-card-exact-variant-set-63-537.png`

Interpretation: workflow/branch nodes and story cards can be promoted to exact component instances without any visible drift. The decision diamond, connectors, headline, and background remain cloned source layers for this loop because they are either one-off or endpoint-sensitive.

## 10 Expected Effects Componentized Rebuild

Slide `10` now has a separate componentized rebuild. The source `6:96` and structured baseline `29:2` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `70:660` | `70:659` | `2,627` | `0.9987331211` | Accepted as current componentized slide 10 baseline. |

QA files:

- `qa/visual-diff/10-effects-componentized-v1.0.json`
- `qa/visual-diff/10-effects-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/10-effects-componentized-70-660.png`
- `assets/components/experience-node-exact-variant-set-70-659.png`

Interpretation: the five TX/AX/UX/EX-PX/CX experience map nodes can be promoted to exact component instances while staying above 99.87% similarity. Arrows, the dense value-chain text panel, left headline, and bottom-left material group remain cloned source layers until a narrower drift check promotes them safely.

## 11 Implementation Demo Plan Componentized Rebuild

Slide `11` now has a separate componentized rebuild. The source `6:1108` and structured baseline `29:104` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `74:649` | `72:661`, `72:697` | `182` | `0.9999122299` | Accepted as current componentized slide 11 baseline. |

QA files:

- `qa/visual-diff/11-demo-plan-componentized-v1.0.json`
- `qa/visual-diff/11-demo-plan-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/11-demo-plan-componentized-74-649.png`
- `assets/components/mvp-checklist-row-exact-variant-set-72-661.png`
- `assets/components/demo-plan-row-exact-variant-set-72-697.png`

Interpretation: the repeated completed-MVP rows and demo-plan row pairs can be promoted to exact component instances while staying above 99.99% similarity. Background, header badge, headline paragraph, and column headings remain cloned source layers for this loop because they are one-off or line-break-sensitive.

## 12 Closing Expansion Componentized Rebuild

Slide `12` now has a separate componentized rebuild. The source `6:983` and structured baseline `29:151` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `77:678` | `75:690`, `75:703` | `95` | `0.9999541860` | Accepted as current componentized slide 12 baseline. |

QA files:

- `qa/visual-diff/12-expansion-componentized-v1.0.json`
- `qa/visual-diff/12-expansion-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/12-expansion-componentized-77-678.png`
- `assets/components/experience-benefit-bubble-exact-variant-set-75-690.png`
- `assets/components/expansion-step-exact-variant-set-75-703.png`

Interpretation: the AX/EX/CX benefit bubbles and four right-side expansion step labels can be promoted to exact component instances while staying above 99.99% similarity. The large orbit vector system, center list, closing statement, and `오늘` arrow remain cloned source layers for this loop because z-order and line-break drift would be more visible than their current reuse gain.

## 13 Appendix References Componentized Rebuild

Slide `13` now has a separate componentized rebuild. The source `6:1586` and structured baseline `29:214` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `80:688` | `79:736`, `79:832`, `79:849` | `0` | `1.0000000000` | Accepted as current componentized slide 13 baseline. |

QA files:

- `qa/visual-diff/13-appendix-componentized-v1.0.json`
- `qa/visual-diff/13-appendix-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/13-appendix-componentized-80-688.png`
- `assets/components/reference-item-2line-exact-variant-set-79-736.png`
- `assets/components/reference-item-3line-exact-variant-set-79-832.png`
- `assets/components/verification-summary-row-exact-variant-set-79-849.png`

Interpretation: all repeated appendix reference rows and verification-summary rows can be promoted to exact component instances with byte-identical visual output. The 31 reference rows are split into 2-line and 3-line sets to keep each variant set below the 30-variant cap.

## 14 Appendix Gantt Componentized Rebuild

Slide `14` now has a separate componentized rebuild. The source `6:1155` and structured baseline `29:357` were not mutated.

| Version | Figma node | Component sets | Changed pixels vs source | Similarity | Decision |
|---|---|---|---:|---:|---|
| v1.0 | `90:777` | `85:875`, `86:885`, `88:987`, `89:813` | `612` | `0.9997048611` | Accepted as current componentized slide 14 baseline. |

QA files:

- `qa/visual-diff/14-gantt-componentized-v1.0.json`
- `qa/visual-diff/14-gantt-componentized-v1.0-diff.png`
- `assets/rebuild-screenshots/14-gantt-componentized-90-777.png`
- `assets/components/gantt-date-tick-exact-variant-set-85-875.png`
- `assets/components/gantt-lane-meta-exact-variant-set-86-885.png`
- `assets/components/gantt-task-bar-exact-variant-set-88-987.png`
- `assets/components/gantt-milestone-exact-variant-set-89-813.png`

Interpretation: the dense Gantt chart can be componentized without visible rebuild drift when exact source geometry is preserved. Fourteen date ticks, nine lane metadata rows, twenty-one task bars, and six milestone markers are component instances. The footer legend/evidence box remains cloned source layers because it is a one-off metadata panel unless later decks repeat the pattern.

## 05 Figma Read Issue

On 2026-07-09, slide `05` source/baseline subtree inspection failed three times with `HTTP 504`, including one full subtree read, one metadata read, and one minimal direct-child read. Current decision: keep the source-preserving baseline and local exported composite for slide `05` until smaller child IDs can be isolated manually or via selection.

## 06 Figma Read Issue

On 2026-07-09, slide `06` source/baseline subtree inspection also failed with `HTTP 504`. The failed paths were a lightweight source+baseline child read for `6:286` / `28:184` and `get_metadata` on `28:184`. Current decision: do not retry full slide or whole-subtree reads; use selected child IDs or manually isolated smaller nodes for callouts and product-panel regions.

## PDF Order Baseline

Final PDF order has been checked in `qa/pdf-order-check.md`. PDF pages 1, 7, and 9 match the selected pilot slides, and the full 1-14 sequence matches the local Figma JPG export order.

## Access State

Previous Figma tools returned:

```text
Looks like you don't have edit access to this file. The file owner can share it with you and make you an editor.
```

Re-check on 2026-07-08 shows the connector is now authenticated as a `Full` seat account with access to `팀 망상궤도`. Source file metadata and read-only `use_figma` context access succeeded. A fresh rebuild workspace has been created at `https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`.

On 2026-07-08 the user pasted the working original slide frames into that workspace. Page 1 now contains the full 14-slide sequence as `6:*` nodes. For the pilot, use:

- `01 Summary`: `6:198`
- `07 데이터 및 활용 기술`: `6:325`
- `09 User Scenario`: `6:1046`

Local screenshots from these pasted nodes are stored under `assets/pasted-working-screenshots/`.

## 01 Summary Structured Rebuild V1

| Metric | Value |
|---|---|
| Source Figma node | `6:198` |
| Rebuild Figma node | `22:2` |
| Rebuild name | `S01/Summary/Structured Rebuild v1.0` |
| Source export | `assets/rebuild-screenshots/01-summary-source-6-198.png` |
| Rebuild export | `assets/rebuild-screenshots/01-summary-structured-22-2.png` |
| Export size | `1920x1080` |
| Changed pixels | `0` |
| Total pixels | `2,073,600` |
| Changed ratio | `0.0000000000` |
| Similarity | `1.0000000000` |
| RMS RGBA normalized | `0.0000000000` |
| Diff bbox | `None` |
| Screenshot SHA-256 | both `6ada89581dc01b4f247661a4caffe9b08c6e89625af6ecb8c75a13d5a8337b5f` |

Layer structure is not a full-slide raster. The clone preserves separate source layers: background image, header text group, vector accent, laptop image, two veil overlays, two footer text nodes, and editable `Panchang` wordmark text.

Font caveat: Figma Plugin API still reports `hasMissingFont: true` on `Pretendard` and `Panchang` text nodes. The current clone is visually identical because it preserves the pasted source text nodes without mutating text properties. Future text edits require font activation/install before final pass.

## 07 System Flow Structured Rebuild V1

| Metric | Value |
|---|---|
| Source Figma node | `6:325` |
| Rebuild Figma node | `25:2` |
| Rebuild name | `S07/SystemFlow/Structured Rebuild v1.0` |
| Source export | `assets/rebuild-screenshots/07-system-flow-source-6-325.png` |
| Rebuild export | `assets/rebuild-screenshots/07-system-flow-structured-25-2.png` |
| Export size | `1920x1080` |
| Changed pixels | `512` |
| Total pixels | `2,073,600` |
| Changed ratio | `0.0002469136` |
| Similarity | `0.9997530864` |
| RMS RGBA normalized | `0.0010272472` |
| Diff bbox | `[1409, 436, 1676, 672]` |
| Source SHA-256 | `e3468452db04c1771cfec39bc7b22b195282ccd3283ea66a735bf9fa3dce99cf` |
| Rebuild SHA-256 | `e345c94a1400281e04bd6f915f2504116b079f86d5b28e3dfba8339e3586631e` |

Layer structure is not a full-slide raster. The clone preserves separate source layers for header text, right-side data/technology tables, diagram panel, diagram title, flow group, entity rail, connectors, and security-risk legend.

Remaining delta: the diff bbox is in the right table area and affects only 512 pixels. This exceeds the requested 98% loop target, but it remains a candidate for a zero-diff polish loop.

## 09 User Scenario Structured Rebuild V1

| Metric | Value |
|---|---|
| Source Figma node | `6:1046` |
| Rebuild Figma node | `26:2` |
| Rebuild name | `S09/UserScenario/Structured Rebuild v1.0` |
| Source export | `assets/rebuild-screenshots/09-user-scenario-source-6-1046.png` |
| Rebuild export | `assets/rebuild-screenshots/09-user-scenario-structured-26-2.png` |
| Export size | `1920x1080` |
| Changed pixels | `0` |
| Total pixels | `2,073,600` |
| Changed ratio | `0.0000000000` |
| Similarity | `1.0000000000` |
| RMS RGBA normalized | `0.0000000000` |
| Diff bbox | `None` |
| Screenshot SHA-256 | both `7b3218ece6438d6c8a8bfa9be2c5396cf0833deedca503c6384254f9a60df2de` |

Layer structure is not a full-slide raster. The clone preserves separate source layers for the background image, header badge/headline, process nodes, decision diamond, branch nodes, connectors, use-case label, four card image fills, and four editable captions.

## Pass / Fail Criteria

### Slide Gate

PASS when:

- Export size is `1920x1080`.
- Text is editable, not baked into a full-slide raster.
- Repeated elements use components or documented patterns.
- No visible text clipping, overlap, or accidental crop.
- Footer/page number are present and aligned.

FAIL when:

- Rebuilt slide is a single full-slide raster image.
- Any core message text is missing.
- Main visual asset is replaced by unrelated or lower-quality imagery.
- Diagram/table text becomes unreadable at presentation scale.

### Token Gate

PASS when:

- Main colors, typography, radius, shadow, spacing are documented in split machine-readable token files under `tokens/token-index.json`.
- Any hardcoded exception is listed in this QA file.

FAIL when:

- Visual rebuild uses untracked colors/effects.
- Typography differs from source but no rationale is recorded.

### Component Gate

PASS when:

- `01` uses editable `HeroWordmark`, `SlideHeader`, `FooterMeta`.
- `07` uses flow/table components rather than a flat diagram image.
- `09` uses reusable process/story-card components.

FAIL when:

- Any 2+ repeated element is rebuilt manually without a documented reason.

## Iteration Log

| Iteration | Slide | Action | Result | Next |
|---|---|---|---|---|
| 0 | all | Local screenshots copied and source analysis created | Ready for Figma duplicate | Provide editable duplicate URL |
| 0.1 | all | Final PDF order checked against local Figma JPG order | PDF order is baseline; exact embedded JPEG SHA differs due recompression | Use `qa/pdf-order-check.md` for sequence |
| 0.2 | all | Figma account permission checked | Connected account has `View` seat; A5 cannot create/edit Figma file | Provide editor-capable duplicate/workspace |
| 0.3 | all | Figma permission re-checked via `@figma` plugin | Connected account has `Full` seat; source file metadata and pilot node metadata are accessible | Create/provide editable duplicate, then build `01 Summary` |
| 0.4 | all | Fresh rebuild workspace created | `https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi` | Continue in fresh workspace unless true duplicate URL is provided |
| 0.5 | foundations | Page skeleton, variables, text styles, effect styles, token specimen created | Figma runtime exposes Inter only; source font names preserved in style descriptions | Resolve Pretendard/Panchang availability before final polish |
| 1 | 01 | Editable rebuild v0 created as `5:2` | 1920x1080 frame with editable text and structured mockup placeholder | Run visual diff and replace placeholders with closer assets/components |
| 1.1 | 01 | User reported that v0 looked materially different from the original | Confirmed. Main causes: placeholder images, missing Panchang/Pretendard runtime fonts, and over-simplified laptop mockup. | Treat `5:2` as failed experiment, not final rebuild |
| 1.2 | 01/07/09 | User pasted working Figma slides into the rebuild workspace | New editable source nodes: `6:198`, `6:325`, `6:1046` | Rebase reverse engineering on pasted source nodes |
| 1.3 | fonts | Fontshare Panchang source captured | CSS and local `woff2` files stored in `assets/fonts/panchang/`; pasted text nodes preserve `Panchang`/`Pretendard` fontName but report `hasMissingFont: true` through the Plugin API | Enable/install fonts in Figma before final editable rebuild |
| 2 | 01 | Created structured clone from pasted source `6:198` | Figma node `22:2`; source and rebuild PNGs are pixel-identical (`0` changed pixels) | Use this as the calibration pattern for `07` and `09`; do not use failed `5:2` as target |
| 2.1 | 01 | Added role-based layer names and `jbyond` shared metadata to clone | Layer mapping `6:199 -> 22:3`, `6:204 -> 22:8`, `6:209 -> 22:13` and related text/overlay nodes recorded | Promote repeated parts to components only after preserving visual QA |
| 3 | 07 | Created structured clone from pasted source `6:325` | Figma node `25:2`; similarity `0.9997530864` | Optional polish loop for right-table micro diff, then componentize flow/table patterns |
| 3.1 | 07 | Refined role taxonomy on clone | Tables, header, diagram panel, flow group, entity rail, connectors, legend renamed and tagged | Update slide/token/component docs |
| 4 | 09 | Created structured clone from pasted source `6:1046` | Figma node `26:2`; source and rebuild PNGs are pixel-identical (`0` changed pixels) | Componentize process rail, branch group, and scenario cards |
| 5 | 02-06, 08, 10-14 | Expanded source-preserving structured clone pattern to the remaining 11 slides | Figma nodes `28:2`, `28:95`, `28:108`, `28:159`, `28:184`, `28:211`, `29:2`, `29:104`, `29:151`, `29:214`, `29:357`; full-deck min similarity `0.9996238426` | Deep-map role taxonomy, extract slide materials, then promote repeated parts to components |
| 6 | 02 | Created componentized rebuild v1.1 from `28:2` using `ProblemCaseCard` and broad `LimitationRow` instances | Figma node `46:2`; similarity `0.9938806906`; passed 98% but introduced visible row-geometry drift | Build an exact row component from source geometry |
| 6.1 | 02 | Created `JByond/Deck/LimitationRowExact/VariantSet` and rebuilt slide 02 v1.2 | Component set `48:88`; slide node `49:76`; similarity `0.9997815394` | Use v1.2 as the componentization pattern for the next repeated families |
| 7 | 04 | Created exact solution axis and flow step component sets, then rebuilt slide 04 from component instances | Component sets `53:174`, `53:184`; slide node `54:150`; similarity `0.9999657600` | Continue component promotion slide by slide |
| 8 | 03 | Created exact evidence screenshot and highlight component sets, then rebuilt slide 03 from component instances | Component sets `58:175`, `58:182`; slide node `58:183`; similarity `1.0000000000` | Use as the raster-evidence plus editable-overlay pattern |
| 9 | 08 | Created exact compact/tall/gate org-card component sets, then rebuilt slide 08 from component instances | Component sets `60:372`, `60:505`, `60:550`; slide node `61:176`; similarity `0.9999146412` | Promote connectors/ops panel only after endpoint drift check |
| 10 | 09 | Created exact scenario process-node and story-card component sets, then rebuilt slide 09 from component instances | Component sets `63:520`, `63:537`; slide node `64:490`; similarity `1.0000000000` | Continue with remaining dense component families |
| 11 | 07 | Created exact system-flow table and entity-pill component sets, then rebuilt slide 07 from component instances | Component sets `66:560`, `66:610`; slide node `68:508`; similarity `0.9995273920` | Promote main flow columns/connectors only after endpoint drift check |
| 12 | 10 | Created exact experience-node component set, then rebuilt slide 10 from component instances | Component set `70:659`; slide node `70:660`; similarity `0.9987331211` | Promote value-chain panel only after dense-text drift check |
| 13 | 11 | Created exact MVP checklist and demo-plan row component sets, then rebuilt slide 11 from component instances | Component sets `72:661`, `72:697`; slide node `74:649`; similarity `0.9999122299` | Promote remaining expansion/reference/Gantt families |
| 14 | 12 | Created exact benefit-bubble and expansion-step component sets, then rebuilt slide 12 from component instances | Component sets `75:690`, `75:703`; slide node `77:678`; similarity `0.9999541860` | Promote large orbit vectors only after z-order drift check |
| 15 | 13 | Created exact 2-line reference item, 3-line reference item, and verification row component sets, then rebuilt slide 13 from component instances | Component sets `79:736`, `79:832`, `79:849`; slide node `80:688`; similarity `1.0000000000` | Normalize reference rows into structured evidence ledger |
| 16 | 14 | Created exact Gantt date tick, lane metadata, task bar, and milestone components, then rebuilt slide 14 from component instances | Component sets `85:875`, `86:885`, `88:987`, `89:813`; slide node `90:777`; similarity `0.9997048611` | Use as the pattern for dense timeline componentization |
| 17 | 01 | Created exact cover media, header, footer, and wordmark components, then rebuilt slide 01 from component instances | Components `92:1179`, `92:1188`, `92:1189`, `92:1192`; slide node `93:1179`; tolerance-aware similarity `1.0000000000`, max delta `1` | Proceed to slide 05/06 with smaller selected child IDs only |

## Known Risks

- Figma source node IDs differ between the user's URL list and the existing deck audit document. Manifest records both candidates until duplicate access confirms mapping.
- Local PPTX is full-slide image based, so it cannot recover editable layers.
- `07` includes `[제휴 TBD]`; preserve source in reverse engineering, but flag before reuse in new decks.
- `09` source uses `케이스보드 칸반`; older markdown mentioning `간반` was stale. Enter-related visual language still needs a product/story decision before public reuse.
- Figma runtime in the fresh rebuild workspace initially did not expose `Panchang` or `Pretendard`, which caused the failed `5:2` visual rebuild to drift. The pasted `6:*` source nodes preserve original font metadata, but `hasMissingFont` is still true for `Panchang`/`Pretendard` in the Plugin API. Panchang source files are now captured from Fontshare under `assets/fonts/panchang/`; Pretendard still needs an equivalent local/source capture if not available in Figma.
- 2026-07-09 re-check: `figma.listAvailableFontsAsync()` still returned no `Panchang` or `Pretendard` entries in the plugin runtime. Continue preserving source text layers rather than editing font/text properties until those fonts are available.
