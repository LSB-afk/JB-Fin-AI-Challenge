---
tags:
  - area/product
  - type/design-token-schema
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# Token Schema Extension

기존 `presentation-tokens.json`은 색/타입/간격 요약에는 충분하지만, 발표덱 재구성에는 부족하다. Pilot v1부터 `token-index.json` 아래 split token files를 source of truth로 사용하고, 다음 확장 타입을 추가한다.

## Source Refs

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `figmaOriginalNodeId` | string | yes | 원본 읽기 전용 Figma node-id, 예: `5053:11835` |
| `pastedWorkingNodeId` | string | yes | 작업 Figma에 사용자가 붙여 넣은 editable source node-id, 예: `6:198` |
| `structuredRebuildNodeId` | string/null | no | 구조화 복제본 node-id, 예: `22:2` |
| `localPixelReference` | path | yes | QA 기준 스크린샷 |
| `sourcePriority` | array | yes | `pastedWorkingNodeId -> figmaOriginalNodeId -> localPixelReference -> finalPdf` 순서 |

## Surface

`surface`는 단일 색이 아니라 fill, opacity, blur, border, blend mode, mask, crop을 묶은 재료다.

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `fills` | array | yes | SOLID, GRADIENT, IMAGE fill stack |
| `blendMode` | string | yes | Figma blend mode |
| `backdropBlur` | number/null | no | glass/backdrop blur 값 |
| `border` | token/null | no | stroke token reference |
| `mask` | string/null | no | rounded-rectangle/image mask 종류 |
| `imageTransform` | matrix/null | no | Figma image crop/transform matrix |

## Font Asset

`fontAsset`은 typography token과 분리한다. typography는 역할별 사용값이고, font asset은 폰트 파일과 권리/가용성 정보다.

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `family` | string | yes | Figma font family |
| `style` | string | yes | Figma style string |
| `weight` | number | yes | CSS weight |
| `provider` | string | yes | Fontshare, local, unknown 등 |
| `localFile` | path/null | no | 재현 가능한 font binary |
| `sha256` | string/null | no | local font file hash |
| `licenseStatus` | string | yes | 배포 전 확인 상태 |
| `figma.hasMissingFont` | boolean | yes | Plugin API 기준 missing font 여부 |

## Raster Asset

`rasterAsset`은 “이미지를 써도 되는지”와 “어디까지 편집 가능한지”를 동시에 기록한다.

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `path` | path | yes | 추출/파생 이미지 경로 |
| `sourceNodeId` | string | yes | Figma image fill node-id |
| `pixelSize` | object | yes | 원본 이미지 픽셀 크기 |
| `placement` | object | yes | slide 안의 x/y/w/h |
| `scaleMode` | string | yes | Figma image scale mode |
| `imageTransform` | matrix/null | no | crop/transform |
| `figmaImageHash` | string/null | no | Figma internal image hash |
| `editableBoundary` | string | yes | placement만 editable인지, 내부 UI도 editable인지 |

## Effect Stack

`effectStack`은 gradient, shadow, blur, stroke, blend를 z-order와 함께 기록한다.

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `zPath` | string | yes | source layer z-order path |
| `fills` | array | no | fill stack |
| `effects` | array | no | shadow/blur/glass effects |
| `opacity` | number | yes | layer opacity |
| `blendMode` | string | yes | layer blend mode |
| `sourceNodeId` | string | yes | Figma source node |

## Component Slots

`component` token은 단순 component 이름 목록이 아니라 slots와 props까지 포함해야 한다.

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `slots` | object | no | text/image/icon/table row 같은 교체 가능 영역 |
| `variantProps` | object | no | `tone`, `size`, `state`, `align` 등 |
| `sourceNodes` | array | no | 반복 패턴의 근거 node-id |
| `editableRequirements` | array | yes | flatten 금지 대상 |
| `rasterAllowed` | array | no | 예외적으로 raster 허용되는 slot |

## QA Provenance Checks

| Field | Type | Required | Purpose |
|---|---|---:|---|
| `visualDiff.source` | path | yes | 비교 원본 |
| `visualDiff.rebuild` | path | yes | 비교 대상 |
| `visualDiff.changedPixels` | number | yes | 픽셀 차이 |
| `visualDiff.similarity` | number | yes | `1 - changedPixels / totalPixels` |
| `layerCompleteness` | object | yes | source layer와 rebuild layer 매핑 |
| `fontGate` | object | yes | missing font / text mutation 가능 여부 |

## 01 Summary Filled Example

```json
{
  "sourceRefs": {
    "figmaOriginalNodeId": "5053:11835",
    "pastedWorkingNodeId": "6:198",
    "structuredRebuildNodeId": "22:2",
    "localPixelReference": "assets/rebuild-screenshots/01-summary-source-6-198.png",
    "sourcePriority": ["pastedWorkingNodeId", "figmaOriginalNodeId", "localPixelReference", "finalPdf"]
  },
  "fontAsset": "{fontAsset.panchang.medium}",
  "surface": "{surface.stage.cover}",
  "rasterAsset": "{surface.image.coverLaptop}",
  "qa": "qa/visual-diff/01-summary-structured-v1.json"
}
```
