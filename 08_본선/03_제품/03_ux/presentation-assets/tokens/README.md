---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Presentation Token System

이 폴더의 기준은 `token-index.json`이다. `presentation-tokens.json`은 초기 flat token 호환용 요약이며, A5 Figma Builder와 AI rebuild는 아래 분리 파일을 우선 사용한다.

| File | Role |
|---|---|
| `primitives.json` | Figma에서 읽은 raw color/type/space/radius/stroke/frame 값 |
| `semantic.json` | stage, surface, text, line, accent 같은 의미 토큰 |
| `typography.json` | 텍스트 role별 font/style/size/line-height/letter-spacing/source node |
| `fonts.json` | 폰트 원천, local file, hash, Figma missing-font 상태 |
| `effects.json` | gradient, image treatment, shadow, stroke recipe |
| `surfaces.json` | fill stack, glass, image mask/crop, panel/table surface recipe |
| `components.json` | `JByond/Deck/*` component별 token contract |
| `slides.json` | `01`, `07`, `09` slide별 layout zone과 editable/raster boundary |
| `assets.json` | source screenshot, Figma image-fill node, raster 허용 정책 |
| `qa-rules.json` | rebuild 검증 규칙 |
| `figma-variable-map.json` | Figma variable/style/component 생성 매핑 |
| `schema-extension.md` | MD로 담기 어려운 source/font/surface/raster/effect/component/QA schema 정의 |
| `token-registry.csv` | 사람이 빠르게 훑는 token 색인 |
| `presentation-tokens.css` | HTML/SVG/local harness용 CSS variable export |
| `specimens/token-specimen.svg` | token visual specimen |

## Source Priority

1. Pasted editable working Figma nodes in `h6RkEn7fGbTwZbzuwaHsWi`: `6:198`, `6:325`, `6:1046`
2. Original read-only Figma nodes: `5053:11835`, `5053:11964`, `5053:12685`
3. Local full-slide PNG/JPG exports for visual QA
4. Final PDF for page order and packaging baseline
5. Earlier Markdown analysis only as interpretation aid

## Builder Rule

Figma rebuild code must not hardcode colors, sizes, or typography when an equivalent token exists. Raw values are allowed only while measuring source nodes or when a new token is being proposed.
