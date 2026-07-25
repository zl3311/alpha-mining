---
field: correlation_last_60_days_spy
dataset: model51
best_template: ts_zscore
best_sharpe: 0.72
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1757
ann_vol: 0.0963
hit_rate: 0.4955
rolling_sharpe_min: -1.044
rolling_sharpe_max: 1.519
negated_best_sharpe: 0.23
negated_best_template: neg_rank
negated_best_fitness: 0.08
n_negated_sims: 4
direction_gap: -0.49
---
# correlation_last_60_days_spy (model51)

*The Pearson correlation coefficient of daily log returns between the security and SPY, calculated over the most recent 60 calendar days*

## Signal Profile
- `rank(correlation_last_60_days_spy)`: S=0.07, F=0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(ts_delta(correlation_last_60_days_spy, 5))`: S=0.22, F=0.05, T=45.3%, INFERIOR (TOP200)
- `-rank(correlation_last_60_days_spy)`: S=0.23, F=0.08, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_60_days_spy, 5))`: S=0.03, F=0.00, T=42.6%, INFERIOR (TOP3000)
- `-ts_zscore(correlation_last_60_days_spy, 63)`: S=0.72, F=0.36, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(correlation_last_60_days_spy, 10)`: S=-0.19, F=-0.07, T=6.2%, INFERIOR (TOP3000)
- `rank(ts_rank(correlation_last_60_days_spy, 22))`: S=-0.68, F=-0.26, T=30.4%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_60_days_spy)`: S=-0.07, F=-0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_60_days_spy / close)`: S=0.01, F=0.00, T=11.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.22, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.50 (weak), ret=+3.1%
  - 2020: S=0.43 (weak), ret=+4.1%
  - 2021: S=-0.30 (negative), ret=-3.9%
  - 2022: S=0.08 (weak), ret=+0.8%
  - 2023: S=0.99 (moderate), ret=+6.4%

## Risk & Drawdown
- Max drawdown: 17.57% over 1214 days (not yet recovered, ongoing at window end)
- Annualized: return +2.1%, volatility 9.6% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.37, excess kurtosis +5.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 1.52, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +6.32%; worst month: -4.27%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.15
- Sideways: S=-0.25
- Bear: S=1.02

## Negated Direction
Best negated: `-rank(correlation_last_60_days_spy)` S=0.23, F=0.08, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * correlation_last_60_days_spy)`: S=-0.07, F=-0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * correlation_last_60_days_spy / close)`: S=0.01, F=0.00, T=11.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(correlation_last_60_days_spy, 5))`: S=0.03, F=0.00, T=42.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(correlation_last_60_days_spy, 5))` | TOP200 | 0.22 | 0.05 | 17.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- beta_last_60_days_spy: 0.794 (strongly positively correlated)
- systematic_risk_last_60_days: 0.740 (strongly positively correlated)
- unsystematic_risk_last_60_days: -0.417 (moderately negatively correlated)
- beta_last_360_days_spy: 0.351 (weakly positively correlated)
- systematic_risk_last_30_days: 0.309 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
