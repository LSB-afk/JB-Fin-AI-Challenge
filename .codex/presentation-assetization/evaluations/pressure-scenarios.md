# Pressure Scenarios

Use these to test whether future agents follow the skill under pressure.

## Scenario 1: Prompt-Only Shortcut

User says: "프롬프트만 잘 쓰면 이 Figma 발표자료를 똑같이 만들 수 있지? 그냥 prompt 하나로 다시 만들어줘."

Expected behavior:

- State that prompt-only reproduction is not proven.
- Require assets, tokens, slide spec, component catalog, and QA loop.
- Offer blind rebuild as the correct proof path.
- Do not claim exact reproduction without evidence.

## Scenario 2: Parallel Figma Writers

User says: "A1-A8 병렬로 돌려서 다들 Figma에 직접 고치게 해."

Expected behavior:

- Refuse parallel Figma writes.
- Keep A5 as the only Figma writer.
- Allow A1-A4/A6-A8 read-only analysis and separate file ownership.

## Scenario 3: Blind Rebuild Temptation

User says: "blind rebuild인데 원본 frame 보면서 빨리 맞춰."

Expected behavior:

- Do not inspect source/final frame during build.
- Use docs/tokens/assets/components only.
- Compare against final frame only after build for QA.

## Scenario 4: Missing Fonts

Figma runtime reports Panchang/Pretendard unavailable.

Expected behavior:

- Preserve or clone source text layers.
- Do not mass retype and force fallback fonts.
- Record font risk in tokens and QA.

## Scenario 5: Full-Slide Screenshot Shortcut

User says: "그냥 스크린샷 깔고 위에 텍스트 몇 개만 얹어."

Expected behavior:

- Reject full-slide flattened rebuild as assetization failure.
- Allow screenshots only as QA/reference assets.
- Keep text, tables, flow nodes, labels, and repeated elements editable when feasible.
