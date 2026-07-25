---
field: correlation_last_30_days_spy
dataset: model51
best_template: ts_zscore
best_sharpe: 0.64
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1125
ann_vol: 0.0509
hit_rate: 0.4964
rolling_sharpe_min: -1.521
rolling_sharpe_max: 2.411
negated_best_sharpe: 0.54
negated_best_template: neg_rank
negated_best_fitness: 0.25
n_negated_sims: 4
direction_gap: -0.1
---
# correlation_last_30_days_spy (model51)

*The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recent 30 calendar days*

## Signal Profile
- `rank(correlation_last_30_days_spy)`: S=-0.03, F=0.00, T=18.9%, INFERIOR (TOP3000)
- `rank(ts_delta(correlation_last_30_days_spy, 5))`: S=0.30, F=0.06, T=43.1%, INFERIOR (TOP3000)
- `-rank(correlation_last_30_days_spy)`: S=0.54, F=0.25, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_30_days_spy, 5))`: S=-0.30, F=-0.06, T=43.1%, INFERIOR (TOP3000)
- `-ts_zscore(correlation_last_30_days_spy, 63)`: S=0.64, F=0.28, T=23.8%, INFERIOR (TOP3000)
- `ts_mean(correlation_last_30_days_spy, 10)`: S=-0.52, F=-0.31, T=9.3%, INFERIOR (TOP3000)
- `rank(ts_rank(correlation_last_30_days_spy, 22))`: S=-0.16, F=-0.03, T=31.6%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_30_days_spy)`: S=0.03, F=0.00, T=18.9%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_30_days_spy / close)`: S=-0.04, F=-0.01, T=14.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+1.8%
  - 2020: S=1.21 (moderate), ret=+6.0%
  - 2021: S=0.68 (moderate), ret=+4.1%
  - 2022: S=-0.79 (negative), ret=-4.9%
  - 2023: S=0.15 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 11.25% over 983 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 5.1% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.26, excess kurtosis +2.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 2.41, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.24%; worst month: -3.82%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.16
- Sideways: S=-0.73
- Bear: S=1.58

## Negated Direction
Best negated: `-rank(correlation_last_30_days_spy)` S=0.54, F=0.25, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * correlation_last_30_days_spy)`: S=0.03, F=0.00, T=18.9%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_30_days_spy / close)`: S=-0.04, F=-0.01, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_30_days_spy, 5))`: S=-0.30, F=-0.06, T=43.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(correlation_last_30_days_spy, 5))` | TOP3000 | 0.31 | 0.06 | 11.2% | 80% | mixed |
| `rank(ts_delta(correlation_last_30_days_spy, 5))` | TOP1000 | 0.18 | 0.03 | 12.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- beta_last_30_days_spy: 0.853 (strongly positively correlated)
- unsystematic_risk_last_60_days: -0.346 (weakly negatively correlated)
- unsystematic_risk_last_90_days: -0.326 (weakly negatively correlated)
- systematic_risk_last_30_days: 0.304 (weakly positively correlated)
- beta_last_60_days_spy: 0.262 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
