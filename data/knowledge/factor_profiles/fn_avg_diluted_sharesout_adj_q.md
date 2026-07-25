---
field: fn_avg_diluted_sharesout_adj_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.79
best_fitness: 0.44
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1147
ann_vol: 0.143
hit_rate: 0.5142
rolling_sharpe_min: 0.065
rolling_sharpe_max: 1.796
redundancy_cluster: 25
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.55
---
# fn_avg_diluted_sharesout_adj_q (fundamental2)

*The sum of dilutive potential common shares or units used in the calculation of the diluted per-share or per-unit computation.*

## Signal Profile
- `rank(fn_avg_diluted_sharesout_adj_q)`: S=-0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(fn_avg_diluted_sharesout_adj_q / close)`: S=0.28, F=0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_avg_diluted_sharesout_adj_q, 5))`: S=0.79, F=0.44, T=36.3%, INFERIOR (TOP500)
- `-rank(fn_avg_diluted_sharesout_adj_q)`: S=0.23, F=0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_avg_diluted_sharesout_adj_q, 5))`: S=-0.77, F=-0.42, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_avg_diluted_sharesout_adj_q, 22)`: S=0.17, F=0.04, T=33.0%, INFERIOR (TOP3000)
- `ts_mean(fn_avg_diluted_sharesout_adj_q, 10)`: S=0.24, F=0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_avg_diluted_sharesout_adj_q, 22))`: S=0.34, F=0.11, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_q)`: S=0.24, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_q / close)`: S=0.25, F=0.08, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.79, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+3.3%
  - 2020: S=1.03 (moderate), ret=+12.6%
  - 2021: S=1.38 (moderate), ret=+17.5%
  - 2022: S=0.56 (moderate), ret=+9.4%
  - 2023: S=0.72 (moderate), ret=+12.6%

## Risk & Drawdown
- Max drawdown: 11.47% over 179 days (recovered)
- Annualized: return +11.3%, volatility 14.3% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +2.72, excess kurtosis +28.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.07, max 1.80, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +12.12%; worst month: -5.49%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.25
- Sideways: S=0.83
- Bear: S=0.33

## Negated Direction
Best negated: `rank(-1 * fn_avg_diluted_sharesout_adj_q)` S=0.24, F=0.08, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_avg_diluted_sharesout_adj_q)`: S=0.24, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_q / close)`: S=0.25, F=0.08, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_avg_diluted_sharesout_adj_q, 5))`: S=-0.77, F=-0.42, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_q, 5))` | TOP500 | 0.79 | 0.44 | 11.5% | 100% | mixed |
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_q, 5))` | TOP1000 | 0.39 | 0.12 | 13.3% | 60% | bull-only |
| `rank(fn_avg_diluted_sharesout_adj_q / close)` | TOP3000 | 0.27 | 0.07 | 5.8% | 60% | bull-only |
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_q, 5))` | TOP200 | 0.20 | 0.06 | 24.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_incremental_shares_attributable_to_share_based_payment_q: 0.743 (strongly positively correlated)
- fn_oth_income_loss_net_of_tax_q: 0.299 (weakly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.130 (weakly positively correlated)
- fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q: 0.128 (weakly positively correlated)
- fn_comp_non_opt_grants_a: 0.125 (weakly positively correlated)

Redundancy cluster #25: 2 similar fields, mean |rho| 0.743 (representative: fn_incremental_shares_attributable_to_share_based_payment_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
