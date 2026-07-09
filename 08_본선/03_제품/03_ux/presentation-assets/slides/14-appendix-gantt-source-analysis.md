---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 14 Appendix Gantt Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/14.jpg` |
| Deck audit node-id | `4939:3419` |
| Pasted working node-id | `6:1155` |
| Structured rebuild node-id | `29:357` |
| Componentized rebuild node-id | `90:777` |
| QA reference | `qa/visual-diff/14-gantt-structured-v1.json`, `qa/visual-diff/14-gantt-componentized-v1.0.json` |
| Figma access | `metadata_large_partial` |

## Message

본선 준비 과정의 사람/AI 협업, 레인별 작업 바, 산출물·검증·심사항목을 간트 형태로 보여주는 증빙 슬라이드다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Header note | 레인별 작업 바 설명 | editable text |
| Date grid | 06/11~07/05 날짜 labels and vertical grid lines | `GanttDateTickExact` |
| Tracks | 9개 레인 with progress %, owners, AI agents | `GanttLaneMetaExact` |
| Task bars | rounded bars inside date grid with 3 internal text rows | `GanttTaskBarExact` |
| Milestone markers | 예선 제출, 본선 안내, 제품§1, MVP/Viz, 동기화, 발표·시연 | `GanttMilestoneExact` |
| Footer evidence box | source/last generated/data quality/next | documented one-off editable metadata card |

## Track Inventory

- `1. 문제정의/JB 리서치` / `80%`
- `2. 제품 결정/범위 확정` / `70%`
- `7. QA/검증/시연 안정화` / `67%`
- `8. 운영 하네스/AI 협업 증빙` / `93%`
- `9. 발표/시연/리허설` / `67%`

Metadata output was truncated for the middle tracks, but the slide clearly follows the same lane pattern for all rows. Use the structured source frame for exact child extraction in the next focused pass.

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:1157` | gantt board root | contains all grid, lanes, bars, milestones |
| `6:1161`-`6:1249` | date header and vertical grid lines | 06/11 through 07/05 |
| `6:1250` onward | lane rows | repeated row groups with labels, progress, owners, AI agents, bars |
| `6:1538`-`6:1567` | milestone lines and labels | key dates |
| `6:1568`-`6:1585` | legend/source footer | source, generated date, quality, next |

## Component Model

- `JByond/Deck/GanttDateTickExact/VariantSet` (`85:875`) - 14 variants
- `JByond/Deck/GanttLaneMetaExact/VariantSet` (`86:885`) - 9 variants
- `JByond/Deck/GanttTaskBarExact/VariantSet` (`88:987`) - 21 variants
- `JByond/Deck/GanttMilestoneExact/VariantSet` (`89:813`) - 6 variants
- `JByond/Deck/GanttEvidenceFooter` - pending only if the footer metadata card repeats in future reporting decks

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `29:357` |
| Source mapping | `6:1155 -> 29:357` |
| QA | `780` changed pixels, similarity `0.9996238426` |
| Scope status | root-structured clone; superseded by componentized loop for repeated Gantt units |

## Componentized Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `90:777` |
| Source mapping | `6:1155 -> 29:357 -> 90:777` |
| Component sets | `85:875`, `86:885`, `88:987`, `89:813` |
| Replacements | 14 date ticks, 9 lane metadata rows, 21 task bars, 6 milestone markers |
| QA | `612` changed pixels, similarity `0.9997048611` |
| QA file | `qa/visual-diff/14-gantt-componentized-v1.0.json` |
| Scope status | accepted componentized baseline |

## QA Risks

- This slide is extremely dense. Text clipping and one-pixel line drift are the biggest risks.
- Date labels and generated date (`2026-07-03 KST`) are time-sensitive.
- Componentization used exact source geometry and replaced 50 repeated units with instances.
- Footer legend/evidence box remains cloned source layers because it is one-off in this deck.
