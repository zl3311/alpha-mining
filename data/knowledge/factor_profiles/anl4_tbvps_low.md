---
field: anl4_tbvps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.06
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0776
ann_vol: 0.0657
hit_rate: 0.5206
rolling_sharpe_min: -1.134
rolling_sharpe_max: 3.333
top_merge_partner: pcr_vol_20
redundancy_cluster: 29
negated_best_sharpe: 0.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.94
---
# anl4_tbvps_low (analyst4)

*Tangible Book Value per Share - The lowest estimation*

## Signal Profile
- `rank(anl4_tbvps_low)`: S=0.54, F=0.31, T=2.1%, INFERIOR (TOP500)
- `rank(anl4_tbvps_low / close)`: S=1.06, F=0.79, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_tbvps_low, 5))`: S=0.46, F=0.13, T=36.1%, INFERIOR (TOP3000)
- `-rank(anl4_tbvps_low)`: S=-0.18, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_low, 5))`: S=0.12, F=0.03, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_tbvps_low, 63)`: S=0.16, F=0.04, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_tbvps_low, 10)`: S=-0.27, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tbvps_low, 22))`: S=-0.35, F=-0.14, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_low)`: S=-0.54, F=-0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_low / close)`: S=-0.87, F=-0.72, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.06, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.40 (negative), ret=-1.7%
  - 2020: S=1.18 (moderate), ret=+10.7%
  - 2021: S=1.89 (strong), ret=+9.8%
  - 2022: S=1.85 (strong), ret=+10.0%
  - 2023: S=0.76 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 7.76% over 184 days (recovered)
- Annualized: return +6.9%, volatility 6.6% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.56, excess kurtosis +4.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 3.33, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.48%; worst month: -3.30%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.92
- Sideways: S=0.40
- Bear: S=0.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_tbvps_low, 5))` S=0.12, F=0.03, INFERIOR
Direction gap: -0.94 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_tbvps_low)`: S=-0.54, F=-0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_low / close)`: S=-0.87, F=-0.72, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_low, 5))`: S=0.12, F=0.03, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tbvps_low / close)` | TOP3000 | 1.06 | 0.79 | 7.8% | 80% | all-weather |
| `rank(anl4_tbvps_low / close)` | TOP500 | 0.88 | 0.72 | 15.2% | 60% | mixed |
| `rank(anl4_tbvps_low / close)` | TOP1000 | 0.64 | 0.41 | 9.3% | 80% | all-weather |
| `rank(anl4_tbvps_low)` | TOP500 | 0.54 | 0.31 | 17.4% | 80% | weak |
| `rank(ts_delta(anl4_tbvps_low, 5))` | TOP3000 | 0.45 | 0.13 | 12.2% | 60% | weak |
| `rank(ts_delta(anl4_tbvps_low, 5))` | TOP1000 | 0.27 | 0.07 | 11.5% | 40% | mixed |
| `rank(ts_delta(anl4_tbvps_low, 5))` | TOP200 | 0.20 | 0.06 | 45.6% | 60% | weak |
| `rank(anl4_tbvps_low)` | TOP1000 | 0.16 | 0.05 | 10.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_tbvps_mean: 0.999 (strongly positively correlated)
- anl4_tbvps_median: 0.999 (strongly positively correlated)
- anl4_tbvps_high: 0.995 (strongly positively correlated)
- anl4_bvps_low: 0.747 (strongly positively correlated)
- anl4_bvps_median: 0.747 (strongly positively correlated)

Redundancy cluster #29: 5 similar fields, mean |rho| 0.883 (representative: anl4_tbvps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pcr_vol_20 | option9 | -0.11 | 1.59 | +0.46 | -0.45 | yes |
| anl4_epsr_flag | analyst4 | -0.26 | 1.79 | +0.61 | -0.38 | no |
| anl4_netdebt_flag | analyst_revision | -0.13 | 1.77 | +0.49 | +0.30 | yes |
| pcr_vol_30 | option9 | -0.11 | 1.59 | +0.46 | -0.25 | yes |
| rp_css_ptg | news18 | -0.17 | 1.54 | +0.48 | +0.83 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
