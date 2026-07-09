---
tags:
  - area/product
  - type/backlog
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# Full Deck Deep Assetization Backlog

The 14-slide source-preserving structured clone baseline is created in Figma and verified in `qa/visual-diff/full-deck-structured-audit-2026-07-09.json`.

All 14 slides now have accepted componentized rebuild loops above the 98% visual gate. Remaining work is optional deeper atomization of one-off connector, orbit, ops-panel, or console-shot internals, not visual parity.

Machine-readable backlog for agent/build execution: `tokens/assetization-backlog.json`.

## Pilot Componentized Status

| Slide | Source | Rebuild | Componentized QA | Promoted component sets |
|---:|---|---|---|---|
| 01 | `6:198` | `22:2` / componentized `93:1179` | tolerance-aware componentized pass `1.0000000000`; max delta `1` | `CoverMediaStackExact` `92:1179`; `CoverHeaderExact` `92:1188`; `CoverFooterExact` `92:1189`; `CoverWordmarkExact` `92:1192` |
| 05 | `6:261` | `28:159` / componentized `98:1189` | componentized pass `1.0000000000`; changed pixels `0` | `FeatureCalloutTopExact` `95:1197`; `FeatureCalloutRightExact` `96:1195` |
| 06 | `6:286` | `28:184` / componentized `101:1206` | componentized pass `1.0000000000`; changed pixels `0` | `ApprovalAuditCalloutExact` `101:1205` |
| 07 | `6:325` | `25:2` / componentized `68:508` | componentized pass `0.9995273920`; changed pixels `980` | `SystemFlowTableExact` `66:560`; `EntityPillExact` `66:610` |
| 09 | `6:1046` | `26:2` / componentized `64:490` | componentized pass `1.0000000000`; changed pixels `0` | `ScenarioProcessNodeExact` `63:520`; `ScenarioCardExact` `63:537` |
| 10 | `6:96` | `29:2` / componentized `70:660` | componentized pass `0.9987331211`; changed pixels `2,627` | `ExperienceNodeExact` `70:659` |
| 11 | `6:1108` | `29:104` / componentized `74:649` | componentized pass `0.9999122299`; changed pixels `182` | `MvpChecklistRowExact` `72:661`; `DemoPlanRowExact` `72:697` |
| 12 | `6:983` | `29:151` / componentized `77:678` | componentized pass `0.9999541860`; changed pixels `95` | `ExperienceBenefitBubbleExact` `75:690`; `ExpansionStepExact` `75:703` |
| 13 | `6:1586` | `29:214` / componentized `80:688` | componentized pass `1.0000000000`; changed pixels `0` | `ReferenceItem2LineExact` `79:736`; `ReferenceItem3LineExact` `79:832`; `VerificationSummaryRowExact` `79:849` |
| 14 | `6:1155` | `29:357` / componentized `90:777` | componentized pass `0.9997048611`; changed pixels `612` | `GanttDateTickExact` `85:875`; `GanttLaneMetaExact` `86:885`; `GanttTaskBarExact` `88:987`; `GanttMilestoneExact` `89:813` |

| Slide | Source | Rebuild | Baseline QA | Deep assetization work |
|---:|---|---|---|---|
| 02 | `6:3` | `28:2` / componentized `49:76` | structured pass `0.9999802276`; componentized pass `0.9997815394` | `slides/02-problem-definition-source-analysis.md`; `ProblemCaseCard` variant set `39:77` and exact `LimitationRowExact` set `48:88` are mapped into v1.2 |
| 03 | `6:313` | `28:95` / componentized `58:183` | structured byte-equal; componentized byte-equal `1.0000000000` | `slides/03-problem-evidence-source-analysis.md`; evidence screenshot assets exported and ledgered; `EvidenceScreenshotExact` set `58:175` and `EvidenceHighlightExact` set `58:182` are mapped into v1.0 |
| 04 | `6:210` | `28:108` / componentized `54:150` | structured pass `0.9999951775`; componentized pass `0.9999657600` | `slides/04-solution-overview-source-analysis.md`; solution composite exported; axis columns `53:174` and flow steps `53:184` mapped into v1.0 |
| 05 | `6:261` | `28:159` / componentized `98:1189` | structured byte-equal; componentized byte-equal `1.0000000000` | `slides/05-key-feature-ui-source-analysis.md`; workbench composite exported; callout component sets `95:1197` and `96:1195` are mapped into v1.0; unresolved `6:285` remains direct-read blocked |
| 06 | `6:286` | `28:184` / componentized `101:1206` | structured byte-equal; componentized byte-equal `1.0000000000` | `slides/06-key-feature-approval-source-analysis.md`; local product-panel crops exported; callout component set `101:1205` mapped into v1.0; timeout-prone `6:304` remains direct-read blocked |
| 08 | `6:592` | `28:211` / componentized `61:176` | structured pass `0.9999995177`; componentized pass `0.9999146412` | `slides/08-ai-org-chart-source-analysis.md`; compact role set `60:372`, tall role set `60:505`, and gate set `60:550` are mapped into v1.0; next promote connectors/ops panel only if delta stays below current threshold |
| 10 | `6:96` | `29:2` / componentized `70:660` | structured pass `0.9997024498`; componentized pass `0.9987331211` | `slides/10-expected-effects-source-analysis.md`; experience nodes `70:659` are mapped into v1.0; next normalize scenario metrics/evidence caveats and promote value-chain panel only after dense-text drift check |
| 11 | `6:1108` | `29:104` / componentized `74:649` | structured pass `0.9998283179`; componentized pass `0.9999122299` | `slides/11-implementation-demo-plan-source-analysis.md`; checklist rows `72:661` and demo-plan rows `72:697` are mapped into v1.0; next isolate any product/demo UI reference only if image fills are present |
| 12 | `6:983` | `29:151` / componentized `77:678` | structured pass `0.9999990355`; componentized pass `0.9999541860` | `slides/12-closing-expansion-source-analysis.md`; benefit bubbles `75:690` and expansion steps `75:703` are mapped into v1.0; next promote large orbit vectors only after z-order drift check |
| 13 | `6:1586` | `29:214` / componentized `80:688` | structured byte-equal; componentized byte-equal `1.0000000000` | `slides/13-appendix-references-source-analysis.md`; reference items `79:736`, `79:832` and verification rows `79:849` are mapped into v1.0; next normalize references into evidence ledger |
| 14 | `6:1155` | `29:357` / componentized `90:777` | structured pass `0.9996238426`; componentized pass `0.9997048611` | `slides/14-appendix-gantt-source-analysis.md`; date ticks `85:875`, lane meta `86:885`, task bars `88:987`, and milestones `89:813` are mapped into v1.0; footer evidence box remains documented one-off |

## Promotion Rule

Do not promote any group to a reusable component until the slide's source/rebuild visual baseline is preserved. Component work should be a controlled refactor of the clone, not a redraw.

## Next Agent Split

- A1: only revisit unresolved text nodes `6:285` and `6:304` if they can be manually isolated.
- A3: optional deeper componentization for slide `07` main flow connectors, slide `08` connector/ops panel, slide `12` large orbit vectors, and slide `14` footer evidence box.
- A4: image/table/graph harvesting for slides `05` and `06`; normalize already-componentized slide evidence into the ledger only when a missing source is found.
- A6: screenshot diff after each component promotion.
