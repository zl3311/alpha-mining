---
field: fnd6_newqv1300_invrmq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.75
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1415
ann_vol: 0.135
hit_rate: 0.5158
rolling_sharpe_min: -0.403
rolling_sharpe_max: 2.549
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 55
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: -0.16
---
# fnd6_newqv1300_invrmq (fundamental6)

*Inventory - Raw Materials*

## Signal Profile
- `rank(fnd6_newqv1300_invrmq)`: S=0.75, F=0.69, T=8.5%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_invrmq / close)`: S=0.81, F=0.75, T=8.7%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_invrmq, 5))`: S=-0.14, F=-0.03, T=55.9%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_invrmq)`: S=-0.40, F=-0.26, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invrmq, 5))`: S=0.65, F=0.34, T=57.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_invrmq, 63)`: S=0.22, F=0.06, T=22.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_invrmq, 10)`: S=0.65, F=0.47, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_invrmq, 22))`: S=-0.22, F=-0.07, T=22.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invrmq)`: S=-0.75, F=-0.69, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invrmq / close)`: S=-0.81, F=-0.75, T=8.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.89 (strong), ret=+15.9%
  - 2020: S=0.10 (weak), ret=+1.4%
  - 2021: S=1.36 (moderate), ret=+26.6%
  - 2022: S=0.96 (moderate), ret=+12.4%
  - 2023: S=-0.32 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 14.15% over 351 days (recovered)
- Annualized: return +10.9%, volatility 13.5% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.02, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.40, max 2.55, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +13.68%; worst month: -8.24%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=0.99
- Bear: S=-1.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_invrmq, 5))` S=0.65, F=0.34, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_invrmq)`: S=-0.75, F=-0.69, T=8.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invrmq / close)`: S=-0.81, F=-0.75, T=8.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invrmq, 5))`: S=0.65, F=0.34, T=57.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_invrmq / close)` | TOP500 | 0.81 | 0.75 | 14.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_invrmq)` | TOP500 | 0.75 | 0.69 | 18.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_invrmq / close)` | TOP1000 | 0.43 | 0.29 | 14.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_invrmq)` | TOP1000 | 0.39 | 0.26 | 19.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_invrmq / close)` | TOP3000 | 0.28 | 0.13 | 16.5% | 40% | bull-only |
| `rank(fnd6_newqv1300_invrmq)` | TOP3000 | 0.21 | 0.10 | 26.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_invfgq: 0.816 (strongly positively correlated)
- fnd6_invwip: 0.765 (strongly positively correlated)
- fnd6_loxdr: 0.661 (moderately positively correlated)
- pv13_revere_term_sector_total: 0.654 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.652 (moderately positively correlated)

Redundancy cluster #55: 2 similar fields, mean |rho| 0.816 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.56 | +0.54 | -0.57 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.28 | 1.30 | +0.49 | -0.53 | yes |
| rp_ess_revenue | news18 | -0.27 | 1.37 | +0.48 | -0.52 | yes |
| cashflow_efficiency_rank_derivative | model16 | -0.26 | 1.29 | +0.48 | -0.33 | yes |
| multi_factor_static_score_derivative | model16 | -0.26 | 1.32 | +0.48 | -0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
