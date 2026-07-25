---
id: "20260715-003-results"
session: "20260715-003"
total_expressions: 55
gate_passers: 5
best_sharpe: 2.15
best_fitness: 3.06
best_alpha_id: "d50Jdpg2"
---

# Results: Session 20260715-003

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 55 |
| Gate-passers (S>=1.25, F>=1.0) | 5 |
| Best Sharpe | 2.15 (`d50Jdpg2`) |
| Best Fitness | 3.06 (`d50Jdpg2`) |
| Budget used | 55 / unlimited |

## Gate-Passers

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Verdict |
|---|----------|-----------|--------|---------|----------|---------|
| 1 | `d50Jdpg2` | `mibnq event-mag + zscore(ts_mean(IV90_call-put,22))` MARKET | 2.15 | 3.06 | 6.3% | BLOCKED (est. self-corr 0.824) |
| 2 | `np2GnbLd` | `pstkrv event-mag + zscore(ts_mean(IV90_call-put,22))` SUBINDUSTRY | 2.03 | 2.45 | 7.7% | FAIL LOW_SUB_UNIVERSE_SHARPE (0.75 vs 0.88); also est. BLOCKED on corr (0.725) |
| 3 | `0mEZAgAp` | `pstkrv event-mag + IV90 spread + volume/adv20` MARKET | 1.69 | 1.98 | 12.8% | BLOCKED (est. self-corr 0.735) |
| 4 | `E5Enqdj1` | `pstkrv event-mag + IV90 spread + sales_estimate_count` MARKET | 1.62 | 1.76 | 11.3% | not individually checked, expected BLOCKED (same family) |
| 5 | `781PxNj1` | `pstkrv event-mag + IV90 spread + historical_vol_90` SUBINDUSTRY | 1.51 | 1.66 | 8.3% | not individually checked, expected BLOCKED (same family) |

## All Expressions Tested (by round)

### Round 1 (18 sims) — fresh stabilizer substitutes for ivaco/drlt/flag/buzz
All 18 INFERIOR. Best: `1Yd3LrAM` (`pstkrv` + `drlt` + `volume/adv20` +
`sales_estimate_count`), S=1.41, F=0.88.

### Round 2 (14 sims) — sparse `-ts_zscore` fields, rank-blended
All 11 completed variants INFERIOR (3 still pending at session end, all
subsequently confirmed INFERIOR too — see meta.md). Best: `d50JlxNx`
(`goodwill` + `ivaco`), S=0.69, F=0.63. 2 `trade_when` concentrated-weight
fix attempts (`fnd6_txbcof`, `fnd6_fyrc`) failed with a unit-mismatch error.

### Round 3 (6 sims) — options-family stabilizer (IV90 spread)
`np2GnbLd` EXCELLENT (S=2.03, F=2.45) but FAIL LOW_SUB_UNIVERSE_SHARPE. 2
INFERIOR (`rank()`-form IV spread instead of `zscore(ts_mean(...))`, and
+`historical_volatility_90` third leg).

### Round 4 (9 sims) — LOW_SUB_UNIVERSE_SHARPE fixes (breadth legs, MARKET, decay sweep)
`d50Jdpg2` SPECTACULAR (S=2.15, F=3.06), `0mEZAgAp`/`E5Enqdj1` GOOD, 1 AVERAGE.

### Diagnostic (2 sims) — pure anchor, no secondary leg
`xAk7RElJ` (`pstkrv` alone) INFERIOR (S=0.43, F=0.17) but self-corr **SAFE
(0.496)**. `E5EnkM6L` (`mibnq` alone) INFERIOR (S=-0.39).

### Round 5 (4 sims) — dual weak-anchor blend (pstkrv + mibnq, no other leg)
All 4 INFERIOR (best F=0.45).

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| `d50Jdpg2` | PASS | PASS | PASS | PASS | PASS | PASS | est. FAIL (0.824 local) | PASS |
| `np2GnbLd` | PASS | PASS | PASS | PASS | PASS | **FAIL (0.75 vs 0.88)** | est. FAIL (0.725 local) | PASS |
| `0mEZAgAp` | PASS | PASS | PASS | PASS | PASS | PASS | est. FAIL (0.735 local) | PASS |

## Dead Ends / Errors This Session

| Expression shape | Result | Note |
|---|---|---|
| Any fresh non-family stabilizer on `pstkrv`/`mibnq` event-magnitude | INFERIOR (F<0.92) | New dead zone: `family-pstkrv-mibnq-generic-stabilizer-exhausted.md` |
| `rank()`-wrapped sparse `-ts_zscore(F,63)` fields, any blend | INFERIOR (F<0.68) | Extends `fundamental2_sparse_ts_zscore` dead zone to 2 new fields |
| `trade_when(ts_std_dev(returns,20) > 0.02, -ts_zscore(F,63), ...)` | Unit-mismatch error | 2nd occurrence this session pair; likely platform issue today |
