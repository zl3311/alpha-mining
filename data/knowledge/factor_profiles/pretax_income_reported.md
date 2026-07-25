---
field: pretax_income_reported
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.68
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.3226
ann_vol: 0.1171
hit_rate: 0.5045
rolling_sharpe_min: -4.255
rolling_sharpe_max: 1.886
negated_best_sharpe: 0.23
negated_best_template: neg_rank
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.45
---
# pretax_income_reported (analyst4)

*Reported Pretax income - actual value for the annual fiscal period*

## Signal Profile
- `rank(pretax_income_reported)`: S=-0.06, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(pretax_income_reported / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_reported, 5))`: S=-0.13, F=-0.02, T=34.7%, INFERIOR (TOP200)
- `-rank(pretax_income_reported)`: S=0.23, F=0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported, 5))`: S=0.46, F=0.11, T=36.8%, INFERIOR (TOP3000)
- `-ts_zscore(pretax_income_reported, 63)`: S=0.68, F=0.31, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_reported, 10)`: S=-0.16, F=-0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_reported, 22))`: S=-0.22, F=-0.06, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported)`: S=0.06, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported / close)`: S=-0.12, F=-0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.11, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.9%
  - 2020: S=-3.58 (negative), ret=-23.1%
  - 2021: S=0.72 (moderate), ret=+8.6%
  - 2022: S=1.23 (moderate), ret=+21.8%
  - 2023: S=-0.17 (negative), ret=-2.0%

## Risk & Drawdown
- Max drawdown: 32.26% over 929 days (recovered)
- Annualized: return +1.3%, volatility 11.7% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.10, excess kurtosis +1.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.25, max 1.89, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.59%; worst month: -5.89%
Positive months: 44%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.64
- Sideways: S=0.56
- Bear: S=-3.81

## Negated Direction
Best negated: `-rank(pretax_income_reported)` S=0.23, F=0.11, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pretax_income_reported)`: S=0.06, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported / close)`: S=-0.12, F=-0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported, 5))`: S=0.46, F=0.11, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pretax_income_reported / close)` | TOP3000 | 0.11 | 0.04 | 32.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_total: 0.967 (strongly positively correlated)
- net_income_total_2: 0.963 (strongly positively correlated)
- fnd6_ci: 0.959 (strongly positively correlated)
- free_cash_flow_total: 0.959 (strongly positively correlated)
- net_income_adjusted: 0.956 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
