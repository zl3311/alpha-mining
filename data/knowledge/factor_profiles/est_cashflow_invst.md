---
field: est_cashflow_invst
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.68
best_fitness: 0.33
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1379
ann_vol: 0.1202
hit_rate: 0.5117
rolling_sharpe_min: -1.161
rolling_sharpe_max: 2.183
negated_best_sharpe: 0.28
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.4
---
# est_cashflow_invst (analyst4)

*Cash Flow From Investing - mean of estimations*

## Signal Profile
- `rank(est_cashflow_invst)`: S=0.25, F=0.12, T=2.4%, INFERIOR (TOP200)
- `rank(est_cashflow_invst / close)`: S=0.17, F=0.06, T=2.3%, INFERIOR (TOP200)
- `rank(ts_delta(est_cashflow_invst, 5))`: S=0.68, F=0.33, T=34.1%, INFERIOR (TOP200)
- `-rank(est_cashflow_invst)`: S=0.22, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_invst, 5))`: S=-0.11, F=-0.01, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(est_cashflow_invst, 22)`: S=0.12, F=0.02, T=34.4%, INFERIOR (TOP3000)
- `ts_mean(est_cashflow_invst, 10)`: S=-0.18, F=-0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(est_cashflow_invst, 22))`: S=0.59, F=0.26, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_invst)`: S=0.28, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_invst / close)`: S=0.29, F=0.11, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+5.5%
  - 2020: S=1.17 (moderate), ret=+13.8%
  - 2021: S=-0.41 (negative), ret=-5.3%
  - 2022: S=1.14 (moderate), ret=+15.0%
  - 2023: S=1.32 (moderate), ret=+11.6%

## Risk & Drawdown
- Max drawdown: 13.79% over 453 days (recovered)
- Annualized: return +8.3%, volatility 12.0% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.81, excess kurtosis +8.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.18, latest 1.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +9.15%; worst month: -5.86%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.14
- Sideways: S=1.34
- Bear: S=0.58

## Negated Direction
Best negated: `rank(-1 * est_cashflow_invst)` S=0.28, F=0.12, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_cashflow_invst)`: S=0.28, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_invst / close)`: S=0.29, F=0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_invst, 5))`: S=-0.11, F=-0.01, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(est_cashflow_invst, 5))` | TOP200 | 0.69 | 0.33 | 13.8% | 80% | mixed |
| `rank(ts_delta(est_cashflow_invst, 5))` | TOP500 | 0.61 | 0.22 | 9.3% | 40% | mixed |
| `rank(est_cashflow_invst)` | TOP200 | 0.26 | 0.12 | 32.9% | 60% | bear-only |
| `rank(est_cashflow_invst / close)` | TOP200 | 0.17 | 0.06 | 26.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_prsho: -0.142 (weakly negatively correlated)
- anl4_ptpr_number: -0.139 (weakly negatively correlated)
- fnd6_txdbclq: -0.118 (weakly negatively correlated)
- anl4_median_capexp: -0.115 (weakly negatively correlated)
- pv13_revere_country: -0.114 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
