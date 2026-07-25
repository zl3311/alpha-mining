---
field: fn_incremental_shares_attributable_to_share_based_payment_a
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.95
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.3222
ann_vol: 0.1457
hit_rate: 0.4996
rolling_sharpe_min: -2.129
rolling_sharpe_max: 2.217
negated_best_sharpe: 0.95
negated_best_template: neg_rank_level
negated_best_fitness: 0.63
n_negated_sims: 10
direction_gap: 0.27
---
# fn_incremental_shares_attributable_to_share_based_payment_a (fundamental2)

*Additional shares included in the calculation of diluted EPS as a result of the potentially dilutive effect of share-based payment arrangements using the treasury stock method.*

## Signal Profile
- `rank(fn_incremental_shares_attributable_to_share_based_payment_a)`: S=-0.15, F=-0.04, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_incremental_shares_attributable_to_share_based_payment_a / close)`: S=0.22, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))`: S=0.68, F=0.37, T=34.1%, INFERIOR (TOP1000)
- `-rank(fn_incremental_shares_attributable_to_share_based_payment_a)`: S=0.34, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))`: S=-0.49, F=-0.25, T=33.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_incremental_shares_attributable_to_share_based_payment_a, 22)`: S=0.46, F=0.33, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(fn_incremental_shares_attributable_to_share_based_payment_a, 10)`: S=-0.29, F=-0.14, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_incremental_shares_attributable_to_share_based_payment_a, 22))`: S=0.56, F=0.35, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_a)`: S=0.95, F=0.63, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_a / close)`: S=0.65, F=0.35, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.93 (strong), ret=+27.0%
  - 2020: S=-0.38 (negative), ret=-5.9%
  - 2021: S=0.69 (moderate), ret=+9.7%
  - 2022: S=0.01 (weak), ret=+0.1%
  - 2023: S=1.53 (strong), ret=+18.5%

## Risk & Drawdown
- Max drawdown: 32.22% over 484 days (recovered)
- Annualized: return +10.1%, volatility 14.6% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.05, excess kurtosis +3.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.13, max 2.22, latest 1.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +14.18%; worst month: -5.22%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.59
- Sideways: S=1.21
- Bear: S=0.34

## Negated Direction
Best negated: `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_a)` S=0.95, F=0.63, INFERIOR
Direction gap: +0.27 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_a)`: S=0.95, F=0.63, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_incremental_shares_attributable_to_share_based_payment_a / close)`: S=0.65, F=0.35, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))`: S=-0.49, F=-0.25, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))` | TOP1000 | 0.69 | 0.37 | 32.2% | 80% | mixed |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))` | TOP500 | 0.56 | 0.29 | 41.2% | 80% | all-weather |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))` | TOP3000 | 0.50 | 0.21 | 26.0% | 60% | mixed |
| `rank(ts_delta(fn_incremental_shares_attributable_to_share_based_payment_a, 5))` | TOP200 | 0.33 | 0.18 | 68.8% | 60% | mixed |
| `rank(fn_incremental_shares_attributable_to_share_based_payment_a / close)` | TOP3000 | 0.21 | 0.05 | 5.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_avg_diluted_sharesout_adj_a: 0.221 (weakly positively correlated)
- fn_comp_options_grants_fair_value_a: -0.129 (weakly negatively correlated)
- min_sg_and_a_expense_guidance: 0.128 (weakly positively correlated)
- selling_general_admin_expense_max_guidance_qtr: 0.128 (weakly positively correlated)
- fnd2_a_ltrmdmrepopliny5: -0.125 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
