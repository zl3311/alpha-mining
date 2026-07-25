---
field: fnd6_newqv1300_capsq
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.02
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0798
ann_vol: 0.0461
hit_rate: 0.5231
rolling_sharpe_min: -0.835
rolling_sharpe_max: 2.817
top_merge_partner: snt_value_fast_d1
redundancy_cluster: 32
negated_best_sharpe: 0.93
negated_best_template: rank_neg_delta
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.09
---
# fnd6_newqv1300_capsq (fundamental6)

*Capital Surplus/Share Premium Reserve*

## Signal Profile
- `rank(fnd6_newqv1300_capsq)`: S=1.02, F=0.63, T=3.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_capsq / close)`: S=0.31, F=0.14, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_capsq, 5))`: S=-0.05, F=-0.01, T=41.8%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_capsq)`: S=-0.32, F=-0.12, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_capsq, 5))`: S=0.93, F=0.45, T=40.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_capsq, 63)`: S=-0.30, F=-0.09, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_capsq, 10)`: S=0.07, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_capsq, 22))`: S=-0.56, F=-0.23, T=19.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_capsq)`: S=-0.32, F=-0.12, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_capsq / close)`: S=-0.29, F=-0.12, T=4.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.13 (moderate), ret=+3.6%
  - 2020: S=0.15 (weak), ret=+0.6%
  - 2021: S=1.24 (moderate), ret=+8.2%
  - 2022: S=1.37 (moderate), ret=+5.8%
  - 2023: S=1.31 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 7.98% over 162 days (recovered)
- Annualized: return +4.7%, volatility 4.6% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.12, excess kurtosis +2.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.83, max 2.82, latest 1.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.92%; worst month: -1.84%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.42
- Sideways: S=1.44
- Bear: S=-0.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_capsq, 5))` S=0.93, F=0.45, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_capsq)`: S=-0.32, F=-0.12, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_capsq / close)`: S=-0.29, F=-0.12, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_capsq, 5))`: S=0.93, F=0.45, T=40.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_capsq)` | TOP3000 | 1.02 | 0.63 | 8.0% | 100% | bull-only |
| `rank(fnd6_newqv1300_capsq / close)` | TOP3000 | 0.31 | 0.14 | 22.3% | 80% | mixed |
| `rank(fnd6_newqv1300_capsq / close)` | TOP500 | 0.32 | 0.13 | 13.1% | 80% | mixed |
| `rank(fnd6_newqv1300_capsq)` | TOP1000 | 0.32 | 0.12 | 14.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_capsq / close)` | TOP1000 | 0.29 | 0.12 | 11.2% | 80% | mixed |
| `rank(fnd6_newqv1300_capsq / close)` | TOP200 | 0.25 | 0.10 | 19.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_capsq)` | TOP500 | 0.08 | 0.02 | 20.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_caps: 0.962 (strongly positively correlated)
- fnd6_fopox: 0.826 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.803 (strongly positively correlated)
- fn_comp_not_rec_q: 0.753 (strongly positively correlated)
- cash: 0.746 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| snt_value_fast_d1 | socialmedia12 | -0.14 | 1.45 | +0.43 | -0.70 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.16 | 1.41 | +0.39 | -0.84 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.14 | 1.47 | +0.45 | -0.10 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.07 | 1.56 | +0.42 | -0.37 | yes |
| anl4_epsr_flag | analyst4 | -0.14 | 1.59 | +0.41 | -0.42 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
