---
field: fnd6_newqv1300_drcq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.24
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.0587
ann_vol: 0.0434
hit_rate: 0.5304
rolling_sharpe_min: -0.197
rolling_sharpe_max: 3.224
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 19
negated_best_sharpe: 0.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -1.13
---
# fnd6_newqv1300_drcq (fundamental6)

*Deferred Revenue - Current*

## Signal Profile
- `rank(fnd6_newqv1300_drcq)`: S=0.98, F=0.63, T=2.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_drcq / close)`: S=1.24, F=0.81, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_drcq, 5))`: S=0.62, F=0.28, T=39.7%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_drcq)`: S=-0.50, F=-0.29, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_drcq, 5))`: S=0.11, F=0.02, T=39.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_drcq, 22)`: S=0.02, F=0.00, T=40.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_drcq, 10)`: S=0.24, F=0.11, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_drcq, 22))`: S=0.06, F=0.01, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drcq)`: S=-0.98, F=-0.63, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drcq / close)`: S=-1.24, F=-0.81, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.24, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.39 (weak), ret=+1.2%
  - 2020: S=1.73 (strong), ret=+6.4%
  - 2021: S=2.29 (strong), ret=+11.2%
  - 2022: S=1.01 (moderate), ret=+5.3%
  - 2023: S=0.58 (moderate), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 5.87% over 281 days (recovered)
- Annualized: return +5.4%, volatility 4.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.35, excess kurtosis +1.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.20, max 3.22, latest 0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.88%; worst month: -3.03%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.21
- Sideways: S=0.37
- Bear: S=0.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_drcq, 5))` S=0.11, F=0.02, INFERIOR
Direction gap: -1.13 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_drcq)`: S=-0.98, F=-0.63, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_drcq / close)`: S=-1.24, F=-0.81, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_drcq, 5))`: S=0.11, F=0.02, T=39.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_drcq / close)` | TOP3000 | 1.24 | 0.81 | 5.9% | 100% | all-weather |
| `rank(fnd6_newqv1300_drcq)` | TOP3000 | 0.97 | 0.63 | 8.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_drcq / close)` | TOP1000 | 0.67 | 0.42 | 8.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_drcq)` | TOP1000 | 0.49 | 0.29 | 17.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_drcq, 5))` | TOP500 | 0.62 | 0.28 | 16.5% | 60% | mixed |
| `rank(fnd6_newqv1300_drcq / close)` | TOP200 | 0.41 | 0.25 | 17.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_drcq)` | TOP200 | 0.36 | 0.22 | 19.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_drcq / close)` | TOP500 | 0.32 | 0.16 | 17.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_drcq, 5))` | TOP1000 | 0.31 | 0.09 | 22.9% | 60% | mixed |
| `rank(fnd6_newqv1300_drcq)` | TOP500 | 0.19 | 0.08 | 28.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_drc: 0.930 (strongly positively correlated)
- fnd6_lcox: 0.688 (moderately positively correlated)
- fnd6_newqv1300_lcoq: 0.654 (moderately positively correlated)
- fnd6_drlt: 0.625 (moderately positively correlated)
- fnd6_newa1v1300_lco: 0.619 (moderately positively correlated)

Redundancy cluster #19: 2 similar fields, mean |rho| 0.93 (representative: fnd6_drc). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.11 | 1.80 | +0.56 | +0.77 | yes |
| fnd6_ivaco | fundamental_investment | -0.12 | 1.91 | +0.55 | +0.85 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.04 | 1.72 | +0.48 | -0.15 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.04 | 1.93 | +0.47 | -0.17 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.04 | 1.93 | +0.47 | -0.17 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
