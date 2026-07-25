---
field: actual_eps_value_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.55
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.337
ann_vol: 0.1153
hit_rate: 0.4964
rolling_sharpe_min: -4.054
rolling_sharpe_max: 3.15
redundancy_cluster: 13
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.08
---
# actual_eps_value_quarterly (analyst4)

*Earnings Per Share (Income Statement/Per Share) (Actual)*

## Signal Profile
- `rank(actual_eps_value_quarterly)`: S=0.32, F=0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(actual_eps_value_quarterly / close)`: S=0.55, F=0.39, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(actual_eps_value_quarterly, 5))`: S=-0.16, F=-0.03, T=36.5%, INFERIOR (TOP200)
- `-rank(actual_eps_value_quarterly)`: S=-0.17, F=-0.07, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_eps_value_quarterly, 5))`: S=0.47, F=0.12, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(actual_eps_value_quarterly, 22)`: S=-0.13, F=-0.02, T=38.3%, INFERIOR (TOP3000)
- `ts_mean(actual_eps_value_quarterly, 10)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(actual_eps_value_quarterly, 22))`: S=0.05, F=0.01, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * actual_eps_value_quarterly)`: S=0.01, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * actual_eps_value_quarterly / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.11 (weak), ret=+0.4%
  - 2020: S=-3.52 (negative), ret=-23.5%
  - 2021: S=1.96 (strong), ret=+26.2%
  - 2022: S=1.77 (strong), ret=+30.9%
  - 2023: S=-0.37 (negative), ret=-3.6%

## Risk & Drawdown
- Max drawdown: 33.70% over 778 days (recovered)
- Annualized: return +6.2%, volatility 11.5% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew -0.06, excess kurtosis +2.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.05, max 3.15, latest -0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +10.92%; worst month: -8.06%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.51
- Bear: S=-3.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(actual_eps_value_quarterly, 5))` S=0.47, F=0.12, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * actual_eps_value_quarterly)`: S=0.01, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * actual_eps_value_quarterly / close)`: S=-0.01, F=0.00, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(actual_eps_value_quarterly, 5))`: S=0.47, F=0.12, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(actual_eps_value_quarterly / close)` | TOP3000 | 0.54 | 0.39 | 33.7% | 60% | bull-only |
| `rank(actual_eps_value_quarterly)` | TOP3000 | 0.32 | 0.19 | 45.0% | 60% | bull-only |
| `rank(actual_eps_value_quarterly / close)` | TOP1000 | 0.27 | 0.15 | 35.9% | 60% | bull-only |
| `rank(actual_eps_value_quarterly)` | TOP1000 | 0.17 | 0.07 | 43.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_nongaap_value: 0.976 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 0.971 (strongly positively correlated)
- fnd6_cptmfmq_opepsq: 0.971 (strongly positively correlated)
- fnd6_cptnewqv1300_opepsq: 0.971 (strongly positively correlated)
- fnd6_newqv1300_oepf12: 0.963 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
