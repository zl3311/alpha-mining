---
field: fnd6_dltr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.0
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0765
ann_vol: 0.0644
hit_rate: 0.5077
rolling_sharpe_min: -1.046
rolling_sharpe_max: 2.941
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.39
---
# fnd6_dltr (fundamental6)

*Long-Term Debt - Reduction*

## Signal Profile
- `rank(fnd6_dltr)`: S=0.77, F=0.53, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_dltr / close)`: S=1.00, F=0.72, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dltr, 5))`: S=0.03, F=0.00, T=34.1%, INFERIOR (TOP500)
- `-rank(fnd6_dltr)`: S=-0.47, F=-0.26, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltr, 5))`: S=0.61, F=0.26, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dltr, 63)`: S=0.26, F=0.11, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dltr, 10)`: S=-0.14, F=-0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dltr, 22))`: S=-0.58, F=-0.33, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltr)`: S=-0.77, F=-0.53, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltr / close)`: S=-1.00, F=-0.72, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.57 (moderate), ret=+2.0%
  - 2020: S=0.26 (weak), ret=+2.0%
  - 2021: S=1.98 (strong), ret=+15.4%
  - 2022: S=1.35 (moderate), ret=+9.9%
  - 2023: S=0.56 (moderate), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 7.65% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +6.4%, volatility 6.4% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.35, excess kurtosis +2.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 2.94, latest 0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.60%; worst month: -2.91%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.80
- Bear: S=-1.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dltr, 5))` S=0.61, F=0.26, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dltr)`: S=-0.77, F=-0.53, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltr / close)`: S=-1.00, F=-0.72, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltr, 5))`: S=0.61, F=0.26, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dltr / close)` | TOP3000 | 0.99 | 0.72 | 7.6% | 100% | bull-only |
| `rank(fnd6_dltr)` | TOP3000 | 0.76 | 0.53 | 14.2% | 80% | bull-only |
| `rank(fnd6_dltr / close)` | TOP1000 | 0.59 | 0.36 | 8.6% | 60% | bull-only |
| `rank(fnd6_dltr)` | TOP1000 | 0.46 | 0.26 | 14.7% | 60% | bull-only |
| `rank(fnd6_dltr / close)` | TOP500 | 0.28 | 0.13 | 15.2% | 60% | bull-only |
| `rank(fnd6_dltr)` | TOP500 | 0.16 | 0.06 | 25.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_rectr: 0.925 (strongly positively correlated)
- fnd6_mfma2_revt: 0.922 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.922 (strongly positively correlated)
- fnd6_newa2v1300_revt: 0.922 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.919 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.43 | 1.77 | +0.75 | -0.49 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.80 | +0.63 | -0.90 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.29 | 1.58 | +0.59 | -0.88 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.56 | +0.57 | -0.92 | yes |
| news_open_vol | news12 | -0.19 | 1.50 | +0.51 | -0.81 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
