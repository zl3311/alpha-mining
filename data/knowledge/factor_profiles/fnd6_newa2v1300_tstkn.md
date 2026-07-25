---
field: fnd6_newa2v1300_tstkn
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.86
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0749
ann_vol: 0.0531
hit_rate: 0.5174
rolling_sharpe_min: -1.524
rolling_sharpe_max: 2.674
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.54
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_newa2v1300_tstkn (fundamental6)

*Treasury Stock - Number of Common Shares*

## Signal Profile
- `rank(fnd6_newa2v1300_tstkn)`: S=0.69, F=0.39, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_tstkn / close)`: S=0.86, F=0.52, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_tstkn, 5))`: S=0.28, F=0.13, T=20.7%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_tstkn)`: S=-0.34, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_tstkn, 5))`: S=0.86, F=0.54, T=35.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_tstkn, 22)`: S=0.38, F=0.27, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_tstkn, 10)`: S=-0.12, F=-0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_tstkn, 22))`: S=-0.45, F=-0.25, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstkn)`: S=-0.34, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstkn / close)`: S=-0.49, F=-0.25, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+1.1%
  - 2020: S=-1.12 (negative), ret=-4.6%
  - 2021: S=1.71 (strong), ret=+10.2%
  - 2022: S=1.96 (strong), ret=+15.2%
  - 2023: S=0.03 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 7.49% over 561 days (recovered)
- Annualized: return +4.5%, volatility 5.3% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.01, excess kurtosis +1.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 2.67, latest -0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.57%; worst month: -2.25%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.15
- Sideways: S=0.76
- Bear: S=-2.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_tstkn, 5))` S=0.86, F=0.54, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_tstkn)`: S=-0.34, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_tstkn / close)`: S=-0.49, F=-0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_tstkn, 5))`: S=0.86, F=0.54, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_tstkn / close)` | TOP3000 | 0.85 | 0.52 | 7.5% | 80% | bull-only |
| `rank(fnd6_newa2v1300_tstkn)` | TOP3000 | 0.68 | 0.39 | 12.4% | 60% | bull-only |
| `rank(fnd6_newa2v1300_tstkn / close)` | TOP1000 | 0.47 | 0.25 | 11.2% | 40% | bull-only |
| `rank(fnd6_newa2v1300_tstkn / close)` | TOP500 | 0.45 | 0.23 | 9.6% | 60% | bull-only |
| `rank(fnd6_newa2v1300_tstkn)` | TOP1000 | 0.33 | 0.15 | 10.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_tstkn, 5))` | TOP200 | 0.28 | 0.13 | 33.6% | 40% | mixed |
| `rank(fnd6_newa2v1300_tstkn)` | TOP500 | 0.26 | 0.11 | 16.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_tstkn, 5))` | TOP500 | 0.10 | 0.02 | 37.2% | 20% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_tstknq: 0.981 (strongly positively correlated)
- fnd6_newa2v1300_tstk: 0.979 (strongly positively correlated)
- fnd6_tstkc: 0.979 (strongly positively correlated)
- fnd6_newqv1300_tstkq: 0.970 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.908 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.46 | 1.64 | +0.62 | -0.82 | yes |
| news_open_vol | news12 | -0.37 | 1.55 | +0.63 | -0.48 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.41 | 1.53 | +0.62 | -0.34 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.32 | 1.48 | +0.54 | -0.94 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.27 | 1.49 | +0.54 | -0.72 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
