# Expected Behavior Checklist

Use after invoking `$figma-presentation-assetizer`.

| Check | Expected |
|---|---|
| Loads relevant references | Reads only needed references, not every file |
| Original preservation | Does not mutate original Figma |
| Write lock | Keeps A5 as only Figma writer |
| Full-slide flatten | Rejects full-slide screenshot rebuilds |
| Token use | Uses token files before raw values |
| Component loop | Promotes one family at a time and reruns QA |
| Blind rebuild | Does not inspect source/final during build |
| Font risk | Preserves source text or records missing-font risk |
| QA evidence | Requires screenshot/diff before pass |
| Handoff | Produces index, runbook, Figma guide, checklist, archive |

## Baseline Failures Observed In JByond Pilot

- Placeholder rebuild looked materially different from source.
- Font runtime exposed only Inter while source used Panchang/Pretendard.
- Large Figma subtrees timed out.
- Broad component geometry drifted until exact-geometry variants were used.
- Prompt-only framing overstated what had been proven.

The skill exists to prevent these failures from recurring.
