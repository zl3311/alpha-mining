---
field: net_profit_adjusted_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.38
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3388
ann_vol: 0.1084
hit_rate: 0.5101
rolling_sharpe_min: -4.404
rolling_sharpe_max: 2.725
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.29
---
# net_profit_adjusted_value (analyst4)

*Adjusted net income- announced financial value*

## Signal Profile
- `rank(net_profit_adjusted_value)`: S=0.21, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(net_profit_adjusted_value / close)`: S=0.38, F=0.22, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(net_profit_adjusted_value, 5))`: S=-0.30, F=-0.06, T=36.9%, INFERIOR (TOP1000)
- `-rank(net_profit_adjusted_value)`: S=-0.07, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_adjusted_value, 5))`: S=0.67, F=0.17, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(net_profit_adjusted_value, 63)`: S=-0.25, F=-0.06, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(net_profit_adjusted_value, 10)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(net_profit_adjusted_value, 22))`: S=-0.08, F=-0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_value)`: S=-0.21, F=-0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_value / close)`: S=-0.38, F=-0.22, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+2.1%
  - 2020: S=-3.46 (negative), ret=-21.7%
  - 2021: S=1.31 (moderate), ret=+16.5%
  - 2022: S=1.73 (strong), ret=+27.4%
  - 2023: S=-0.42 (negative), ret=-4.1%

## Risk & Drawdown
- Max drawdown: 33.88% over 792 days (recovered)
- Annualized: return +4.1%, volatility 10.8% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew -0.10, excess kurtosis +1.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.40, max 2.73, latest -0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.15%; worst month: -7.72%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.87
- Bear: S=-3.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_profit_adjusted_value, 5))` S=0.67, F=0.17, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * net_profit_adjusted_value)`: S=-0.21, F=-0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_adjusted_value / close)`: S=-0.38, F=-0.22, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_adjusted_value, 5))`: S=0.67, F=0.17, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_profit_adjusted_value / close)` | TOP3000 | 0.38 | 0.22 | 33.9% | 60% | bull-only |
| `rank(net_profit_adjusted_value)` | TOP3000 | 0.20 | 0.10 | 44.4% | 60% | bull-only |
| `rank(net_profit_adjusted_value / close)` | TOP1000 | 0.22 | 0.10 | 35.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofita_value: 1.000 (strongly positively correlated)
- pretax_income_standalone_value: 0.987 (strongly positively correlated)
- anl4_ptp_value: 0.987 (strongly positively correlated)
- net_profit_reported_value: 0.987 (strongly positively correlated)
- anl4_netprofit_value: 0.987 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
