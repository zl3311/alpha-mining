---
field: fn_assets_fair_val_l2_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.21
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0674
ann_vol: 0.0392
hit_rate: 0.515
rolling_sharpe_min: -0.523
rolling_sharpe_max: 2.534
top_merge_partner: fnd6_ivaco
redundancy_cluster: 21
negated_best_sharpe: 0.29
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.92
---
# fn_assets_fair_val_l2_q (fundamental2)

*Asset Fair Value, Recurring, Level 2*

## Signal Profile
- `rank(fn_assets_fair_val_l2_q)`: S=0.97, F=0.55, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_l2_q / close)`: S=1.21, F=0.74, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_l2_q, 5))`: S=0.85, F=0.55, T=38.0%, INFERIOR (TOP500)
- `-rank(fn_assets_fair_val_l2_q)`: S=-0.13, F=-0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l2_q, 5))`: S=-0.37, F=-0.16, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_assets_fair_val_l2_q, 63)`: S=0.55, F=0.27, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l2_q, 10)`: S=-0.18, F=-0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l2_q, 22))`: S=0.65, F=0.38, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_q)`: S=0.29, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_q / close)`: S=0.20, F=0.08, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.22, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.13 (moderate), ret=+3.1%
  - 2020: S=0.89 (moderate), ret=+3.6%
  - 2021: S=0.81 (moderate), ret=+3.0%
  - 2022: S=0.88 (moderate), ret=+3.9%
  - 2023: S=2.41 (strong), ret=+9.8%

## Risk & Drawdown
- Max drawdown: 6.74% over 312 days (recovered)
- Annualized: return +4.8%, volatility 3.9% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.52, excess kurtosis +1.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.52, max 2.53, latest 2.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +3.46%; worst month: -2.66%
Positive months: 70%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.84
- Sideways: S=1.56
- Bear: S=1.29

## Negated Direction
Best negated: `rank(-1 * fn_assets_fair_val_l2_q)` S=0.29, F=0.15, INFERIOR
Direction gap: -0.92 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l2_q)`: S=0.29, F=0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_q / close)`: S=0.20, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l2_q, 5))`: S=-0.37, F=-0.16, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_assets_fair_val_l2_q / close)` | TOP3000 | 1.22 | 0.74 | 6.7% | 100% | all-weather |
| `rank(ts_delta(fn_assets_fair_val_l2_q, 5))` | TOP500 | 0.85 | 0.55 | 20.6% | 80% | all-weather |
| `rank(fn_assets_fair_val_l2_q)` | TOP3000 | 0.98 | 0.55 | 11.5% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l2_q, 5))` | TOP200 | 0.66 | 0.36 | 29.7% | 80% | all-weather |
| `rank(ts_delta(fn_assets_fair_val_l2_q, 5))` | TOP3000 | 0.39 | 0.14 | 23.6% | 60% | mixed |
| `rank(ts_delta(fn_assets_fair_val_l2_q, 5))` | TOP1000 | 0.19 | 0.05 | 25.3% | 80% | weak |
| `rank(fn_assets_fair_val_l2_q / close)` | TOP1000 | 0.17 | 0.04 | 13.5% | 80% | bull-only |
| `rank(fn_assets_fair_val_l2_q)` | TOP1000 | 0.14 | 0.03 | 18.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_l2_a: 0.819 (strongly positively correlated)
- fnd2_unrgtxbnfinregfcrps: 0.571 (moderately positively correlated)
- fn_comp_not_rec_a: 0.567 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.565 (moderately positively correlated)
- fnd2_a_dfdtxava: 0.554 (moderately positively correlated)

Redundancy cluster #21: 2 similar fields, mean |rho| 0.819 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.18 | 1.98 | +0.63 | -0.46 | yes |
| est_rd_expense | analyst4 | -0.08 | 1.63 | +0.41 | -0.90 | yes |
| implied_volatility_call_20 | option8 | +0.04 | 1.67 | +0.41 | -0.81 | yes |
| max_net_income_guidance | analyst4 | +0.05 | 1.73 | +0.42 | -0.73 | yes |
| implied_volatility_call_30 | option8 | +0.06 | 1.62 | +0.39 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
