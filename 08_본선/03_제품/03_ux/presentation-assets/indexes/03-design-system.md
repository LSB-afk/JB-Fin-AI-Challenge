---
tags:
  - area/product
  - type/index
  - status/active
date: 2026-07-09
up: "[[Presentation Assets Index]]"
---

# Design System Index

이 색인은 token system, component catalog, token export 문서를 정리한다.

## Component Catalog

| 문서 | 역할 |
|---|---|
| [`../components/component-catalog.md`](../components/component-catalog.md) | Figma component naming, promoted component sets, candidates, promotion queue, component gate |

## Token Entry Points

| 문서 | 역할 |
|---|---|
| [`../tokens/README.md`](../tokens/README.md) | token system 설명과 source priority |
| [`../tokens/token-index.json`](../tokens/token-index.json) | token system의 machine-readable index |
| [`../tokens/token-notes.md`](../tokens/token-notes.md) | 사람이 읽는 token 해석 노트 |
| [`../tokens/schema-extension.md`](../tokens/schema-extension.md) | MD로 담기 어려운 source/font/surface/raster/effect/component/QA schema 정의 |
| [`../tokens/token-registry.csv`](../tokens/token-registry.csv) | 빠르게 훑는 token registry |

## Token Source Files

| 문서 | 역할 |
|---|---|
| [`../tokens/primitives.json`](../tokens/primitives.json) | raw color/type/space/radius/stroke/frame 값 |
| [`../tokens/semantic.json`](../tokens/semantic.json) | stage, surface, text, line, accent 의미 토큰 |
| [`../tokens/typography.json`](../tokens/typography.json) | text role, font/style/size/line-height/source node |
| [`../tokens/fonts.json`](../tokens/fonts.json) | font source, local files, Figma missing-font 상태 |
| [`../tokens/effects.json`](../tokens/effects.json) | gradient, shadow, image treatment, stroke recipe |
| [`../tokens/surfaces.json`](../tokens/surfaces.json) | fill stack, glass, mask/crop, panel/table surface recipe |
| [`../tokens/components.json`](../tokens/components.json) | `JByond/Deck/*` component token contract |
| [`../tokens/slides.json`](../tokens/slides.json) | slide별 layout zone, editable/raster boundary |
| [`../tokens/assets.json`](../tokens/assets.json) | source screenshot, Figma image-fill node, raster policy |
| [`../tokens/qa-rules.json`](../tokens/qa-rules.json) | rebuild 검증 규칙 |
| [`../tokens/assetization-backlog.json`](../tokens/assetization-backlog.json) | machine-readable material extraction and component promotion backlog |
| [`../tokens/figma-variable-map.json`](../tokens/figma-variable-map.json) | Figma variable/style/component 생성 매핑 |

## Token Exports And Specimens

| 문서 | 역할 |
|---|---|
| [`../tokens/presentation-tokens.json`](../tokens/presentation-tokens.json) | 초기 flat token 호환용 요약 |
| [`../tokens/presentation-tokens.css`](../tokens/presentation-tokens.css) | HTML/SVG/local harness용 CSS variable export |
| [`../tokens/specimens/token-specimen.svg`](../tokens/specimens/token-specimen.svg) | token visual specimen |

## Read Order

1. [`../tokens/README.md`](../tokens/README.md)
2. [`../tokens/token-index.json`](../tokens/token-index.json)
3. [`../tokens/primitives.json`](../tokens/primitives.json), [`../tokens/semantic.json`](../tokens/semantic.json), [`../tokens/components.json`](../tokens/components.json)
4. [`../components/component-catalog.md`](../components/component-catalog.md)
