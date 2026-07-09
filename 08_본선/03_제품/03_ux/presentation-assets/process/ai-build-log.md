---
tags:
  - area/product
  - type/log
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# AI Build Log

## 2026-07-08 Initial Repo Package

1. Task
   - JByond 발표덱 pilot 3장 자산화 패키지 생성.
2. Inputs
   - Local source screenshots: `01 Summary.jpg`, `07 데이터 및 활용 기술.jpg`, `09 사용자 시나리오.jpg`
   - Deck audit: `발표자료-피그마-정합성체크.md`
   - Design tokens: `jb-console-tokens.json`, `jb-console-tokens.css`
   - Parallel explorer outputs: A1/A2+A3/A4+A6 read-only analysis
3. Output
   - `presentation-assets/README.md`
   - `presentation-assets/manifest.json`
   - `presentation-assets/slides/*-source-analysis.md`
   - `presentation-assets/tokens/*`
   - `presentation-assets/components/component-catalog.md`
   - `presentation-assets/assets/asset-ledger.md`
   - `presentation-assets/qa/rebuild-diff.md`
   - `presentation-assets/process/*`
4. Assumptions
   - Pilot slides remain `01`, `07`, `09`.
   - Editable Figma duplicate will be provided later.
   - Full-slide local JPGs are reference assets only, not rebuild content.
5. Open risks
   - Source Figma file access is blocked.
   - Connected Figma account has a `View` seat, so A5 cannot create a new editable rebuild file from this connector.
   - User-provided node-id list and existing deck audit node IDs do not yet map 1:1.
   - Exact Figma font/effect/image fill values require duplicate access.
6. Next action
   - A5 Figma Slide Builder creates the duplicate file structure and builds `01 Summary` calibration slide after editable URL is available.

## Decisions

- Keep original Figma untouched.
- Treat `01 Summary` as calibration slide before `07` and `09`.
- Use `deck.*` tokens for presentation-specific choices and keep `jb-console` tokens as base.
- Allow raster only for photos, laptop/device mockups, and story-card illustrations until original editable source is available.

## 2026-07-08 PDF Order Check

1. Task
   - 최종 발표 PDF를 기준으로 14장 순서와 pilot slide page를 확인.
2. Inputs
   - `08_본선/05_제출/제출본/PPT/JBFinAI_JByond_본선_PPT.pdf`
   - `08_본선/05_제출/제출본/PPT/Figma/*.jpg`
3. Output
   - `qa/pdf-order-check.md`
   - `manifest.json` final PDF metadata
   - `slides/_inventory-14.md` PDF page mapping
4. Assumptions
   - PDF embedded JPEGs are recompressed by PowerPoint, so exact SHA mismatch is expected.
5. Open risks
   - PDF is still a flattened packaging reference; editable layer recovery still requires Figma duplicate access.
6. Next action
   - Use PDF page order as the final submitted sequence when A5 rebuilds slides in Figma.

## 2026-07-08 Figma Access Check

1. Task
   - A5 build 가능 여부를 확인하기 위해 Figma connector account/plan 상태 확인.
2. Result
   - Initial connector account had a `View` seat on the available team plan.
   - Original source file returned edit-access blocker.
3. Decision
   - Do not create an unofficial blank Figma file from a view-only account.
   - Keep repo package as the build source-of-truth until editor-capable duplicate/workspace is provided.

## 2026-07-08 Figma Access Re-check

1. Task
   - `@figma` plugin으로 계정/파일 권한 재확인.
2. Result
   - Connected account changed to `김주용`.
   - `팀 망상궤도` plan has `Full` seat.
   - Source file top-level metadata loaded: `28` pages, primary deck page `4595:2`.
   - Read-only `use_figma` context probe succeeded.
   - Pilot node metadata loaded for `5053:11835`, `5053:11964`, `5053:12685`.
3. Decision
   - A5 is no longer blocked by account permission.
   - Next blocker is choosing an editable duplicate URL or approving a fresh rebuild workspace.

## 2026-07-08 Token System Expansion

1. Task
   - 기존 flat `presentation-tokens.json`만으로는 발표덱 재구성에 부족하다는 판단에 따라 token system을 machine-readable 구조로 확장.
2. Inputs
   - Figma read-only extraction from `5053:11835`, `5053:11964`, `5053:12685`.
   - Local source screenshots and PDF order baseline.
   - Existing component catalog and first-pass token notes.
3. Output
   - `tokens/token-index.json`
   - `tokens/primitives.json`
   - `tokens/semantic.json`
   - `tokens/typography.json`
   - `tokens/effects.json`
   - `tokens/components.json`
   - `tokens/slides.json`
   - `tokens/assets.json`
   - `tokens/qa-rules.json`
   - `tokens/figma-variable-map.json`
   - `tokens/token-registry.csv`
   - `tokens/presentation-tokens.css`
   - `tokens/specimens/token-specimen.svg`
4. Decision
   - `presentation-tokens.json` remains only as compatibility summary.
   - A5 Builder must use `token-index.json` and split token files as source of truth.

## 2026-07-08 Figma Rebuild Workspace V0

1. Task
   - Fresh Figma rebuild workspace를 만들고, A5 Builder의 첫 실제 산출물을 생성.
2. Output
   - Figma file: `https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`
   - Pages: `00 Cover`, `01 Foundations`, `02 Components`, `03 Pilot Slides`, `04 References`, `05 QA`
   - Variables: `JByond Deck / Color`, `JByond Deck / Size`
   - Text styles: `JByond/Deck/*` role styles with source font descriptions
   - Effect styles: product shot shadow, card shadow
   - Foundations specimen frame: `4:2`
   - `01 Summary` editable rebuild v0: `5:2`
3. Decision
   - This file is a fresh rebuild workspace, not a duplicate of the original.
   - Source Figma remains read-only reference.
4. Known issue
   - Figma runtime exposes `Inter` only in the new file; original font tokens are `Pretendard` and `Panchang`.

## 2026-07-08 Source Rebase After User-Pasted Working Slides

1. Trigger
   - User reported that the `01 Summary` rebuild v0 looked materially different from the original.
2. Root cause
   - v0 used placeholder image layers instead of original image fills.
   - v0 did not have `Panchang`/`Pretendard` available in the generated Figma runtime.
   - v0 simplified the laptop/product visual, so it was structurally editable but not presentation-quality.
3. New source state
   - User pasted working original slide frames into `https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`.
   - Page 1 now contains the full 14-slide sequence as `6:*` nodes.
4. Pilot source nodes
   - `01 Summary`: `6:198`
   - `07 데이터 및 활용 기술`: `6:325`
   - `09 User Scenario`: `6:1046`
5. Captured working source screenshots
   - `assets/pasted-working-screenshots/01-summary-6-198.png`
   - `assets/pasted-working-screenshots/07-system-flow-6-325.png`
   - `assets/pasted-working-screenshots/09-user-scenario-6-1046.png`
6. Font source capture
   - Fontshare Panchang CSS: `assets/fonts/panchang/fontshare-panchang.css`
   - Local Panchang weights: `assets/fonts/panchang/Panchang-*.woff2`
7. Decision
   - Keep `5:2` as a failure/QA experiment.
   - Use pasted editable source nodes as the reverse-engineering baseline going forward.

## 2026-07-09 01 Summary Structured Rebuild V1

1. Task
   - 사용자 피드백에 따라 placeholder 재구성을 중단하고, pasted editable source `6:198`를 기준으로 고품질 구조화 복제본을 생성.
2. Inputs
   - Working Figma file: `h6RkEn7fGbTwZbzuwaHsWi`
   - Source node: `6:198`
   - Font guidance: Panchang from Fontshare, Pretendard/Panchang Figma missing-font risk
3. Output
   - Figma structured rebuild node: `22:2` / `S01/Summary/Structured Rebuild v1.0`
   - Layer map: `6:199 -> 22:3`, `6:204 -> 22:8`, `6:209 -> 22:13`, plus header/footer/overlay nodes
   - QA exports:
     - `assets/rebuild-screenshots/01-summary-source-6-198.png`
     - `assets/rebuild-screenshots/01-summary-structured-22-2.png`
   - Visual diff record: `qa/visual-diff/01-summary-structured-v1.json`
4. Verification
   - Both screenshots are `1920x1080`.
   - SHA-256 is identical for source and rebuild screenshots.
   - Pixel comparison changed pixels: `0 / 2,073,600`; similarity `1.0000000000`.
5. Decision
   - `22:2` is the new calibration rebuild for slide 01.
   - `5:2` remains only as a failed experiment and should not be reused as a visual baseline.
   - Do not mutate text content or font properties until `Pretendard` and `Panchang` are available to the Figma runtime.
6. Next action
   - Apply the same source-clone + structure + QA loop to `07` (`6:325`) and `09` (`6:1046`), then componentize repeated patterns without breaking the pixel baseline.

## 2026-07-09 07/09 Structured Rebuild V1

1. Task
   - `01 Summary`에서 검증된 source-clone 방식으로 `07 데이터 및 활용 기술`, `09 User Scenario`를 구조화 복제.
2. Inputs
   - `07` source node: `6:325`
   - `09` source node: `6:1046`
   - Working Figma file: `h6RkEn7fGbTwZbzuwaHsWi`
3. Figma outputs
   - `07`: `25:2` / `S07/SystemFlow/Structured Rebuild v1.0`
   - `09`: `26:2` / `S09/UserScenario/Structured Rebuild v1.0`
4. Structuring decisions
   - Do not redraw or mutate text. Clone source layers, then add role-based names and `jbyond` shared plugin metadata.
   - For `07`, refine taxonomy after clone: tables, header, diagram panel, flow group, entity rail, connectors, and legend.
   - For `09`, name process nodes, decision/branch group, connectors, use-case label, and four story cards directly from source node mapping.
5. Verification
   - `07` source/rebuild PNGs are both `1920x1080`; changed pixels `512 / 2,073,600`; similarity `0.9997530864`.
   - `09` source/rebuild PNGs are both `1920x1080`; changed pixels `0 / 2,073,600`; similarity `1.0000000000`.
6. Content notes
   - `07` source currently says `통계 실행`; derivative decks should verify whether `통제 실행` was intended.
   - `09` source says `케이스보드 칸반`; earlier `간반` wording in markdown was stale.
7. Next action
   - Treat 3-slide pilot as passing the requested 98% loop target.
   - Expand the same source-clone + QA pattern to the remaining 11 slides, then promote repeated elements to components after preserving pixel baselines.

## 2026-07-09 Full 14-Slide Structured Clone Baseline

1. Task
   - Pilot 3장 기준이 98%를 넘었기 때문에, 같은 source-preserving clone + QA 방식을 14장 전체로 확장.
2. Figma outputs
   - `02`: `28:2`
   - `03`: `28:95`
   - `04`: `28:108`
   - `05`: `28:159`
   - `06`: `28:184`
   - `08`: `28:211`
   - `10`: `29:2`
   - `11`: `29:104`
   - `12`: `29:151`
   - `13`: `29:214`
   - `14`: `29:357`
3. Verification
   - Figma metadata audit: all 14 rebuild frames exist, all are `1920x1080`, all preserve source child counts.
   - Full PNG byte-equal export: slides `03`, `05`, `06`, `13`.
   - Full screenshot pixel diff: slides `01`, `02`, `04`, `07`, `08`, `09`, `10`, `11`, `12`, `14`.
   - Full-deck audit file: `qa/visual-diff/full-deck-structured-audit-2026-07-09.json`.
   - Minimum similarity: `0.9996238426` on slide `14`.
4. Decision
   - All 14 source-preserving structured clones pass the visual gate.
   - Slides `02-06`, `08`, and `10-14` are still root-structured clones, not fully assetized slides.
   - Next work must decompose those remaining slides into role-level taxonomy, extracted materials, and reusable components without breaking their pixel baselines.

## 2026-07-09 Full 14-Slide Source Analysis And Backlog Contract

1. Task
   - User-pasted working Figma slides were treated as the editable reverse-engineering baseline.
   - Remaining 11 slides were documented with source-analysis files and connected to the manifest.
2. Output
   - Added source-analysis docs for slides `02-06`, `08`, and `10-14`.
   - Added `tokens/assetization-backlog.json` as the machine-readable contract for material extraction, component promotion, token-family mapping, and QA follow-up.
   - Updated `README.md`, `asset-ledger.md`, `component-catalog.md`, `token-notes.md`, and `slides/full-deck-deep-assetization-backlog.md`.
3. Figma extraction caveats
   - The two key-feature slides passed visual clone QA, but full-slide metadata extraction timed out at this stage. Later selected-child workflows resolved the callout componentization loops for both slides.
   - Slide `14` metadata is very large; the first pass captured the major Gantt structure, but lane/task modeling still needs a dedicated extraction loop.
4. Decision
   - The current deck should be considered a high-fidelity source-preserving clone baseline, not yet a finished reusable design system.
   - Next work should follow `tokens/assetization-backlog.json` slide by slide and rerun visual QA after every component promotion.

## 2026-07-09 Asset Extraction And First Component Promotion

1. Task
   - Move from visual clone baseline into concrete assetization: extract reusable raster materials and create the first Figma component without mutating source/rebuild slides.
2. Figma outputs
   - Created `JByond/Deck/ProblemCaseCard` component on `02 Components`.
   - Component node id: `36:16`.
   - Source: duplicate of slide 02 node `6:11`; source slide `6:3` remains preserved.
3. Extracted assets
   - `assets/images/03-problem-evidence/regulation-evidence-2051-6-321.png`
   - `assets/images/03-problem-evidence/article-evidence-123-6-320.png`
   - `assets/images/04-solution-overview/solution-composite-2093-6-260.png`
   - `assets/images/05-key-feature-ui/case-workbench-composite-2094-6-262.png`
   - `assets/components/problem-case-card-36-16.png`
4. Verification
   - Figma component metadata for `36:16` loaded successfully.
   - Exported image dimensions and SHA-256 hashes were recorded in `assets/asset-ledger.md` and token files.
5. Caveat
   - Figma available fonts still only expose Inter in the plugin runtime. The component preserves original missing-font text nodes by duplication, but future text mutation still requires Pretendard/Panchang availability.

## 2026-07-09 ProblemCaseCard Variant Set And Slide 06 Local Crops

1. Task
   - Continue component promotion and material extraction without mutating the source/rebuild slide baselines.
2. Figma outputs
   - Created `JByond/Deck/ProblemCaseCard/VariantSet` on `02 Components`.
   - Component set node id: `39:77`.
   - Variants: `39:16`, `39:31`, `39:46`, `39:61`, `39:76`.
   - Variant properties: `Size=large/small`, `Source=capital/aqua/farm/student`.
3. Extracted assets
   - `assets/components/problem-case-card-variant-set-39-77.png`
   - `assets/images/06-key-feature-approval/floating-case-detail-local-crop.png`
   - `assets/images/06-key-feature-approval/approval-queue-local-crop.png`
   - `assets/images/06-key-feature-approval/report-viewer-local-crop.png`
   - `assets/images/06-key-feature-approval/sidebar-queue-local-crop.png`
4. Verification
   - Figma metadata and screenshot export for `39:77` succeeded.
   - Local slide 06 crops were visually inspected and hash/size recorded.
5. Caveat
   - Slide `6:286` Figma subtree read timed out again. Slide 06 crops are marked as local final-JPG-derived temporary assets until smaller Figma subtree IDs can be isolated.

## 2026-07-09 Slide 02 LimitationRow Component Promotion

1. Task
   - Promote the slide 02 existing-approach comparison rows into reusable Figma variants without mutating source or structured rebuild slides.
2. Figma outputs
   - Created `JByond/Deck/LimitationRow/VariantSet` on `02 Components`.
   - Component set node id: `42:17`.
   - Variants: `42:6` (`chatbot`), `42:11` (`dashboard`), `42:16` (`rpa`).
3. QA adjustment
   - First screenshot showed right-edge text clipping on the first row.
   - Expanded child component bounds to `820x40` and set the component set to `840x250`.
   - Re-exported screenshot to `assets/components/limitation-row-variant-set-42-17.png`.
4. Verification
   - Figma metadata for `42:17` loaded successfully.
   - Screenshot was visually inspected after the width fix.
   - SHA-256 recorded: `29e1a69658e1d2654ef640c09a89df5199094f9f0d61f8f78b1280b502bf6de1`.

## 2026-07-09 Slide 02 Componentized Rebuild Loop

1. Task
   - Validate whether slide `02` can remain visually faithful while replacing repeated elements with Figma component instances.
2. Font/runtime finding
   - `figma.listAvailableFontsAsync()` still returned no `Panchang` or `Pretendard` entries.
   - Decision: do not retype or mutate source text. Preserve cloned source text layers inside components until the fonts are available in Figma.
3. Figma outputs
   - Componentized rebuild v1.1: `46:2`, using `ProblemCaseCard/VariantSet` `39:77` and `LimitationRow/VariantSet` `42:17`.
   - Exact row component set: `JByond/Deck/LimitationRowExact/VariantSet`, node `48:88`.
   - Componentized rebuild v1.2: `49:76`, using `39:77` and `48:88`.
4. QA loop
   - v1.1 source similarity: `0.9938806906`, changed pixels `12,689`.
   - v1.1 passed the 98% gate, but visual diff showed row text/arrow geometry drift.
   - v1.2 source similarity: `0.9997815394`, changed pixels `453`.
   - v1.2 is accepted as the current slide 02 componentized baseline.
5. Decision
   - For text-heavy presentation components, exact source geometry can be more important than generic auto-layout friendliness.
   - Keep `42:17` as a broader reusable row component, but use `48:88` when the rebuild must preserve the submitted-deck visual match.

## 2026-07-09 Slide 04 Componentized Rebuild Loop

1. Task
   - Continue moving from source-preserving clone baseline to reusable component instances while maintaining visual fidelity above the 98% target.
2. Figma outputs
   - Created `JByond/Deck/SolutionAxisColumnExact/VariantSet`, node `53:174`.
   - Created `JByond/Deck/SolutionFlowStepExact/VariantSet`, node `53:184`.
   - Created `S04/SolutionOverview/Componentized Rebuild v1.0`, node `54:150`.
3. QA
   - Source node: `6:210`
   - Structured baseline: `28:108`
   - Componentized rebuild similarity: `0.9999657600`
   - Changed pixels: `71 / 2,073,600`
   - Visual diff: `qa/visual-diff/04-solution-componentized-v1.0.json`
4. Decision
   - Accept `54:150` as the current slide 04 componentized baseline.
   - Right-side product screenshot remains raster-allowed; left-side axis columns and flow pills are now component instances.

## 2026-07-09 Slide 03 Componentized Rebuild Loop

1. Task
   - Convert slide `03` evidence screenshots and blue highlight overlays into reusable component instances without changing the submitted-deck visual.
2. Figma outputs
   - Created `JByond/Deck/EvidenceScreenshotExact/VariantSet`, node `58:175`.
   - Created `JByond/Deck/EvidenceHighlightExact/VariantSet`, node `58:182`.
   - Created `S03/ProblemEvidence/Componentized Rebuild v1.0`, node `58:183`.
3. QA
   - Source node: `6:313`
   - Structured baseline: `28:95`
   - Componentized rebuild similarity: `1.0000000000`
   - Changed pixels: `0 / 2,073,600`
   - Visual diff: `qa/visual-diff/03-problem-evidence-componentized-v1.0.json`
4. Decision
   - Accept `58:183` as the current slide 03 componentized baseline.
   - Evidence screenshots remain raster image-fill components because they are source/citation material.
   - Highlight overlays are editable component instances so the evidence-highlight pattern can be reused without baking overlays into the evidence images.

## 2026-07-09 Slide 08 Componentized Rebuild Loop

1. Task
   - Convert the repeated AI org-chart cards into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/OrgRoleNodeCompactExact/VariantSet`, node `60:372`.
   - Created `JByond/Deck/OrgRoleNodeTallExact/VariantSet`, node `60:505`.
   - Created `JByond/Deck/OrgGateNodeExact/VariantSet`, node `60:550`.
   - Created `S08/AIOrgChart/Componentized Rebuild v1.0`, node `61:176`.
3. QA
   - Source node: `6:592`
   - Structured baseline: `28:211`
   - Componentized rebuild similarity: `0.9999146412`
   - Changed pixels: `177 / 2,073,600`
   - Visual diff: `qa/visual-diff/08-ai-org-componentized-v1.0.json`
4. Decision
   - Accept `61:176` as the current slide 08 componentized baseline.
   - Connector arrows and the bottom-right operations panel remain cloned source layers until a narrower promotion loop verifies endpoint drift.

## 2026-07-09 Slide 09 Componentized Rebuild Loop

1. Task
   - Convert the repeated user-scenario workflow nodes and story cards into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/ScenarioProcessNodeExact/VariantSet`, node `63:520`.
   - Created `JByond/Deck/ScenarioCardExact/VariantSet`, node `63:537`.
   - Created `S09/UserScenario/Componentized Rebuild v1.0`, node `64:490`.
3. QA
   - Source node: `6:1046`
   - Structured baseline: `26:2`
   - Componentized rebuild similarity: `1.0000000000`
   - Changed pixels: `0 / 2,073,600`
   - Visual diff: `qa/visual-diff/09-user-scenario-componentized-v1.0.json`
4. Decision
   - Accept `64:490` as the current slide 09 componentized baseline.
   - Process/branch nodes and story cards are now component instances.
   - Decision diamond, connector arrows, headline, background, and use-case label remain cloned source layers until a narrower loop can promote them without endpoint or text drift.

## 2026-07-09 Slide 07 Componentized Rebuild Loop

1. Task
   - Convert the right-side system-flow tables and bottom entity rail pills into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/SystemFlowTableExact/VariantSet`, node `66:560`.
   - Created `JByond/Deck/EntityPillExact/VariantSet`, node `66:610`.
   - Created `S07/SystemFlow/Componentized Rebuild v1.0`, node `68:508`.
3. QA
   - Source node: `6:325`
   - Structured baseline: `25:2`
   - Componentized rebuild similarity: `0.9995273920`
   - Changed pixels: `980 / 2,073,600`
   - Visual diff: `qa/visual-diff/07-system-flow-componentized-v1.0.json`
4. Decision
   - Accept `68:508` as the current slide 07 componentized baseline.
   - Right-side tables and bottom entity pills are now component instances.
   - Main flow columns, nodes, and connectors remain cloned source layers until a narrower loop can promote them without connector endpoint drift.

## 2026-07-09 Slide 10 Componentized Rebuild Loop

1. Task
   - Convert the repeated TX/AX/UX/EX-PX/CX experience map nodes into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/ExperienceNodeExact/VariantSet`, node `70:659`.
   - Created `S10/ExpectedEffects/Componentized Rebuild v1.0`, node `70:660`.
3. QA
   - Source node: `6:96`
   - Structured baseline: `29:2`
   - Componentized rebuild similarity: `0.9987331211`
   - Changed pixels: `2,627 / 2,073,600`
   - Visual diff: `qa/visual-diff/10-effects-componentized-v1.0.json`
4. Decision
   - Accept `70:660` as the current slide 10 componentized baseline.
   - Experience map nodes are now component instances.
   - Arrows, left headline, bottom-left material group, and dense value-chain panel remain cloned source layers until a narrower loop can promote them without text reflow or connector drift.

## 2026-07-09 Slide 11 Componentized Rebuild Loop

1. Task
   - Convert the repeated completed-MVP checklist rows and demo-plan row pairs into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/MvpChecklistRowExact/VariantSet`, node `72:661`.
   - Created `JByond/Deck/DemoPlanRowExact/VariantSet`, node `72:697`.
   - Created `S11/ImplementationDemoPlan/Componentized Rebuild v1.0`, node `74:649`.
3. QA
   - Source node: `6:1108`
   - Structured baseline: `29:104`
   - Componentized rebuild similarity: `0.9999122299`
   - Changed pixels: `182 / 2,073,600`
   - Visual diff: `qa/visual-diff/11-demo-plan-componentized-v1.0.json`
4. Decision
   - Accept `74:649` as the current slide 11 componentized baseline.
   - MVP checklist rows and demo-plan row pairs are now component instances.
   - Background, header badge, headline paragraph, and column titles remain cloned source layers because they are either one-off or line-break-sensitive.

## 2026-07-09 Slide 12 Componentized Rebuild Loop

1. Task
   - Convert the repeated AX/EX/CX benefit bubbles and right-side expansion step labels into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/ExperienceBenefitBubbleExact/VariantSet`, node `75:690`.
   - Created `JByond/Deck/ExpansionStepExact/VariantSet`, node `75:703`.
   - Created `S12/ClosingExpansion/Componentized Rebuild v1.0`, node `77:678`.
3. QA
   - Source node: `6:983`
   - Structured baseline: `29:151`
   - Componentized rebuild similarity: `0.9999541860`
   - Changed pixels: `95 / 2,073,600`
   - Visual diff: `qa/visual-diff/12-expansion-componentized-v1.0.json`
4. Decision
   - Accept `77:678` as the current slide 12 componentized baseline.
   - AX/EX/CX benefit bubbles and expansion step labels are now component instances.
   - Large orbit vectors, center list, closing statement, and the `오늘` arrow remain cloned source layers because z-order and line-break drift risk is higher than the immediate reuse value.

## 2026-07-09 Slide 13 Componentized Rebuild Loop

1. Task
   - Convert the repeated appendix reference rows and verification summary rows into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/ReferenceItem2LineExact/VariantSet`, node `79:736`.
   - Created `JByond/Deck/ReferenceItem3LineExact/VariantSet`, node `79:832`.
   - Created `JByond/Deck/VerificationSummaryRowExact/VariantSet`, node `79:849`.
   - Created `S13/AppendixReferences/Componentized Rebuild v1.0`, node `80:688`.
3. QA
   - Source node: `6:1586`
   - Structured baseline: `29:214`
   - Componentized rebuild similarity: `1.0000000000`
   - Changed pixels: `0 / 2,073,600`
   - Visual diff: `qa/visual-diff/13-appendix-componentized-v1.0.json`
4. Decision
   - Accept `80:688` as the current slide 13 componentized baseline.
   - The 31 reference rows are split into 2-line and 3-line component sets to keep each set under the 30-variant cap.
   - Evidence URL/file provenance is not fully normalized yet; that becomes a structured evidence-ledger task rather than a visual rebuild task.

## 2026-07-09 Slide 14 Componentized Rebuild Loop

1. Task
   - Convert the dense Gantt chart into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/GanttDateTickExact/VariantSet`, node `85:875`.
   - Created `JByond/Deck/GanttLaneMetaExact/VariantSet`, node `86:885`.
   - Created `JByond/Deck/GanttTaskBarExact/VariantSet`, node `88:987`.
   - Created `JByond/Deck/GanttMilestoneExact/VariantSet`, node `89:813`.
   - Created `S14/AppendixGantt/Componentized Rebuild v1.0`, node `90:777`.
3. QA
   - Source node: `6:1155`
   - Structured baseline: `29:357`
   - Componentized rebuild similarity: `0.9997048611`
   - Changed pixels: `612 / 2,073,600`
   - Visual diff: `qa/visual-diff/14-gantt-componentized-v1.0.json`
4. Decision
   - Accept `90:777` as the current slide 14 componentized baseline.
   - Fourteen date ticks, nine lane metadata rows, twenty-one task bars, and six milestone markers are now component instances.
   - The footer legend/evidence box remains cloned source layers because it is a one-off pattern in this deck and does not yet justify a component.

## 2026-07-09 Slide 05 Figma Read Issue

1. Observation
   - Slide `05` source/baseline frames are visually verified through the existing structured clone baseline, but Figma subtree reads are unstable.
2. Failed reads
   - Full subtree candidate extraction for `6:261` / `28:159`: `HTTP 504`.
   - `get_metadata` on `28:159`: `HTTP 504`.
   - Minimal direct-child `use_figma` read on `28:159`: `HTTP 504`.
3. Decision
   - Do not keep retrying the same heavy read path.
   - Continue with other slides and retry slide `05` only through smaller manually isolated child IDs or selected-node workflows.
4. Follow-up probe
   - Single-node `get_metadata` succeeded for `6:262-6:284` except `6:285`.
   - A bundled `use_figma` loop over the same range still returned `HTTP 504`.
   - Next Slide 05 build should use one-node metadata probes and narrowly scoped write calls; avoid traversing `6:261` / `28:159`.

## 2026-07-09 Slide 05 Componentized Rebuild Loop

1. Task
   - Promote the safe, isolated Slide 05 callout label groups and compose a full componentized rebuild without direct-reading unresolved node `6:285`.
2. Figma outputs
   - Created `JByond/Deck/FeatureCalloutTopExact/VariantSet`, node `95:1197`.
   - Created `JByond/Deck/FeatureCalloutRightExact/VariantSet`, node `96:1195`.
   - Created `S05/KeyFeatureUI/Componentized Rebuild v1.0`, node `98:1189`.
   - Component instances in `98:1189`: `98:1214`, `98:1217`, `98:1220`, `98:1223`.
   - Hidden original callout layers in `98:1189`: `98:1199`, `98:1202`, `98:1205`, `98:1206`, `98:1207`, `98:1208`.
3. Source mapping
   - Top callouts: `6:271` (`Case Board`) and `6:274` (`Risk Signal`).
   - Right callouts: `6:277` + `6:279` (`Agent Run`) and `6:278` + `6:280` (`Evidence Pack`).
4. Evidence
   - `assets/rebuild-screenshots/05-key-feature-ui-source-6-261.png`
   - `assets/rebuild-screenshots/05-key-feature-ui-componentized-98-1189.png`
   - `qa/visual-diff/05-key-feature-ui-componentized-v1.0.json`
   - `assets/components/feature-callout-top-exact-variant-set-95-1197.png`
   - `assets/components/feature-callout-right-exact-variant-set-96-1195.png`
5. QA
   - Source node: `6:261`
   - Structured baseline: `28:159`
   - Componentized rebuild similarity: `1.0000000000`
   - Changed pixels: `0 / 2,073,600`
6. Decision
   - Accept `98:1189` as the current slide 05 componentized baseline.
   - Product screenshot remains raster-allowed. Connector vectors remain cloned source layers unless a later connector-only loop proves reuse value without endpoint drift.
   - Do not direct-read `6:285` until it can be manually isolated.

## 2026-07-09 Slide 06 Figma Read Issue

1. Observation
   - Slide `06` source/baseline frames are visually verified through the structured clone baseline and local product-panel crops, but Figma subtree reads are unstable.
2. Failed reads
   - Lightweight source+baseline child read for `6:286` / `28:184`: `HTTP 504`.
   - `get_metadata` on `28:184`: `HTTP 504`.
3. Decision
   - Do not retry full slide or whole-subtree reads.
   - Retry only with selected child IDs or manually isolated smaller node IDs for callouts, approval queue, report viewer, and sidebar regions.

## 2026-07-09 Slide 06 Componentized Rebuild Loop

1. Task
   - Promote the selected Slide 06 approval/audit callout groups and compose a full componentized rebuild without direct-reading timeout-prone node `6:304`.
2. Figma outputs
   - Created `JByond/Deck/ApprovalAuditCalloutExact/VariantSet`, node `101:1205`.
   - Created `S06/KeyFeatureApproval/Componentized Rebuild v1.0`, node `101:1206`.
   - Component instances in `101:1206`: `101:1233`, `101:1236`.
   - Hidden original callout layers in `101:1206`: `101:1225`, `101:1229`.
3. Source mapping
   - `L0~L4 Gate`: source node `6:309`.
   - `Audit LogAgent`: source node `6:305`.
4. Evidence
   - `assets/rebuild-screenshots/06-key-feature-approval-source-6-286.png`
   - `assets/rebuild-screenshots/06-key-feature-approval-componentized-101-1206.png`
   - `qa/visual-diff/06-key-feature-approval-componentized-v1.0.json`
   - `assets/components/approval-audit-callout-exact-variant-set-101-1205.png`
5. QA
   - Source node: `6:286`
   - Structured baseline: `28:184`
   - Componentized rebuild similarity: `1.0000000000`
   - Changed pixels: `0 / 2,073,600`
6. Decision
   - Accept `101:1206` as the current slide 06 componentized baseline.
   - Approval queue/report viewer remain raster-allowed product material. Promote internal console-shot cards only if future decks require editing those UI internals.

## 2026-07-09 Slide 01 Componentized Rebuild Loop

1. Task
   - Convert the cover slide into reusable component instances while preserving the source visual baseline.
2. Figma outputs
   - Created `JByond/Deck/CoverMediaStackExact`, node `92:1179`.
   - Created `JByond/Deck/CoverHeaderExact`, node `92:1188`.
   - Created `JByond/Deck/CoverFooterExact`, node `92:1189`.
   - Created `JByond/Deck/CoverWordmarkExact`, node `92:1192`.
   - Created `S01/Summary/Componentized Rebuild v1.0`, node `93:1179`.
3. Failure and correction
   - First header component attempt tried to load `Pretendard SemiBold` and failed because the Figma Plugin runtime did not expose `Pretendard`.
   - Corrected approach: clone source text nodes into components without mutating characters/font properties, preserving original font metadata.
4. QA
   - Source node: `6:198`
   - Structured baseline: `22:2`
   - Componentized rebuild tolerance-aware similarity: `1.0000000000`
   - Tolerance-aware changed pixels: `0 / 2,073,600`
   - Exact-pixel changed pixels: `923,512`, but max channel delta is only `1`.
   - Visual diff: `qa/visual-diff/01-summary-componentized-v1.0.json`
5. Decision
   - Accept `93:1179` as the current slide 01 componentized baseline.
   - Use tolerance-aware QA for component-instance quantization when max channel delta is `1` and no visible layout drift exists.
