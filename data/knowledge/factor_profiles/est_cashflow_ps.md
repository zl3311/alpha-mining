---
field: est_cashflow_ps
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1081
ann_vol: 0.0623
hit_rate: 0.5126
rolling_sharpe_min: -1.046
rolling_sharpe_max: 3.054
redundancy_cluster: 9
negated_best_sharpe: 0.4
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.38
---
# est_cashflow_ps (analyst4)

*Cash Flow Per Share - average of estimations*

## Signal Profile
- `rank(est_cashflow_ps)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(est_cashflow_ps / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(est_cashflow_ps, 5))`: S=0.71, F=0.25, T=36.2%, INFERIOR (TOP3000)
- `-rank(est_cashflow_ps)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_ps, 5))`: S=-0.38, F=-0.16, T=34.9%, INFERIOR (TOP3000)
- `-ts_zscore(est_cashflow_ps, 63)`: S=0.16, F=0.04, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(est_cashflow_ps, 10)`: S=-0.07, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(est_cashflow_ps, 22))`: S=0.12, F=0.03, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_ps)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_ps / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+5.4%
  - 2020: S=0.94 (moderate), ret=+6.3%
  - 2021: S=0.22 (weak), ret=+1.5%
  - 2022: S=-0.45 (negative), ret=-2.7%
  - 2023: S=2.30 (strong), ret=+11.9%

## Risk & Drawdown
- Max drawdown: 10.81% over 474 days (recovered)
- Annualized: return +4.6%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.12, excess kurtosis +1.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 3.05, latest 2.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +4.59%; worst month: -3.97%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.60
- Sideways: S=1.23
- Bear: S=0.38

## Negated Direction
Best negated: `rank(-1 * est_cashflow_ps / close)` S=0.40, F=0.25, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_cashflow_ps)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_ps / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_ps, 5))`: S=-0.38, F=-0.16, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(est_cashflow_ps, 5))` | TOP3000 | 0.74 | 0.25 | 10.8% | 80% | mixed |
| `rank(ts_delta(est_cashflow_ps, 5))` | TOP200 | 0.43 | 0.18 | 28.7% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_qfv4_cfps_high: 0.809 (strongly positively correlated)
- anl4_qf_az_wol_spfc: 0.807 (strongly positively correlated)
- anl4_qfd1_az_wol_spfc: 0.807 (strongly positively correlated)
- cashflow_per_share_median_value: 0.720 (strongly positively correlated)
- cashflow_per_share_maximum: 0.621 (moderately positively correlated)

Redundancy cluster #9: 4 similar fields, mean |rho| 0.783 (representative: anl4_qfd1_az_wol_spfc). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
