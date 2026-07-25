---
field: fnd6_newqv1300_drltq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.43
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 12
max_drawdown: 0.0384
ann_vol: 0.0323
hit_rate: 0.5433
rolling_sharpe_min: -0.35
rolling_sharpe_max: 2.977
top_merge_partner: fnd6_ivaco
redundancy_cluster: 8
negated_best_sharpe: -0.41
negated_best_template: rank_neg_delta
negated_best_fitness: -0.14
n_negated_sims: 4
direction_gap: -1.84
---
# fnd6_newqv1300_drltq (fundamental6)

*Deferred Revenue - Long-term*

## Signal Profile
- `rank(fnd6_newqv1300_drltq)`: S=1.27, F=0.75, T=2.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_drltq / close)`: S=1.43, F=0.87, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_drltq, 5))`: S=0.98, F=0.65, T=40.0%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_drltq)`: S=-0.80, F=-0.43, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_drltq, 5))`: S=-0.41, F=-0.14, T=38.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_drltq, 22)`: S=0.29, F=0.11, T=38.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_drltq, 10)`: S=0.46, F=0.27, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_drltq, 22))`: S=0.36, F=0.14, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drltq)`: S=-1.27, F=-0.75, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drltq / close)`: S=-1.43, F=-0.87, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/18P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 24F/2P
- LOW_SUB_UNIVERSE_SHARPE: 12F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.43, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.44 (moderate), ret=+3.7%
  - 2020: S=1.95 (strong), ret=+6.1%
  - 2021: S=2.33 (strong), ret=+8.5%
  - 2022: S=1.17 (moderate), ret=+3.8%
  - 2023: S=0.16 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 3.84% over 151 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 3.2% (fraction of booksize)
- Hit rate: 54.3% positive days
- Tail shape: skew +0.33, excess kurtosis +2.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.35, max 2.98, latest 0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +2.54%; worst month: -2.39%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.43
- Sideways: S=0.71
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_drltq, 5))` S=-0.41, F=-0.14, INFERIOR
Direction gap: -1.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_drltq)`: S=-1.27, F=-0.75, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drltq / close)`: S=-1.43, F=-0.87, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_drltq, 5))`: S=-0.41, F=-0.14, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_drltq / close)` | TOP3000 | 1.43 | 0.87 | 3.8% | 100% | all-weather |
| `rank(fnd6_newqv1300_drltq)` | TOP3000 | 1.27 | 0.75 | 3.8% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_drltq, 5))` | TOP200 | 0.98 | 0.65 | 19.0% | 100% | all-weather |
| `rank(fnd6_newqv1300_drltq / close)` | TOP500 | 0.81 | 0.52 | 6.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_drltq / close)` | TOP1000 | 0.88 | 0.49 | 5.3% | 80% | mixed |
| `rank(fnd6_newqv1300_drltq)` | TOP1000 | 0.78 | 0.43 | 6.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_drltq, 5))` | TOP500 | 0.75 | 0.39 | 18.4% | 80% | mixed |
| `rank(fnd6_newqv1300_drltq)` | TOP500 | 0.66 | 0.38 | 8.2% | 60% | bull-only |
| `rank(fnd6_newqv1300_drltq / close)` | TOP200 | 0.53 | 0.32 | 13.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_drltq)` | TOP200 | 0.54 | 0.32 | 14.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_drltq, 5))` | TOP1000 | 0.53 | 0.22 | 27.0% | 60% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_drltq, 5))` | TOP3000 | 0.41 | 0.14 | 15.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_drlt: 0.914 (strongly positively correlated)
- fnd6_newqv1300_drcq: 0.617 (moderately positively correlated)
- fnd6_drc: 0.563 (moderately positively correlated)
- fnd6_newqv1300_capsq: 0.389 (weakly positively correlated)
- fnd6_newa1v1300_aol2: 0.378 (weakly positively correlated)

Redundancy cluster #8: 2 similar fields, mean |rho| 0.914 (representative: fnd6_drlt). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.07 | 2.04 | +0.62 | +0.50 | yes |
| fn_liab_fair_val_l2_q | fundamental2 | +0.17 | 1.85 | +0.42 | -0.92 | yes |
| min_net_income_guidance | analyst4 | +0.01 | 1.94 | +0.51 | +0.85 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.05 | 1.99 | +0.50 | +0.74 | yes |
| max_net_income_guidance | analyst4 | +0.01 | 1.93 | +0.50 | +0.85 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
