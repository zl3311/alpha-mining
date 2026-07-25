---
field: fnd6_drc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.27
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0534
ann_vol: 0.0413
hit_rate: 0.5255
rolling_sharpe_min: -0.595
rolling_sharpe_max: 3.671
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 19
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -1.07
---
# fnd6_drc (fundamental6)

*Deferred Revenue - Current*

## Signal Profile
- `rank(fnd6_drc)`: S=0.95, F=0.60, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_drc / close)`: S=1.27, F=0.82, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_drc, 5))`: S=0.36, F=0.16, T=34.0%, INFERIOR (TOP500)
- `-rank(fnd6_drc)`: S=-0.50, F=-0.28, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_drc, 5))`: S=0.20, F=0.07, T=31.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_drc, 22)`: S=-0.21, F=-0.09, T=23.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_drc, 10)`: S=0.06, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_drc, 22))`: S=0.07, F=0.02, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drc)`: S=-0.04, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drc / close)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.27, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.02 (weak), ret=+0.1%
  - 2020: S=2.22 (strong), ret=+8.0%
  - 2021: S=2.20 (strong), ret=+10.2%
  - 2022: S=1.38 (moderate), ret=+6.8%
  - 2023: S=0.16 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 5.34% over 286 days (recovered)
- Annualized: return +5.2%, volatility 4.1% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.32, excess kurtosis +1.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.59, max 3.67, latest 0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.14%; worst month: -2.66%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.49
- Sideways: S=0.20
- Bear: S=0.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_drc, 5))` S=0.20, F=0.07, INFERIOR
Direction gap: -1.07 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_drc)`: S=-0.04, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_drc / close)`: S=-0.10, F=-0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_drc, 5))`: S=0.20, F=0.07, T=31.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_drc / close)` | TOP3000 | 1.27 | 0.82 | 5.3% | 100% | all-weather |
| `rank(fnd6_drc)` | TOP3000 | 0.94 | 0.60 | 6.0% | 100% | bull-only |
| `rank(fnd6_drc / close)` | TOP1000 | 0.68 | 0.41 | 7.1% | 80% | bull-only |
| `rank(fnd6_drc)` | TOP1000 | 0.49 | 0.28 | 14.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_drc, 5))` | TOP500 | 0.35 | 0.16 | 31.1% | 80% | all-weather |
| `rank(ts_delta(fnd6_drc, 5))` | TOP3000 | 0.28 | 0.09 | 24.4% | 80% | weak |
| `rank(fnd6_drc / close)` | TOP500 | 0.16 | 0.06 | 18.3% | 40% | bull-only |
| `rank(fnd6_drc / close)` | TOP200 | 0.10 | 0.03 | 21.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_drcq: 0.930 (strongly positively correlated)
- fnd6_lcox: 0.778 (strongly positively correlated)
- fnd6_newa1v1300_lco: 0.700 (moderately positively correlated)
- fnd6_newqv1300_lcoq: 0.698 (moderately positively correlated)
- liabilities_curr: 0.661 (moderately positively correlated)

Redundancy cluster #19: 2 similar fields, mean |rho| 0.93 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.15 | 1.86 | +0.59 | +0.70 | yes |
| fnd6_ivaco | fundamental_investment | -0.03 | 1.86 | +0.50 | +0.84 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.02 | 1.91 | +0.46 | -0.12 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.02 | 1.91 | +0.46 | -0.12 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.03 | 1.73 | +0.47 | -0.07 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
