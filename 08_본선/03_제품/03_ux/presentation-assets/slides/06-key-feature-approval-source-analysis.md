---
tags:
  - area/product
  - type/design
  - status/active
date: 2026-07-09
up: "[[JByond 발표덱 자산화]]"
---

# 06 Key Feature Approval Source Analysis

## Source

| 항목 | 값 |
|---|---|
| Local export | `08_본선/05_제출/제출본/PPT/Figma/06 주요기능.jpg` |
| Deck audit node-id | `4977:5213` |
| Pasted working node-id | `6:286` |
| Structured rebuild node-id | `28:184` |
| QA reference | `qa/visual-diff/full-deck-structured-audit-2026-07-09.json` |
| Figma access | `visual_reference_ok_metadata_timeout` |

## Message

AI Agent가 정리한 초안은 바로 실행되지 않고, RM과 준법 담당자의 승인 게이트를 통과한 뒤에만 고객 대상 조치로 이어진다. 모든 판단과 승인 과정은 Audit Log로 남는다.

## Layout

| 영역 | 구조 | Rebuild 단위 |
|---|---|---|
| Background | deep navy with split product screenshots | `FrameDark.productShot` |
| Left floating case card | selected case summary and risk/goal boxes | `CaseDetailCard` |
| Center sidebar crop | console sidebar with approval/routing queues | raster/console mockup |
| Right approval queue | agent approval cards and integrated report viewer | `ApprovalQueuePanel` |
| Left callout labels | `L0-L4 Gate`, `Audit LogAgent` | editable callout text |
| Bottom headline | `Key Feature 2.` and approval/audit message | editable text |

## Text Inventory

- `Key Feature 2.`
- `Approval Gate & Audit Log / Agent 실행 기록`
- `AI Agent가 정리한 초안은 바로 실행되지 않습니다.`
- `RM과 준법 담당자의 승인 게이트를 통과한 뒤에만 고객 대상 조치로 이어집니다.`
- `모든 판단과 승인 과정은 Audit Log로 남아 사후 검토가 가능합니다.`
- `L0-L4 Gate` / `위험도에 따라 승인 레벨과 담당자를 자동 분기`
- `Audit LogAgent` / `Agent 실행, RM 판단, 준법 승인, 보류 사유 기록`
- UI labels: `에이전트 승인 큐`, `통합 리포트 뷰어`, `재실행(R)`

## Visual Layer Model

| Role | Notes |
|---|---|
| `CaseDetailCard` | left floating white card, case metadata and risk/goal boxes |
| `ApprovalQueue` | right upper queue with agent cards, status, expected output file names |
| `IntegratedReportViewer` | right lower report panel with tabs and rich markdown-style body |
| `GateCallout` | left connector from case to approval level explanation |
| `AuditCallout` | connector to report/audit output area |

## Component Model

- `JByond/Deck/ApprovalGateCallout`
- `JByond/Deck/AuditLogCallout`
- `JByond/ConsoleShot/CaseDetailCard`
- `JByond/ConsoleShot/ApprovalQueueCard`
- `JByond/ConsoleShot/ReportViewer`

## Structured Rebuild V1

| 항목 | 값 |
|---|---|
| Figma node | `28:184` |
| Source mapping | `6:286 -> 28:184` |
| QA | full PNG byte-equal export, similarity `1.0000000000` |
| Scope status | componentized rebuild v1.0 accepted; full subtree metadata remains unstable |

## QA Risks

- The right report viewer has dense small text and can easily blur or clip after refactor.
- Approval queue cards and report body are likely raster/product screenshot layers; if made editable, use a separate console-shot component set.
- Metadata extraction should be retried on subtrees after identifying child IDs from the structured clone.

## 2026-07-09 Figma Read Issue

- Lightweight `use_figma` read covering source `6:286` and baseline `28:184` returned `HTTP 504`.
- `get_metadata` on baseline `28:184` also returned `HTTP 504`.
- Do not retry full slide or whole-subtree reads. Selected child IDs are required for any further atomization.

## 2026-07-09 Componentized Rebuild V1.0

Slide `06` now has an accepted componentized rebuild. The build avoided direct access to timeout-prone node `6:304` by cloning the verified structured baseline `28:184`, hiding the original approval/audit callout frames, and placing promoted callout component instances at exact source coordinates.

| Component | Figma node | Source nodes | Variants | Evidence |
|---|---|---|---|---|
| `JByond/Deck/ApprovalAuditCalloutExact/VariantSet` | `101:1205` | `6:309`, `6:305` | `L0L4Gate`, `AuditLogAgent` | `assets/components/approval-audit-callout-exact-variant-set-101-1205.png` |

| 항목 | 값 |
|---|---|
| Componentized rebuild node | `101:1206` |
| Source screenshot | `assets/rebuild-screenshots/06-key-feature-approval-source-6-286.png` |
| Rebuild screenshot | `assets/rebuild-screenshots/06-key-feature-approval-componentized-101-1206.png` |
| Visual diff | `qa/visual-diff/06-key-feature-approval-componentized-v1.0.json` |
| QA | byte-identical screenshot export, similarity `1.0000000000`, changed pixels `0` |
| Component instances | `101:1233`, `101:1236` |
| Hidden original callout layers | `101:1225`, `101:1229` |

Further atomization should focus only on reusable console-shot internals, such as approval queue cards or report viewer rows, and only if future decks need those areas editable.
