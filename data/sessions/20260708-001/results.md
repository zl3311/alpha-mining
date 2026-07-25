---
id: "20260708-001-results"
session: "20260708-001"
total_expressions: 95
gate_passers: 36
best_sharpe: 2.62
best_fitness: 2.73
best_alpha_id: "wpl5eP5v"
best_submittable_alpha_id: "wpl5eP5v"
---

# Results: Session 20260708-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 95 |
| Gate-passers (S>=1.25, F>=1.0) | 36 |
| Best Sharpe (any) | 2.62 (itci control, corr-blocked) |
| Best Fitness (any) | 2.73 (itci control, corr-blocked) |
| Best submittable | wpl5eP5v — EXCELLENT S=2.09 F=2.20, self-corr PASS 0.6676 |
| Rounds | 7 |
| Budget used | 95 (unlimited) |

## Submittable Candidate

| Alpha ID | Expression | Sharpe | Fitness | Turnover | Grade | Self-Corr | Verdict |
|----------|-----------|--------|---------|----------|-------|-----------|---------|
| wpl5eP5v | `ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_ppegtq / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close), 5)` | 2.09 | 2.20 | 8.7% | EXCELLENT | 0.6676 PASS | SAFE |

Platform: https://platform.worldquantbrain.com/alpha/wpl5eP5v

## Round-by-Round Gate-Passers (S>=1.25, F>=1.0)

### Round 1 — negated fresh fundamental6 blends (19 sims, 0 gate-passers)
All INFERIOR/AVERAGE. Best: `rank(-1*fnd6_intc/close)*sign(-1*ts_delta(fnd6_txw,5)) + rank(-1*fnd6_txdbca)` S=0.79 F=1.06 AVERAGE.

### Round 2 — negated blocks + value anchors + diagnostics (16 sims, 0 gate-passers)
All INFERIOR. Diagnostics proved negation-asymmetry pattern stale: `rank(-1*fnd6_intc/close)` S=-0.82 (claimed 1.32), `rank(-1*fnd6_txdbca)` S=0.36 (claimed 1.06), `rank(-1*fnd6_txw)` S=0.53 (claimed 0.89).

### Round 3 — event-magnitude transfer screen (13 sims, 10 gate-passers)

| Alpha ID | Field | Expression (short) | S | F | Grade | Self-Corr |
|----------|-------|---------------------|---|---|-------|-----------|
| kq0nbNkd | itci (control) | abs(ts_delta(itci/close,3))+lev+drlt | 2.62 | 2.73 | SPECTACULAR | blocked (itci family) |
| E5EqbQRP | ppegtq | abs(ts_delta(ppegtq/close,3))+lev+drlt | 1.72 | 1.74 | GOOD | PASS 0.660 |
| KP9n6KNz | (base) | lev+drlt | 1.88 | 1.58 | GOOD | n/a |
| P03n6nmE | cshtr | abs(ts_delta(cshtr,3))+lev+drlt | 1.89 | 1.58 | GOOD | FAIL 0.793 |
| 0mEAdNl8 | drc d=5 | abs(ts_delta(drc/close,5))+lev+drlt | 1.83 | 1.52 | GOOD | FAIL 0.753 |
| RR8NYLej | drc d=3 | abs(ts_delta(drc/close,3))+lev+drlt | 1.82 | 1.51 | GOOD | FAIL 0.757 |
| 2rLvRP6Y | dd1q | abs(ts_delta(dd1q/close,3))+lev+drlt | 1.65 | 1.51 | GOOD | PASS 0.680 |
| mLbqAv0W | dd1q d=5 | d=5 variant | 1.61 | 1.45 | AVERAGE | n/a |
| 2rLvQVRw | sales_est d=3 | abs(ts_delta(sales_est,3))+lev+drlt | 1.77 | 1.42 | AVERAGE | n/a |
| vRl5zxPd | sales_est d=5 | d=5 variant | 1.76 | 1.39 | AVERAGE | n/a |

### Round 4 — event-magnitude + alt stabilizers (15 sims, ~10 gate-passers)

| Alpha ID | Expression (short) | S | F | Grade |
|----------|---------------------|---|---|-------|
| 9qr9AXde | drc d=5+lev+drlt+sales_est (4fac) | 2.05 | 1.74 | GOOD |
| (drc d=5+lev+ivaco) | drc d=5+lev+ivaco | 2.04 | 1.81 | GOOD |
| XgnkYALm | cshtr+lev+drlt decay=10 | 1.90 | 1.60 | GOOD |
| E5EqgLd1 | drc d=3+lev+drlt+acdo (4fac) | 1.90 | 1.61 | GOOD |
| zqm5onQV | drc d=5+lev+acdo | 1.81 | 1.55 | GOOD |
| LL1nlW6n | drc d=3+lev+acdo | 1.80 | 1.54 | GOOD |
| rKlbzaZE | ppegtq+lev+acdo | 1.55 | 1.53 | GOOD |
| MPQb8Yb9 | cshtr+lev+acdo | 1.67 | 1.41 | AVERAGE |
| (+ cshtr+ivaco, cshtr+fatl AVERAGE) | | | | |

### Round 5 — ppegtq/dd1q fitness boost (12 sims, ~7 gate-passers)

| Alpha ID | Expression (short) | S | F | Grade | Self-Corr |
|----------|---------------------|---|---|-------|-----------|
| np2n36VM | ppegtq+lev+drlt+dlto (4fac) | 1.77 | 1.92 | GOOD | FAIL |
| WjGNg8JZ | ppegtq+lev+drlt+acdo (4fac) | 1.79 | 1.85 | GOOD | (timed out) |
| 781xJ3J2 | ppegtq+lev+ivaco | 1.84 | 1.81 | GOOD | FAIL |
| P03n1eYJ | ppegtq+lev+drlt+fatl (4fac) | 1.64 | 1.79 | GOOD | (timed out) |
| 88QOLqXm | dd1q+lev+drlt decay=10 | 1.65 | 1.51 | GOOD | n/a |
| LL1nkPYM | ppegtq d=10+lev+drlt | 1.52 | 1.46 | AVERAGE | n/a |
| 1YdoJnZz | ppegtq+dd1q+lev (dual event) | 1.44 | 1.46 | AVERAGE | n/a |

### Round 6 — ppegtq + ivaco + stabilizer combos (10 sims, 7 gate-passers)

| Alpha ID | Expression (short) | S | F | Grade | Self-Corr |
|----------|---------------------|---|---|-------|-----------|
| **wpl5eP5v** | **ppegtq+lev+ivaco+drlt (4fac)** | **2.09** | **2.20** | **EXCELLENT** | **PASS 0.6676** |
| KP9nbgjl | ppegtq+lev+ivaco+sales_est | 1.96 | 1.89 | GOOD | n/a |
| zqm59lYR | ppegtq d=5+lev+ivaco+dlto | 1.77 | 1.87 | GOOD | n/a |
| vRl5LzA3 | ppegtq+lev+ivaco+fatl | 1.72 | 1.86 | GOOD | n/a |
| blqNLKlr | ppegtq+lev+ivaco decay=10 | 1.84 | 1.81 | GOOD | n/a |
| LL1npGYm | ppegtq d=5+lev+ivaco | 1.77 | 1.72 | GOOD | n/a |
| 9qr9webr | dd1q+lev+ivaco | 1.69 | 1.59 | GOOD | n/a |

### Round 7 — weight-rebalance variants (10 sims, in-flight at session end)
Submitted but not collected (satisficed on wpl5eP5v before round 7 completed).

## BRAIN Check Results (submittable candidate)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| wpl5eP5v | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.6676) | PASS |

All 8 checks PASS (7 computable via brain_check.py f=0 ALL PASS + SELF_CORRELATION PASS via /check).
