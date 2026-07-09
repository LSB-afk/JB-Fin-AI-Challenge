---
tags:
  - area/product
  - type/index
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
aliases:
  - JByond 발표덱 문서 색인
  - presentation-assets index
---

# Presentation Assets Index

이 파일은 `presentation-assets/`의 메인 문서 색인이다. 문서가 많기 때문에 2계층으로 읽는다.

1. 먼저 아래 **Main Entry Points**에서 현재 목적에 맞는 진입점을 고른다.
2. 세부 파일은 **Category Indexes**의 하위 색인에서 찾는다.

## Main Entry Points

| 목적 | 먼저 볼 문서 | 설명 |
|---|---|---|
| 발표덱의 철학과 전체 정의 이해 | [`deck-definition.md`](deck-definition.md) | 시니어 디자이너/PM/AI 빌더가 먼저 읽는 상위 정의서 |
| 현재 산출물 상태 확인 | [`README.md`](README.md) | 전체 작업 상태, Figma 위치, QA 통과 현황 |
| 자동화/에이전트 기준 데이터 확인 | [`manifest.json`](manifest.json) | Figma node-id, source, final page, rebuild status |
| 14장 순서와 node 매핑 확인 | [`slides/_inventory-14.md`](slides/_inventory-14.md) | PDF 순서, source/rebuild/componentized node mapping |
| 디자인 시스템 구성 확인 | [`tokens/README.md`](tokens/README.md) | token system 진입점 |
| 컴포넌트 확인 | [`components/component-catalog.md`](components/component-catalog.md) | promoted/candidate component catalog |
| 자산 출처 확인 | [`assets/asset-ledger.md`](assets/asset-ledger.md) | 이미지, 폰트, 캡처, component evidence ledger |
| QA 결과 확인 | [`qa/rebuild-diff.md`](qa/rebuild-diff.md) | slide별 rebuild diff와 pass/fail |
| AI 제작 과정 확인 | [`process/ai-build-log.md`](process/ai-build-log.md) | decision log와 build loop |
| 다음 발표덱에 같은 방식 적용 | [`../../../../.agents/skills/figma-presentation-assetizer/SKILL.md`](../../../../.agents/skills/figma-presentation-assetizer/SKILL.md) | repo-local Codex skill entry |
| 작업 노하우 재사용 | [`../../../../.codex/presentation-assetization/references/operator-knowhow.md`](../../../../.codex/presentation-assetization/references/operator-knowhow.md) | 실패 모드, 판단 기준, 증명 수준 |

## Category Indexes

| 카테고리 | 색인 파일 | 포함 범위 |
|---|---|---|
| Overview | [`indexes/01-overview.md`](indexes/01-overview.md) | 루트 문서, Figma 위치, 최종 진입점 |
| Slides | [`indexes/02-slides.md`](indexes/02-slides.md) | 14장 source-analysis, inventory, backlog |
| Design System | [`indexes/03-design-system.md`](indexes/03-design-system.md) | tokens, component catalog, token specimen |
| Assets | [`indexes/04-assets.md`](indexes/04-assets.md) | asset ledger, fonts, vector source docs |
| QA | [`indexes/05-qa.md`](indexes/05-qa.md) | rebuild diff, PDF check, visual diff JSON |
| Process | [`indexes/06-process.md`](indexes/06-process.md) | prompts, AI build log, parallel agent model, Figma build ledger |
| Handoff | [`indexes/07-handoff.md`](indexes/07-handoff.md) | 팀 공유, Figma 사용, AI 재사용 runbook |

## Reading Paths

| 상황 | 읽는 순서 |
|---|---|
| 디자이너가 전체 의도를 파악 | `deck-definition.md` -> `README.md` -> `components/component-catalog.md` -> `tokens/README.md` |
| AI가 새 슬라이드를 재구성 | `deck-definition.md` -> `manifest.json` -> `slides/<slide>-source-analysis.md` -> `tokens/token-index.json` -> `components/component-catalog.md` -> `process/rebuild-prompts.md` |
| QA 담당자가 결과 검증 | `qa/rebuild-diff.md` -> `qa/visual-diff/*.json` -> `assets/rebuild-screenshots/` |
| 자산 출처 검토 | `assets/asset-ledger.md` -> `tokens/assets.json` -> `slides/*-source-analysis.md` |
| Figma 최종 결과 확인 | `README.md`의 `Final Figma Page` -> `manifest.json`의 `finalFigmaPage` |
| 팀원에게 공유 | `handoff/README.md` -> `handoff/team-quickstart.md` -> `handoff/share-checklist.md` |

## Current Figma Result

Working Figma file:

`https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`

최종 검토 페이지:

`99 Final Componentized Deck` / page id `106:1201`

14개 accepted componentized rebuild frame은 이 페이지에 PDF 순서대로 배치되어 있다.
