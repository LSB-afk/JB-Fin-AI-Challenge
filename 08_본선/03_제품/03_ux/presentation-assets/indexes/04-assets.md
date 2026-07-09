---
tags:
  - area/product
  - type/index
  - status/active
date: 2026-07-09
up: "[[Presentation Assets Index]]"
---

# Assets Index

이 색인은 자산 관련 문서와 source asset index를 정리한다. 이미지 파일 자체는 수가 많으므로 여기서 전부 나열하지 않고, [`../assets/asset-ledger.md`](../assets/asset-ledger.md)를 기준 색인으로 둔다.

## Asset Ledgers

| 문서 | 역할 |
|---|---|
| [`../assets/asset-ledger.md`](../assets/asset-ledger.md) | full-slide reference, rebuild screenshot, component evidence, extracted images, font, source node, hash, raster policy |
| [`../tokens/assets.json`](../tokens/assets.json) | machine-readable asset/source/raster policy |
| [`../tokens/assetization-backlog.json`](../tokens/assetization-backlog.json) | slide별 material extraction 및 component promotion backlog |

## Font Assets

| 문서 | 역할 |
|---|---|
| [`../assets/fonts/panchang/README.md`](../assets/fonts/panchang/README.md) | Panchang font package 설명 |
| [`../assets/fonts/panchang/fontshare-panchang.css`](../assets/fonts/panchang/fontshare-panchang.css) | Fontshare Panchang CSS source |
| [`../tokens/fonts.json`](../tokens/fonts.json) | font source, local file, Figma runtime status |

## Vector Source Files

| 문서 | 역할 |
|---|---|
| [`../assets/vectors/01-summary/rectangle-240654842.svg`](../assets/vectors/01-summary/rectangle-240654842.svg) | slide 01 vector/source shape |
| [`../assets/vectors/01-summary/rectangle-240654843.svg`](../assets/vectors/01-summary/rectangle-240654843.svg) | slide 01 vector/source shape |
| [`../assets/vectors/01-summary/vector-27663.svg`](../assets/vectors/01-summary/vector-27663.svg) | slide 01 vector/source shape |

## Asset Image Directories

| 경로 | 역할 | 색인 기준 |
|---|---|---|
| `../assets/source-screenshots/` | local source screenshot references | [`../assets/asset-ledger.md`](../assets/asset-ledger.md) |
| `../assets/pasted-working-screenshots/` | pasted Figma source screenshots | [`../assets/asset-ledger.md`](../assets/asset-ledger.md) |
| `../assets/rebuild-screenshots/` | source/structured/componentized QA screenshots | [`../assets/asset-ledger.md`](../assets/asset-ledger.md), [`05-qa.md`](05-qa.md) |
| `../assets/components/` | component evidence screenshots | [`../assets/asset-ledger.md`](../assets/asset-ledger.md), [`../components/component-catalog.md`](../components/component-catalog.md) |
| `../assets/images/` | extracted slide material images | [`../assets/asset-ledger.md`](../assets/asset-ledger.md) |

## Asset Policy

- Full-slide screenshots are QA references only.
- Raster is allowed for product UI captures, evidence captures, photo/background material, and image fills with no editable source.
- Text, table, flow node, connector, label, entity pill, Gantt row must remain editable when feasible.
- Every reusable asset should have source slide, source node, path, hash/crop when available, and rebuild policy.
