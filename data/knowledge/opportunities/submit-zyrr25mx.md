---
type: "submit-candidate"
alpha_id: "ZYrr25Mx"
status: "ARCHIVED"
priority: "low"
grade: "EXCELLENT"
sharpe: 1.86
fitness: 2.41
self_corr_max: null
neutralization: "MARKET"
family: "cogs_revision_market"
session: null
brain_url: "https://platform.worldquantbrain.com/alpha/ZYrr25Mx"
queued: "2026-06-25"
---

# Submit ZYrr25Mx (COGS revision MARKET)

> **Archived, never submitted.** The project ended while this candidate was still in the
> queue. Kept as a record of the submission-review format.

## Expression
`ts_decay_linear(cogs + cfi + bvps + cfi*(-ret), 5)` MARKET neut.

## Why submittable
- EXCELLENT grade, S=1.86, F=2.41.
- COGS family — check dead zone `family-cogs` (self-corr 0.72-0.79 historically blocks).

## Risk
- Dead zone `family-cogs.md` warns self-corr is 0.72-0.79 against the book.
- Self-corr has not been re-checked against the current 29-ACTIVE book.

## Reviewer action
Re-run `pnl_correlation.py --alphas ZYrr25Mx --vs-book` before submitting.
If self-corr passes, submit on BRAIN platform and flip status.
