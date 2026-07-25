---
type: "submit-candidate"
alpha_id: "GrLJLGN5"
status: "SUBMITTED"
submitted: "2026-07-11"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.77
fitness: 2.40
turnover: 0.207
self_corr_max: 0.7795
neutralization: "SUBINDUSTRY"
decay: 6
family: "negated_relationship_return_intraday_blend"
session: "20260705-001"
brain_url: "https://platform.worldquantbrain.com/alpha/GrLJLGN5"
queued: "2026-07-05"
long_term_value: "MEDIUM"
---

# Submit GrLJLGN5 (Negated Customer Return + PTPR + Gap)

## Expression

`ts_decay_linear(rank(-1 * rel_ret_cust) + rank(anl4_ptpr_flag) + rank(open/close - 1), 5)`

## Why submittable

- Minimal 3-factor EXCELLENT+ alpha from negation-dominant building block discovery.
- BRAIN self-corr **PASS** (0.7795) via Sharpe premium vs LLR0n261 (S=2.51).
- All 7 computable BRAIN checks pass.

## Risk

- Self-corr is above 0.7 raw threshold; relies on Sharpe premium escape (margin +0.009).
- Shares ptpr + open/close legs with several book entries (expected for this template family).

## Outcome

Submitted by the user on 2026-07-11. BRAIN reports `ACTIVE`, and all submission
checks pass. `data/book/GrLJLGN5.md` is reconciled to `status: ACTIVE`.
