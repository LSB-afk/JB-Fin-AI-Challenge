---
tags:
  - area/system
  - type/process
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# Parallel Agent Operating Model

## Rule

Figma write 작업은 `A5 Figma Slide Builder`만 수행한다. 다른 에이전트는 읽기, 분석, 문서화, QA만 맡는다. Repo 파일도 소유권별로 나누고 같은 파일을 동시에 편집하지 않는다.

## Agents

| Agent | Role | Write scope | Can run in parallel? |
|---|---|---|---|
| A0 Orchestrator | 통합, manifest, 상태 관리 | `README.md`, `manifest.json`, `qa/rebuild-diff.md` | No, coordinator |
| A1 Figma Reverse Engineer | 원본 구조/텍스트/레이어 분석 | `slides/*`, `assets/source-screenshots/*` | Yes |
| A2 Token Cartographer | 색/타입/효과/간격 토큰화 | `tokens/*` | Yes |
| A3 Component Architect | 컴포넌트 모델링 | `components/*` | Yes |
| A4 Asset Harvester | 이미지/표/그래프/출처 ledger | `assets/*` | Yes |
| A5 Figma Slide Builder | duplicate Figma 실제 생성 | Figma duplicate only | Sequential only |
| A6 Visual QA Judge | screenshot diff, quality gates | `qa/*` | Yes after build |
| A7 AI Process Librarian | prompts, build log, model reasoning | `process/*` | Yes |
| A8 Evidence Recorder | session/decision/telemetry append | `08_본선/04_증빙/**` | Yes, append-only |

## Waves

1. Wave 0 - 준비: duplicate URL, node-id mapping, write lock 확정
2. Wave 1 - 병렬 분석: A1/A2/A3/A4 동시 실행
3. Wave 2 - 단일 빌드: A5가 `01 Summary`만 먼저 생성
4. Wave 3 - QA 루프: A6 검증, A5 수정, 최소 2회
5. Wave 4 - 확장: A5가 `07`, `09` 생성, A6 검증
6. Wave 5 - 문서화: A7/A8/A0 통합

## Handoff Format

각 에이전트는 끝날 때 아래 6블록으로 남긴다.

```text
1. Task        - 수행한 일
2. Inputs      - 읽은 파일/노드/이미지
3. Output      - 만든 파일 또는 반환 데이터
4. Assumptions - 확인 전 가정
5. Open risks  - 미해결 위험
6. Next action - 다음 담당자와 행동
```

## Conflict Prevention

- A5 외에는 Figma mutation 금지.
- A0 외에는 `manifest.json` 직접 수정 금지. 다른 에이전트는 patch proposal만 전달.
- A6는 QA 파일을 수정할 수 있지만, pass 판정은 screenshot 증거가 있을 때만 기록한다.
- A8는 append-only 로그만 다룬다. 기존 로그 수정/정리 금지.

