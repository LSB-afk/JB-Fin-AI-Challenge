---
tags:
  - area/product
  - type/qa
  - status/active
date: 2026-07-08
up: "[[JByond 발표덱 자산화]]"
---

# PDF Order Check

## Source

| 항목 | 값 |
|---|---|
| PDF | `08_본선/05_제출/제출본/PPT/JBFinAI_JByond_본선_PPT.pdf` |
| PDF pages | 14 |
| PDF page size | `960 x 540 pts` |
| Embedded images | 1 JPEG image per page |
| Embedded image size | `1920 x 1080` |
| Local export folder | `08_본선/05_제출/제출본/PPT/Figma/` |

## Result

PDF page order matches the local Figma JPG export order. The pilot slides are confirmed:

| PDF page | Local Figma export | Pilot role |
|---:|---|---|
| 1 | `01 Summary.jpg` | Calibration cover |
| 7 | `07 데이터 및 활용 기술.jpg` | System flow |
| 9 | `09 사용자 시나리오.jpg` | User scenario |

## Full Mapping

| PDF page | Local Figma export |
|---:|---|
| 1 | `01 Summary.jpg` |
| 2 | `02 문제정의.jpg` |
| 3 | `03 문제 정의.jpg` |
| 4 | `04 솔루션 개요.jpg` |
| 5 | `05 주요기능.jpg` |
| 6 | `06 주요기능.jpg` |
| 7 | `07 데이터 및 활용 기술.jpg` |
| 8 | `08 데이터 및 활용 기술.jpg` |
| 9 | `09 사용자 시나리오.jpg` |
| 10 | `10 기대효과.jpg` |
| 11 | `11 실제 구현 흐름 및 시연 계획.jpg` |
| 12 | `12 마무리.jpg` |
| 13 | `13 Appendix.jpg` |
| 14 | `14.jpg` |

## Verification Notes

- `pdfinfo` confirmed 14 pages.
- `pdfimages -list` showed exactly one `1920 x 1080` JPEG image per page.
- Exact SHA between PDF-embedded JPEG and local JPG export is not expected to match because PowerPoint recompressed images during PDF export.
- For ordering, use page number + local export order as the baseline. For pixel-perfect QA, use local JPG exports as primary reference and PDF as final packaging reference.
- The older Figma fit-check note has stale section labels for pages 11-13; the final PDF/JPG export names are the baseline for slide order and section naming.
- PDF/PPTX are flattened packaging references; they do not remove the need for editable Figma access for the A5 rebuild.
