---
field: fnd6_newqv1300_tstkq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.87
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0955
ann_vol: 0.0589
hit_rate: 0.5085
rolling_sharpe_min: -1.906
rolling_sharpe_max: 2.674
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.36
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.51
---
# fnd6_newqv1300_tstkq (fundamental6)

*Treasury Stock - Total (All Capital)*

## Signal Profile
- `rank(fnd6_newqv1300_tstkq)`: S=0.76, F=0.47, T=2.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_tstkq / close)`: S=0.87, F=0.56, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_tstkq, 5))`: S=0.29, F=0.07, T=39.3%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_tstkq)`: S=-0.32, F=-0.14, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tstkq, 5))`: S=0.36, F=0.11, T=39.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_tstkq, 63)`: S=-0.04, F=0.00, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_tstkq, 10)`: S=-0.20, F=-0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_tstkq, 22))`: S=-0.62, F=-0.28, T=17.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstkq)`: S=-0.32, F=-0.14, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstkq / close)`: S=-0.42, F=-0.21, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.86, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.28 (moderate), ret=+3.2%
  - 2020: S=-1.47 (negative), ret=-5.8%
  - 2021: S=1.69 (strong), ret=+11.2%
  - 2022: S=1.90 (strong), ret=+16.7%
  - 2023: S=-0.12 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 9.55% over 556 days (recovered)
- Annualized: return +5.1%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.04, excess kurtosis +1.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 2.67, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.02%; worst month: -2.32%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.88
- Bear: S=-2.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_tstkq, 5))` S=0.36, F=0.11, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_tstkq)`: S=-0.32, F=-0.14, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstkq / close)`: S=-0.42, F=-0.21, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tstkq, 5))`: S=0.36, F=0.11, T=39.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_tstkq / close)` | TOP3000 | 0.86 | 0.56 | 9.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstkq)` | TOP3000 | 0.74 | 0.47 | 12.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstkq / close)` | TOP1000 | 0.41 | 0.21 | 9.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstkq)` | TOP1000 | 0.31 | 0.14 | 12.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstkq / close)` | TOP500 | 0.22 | 0.09 | 14.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_tstkq, 5))` | TOP3000 | 0.28 | 0.07 | 16.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_tstkq, 5))` | TOP200 | 0.21 | 0.06 | 39.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_tstkq, 5))` | TOP500 | 0.19 | 0.05 | 30.4% | 60% | all-weather |
| `rank(fnd6_newqv1300_tstkq)` | TOP500 | 0.13 | 0.04 | 17.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_tstk: 0.992 (strongly positively correlated)
- fnd6_tstkc: 0.989 (strongly positively correlated)
- fnd6_newqv1300_tstknq: 0.973 (strongly positively correlated)
- fnd6_newa2v1300_tstkn: 0.970 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.925 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.50 | 1.75 | +0.72 | -0.91 | yes |
| news_open_vol | news12 | -0.41 | 1.63 | +0.71 | -0.26 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.34 | 1.53 | +0.59 | -0.95 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.40 | 1.44 | +0.58 | -0.93 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.43 | 1.52 | +0.61 | -0.48 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
