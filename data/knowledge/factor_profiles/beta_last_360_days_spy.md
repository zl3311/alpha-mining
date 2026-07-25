---
field: beta_last_360_days_spy
dataset: model51
best_template: rank_delta
best_sharpe: 0.75
best_fitness: 0.33
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1269
ann_vol: 0.1181
hit_rate: 0.4988
rolling_sharpe_min: -1.301
rolling_sharpe_max: 2.166
negated_best_sharpe: 0.05
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.7
---
# beta_last_360_days_spy (model51)

*The rolling beta value of the security relative to SPY, calculated via regression over the last 360 calendar days, representing market sensitivity*

## Signal Profile
- `rank(beta_last_360_days_spy)`: S=0.16, F=0.08, T=10.0%, INFERIOR (TOP3000)
- `rank(beta_last_360_days_spy / close)`: S=0.06, F=0.02, T=10.6%, INFERIOR (TOP3000)
- `rank(ts_delta(beta_last_360_days_spy, 5))`: S=0.75, F=0.33, T=47.1%, INFERIOR (TOP200)
- `-rank(beta_last_360_days_spy)`: S=-0.03, F=-0.01, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_360_days_spy, 5))`: S=0.05, F=0.00, T=43.6%, INFERIOR (TOP3000)
- `-ts_zscore(beta_last_360_days_spy, 63)`: S=0.30, F=0.11, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(beta_last_360_days_spy, 10)`: S=0.17, F=0.09, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(beta_last_360_days_spy, 22))`: S=-0.37, F=-0.12, T=28.6%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_360_days_spy)`: S=-0.16, F=-0.08, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_360_days_spy / close)`: S=-0.06, F=-0.02, T=9.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.10 (strong), ret=+12.3%
  - 2020: S=-0.21 (negative), ret=-2.5%
  - 2021: S=1.79 (strong), ret=+24.5%
  - 2022: S=0.44 (weak), ret=+6.9%
  - 2023: S=0.29 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 12.69% over 415 days (not yet recovered, ongoing at window end)
- Annualized: return +8.8%, volatility 11.8% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.99, excess kurtosis +7.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 2.17, latest 0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +10.47%; worst month: -7.64%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.30
- Sideways: S=0.64
- Bear: S=1.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(beta_last_360_days_spy, 5))` S=0.05, F=0.00, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * beta_last_360_days_spy)`: S=-0.16, F=-0.08, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * beta_last_360_days_spy / close)`: S=-0.06, F=-0.02, T=9.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(beta_last_360_days_spy, 5))`: S=0.05, F=0.00, T=43.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(beta_last_360_days_spy, 5))` | TOP200 | 0.75 | 0.33 | 12.7% | 80% | mixed |
| `rank(ts_delta(beta_last_360_days_spy, 5))` | TOP500 | 0.35 | 0.09 | 18.0% | 80% | mixed |
| `rank(beta_last_360_days_spy)` | TOP3000 | 0.17 | 0.08 | 41.1% | 60% | bear-only |
| `rank(beta_last_360_days_spy)` | TOP500 | 0.18 | 0.08 | 41.5% | 80% | bear-only |

## Correlation Notes
Top correlates:
- beta_last_60_days_spy: 0.462 (moderately positively correlated)
- systematic_risk_last_360_days: 0.415 (moderately positively correlated)
- historical_volatility_120: 0.409 (moderately positively correlated)
- parkinson_volatility_120: 0.361 (weakly positively correlated)
- correlation_last_60_days_spy: 0.351 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
