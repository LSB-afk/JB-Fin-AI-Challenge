---
tags:
  - area/product
  - type/index
  - status/active
date: 2026-07-09
up: "[[Presentation Assets Index]]"
---

# Overview Index

이 색인은 `presentation-assets/`의 상위 진입 문서를 정리한다.

| 문서 | 역할 | 읽는 시점 |
|---|---|---|
| [`../INDEX.md`](../INDEX.md) | 전체 문서 색인의 메인 진입점 | 항상 처음 |
| [`../deck-definition.md`](../deck-definition.md) | 발표덱의 철학, 서사, 시각 문법, 재현 원칙, 누락 리뷰 | 디자이너/PM/AI 빌더가 방향을 잡을 때 |
| [`../README.md`](../README.md) | 산출물 상태, Figma workspace, final page, rebuild node 현황 | 현재 상태를 빠르게 확인할 때 |
| [`../manifest.json`](../manifest.json) | source/rebuild/final Figma node, token system, QA status, machine-readable manifest | 자동화, 후속 에이전트, 검증 스크립트 |

## Root-Level Contract

| 항목 | 기준 |
|---|---|
| 프로젝트 목적 | 최종 Figma 발표덱을 반복 가능, 재사용 가능, 변형 가능한 디자인 자산으로 전환 |
| 최종 Figma page | `99 Final Componentized Deck` |
| Working file key | `h6RkEn7fGbTwZbzuwaHsWi` |
| 최종 frame 수 | 14 |
| QA 기준 | `1920x1080`, no full-slide flatten image, visual similarity `>= 0.98`, token/component/asset ledger 기록 |

## Adjacent Category Indexes

| 색인 | 설명 |
|---|---|
| [`02-slides.md`](02-slides.md) | slide별 source-analysis와 inventory |
| [`03-design-system.md`](03-design-system.md) | token/component 문서 |
| [`04-assets.md`](04-assets.md) | asset/font/vector 문서 |
| [`05-qa.md`](05-qa.md) | QA와 visual diff 문서 |
| [`06-process.md`](06-process.md) | process, prompt, agent 운영 문서 |
