---
id: "20260712-001"
date: "2026-07-12"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
status: "productive"
budget: "unlimited"
budget_used: 44
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
research_question: "Can cross-dataset event-magnitude (fundamental×options IV) with a fresh fundamental anchor produce a decorrelated SPECTACULAR+ alpha?"
rounds: 4
gate_passers: 39
submissions: 0
submittable_candidates: 1
winner: "VkPdaQ2b"
winner_grade: "SPECTACULAR"
winner_sharpe: 2.18
winner_fitness: 2.65
winner_self_corr: 0.697
winner_self_corr_result: "PASS (local ≤ 0.70 auto-pass threshold)"
tags:
  - "session_20260712-001"
  - "EXPLORE"
  - "gric_flag_spread"
  - "multi_horizon_spread"
  - "event_magnitude"
  - "iv_spread"
  - "cptmfmq_dlttq"
---

# Session 20260712-001: EXPLORE — gric_flag Multi-Horizon Spread + Fresh Stabilizers

## Context Assessment (Phase 0)

- **Book:** 46 ACTIVE + 10 PENDING across 53+ mechanism families.
- **Event-magnitude family:** 5 ACTIVE + 1 ACTIVE (YP0bLdzA, submitted 2026-07-11) entries —
  itci, ppegtq, tlcf, txw, fn_liab_fair_val_l2_q as anchors. Family near-saturated.
- **Dead zones:** `{open/close-1 + ptpr/netdebt_flag}` skeleton always gives 0.74-0.91
  self-corr (rule: overnight-gap-flag-skeleton-saturated). `fnd6_dltis` dead in event-magnitude
  (0.94 corr with WjGVJ7bN). `negated-fresh-fundamental6-blends` dead.
- **24h gate-passers:** `anl4_gric_flag` multi-horizon spread EXCELLENT (S=2.15–2.53, F=2.24–2.37)
  but ALL used the saturated skeleton → all blocked. `fn_liab_fair_val_l2_q` variants already
  exploited. No genuinely new mechanism family gate-passer → EXPLOIT doesn't trigger.
- **Opportunities:** All hypothesis files closed/resolved. No RECOMBINE trigger.
- **Strategy:** EXPLORE — `anl4_gric_flag` multi-horizon spread on event-magnitude-style
  template (avoiding skeleton), plus `anl4_epsr_flag` × fresh fundamental as secondary direction.

## Key Insight from 20260711 Results

The `anl4_gric_flag` multi-horizon spread (EXCELLENT S=2.53 on the skeleton) was BLOCKED
only because of the skeleton, not because of the signal quality. The signal itself is strong.
Testing it on a leverage + fresh-stabilizer template (analogous to the proven event-magnitude
template) should preserve signal strength while breaking the self-corr bottleneck.

## Key Insights

1. **gric_flag multi-horizon spread is PnL-similar to txw event-magnitude** — both capture earnings-event dynamics. Any multi-horizon spread of an analyst flag correlated with WjGVJ7bN (excise_tax_event_magnitude) via primary signal proximity + shared stabilizers.

2. **ALL event-magnitude fundamentals firing at earnings time are correlated** — epsr_flag, fatl, dlto event-magnitudes share the earnings timing pattern with existing book entries. Shared stabilizers (ivaco/buzz/drlt) compound this to 0.7-0.9 correlation.

3. **The cross-dataset IV stabilizer creates overlap with the options IV family** — using `zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22))` inside any alpha creates 0.64-0.76 correlation with vRm07LP3 (options_iv_spread) and omY3pZq2 (sentiment_iv_spread).

4. **Diluting the IV weight via a 4th fresh-field component decorrelates from the IV family** — adding `anl4_gric_flag` as 4th factor (reducing IV from 1/3 → 1/4 weight) dropped the omY3pZq2 correlation from 0.758 → 0.670 and the npWYoqQz correlation from 0.716 → 0.697 (below 0.70 auto-pass threshold).

5. **Vol-gated trade_when fails for abs-delta inner expressions** — confirmed: `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(abs(ts_delta(F/close, d))) + ..., 5), ...)` causes BRAIN unit-type error. Vol-gate only works with level/rank inner expressions (cf. 0m7lnAEr).

## Round Log

### Round 1 (r1_gric_spread): gric_flag multi-horizon spread → BLOCKED 0.925 vs WjGVJ7bN
### Round 2 (r2_epsr_fatl_dlto): epsr/fatl/dlto event-magnitude → BLOCKED 0.768-0.908 (earnings timing)
### Round 3 (r3_ivfresh): cptmfmq/dlto event-magnitude + IV → 9qrEVpMV SPECTACULAR 0.758 (0.013 short of escape threshold)
### Round 4 (r4_iv_variants): IV form variants + gric_flag → **VkPdaQ2b SPECTACULAR 0.697 AUTO-PASS ← WINNER**
