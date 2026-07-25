---
id: "20260718-001"
date: "2026-07-18"
strategy: "EXPLORE"
research_question: "Can genuinely novel operator-tree shapes (ts_arg_min recency, multi-horizon spreads, IV-skew x lease/deferred-tax, L1-L2 fair-val dispersion, regime-divergence) plus event-magnitude on unused anchors (op_lease, goodwill_acquired, txfed, xintq, fair_val_l1/l3, accrued_liab_curr, interest_paid) with fresh stabilizers (anl4_fcf_flag) produce a decorrelated EXCELLENT+ alpha?"
budget_used: 20
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 12
submissions: 1
submittable_candidates: 1
submitted: ["xAd6K9Np"]
submitted_date: "2026-07-19"
status: "productive"
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
rounds: 1
simulations: 20
best_alpha: "xAd6K9Np"
best_grade: "EXCELLENT"
best_sharpe: 1.91
best_fitness: 2.02
best_self_corr: 0.6826
best_self_corr_peer: "wpl5eP5v"
best_self_corr_method: "AUTHORITATIVE BRAIN /alphas/xAd6K9Np/check (SELF_CORRELATION: {result: PASS, value: 0.6826, limit: 0.7})"
tags:
  - "session_20260718-001"
  - "EXPLORE"
  - "novel_structure"
  - "event_magnitude"
candidates:
  - id: "xAd6K9Np"
    grade: "EXCELLENT"
    sharpe: 1.91
    fitness: 2.02
    turnover: 0.1199
    self_corr_value: 0.6826
    self_corr_result: "PASS (AUTHORITATIVE, via BRAIN /check)"
    self_corr_peer: "wpl5eP5v"
    verdict: "SUBMITTED"
    status: "ACTIVE (submitted 2026-07-19 by human)"
  - id: "gJ9AY6dJ"
    grade: "EXCELLENT"
    sharpe: 2.45
    fitness: 2.25
    self_corr_value: 0.993
    self_corr_result: "FAIL"
    verdict: "BLOCKED (near-duplicate of ZYpjKeKx accrued_liab template)"
  - id: "pwKXqJEb"
    grade: "EXCELLENT"
    sharpe: 2.31
    fitness: 2.08
    self_corr_value: 0.681
    self_corr_result: "PENDING (server estimate)"
    verdict: "BLOCKED (LOW_SUB_UNIVERSE_SHARPE FAIL val=0.86 lim=1.0)"
  - id: "kqZdzozK"
    grade: "GOOD"
    sharpe: 1.85
    fitness: 1.51
    self_corr_value: 0.6004
    self_corr_result: "PENDING"
    verdict: "BELOW_TARGET (novel L1-L2 dispersion; LOW_SUB_UNIVERSE FAIL)"
---

# Session 20260718-001: EXPLORE — Accrued-Current Event-Magnitude + Fresh FCF Stabilizer

## Outcome

**Found:** [xAd6K9Np](https://platform.worldquantbrain.com/alpha/xAd6K9Np) —
EXCELLENT, S=1.91, F=2.02, T=12.0%, **all 8 BRAIN checks PASS**, including
SELF_CORRELATION confirmed **AUTHORITATIVELY** via BRAIN
`/alphas/xAd6K9Np/check`: `{result: PASS, value: 0.6826, limit: 0.7}` vs
top peer `wpl5eP5v` (ppegtq event-magnitude). Local PnL vs-book matched
(max 0.683). Initially recorded PENDING (agent did not submit). **Update 2026-07-19:**
submitted by human; BRAIN confirms `status: ACTIVE`, remaining checks PASS.
`data/book/xAd6K9Np.md` and `submit-xad6k9np.md` updated accordingly.

## Context Assessment (Phase 0)

- Book: ~46 ACTIVE + ~10 PENDING across 50+ mechanism families.
- No open high-priority hypothesis opportunities (non-submit files
  closed/exhausted/static reference).
- Last 3 sessions: EXPLORE / EXPLORE / HYPOTHESIS → decision tree DEFAULT →
  EXPLORE.
- HF server healthy: 53434→53454 results, budget 5000→4980, worker idle then
  at_capacity during batch. No new-24h gate-passers at session start.
- Novelty rule applied: 10/20 round-1 expressions used novel tree shapes.

## Strategy

```
STRATEGY: EXPLORE
TARGET: Novel trees on unused fundamental2/6 anchors + event-magnitude with fresh stabilizers
BUDGET: unlimited (satisfice on first EXCELLENT+ SAFE)
CONSTRAINTS: novelty-required; avoid dead-zone templates
RATIONALE: No active HYPOTHESIS; no novel-family EXPLOIT target; DEFAULT → EXPLORE.
```

## Key Findings

- `fn_accrued_liab_curr_q` (current accrued liabilities) is a viable event-magnitude
  anchor distinct from book sibling `fn_accrued_liab_q` (`ZYpjKeKx`). Copying the
  ZYpjKeKx analyst-flag recipe onto `_curr` yields EXCELLENT but self-corr 0.993 FAIL.
  Switching to leverage + ivaco + fresh `anl4_fcf_flag` densifier passes self-corr
  at 0.6826.
- `anl4_fcf_flag` works as a fresh-stabilizer densifier (same role as `anl4_gric_flag`
  / `anl4_cff_flag` in prior sessions) — never previously in the book.
- Most novel tree shapes (multi-horizon, IV-skew×lease/tax, debt-rate×pcr,
  regime-divergence, ts_arg_min) capped at AVERAGE/INFERIOR this round.
- L1−L2 fair-val level dispersion (`kqZdzozK`) reached GOOD with promising low
  corr (~0.60) but failed LOW_SUB_UNIVERSE — worth a densifier refine later.
- `fn_liab_fair_val_l1_q` event-magnitude reached EXCELLENT aggregate but failed
  LOW_SUB_UNIVERSE (0.86 < 1.0).

## Next Steps

- Human may submit `xAd6K9Np` via platform URL (agent does not submit).
- Optional follow-up: densify `kqZdzozK` (L1−L2 dispersion) or fix
  `pwKXqJEb` SUB_UNIVERSE — not needed for this session's satisfice goal.
