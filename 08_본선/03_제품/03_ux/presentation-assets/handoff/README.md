---
tags:
  - area/product
  - type/handoff
  - status/active
date: 2026-07-09
up: "[[Presentation Assets Index]]"
aliases:
  - JByond 발표덱 팀 공유 패키지
  - presentation handoff package
---

# JByond Presentation Assetization Handoff

이 폴더는 JByond 발표덱 자산화 결과를 팀원과 AI가 실제로 재사용할 수 있도록 만든 공유 패키지다.

원본 발표자료를 단순히 저장한 것이 아니라, 다음 목적을 위해 패키징했다.

- 디자이너가 발표덱의 철학과 시각 문법을 빠르게 이해한다.
- PM/기획자가 14장 흐름과 각 장의 역할을 확인한다.
- AI 빌더가 문서, 자산, 토큰, 컴포넌트로 새 Figma 슬라이드를 재생성한다.
- QA 담당자가 원본 대비 품질을 검증한다.

## Start Here

| 사용자 | 먼저 볼 문서 | 다음 문서 |
|---|---|---|
| 디자이너 | [`team-quickstart.md`](team-quickstart.md) | [`../deck-definition.md`](../deck-definition.md), [`figma-usage-guide.md`](figma-usage-guide.md) |
| PM/팀 리드 | [`team-quickstart.md`](team-quickstart.md) | [`../INDEX.md`](../INDEX.md), [`../slides/_inventory-14.md`](../slides/_inventory-14.md) |
| AI 빌더 | [`ai-reuse-runbook.md`](ai-reuse-runbook.md) | [`../process/rebuild-prompts.md`](../process/rebuild-prompts.md), [`../tokens/token-index.json`](../tokens/token-index.json) |
| QA 담당자 | [`share-checklist.md`](share-checklist.md) | [`../qa/rebuild-diff.md`](../qa/rebuild-diff.md), [`../qa/visual-diff/`](../qa/visual-diff/) |

## What Is Included

| 범주 | 위치 | 설명 |
|---|---|---|
| 상위 정의서 | [`../deck-definition.md`](../deck-definition.md) | 발표덱 철학, 서사, 시각 문법, 재현 원칙 |
| 전체 색인 | [`../INDEX.md`](../INDEX.md) | 모든 문서의 2계층 색인 |
| Figma 결과물 | `99 Final Componentized Deck` | 14장 최종 componentized rebuild page |
| 슬라이드 분석 | [`../slides/`](../slides/) | 14장 source-analysis와 inventory |
| 디자인 시스템 | [`../tokens/`](../tokens/), [`../components/`](../components/) | 토큰, 컴포넌트, 변수 매핑 |
| 자산 장부 | [`../assets/asset-ledger.md`](../assets/asset-ledger.md) | 이미지, 폰트, 캡처, component evidence |
| QA 기록 | [`../qa/`](../qa/) | visual diff, rebuild diff, PDF order check |
| AI 제작 로그 | [`../process/`](../process/) | prompt, decision, build log, agent model |

## Reusable Codex Workflow

다음 발표덱 자산화 프로젝트에서는 `$figma-presentation-assetizer`를 먼저 호출한다.

| 항목 | 위치 |
|---|---|
| Codex skill entry | [`../../../../../.agents/skills/figma-presentation-assetizer/SKILL.md`](../../../../../.agents/skills/figma-presentation-assetizer/SKILL.md) |
| Portable package | [`../../../../../.codex/presentation-assetization/README.md`](../../../../../.codex/presentation-assetization/README.md) |
| Operator know-how | [`../../../../../.codex/presentation-assetization/references/operator-knowhow.md`](../../../../../.codex/presentation-assetization/references/operator-knowhow.md) |
| Reuse playbook | [`../../../../../.codex/presentation-assetization/references/reuse-playbook.md`](../../../../../.codex/presentation-assetization/references/reuse-playbook.md) |
| Agent model | [`../../../../../.codex/presentation-assetization/agents/registry.json`](../../../../../.codex/presentation-assetization/agents/registry.json) |
| Validation scripts | [`../../../../../.codex/presentation-assetization/scripts/`](../../../../../.codex/presentation-assetization/scripts/) |

핵심 규칙은 동일하다. 원본 Figma는 보존하고, Figma write는 A5만 수행하며, full-slide flatten shortcut 없이 토큰/컴포넌트/자산/QA 근거를 남긴다.

## Shareable Archive

팀에 파일로 전달할 때는 아래 압축본을 사용한다.

`../presentation-assets-handoff-2026-07-09.zip`

압축본에는 `presentation-assets/` 전체가 포함되어 있고, `.DS_Store` 같은 로컬 메타 파일은 제외했다.

## Figma Location

Working Figma file:

`https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`

최종 검토 페이지:

`99 Final Componentized Deck`

이 페이지에는 PDF 순서대로 정렬된 14개 final componentized rebuild frame이 있다.

## What This Package Proves

현재 패키지는 다음을 입증한다.

- 원본 발표덱 14장을 source-preserving 방식으로 구조화할 수 있다.
- 주요 반복 요소를 Figma component instance로 치환하면서 높은 시각 유사도를 유지할 수 있다.
- 토큰, 자산, 컴포넌트, QA, prompt/process log를 함께 남기면 발표덱을 재사용 가능한 제작 자산으로 바꿀 수 있다.

아직 입증하지 않은 것은 다음이다.

- 원본 Figma frame 없이 prompt만으로 14장을 완전 생성하는 것.
- 모든 one-off vector/connector를 flexible component system으로 바꾸는 것.
- 외부 디자이너나 AI가 blind rebuild를 했을 때 같은 품질을 재현하는 것.

## Recommended First Team Test

팀 공유 후 첫 검증은 slide `09 User Scenario` blind rebuild가 적합하다.

1. 원본 frame과 final frame을 직접 참조하지 않는다.
2. [`../slides/09-user-scenario-source-analysis.md`](../slides/09-user-scenario-source-analysis.md), [`../tokens/`](../tokens/), [`../components/component-catalog.md`](../components/component-catalog.md), [`../assets/asset-ledger.md`](../assets/asset-ledger.md)만 입력으로 준다.
3. 새 Figma page에 `S09/UserScenario/Blind Rebuild v0.1`을 만든다.
4. [`../qa/rebuild-diff.md`](../qa/rebuild-diff.md) 방식으로 visual diff를 기록한다.

이 테스트가 통과하면 “원본을 잘 복제했다”에서 “문서와 자산만으로 재생산 가능하다”로 증명 수준이 올라간다.
