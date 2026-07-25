---
field: fn_liab_fair_val_l2_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.41
best_fitness: 0.86
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0921
ann_vol: 0.0333
hit_rate: 0.5328
rolling_sharpe_min: -1.81
rolling_sharpe_max: 3.081
top_merge_partner: fnd6_ivaco
redundancy_cluster: 10
negated_best_sharpe: 0.58
negated_best_template: neg_rank_level
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.83
---
# fn_liab_fair_val_l2_q (fundamental2)

*Liabilities Fair Value, Recurring, Level 2*

## Signal Profile
- `rank(fn_liab_fair_val_l2_q)`: S=1.00, F=0.57, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_liab_fair_val_l2_q / close)`: S=1.41, F=0.86, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_liab_fair_val_l2_q, 5))`: S=0.64, F=0.27, T=36.5%, INFERIOR (TOP3000)
- `-rank(fn_liab_fair_val_l2_q)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l2_q, 5))`: S=0.46, F=0.23, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_liab_fair_val_l2_q, 63)`: S=0.71, F=0.38, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_l2_q, 10)`: S=-0.05, F=-0.01, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_l2_q, 22))`: S=-0.63, F=-0.34, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_q)`: S=0.58, F=0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_q / close)`: S=0.49, F=0.28, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.96 (strong), ret=+5.0%
  - 2020: S=-0.06 (negative), ret=-0.2%
  - 2021: S=0.46 (weak), ret=+1.8%
  - 2022: S=2.05 (strong), ret=+6.9%
  - 2023: S=3.11 (strong), ret=+9.4%

## Risk & Drawdown
- Max drawdown: 9.21% over 735 days (recovered)
- Annualized: return +4.7%, volatility 3.3% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.02, excess kurtosis +1.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.81, max 3.08, latest 3.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +2.75%; worst month: -2.22%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.44
- Sideways: S=1.71
- Bear: S=0.18

## Negated Direction
Best negated: `rank(-1 * fn_liab_fair_val_l2_q)` S=0.58, F=0.35, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_l2_q)`: S=0.58, F=0.35, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_q / close)`: S=0.49, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l2_q, 5))`: S=0.46, F=0.23, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_liab_fair_val_l2_q / close)` | TOP3000 | 1.40 | 0.86 | 9.2% | 80% | mixed |
| `rank(fn_liab_fair_val_l2_q)` | TOP3000 | 1.00 | 0.57 | 15.8% | 80% | bull-only |
| `rank(ts_delta(fn_liab_fair_val_l2_q, 5))` | TOP3000 | 0.63 | 0.27 | 11.6% | 80% | all-weather |
| `rank(fn_liab_fair_val_l2_q / close)` | TOP1000 | 0.13 | 0.03 | 10.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_liab_fair_val_l2_a: 0.738 (strongly positively correlated)
- fn_assets_fair_val_l2_q: 0.553 (moderately positively correlated)
- fn_assets_fair_val_l2_a: 0.533 (moderately positively correlated)
- fnd6_newqv1300_aol2q: 0.481 (moderately positively correlated)
- fnd6_newa1v1300_aol2: 0.466 (moderately positively correlated)

Redundancy cluster #10: 2 similar fields, mean |rho| 0.738 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | +0.00 | 1.95 | +0.55 | -0.50 | yes |
| implied_volatility_call_120 | option8 | +0.10 | 1.86 | +0.46 | -0.84 | yes |
| implied_volatility_call_270 - implied_volatility_put_270 | option8 | +0.02 | 2.26 | +0.46 | -0.86 | yes |
| implied_volatility_call_90 | option8 | +0.09 | 1.91 | +0.45 | -0.72 | yes |
| anl4_qf_az_eps_number | analyst4 | +0.06 | 1.89 | +0.49 | -0.27 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
