---
field: beta_last_60_days_spy
dataset: model51
cluster: model51_risk_beta
coverage: 0.9752
community_alphas: 1673
best_template: ts_zscore
best_sharpe: 0.65
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1709
ann_vol: 0.1253
hit_rate: 0.5077
rolling_sharpe_min: -1.255
rolling_sharpe_max: 1.673
negated_best_sharpe: 0.14
negated_best_template: neg_rank
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.51
---
# beta_last_60_days_spy (model51)

*The rolling beta value of the security relative to SPY, calculated via regression over the last 60 calendar days, representing market sensitivity*

## Signal Profile
- `rank(beta_last_60_days_spy)`: S=0.00, F=0.00, T=14.1%, INFERIOR (TOP3000)
- `rank(beta_last_60_days_spy / close)`: S=-0.05, F=-0.01, T=12.5%, INFERIOR (TOP3000)
- `rank(ts_delta(beta_last_60_days_spy, 5))`: S=0.20, F=0.05, T=45.2%, INFERIOR (TOP200)
- `-rank(beta_last_60_days_spy)`: S=0.14, F=0.06, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_60_days_spy, 5))`: S=0.06, F=0.01, T=42.6%, INFERIOR (TOP3000)
- `-ts_zscore(beta_last_60_days_spy, 63)`: S=0.65, F=0.33, T=20.3%, INFERIOR (TOP3000)
- `ts_mean(beta_last_60_days_spy, 10)`: S=-0.02, F=0.00, T=5.8%, INFERIOR (TOP3000)
- `rank(ts_rank(beta_last_60_days_spy, 22))`: S=-0.68, F=-0.28, T=29.3%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_60_days_spy)`: S=0.00, F=0.00, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_60_days_spy / close)`: S=0.01, F=0.00, T=11.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/0P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 23F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.20, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.04 (negative), ret=-0.3%
  - 2020: S=0.61 (moderate), ret=+7.2%
  - 2021: S=-0.06 (negative), ret=-1.0%
  - 2022: S=0.76 (moderate), ret=+11.5%
  - 2023: S=-0.61 (negative), ret=-4.8%

## Risk & Drawdown
- Max drawdown: 17.09% over 539 days (recovered)
- Annualized: return +2.6%, volatility 12.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.78, excess kurtosis +6.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 1.67, latest -0.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +9.37%; worst month: -5.56%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.47
- Sideways: S=-0.85
- Bear: S=0.69

## Negated Direction
Best negated: `-rank(beta_last_60_days_spy)` S=0.14, F=0.06, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * beta_last_60_days_spy)`: S=0.00, F=0.00, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_60_days_spy / close)`: S=0.01, F=0.00, T=11.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_60_days_spy, 5))`: S=0.06, F=0.01, T=42.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(beta_last_60_days_spy, 5))` | TOP200 | 0.20 | 0.05 | 17.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- correlation_last_60_days_spy: 0.794 (strongly positively correlated)
- systematic_risk_last_60_days: 0.622 (moderately positively correlated)
- beta_last_360_days_spy: 0.462 (moderately positively correlated)
- unsystematic_risk_last_60_days: -0.405 (moderately negatively correlated)
- historical_volatility_120: 0.379 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
