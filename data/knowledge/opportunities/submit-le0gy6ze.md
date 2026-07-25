---
type: "submit-candidate"
alpha_id: "0m8GV1Pp"
status: "SUBMITTED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.64
fitness: 2.77
turnover: 0.041
self_corr_max: 0.5492
neutralization: "SUBINDUSTRY"
decay: 6
family: "event_leverage_fundamental"
session: "20260611-001"
brain_url: "https://platform.worldquantbrain.com/alpha/0m8GV1Pp"
queued: "2026-06-11"
supersedes: "le0gY6Ze"
---

# Submit 0m8GV1Pp (event magnitude d=3 + leverage + deferred revenue)

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`

## Why Submittable

- Self-corr 0.5466 vs current book (SAFE — well below 0.70 threshold).
- All 8 BRAIN checks PASS (verified via /alphas/{id}/check endpoint).
- SPECTACULAR grade, S=2.62, F=2.74. Would be the 5th SPECTACULAR in the book
  and the 2nd-highest fitness.
- Novel template family — abs(ts_delta) event detection is structurally unique.

## Risk Assessment

Top correlated peer is MPbgqZ7o (fundamental_sentiment, corr=0.547). Both use
fundamental6 dataset but different mechanism families. After submission, other
event+leverage variants will be blocked by mutual self-corr.

## Reviewer Action

BRAIN check reported `0m8GV1Pp` as ACTIVE on 2026-06-17. `data/book/0m8GV1Pp.md`
has been flipped to `status: ACTIVE`.
