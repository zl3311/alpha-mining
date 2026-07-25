---
field: anl4_netprofit_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.5
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2746
ann_vol: 0.1
hit_rate: 0.5077
rolling_sharpe_min: -3.504
rolling_sharpe_max: 2.507
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.34
---
# anl4_netprofit_low (analyst4)

*Net Profit - The Lowest Estimation*

## Signal Profile
- `rank(anl4_netprofit_low)`: S=0.33, F=0.19, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_netprofit_low / close)`: S=0.50, F=0.32, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofit_low, 5))`: S=0.55, F=0.17, T=37.2%, INFERIOR (TOP500)
- `-rank(anl4_netprofit_low)`: S=-0.09, F=-0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_low, 5))`: S=0.16, F=0.03, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netprofit_low, 63)`: S=-0.01, F=0.00, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofit_low, 10)`: S=0.06, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofit_low, 22))`: S=-0.11, F=-0.02, T=14.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_low)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_low / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.50, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+1.8%
  - 2020: S=-2.60 (negative), ret=-16.1%
  - 2021: S=1.25 (moderate), ret=+15.1%
  - 2022: S=1.68 (strong), ret=+23.7%
  - 2023: S=-0.01 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 27.46% over 807 days (recovered)
- Annualized: return +5.0%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.04, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.50, max 2.51, latest -0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.70%; worst month: -5.51%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.19
- Sideways: S=0.97
- Bear: S=-3.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofit_low, 5))` S=0.16, F=0.03, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofit_low)`: S=0.08, F=0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofit_low / close)`: S=0.09, F=0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofit_low, 5))`: S=0.16, F=0.03, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofit_low / close)` | TOP3000 | 0.50 | 0.32 | 27.5% | 60% | bull-only |
| `rank(anl4_netprofit_low)` | TOP3000 | 0.33 | 0.19 | 39.5% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofit_low, 5))` | TOP500 | 0.55 | 0.17 | 10.2% | 60% | mixed |
| `rank(ts_delta(anl4_netprofit_low, 5))` | TOP1000 | 0.34 | 0.07 | 7.4% | 40% | mixed |
| `rank(anl4_netprofit_low / close)` | TOP1000 | 0.15 | 0.06 | 30.8% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofit_low, 5))` | TOP3000 | 0.21 | 0.03 | 6.1% | 40% | weak |
| `rank(anl4_netprofit_low)` | TOP1000 | 0.08 | 0.03 | 45.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptp_low: 0.996 (strongly positively correlated)
- anl4_netprofit_mean: 0.995 (strongly positively correlated)
- anl4_netprofit_median: 0.994 (strongly positively correlated)
- anl4_ptp_mean: 0.991 (strongly positively correlated)
- est_netprofit: 0.990 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
