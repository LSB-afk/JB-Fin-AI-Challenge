---
tags:
  - area/product
  - type/design
  - type/brief
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
aliases:
  - JByond 발표덱 정의서
  - JByond deck definition
---

# JByond Presentation Deck Definition

이 문서는 JByond 발표덱을 한 파일로 이해하기 위한 상위 정의서다. 목적은 시니어 디자이너, PM, AI 빌더가 이 문서만 먼저 읽어도 “이 발표자료가 어떤 철학으로 설계됐고, 무엇을 보여주려 했으며, 어떤 규칙으로 다시 만들 수 있는지”를 파악하게 하는 것이다.

세부 수치, node-id, 토큰, 자산, QA 결과는 하위 문서에 남긴다. 이 파일은 그 자료들을 해석하는 관점과 제작 원칙을 고정한다.

## 1. Deck Thesis

JByond 발표덱의 핵심은 “AI 기능 소개”가 아니다. 이 덱은 지역 금융 조직이 실제 현장에서 겪는 파편화된 업무, 책임 전가, 근거 부족, 승인 지연 문제를 **역할 기반 AI 운영체계**로 재구성할 수 있다는 것을 보여준다.

이 덱이 말하는 제품은 챗봇이나 대시보드가 아니라, 케이스가 발생했을 때 사람과 AI Agent가 어떤 순서로 판단하고, 증거를 남기고, 승인하고, 다음 역할로 넘기는지를 다루는 운영 구조다.

디자인의 주된 메시지는 다음 세 가지다.

1. **통제 가능한 AI**
   - AI는 독립적으로 결정을 내리는 존재가 아니라, 사람이 승인하고 추적할 수 있는 업무 실행 보조 계층으로 표현된다.
   - `L0-L4 Gate`, `AuditLogAgent`, `EvidencePack`, `AgentRun` 같은 객체명이 반복되는 이유는 “AI가 했습니다”가 아니라 “누가, 어떤 근거로, 어디까지 했는지 남깁니다”를 보여주기 위해서다.

2. **현업 업무의 재배열**
   - 여러 부서, 지점, 본부, 제휴기관, 고객 접점을 하나의 흐름 안에 놓는다.
   - 슬라이드의 많은 도표는 예쁜 장식이 아니라 책임과 이관의 지도다.

3. **발표용 비주얼이면서 운영 문서 같은 밀도**
   - 이 덱은 마케팅 랜딩 페이지처럼 넓고 감성적인 자료가 아니다.
   - 심사위원이 “실제로 구현했고, 운영 구조를 이해하고 있다”고 느끼도록 일부러 콘솔, 표, 흐름도, 간트, 레퍼런스를 높은 밀도로 배치한다.

## 2. Narrative Arc

14장은 하나의 설득 흐름으로 읽혀야 한다.

| 구간 | Slides | 역할 | 디자이너가 보아야 할 의도 |
|---|---:|---|---|
| Opening | 01 | 한 문장 포지셔닝 | JByond를 브랜드/제품명으로 먼저 각인한다. 어두운 무대 위에 제품 이미지를 올려 “실행 가능한 시스템”처럼 보이게 한다. |
| Problem | 02-03 | 문제의 현실화 | 현장의 업무 단절과 기존 접근의 한계를 카드/증거 이미지로 보여준다. 주장보다 사례와 근거가 먼저 온다. |
| Solution | 04 | 해결 구조 | 계열사, 역할, 케이스, AI Agent, 담당자, 다음 역할을 하나의 오케스트레이션으로 정리한다. |
| Product Proof | 05-06 | 실제 화면 증거 | 제품 UI 캡처를 중심에 두고, 핵심 객체와 승인 구조를 callout으로 해석한다. |
| Operating System | 07-08 | 시스템/조직 구조 | 데이터, 기술, 역할 조직도, 운영 Agent를 통해 제품이 단일 화면이 아니라 운영체계임을 증명한다. |
| Scenario | 09 | 사용자 여정 | 고객/지점/본부/AI/승인의 흐름을 한 장의 업무 시나리오로 묶는다. |
| Impact | 10 | 기대효과 | AX, UX, EX/PX, CX 같은 경험 축으로 효과를 조직 전체로 확장한다. |
| Execution | 11 | 구현/시연 계획 | 이미 만든 것과 시연할 것을 분리해 실행력을 보여준다. |
| Expansion | 12 | 확장 철학 | 특정 과제가 아니라 JB금융의 AX 운영체계로 확장된다는 결론을 만든다. |
| Evidence | 13-14 | 출처/일정 증빙 | 레퍼런스와 간트로 “그럴듯한 이야기”를 “검증 가능한 산출물”로 닫는다. |

이 흐름을 벗어나면 덱의 설득력이 약해진다. 특히 제품 화면보다 추상적 비전이 앞서거나, 증빙 슬라이드가 빠지면 이 자료의 성격이 변한다.

## 3. Design Philosophy

### 3.1 Enterprise Control Room

전체 톤은 “금융권 AI 운영 관제실”에 가깝다. 배경은 짙고, 정보 패널은 밝거나 반투명하며, 파란 계열의 선과 강조가 시스템적 질서를 만든다.

이 덱은 따뜻한 브랜드 친밀감보다 신뢰, 통제, 추적 가능성을 우선한다. 따라서 장식적 일러스트, 과한 그라데이션, 마케팅식 히어로 카드는 맞지 않는다.

### 3.2 Evidence Before Claim

문장은 주장하지만, 화면은 근거를 보여준다.

- 문제 슬라이드는 실제 사례 카드와 증거 캡처를 사용한다.
- 기능 슬라이드는 실제 제품 UI 캡처를 보여준다.
- 시스템 슬라이드는 객체명과 데이터 흐름을 노출한다.
- 마지막은 출처와 일정으로 닫는다.

디자인 재현 시 가장 중요한 기준은 “그럴듯한 AI 덱”이 아니라 “근거가 있는 운영 덱”처럼 보이는가다.

### 3.3 Dense But Navigable

정보 밀도는 높지만, 시선의 경로는 분명해야 한다.

- 왼쪽 상단은 맥락과 제목.
- 중앙 또는 오른쪽은 핵심 증거/도표/제품 화면.
- 하단은 footer, entity rail, evidence, timeline 같은 보조 구조.
- 작은 라벨과 caption은 장식이 아니라 해석 장치다.

밀도를 줄인다고 좋은 재현이 아니다. 대신 그룹, 라인, 여백, 라벨 위계로 읽히게 해야 한다.

## 4. Visual Grammar

| 영역 | 규칙 |
|---|---|
| Canvas | 모든 발표 슬라이드는 `1920x1080` 기준이다. |
| Stage | 기본 배경은 dark navy 계열의 깊은 무대다. |
| Accent | blue/cyan/teal 계열은 AI, 흐름, 시스템 객체, active state를 표시한다. |
| Surface | 흰색 또는 어두운 반투명 패널은 증거, 표, 제품 UI를 담는 표면이다. |
| Typography | 큰 브랜드 wordmark는 Panchang, 본문/표/라벨은 Pretendard 계열을 기준으로 한다. |
| Density | 발표용 헤드라인보다 작은 운영 라벨과 표가 많다. 이 밀도 자체가 제품의 진정성을 만든다. |
| Raster | 제품 화면, 증거 캡처, 사진성 배경은 raster 허용. 흐름, 표, 라벨, 제목은 editable layer가 원칙이다. |
| Components | 반복되는 카드, 행, 노드, 라벨, tick, task bar는 component instance 또는 documented pattern이어야 한다. |

## 5. Token System

토큰은 `tokens/token-index.json`을 시작점으로 읽는다. 구조는 다음 3계층이다.

| Layer | 현재 파일 | 역할 |
|---|---|---|
| Primitive | `tokens/primitives.json` | Figma에서 관측한 raw color, size, radius, stroke, frame 값 |
| Semantic | `tokens/semantic.json` | stage, surface, text, line, accent 같은 의미 토큰 |
| Component | `tokens/components.json` | `JByond/Deck/*` component별 사용 계약 |

보조 토큰 파일은 다음을 담당한다.

- `tokens/typography.json`: text role, font, size, line-height, source node
- `tokens/fonts.json`: Panchang/Pretendard 원천과 Figma missing-font 상태
- `tokens/effects.json`: shadow, gradient, image treatment
- `tokens/surfaces.json`: glass, panel, image mask/crop, table surface
- `tokens/slides.json`: slide별 layout zone과 editable/raster boundary
- `tokens/assets.json`: 이미지와 source node 연결
- `tokens/qa-rules.json`: rebuild 검증 기준
- `tokens/figma-variable-map.json`: Figma variable/style/component 매핑

정책은 명확하다. 새로 만드는 Figma build script는 raw color나 size를 직접 박지 않고 토큰을 먼저 참조한다. raw 값은 측정 중이거나 새 토큰을 제안할 때만 허용된다.

## 6. Component Model

현재 컴포넌트화의 원칙은 “예쁜 일반화”보다 “픽셀 기준을 깨지 않는 정확한 재사용”이다.

따라서 많은 component 이름에 `Exact`가 붙는다. 이는 아직 broad auto-layout component보다 원본 geometry 보존이 중요하다는 뜻이다.

대표 component family:

- Cover: `CoverMediaStackExact`, `CoverHeaderExact`, `CoverFooterExact`, `CoverWordmarkExact`
- Problem: `ProblemCaseCard`, `LimitationRowExact`
- Evidence: `EvidenceScreenshotExact`, `EvidenceHighlightExact`
- Solution: `SolutionAxisColumnExact`, `SolutionFlowStepExact`
- Product Callout: `FeatureCalloutTopExact`, `FeatureCalloutRightExact`, `ApprovalAuditCalloutExact`
- System: `SystemFlowTableExact`, `EntityPillExact`
- Org/Scenario: `OrgRoleNode*`, `ScenarioProcessNodeExact`, `ScenarioCardExact`
- Appendix: `ReferenceItem*`, `GanttDateTickExact`, `GanttLaneMetaExact`, `GanttTaskBarExact`, `GanttMilestoneExact`

장기적으로는 `Exact` component를 기반으로 `Flexible` component를 별도 승격할 수 있다. 단, 승격 후에도 원본 대비 visual QA를 통과해야 한다.

## 7. Asset Policy

이 덱의 자산은 세 종류로 나뉜다.

| 종류 | 예시 | 정책 |
|---|---|---|
| QA reference | full-slide screenshot, PDF page image | 비교 기준일 뿐, rebuild content로 쓰지 않는다. |
| Raster-allowed material | 제품 UI 캡처, 기사/규정 증거 캡처, cover stage image | 원본성이 중요하거나 editable source가 없으면 raster 허용. 출처와 crop/hash를 기록한다. |
| Editable layer | 제목, 표, flow node, connector, label, entity pill, gantt row | 가능한 한 Figma layer 또는 component instance로 유지한다. |

핵심은 “full-slide flatten 금지”다. 전체 슬라이드를 한 장 이미지로 붙이는 것은 제출용 PDF로는 괜찮지만, 자산화 목적에는 실패다.

## 8. Figma Implementation State

Working Figma file:

`https://www.figma.com/design/h6RkEn7fGbTwZbzuwaHsWi`

최종 검토 페이지:

`99 Final Componentized Deck` / page id `106:1201`

이 페이지에는 14개 accepted componentized rebuild frame이 PDF 순서대로 배치되어 있다.

| Slide | Final node-id | 상태 |
|---:|---|---|
| 01 | `93:1179` | componentized pass |
| 02 | `49:76` | componentized pass |
| 03 | `58:183` | componentized pass |
| 04 | `54:150` | componentized pass |
| 05 | `98:1189` | componentized pass |
| 06 | `101:1206` | componentized pass |
| 07 | `68:508` | componentized pass |
| 08 | `61:176` | componentized pass |
| 09 | `64:490` | componentized pass |
| 10 | `70:660` | componentized pass |
| 11 | `74:649` | componentized pass |
| 12 | `77:678` | partial componentized pass |
| 13 | `80:688` | componentized pass |
| 14 | `90:777` | componentized pass |

## 9. Rebuild Recipe

현재 입증된 제작 방식은 다음이다.

1. 원본 또는 pasted editable source frame을 확보한다.
2. source-preserving structured clone을 만든다.
3. layer naming, role taxonomy, metadata를 입힌다.
4. full-slide screenshot을 `1920x1080`으로 추출한다.
5. 원본 대비 pixel diff를 계산한다.
6. 반복 요소를 component set으로 승격한다.
7. 승격한 component instance를 slide clone에 치환한다.
8. 다시 QA를 돌려 visual drift를 기록한다.
9. token, asset ledger, component catalog, prompt log를 갱신한다.

이 방식은 “프롬프트만으로 무에서 생성”이 아니다. 검증된 방식은 다음 조합이다.

`screenshot + source assets + slide blueprint + tokens + component catalog + Figma build script + QA loop`

Blind rebuild 검증을 하려면 원본 frame을 직접 보지 않고 `slides/*-source-analysis.md`, `tokens/*`, `assets/*`, `components/component-catalog.md`, `process/rebuild-prompts.md`만으로 새 페이지에 한 장을 다시 만들어야 한다.

## 10. Quality Standard

현재 품질 기준은 다음이다.

| Gate | 기준 |
|---|---|
| Slide | `1920x1080`, no visible clipping, no incoherent overlap |
| Visual QA | source 대비 `>= 0.98` similarity. 현재 accepted frame은 대체로 `0.9987~1.0` |
| Editability | full-slide flatten 금지. 주요 텍스트/표/flow는 editable 또는 component instance |
| Token | 주요 색, typography, surface, effect, spacing은 token file에 연결 |
| Component | 2회 이상 반복되는 요소는 component 또는 documented pattern |
| Asset | 출처, source node, 사용 slide, crop/hash, raster 허용 이유 기록 |
| Process | 실패한 rebuild, 수정 루프, 남은 caveat를 기록 |

## 11. What This Proves

현재 산출물은 다음을 입증한다.

- 최종 Figma 발표덱 14장을 source-preserving 방식으로 고품질 구조화할 수 있다.
- 주요 반복 요소를 component instance로 바꾸면서도 시각 품질을 거의 유지할 수 있다.
- 토큰, 자산, 컴포넌트, QA, prompt/process log를 함께 남기면 덱을 재사용 가능한 제작 자산으로 바꿀 수 있다.
- 시니어 디자이너가 후속 작업을 이어받을 수 있는 수준의 구조와 근거가 남아 있다.

아직 입증하지 않은 것은 다음이다.

- 원본 Figma frame 없이 prompt만으로 동일 품질을 생성하는 것.
- 모든 one-off vector와 connector를 완전한 flexible component system으로 바꾸는 것.
- Figma runtime에서 Panchang/Pretendard를 새 텍스트 생성에 안정적으로 적용하는 것.
- 외부 디자이너가 문서만 보고 blind rebuild를 했을 때 동일 QA를 통과하는 것.

## 12. Documentation Coverage Review

현재 문서 세트는 44개 이상의 md/json/csv 파일로 구성되어 있고, 14개 slide source-analysis 파일은 모두 존재한다. 큰 범주는 대체로 갖춰져 있다.

| 범주 | 현재 문서 | 판단 |
|---|---|---|
| Project entry | `README.md`, `manifest.json` | 충분. 위치, node-id, 상태 확인 가능 |
| Slide inventory | `slides/_inventory-14.md` | 충분. PDF 순서와 Figma node 매핑 가능 |
| Slide analysis | `slides/*-source-analysis.md` 14개 | 충분. 전 장 분석 존재 |
| Tokens | `tokens/token-index.json`, split token files, `token-registry.csv` | 충분. 3계층 구조 존재 |
| Components | `components/component-catalog.md` | 충분. promoted/candidate/status 구분 존재 |
| Assets | `assets/asset-ledger.md`, `tokens/assets.json` | 대체로 충분. 일부 evidence normalization은 남음 |
| QA | `qa/rebuild-diff.md`, `qa/visual-diff/*.json` | 충분. visual diff와 루프 기록 존재 |
| Process | `process/ai-build-log.md`, `process/rebuild-prompts.md`, `process/parallel-agent-operating-model.md` | 충분. 다만 blind rebuild용 runbook은 별도 필요 |
| Design philosophy | 이 파일 `deck-definition.md` | 이번에 보강 |

## 13. Missing Or Weak Documents

필수 누락은 크지 않다. 다만 “프롬프트와 청사진만으로 다시 만들 수 있는가”를 강하게 입증하려면 다음 문서가 더 필요하다.

| 우선순위 | 문서 | 이유 |
|---:|---|---|
| 0 | `blind-rebuild-runbook.md` | 원본 frame을 보지 않고 `md + tokens + assets + components`만으로 한 장을 재생성하는 절차가 필요하다. |
| 0 | `blind-rebuild-eval.md` | blind rebuild 결과와 원본 대비 diff, 실패 원인을 기록해야 “문서만으로 재현 가능” 주장을 검증할 수 있다. |
| 1 | `layout-grammar.json` | 현재 layout은 문서와 토큰에 분산되어 있다. zone, grid, safe area, anchor, z-order를 기계적으로 읽는 별도 schema가 있으면 재현성이 올라간다. |
| 1 | `font-install-runbook.md` | Panchang/Pretendard가 Figma runtime에서 missing으로 잡힌다. 디자이너/빌더 환경에서 폰트를 어떻게 enable하는지 절차가 필요하다. |
| 1 | `evidence-ledger-normalized.json` | slide 13 references와 각 주장/수치/캡처를 연결하는 구조화 evidence ledger가 있으면 심사/재사용 신뢰도가 오른다. |
| 2 | `component-maturity-matrix.md` | `Exact`, `Flexible candidate`, `One-off documented pattern`의 성숙도를 한눈에 보는 문서가 있으면 디자인 시스템 운영이 쉬워진다. |
| 2 | `copy-system.md` | 헤드라인, eyebrow, caption, label, evidence note의 문체 규칙이 아직 암묵적이다. 한국어 발표 카피 재생성에 필요하다. |
| 2 | `export-package-checklist.md` | Figma 최종 페이지에서 PDF/PPT 제출본으로 다시 내보낼 때의 품질 체크리스트가 필요하다. |

## 14. Recommended Next Verification

다음 검증은 한 장을 골라 blind rebuild를 하는 것이다.

추천 대상은 slide `09 User Scenario`다.

이유:

- workflow, decision, branch, scenario card가 있어 발표덱 문법을 잘 대표한다.
- componentized rebuild가 이미 `1.0` similarity로 통과했다.
- 이미지, flow, label, caption이 섞여 있어 문서/토큰/컴포넌트만으로 재현 가능한지 평가하기 좋다.

검증 절차:

1. 원본 frame `6:1046`과 final frame `64:490`을 빌더 컨텍스트에서 숨긴다.
2. `slides/09-user-scenario-source-analysis.md`, `tokens/*`, `components/component-catalog.md`, `assets/asset-ledger.md`, `process/rebuild-prompts.md`만 사용한다.
3. 새 Figma page에 `S09/UserScenario/Blind Rebuild v0.1`을 만든다.
4. screenshot diff를 수행한다.
5. 실패한 요소를 `blind-rebuild-eval.md`에 남긴다.
6. 필요한 토큰/schema/doc을 보강한다.

이 루프가 통과하면 이 자산화 프로젝트는 “원본을 잘 복제했다”에서 “문서와 자산만으로 재생산할 수 있다”로 한 단계 넘어간다.
