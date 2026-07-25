---
field: fn_comp_options_exercisable_number_a
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 1.2
best_fitness: 1.11
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.4491
ann_vol: 0.1694
hit_rate: 0.5142
rolling_sharpe_min: -2.124
rolling_sharpe_max: 2.961
top_merge_partner: fnd6_pnrsho
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.78
---
# fn_comp_options_exercisable_number_a (fundamental2)

*The number of shares into which fully or partially vested stock options outstanding as of the balance sheet date can be currently converted under the option plan.*

## Signal Profile
- `rank(fn_comp_options_exercisable_number_a)`: S=0.63, F=0.37, T=1.8%, INFERIOR (TOP200)
- `rank(fn_comp_options_exercisable_number_a / close)`: S=0.71, F=0.40, T=1.6%, INFERIOR (TOP500)
- `rank(ts_delta(fn_comp_options_exercisable_number_a, 5))`: S=0.88, F=0.60, T=32.5%, INFERIOR (TOP500)
- `-rank(fn_comp_options_exercisable_number_a)`: S=-0.22, F=-0.06, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercisable_number_a, 5))`: S=0.42, F=0.18, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_options_exercisable_number_a, 22)`: S=0.39, F=0.25, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_exercisable_number_a, 10)`: S=-0.35, F=-0.30, T=0.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_exercisable_number_a, 22))`: S=1.20, F=1.11, T=14.9%, AVERAGE (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_number_a)`: S=-0.19, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_number_a / close)`: S=-0.15, F=-0.05, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.88, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.80 (strong), ret=+26.0%
  - 2020: S=0.28 (weak), ret=+5.5%
  - 2021: S=0.11 (weak), ret=+1.9%
  - 2022: S=0.38 (weak), ret=+6.7%
  - 2023: S=2.56 (strong), ret=+33.4%

## Risk & Drawdown
- Max drawdown: 44.91% over 1197 days (recovered)
- Annualized: return +15.0%, volatility 16.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.52, excess kurtosis +6.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.12, max 2.96, latest 2.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +15.68%; worst month: -8.21%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.74
- Sideways: S=1.26
- Bear: S=0.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_exercisable_number_a, 5))` S=0.42, F=0.18, INFERIOR
Direction gap: -0.78 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_options_exercisable_number_a)`: S=-0.19, F=-0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_exercisable_number_a / close)`: S=-0.15, F=-0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_exercisable_number_a, 5))`: S=0.42, F=0.18, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_comp_options_exercisable_number_a, 5))` | TOP500 | 0.88 | 0.60 | 44.9% | 100% | all-weather |
| `rank(fn_comp_options_exercisable_number_a / close)` | TOP500 | 0.71 | 0.40 | 8.2% | 60% | all-weather |
| `rank(fn_comp_options_exercisable_number_a)` | TOP200 | 0.66 | 0.37 | 13.9% | 60% | all-weather |
| `rank(fn_comp_options_exercisable_number_a)` | TOP500 | 0.69 | 0.33 | 6.2% | 80% | mixed |
| `rank(fn_comp_options_exercisable_number_a / close)` | TOP200 | 0.54 | 0.30 | 11.3% | 80% | all-weather |
| `rank(ts_delta(fn_comp_options_exercisable_number_a, 5))` | TOP1000 | 0.49 | 0.22 | 42.6% | 80% | mixed |
| `rank(fn_comp_options_exercisable_number_a / close)` | TOP1000 | 0.30 | 0.12 | 14.5% | 40% | mixed |
| `rank(fn_comp_options_exercisable_number_a)` | TOP1000 | 0.23 | 0.06 | 8.3% | 40% | weak |
| `rank(fn_comp_options_exercisable_number_a)` | TOP3000 | 0.21 | 0.05 | 11.7% | 60% | bear-only |
| `rank(fn_comp_options_exercisable_number_a / close)` | TOP3000 | 0.16 | 0.05 | 28.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fn_payments_for_repurchase_of_common_stock_a: 0.135 (weakly positively correlated)
- fn_repurchased_shares_a: 0.134 (weakly positively correlated)
- fnd6_txtubpospdec: 0.126 (weakly positively correlated)
- fn_incremental_shares_attributable_to_share_based_payment_a: 0.095 (weakly positively correlated)
- fnd6_prchq: -0.094 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_pnrsho | fundamental6 | -0.03 | 1.26 | +0.38 | -0.82 | yes |
| fnd6_idit | fundamental6 | -0.07 | 1.43 | +0.36 | -0.83 | yes |
| fnd6_optprcca | fundamental6 | -0.06 | 1.23 | +0.34 | -0.89 | yes |
| fnd6_optprcwa | fundamental6 | -0.04 | 1.24 | +0.35 | -0.86 | yes |
| fnd6_optosby | fundamental6 | -0.02 | 1.37 | +0.34 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
