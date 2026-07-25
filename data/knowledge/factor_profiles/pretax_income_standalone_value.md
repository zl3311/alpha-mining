---
field: pretax_income_standalone_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.32
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.4132
ann_vol: 0.1213
hit_rate: 0.5069
rolling_sharpe_min: -4.756
rolling_sharpe_max: 2.634
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: 0.17
---
# pretax_income_standalone_value (analyst4)

*Pretax Profit - actual value for the quarter*

## Signal Profile
- `rank(pretax_income_standalone_value)`: S=0.23, F=0.11, T=2.0%, INFERIOR (TOP3000)
- `rank(pretax_income_standalone_value / close)`: S=0.32, F=0.18, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_standalone_value, 5))`: S=0.10, F=0.01, T=37.1%, INFERIOR (TOP200)
- `-rank(pretax_income_standalone_value)`: S=-0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_standalone_value, 5))`: S=0.49, F=0.11, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(pretax_income_standalone_value, 22)`: S=0.11, F=0.02, T=37.9%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_standalone_value, 10)`: S=-0.14, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_standalone_value, 22))`: S=0.37, F=0.12, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_standalone_value)`: S=-0.23, F=-0.11, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_standalone_value / close)`: S=-0.32, F=-0.18, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.32, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.08 (weak), ret=+0.4%
  - 2020: S=-3.88 (negative), ret=-27.8%
  - 2021: S=1.31 (moderate), ret=+17.8%
  - 2022: S=1.70 (strong), ret=+30.2%
  - 2023: S=-0.16 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 41.32% over 801 days (recovered)
- Annualized: return +3.8%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew -0.14, excess kurtosis +1.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.76, max 2.63, latest -0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.57%; worst month: -9.10%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.98
- Sideways: S=0.76
- Bear: S=-3.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(pretax_income_standalone_value, 5))` S=0.49, F=0.11, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * pretax_income_standalone_value)`: S=-0.23, F=-0.11, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_standalone_value / close)`: S=-0.32, F=-0.18, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_standalone_value, 5))`: S=0.49, F=0.11, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pretax_income_standalone_value / close)` | TOP3000 | 0.32 | 0.18 | 41.3% | 60% | bull-only |
| `rank(pretax_income_standalone_value)` | TOP3000 | 0.22 | 0.11 | 47.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptp_value: 1.000 (strongly positively correlated)
- net_profit_reported_value: 0.994 (strongly positively correlated)
- anl4_netprofit_value: 0.994 (strongly positively correlated)
- net_profit_adjusted_value: 0.987 (strongly positively correlated)
- anl4_netprofita_value: 0.987 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
