---
field: anl4_qfd1_az_hgih_spfc
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1252
ann_vol: 0.0813
hit_rate: 0.4915
rolling_sharpe_min: -1.702
rolling_sharpe_max: 2.826
redundancy_cluster: 1
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.31
---
# anl4_qfd1_az_hgih_spfc (analyst4)

*Cash Flow - The highest estimation, per share*

## Signal Profile
- `rank(anl4_qfd1_az_hgih_spfc)`: S=0.31, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qfd1_az_hgih_spfc / close)`: S=0.72, F=0.49, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qfd1_az_hgih_spfc, 5))`: S=0.80, F=0.30, T=36.4%, INFERIOR (TOP3000)
- `-rank(anl4_qfd1_az_hgih_spfc)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_hgih_spfc, 5))`: S=-0.31, F=-0.12, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qfd1_az_hgih_spfc, 63)`: S=0.17, F=0.04, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_hgih_spfc, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_hgih_spfc, 22))`: S=0.03, F=0.00, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_spfc)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_spfc / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.72, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.55 (negative), ret=-3.4%
  - 2020: S=-0.02 (negative), ret=-0.2%
  - 2021: S=2.02 (strong), ret=+17.1%
  - 2022: S=1.70 (strong), ret=+14.2%
  - 2023: S=0.18 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 12.52% over 772 days (recovered)
- Annualized: return +5.9%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.42, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.70, max 2.83, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.09%; worst month: -4.97%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.49
- Sideways: S=-0.51
- Bear: S=-0.09

## Negated Direction
Best negated: `rank(-1 * anl4_qfd1_az_hgih_spfc / close)` S=0.41, F=0.25, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_hgih_spfc)`: S=0.34, F=0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_hgih_spfc / close)`: S=0.41, F=0.25, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_hgih_spfc, 5))`: S=-0.31, F=-0.12, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qfd1_az_hgih_spfc / close)` | TOP3000 | 0.72 | 0.49 | 12.5% | 60% | mixed |
| `rank(ts_delta(anl4_qfd1_az_hgih_spfc, 5))` | TOP3000 | 0.83 | 0.30 | 8.2% | 80% | mixed |
| `rank(anl4_qfd1_az_hgih_spfc / close)` | TOP1000 | 0.32 | 0.16 | 18.2% | 40% | bull-only |
| `rank(ts_delta(anl4_qfd1_az_hgih_spfc, 5))` | TOP200 | 0.37 | 0.15 | 34.9% | 80% | weak |
| `rank(anl4_qfd1_az_hgih_spfc)` | TOP3000 | 0.30 | 0.14 | 26.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_hgih_spfc: 1.000 (strongly positively correlated)
- anl4_qf_az_cfps_mean: 0.998 (strongly positively correlated)
- cashflow_per_share_average: 0.998 (strongly positively correlated)
- anl4_qf_az_cfps_median: 0.998 (strongly positively correlated)
- anl4_qfd1_az_cfps_median: 0.998 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
