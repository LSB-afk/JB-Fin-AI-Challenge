---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 02 Problem Definition Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/02 문제정의.jpg` |
| Deck audit node-id | `4815:9181` |
| Pasted working node-id | `6:3` |
| Structured rebuild node-id | `28:2` |
| QA reference | `qa/visual-diff/02-problem-structured-v1.json` |
| Figma access | `metadata_partial_ok` |

## Message

기존 금융 업무는 고객 신호가 `Case`로 묶이지 않아 RM이 여러 시스템과 근거를 직접 읽고 판단해야 한다. 이 장은 여러 지역/업무 케이스를 카드로 보여주고, 챗봇·대시보드·RPA의 한계를 비교한다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | 딥 네이비 배경 이미지/gradient | `FrameDark.deep` |
| Header | `Problem Definition` pill + 대형 문제 문장 + 설명문 | editable text |
| Case cards | 5개 업무/고객 상황 카드, 중앙 3장 강조 + 양끝 일부 crop | `ComparisonCard` / `CaseSignalCard` |
| Existing approach table | 챗봇·대시보드·RPA와 한계 문장, arrow connector | editable row stack + vectors |
| Scenario note | `가상 시나리오 (지역 통계·기사 기반 구성)` | editable footnote |

## Text Inventory

- `Problem Definition`
- `분리된 케이스를 RM이 일일이 읽고, 근거를 찾아서 계속 판단해 넘겨야 한다는 점`
- `전북은행 RM은 여신·사후관리 케이스를 처리할 때 매번 고객 상태, 거래 신호, 서류, 정책·규제 근거를 여러 시스템에서 직접 확인해야 한다.`
- Case examples:
  - `오** 39세 (전북 군산시)` / `기업여신·기술신용` / `JB우리캐피탈`
  - `임** (전북 전주시)` / `학생 생활비·학자금 대출` / `전북은행`
  - `문** 45세 (전남 완도군)` / `수산업 운전자금` / `광주은행`
  - `문** 54세 (전남 완도군)` / `수산업 운전자금` / `전북은행`
  - `송** 50세 (전남 해남군)` / `농수산 여신 사후 관리` / `전북은행`
- Existing approach rows:
  - `챗봇` -> `사용자가 질문을 잘해야함`
  - `대시보드` -> `현황은 보이지만 다음 역할로 흐르지 않음`
  - `RPA` -> `특정 반복 업무에만 제한적으로 작동`

## Figma Layer Summary

| Source node | Role | Notes |
|---|---|---|
| `6:4` | background image/gradient | full-slide deep navy background |
| `6:5` | header group | pill, headline, supporting copy |
| `6:11`, `6:25`, `6:39`, `6:55`, `6:69` | case cards | repeated card pattern; center cards full, side cards cropped |
| `6:83`-`6:91` | existing approach table | explanation and three limitation rows |
| `6:92`-`6:94` | row arrows | vector connectors |
| `6:95` | scenario note | source caveat |

Observed Figma summary: `43` text nodes, `3` visible vector arrows, dominant fonts `Pretendard Medium`, `Pretendard SemiBold`, `Pretendard Regular`, and `Pretendard Light`.

## Component Model

- `JByond/Deck/CaseSignalCard`
- `JByond/Deck/ComparisonLimitRow`
- `JByond/Deck/ScenarioFootnote`
- `JByond/Deck/SlideHeader`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:2` |
| Source mapping | `6:3 -> 28:2` |
| QA | `41` changed pixels, similarity `0.9999802276` |
| Scope status | structured baseline preserved; componentized baseline accepted as `49:76` |

## Componentized Rebuild Loop

| Version | Figma node | Component sets | QA | Decision |
|---|---|---|---|---|
| v1.1 | `46:2` | `ProblemCaseCard/VariantSet=39:77`, `LimitationRow/VariantSet=42:17` | `12,689` changed pixels, similarity `0.9938806906` | 98% gate는 통과했지만 row text/arrow geometry drift가 보여 최종 baseline으로는 보류 |
| v1.2 | `49:76` | `ProblemCaseCard/VariantSet=39:77`, `LimitationRowExact/VariantSet=48:88` | `453` changed pixels, similarity `0.9997815394` | current componentized baseline |

Reasoning: card components were visually stable, but the broad `LimitationRow` component normalized row width/height and shifted arrows/text. `LimitationRowExact` preserves the original row origin, arrow offsets, and text bounds from structured source nodes `28:83`, `28:88`, `28:91`, `28:86`, `28:89`, `28:92`, `28:87`, `28:90`, `28:93`.

## QA Risks

- Case cards have many nested small text nodes; component promotion must preserve crop and card shadow.
- Scenario content is explicitly synthetic; derivative decks need the same caveat.
- This slide has no extracted image assets yet. The case cards are editable text/shape layers in Figma and should not be replaced by raster screenshots.
