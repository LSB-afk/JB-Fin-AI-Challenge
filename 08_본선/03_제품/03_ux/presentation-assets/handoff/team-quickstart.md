---
tags:
  - area/product
  - type/handoff
  - status/active
date: 2026-07-09
up: "[[JByond Presentation Assetization Handoff]]"
---

# Team Quickstart

이 문서는 팀원이 30분 안에 자산화 결과를 이해하고 자기 역할에 맞게 쓰도록 돕는 안내서다.

## 1. 한 문장 요약

이 패키지는 최종 발표용 Figma 덱을 **재구성 가능한 디자인 자산 세트**로 바꾼 결과다. 단순 PDF/PPT 보관이 아니라, slide blueprint, token, component, asset ledger, QA 기록, AI prompt/process log를 함께 남겼다.

## 2. 먼저 이해할 것

| 질문 | 답 |
|---|---|
| 이게 완전 자동 생성 증명인가? | 아니다. 현재는 원본 Figma layer를 보존한 source-preserving 복제/구조화/컴포넌트화 증명이다. |
| 그래도 재사용 가능한가? | 가능하다. 스크린샷, 청사진, 자산, 토큰, 컴포넌트, QA 루프가 있어서 Figma에서 같은 수준으로 재구성할 기반이 있다. |
| 최종 결과물은 어디 있나? | Figma file `h6RkEn7fGbTwZbzuwaHsWi`의 `99 Final Componentized Deck` page. |
| 문서의 시작점은? | [`../INDEX.md`](../INDEX.md), [`../deck-definition.md`](../deck-definition.md). |

## 3. 역할별 사용법

### Designer

1. [`../deck-definition.md`](../deck-definition.md)를 읽어 철학과 시각 문법을 파악한다.
2. Figma에서 `99 Final Componentized Deck` page를 열어 최종 14장을 본다.
3. [`../components/component-catalog.md`](../components/component-catalog.md)에서 어떤 요소가 component화됐는지 확인한다.
4. [`../tokens/README.md`](../tokens/README.md)와 [`../tokens/token-registry.csv`](../tokens/token-registry.csv)로 색, 폰트, surface, effect 계열을 확인한다.

### PM / Story Owner

1. [`../deck-definition.md`](../deck-definition.md)의 `Narrative Arc`를 읽는다.
2. [`../slides/_inventory-14.md`](../slides/_inventory-14.md)에서 14장 순서와 역할을 확인한다.
3. 새 발표 흐름을 만들 때는 기존 장표를 무작정 복사하지 말고 `Opening -> Problem -> Solution -> Proof -> Operating System -> Scenario -> Impact -> Execution -> Evidence` 흐름을 유지한다.

### AI Builder

1. [`ai-reuse-runbook.md`](ai-reuse-runbook.md)를 따른다.
2. 특정 slide를 만들 때 해당 [`../slides/*-source-analysis.md`](../slides/) 파일을 먼저 읽는다.
3. 토큰은 [`../tokens/token-index.json`](../tokens/token-index.json)을 기준으로 사용한다.
4. component는 [`../components/component-catalog.md`](../components/component-catalog.md)를 기준으로 사용한다.
5. 결과는 [`../qa/rebuild-diff.md`](../qa/rebuild-diff.md) 방식으로 검증한다.

### QA Reviewer

1. [`../qa/rebuild-diff.md`](../qa/rebuild-diff.md)에서 accepted baseline과 similarity를 확인한다.
2. slide별 JSON은 [`../qa/visual-diff/`](../qa/visual-diff/)에서 확인한다.
3. 새 rebuild는 full-slide screenshot, pixel diff, clipping, full-slide flatten 여부를 같이 본다.

## 4. 공유 받은 사람이 바로 해야 할 일

1. Figma에서 `99 Final Componentized Deck` page를 연다.
2. [`../deck-definition.md`](../deck-definition.md)를 읽는다.
3. 자기 역할에 맞는 문서만 추가로 읽는다.
4. 새 작업을 시작하기 전 [`share-checklist.md`](share-checklist.md)를 확인한다.

## 5. 금지 사항

- 원본 Figma source frame을 덮어쓰지 않는다.
- full-slide screenshot을 새 rebuild content로 쓰지 않는다.
- 토큰이 있는 값을 hardcode하지 않는다.
- Panchang/Pretendard font availability를 확인하지 않은 상태에서 새 텍스트를 대량 재입력하지 않는다.
- component promotion 후 QA diff 없이 accepted로 표시하지 않는다.
