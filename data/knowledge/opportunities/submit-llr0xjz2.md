---
type: "submit-candidate"
alpha_id: "LLR0Xjz2"
status: "ARCHIVED"
priority: "low"
grade: "AVERAGE"
sharpe: 1.75
fitness: 1.48
self_corr_max: 0.675
neutralization: "SUBINDUSTRY"
family: "fundamental_analyst_coverage"
session: "20260615-001"
brain_url: "https://platform.worldquantbrain.com/alpha/LLR0Xjz2"
queued: "2026-06-25"
---

# Submit LLR0Xjz2 (fundamental + analyst coverage blend)

> **Archived, never submitted.** The project ended while this candidate was still in the
> queue. Kept as a record of the submission-review format.

## Expression
`ts_decay_linear(rank(fnd6_acdo) + rank(fnd6_dlto / close) + rank(sales_estimate_count), 10)`

## Why submittable
- AVERAGE grade, S=1.75, F=1.48. All 8 IS checks pass.
- Self-corr 0.675 (below 0.70 gate — PASS but borderline RISKY).
- Clean decorrelated blend — no itci, IV-spread, or flag*(-ret) components.

## Risk
- Borderline self-corr 0.675 — OS drift could push over 0.70.
- AVERAGE grade means low points-per-submission-slot.

## Reviewer action
Re-run `pnl_correlation.py --alphas LLR0Xjz2 --vs-book` to confirm self-corr
still passes against current 29-ACTIVE book. Submit only if self-corr holds.
