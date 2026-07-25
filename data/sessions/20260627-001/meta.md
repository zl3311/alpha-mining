---
id: "20260627-001"
date: "2026-06-27"
strategy: "EXPLORE"
trigger: "cron"
budget: "unlimited"
budget_used: 0
target_grade: "EXCELLENT+"
status: "completed"
result: "3 EXCELLENT submittable candidates identified (from prior session gate-passers)"
gate_passers: 3
submissions: 1
submitted: ["XgpJGaL0"]
candidates:
  - id: "XgpJGaL0"
    grade: "EXCELLENT"
    sharpe: 2.08
    fitness: 2.36
    self_corr_value: 0.604
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "MPp3WAd9"
    grade: "EXCELLENT"
    sharpe: 1.95
    fitness: 2.42
    self_corr_value: 0.662
    self_corr_result: "PASS"
    verdict: "BLOCKED — sibling XgpJGaL0 now ACTIVE (mutual corr ~0.90-0.95)"
  - id: "E5wR7wN0"
    grade: "EXCELLENT"
    sharpe: 1.95
    fitness: 2.36
    self_corr_value: 0.632
    self_corr_result: "PASS"
    verdict: "BLOCKED — sibling XgpJGaL0 now ACTIVE (mutual corr ~0.90-0.95)"
best_alpha: "XgpJGaL0"
best_sharpe: 2.08
best_fitness: 2.36
best_self_corr: 0.604
---

# 20260627-001: EXPLORE Session — Cumulative Revision + Depreciation Discovery

## Context Assessment

- Book: 30+ ACTIVE alphas, 9 SPECTACULAR, ~20 EXCELLENT
- Self-corr wall: 0.7 threshold + 1.10x Sharpe premium escape
- Field exploration effectively complete; need structurally novel templates
- No active hypothesis opportunities (all closed/resolved)
- HF server: healthy, 4819 budget remaining, worker at capacity

## Strategy

EXPLORE mode. Checked recent gate-passers from HF server for novel submittable
candidates. Found EXCELLENT results from a cumulative-revision + depreciation
family (`zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close)`).

## Key Discovery: Cumulative Revision + Depreciation Family

The template `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + STABILIZER, 5)` produces a family of EXCELLENT-grade alphas that pass all 8 BRAIN checks AND self-correlation.

### Novel elements
- `fnd6_newqv1300_dpactq` (quarterly depreciation of property/assets) adds a
  depreciation-intensity value signal that combines well with analyst revision
- The `zscore(ts_sum())` wrapper avoids the `flag*(-ret)` driver that saturates existing analyst entries
- Three different stabilizer legs produce viable candidates

### Results

| Alpha | Expression (stabilizer) | S | F | T | Self-Corr | BRAIN |
|-------|------------------------|---|---|---|-----------|-------|
| XgpJGaL0 | + rank(open/close - 1) | 2.08 | 2.36 | 16.0% | 0.604 PASS | ALL PASS |
| MPp3WAd9 | + rank(-1 * equity/assets) | 1.95 | 2.42 | 9.7% | 0.662 PASS | ALL PASS |
| E5wR7wN0 | + rank(abs(ts_delta(dpactq/close, 3))) | 1.95 | 2.36 | 13.3% | 0.632 PASS | ALL PASS |

### Submission Recommendation

Per submission-priority-long-term rule: submit **XgpJGaL0** first (lowest self-corr
0.604, highest Sharpe 2.08). The other two are companions at higher self-corr.

**NOT submitted** at session time. Subsequently submitted and confirmed ACTIVE on BRAIN.

## Lessons Learned

1. **`fnd6_newqv1300_dpactq` is a productive novel field** — depreciation as a
   value signal decorrelates from existing book families
2. **BRAIN self-corr ≈ PnL corr for this family** — no inflation (multiplier ~1.0x),
   confirming the 1.45-1.6x gap is specific to IV270 spread, not universal
3. **Three stabilizer variants all pass** — intraday reversal, leverage, and event
   magnitude each provide viable third legs
4. **The cumrev template generalizes** — `zscore(ts_sum(flag, 22))` combined with
   novel fundamental legs continues to produce EXCELLENT results
