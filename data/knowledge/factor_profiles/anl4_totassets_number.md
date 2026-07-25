---
field: anl4_totassets_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 1.34
best_fitness: 0.96
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0441
ann_vol: 0.0381
hit_rate: 0.532
rolling_sharpe_min: 0.077
rolling_sharpe_max: 2.794
top_merge_partner: fn_repayments_of_debt_a
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.86
---
# anl4_totassets_number (analyst4)

*Total Assets - number of estimations*

## Signal Profile
- `rank(anl4_totassets_number)`: S=1.16, F=0.69, T=3.4%, INFERIOR (TOP1000)
- `rank(anl4_totassets_number / close)`: S=0.34, F=0.17, T=3.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_totassets_number, 5))`: S=-0.11, F=-0.01, T=36.9%, INFERIOR (TOP3000)
- `-rank(anl4_totassets_number)`: S=-1.16, F=-0.69, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_number, 5))`: S=0.48, F=0.17, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_totassets_number, 22)`: S=0.22, F=0.06, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_number, 10)`: S=1.34, F=0.96, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_number, 22))`: S=0.60, F=0.29, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_number)`: S=-0.76, F=-0.43, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_number / close)`: S=-0.21, F=-0.08, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 10F/19P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.17, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+2.1%
  - 2020: S=2.25 (strong), ret=+8.3%
  - 2021: S=0.94 (moderate), ret=+3.8%
  - 2022: S=0.61 (moderate), ret=+2.7%
  - 2023: S=1.57 (strong), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 4.41% over 123 days (recovered)
- Annualized: return +4.5%, volatility 3.8% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew -0.03, excess kurtosis +0.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.08, max 2.79, latest 1.61

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.54%; worst month: -3.34%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.61
- Sideways: S=1.04
- Bear: S=1.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totassets_number, 5))` S=0.48, F=0.17, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_totassets_number)`: S=-0.76, F=-0.43, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_number / close)`: S=-0.21, F=-0.08, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_number, 5))`: S=0.48, F=0.17, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totassets_number)` | TOP1000 | 1.17 | 0.69 | 4.4% | 100% | all-weather |
| `rank(anl4_totassets_number)` | TOP500 | 0.78 | 0.43 | 7.4% | 80% | all-weather |
| `rank(anl4_totassets_number)` | TOP3000 | 0.74 | 0.30 | 4.0% | 80% | mixed |
| `rank(anl4_totassets_number / close)` | TOP200 | 0.34 | 0.17 | 16.9% | 60% | mixed |
| `rank(anl4_totassets_number)` | TOP200 | 0.23 | 0.09 | 11.3% | 60% | mixed |
| `rank(anl4_totassets_number / close)` | TOP1000 | 0.22 | 0.09 | 26.2% | 40% | bear-only |
| `rank(anl4_totassets_number / close)` | TOP500 | 0.21 | 0.08 | 23.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfi_number: 0.545 (moderately positively correlated)
- anl4_totgw_number: 0.470 (moderately positively correlated)
- anl4_cfo_number: 0.343 (weakly positively correlated)
- anl4_cff_number: 0.297 (weakly positively correlated)
- fn_entity_common_stock_shares_out_a: -0.252 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_repayments_of_debt_a | fundamental2 | -0.07 | 1.72 | +0.53 | -0.33 | yes |
| fnd6_rank | fundamental6 | -0.09 | 1.73 | +0.55 | +0.19 | yes |
| fnd6_dxd5 | fundamental6 | +0.00 | 1.65 | +0.46 | -0.91 | yes |
| fn_taxes_payable_q | fundamental2 | -0.02 | 1.64 | +0.47 | -0.68 | yes |
| fnd6_dd5 | fundamental6 | +0.01 | 1.60 | +0.43 | -0.91 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
