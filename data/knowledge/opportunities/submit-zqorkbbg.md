---
type: "submit-candidate"
alpha_id: "zqOrkbbG"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 1.82
fitness: 2.01
turnover: 0.1176
self_corr_max: 0.6202
neutralization: "SUBINDUSTRY"
decay: 6
family: "accrual_analyst_buzz"
session: "20260613-001"
brain_url: "https://platform.worldquantbrain.com/alpha/zqOrkbbG"
queued: "2026-06-13"
---

# Submit zqOrkbbG (Accrued Liability Analyst Buzz)

## Expression

`ts_decay_linear(rank(fn_accrued_liab_q / close) + rank(anl4_cfi_flag) + rank(anl4_bvps_flag) + rank(ts_mean(scl12_buzz, 5)), 5)`

## Why Submittable

- BRAIN self-correlation check PASS at 0.6202, below the 0.70 threshold.
- All computable BRAIN checks PASS.
- EXCELLENT grade, S=1.82, F=2.01, turnover 11.76%.

## Risk Assessment

Top observed peer is `xARzmVEW` at 0.620, safely below the raw threshold. Recheck
before official submission if another quality-revision or accrued-liability
candidate is activated first.

## Reviewer Action

BRAIN check reported this alpha as ACTIVE on 2026-06-17. `data/book/zqOrkbbG.md`
has been flipped to `status: ACTIVE`.
