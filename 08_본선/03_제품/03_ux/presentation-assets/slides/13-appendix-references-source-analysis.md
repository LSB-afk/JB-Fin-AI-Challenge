---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 13 Appendix References Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/13 Appendix.jpg` |
| Deck audit node-id | `4977:5378` |
| Pasted working node-id | `6:1586` |
| Structured rebuild node-id | `29:214` |
| QA reference | `qa/visual-diff/full-deck-structured-audit-2026-07-09.json` |
| Figma access | `metadata_ok` |

## Message

발표자료의 통계·법령·데이터·기술·문헌 출처와 검증 상태를 한 장에 통합한 appendix다. 재사용 시에는 디자인 자산뿐 아니라 evidence ledger로도 취급해야 한다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Header | `Appendix` pill + title + subtitle | editable text |
| Column 1 | 통계·수치 출처 | `ReferenceColumn` |
| Column 2 | 법령·규제, 활용 데이터, 기술 스택 | `ReferenceColumn` with section headings |
| Column 3 | 연구·문헌, 검증요약 | `ReferenceColumn` + `VerificationSummary` |

## Key Sections

- `통계 · 수치 출처`
- `법령 · 규제 근거`
- `활용 데이터`
- `기술 스택 · 모델`
- `연구 · 문헌`
- `검증 결과 요약 · 2026-07-05 적대적 재검증`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:1587` | header | appendix pill/title/subtitle |
| `6:1593` | statistics column | items include 피해자 누적 인정, HUG 보증사고액, 보이스피싱 피해액, 자영업자 지표 |
| `6:1631` | regulation/data/tech column | legal clauses, data sources, model/runtime stack |
| `6:1696` | literature/verification column | Gartner TX, Service-Profit Chain, Prediction Machines, KLM, verification summary |

## Component Model

- `JByond/Deck/ReferenceColumn`
- `JByond/Deck/ReferenceItem`
- `JByond/Deck/ReferenceDomain`
- `JByond/Deck/VerificationSummary`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `29:214` |
| Source mapping | `6:1586 -> 29:214` |
| QA | full PNG byte-equal export, similarity `1.0000000000` |
| Scope status | root-structured clone; evidence ledger normalization pending |

## Componentized Rebuild V1.0

| 항목 | 값 |
|---|---|
| Figma node | `80:688` |
| Component sets | `79:736` `JByond/Deck/ReferenceItem2LineExact/VariantSet`; `79:832` `JByond/Deck/ReferenceItem3LineExact/VariantSet`; `79:849` `JByond/Deck/VerificationSummaryRowExact/VariantSet` |
| Replaced source units | `31` reference item frames and `4` verification summary rows |
| Instance count | `35` component instances |
| Screenshot | `assets/rebuild-screenshots/13-appendix-componentized-80-688.png` |
| Component evidence | `assets/components/reference-item-2line-exact-variant-set-79-736.png`; `assets/components/reference-item-3line-exact-variant-set-79-832.png`; `assets/components/verification-summary-row-exact-variant-set-79-849.png` |
| QA | `0` changed pixels, similarity `1.0000000000`; see `qa/visual-diff/13-appendix-componentized-v1.0.json` |
| Scope status | repeated reference rows componentized; source URL/file provenance still needs structured evidence ledger normalization |

## QA Risks

- Source contains date-specific and law-specific claims; this slide must be reviewed before reuse after 2026-07-05.
- Several items are caveated as partial checks or scenarios. Preserve caution labels.
- This slide should eventually sync to a structured evidence table, not only markdown.
