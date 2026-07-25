---
field: fnd6_optosby
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.02
best_fitness: 0.74
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.2128
ann_vol: 0.19
hit_rate: 0.5045
rolling_sharpe_min: -0.973
rolling_sharpe_max: 2.644
top_merge_partner: fn_assets_fair_val_l3_a
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.04
---
# fnd6_optosby (fundamental6)

*Options Outstanding - Beginning of Year*

## Signal Profile
- `rank(fnd6_optosby)`: S=0.66, F=0.46, T=3.4%, INFERIOR (TOP200)
- `rank(fnd6_optosby / close)`: S=0.73, F=0.56, T=3.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optosby, 5))`: S=1.02, F=0.74, T=37.1%, INFERIOR (TOP1000)
- `-rank(fnd6_optosby)`: S=-0.39, F=-0.15, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optosby, 5))`: S=-0.53, F=-0.26, T=40.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optosby, 22)`: S=0.09, F=0.03, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optosby, 10)`: S=0.66, F=0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optosby, 22))`: S=0.15, F=0.05, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosby)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosby / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.08 (moderate), ret=+22.4%
  - 2020: S=1.42 (moderate), ret=+23.2%
  - 2021: S=1.43 (moderate), ret=+28.8%
  - 2022: S=1.58 (strong), ret=+34.0%
  - 2023: S=-0.98 (negative), ret=-13.1%

## Risk & Drawdown
- Max drawdown: 21.28% over 268 days (not yet recovered, ongoing at window end)
- Annualized: return +19.5%, volatility 19.0% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +1.72, excess kurtosis +23.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 2.64, latest -0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +25.55%; worst month: -8.17%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.87
- Sideways: S=0.86
- Bear: S=0.47

## Negated Direction
Best negated: `rank(-1 * fnd6_optosby / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.04 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optosby)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosby / close)`: S=-0.02, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optosby, 5))`: S=-0.53, F=-0.26, T=40.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_optosby, 5))` | TOP1000 | 1.02 | 0.74 | 21.3% | 80% | mixed |
| `rank(fnd6_optosby / close)` | TOP200 | 0.74 | 0.56 | 10.3% | 80% | mixed |
| `rank(fnd6_optosby / close)` | TOP500 | 0.75 | 0.48 | 15.6% | 80% | mixed |
| `rank(fnd6_optosby)` | TOP200 | 0.68 | 0.46 | 15.7% | 60% | all-weather |
| `rank(fnd6_optosby)` | TOP500 | 0.72 | 0.41 | 10.2% | 80% | mixed |
| `rank(ts_delta(fnd6_optosby, 5))` | TOP3000 | 0.53 | 0.26 | 30.2% | 80% | mixed |
| `rank(fnd6_optosby / close)` | TOP1000 | 0.46 | 0.23 | 15.9% | 60% | bear-only |
| `rank(ts_delta(fnd6_optosby, 5))` | TOP500 | 0.32 | 0.16 | 30.3% | 80% | mixed |
| `rank(fnd6_optosby)` | TOP1000 | 0.39 | 0.15 | 10.6% | 40% | mixed |
| `rank(ts_delta(fnd6_optosby, 5))` | TOP200 | 0.18 | 0.08 | 44.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_mrc1: 0.169 (weakly positively correlated)
- fnd6_txndb: 0.136 (weakly positively correlated)
- fnd6_mrct: 0.129 (weakly positively correlated)
- fnd6_newa1v1300_acominc: 0.114 (weakly positively correlated)
- fnd6_ivao: -0.114 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l3_a | fundamental2 | +0.02 | 1.43 | +0.41 | -0.82 | yes |
| sharesout | pv1 | -0.08 | 1.46 | +0.43 | -0.49 | yes |
| pv13_revere_company_total | pv13 | +0.01 | 1.47 | +0.41 | -0.61 | yes |
| fn_income_taxes_paid_q | fundamental2 | -0.04 | 1.40 | +0.38 | -0.77 | yes |
| fn_comp_options_exercisable_number_a | fundamental2 | -0.02 | 1.37 | +0.34 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
