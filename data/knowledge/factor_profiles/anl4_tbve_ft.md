---
field: anl4_tbve_ft
dataset: analyst4
best_template: ts_zscore
best_sharpe: 1.7
best_fitness: 2.62
best_universe: TOP3000
grade: SPECTACULAR
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 35
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1142
ann_vol: 0.0687
hit_rate: 0.5628
rolling_sharpe_min: -0.682
rolling_sharpe_max: 3.431
top_merge_partner: fn_comp_options_forfeitures_and_expirations_a
negated_best_sharpe: 0.07
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -1.63
---
# anl4_tbve_ft (analyst4)

*Tangible Book Value per Share - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_tbve_ft)`: S=1.26, F=1.04, T=2.2%, AVERAGE (TOP3000)
- `rank(anl4_tbve_ft / close)`: S=0.48, F=0.34, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_tbve_ft, 5))`: S=0.35, F=0.22, T=23.3%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(anl4_tbve_ft), 5)`: S=1.25, F=1.03, T=2.2%, AVERAGE (TOP3000)
- `-rank(anl4_tbve_ft)`: S=-0.20, F=-0.08, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbve_ft, 5))`: S=-0.18, F=-0.10, T=7.6%, INFERIOR (TOP3000)
- `ts_zscore(anl4_tbve_ft, 22)`: S=1.70, F=2.62, T=1.3%, SPECTACULAR (TOP3000)
- `ts_mean(anl4_tbve_ft, 10)`: S=0.19, F=0.08, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tbve_ft, 22))`: S=0.25, F=0.20, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbve_ft)`: S=0.07, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbve_ft / close)`: S=-0.48, F=-0.34, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/18P
- LOW_FITNESS: 30F/5P
- LOW_SHARPE: 31F/4P
- LOW_SUB_UNIVERSE_SHARPE: 8F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.25, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.36 (strong), ret=+8.5%
  - 2020: S=1.14 (moderate), ret=+5.9%
  - 2021: S=1.58 (strong), ret=+16.0%
  - 2022: S=0.85 (moderate), ret=+6.8%
  - 2023: S=1.04 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 11.42% over 199 days (recovered)
- Annualized: return +8.6%, volatility 6.9% (fraction of booksize)
- Hit rate: 56.3% positive days
- Tail shape: skew -0.22, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.68, max 3.43, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +4.67%; worst month: -3.65%
Positive months: 70%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.05
- Sideways: S=1.53
- Bear: S=0.01

## Negated Direction
Best negated: `rank(-1 * anl4_tbve_ft)` S=0.07, F=0.03, INFERIOR
Direction gap: -1.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_tbve_ft)`: S=0.07, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbve_ft / close)`: S=-0.48, F=-0.34, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbve_ft, 5))`: S=-0.18, F=-0.10, T=7.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tbve_ft)` | TOP3000 | 1.25 | 1.04 | 11.4% | 100% | mixed |
| `ts_decay_linear(rank(anl4_tbve_ft), 5)` | TOP3000 | 1.24 | 1.03 | 11.4% | 100% | mixed |
| `rank(anl4_tbve_ft / close)` | TOP200 | 0.49 | 0.34 | 25.4% | 80% | mixed |
| `rank(anl4_tbve_ft)` | TOP500 | 0.39 | 0.30 | 30.6% | 60% | bull-only |
| `rank(ts_delta(anl4_tbve_ft, 5))` | TOP3000 | 0.34 | 0.22 | 69.9% | 80% | bull-only |
| `rank(ts_delta(anl4_tbve_ft, 5))` | TOP200 | 0.20 | 0.13 | 34.6% | 60% | bull-only |
| `rank(ts_delta(anl4_tbve_ft, 5))` | TOP500 | 0.21 | 0.12 | 42.6% | 40% | bull-only |
| `rank(anl4_tbve_ft)` | TOP1000 | 0.20 | 0.08 | 26.1% | 60% | bull-only |
| `rank(anl4_tbve_ft / close)` | TOP500 | 0.19 | 0.08 | 41.0% | 60% | bear-only |
| `rank(anl4_tbve_ft / close)` | TOP1000 | 0.19 | 0.08 | 37.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_tot_gw_ft: 0.745 (strongly positively correlated)
- anl4_fcfps_flag: 0.729 (strongly positively correlated)
- anl4_bvps_flag: 0.701 (strongly positively correlated)
- rel_num_comp: 0.691 (moderately positively correlated)
- rel_num_all: 0.685 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.24 | 1.96 | +0.71 | -0.68 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.23 | 2.33 | +0.70 | -0.66 | yes |
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.24 | 2.69 | +0.67 | -0.81 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.22 | 2.50 | +0.63 | -0.81 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.33 | 1.85 | +0.60 | +0.10 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: trade_when
