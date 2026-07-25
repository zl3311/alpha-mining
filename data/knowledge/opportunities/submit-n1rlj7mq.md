---
type: "submit-candidate"
alpha_id: "N1rlJ7mq"
status: "SUBMITTED"
priority: "resolved"
submitted: "2026-07-19"
grade: "EXCELLENT"
sharpe: 2.32
fitness: 2.07
turnover: 0.1109
self_corr_max: 0.6903
neutralization: "SUBINDUSTRY"
decay: 6
family: "pstkrv_event_magnitude_dual_stabilizer"
session: "20260719-001"
brain_url: "https://platform.worldquantbrain.com/alpha/N1rlJ7mq"
queued: "2026-07-19"
---

# Submit N1rlJ7mq (Preferred-Stock-Redemption Event-Magnitude + Dual Stabilizer + FCF + Buzz)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`

## Why submittable

- **All 8 BRAIN checks PASS, including SELF_CORRELATION**, confirmed
  AUTHORITATIVELY via BRAIN `/alphas/N1rlJ7mq/check`:
  `{result: PASS, value: 0.6903, limit: 0.7}` (reconfirmed on a second poll).
- Grade EXCELLENT, S=2.32, F=2.07, T=11.09%. SUBINDUSTRY, decay=6.
- Fresh anchor `fnd6_pstkrv` (Preferred Stock — Redemption Value) — never in
  the submitted book; redundancy cluster #81; standalone INFERIOR but strong
  under event-magnitude + dual-stabilizer form.
- Closest peer `1YJagrVk` at 0.690 — clears Gate 1 without Sharpe premium.

## Caveat

Self-corr margin under 0.70 is thin (~0.01). Submitted 2026-07-19 by human;
BRAIN confirms ACTIVE.
