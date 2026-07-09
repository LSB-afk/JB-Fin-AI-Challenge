---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# 01 Summary Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `assets/source-screenshots/01-summary.jpg` |
| Deck audit node-id | `4915:2719` |
| Provided URL candidate | `5053:11835` |
| Pasted working node-id | `6:198` |
| Pasted working screenshot | `assets/pasted-working-screenshots/01-summary-6-198.png` |
| Figma access | `working_source_available_in_h6RkEn7fGbTwZbzuwaHsWi` |

## Message

`JByond`를 첫 화면에서 제품명으로 각인시키고, "금융 Case -> AI Agent 근거 정리 -> 사람 승인 -> 감사 로그"라는 제품 정의를 한 문장으로 전달한다. 이 슬라이드는 전체 assetization의 calibration slide다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | 딥 네이비-블루 사진형 배경, 좌하단 어둡고 우상단 밝음 | `Deck/BackgroundImage` image fill + overlay |
| Eyebrow | 상단 중앙 `Local Guard OS | Summary` | editable text |
| Headline | 상단 중앙 2줄 한글 설명, 핵심 단어 흰색 강조 | editable rich text 또는 2개 text layer |
| Product title | 화면 중앙을 가로지르는 초대형 `JByond` | editable text, tracking/opacity 조정 |
| Device mockup | 중앙 노트북 목업과 RM 포털 화면 | image asset, 별도 crop frame |
| Footer | 좌측 대회명, 우측 팀/팀원 | editable text |

## Text Inventory

- `Local Guard OS | Summary`
- `금융 Case가 들어오면 AI Agent가 근거를 정리하고, 사람은 승인하며,`
- `모든 판단과 데이터 사용이 감사 로그로 남는 금융 AI 운영 콘솔`
- `JByond`
- `JB금융그룹 Fin:AI Challenge`
- `GoLab 이승보 김주용 김민주 이재형`

## Visual Recipe

- Canvas: `1920x1080`
- Background: full-bleed image with blue overlay, no card frame
- Main title: extremely large white text crossing laptop image; treat as brand layer, not decoration
- Device: centered, approx lower-middle; screenshot inside laptop is not rebuilt in pilot unless Figma original exposes separate image
- Footer: small white text, 36-40px margins from edges

## Editable Layer Model

1. `SlideFrame/01 Summary`
2. `Background/blue-photo`
3. `Overlay/blue-vignette`
4. `Text/Eyebrow`
5. `Text/HeadlineLine1`
6. `Text/HeadlineLine2`
7. `Image/LaptopMockup`
8. `Text/ProductName`
9. `Text/FooterEvent`
10. `Text/FooterTeam`

## Pasted Source Layer Inventory

Primary source is now the pasted editable Figma node `6:198` in `h6RkEn7fGbTwZbzuwaHsWi`. Local JPG/PDF exports are fallback references only.

| z | Source node | Type | Structured node | Role name | x | y | w | h | Key style / asset |
|---:|---|---|---|---|---:|---:|---:|---:|---|
| 0 | `6:198` | FRAME | `22:2` | `S01/Summary/Structured Rebuild v1.0` | 0 | 0 | 1920 | 1080 | stage gradient `#08124A -> #6583EC -> #08124A` |
| 1 | `6:199` | RECTANGLE | `22:3` | `Asset/CoverStageImage` | 357 | 234 | 1205 | 904 | image fill, active hash `8bc0a0c02f87f84ead092948aabd1d878f8f8364`, scale `FILL` |
| 2 | `6:200` | FRAME | `22:4` | `TextGroup/CoverHeader` | 288 | 79 | 1344 | 155 | header text group |
| 2.1 | `6:201` | TEXT | `22:5` | `Text/CoverEyebrow` | 0 | 0 | 1344 | 28 | Pretendard SemiBold 25, line-height 110%, white 60%, center |
| 2.2 | `6:202` | TEXT | `22:6` | `Text/CoverStatement` | 0 | 51 | 1344 | 104 | Pretendard Medium 40, line-height 130%, letter-spacing -2%, mixed fill |
| 3 | `6:203` | VECTOR | `22:7` | `Vector/HandAccent` | 833 | 945.5 | 73.658 | 53.46 | fill `#344895` |
| 4 | `6:204` | RECTANGLE | `22:8` | `Asset/ProductLaptopImage` | 447 | 257 | 1026 | 702 | image fill, active hash `0ce013a6187f2589651792e1e79188e43955f00b`, scale `FILL` |
| 5 | `6:205` | VECTOR | `22:9` | `Overlay/BottomVeilBase` | 0 | 271 | 1920 | 829 | vector overlay, no visible fill reported |
| 6 | `6:206` | VECTOR | `22:10` | `Overlay/BottomVeilGradient` | 0 | 234 | 1920 | 829 | gradient opacity 20%, `#5A76DD00 -> #283B7F` |
| 7 | `6:207` | TEXT | `22:11` | `Text/FooterEvent` | 38 | 1021 | 301 | 28 | Pretendard Regular 25, line-height 110%, `#F8F8F8` |
| 8 | `6:208` | TEXT | `22:12` | `Text/FooterTeam` | 1524 | 1021 | 365 | 28 | Pretendard Regular 25, line-height 110%, white 80% |
| 9 | `6:209` | TEXT | `22:13` | `Text/HeroWordmark` | 84 | 414 | 1764 | 330 | Panchang Medium 300, line-height 110%, letter-spacing 9% |

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `22:2` |
| 위치 | `x=28148`, `y=0`, `1920x1080` |
| Source mapping | `6:198 -> 22:2`, child layers mapped by z-order |
| Source screenshot | `assets/rebuild-screenshots/01-summary-source-6-198.png` |
| Rebuild screenshot | `assets/rebuild-screenshots/01-summary-structured-22-2.png` |
| Pixel diff | `0 / 2,073,600` changed pixels, similarity `1.0000000000` |
| QA status | `pass_pixel_identical` |

This rebuild intentionally clones the pasted editable source instead of redrawing from placeholders. It preserves original image fills, text nodes, vector overlays, blend modes, and Figma font metadata, then adds stable role names and `jbyond` shared plugin metadata.

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `93:1179` |
| 위치 | `x=89741.3125`, `y=0`, `1920x1080` |
| Component instances | `CoverMediaStackExact=92:1179`, `CoverHeaderExact=92:1188`, `CoverFooterExact=92:1189`, `CoverWordmarkExact=92:1192` |
| Rebuild screenshot | `assets/rebuild-screenshots/01-summary-componentized-93-1179.png` |
| QA record | `qa/visual-diff/01-summary-componentized-v1.0.json` |
| QA status | `pass_tolerance_delta_le_1` |

Componentization keeps the visual source intact while reducing the rebuilt frame to four reusable instances:

- `JByond/Deck/CoverMediaStackExact`: stage image, laptop image, hand accent, and veil overlays.
- `JByond/Deck/CoverHeaderExact`: eyebrow and headline group.
- `JByond/Deck/CoverFooterExact`: event and team footer.
- `JByond/Deck/CoverWordmarkExact`: editable Panchang `JByond` wordmark.

The plugin runtime could not load `Pretendard`, so text nodes were cloned into components without mutating characters, font, line-height, or fill metadata. Exact-pixel comparison reports many one-channel deltas from Figma instance rendering, but `maxChannelDelta=1`; with `pixelTolerancePerChannel=1`, changed pixels are `0 / 2,073,600` and similarity is `1.0000000000`.

## Rebuild Notes

- `JByond` must stay editable text. Do not flatten it into the background. Use `Panchang Medium` from `assets/fonts/panchang/Panchang-Medium.woff2` when rebuilding outside Figma.
- Laptop mockup can remain image fill in pilot because it is a visual product hero, not reusable UI structure.
- The headline should be editable and preserve mixed emphasis.
- Exact background and laptop image layers are available in the pasted working source: `6:199` and `6:204`.

## QA Risks

- Large `JByond` can visually drift if font weight or letter spacing differs.
- Background and laptop are no longer only flattened JPG references; they are available as separate image layers in pasted working node `6:198`.
- Footer team spelling must remain `GoLab`, while some docs use `Go Lab`; keep manifest note until final team spelling is decided.
