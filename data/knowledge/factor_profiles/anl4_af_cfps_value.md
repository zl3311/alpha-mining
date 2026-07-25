---
field: anl4_af_cfps_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1545
ann_vol: 0.1122
hit_rate: 0.4899
rolling_sharpe_min: -1.257
rolling_sharpe_max: 2.669
redundancy_cluster: 13
negated_best_sharpe: 0.82
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: 0.25
---
# anl4_af_cfps_value (analyst4)

*Cash Flow Per Share - Actual Value*

## Signal Profile
- `rank(anl4_af_cfps_value)`: S=0.16, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(anl4_af_cfps_value / close)`: S=0.57, F=0.41, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_af_cfps_value, 5))`: S=-0.26, F=-0.08, T=36.9%, INFERIOR (TOP500)
- `-rank(anl4_af_cfps_value)`: S=-0.09, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_cfps_value, 5))`: S=0.82, F=0.36, T=38.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_af_cfps_value, 22)`: S=-0.08, F=-0.02, T=31.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_af_cfps_value, 10)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_af_cfps_value, 22))`: S=-0.72, F=-0.39, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_cfps_value)`: S=-0.16, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_cfps_value / close)`: S=-0.57, F=-0.41, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.37 (negative), ret=-2.2%
  - 2020: S=-0.56 (negative), ret=-6.7%
  - 2021: S=1.45 (moderate), ret=+15.4%
  - 2022: S=1.71 (strong), ret=+26.1%
  - 2023: S=-0.23 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 15.45% over 226 days (recovered)
- Annualized: return +6.3%, volatility 11.2% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.25, excess kurtosis +2.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.67, latest -0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.33%; worst month: -5.28%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.33
- Sideways: S=-0.16
- Bear: S=-2.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_af_cfps_value, 5))` S=0.82, F=0.36, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_af_cfps_value)`: S=-0.16, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_af_cfps_value / close)`: S=-0.57, F=-0.41, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_af_cfps_value, 5))`: S=0.82, F=0.36, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_af_cfps_value / close)` | TOP3000 | 0.56 | 0.41 | 15.4% | 40% | bull-only |
| `rank(anl4_af_cfps_value / close)` | TOP1000 | 0.23 | 0.13 | 18.1% | 60% | bull-only |
| `rank(anl4_af_cfps_value)` | TOP3000 | 0.14 | 0.06 | 36.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_af_eps_value: 0.917 (strongly positively correlated)
- earnings_per_share_average: 0.911 (strongly positively correlated)
- anl4_qf_az_eps_mean: 0.911 (strongly positively correlated)
- anl4_qfd1_azeps: 0.911 (strongly positively correlated)
- anl4_qf_az_eps: 0.911 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
