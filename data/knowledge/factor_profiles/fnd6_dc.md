---
field: fnd6_dc
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.03
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.4761
ann_vol: 0.2008
hit_rate: 0.4704
rolling_sharpe_min: -1.234
rolling_sharpe_max: 2.936
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.69
---
# fnd6_dc (fundamental6)

*Deferred Charges*

## Signal Profile
- `rank(fnd6_dc)`: S=0.54, F=0.19, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_dc / close)`: S=0.62, F=0.24, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dc, 5))`: S=0.49, F=0.38, T=16.7%, INFERIOR (TOP200)
- `-rank(fnd6_dc)`: S=0.15, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dc, 5))`: S=-0.14, F=-0.06, T=16.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dc, 22)`: S=0.22, F=0.14, T=13.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dc, 10)`: S=0.12, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dc, 22))`: S=1.03, F=0.92, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dc)`: S=0.34, F=0.16, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dc / close)`: S=0.33, F=0.16, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+5.3%
  - 2020: S=1.11 (moderate), ret=+19.9%
  - 2021: S=0.48 (weak), ret=+8.0%
  - 2022: S=0.03 (weak), ret=+0.8%
  - 2023: S=0.88 (moderate), ret=+13.9%

## Risk & Drawdown
- Max drawdown: 47.61% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +9.8%, volatility 20.1% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew -1.37, excess kurtosis +26.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 2.94, latest 0.86

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +16.54%; worst month: -16.05%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.86
- Sideways: S=0.96
- Bear: S=-0.46

## Negated Direction
Best negated: `rank(-1 * fnd6_dc)` S=0.34, F=0.16, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dc)`: S=0.34, F=0.16, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dc / close)`: S=0.33, F=0.16, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dc, 5))`: S=-0.14, F=-0.06, T=16.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dc, 5))` | TOP200 | 0.49 | 0.38 | 47.6% | 100% | mixed |
| `rank(ts_delta(fnd6_dc, 5))` | TOP1000 | 0.53 | 0.33 | 25.0% | 60% | mixed |
| `rank(fnd6_dc / close)` | TOP3000 | 0.64 | 0.24 | 5.6% | 60% | mixed |
| `rank(fnd6_dc)` | TOP3000 | 0.56 | 0.19 | 7.0% | 60% | bull-only |
| `rank(fnd6_dc / close)` | TOP500 | 0.41 | 0.16 | 12.1% | 60% | bull-only |
| `rank(fnd6_dc)` | TOP500 | 0.33 | 0.11 | 13.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_dc, 5))` | TOP500 | 0.19 | 0.07 | 39.6% | 60% | mixed |
| `rank(ts_delta(fnd6_dc, 5))` | TOP3000 | 0.14 | 0.04 | 41.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- parkinson_volatility_150: -0.395 (weakly negatively correlated)
- unsystematic_risk_last_30_days: -0.393 (weakly negatively correlated)
- historical_volatility_150: -0.388 (weakly negatively correlated)
- parkinson_volatility_180: -0.387 (weakly negatively correlated)
- historical_volatility_180: -0.381 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
