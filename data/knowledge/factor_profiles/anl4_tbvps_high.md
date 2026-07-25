---
field: anl4_tbvps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.09
best_fitness: 0.84
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0853
ann_vol: 0.0677
hit_rate: 0.5158
rolling_sharpe_min: -0.932
rolling_sharpe_max: 3.314
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 29
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -1.0
---
# anl4_tbvps_high (analyst4)

*Tangible Book Value per Share - The highest estimation*

## Signal Profile
- `rank(anl4_tbvps_high)`: S=0.59, F=0.35, T=2.1%, INFERIOR (TOP500)
- `rank(anl4_tbvps_high / close)`: S=1.09, F=0.84, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_tbvps_high, 5))`: S=0.45, F=0.13, T=36.0%, INFERIOR (TOP3000)
- `-rank(anl4_tbvps_high)`: S=-0.16, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_high, 5))`: S=0.09, F=0.02, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_tbvps_high, 63)`: S=0.33, F=0.12, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_tbvps_high, 10)`: S=-0.22, F=-0.11, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_tbvps_high, 22))`: S=-0.24, F=-0.08, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_high)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_high / close)`: S=0.03, F=0.00, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.09, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.22 (negative), ret=-1.0%
  - 2020: S=1.25 (moderate), ret=+12.0%
  - 2021: S=1.98 (strong), ret=+10.2%
  - 2022: S=1.83 (strong), ret=+9.9%
  - 2023: S=0.72 (moderate), ret=+5.1%

## Risk & Drawdown
- Max drawdown: 8.53% over 194 days (recovered)
- Annualized: return +7.4%, volatility 6.8% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.62, excess kurtosis +5.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 3.31, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.98%; worst month: -3.25%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.03
- Sideways: S=0.39
- Bear: S=0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_tbvps_high, 5))` S=0.09, F=0.02, INFERIOR
Direction gap: -1.00 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_tbvps_high)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_tbvps_high / close)`: S=0.03, F=0.00, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_tbvps_high, 5))`: S=0.09, F=0.02, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_tbvps_high / close)` | TOP3000 | 1.09 | 0.84 | 8.5% | 80% | all-weather |
| `rank(anl4_tbvps_high / close)` | TOP500 | 0.86 | 0.71 | 17.8% | 60% | mixed |
| `rank(anl4_tbvps_high / close)` | TOP1000 | 0.66 | 0.43 | 9.4% | 80% | all-weather |
| `rank(anl4_tbvps_high)` | TOP500 | 0.58 | 0.35 | 15.2% | 60% | mixed |
| `rank(ts_delta(anl4_tbvps_high, 5))` | TOP3000 | 0.44 | 0.13 | 10.6% | 60% | mixed |
| `rank(anl4_tbvps_high)` | TOP1000 | 0.13 | 0.05 | 10.6% | 40% | bull-only |
| `rank(ts_delta(anl4_tbvps_high, 5))` | TOP1000 | 0.16 | 0.04 | 18.9% | 60% | bull-only |
| `rank(anl4_tbvps_high)` | TOP3000 | 0.09 | 0.02 | 5.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_tbvps_median: 0.999 (strongly positively correlated)
- anl4_tbvps_mean: 0.999 (strongly positively correlated)
- anl4_tbvps_low: 0.995 (strongly positively correlated)
- anl4_bvps_median: 0.756 (strongly positively correlated)
- anl4_bvps_mean: 0.756 (strongly positively correlated)

Redundancy cluster #29: 5 similar fields, mean |rho| 0.883 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.27 | 1.83 | +0.65 | -0.43 | no |
| pcr_vol_20 | option9 | -0.10 | 1.61 | +0.48 | -0.46 | yes |
| anl4_netdebt_flag | analyst_revision | -0.12 | 1.79 | +0.51 | +0.30 | yes |
| pcr_vol_30 | option9 | -0.11 | 1.61 | +0.48 | -0.28 | yes |
| anl4_cfi_flag | analyst_revision | -0.02 | 1.61 | +0.44 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
