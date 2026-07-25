---
field: systematic_risk_last_30_days
dataset: model51
best_template: rank_delta
best_sharpe: 0.59
best_fitness: 0.21
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1921
ann_vol: 0.1052
hit_rate: 0.5134
rolling_sharpe_min: -1.164
rolling_sharpe_max: 2.302
negated_best_sharpe: 0.06
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.53
---
# systematic_risk_last_30_days (model51)

*The portion of the security’s return variance attributed to systematic (market) risk, quantified as R² from a regression on SPY, over the last 30 calendar days*

## Signal Profile
- `rank(systematic_risk_last_30_days)`: S=0.04, F=0.01, T=23.4%, INFERIOR (TOP3000)
- `rank(systematic_risk_last_30_days / close)`: S=0.00, F=0.00, T=15.6%, INFERIOR (TOP3000)
- `rank(ts_delta(systematic_risk_last_30_days, 5))`: S=0.59, F=0.21, T=48.0%, INFERIOR (TOP200)
- `-rank(systematic_risk_last_30_days)`: S=0.06, F=0.01, T=21.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_30_days, 5))`: S=-0.59, F=-0.15, T=52.0%, INFERIOR (TOP3000)
- `-ts_zscore(systematic_risk_last_30_days, 63)`: S=0.18, F=0.04, T=26.1%, INFERIOR (TOP3000)
- `ts_mean(systematic_risk_last_30_days, 10)`: S=-0.17, F=-0.09, T=9.1%, INFERIOR (TOP3000)
- `rank(ts_rank(systematic_risk_last_30_days, 22))`: S=0.04, F=0.00, T=34.1%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_30_days)`: S=-0.04, F=-0.01, T=23.4%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_30_days / close)`: S=0.00, F=0.00, T=17.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.61 (moderate), ret=+4.2%
  - 2020: S=0.80 (moderate), ret=+7.8%
  - 2021: S=0.40 (weak), ret=+5.2%
  - 2022: S=0.74 (moderate), ret=+9.6%
  - 2023: S=0.51 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 19.21% over 468 days (recovered)
- Annualized: return +6.2%, volatility 10.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.40, excess kurtosis +3.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.30, latest 0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.23%; worst month: -6.01%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.32
- Sideways: S=0.59
- Bear: S=0.94

## Negated Direction
Best negated: `-rank(systematic_risk_last_30_days)` S=0.06, F=0.01, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * systematic_risk_last_30_days)`: S=-0.04, F=-0.01, T=23.4%, INFERIOR (TOP3000)
- `rank(-1 * systematic_risk_last_30_days / close)`: S=0.00, F=0.00, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(systematic_risk_last_30_days, 5))`: S=-0.59, F=-0.15, T=52.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(systematic_risk_last_30_days, 5))` | TOP200 | 0.59 | 0.21 | 19.2% | 100% | mixed |
| `rank(ts_delta(systematic_risk_last_30_days, 5))` | TOP1000 | 0.59 | 0.17 | 10.0% | 80% | mixed |
| `rank(ts_delta(systematic_risk_last_30_days, 5))` | TOP3000 | 0.59 | 0.15 | 13.5% | 80% | mixed |
| `rank(ts_delta(systematic_risk_last_30_days, 5))` | TOP500 | 0.32 | 0.07 | 12.9% | 80% | mixed |

## Correlation Notes
Top correlates:
- systematic_risk_last_60_days: 0.497 (moderately positively correlated)
- systematic_risk_last_360_days: 0.370 (weakly positively correlated)
- implied_volatility_put_10: 0.327 (weakly positively correlated)
- implied_volatility_mean_10: 0.326 (weakly positively correlated)
- implied_volatility_call_10: 0.323 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
