---
type: "submit-candidate"
alpha_id: "blL55wRp"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.10
fitness: 2.03
turnover: 0.167
self_corr_max: 0.6941
self_corr_method: "brain_self_correlation_check"
neutralization: "SUBINDUSTRY"
decay: 6
family: "capital_intensity_totassets_volregime"
session: "20260618-001"
brain_url: "https://platform.worldquantbrain.com/alpha/blL55wRp"
queued: "2026-06-18"
---

# Submit blL55wRp (capital intensity + total assets revision, vol-gated)

## Expression
`trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(fnd6_fate / close) + rank(anl4_totassets_flag) + rank(open / close - 1) + rank(ts_mean(scl12_buzz, 5)), 5), ts_std_dev(returns, 20) < 0.01)`

## Why submittable
- Self-corr 0.6941 vs current book (BRAIN authoritative PASS); all 8 computable BRAIN checks pass.
- Grade EXCELLENT, S=2.10, F=2.03.
- Thin margin (0.006 below 0.70 limit) — submit promptly before book changes could shift the corr boundary.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/blL55wRp.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
