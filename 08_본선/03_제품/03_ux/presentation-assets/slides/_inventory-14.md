---
tags:
  - area/product
  - type/inventory
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# 14 Slide Inventory

Source: `08_본선/05_제출/제출본/발표자료/발표자료-피그마-정합성체크.md`

Final PDF order check: `qa/pdf-order-check.md`. PDF page order matches the local Figma JPG export order.

| PDF page | JPG export | Deck audit node-id | Working Figma node-id | Structured rebuild node-id | Componentized rebuild node-id | Section | Assetization priority | Notes |
|---:|---|---|---|---|---|---|---|---|
| 1 | `01 Summary.jpg` | `4915:2719` | `6:198` | `22:2` | `93:1179` | Summary | Componentized | Cover media stack, header, footer, and wordmark componentized; tolerance-aware accepted baseline |
| 2 | `02 문제정의.jpg` | `4815:9181` | `6:3` | `28:2` | `49:76` | Problem Definition | Componentized | Case cards and limitation rows componentized; accepted baseline |
| 3 | `03 문제 정의.jpg` | `4852:2204` | `6:313` | `28:95` | `58:183` | Problem Definition | Componentized | Evidence screenshot/highlight components; byte-equal componentized export |
| 4 | `04 솔루션 개요.jpg` | `4815:12466` | `6:210` | `28:108` | `54:150` | Solution Overview | Componentized | Axis columns and flow steps componentized |
| 5 | `05 주요기능.jpg` | `4852:2316` | `6:261` | `28:159` | `98:1189` | Key Feature 1 | Componentized | Feature callout labels componentized; byte-equal componentized export |
| 6 | `06 주요기능.jpg` | `4977:5213` | `6:286` | `28:184` | `101:1206` | Key Feature 2 | Componentized | Approval/audit callouts componentized; byte-equal componentized export |
| 7 | `07 데이터 및 활용 기술.jpg` | `4877:1440` | `6:325` | `25:2` | `68:508` | 데이터 및 활용 기술 | Componentized | Dark tables and entity pills componentized |
| 8 | `08 데이터 및 활용 기술.jpg` | `4939:2710` | `6:592` | `28:211` | `61:176` | AI 업무 지원 조직도 | Componentized | Org chart role/gate component family promoted |
| 9 | `09 사용자 시나리오.jpg` | `4915:2636` | `6:1046` | `26:2` | `64:490` | User Scenario | Componentized | Process flow nodes and story cards componentized; byte-equal componentized export |
| 10 | `10 기대효과.jpg` | `4852:1918` | `6:96` | `29:2` | `70:660` | 기대효과·확장성 | Componentized | Experience nodes componentized; includes flagged queueing number |
| 11 | `11 실제 구현 흐름 및 시연 계획.jpg` | `4960:1054` | `6:1108` | `29:104` | `74:649` | 본선 구현 결과/시연 계획 | Componentized | MVP checklist and demo-plan rows componentized |
| 12 | `12 마무리.jpg` | `4939:4127` | `6:983` | `29:151` | `77:678` | 마무리 / AX 운영체계 확장 | Partial componentized | Benefit bubbles and expansion steps promoted; large orbit vector remains documented pattern |
| 13 | `13 Appendix.jpg` | `4977:5378` | `6:1586` | `29:214` | `80:688` | Appendix / References | Componentized | References and verification rows componentized; byte-equal componentized export |
| 14 | `14.jpg` | `4939:3419` | `6:1155` | `29:357` | `90:777` | Appendix 협업 간트 | Componentized | Date ticks, lane metadata, task bars, and milestones componentized; accepted baseline |

## Expansion Rule

The 3-slide pilot has expanded into source-preserving structured clones for all 14 slides. All 14 slides now have accepted componentized rebuild loops above the 98% visual gate. Remaining work is optional deeper atomization of one-off regions, not visual parity.
