---
type: "submit-candidate"
alpha_id: "ZYpjKeKx"
status: "SUBMITTED"
submitted: "2026-07-06"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.49
fitness: 2.25
turnover: 0.278
self_corr_max: 0.750
neutralization: "SUBINDUSTRY"
decay: 6
family: "accrued_liability_event_magnitude"
session: "20260622-001"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpjKeKx"
queued: "2026-06-22"
---

# Submit ZYpjKeKx (Accrued Liability Event-Magnitude)

## Expression
`rank(abs(ts_delta(fn_accrued_liab_q / close, 3))) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`

## Why submittable
- Self-corr 0.750 vs current book; BRAIN authoritative check: PASS (Sharpe premium).
- Top peer zqOrkbbG (S=1.82, corr 0.750): margin +0.488 above 1.1x threshold.
- Second peer xARzmVEW (S=2.05, corr 0.736): margin +0.235 above 1.1x threshold.
- All 7 computable BRAIN checks PASS.
- Grade EXCELLENT, S=2.49, F=2.25.

## Outcome

Submitted by the user on 2026-07-06. BRAIN reports `ACTIVE`, and all submission
checks pass. `data/book/ZYpjKeKx.md` is reconciled to `status: ACTIVE`.
