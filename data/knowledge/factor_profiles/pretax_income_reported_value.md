---
field: pretax_income_reported_value
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.43
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.4008
ann_vol: 0.1252
hit_rate: 0.5077
rolling_sharpe_min: -4.189
rolling_sharpe_max: 2.345
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.17
---
# pretax_income_reported_value (analyst4)

*Reported Pretax income - actual value for the quarter*

## Signal Profile
- `rank(pretax_income_reported_value)`: S=0.10, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(pretax_income_reported_value / close)`: S=0.13, F=0.05, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_reported_value, 5))`: S=0.17, F=0.03, T=39.3%, INFERIOR (TOP1000)
- `-rank(pretax_income_reported_value)`: S=0.03, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported_value, 5))`: S=0.31, F=0.09, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(pretax_income_reported_value, 22)`: S=0.23, F=0.05, T=39.6%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_reported_value, 10)`: S=0.00, F=0.00, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_reported_value, 22))`: S=0.60, F=0.24, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_value)`: S=0.43, F=0.29, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_value / close)`: S=0.40, F=0.26, T=4.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.11, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.42 (negative), ret=-2.4%
  - 2020: S=-3.25 (negative), ret=-24.9%
  - 2021: S=0.82 (moderate), ret=+10.3%
  - 2022: S=1.44 (moderate), ret=+26.8%
  - 2023: S=-0.22 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 40.08% over 948 days (recovered)
- Annualized: return +1.4%, volatility 12.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.17, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.19, max 2.35, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.43%; worst month: -8.62%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=0.52
- Bear: S=-3.47

## Negated Direction
Best negated: `rank(-1 * pretax_income_reported_value)` S=0.43, F=0.29, INFERIOR
Direction gap: -0.17 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pretax_income_reported_value)`: S=0.43, F=0.29, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_reported_value / close)`: S=0.40, F=0.26, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_reported_value, 5))`: S=0.31, F=0.09, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pretax_income_reported_value / close)` | TOP3000 | 0.11 | 0.05 | 40.1% | 40% | bull-only |
| `rank(ts_delta(pretax_income_reported_value, 5))` | TOP1000 | 0.16 | 0.03 | 13.6% | 40% | bull-only |
| `rank(pretax_income_reported_value)` | TOP3000 | 0.09 | 0.03 | 44.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_actual_reported_value: 1.000 (strongly positively correlated)
- fnd6_newqv1300_ibmiiq: 0.953 (strongly positively correlated)
- anl4_ptp_value: 0.953 (strongly positively correlated)
- pretax_income_standalone_value: 0.953 (strongly positively correlated)
- fnd6_newqv1300_piq: 0.952 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
