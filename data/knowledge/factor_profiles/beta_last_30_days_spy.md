---
field: beta_last_30_days_spy
dataset: model51
best_template: rank_delta
best_sharpe: 0.46
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.1193
ann_vol: 0.0701
hit_rate: 0.5053
rolling_sharpe_min: -1.45
rolling_sharpe_max: 2.494
negated_best_sharpe: 0.14
negated_best_template: neg_rank
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.32
---
# beta_last_30_days_spy (model51)

*The rolling beta value of the security relative to SPY, calculated via regression over the last 30 calendar days, representing market sensitivity*

## Signal Profile
- `rank(beta_last_30_days_spy)`: S=-0.01, F=0.00, T=18.1%, INFERIOR (TOP3000)
- `rank(beta_last_30_days_spy / close)`: S=-0.02, F=0.00, T=15.2%, INFERIOR (TOP3000)
- `rank(ts_delta(beta_last_30_days_spy, 5))`: S=0.46, F=0.13, T=43.0%, INFERIOR (TOP3000)
- `-rank(beta_last_30_days_spy)`: S=0.14, F=0.05, T=19.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_30_days_spy, 5))`: S=-0.46, F=-0.13, T=43.0%, INFERIOR (TOP3000)
- `-ts_zscore(beta_last_30_days_spy, 63)`: S=0.36, F=0.13, T=23.3%, INFERIOR (TOP3000)
- `ts_mean(beta_last_30_days_spy, 10)`: S=-0.15, F=-0.08, T=8.8%, INFERIOR (TOP3000)
- `rank(ts_rank(beta_last_30_days_spy, 22))`: S=0.10, F=0.01, T=30.5%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_30_days_spy)`: S=0.01, F=0.00, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_30_days_spy / close)`: S=-0.02, F=0.00, T=14.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.19 (weak), ret=+0.7%
  - 2020: S=1.55 (strong), ret=+11.1%
  - 2021: S=0.40 (weak), ret=+3.0%
  - 2022: S=-0.07 (negative), ret=-0.7%
  - 2023: S=0.31 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 11.93% over 983 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.32, excess kurtosis +2.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 2.49, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.16%; worst month: -4.70%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.72
- Sideways: S=-1.22
- Bear: S=1.40

## Negated Direction
Best negated: `-rank(beta_last_30_days_spy)` S=0.14, F=0.05, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * beta_last_30_days_spy)`: S=0.01, F=0.00, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_30_days_spy / close)`: S=-0.02, F=0.00, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_30_days_spy, 5))`: S=-0.46, F=-0.13, T=43.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(beta_last_30_days_spy, 5))` | TOP3000 | 0.46 | 0.13 | 11.9% | 80% | all-weather |
| `rank(ts_delta(beta_last_30_days_spy, 5))` | TOP1000 | 0.43 | 0.12 | 15.9% | 100% | mixed |
| `rank(ts_delta(beta_last_30_days_spy, 5))` | TOP200 | 0.39 | 0.12 | 21.3% | 60% | mixed |
| `rank(ts_delta(beta_last_30_days_spy, 5))` | TOP500 | 0.26 | 0.06 | 16.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- correlation_last_30_days_spy: 0.853 (strongly positively correlated)
- historical_volatility_90: 0.488 (moderately positively correlated)
- historical_volatility_30: 0.416 (moderately positively correlated)
- parkinson_volatility_90: 0.395 (weakly positively correlated)
- historical_volatility_120: 0.358 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
