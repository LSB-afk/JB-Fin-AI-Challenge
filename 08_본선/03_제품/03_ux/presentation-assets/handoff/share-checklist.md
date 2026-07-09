---
tags:
  - area/product
  - type/checklist
  - status/active
date: 2026-07-09
up: "[[JByond Presentation Assetization Handoff]]"
---

# Share Checklist

이 체크리스트는 팀원에게 패키지를 공유하거나, 공유 받은 팀원이 재사용을 시작하기 전에 확인하는 기준이다.

## Before Sharing

| Check | Status |
|---|---|
| Figma file link is accessible | 확인 필요 |
| `99 Final Componentized Deck` page exists | done |
| 14 final frames are present | done |
| [`../INDEX.md`](../INDEX.md) exists | done |
| [`../deck-definition.md`](../deck-definition.md) exists | done |
| [`../manifest.json`](../manifest.json) includes final page and index links | done |
| [`../qa/rebuild-diff.md`](../qa/rebuild-diff.md) records accepted QA baselines | done |
| Team understands this is source-preserving assetization, not prompt-only generation | 확인 필요 |

## When A Teammate Receives The Package

| Step | Expected output |
|---|---|
| Open [`README.md`](../README.md) | Understand current state |
| Open [`INDEX.md`](../INDEX.md) | Know where each document lives |
| Open [`deck-definition.md`](../deck-definition.md) | Understand deck philosophy |
| Open Figma `99 Final Componentized Deck` | See final visual result |
| Choose role-specific path in [`team-quickstart.md`](team-quickstart.md) | Know next action |

## Before Starting New Figma Work

| Check | Rule |
|---|---|
| Source preservation | Do not overwrite original source frames |
| Final preservation | Do not directly mutate accepted final frames |
| New page/frame | Use a new page or clearly named candidate frame |
| Token use | Use token files before raw values |
| Component use | Use existing component sets when available |
| Font risk | Check Panchang/Pretendard availability |
| QA plan | Decide how screenshot diff will be recorded |

## Before Claiming Reuse Success

| Gate | Pass condition |
|---|---|
| Visual | similarity `>= 0.98`, or clearly documented exception |
| Editability | no full-slide flattened image |
| Component | repeated elements use component or documented pattern |
| Asset | raster materials are ledgered |
| Token | core colors/type/effects/spacing refer to tokens |
| QA | diff JSON or QA note exists |
| Process | prompt/build notes are recorded |

## Recommended Team Pilot

Run one blind rebuild before claiming full reuse.

Recommended slide:

`09 User Scenario`

Why:

- It has flow nodes, decision logic, scenario cards, labels, and imagery.
- Existing accepted componentized rebuild is pixel-identical.
- It is complex enough to test the documentation but not as risky as dense Gantt/reference slides.

Minimum result to record:

- new Figma page/frame node
- input docs used
- component instances used
- assets used
- screenshot diff result
- missing documents or token gaps
