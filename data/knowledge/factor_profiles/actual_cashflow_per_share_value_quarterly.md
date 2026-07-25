---
field: actual_cashflow_per_share_value_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.49
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2049
ann_vol: 0.1027
hit_rate: 0.5012
rolling_sharpe_min: -1.965
rolling_sharpe_max: 2.849
negated_best_sharpe: 0.25
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.24
---
# actual_cashflow_per_share_value_quarterly (analyst4)

*Cash Flow Per Share - actual value for the quarter*

## Signal Profile
- `rank(actual_cashflow_per_share_value_quarterly)`: S=0.29, F=0.15, T=3.7%, INFERIOR (TOP3000)
- `rank(actual_cashflow_per_share_value_quarterly / close)`: S=0.49, F=0.31, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_delta(actual_cashflow_per_share_value_quarterly, 5))`: S=0.25, F=0.04, T=39.1%, INFERIOR (TOP1000)
- `-rank(actual_cashflow_per_share_value_quarterly)`: S=-0.15, F=-0.05, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_cashflow_per_share_value_quarterly, 5))`: S=0.11, F=0.01, T=39.1%, INFERIOR (TOP3000)
- `ts_zscore(actual_cashflow_per_share_value_quarterly, 22)`: S=0.31, F=0.07, T=39.5%, INFERIOR (TOP3000)
- `ts_mean(actual_cashflow_per_share_value_quarterly, 10)`: S=-0.14, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(actual_cashflow_per_share_value_quarterly, 22))`: S=0.20, F=0.04, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * actual_cashflow_per_share_value_quarterly)`: S=0.18, F=0.07, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * actual_cashflow_per_share_value_quarterly / close)`: S=0.25, F=0.12, T=4.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.47, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.29 (negative), ret=-7.8%
  - 2020: S=-1.26 (negative), ret=-10.0%
  - 2021: S=1.58 (strong), ret=+16.6%
  - 2022: S=1.85 (strong), ret=+28.2%
  - 2023: S=-0.40 (negative), ret=-3.3%

## Risk & Drawdown
- Max drawdown: 20.49% over 1090 days (recovered)
- Annualized: return +4.8%, volatility 10.3% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.01, excess kurtosis +1.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.97, max 2.85, latest -0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.11%; worst month: -4.88%
Positive months: 44%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.04
- Sideways: S=-0.05
- Bear: S=-2.23

## Negated Direction
Best negated: `rank(-1 * actual_cashflow_per_share_value_quarterly / close)` S=0.25, F=0.12, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * actual_cashflow_per_share_value_quarterly)`: S=0.18, F=0.07, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * actual_cashflow_per_share_value_quarterly / close)`: S=0.25, F=0.12, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_cashflow_per_share_value_quarterly, 5))`: S=0.11, F=0.01, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actual_cashflow_per_share_value_quarterly / close)` | TOP3000 | 0.47 | 0.31 | 20.5% | 40% | bull-only |
| `rank(actual_cashflow_per_share_value_quarterly)` | TOP3000 | 0.28 | 0.15 | 33.1% | 40% | bull-only |
| `rank(actual_cashflow_per_share_value_quarterly / close)` | TOP1000 | 0.19 | 0.09 | 19.7% | 40% | bull-only |
| `rank(actual_cashflow_per_share_value_quarterly)` | TOP1000 | 0.14 | 0.05 | 26.5% | 60% | bull-only |
| `rank(ts_delta(actual_cashflow_per_share_value_quarterly, 5))` | TOP1000 | 0.24 | 0.04 | 8.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- est_epsr: 0.892 (strongly positively correlated)
- anl4_epsr_mean: 0.890 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.890 (strongly positively correlated)
- anl4_qf_az_wol_spe: 0.890 (strongly positively correlated)
- anl4_median_epsreported: 0.889 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
