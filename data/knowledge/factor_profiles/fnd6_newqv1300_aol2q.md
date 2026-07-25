---
field: fnd6_newqv1300_aol2q
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.27
best_fitness: 0.9
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0909
ann_vol: 0.0497
hit_rate: 0.519
rolling_sharpe_min: -1.503
rolling_sharpe_max: 3.75
top_merge_partner: rank(scl12_buzz * (-1 * returns))
redundancy_cluster: 17
negated_best_sharpe: 0.42
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.85
---
# fnd6_newqv1300_aol2q (fundamental6)

*Assets Level 2 (Observable)*

## Signal Profile
- `rank(fnd6_newqv1300_aol2q)`: S=0.97, F=0.68, T=6.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_aol2q / close)`: S=1.27, F=0.90, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_aol2q, 5))`: S=0.45, F=0.14, T=51.1%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_aol2q)`: S=-0.31, F=-0.13, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aol2q, 5))`: S=0.14, F=0.03, T=64.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_aol2q, 22)`: S=0.09, F=0.02, T=40.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_aol2q, 10)`: S=0.55, F=0.32, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aol2q, 22))`: S=0.95, F=0.47, T=23.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aol2q)`: S=0.42, F=0.25, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aol2q / close)`: S=0.21, F=0.09, T=9.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.4%
  - 2020: S=-0.69 (negative), ret=-2.8%
  - 2021: S=2.06 (strong), ret=+15.1%
  - 2022: S=1.82 (strong), ret=+8.7%
  - 2023: S=2.72 (strong), ret=+10.5%

## Risk & Drawdown
- Max drawdown: 9.09% over 745 days (recovered)
- Annualized: return +6.3%, volatility 5.0% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.16, excess kurtosis +2.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 3.75, latest 2.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +3.97%; worst month: -2.08%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.71
- Sideways: S=1.09
- Bear: S=-0.22

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_aol2q)` S=0.42, F=0.25, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aol2q)`: S=0.42, F=0.25, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aol2q / close)`: S=0.21, F=0.09, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aol2q, 5))`: S=0.14, F=0.03, T=64.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_aol2q / close)` | TOP3000 | 1.28 | 0.90 | 9.1% | 60% | mixed |
| `rank(fnd6_newqv1300_aol2q)` | TOP3000 | 0.97 | 0.68 | 18.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_aol2q / close)` | TOP1000 | 0.39 | 0.17 | 14.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aol2q, 5))` | TOP3000 | 0.46 | 0.14 | 20.6% | 80% | mixed |
| `rank(fnd6_newqv1300_aol2q)` | TOP1000 | 0.31 | 0.13 | 22.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_aol2q, 5))` | TOP500 | 0.24 | 0.07 | 32.7% | 80% | mixed |
| `rank(fnd6_newqv1300_aol2q / close)` | TOP500 | 0.09 | 0.02 | 17.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_aol2: 0.886 (strongly positively correlated)
- fnd6_newa1v1300_caps: 0.693 (moderately positively correlated)
- fnd6_tfva: 0.675 (moderately positively correlated)
- fnd6_ivch: 0.674 (moderately positively correlated)
- fnd6_fopox: 0.672 (moderately positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.19 | 2.23 | +0.60 | +0.10 | yes |
| implied_volatility_call_20 | option8 | -0.03 | 1.80 | +0.52 | -0.72 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.21 | 2.60 | +0.58 | +0.27 | yes |
| rp_ess_dividends | news18 | -0.02 | 1.88 | +0.48 | -0.77 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.00 | 1.93 | +0.48 | -0.56 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
