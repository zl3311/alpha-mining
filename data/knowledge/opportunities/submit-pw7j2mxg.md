---
type: "submit-candidate"
alpha_id: "pw7j2MXg"
status: "REJECTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 1.98
fitness: 2.01
turnover: 0.030
self_corr_max: 0.7414
self_corr_verdict: "FAIL"
neutralization: "SUBINDUSTRY"
decay: 6
family: "leverage_fundamental"
session: "20260609-001"
brain_url: "https://platform.worldquantbrain.com/alpha/pw7j2MXg"
queued: "2026-06-09"
---

# Submit pw7j2MXg (zscore leverage + 2x itci)

## Expression
`zscore(-1 * equity / assets) + rank(fnd6_itci / close) + rank(fnd6_itci / close)` SUBINDUSTRY neut.

## Why submittable
- Self-corr 0.412 vs current book (SAFE — very low).
- All 8 BRAIN checks PASS (verified via /alphas/{id}/check endpoint).
- EXCELLENT grade, S=1.98, F=2.01. Would be the 3rd EXCELLENT-tier alpha
  and the first leverage-family entry in the book.

## Status Update (2026-06-17)

REJECTED. After `0m8GV1Pp` (event3d leverage, S=2.64) was submitted/activated,
the authoritative BRAIN `/check` for `pw7j2MXg` now returns SELF_CORRELATION
FAIL: corr 0.7414 vs `0m8GV1Pp` (> 0.70), and the Sharpe-premium escape is not
met (candidate S=1.98 < 1.10 x 2.64 = 2.90). The earlier 0.412 figure was
measured against an older book that did not yet contain the event/leverage
family. This candidate is no longer submittable.
