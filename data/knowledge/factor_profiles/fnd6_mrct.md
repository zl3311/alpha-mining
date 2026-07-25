---
field: fnd6_mrct
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.52
best_fitness: 1.33
best_universe: TOP1000
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.198
ann_vol: 0.2041
hit_rate: 0.5223
rolling_sharpe_min: -0.228
rolling_sharpe_max: 2.866
top_merge_partner: fnd6_city
redundancy_cluster: 6
negated_best_sharpe: -0.44
negated_best_template: rank_neg_delta
negated_best_fitness: -0.19
n_negated_sims: 4
direction_gap: -1.96
---
# fnd6_mrct (fundamental6)

*Rental Commitments - Minimum - 5-Year Total*

## Signal Profile
- `rank(fnd6_mrct)`: S=0.87, F=0.68, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mrct / close)`: S=0.87, F=0.64, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mrct, 5))`: S=1.52, F=1.33, T=40.3%, AVERAGE (TOP1000)
- `-rank(fnd6_mrct)`: S=-0.42, F=-0.25, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrct, 5))`: S=-0.44, F=-0.19, T=43.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mrct, 63)`: S=-0.02, F=0.00, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mrct, 10)`: S=0.39, F=0.21, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mrct, 22))`: S=1.20, F=1.00, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrct)`: S=-0.87, F=-0.68, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrct / close)`: S=-0.87, F=-0.64, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 22F/4P
- LOW_SHARPE: 23F/3P
- LOW_SUB_UNIVERSE_SHARPE: 17F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.90 (strong), ret=+48.8%
  - 2020: S=1.00 (moderate), ret=+15.8%
  - 2021: S=2.07 (strong), ret=+43.8%
  - 2022: S=2.15 (strong), ret=+46.1%
  - 2023: S=-0.10 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 19.80% over 215 days (recovered)
- Annualized: return +31.2%, volatility 20.4% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +2.27, excess kurtosis +25.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.23, max 2.87, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +26.99%; worst month: -6.41%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.96
- Sideways: S=1.58
- Bear: S=1.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mrct, 5))` S=-0.44, F=-0.19, INFERIOR
Direction gap: -1.96 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mrct)`: S=-0.87, F=-0.68, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mrct / close)`: S=-0.87, F=-0.64, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mrct, 5))`: S=-0.44, F=-0.19, T=43.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mrct, 5))` | TOP1000 | 1.53 | 1.33 | 19.8% | 80% | all-weather |
| `rank(ts_delta(fnd6_mrct, 5))` | TOP500 | 1.01 | 0.85 | 26.0% | 80% | all-weather |
| `rank(fnd6_mrct)` | TOP3000 | 0.87 | 0.68 | 17.6% | 80% | bull-only |
| `rank(fnd6_mrct / close)` | TOP3000 | 0.87 | 0.64 | 8.4% | 100% | all-weather |
| `rank(ts_delta(fnd6_mrct, 5))` | TOP200 | 0.48 | 0.30 | 37.2% | 80% | mixed |
| `rank(fnd6_mrct)` | TOP1000 | 0.42 | 0.25 | 25.0% | 60% | bull-only |
| `rank(fnd6_mrct / close)` | TOP1000 | 0.44 | 0.25 | 8.9% | 100% | bull-only |
| `rank(ts_delta(fnd6_mrct, 5))` | TOP3000 | 0.48 | 0.21 | 39.0% | 80% | mixed |
| `rank(fnd6_mrct / close)` | TOP500 | 0.20 | 0.08 | 17.0% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mrc1: 0.708 (strongly positively correlated)
- fnd6_mrcta: 0.320 (weakly positively correlated)
- fnd6_ivstch: 0.187 (weakly positively correlated)
- anl4_ebitda_number: 0.163 (weakly positively correlated)
- fnd6_txpd: 0.157 (weakly positively correlated)

Redundancy cluster #6: 2 similar fields, mean |rho| 0.708 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_city | fundamental_rare_event | -0.00 | 2.16 | +0.60 | +0.29 | yes |
| fn_assets_fair_val_a | fundamental2 | +0.03 | 2.05 | +0.52 | -0.38 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.04 | 2.09 | +0.47 | -0.90 | yes |
| news_mins_3_pct_dn | news12 | -0.04 | 2.07 | +0.54 | +0.02 | yes |
| news_mins_4_pct_dn | news12 | -0.04 | 2.06 | +0.53 | -0.10 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
