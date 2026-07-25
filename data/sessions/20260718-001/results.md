---
id: "20260718-001-results"
session: "20260718-001"
total_expressions: 20
gate_passers: 12
best_sharpe: 2.45
best_fitness: 2.25
best_alpha_id: "xAd6K9Np"
---

# Results: Session 20260718-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 20 |
| Gate-passers (S>=1.25, F>=1.0) | 12 |
| Best Sharpe | 2.45 (gJ9AY6dJ, self-corr FAIL) |
| Best Fitness (submittable) | 2.02 (xAd6K9Np) |
| Budget used | 20 / unlimited |

## Gate-Passers

| # | Alpha ID | Expression (abbrev) | Sharpe | Fitness | Turnover | Verdict |
|---|----------|---------------------|--------|---------|----------|---------|
| 1 | xAd6K9Np | accrued_curr event + lev + ivaco + fcf + buzz | 1.91 | 2.02 | 12.0% | **SAFE** |
| 2 | gJ9AY6dJ | accrued_curr + cfi + bvps + buzz (ZYpjKeKx clone) | 2.45 | 2.25 | 27.8% | BLOCKED corr 0.993 |
| 3 | pwKXqJEb | fair_val_l1 event + lev + ivaco + fcf + buzz | 2.31 | 2.08 | 11.5% | BLOCKED SUB_UNIV |
| 4 | 3qebMb3z | op_lease event + lev + ivaco + drlt + buzz | 1.88 | 1.83 | 10.5% | BLOCKED corr 0.875 |
| 5 | JjvwVPYO | txfed event + lev + ivaco + buzz | 1.61 | 1.69 | 11.8% | BLOCKED corr 0.793 |
| 6 | bldkYLgq | assets_fair_val_l3 event + lev + ivaco + ffo + buzz | 1.93 | 1.63 | 10.8% | BLOCKED corr 0.724 |
| 7 | kqZdzozK | abs(L1−L2 fair_val)/close + lev + fcf | 1.85 | 1.51 | 2.4% | GOOD; SUB_UNIV FAIL |
| 8 | 2rN01epb | interest_paid event + lev + drlt + buzz | 1.58 | 1.47 | 11.1% | AVERAGE; corr FAIL |
| 9 | RR1MGE5a | accrued_curr event × fcf + buzz (product) | 1.78 | 1.46 | 23.9% | AVERAGE; corr FAIL |
| 10 | RR1MGoE1 | op_lease event + lev + ivaco + fcf + buzz | 1.54 | 1.37 | 11.9% | AVERAGE; corr FAIL |
| 11 | np8Jp1QE | dfdtxasoprlcarryfwd event + lev + ivaco + buzz | 1.49 | 1.34 | 11.0% | AVERAGE; corr FAIL |
| 12 | j2rvqd65 | ts_arg_min lease recency + lev + ivaco + buzz | 1.95 | 1.12 | 26.2% | AVERAGE; corr FAIL |

## All Expressions Tested

| # | Alpha ID | Sharpe | Fitness | Turnover | Status | Structure |
|---|----------|--------|---------|----------|--------|-----------|
| 1 | gJ9AY6dJ | 2.45 | 2.25 | 27.8% | GATE_PASS | accrued_curr clone of ZYpjKeKx |
| 2 | pwKXqJEb | 2.31 | 2.08 | 11.5% | GATE_PASS | fair_val_l1 event-mag |
| 3 | xAd6K9Np | 1.91 | 2.02 | 12.0% | GATE_PASS | accrued_curr + fresh fcf |
| 4 | 3qebMb3z | 1.88 | 1.83 | 10.5% | GATE_PASS | op_lease event-mag |
| 5 | JjvwVPYO | 1.61 | 1.69 | 11.8% | GATE_PASS | txfed event-mag |
| 6 | bldkYLgq | 1.93 | 1.63 | 10.8% | GATE_PASS | assets_fv_l3 event-mag |
| 7 | kqZdzozK | 1.85 | 1.51 | 2.4% | GATE_PASS | novel L1−L2 dispersion |
| 8 | 2rN01epb | 1.58 | 1.47 | 11.1% | GATE_PASS | interest_paid event-mag |
| 9 | RR1MGE5a | 1.78 | 1.46 | 23.9% | GATE_PASS | product event×fcf |
| 10 | RR1MGoE1 | 1.54 | 1.37 | 11.9% | GATE_PASS | op_lease + fcf |
| 11 | np8Jp1QE | 1.49 | 1.34 | 11.0% | GATE_PASS | deferred-tax-carryfwd event |
| 12 | j2rvqd65 | 1.95 | 1.12 | 26.2% | GATE_PASS | novel ts_arg_min |
| 13 | qM68Q7Gj | 1.26 | 0.94 | 9.2% | BELOW_GATE | MA crossover lease |
| 14 | ZYK5Y370 | 1.23 | 0.91 | 11.3% | BELOW_GATE | goodwill_acquired event |
| 15 | O0xOljnv | 1.07 | 0.78 | 4.2% | BELOW_GATE | goodwill × ffo product |
| 16 | LLdW0pM6 | 1.07 | 0.66 | 21.2% | BELOW_GATE | IV skew + lease |
| 17 | O0xOlbEJ | 1.12 | 0.63 | 20.8% | BELOW_GATE | IV skew + deferred tax |
| 18 | akE65P81 | 0.88 | 0.59 | 8.6% | BELOW_GATE | multi-horizon lease |
| 19 | 58kxPkKJ | 0.50 | 0.13 | 31.9% | BELOW_GATE | debt-rate + pcr_vol |
| 20 | np89LKVE | 0.17 | 0.05 | 52.8% | BELOW_GATE | regime-divergence interest |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|------------------|------------------|---------------------|
| xAd6K9Np | PASS | PASS | PASS | PASS | PASS | PASS (1.25≥0.83) | **PASS 0.6826** | PASS |
| pwKXqJEb | PASS | PASS | PASS | PASS | PASS | **FAIL 0.86<1.0** | PENDING ~0.681 | PASS |
| kqZdzozK | PASS | PASS | PASS | PASS | PASS | **FAIL 0.32<0.8** | PENDING ~0.600 | PASS |
| gJ9AY6dJ | (not fully checked) | | | | | | **FAIL 0.993** | |

## Winning Expression

```
ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```
