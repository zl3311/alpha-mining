---
field: net_profit_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.31
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3922
ann_vol: 0.1139
hit_rate: 0.5061
rolling_sharpe_min: -4.638
rolling_sharpe_max: 2.649
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: 0.07
---
# net_profit_reported_value (analyst4)

*Net profit- announced financial value*

## Signal Profile
- `rank(net_profit_reported_value)`: S=0.25, F=0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(net_profit_reported_value / close)`: S=0.31, F=0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(net_profit_reported_value, 5))`: S=-0.06, F=-0.01, T=36.4%, INFERIOR (TOP200)
- `-rank(net_profit_reported_value)`: S=-0.06, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_reported_value, 5))`: S=0.38, F=0.08, T=35.7%, INFERIOR (TOP3000)
- `ts_zscore(net_profit_reported_value, 22)`: S=-0.07, F=-0.01, T=38.1%, INFERIOR (TOP3000)
- `ts_mean(net_profit_reported_value, 10)`: S=0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(net_profit_reported_value, 22))`: S=0.19, F=0.04, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_reported_value)`: S=-0.25, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_reported_value / close)`: S=-0.31, F=-0.16, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.08 (weak), ret=+0.4%
  - 2020: S=-3.79 (negative), ret=-26.2%
  - 2021: S=1.35 (moderate), ret=+17.5%
  - 2022: S=1.70 (strong), ret=+28.0%
  - 2023: S=-0.26 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 39.22% over 801 days (recovered)
- Annualized: return +3.4%, volatility 11.4% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.13, excess kurtosis +1.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.64, max 2.65, latest -0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.85%; worst month: -9.76%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=0.79
- Bear: S=-3.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_profit_reported_value, 5))` S=0.38, F=0.08, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * net_profit_reported_value)`: S=-0.25, F=-0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * net_profit_reported_value / close)`: S=-0.31, F=-0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_profit_reported_value, 5))`: S=0.38, F=0.08, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_profit_reported_value / close)` | TOP3000 | 0.30 | 0.16 | 39.2% | 60% | bull-only |
| `rank(net_profit_reported_value)` | TOP3000 | 0.24 | 0.13 | 45.1% | 60% | bull-only |
| `rank(net_profit_reported_value / close)` | TOP1000 | 0.15 | 0.06 | 37.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netprofit_value: 1.000 (strongly positively correlated)
- pretax_income_standalone_value: 0.994 (strongly positively correlated)
- anl4_ptp_value: 0.994 (strongly positively correlated)
- fnd6_mfmq_piq: 0.987 (strongly positively correlated)
- fnd6_newqv1300_piq: 0.987 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
