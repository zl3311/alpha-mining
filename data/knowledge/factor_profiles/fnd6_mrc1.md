---
field: fnd6_mrc1
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.27
best_fitness: 1.02
best_universe: TOP1000
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.204
ann_vol: 0.2091
hit_rate: 0.515
rolling_sharpe_min: -0.658
rolling_sharpe_max: 2.541
top_merge_partner: fn_assets_fair_val_a
redundancy_cluster: 6
negated_best_sharpe: 0.12
negated_best_template: neg_rank_level
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -1.15
---
# fnd6_mrc1 (fundamental6)

*Rental Commitments - Minimum - 1st Year*

## Signal Profile
- `rank(fnd6_mrc1)`: S=0.91, F=0.73, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrc1 / close)`: S=0.92, F=0.69, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrc1, 5))`: S=1.27, F=1.02, T=41.3%, AVERAGE (TOP1000)
- `-rank(fnd6_mrc1)`: S=-0.37, F=-0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc1, 5))`: S=-0.84, F=-0.64, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrc1, 63)`: S=0.19, F=0.08, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrc1, 10)`: S=0.23, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrc1, 22))`: S=0.92, F=0.66, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc1)`: S=0.12, F=0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc1 / close)`: S=-0.09, F=-0.02, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 24F/5P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.83 (strong), ret=+42.2%
  - 2020: S=1.17 (moderate), ret=+19.5%
  - 2021: S=1.98 (strong), ret=+43.6%
  - 2022: S=1.21 (moderate), ret=+28.1%
  - 2023: S=-0.15 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 20.40% over 172 days (recovered)
- Annualized: return +26.7%, volatility 20.9% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +2.13, excess kurtosis +23.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 2.54, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +27.42%; worst month: -12.05%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.82
- Sideways: S=1.90
- Bear: S=1.00

## Negated Direction
Best negated: `rank(-1 * fnd6_mrc1)` S=0.12, F=0.04, INFERIOR
Direction gap: -1.15 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrc1)`: S=0.12, F=0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrc1 / close)`: S=-0.09, F=-0.02, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrc1, 5))`: S=-0.84, F=-0.64, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mrc1, 5))` | TOP1000 | 1.28 | 1.02 | 20.4% | 80% | all-weather |
| `rank(fnd6_mrc1)` | TOP3000 | 0.90 | 0.73 | 19.2% | 80% | bull-only |
| `rank(fnd6_mrc1 / close)` | TOP3000 | 0.91 | 0.69 | 7.8% | 100% | all-weather |
| `rank(ts_delta(fnd6_mrc1, 5))` | TOP500 | 0.76 | 0.55 | 40.9% | 80% | mixed |
| `rank(fnd6_mrc1 / close)` | TOP1000 | 0.44 | 0.25 | 10.1% | 60% | bull-only |
| `rank(fnd6_mrc1)` | TOP1000 | 0.36 | 0.21 | 29.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_mrc1, 5))` | TOP200 | 0.35 | 0.19 | 33.5% | 60% | mixed |
| `rank(fnd6_mrc1 / close)` | TOP500 | 0.09 | 0.02 | 20.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrct: 0.708 (strongly positively correlated)
- fnd6_mrcta: 0.240 (weakly positively correlated)
- fnd6_optosby: 0.169 (weakly positively correlated)
- fnd6_txpd: 0.164 (weakly positively correlated)
- fnd6_ivst: 0.149 (weakly positively correlated)

Redundancy cluster #6: 2 similar fields, mean |rho| 0.708 (representative: fnd6_mrct). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_a | fundamental2 | -0.02 | 1.91 | +0.51 | -0.63 | yes |
| news_mins_4_pct_dn | news12 | -0.05 | 1.87 | +0.57 | +0.16 | yes |
| anl4_netprofit_flag | analyst4 | -0.02 | 1.76 | +0.48 | -0.49 | yes |
| news_open_gap | news12 | -0.01 | 1.73 | +0.46 | -0.73 | yes |
| anl4_ptp_flag | analyst_revision | -0.04 | 1.96 | +0.53 | +0.07 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
