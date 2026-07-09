# A6 Visual QA Judge

Owns visual QA and pass/fail evidence.

## Outputs

- `qa/rebuild-diff.md`
- `qa/visual-diff/*.json`
- diff images when available

## Gates

- `1920x1080`
- no full-slide flatten
- no visible clipping
- similarity `>= 0.98` unless documented exception
- component/token/asset provenance recorded

## Rules

- Pass requires screenshot or equivalent export evidence.
- Tolerance-aware pixel deltas are allowed only when no visible layout drift exists.
- Record drift areas and likely causes.
