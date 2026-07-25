---
field: fnd6_txndb
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.85
best_fitness: 0.71
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 11
max_drawdown: 0.262
ann_vol: 0.2296
hit_rate: 0.4899
rolling_sharpe_min: -1.095
rolling_sharpe_max: 2.818
top_merge_partner: multi_factor_static_score_derivative
negated_best_sharpe: -0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.91
---
# fnd6_txndb (fundamental6)

*Net Deferred Tax Asset (Liab) - Total*

## Signal Profile
- `rank(fnd6_txndb)`: S=1.04, F=0.54, T=2.3%, INFERIOR (TOP1000)
- `rank(fnd6_txndb / close)`: S=0.88, F=0.44, T=2.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_txndb, 5))`: S=0.85, F=0.71, T=28.4%, INFERIOR (TOP200)
- `-rank(fnd6_txndb)`: S=-1.04, F=-0.54, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndb, 5))`: S=-0.33, F=-0.11, T=40.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txndb, 63)`: S=0.02, F=0.00, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txndb, 10)`: S=0.27, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txndb, 22))`: S=-0.13, F=-0.03, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndb)`: S=-0.19, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndb / close)`: S=-0.06, F=-0.01, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=-0.39 (negative), ret=-6.7%
  - 2021: S=1.77 (strong), ret=+52.0%
  - 2022: S=1.18 (moderate), ret=+37.2%
  - 2023: S=0.88 (moderate), ret=+12.7%

## Risk & Drawdown
- Max drawdown: 26.20% over 135 days (recovered)
- Annualized: return +19.4%, volatility 23.0% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew -0.21, excess kurtosis +27.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.82, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +22.17%; worst month: -9.83%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.64
- Sideways: S=1.32
- Bear: S=0.87

## Negated Direction
Best negated: `rank(-1 * fnd6_txndb / close)` S=-0.06, F=-0.01, INFERIOR
Direction gap: -0.91 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txndb)`: S=-0.19, F=-0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndb / close)`: S=-0.06, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndb, 5))`: S=-0.33, F=-0.11, T=40.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txndb, 5))` | TOP200 | 0.85 | 0.71 | 26.2% | 80% | all-weather |
| `rank(fnd6_txndb)` | TOP1000 | 1.04 | 0.54 | 4.6% | 80% | mixed |
| `rank(fnd6_txndb / close)` | TOP1000 | 0.87 | 0.44 | 5.2% | 80% | all-weather |
| `rank(ts_delta(fnd6_txndb, 5))` | TOP500 | 0.55 | 0.31 | 29.8% | 40% | mixed |
| `rank(fnd6_txndb)` | TOP500 | 0.61 | 0.28 | 6.5% | 80% | all-weather |
| `rank(fnd6_txndb)` | TOP200 | 0.36 | 0.17 | 10.3% | 60% | mixed |
| `rank(fnd6_txndb / close)` | TOP200 | 0.36 | 0.17 | 9.6% | 80% | mixed |
| `rank(ts_delta(fnd6_txndb, 5))` | TOP3000 | 0.34 | 0.12 | 18.1% | 80% | weak |
| `rank(ts_delta(fnd6_txndb, 5))` | TOP1000 | 0.26 | 0.08 | 22.8% | 40% | weak |
| `rank(fnd6_txndb / close)` | TOP500 | 0.26 | 0.08 | 9.7% | 80% | mixed |
| `rank(fnd6_txndb)` | TOP3000 | 0.21 | 0.04 | 5.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_fca: -0.406 (moderately negatively correlated)
- fnd6_newa1v1300_ibc: 0.376 (weakly positively correlated)
- fnd6_newa1v1300_ebit: 0.348 (weakly positively correlated)
- fnd6_newa2v1300_oiadp: 0.348 (weakly positively correlated)
- ebit: 0.347 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.08 | 1.24 | +0.39 | -0.90 | yes |
| growth_potential_rank_derivative | model16 | -0.08 | 1.27 | +0.38 | -0.94 | yes |
| analyst_revision_rank_derivative | model16 | -0.08 | 1.30 | +0.37 | -0.96 | yes |
| relative_valuation_rank_derivative | model16 | -0.08 | 1.30 | +0.37 | -0.96 | yes |
| earnings_certainty_rank_derivative | model16 | -0.08 | 1.30 | +0.37 | -0.96 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
