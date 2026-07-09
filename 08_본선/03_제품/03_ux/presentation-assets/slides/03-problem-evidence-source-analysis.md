---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 03 Problem Evidence Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/03 문제 정의.jpg` |
| Deck audit node-id | `4852:2204` |
| Pasted working node-id | `6:313` |
| Structured rebuild node-id | `28:95` |
| QA reference | `qa/visual-diff/full-deck-structured-audit-2026-07-09.json` |
| Figma access | `metadata_ok` |

## Message

사후점검 규제 강화로 RM의 근거 대조 업무가 더 정교해져야 하며, 더 많은 Case를 빠르게 처리하는 것보다 더 안전하게 판단해야 한다는 근거 슬라이드다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Header | 중앙 `Problem Definition` pill, 대형 headline, supporting copy | editable text |
| Left evidence image | 기사/문서형 캡처 이미지 | raster allowed as evidence screenshot |
| Right evidence image | 규제/문서형 캡처 이미지 | raster allowed as evidence screenshot |
| Highlights | 파란/반투명 highlight rectangles | editable overlay rectangles |

## Text Inventory

- `Problem Definition`
- `6월 말, 사후점검 규제는 강화되고 더 정교한 관리가 필요해졌다`
- `사후점검 규제 강화로 RM의 근거 대조 업무는 더 정교져야한다. 즉, 더 많은 Case를 더 빠르게 처리하는 것이 아니라, 더 많은 Case를 더 안전하게 판단해야 하는 상황이다.`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:314` | header group | contains pill/headline/body text |
| `6:321` | left evidence image | image fill hash `1c98e132999733e68ecda85f675d543a326770ec`, `823x331`, scale `FILL` |
| `6:320` | right evidence image | image fill hash `f01e1d802bbe4add596c24628a6ca1b04e804a10`, `804x443`, scale `CROP` |
| `6:322`-`6:324` | evidence highlights | overlay rectangles |

Observed Figma summary: `3` text nodes, `2` image fill nodes, `5` rectangles. Fonts are `Pretendard Medium`, `Pretendard SemiBold`, and `Pretendard Regular`.

## Component Model

- `JByond/Deck/EvidenceScreenshot`
- `JByond/Deck/EvidenceHighlight`
- `JByond/Deck/SlideHeader.centered`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:95` |
| Source mapping | `6:313 -> 28:95` |
| QA | full PNG byte-equal export, similarity `1.0000000000` |
| Scope status | root-structured clone; image assets extracted and component promotion completed in v1.0 |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `58:183` |
| Source mapping | `6:313 -> 28:95 -> 58:183` |
| Component sets | `JByond/Deck/EvidenceScreenshotExact/VariantSet` `58:175`; `JByond/Deck/EvidenceHighlightExact/VariantSet` `58:182` |
| Component instances | evidence screenshots `58:196`, `58:198`; highlights `58:200`, `58:202`, `58:204` |
| QA | `0` changed pixels, similarity `1.0000000000` |
| Visual diff | `qa/visual-diff/03-problem-evidence-componentized-v1.0.json` |
| Screenshot | `assets/rebuild-screenshots/03-problem-evidence-componentized-58-183.png` |

Decision: evidence images remain raster image-fill components because they are captured evidence material, not redrawable UI. Highlight rectangles are editable component instances so future evidence slides can reuse the overlay pattern without baking highlights into the images.

## QA Risks

- Evidence images must keep source/citation provenance. They are allowed raster assets, not UI components.
- Headline typo/spacing in source should be preserved in source clone, but derivative decks may need editorial correction.
