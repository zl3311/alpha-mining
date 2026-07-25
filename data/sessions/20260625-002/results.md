---
id: "20260625-002-results"
session: "20260625-002"
total_expressions: 26
gate_passers: 16
best_sharpe: 3.02
best_fitness: 3.48
best_alpha_id: "P0p7LAvL"
---

# Results: Session 20260625-002

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 26 |
| Gate-passers (S>=1.25, F>=1.0) | 16 |
| SPECTACULAR count | 16 |
| Best Sharpe | 3.04 (IV60 variant, blocked by self-corr) |
| Best Fitness | 5.13 (IV60 variant, blocked by self-corr) |
| Best submittable | P0p7LAvL S=3.02 F=3.48 (non-IV, PASS) |
| Budget used | 26 / no cap |

## Strategy A: Fix SUB_UNIVERSE on IV60 Blends (13 sims)

| Alpha ID | Expression (abbrev) | S | F | T% | IS Checks | Self-Corr |
|----------|--------------------:|--:|--:|---:|-----------|-----------|
| kq3jpXrz | IV60+guidance+bvps+itci | 2.82 | 5.04 | 4.6 | ALL PASS | FAIL 0.83 |
| MPp7v5dL | IV60+guidance+bvps+dlto | 2.82 | 5.04 | 4.4 | ALL PASS | FAIL (est) |
| kq3jpnOP | IV60+guidance+bvps+acdo | 2.81 | 5.02 | 4.3 | ALL PASS | FAIL (est) |
| e7OzMOZN | IV60+guidance+dpactq+bvps | 2.72 | 4.83 | 9.1 | ALL PASS | FAIL 0.81 |
| 3q7p9OZO | IV60(66d)+guidance+bvps | 3.04 | 5.13 | 5.2 | FAIL SUB | — |
| qMAj267E | IV60+guidance+epsr+bvps | 2.70 | 4.13 | 6.2 | FAIL SUB | — |
| 88zlWeQm | IV60+guidance+bvps (MARKET,d5) | 2.73 | 4.01 | 5.8 | ? | — |
| blLj1e7r | IV60+guidance+fatl+bvps | 2.47 | 3.69 | 6.4 | ? | — |
| P0p7L0AJ | IV60+guidance+bvps (MARKET,d8) | 2.24 | 3.32 | 5.7 | ? | — |
| E5wln5MP | IV60+guidance+bvps+operating_income | 2.29 | 3.22 | 6.0 | ? | — |
| npg7G0ga | IV60+guidance+sales_est+bvps | 2.30 | 3.21 | 5.6 | ? | — |
| zq9k7paE | IV60+guidance+bvps (MARKET,d10) | 2.23 | 3.14 | 5.9 | ? | — |
| zq9k73AG | IV60(66d)+guidance+bvps (MARKET) | 1.93 | 2.67 | 6.1 | ? | — |

**Conclusion**: 4-factor IV60 blends pass all IS checks (sub-universe fixed) but fail self-corr (0.81-0.83 against 88z7MM37 S=2.78, premium escape requires S>=3.06).

## Strategy B: Novel Non-IV Blends (13 sims)

| Alpha ID | Expression (abbrev) | S | F | T% | IS Checks | Self-Corr |
|----------|--------------------:|--:|--:|---:|-----------|-----------|
| **P0p7LAvL** | **acdo+open/close+ptpr_flag+itci** | **3.02** | **3.48** | **13.7** | **ALL PASS** | **0.63 PASS** |
| **3q7lm2p6** | **acdo+open/close+netdebt_flag+itci** | **2.95** | **3.44** | **14.9** | **ALL PASS** | **~PASS** |
| Wjp7rYeN | acdo+open/close+bvps_flag+itci | 2.53 | 2.80 | 14.9 | FAIL SUB | — |
| 88zlW2mv | dpactq+epsr+dlto+acdo | 1.35 | 1.27 | 6.3 | — | — |

**Conclusion**: The `acdo + open/close + analyst_flag + itci` template produces SPECTACULAR grade with self-corr well below 0.7. The `ptpr_flag` variant (P0p7LAvL) is the strongest.

## Winner: P0p7LAvL

| Check | Result | Value | Limit |
|-------|--------|-------|-------|
| LOW_SHARPE | PASS | 3.02 | 1.25 |
| LOW_FITNESS | PASS | 3.48 | 1.0 |
| LOW_TURNOVER | PASS | 13.7% | 1% |
| HIGH_TURNOVER | PASS | 13.7% | 70% |
| CONCENTRATED_WEIGHT | PASS | — | — |
| LOW_SUB_UNIVERSE_SHARPE | PASS | 1.38 | 1.31 |
| SELF_CORRELATION | PASS | 0.6318 | 0.70 |
| MATCHES_COMPETITION | PASS | — | — |
