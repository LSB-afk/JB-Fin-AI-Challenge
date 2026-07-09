---
tags:
  - area/product
  - type/runbook
  - status/active
date: 2026-07-09
up: "[[JByond Presentation Assetization Handoff]]"
---

# AI Reuse Runbook

이 문서는 AI가 JByond 발표덱 자산을 재사용해 새 Figma 슬라이드나 blind rebuild를 만들 때 따라야 할 절차다.

## 1. Input Contract

AI에게 최소한 다음 입력을 제공한다.

| 입력 | 위치 | 용도 |
|---|---|---|
| Deck definition | [`../deck-definition.md`](../deck-definition.md) | 철학, 서사, 시각 문법 |
| Document index | [`../INDEX.md`](../INDEX.md) | 필요한 문서 탐색 |
| Manifest | [`../manifest.json`](../manifest.json) | Figma node-id, final page, status |
| Slide spec | `../slides/<slide>-source-analysis.md` | 해당 slide의 구조와 내용 |
| Token index | [`../tokens/token-index.json`](../tokens/token-index.json) | token source of truth |
| Component catalog | [`../components/component-catalog.md`](../components/component-catalog.md) | 사용 가능한 component와 variants |
| Asset ledger | [`../assets/asset-ledger.md`](../assets/asset-ledger.md) | 이미지/폰트/캡처 출처 |
| Prompt history | [`../process/rebuild-prompts.md`](../process/rebuild-prompts.md) | 기존 build prompt와 QA 기준 |
| QA rules | [`../tokens/qa-rules.json`](../tokens/qa-rules.json) | 검증 기준 |

## 2. Build Modes

| Mode | 목적 | 원본 frame 접근 | 성공 기준 |
|---|---|---|---|
| Source-preserving rebuild | 원본과 거의 같은 구조화 복제 | 허용 | visual similarity `>= 0.98`, no full-slide flatten |
| Componentized rebuild | 반복 요소를 component instance로 치환 | 허용 | visual similarity `>= 0.98`, component ledger 업데이트 |
| Blind rebuild | 문서/자산/토큰만으로 재생성 | 금지 | 원본 대비 diff 기록, 실패 원인 문서화 |
| Derivative slide | 새로운 내용으로 같은 문법 적용 | 원본은 reference만 | deck philosophy와 token/component 사용 준수 |

## 3. AI Build Procedure

1. `deck-definition.md`를 읽고 이 덱이 “통제 가능한 금융 AI 운영체계”를 보여준다는 점을 고정한다.
2. 만들 slide의 목적을 정한다.
3. 관련 `slides/*-source-analysis.md`를 읽는다.
4. `tokens/token-index.json`에서 primitive, semantic, component token 파일을 따라간다.
5. `components/component-catalog.md`에서 재사용 가능한 component family를 고른다.
6. `assets/asset-ledger.md`에서 필요한 raster-allowed material을 확인한다.
7. Figma에는 새 page 또는 새 frame을 만든다. source/final frame을 덮어쓰지 않는다.
8. full-slide screenshot을 추출하고 visual diff를 계산한다.
9. 결과를 `qa/rebuild-diff.md` 또는 별도 eval 문서에 기록한다.

## 4. Copy-Paste AI Prompt

```text
You are rebuilding or extending the JByond presentation deck as a reusable Figma design asset.

Read these source documents first:
- presentation-assets/deck-definition.md
- presentation-assets/INDEX.md
- presentation-assets/manifest.json
- presentation-assets/slides/<SLIDE_SPEC>.md
- presentation-assets/tokens/token-index.json and referenced token files
- presentation-assets/components/component-catalog.md
- presentation-assets/assets/asset-ledger.md
- presentation-assets/process/rebuild-prompts.md

Design intent:
- This is not a generic AI pitch deck.
- It is an enterprise financial AI operating-system deck.
- The visual language is dark control-room, evidence-first, dense but navigable.
- AI must appear controllable, auditable, and role-based.

Build rules:
- Canvas must be 1920x1080.
- Do not use a full-slide flattened screenshot as the rebuild content.
- Use tokens before raw values.
- Use existing component families when available.
- Raster is allowed only for product UI captures, evidence captures, photo/background material, and documented image fills.
- Keep headline, labels, tables, flow nodes, entity pills, and Gantt rows editable when feasible.
- Do not mutate source frames.
- If Panchang or Pretendard is unavailable, preserve source text metadata or record the font risk.

Output:
- Figma page/frame name
- Created node IDs
- Component instances used
- Assets used with ledger references
- Token files referenced
- Visual QA result
- Any drift, missing font, clipping, or rasterization caveat
```

## 5. Blind Rebuild Prompt

```text
Run a blind rebuild test for slide <SLIDE_NO>.

You may use:
- deck-definition.md
- INDEX.md
- manifest.json only for source file identity and final QA references
- the slide source-analysis markdown
- tokens/*
- components/component-catalog.md
- assets/asset-ledger.md
- process/rebuild-prompts.md

You may not inspect or clone the original source frame or the accepted final frame during build.

Create a new Figma page named:
Blind Rebuild / <SLIDE_NO> / <DATE>

Create one 1920x1080 frame named:
S<SLIDE_NO>/<ROLE>/Blind Rebuild v0.1

After building, compare against the accepted final frame only for QA.
Record:
- similarity
- changed pixels
- visible drift areas
- missing tokens/assets/components
- document gaps that prevented accurate reconstruction
```

## 6. Required QA After AI Build

| Check | Required |
|---|---|
| Frame size | `1920x1080` |
| Full-slide flatten | Must be absent |
| Text clipping | Must be absent |
| Component use | Required for repeated elements |
| Token use | Required when token exists |
| Asset provenance | Required for every raster material |
| Visual diff | Required for rebuilds |
| Drift notes | Required when similarity is below accepted baseline |

## 7. Failure Handling

If the rebuild fails, do not simply “make it look nicer.” Record what failed.

| Failure | 기록할 내용 |
|---|---|
| Font mismatch | font, affected text role, fallback behavior |
| Layout drift | affected zone, expected anchor, actual offset |
| Component mismatch | component used, missing variant, source geometry issue |
| Asset mismatch | missing source, crop issue, raster policy |
| Token gap | raw value needed, proposed token name |
| QA drift | changed pixels, similarity, bbox if available |
