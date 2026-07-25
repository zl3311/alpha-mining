---
type: "submit-candidate"
alpha_id: "KP9V7YLz"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.83
fitness: 2.49
turnover: 0.1563
self_corr_max: 0.8015
neutralization: "SUBINDUSTRY"
decay: 6
family: "msaq_event_magnitude_stabilizer_blend"
session: "20260714-001"
brain_url: "https://platform.worldquantbrain.com/alpha/KP9V7YLz"
queued: "2026-07-14"
long_term_value: "LOW"
---

# Submit KP9V7YLz (MSAQ Event-Magnitude + FFO-Revision Stabilizer Blend)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Why It Is Submittable

- Grade EXCELLENT with Sharpe 2.83, fitness 2.49, and turnover 15.63%.
- All BRAIN checks pass.
- BRAIN measured self-correlation 0.8015 against ACTIVE `O0Z6NE0b`, and
  returned PASS because 2.83 Sharpe exceeds the required 2.31 premium.

## Reviewer Action

Submitted directly to BRAIN on 2026-07-14. The scoring submission passed its
self-correlation check through the 1.10x Sharpe-premium override.
