---
type: "submit-candidate"
alpha_id: "E5KlNNj9"
status: "SUPERSEDED"
priority: "low"
superseded_by: "pw7j2MXg"
grade: "GOOD"
sharpe: 1.88
fitness: 1.58
turnover: 0.017
self_corr_max: 0.564
neutralization: "SUBINDUSTRY"
decay: 6
family: "leverage_fundamental"
session: "20260609-001"
brain_url: "https://platform.worldquantbrain.com/alpha/E5KlNNj9"
queued: "2026-06-09"
---

# Submit E5KlNNj9 (leverage + drlt blend)

## Expression
`ts_decay_linear(rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5)` SUBINDUSTRY neut.

## Why submittable
- Self-corr 0.564 vs current book (SAFE — well below 0.70 threshold).
- All 8 BRAIN checks PASS (verified via /alphas/{id}/check endpoint).
- GOOD grade, S=1.88, F=1.58.
- First leverage-family alpha — entirely novel mechanism in the book.

## Risk assessment
- Top correlated peer is 6Xzm6PQP (guidance_fundamental, corr=0.564). The
  correlation is from shared underlying fundamental exposure, not field overlap.
- After submission, other leverage variants (j2gjVLWQ, 78djRjAO, 1YgwAVxz,
  A13lQM7E) will likely fail mutual self-corr vs this entry.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/E5KlNNj9.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
