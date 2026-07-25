---
type: "submit-candidate"
alpha_id: "GrwrVP5G"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.04
fitness: 2.29
turnover: 0.0289
self_corr_max: 0.5735
self_corr_method: "brain_self_correlation_breakdown"
self_corr_verdict: "SAFE"
neutralization: "MARKET"
decay: 6
family: "event_leverage_capital_intensity_product"
session: "20260616-001"
brain_url: "https://platform.worldquantbrain.com/alpha/GrwrVP5G"
queued: "2026-06-16"
---

# Submit GrwrVP5G (Event Leverage Capital-Intensity Product)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(fnd6_fatl / close), 5)`

## Why Submittable

- EXCELLENT grade, S=2.04, F=2.29, turnover 2.89%.
- All computable BRAIN checks PASS.
- BRAIN self-correlation breakdown shows max correlation 0.5735 vs `d5Q3ZmWv`,
  below the 0.70 gate.

## Risk Assessment

Verified SAFE on 2026-06-17 via:

`uv run python3 scripts/pnl_correlation.py --alphas GrwrVP5G --brain-corr`

Top peer was `d5Q3ZmWv` at 0.5735, so the self-correlation gate should clear
without needing the Sharpe-premium escape.

## Reviewer Action

Submitted on the BRAIN platform on 2026-06-17. `data/book/GrwrVP5G.md` has been
flipped to `status: ACTIVE`.
