---
field: fnd6_newqv1300_tstknq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0691
ann_vol: 0.054
hit_rate: 0.5134
rolling_sharpe_min: -1.571
rolling_sharpe_max: 2.776
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 36
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_newqv1300_tstknq (fundamental6)

*Treasury Stock - Number of Common Shares*

## Signal Profile
- `rank(fnd6_newqv1300_tstknq)`: S=0.79, F=0.48, T=4.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_tstknq / close)`: S=0.92, F=0.58, T=4.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_tstknq, 5))`: S=0.45, F=0.14, T=42.3%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_tstknq)`: S=-0.41, F=-0.20, T=5.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tstknq, 5))`: S=0.55, F=0.28, T=48.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_tstknq, 63)`: S=0.07, F=0.01, T=21.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_tstknq, 10)`: S=-0.20, F=-0.07, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_tstknq, 22))`: S=-0.97, F=-0.54, T=19.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstknq)`: S=0.27, F=0.12, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstknq / close)`: S=0.22, F=0.08, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+1.5%
  - 2020: S=-1.09 (negative), ret=-4.7%
  - 2021: S=1.88 (strong), ret=+11.5%
  - 2022: S=2.02 (strong), ret=+15.8%
  - 2023: S=-0.02 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 6.91% over 509 days (recovered)
- Annualized: return +4.9%, volatility 5.4% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.03, excess kurtosis +1.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.78, latest -0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.86%; worst month: -2.00%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.61
- Bear: S=-1.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_tstknq, 5))` S=0.55, F=0.28, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_tstknq)`: S=0.27, F=0.12, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tstknq / close)`: S=0.22, F=0.08, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tstknq, 5))`: S=0.55, F=0.28, T=48.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_tstknq / close)` | TOP3000 | 0.91 | 0.58 | 6.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstknq)` | TOP3000 | 0.78 | 0.48 | 11.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstknq / close)` | TOP1000 | 0.55 | 0.31 | 10.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstknq)` | TOP1000 | 0.40 | 0.20 | 10.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_tstknq / close)` | TOP500 | 0.38 | 0.19 | 10.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_tstknq, 5))` | TOP3000 | 0.46 | 0.14 | 13.6% | 40% | mixed |
| `rank(fnd6_newqv1300_tstknq)` | TOP500 | 0.23 | 0.10 | 16.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_tstkn: 0.981 (strongly positively correlated)
- fnd6_newqv1300_tstkq: 0.973 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.968 (strongly positively correlated)
- fnd6_tstkc: 0.967 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.899 (strongly positively correlated)

Redundancy cluster #36: 4 similar fields, mean |rho| 0.734 (representative: anl4_fcf_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.47 | 1.70 | +0.67 | -0.82 | yes |
| news_open_vol | news12 | -0.38 | 1.62 | +0.69 | -0.47 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.40 | 1.58 | +0.66 | -0.36 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.33 | 1.54 | +0.59 | -0.95 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.25 | 1.51 | +0.57 | -0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
