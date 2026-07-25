---
alpha_id: "GrLJLGN5"
status: "ACTIVE"
submitted: "2026-07-11"
grade: "EXCELLENT"
sharpe: 2.77
fitness: 2.40
turnover: 0.207
decay: 6
neutralization: "SUBINDUSTRY"
universe: "TOP3000"
region: "USA"
family: "negated_relationship_return_intraday_blend"
self_corr_max: 0.7795
self_corr_peer: "LLR0n261"
self_corr_result: "PASS"
session: "20260705-001"
brain_url: "https://platform.worldquantbrain.com/alpha/GrLJLGN5"
expression: "ts_decay_linear(rank(-1 * rel_ret_cust) + rank(anl4_ptpr_flag) + rank(open/close - 1), 5)"
---

# GrLJLGN5 — Negated Customer Return + PTPR + Intraday Gap

## Expression

```
ts_decay_linear(rank(-1 * rel_ret_cust) + rank(anl4_ptpr_flag) + rank(open/close - 1), 5)
```

## Mechanism

Minimal 3-factor cross-direction blend from the negation sweep building blocks:

1. **rank(-1 * rel_ret_cust)** (pv13): Customer relationship return signal, reversed.
   High customer-linked returns often reflect supply-chain dependency or
   customer-concentration risk; negating captures the underperformance of
   stocks overly tied to customer momentum.

2. **rank(anl4_ptpr_flag)** (analyst4): Pre-tax profit revision catalyst.

3. **rank(open/close - 1)** (price): Overnight gap confirmation.

## Self-Correlation (BRAIN authoritative)

- BRAIN `/check` SELF_CORRELATION: **PASS**, value=0.7795, limit=0.7
- Top peer: `LLR0n261` (S=2.51) — Sharpe premium escape: 2.77 >= 1.10 × 2.51 = 2.761
- Other peers: omVpwdqk (0.680), vR56vdYd (0.670), JjpzQAze (0.651), O0ZOJbaq (0.651)

## BRAIN Checks

All 7 computable checks PASS (verified via `brain_check.py`).
