---
field: reporting_currency_code_9
dataset: analyst4
best_template: rank_level
best_sharpe: 0.84
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.2201
ann_vol: 0.1356
hit_rate: 0.5336
rolling_sharpe_min: -0.84
rolling_sharpe_max: 2.547
top_merge_partner: multi_factor_static_score_derivative
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.7
n_negated_sims: 10
direction_gap: 0.03
---
# reporting_currency_code_9 (analyst4)

*Home currency of instrument*

## Signal Profile
- `rank(reporting_currency_code_9)`: S=0.84, F=0.80, T=2.7%, INFERIOR (TOP3000)
- `rank(reporting_currency_code_9 / close)`: S=0.52, F=0.34, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(reporting_currency_code_9, 5))`: S=0.12, F=0.06, T=12.9%, INFERIOR (TOP200)
- `-rank(reporting_currency_code_9)`: S=-0.45, F=-0.37, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(reporting_currency_code_9, 5))`: S=0.87, F=0.70, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(reporting_currency_code_9, 63)`: S=0.16, F=0.11, T=13.1%, INFERIOR (TOP3000)
- `ts_mean(reporting_currency_code_9, 10)`: S=0.52, F=0.45, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(reporting_currency_code_9, 22))`: S=-0.32, F=-0.22, T=17.6%, INFERIOR (TOP3000)
- `rank(-1 * reporting_currency_code_9)`: S=-0.84, F=-0.80, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * reporting_currency_code_9 / close)`: S=-0.17, F=-0.07, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.82, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.79 (strong), ret=+12.6%
  - 2020: S=0.70 (moderate), ret=+6.9%
  - 2021: S=1.36 (moderate), ret=+20.9%
  - 2022: S=0.14 (weak), ret=+2.9%
  - 2023: S=1.14 (moderate), ret=+11.2%

## Risk & Drawdown
- Max drawdown: 22.01% over 220 days (recovered)
- Annualized: return +11.1%, volatility 13.6% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew -1.51, excess kurtosis +18.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.55, latest 1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +13.02%; worst month: -11.74%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.79
- Sideways: S=0.82
- Bear: S=0.97

## Negated Direction
Best negated: `rank(-1 * ts_delta(reporting_currency_code_9, 5))` S=0.87, F=0.70, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * reporting_currency_code_9)`: S=-0.84, F=-0.80, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * reporting_currency_code_9 / close)`: S=-0.17, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(reporting_currency_code_9, 5))`: S=0.87, F=0.70, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(reporting_currency_code_9)` | TOP3000 | 0.82 | 0.80 | 22.0% | 100% | all-weather |
| `rank(reporting_currency_code_9)` | TOP500 | 0.55 | 0.58 | 47.2% | 100% | mixed |
| `rank(reporting_currency_code_9)` | TOP1000 | 0.45 | 0.37 | 36.7% | 80% | all-weather |
| `rank(reporting_currency_code_9 / close)` | TOP200 | 0.53 | 0.34 | 15.8% | 100% | mixed |
| `rank(reporting_currency_code_9 / close)` | TOP500 | 0.51 | 0.30 | 18.6% | 80% | bear-only |
| `rank(reporting_currency_code_9)` | TOP200 | 0.25 | 0.23 | 66.4% | 60% | weak |
| `rank(reporting_currency_code_9 / close)` | TOP1000 | 0.34 | 0.17 | 23.1% | 60% | bear-only |
| `rank(reporting_currency_code_9 / close)` | TOP3000 | 0.17 | 0.07 | 42.9% | 40% | bear-only |
| `rank(ts_delta(reporting_currency_code_9, 5))` | TOP200 | 0.11 | 0.06 | 48.7% | 20% | bull-only |
| `rank(ts_delta(reporting_currency_code_9, 5))` | TOP500 | 0.05 | 0.02 | 53.3% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_totassets_flag: 0.771 (strongly positively correlated)
- anl4_cff_flag: 0.726 (strongly positively correlated)
- anl4_cfi_flag: 0.722 (strongly positively correlated)
- anl4_fcfps_flag: 0.687 (moderately positively correlated)
- anl4_tot_gw_ft: 0.684 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.33 | 1.39 | +0.55 | -0.28 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.30 | 1.37 | +0.51 | -0.69 | yes |
| cashflow_efficiency_rank_derivative | model16 | -0.33 | 1.36 | +0.54 | -0.34 | yes |
| growth_potential_rank_derivative | model16 | -0.33 | 1.44 | +0.55 | -0.20 | yes |
| relative_valuation_rank_derivative | model16 | -0.33 | 1.48 | +0.55 | -0.12 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
