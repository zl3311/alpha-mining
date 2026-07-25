---
field: est_cashflow_fin
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.83
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.4624
ann_vol: 0.1395
hit_rate: 0.5174
rolling_sharpe_min: -1.743
rolling_sharpe_max: 3.153
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.37
---
# est_cashflow_fin (analyst4)

*Cash Flow From Financing - mean of estimations*

## Signal Profile
- `rank(est_cashflow_fin)`: S=0.07, F=0.02, T=2.5%, INFERIOR (TOP200)
- `rank(est_cashflow_fin / close)`: S=0.12, F=0.04, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(est_cashflow_fin, 5))`: S=0.14, F=0.03, T=34.2%, INFERIOR (TOP200)
- `-rank(est_cashflow_fin)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_fin, 5))`: S=0.83, F=0.32, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(est_cashflow_fin, 63)`: S=0.46, F=0.17, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(est_cashflow_fin, 10)`: S=-0.28, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(est_cashflow_fin, 22))`: S=-0.94, F=-0.52, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_fin)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_fin / close)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.13, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+5.0%
  - 2020: S=2.41 (strong), ret=+28.3%
  - 2021: S=-0.45 (negative), ret=-7.5%
  - 2022: S=-1.30 (negative), ret=-24.5%
  - 2023: S=0.85 (moderate), ret=+7.8%

## Risk & Drawdown
- Max drawdown: 46.24% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 14.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.15, excess kurtosis +2.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.74, max 3.15, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.82%; worst month: -12.71%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.75
- Sideways: S=0.59
- Bear: S=2.51

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_cashflow_fin, 5))` S=0.83, F=0.32, INFERIOR
Direction gap: +0.37 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_cashflow_fin)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * est_cashflow_fin / close)`: S=0.10, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_cashflow_fin, 5))`: S=0.83, F=0.32, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_cashflow_fin / close)` | TOP200 | 0.13 | 0.04 | 46.2% | 60% | bear-only |
| `rank(ts_delta(est_cashflow_fin, 5))` | TOP200 | 0.14 | 0.03 | 24.1% | 60% | weak |
| `rank(est_cashflow_fin / close)` | TOP500 | 0.09 | 0.02 | 42.5% | 40% | bear-only |
| `rank(est_cashflow_fin)` | TOP200 | 0.09 | 0.02 | 50.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_median: 0.954 (strongly positively correlated)
- anl4_cff_low: 0.946 (strongly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_a: 0.830 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.826 (strongly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.818 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
