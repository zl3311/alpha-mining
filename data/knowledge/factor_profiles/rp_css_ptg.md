---
field: rp_css_ptg
dataset: news18
best_template: rank_level
best_sharpe: 0.98
best_fitness: 0.3
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.086
ann_vol: 0.0999
hit_rate: 0.5198
rolling_sharpe_min: -0.283
rolling_sharpe_max: 2.492
top_merge_partner: anl4_afv4_dts_spe
negated_best_sharpe: 0.13
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.85
---
# rp_css_ptg (news18)

*Composite sentiment score of price target news*

## Signal Profile
- `rank(rp_css_ptg)`: S=0.98, F=0.30, T=107.1%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_ptg, 5))`: S=0.37, F=0.04, T=162.7%, INFERIOR (TOP3000)
- `-rank(rp_css_ptg)`: S=-0.28, F=-0.03, T=123.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_ptg, 5))`: S=-0.37, F=-0.04, T=162.7%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_ptg, 22)`: S=0.16, F=0.01, T=133.3%, INFERIOR (TOP3000)
- `ts_mean(rp_css_ptg, 10)`: S=0.08, F=0.01, T=17.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_ptg, 22))`: S=0.07, F=0.00, T=135.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ptg)`: S=0.13, F=0.01, T=136.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ptg / close)`: S=-0.02, F=0.00, T=140.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.00, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.27 (negative), ret=-2.4%
  - 2020: S=1.67 (strong), ret=+18.6%
  - 2021: S=1.83 (strong), ret=+20.2%
  - 2022: S=0.90 (moderate), ret=+9.4%
  - 2023: S=0.51 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 8.60% over 291 days (recovered)
- Annualized: return +10.0%, volatility 10.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.32, excess kurtosis +4.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.28, max 2.49, latest 0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.58%; worst month: -4.28%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.22
- Sideways: S=0.71
- Bear: S=2.15

## Negated Direction
Best negated: `rank(-1 * rp_css_ptg)` S=0.13, F=0.01, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_css_ptg)`: S=0.13, F=0.01, T=136.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_ptg / close)`: S=-0.02, F=0.00, T=140.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_ptg, 5))`: S=-0.37, F=-0.04, T=162.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_ptg)` | TOP200 | 1.00 | 0.30 | 8.6% | 80% | mixed |
| `rank(rp_css_ptg)` | TOP500 | 0.64 | 0.12 | 10.8% | 60% | mixed |
| `rank(ts_delta(rp_css_ptg, 5))` | TOP3000 | 0.38 | 0.04 | 13.3% | 40% | weak |
| `rank(rp_css_ptg)` | TOP1000 | 0.30 | 0.03 | 10.3% | 40% | weak |
| `rank(ts_delta(rp_css_ptg, 5))` | TOP500 | 0.18 | 0.02 | 17.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- rp_css_earnings: 0.578 (moderately positively correlated)
- rp_css_revenue: 0.436 (moderately positively correlated)
- fnd6_prch: -0.373 (weakly negatively correlated)
- fnd6_prchq: -0.369 (weakly negatively correlated)
- anl4_fcf_number: -0.347 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.26 | 1.64 | +0.65 | -0.77 | yes |
| parkinson_volatility_120 | option8 | -0.21 | 1.50 | +0.50 | -0.62 | yes |
| news_open_vol | news12 | -0.16 | 1.47 | +0.47 | -0.80 | yes |
| fnd6_optprcby | fundamental6 | -0.17 | 1.54 | +0.55 | +0.67 | yes |
| fnd6_fopo | fundamental6 | -0.18 | 1.52 | +0.45 | -0.53 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
