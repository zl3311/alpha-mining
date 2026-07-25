---
field: fnd6_newa1v1300_aocipen
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.99
best_fitness: 0.81
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2126
ann_vol: 0.1865
hit_rate: 0.5255
rolling_sharpe_min: 0.113
rolling_sharpe_max: 2.695
top_merge_partner: fn_income_taxes_paid_q
negated_best_sharpe: 0.66
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.33
---
# fnd6_newa1v1300_aocipen (fundamental6)

*Accum Other Comp Inc - Min Pension Liab Adj*

## Signal Profile
- `rank(fnd6_newa1v1300_aocipen)`: S=0.27, F=0.15, T=3.4%, INFERIOR (TOP200)
- `rank(fnd6_newa1v1300_aocipen / close)`: S=0.27, F=0.15, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa1v1300_aocipen, 5))`: S=0.99, F=0.81, T=27.3%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_aocipen)`: S=0.25, F=0.10, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aocipen, 5))`: S=-0.44, F=-0.18, T=39.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_aocipen, 22)`: S=0.13, F=0.04, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aocipen, 10)`: S=-0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aocipen, 22))`: S=0.24, F=0.09, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocipen)`: S=0.54, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocipen / close)`: S=0.66, F=0.37, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.99, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+20.7%
  - 2020: S=1.37 (moderate), ret=+36.7%
  - 2021: S=0.23 (weak), ret=+4.9%
  - 2022: S=2.13 (strong), ret=+21.9%
  - 2023: S=0.63 (moderate), ret=+6.3%

## Risk & Drawdown
- Max drawdown: 21.26% over 253 days (recovered)
- Annualized: return +18.5%, volatility 18.6% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +1.15, excess kurtosis +31.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.11, max 2.69, latest 0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +23.58%; worst month: -8.77%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.04
- Sideways: S=1.20
- Bear: S=-0.34

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_aocipen / close)` S=0.66, F=0.37, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aocipen)`: S=0.54, F=0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aocipen / close)`: S=0.66, F=0.37, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aocipen, 5))`: S=-0.44, F=-0.18, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_aocipen, 5))` | TOP500 | 0.99 | 0.81 | 21.3% | 100% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_aocipen, 5))` | TOP200 | 0.59 | 0.39 | 21.0% | 100% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_aocipen, 5))` | TOP3000 | 0.59 | 0.28 | 16.8% | 80% | mixed |
| `rank(fnd6_newa1v1300_aocipen)` | TOP200 | 0.28 | 0.15 | 41.8% | 60% | bear-only |
| `rank(fnd6_newa1v1300_aocipen / close)` | TOP200 | 0.29 | 0.15 | 41.8% | 60% | bear-only |
| `rank(ts_delta(fnd6_newa1v1300_aocipen, 5))` | TOP1000 | 0.30 | 0.10 | 33.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_reajo: 0.446 (moderately positively correlated)
- fnd6_ds: 0.299 (weakly positively correlated)
- fnd6_newa1v1300_dcom: 0.185 (weakly positively correlated)
- historical_volatility_150: -0.174 (weakly negatively correlated)
- parkinson_volatility_150: -0.173 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_income_taxes_paid_q | fundamental2 | -0.01 | 1.35 | +0.36 | -0.73 | yes |
| sharesout | pv1 | -0.04 | 1.41 | +0.37 | -0.61 | yes |
| fn_incremental_shares_attributable_to_share_based_payment_q | fundamental2 | +0.01 | 1.48 | +0.36 | -0.73 | yes |
| anl4_rd_exp_flag | analyst4 | -0.09 | 1.42 | +0.39 | -0.20 | yes |
| pv13_revere_company_total | pv13 | +0.04 | 1.42 | +0.36 | -0.49 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
