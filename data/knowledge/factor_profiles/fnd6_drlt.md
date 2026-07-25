---
field: fnd6_drlt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.46
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 31
regime_profile: all-weather
n_variations_with_pnl: 13
max_drawdown: 0.0296
ann_vol: 0.0308
hit_rate: 0.536
rolling_sharpe_min: -0.232
rolling_sharpe_max: 3.135
top_merge_partner: fnd6_rank
redundancy_cluster: 8
negated_best_sharpe: 0.04
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -1.42
---
# fnd6_drlt (fundamental6)

*Deferred Revenue - Long-term*

## Signal Profile
- `rank(fnd6_drlt)`: S=1.24, F=0.71, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_drlt / close)`: S=1.46, F=0.87, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_drlt, 5))`: S=0.58, F=0.40, T=22.8%, INFERIOR (TOP200)
- `ts_decay_linear(rank(fnd6_drlt), 5)`: S=1.24, F=0.71, T=1.1%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_drlt), ts_std_dev(returns,20)<0.01)`: S=1.24, F=0.73, T=1.7%, INFERIOR (TOP3000)
- `-rank(fnd6_drlt)`: S=-0.74, F=-0.37, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_drlt, 5))`: S=0.04, F=0.01, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_drlt, 63)`: S=0.44, F=0.32, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_drlt, 10)`: S=0.29, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_drlt, 22))`: S=-0.14, F=-0.05, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drlt)`: S=-1.24, F=-0.71, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drlt / close)`: S=-1.46, F=-0.87, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/20P
- LOW_FITNESS: 31F/0P
- LOW_SHARPE: 29F/2P
- LOW_SUB_UNIVERSE_SHARPE: 17F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.45, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.33 (moderate), ret=+3.3%
  - 2020: S=2.26 (strong), ret=+6.7%
  - 2021: S=2.16 (strong), ret=+7.5%
  - 2022: S=1.14 (moderate), ret=+3.6%
  - 2023: S=0.29 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 2.96% over 151 days (not yet recovered, ongoing at window end)
- Annualized: return +4.5%, volatility 3.1% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew +0.16, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.23, max 3.13, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +2.15%; worst month: -2.18%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.54
- Sideways: S=0.86
- Bear: S=0.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_drlt, 5))` S=0.04, F=0.01, INFERIOR
Direction gap: -1.42 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_drlt)`: S=-1.24, F=-0.71, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drlt / close)`: S=-1.46, F=-0.87, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_drlt, 5))`: S=0.04, F=0.01, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_drlt / close)` | TOP3000 | 1.45 | 0.87 | 3.0% | 100% | all-weather |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_drlt), ts_std_dev(returns,20)<0.01)` | TOP3000 | 1.24 | 0.73 | 3.6% | 100% | mixed |
| `rank(fnd6_drlt)` | TOP3000 | 1.23 | 0.71 | 3.6% | 100% | mixed |
| `ts_decay_linear(rank(fnd6_drlt), 5)` | TOP3000 | 1.23 | 0.71 | 3.6% | 100% | mixed |
| `rank(fnd6_drlt / close)` | TOP1000 | 0.84 | 0.44 | 4.9% | 80% | mixed |
| `rank(ts_delta(fnd6_drlt, 5))` | TOP200 | 0.58 | 0.40 | 36.2% | 80% | weak |
| `rank(fnd6_drlt)` | TOP1000 | 0.72 | 0.37 | 5.0% | 80% | bull-only |
| `rank(fnd6_drlt / close)` | TOP500 | 0.56 | 0.29 | 8.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_drlt, 5))` | TOP1000 | 0.52 | 0.27 | 39.4% | 60% | mixed |
| `rank(fnd6_drlt)` | TOP200 | 0.38 | 0.19 | 11.5% | 60% | bull-only |
| `rank(fnd6_drlt)` | TOP500 | 0.42 | 0.19 | 8.8% | 60% | bull-only |
| `rank(fnd6_drlt / close)` | TOP200 | 0.36 | 0.17 | 12.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_drlt, 5))` | TOP500 | 0.19 | 0.07 | 52.7% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_drltq: 0.914 (strongly positively correlated)
- fnd6_drc: 0.632 (moderately positively correlated)
- fnd6_newqv1300_drcq: 0.625 (moderately positively correlated)
- fnd6_newa1v1300_aol2: 0.435 (moderately positively correlated)
- fnd6_newa1v1300_caps: 0.429 (moderately positively correlated)

Redundancy cluster #8: 2 similar fields, mean |rho| 0.914 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_rank | fundamental6 | -0.12 | 1.96 | +0.50 | -0.51 | yes |
| fnd6_ivaco | fundamental_investment | -0.01 | 2.00 | +0.55 | +0.47 | yes |
| implied_volatility_call_90 | option8 | +0.03 | 1.98 | +0.52 | +0.77 | yes |
| implied_volatility_put_60 | option8 | +0.05 | 2.01 | +0.49 | +0.73 | yes |
| implied_volatility_call_270 | option8 | +0.06 | 1.95 | +0.49 | +0.57 | yes |

## Actionability
Already in submitted book (alpha: ['0mzQQvX8']).
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
