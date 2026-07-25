---
field: fn_liab_fair_val_l1_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.86
best_fitness: 0.65
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2238
ann_vol: 0.1788
hit_rate: 0.4761
rolling_sharpe_min: -1.165
rolling_sharpe_max: 3.073
top_merge_partner: growth_potential_rank_derivative
negated_best_sharpe: 0.99
negated_best_template: rank_neg_delta
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 0.13
---
# fn_liab_fair_val_l1_q (fundamental2)

*Liabilities Fair Value, Recurring, Level 1*

## Signal Profile
- `rank(fn_liab_fair_val_l1_q)`: S=0.30, F=0.08, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_liab_fair_val_l1_q / close)`: S=0.22, F=0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_liab_fair_val_l1_q, 5))`: S=0.86, F=0.65, T=26.8%, INFERIOR (TOP200)
- `-rank(fn_liab_fair_val_l1_q)`: S=0.79, F=0.40, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l1_q, 5))`: S=0.99, F=0.62, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_liab_fair_val_l1_q, 22)`: S=0.08, F=0.02, T=25.0%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_l1_q, 10)`: S=0.07, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_l1_q, 22))`: S=-0.55, F=-0.31, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_q)`: S=-0.30, F=-0.08, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_q / close)`: S=-0.22, F=-0.05, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 9F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.86, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.54 (negative), ret=-8.5%
  - 2020: S=1.32 (moderate), ret=+24.7%
  - 2021: S=1.35 (moderate), ret=+23.1%
  - 2022: S=2.59 (strong), ret=+52.7%
  - 2023: S=-1.12 (negative), ret=-16.7%

## Risk & Drawdown
- Max drawdown: 22.38% over 232 days (not yet recovered, ongoing at window end)
- Annualized: return +15.4%, volatility 17.9% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +1.16, excess kurtosis +10.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 3.07, latest -1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +20.11%; worst month: -7.07%
Positive months: 53%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.58
- Sideways: S=-0.47
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_liab_fair_val_l1_q, 5))` S=0.99, F=0.62, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_l1_q)`: S=-0.30, F=-0.08, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l1_q / close)`: S=-0.22, F=-0.05, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l1_q, 5))`: S=0.99, F=0.62, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_liab_fair_val_l1_q, 5))` | TOP200 | 0.86 | 0.65 | 22.4% | 60% | mixed |
| `rank(ts_delta(fn_liab_fair_val_l1_q, 5))` | TOP500 | 0.32 | 0.15 | 32.9% | 60% | mixed |
| `rank(fn_liab_fair_val_l1_q)` | TOP3000 | 0.30 | 0.08 | 10.5% | 60% | mixed |
| `rank(fn_liab_fair_val_l1_q / close)` | TOP3000 | 0.21 | 0.05 | 11.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.289 (weakly positively correlated)
- unsystematic_risk_last_30_days: -0.277 (weakly negatively correlated)
- min_stock_option_expense_guidance: 0.276 (weakly positively correlated)
- stock_option_expense_max_guidance_qtr: 0.276 (weakly positively correlated)
- anl4_cff_low: -0.270 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| growth_potential_rank_derivative | model16 | -0.14 | 1.33 | +0.44 | +0.07 | yes |
| multi_factor_static_score_derivative | model16 | -0.14 | 1.30 | +0.44 | +0.12 | yes |
| relative_valuation_rank_derivative | model16 | -0.14 | 1.37 | +0.44 | +0.02 | yes |
| earnings_certainty_rank_derivative | model16 | -0.14 | 1.37 | +0.44 | +0.02 | yes |
| fnd6_newqv1300_stkcpaq | fundamental6 | -0.07 | 1.25 | +0.38 | -0.55 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
