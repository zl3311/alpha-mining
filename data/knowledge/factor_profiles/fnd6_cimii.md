---
field: fnd6_cimii
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.81
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.3474
ann_vol: 0.1988
hit_rate: 0.5263
rolling_sharpe_min: -0.943
rolling_sharpe_max: 2.91
top_merge_partner: news_mins_5_pct_up
negated_best_sharpe: 0.17
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.64
---
# fnd6_cimii (fundamental6)

*Comprehensive Income - Noncontrolling Interest*

## Signal Profile
- `rank(fnd6_cimii)`: S=0.42, F=0.20, T=3.0%, INFERIOR (TOP200)
- `rank(fnd6_cimii / close)`: S=0.42, F=0.20, T=3.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cimii, 5))`: S=0.81, F=0.54, T=36.1%, INFERIOR (TOP3000)
- `-rank(fnd6_cimii)`: S=0.17, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cimii, 5))`: S=-0.46, F=-0.24, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cimii, 63)`: S=0.26, F=0.16, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cimii, 10)`: S=-0.47, F=-0.23, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cimii, 22))`: S=0.23, F=0.09, T=19.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cimii)`: S=0.17, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cimii / close)`: S=0.13, F=0.03, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+5.1%
  - 2020: S=2.17 (strong), ret=+36.6%
  - 2021: S=-0.09 (negative), ret=-2.3%
  - 2022: S=0.34 (weak), ret=+6.1%
  - 2023: S=2.26 (strong), ret=+33.8%

## Risk & Drawdown
- Max drawdown: 34.74% over 947 days (recovered)
- Annualized: return +16.2%, volatility 19.9% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.14, excess kurtosis +38.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 2.91, latest 2.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +16.12%; worst month: -22.72%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.85
- Sideways: S=-0.04
- Bear: S=1.89

## Negated Direction
Best negated: `-rank(fnd6_cimii)` S=0.17, F=0.04, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cimii)`: S=0.17, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cimii / close)`: S=0.13, F=0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cimii, 5))`: S=-0.46, F=-0.24, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cimii, 5))` | TOP3000 | 0.81 | 0.54 | 34.7% | 80% | all-weather |
| `rank(ts_delta(fnd6_cimii, 5))` | TOP1000 | 0.46 | 0.24 | 26.7% | 80% | all-weather |
| `rank(fnd6_cimii / close)` | TOP200 | 0.42 | 0.20 | 11.0% | 60% | bull-only |
| `rank(fnd6_cimii)` | TOP200 | 0.41 | 0.20 | 11.2% | 60% | bull-only |
| `rank(fnd6_cimii / close)` | TOP3000 | 0.21 | 0.06 | 13.9% | 60% | bull-only |
| `rank(fnd6_cimii)` | TOP3000 | 0.15 | 0.04 | 15.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma2_recch: -0.203 (weakly negatively correlated)
- fnd6_newa1v1300_aoloch: -0.168 (weakly negatively correlated)
- fnd6_mfma1_aoloch: -0.168 (weakly negatively correlated)
- fnd6_acdo: 0.119 (weakly positively correlated)
- fnd2_a_eplsbvdcpcstnrgprg: -0.117 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_5_pct_up | news12 | -0.04 | 1.16 | +0.32 | -0.77 | yes |
| rp_ess_insider | news18 | +0.00 | 1.16 | +0.33 | -0.62 | yes |
| fnd2_ebitfr | fundamental2 | +0.00 | 1.20 | +0.31 | -0.68 | yes |
| pv13_revere_key_sector_total | pv13 | +0.04 | 1.15 | +0.30 | -0.76 | yes |
| min_tangible_book_value_per_share_guidance | analyst4 | +0.00 | 1.15 | +0.32 | -0.50 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
