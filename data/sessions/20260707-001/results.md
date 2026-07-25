---
id: "20260707-001-results"
session: "20260707-001"
total_expressions: 8
gate_passers: 6
best_sharpe: 2.62
best_fitness: 2.74
best_alpha_id: "2rLRzov8"
best_submittable_id: "2rLRzov8"
---

# Results: Session 20260707-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Candidates verified (24h queue, novel negated direction) | 8 |
| Passed all 7 computable BRAIN checks | 6 |
| Authoritative self-corr PASS (EXCELLENT+) | 1 |
| Best submittable Sharpe / Fitness | 2.06 / 2.13 |
| Budget used (new simulations) | 0 (verification-only session) |
| Strategy | EXPLOIT (24h gate-passer verification + self-corr) |

## Candidate Verification Table

| # | Alpha ID | Grade | S | F | T | Family | BRAIN 7-check | Self-Corr | Verdict |
|---|----------|-------|---|---|---|--------|---------------|-----------|---------|
| 1 | 1Yd65kmJ | SPECTACULAR | 2.62 | 2.74 | 3.5% | itci_event_magnitude_neg_leverage | ALL PASS | 0.997 vs 0m8GV1Pp → **FAIL** | BLOCKED (duplicate of 0m8GV1Pp, delta 5 vs 3) |
| 2 | VkPnWlMb | EXCELLENT | 2.37 | 2.18 | 17.0% | negated_tax_intraday | ALL PASS | 0.939 → **FAIL** | BLOCKED (saturated ptpr+open/close core) |
| 3 | RR8Xg8wb | EXCELLENT | 2.31 | 2.07 | 17.6% | negated_deferred_tax_intraday | ALL PASS | 0.941 → **FAIL** | BLOCKED (saturated ptpr+open/close core) |
| 4 | **2rLRzov8** | **EXCELLENT** | **2.06** | **2.13** | **12.8%** | **negated_enterprise_value_blend** | **ALL PASS** | **0.6495 → PASS** | **SAFE** |
| 5 | YP0XZxav | EXCELLENT | 2.02 | 2.22 | 5.4% | itci_event_magnitude_netdebt | FAIL LOW_SUB_UNIVERSE_SHARPE (0.84<0.87) | n/a | BLOCKED |
| 6 | JjOmZ9rn | EXCELLENT | 1.90 | 2.19 | 14.1% | negated_enterprise_value_blend | ALL PASS | UNCHECKED (BRAIN timeout) | RISKY / REDUNDANT with 2rLRzov8 |
| 7 | 88QrdQ7z | EXCELLENT | 1.82 | 2.15 | 11.7% | negated_enterprise_value_blend | ALL PASS | UNCHECKED (BRAIN timeout) | RISKY / REDUNDANT with 2rLRzov8 |
| 8 | xAkXAYZJ | EXCELLENT | 1.74 | 2.01 | 11.2% | dpactq_event_magnitude_flags | FAIL LOW_SUB_UNIVERSE_SHARPE (0.72<0.75) | n/a | BLOCKED |

## Winner: 2rLRzov8 (SAFE)

**Expression:**
```
ts_decay_linear(rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close - 1), 5)
```

**Config:** SUBINDUSTRY neutralization, decay 6, delay 1, truncation 0.08, TOP3000, USA

**Metrics:** EXCELLENT S=2.06, F=2.13, T=12.8%

**BRAIN checks:** All 7 computable PASS + authoritative SELF_CORRELATION PASS (0.6495 vs
O0ZOJbaq, below 0.7 auto-pass threshold).

**Platform URL:** https://platform.worldquantbrain.com/alpha/2rLRzov8

**Discovery session:** 20260706-002 (interrupted EXPLORE session; this session completed
the verification).

## Family Analysis: Negated-Direction Gate-Passers (24h queue)

Three novel negated-direction families appeared in the 24h gate-passers:

### Negated tax (fnd6_txw, fnd6_txdbca) — BLOCKED
`rank(-1 * fnd6_txw) + rank(anl4_ptpr_flag) + rank(open/close - 1)` reaches EXCELLENT
(S=2.37) but self-corr **0.94** vs book. The `anl4_ptpr_flag + open/close - 1` core is
the saturated cluster (LLR0n261 / O0ZOJbaq / O0pl2znv). Negating the fundamental anchor
does NOT decorrelate when the analyst-flag + intraday core is shared. Same wall that
blocked the 20260703-001 sales_estimate_count variants.

### Negated enterprise value — PASS (winner family)
`rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + ...` reaches EXCELLENT
and self-corr **0.6495**. The key decorrelation move is using `anl4_netdebt_flag` instead
of `anl4_ptpr_flag`, plus the negated EV anchor (no positive-EV or negated-EV entry in
book). Adding `fnd6_cshtr` + `fnd6_drlt` as quality companions lifts fitness without
re-correlating above 0.7.

### itci event-magnitude — BLOCKED
`rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)`
is SPECTACULAR (S=2.62) but self-corr **0.997** vs 0m8GV1Pp — it is a near-duplicate of
the existing book entry (same fields, delta 5 vs 3). The event-magnitude-on-itci family
is already claimed by 0m8GV1Pp / d5Q3ZmWv. The `abs(ts_delta(itci/close, 5)) + netdebt`
variant (YP0XZxav) is more decorrelated but fails LOW_SUB_UNIVERSE_SHARPE.

## BRAIN Check Detail (winner)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| 2rLRzov8 | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.6495) | PASS |
