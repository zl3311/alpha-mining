---
field: fnd2_itxreexftfedstyitxrt
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.77
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2072
ann_vol: 0.0695
hit_rate: 0.5328
rolling_sharpe_min: -2.269
rolling_sharpe_max: 2.881
redundancy_cluster: 32
negated_best_sharpe: 0.77
negated_best_template: rank_neg_delta
negated_best_fitness: 0.54
n_negated_sims: 10
direction_gap: 0.01
---
# fnd2_itxreexftfedstyitxrt (fundamental2)

*Income tax amount computed at the federal tax rate, before any adjustments*

## Signal Profile
- `rank(fnd2_itxreexftfedstyitxrt)`: S=0.76, F=0.49, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd2_itxreexftfedstyitxrt / close)`: S=0.73, F=0.43, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_itxreexftfedstyitxrt, 5))`: S=0.24, F=0.11, T=23.6%, INFERIOR (TOP200)
- `-rank(fnd2_itxreexftfedstyitxrt)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_itxreexftfedstyitxrt, 5))`: S=0.77, F=0.54, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_itxreexftfedstyitxrt, 22)`: S=0.14, F=0.06, T=16.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_itxreexftfedstyitxrt, 10)`: S=0.16, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_itxreexftfedstyitxrt, 22))`: S=-0.72, F=-0.57, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreexftfedstyitxrt)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreexftfedstyitxrt / close)`: S=-0.46, F=-0.25, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.52 (strong), ret=+6.7%
  - 2020: S=-1.11 (negative), ret=-7.4%
  - 2021: S=0.57 (moderate), ret=+5.4%
  - 2022: S=1.94 (strong), ret=+13.8%
  - 2023: S=1.29 (moderate), ret=+7.1%

## Risk & Drawdown
- Max drawdown: 20.72% over 659 days (recovered)
- Annualized: return +5.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew -0.16, excess kurtosis +1.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.27, max 2.88, latest 1.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.89%; worst month: -4.87%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.53
- Sideways: S=2.15
- Bear: S=-2.37

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_itxreexftfedstyitxrt, 5))` S=0.77, F=0.54, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_itxreexftfedstyitxrt)`: S=-0.23, F=-0.10, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreexftfedstyitxrt / close)`: S=-0.46, F=-0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_itxreexftfedstyitxrt, 5))`: S=0.77, F=0.54, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_itxreexftfedstyitxrt)` | TOP3000 | 0.75 | 0.49 | 20.7% | 80% | bull-only |
| `rank(fnd2_itxreexftfedstyitxrt / close)` | TOP3000 | 0.71 | 0.43 | 9.3% | 100% | all-weather |
| `rank(fnd2_itxreexftfedstyitxrt / close)` | TOP1000 | 0.46 | 0.25 | 12.7% | 80% | bull-only |
| `rank(ts_delta(fnd2_itxreexftfedstyitxrt, 5))` | TOP200 | 0.23 | 0.11 | 36.9% | 80% | mixed |
| `rank(fnd2_itxreexftfedstyitxrt)` | TOP1000 | 0.22 | 0.10 | 34.5% | 60% | bull-only |
| `rank(fnd2_itxreexftfedstyitxrt / close)` | TOP500 | 0.20 | 0.09 | 21.2% | 40% | bull-only |
| `rank(fnd2_itxreexftfedstyitxrt / close)` | TOP200 | 0.05 | 0.02 | 41.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- highest_sales_estimate: 0.891 (strongly positively correlated)
- median_sales_estimate: 0.888 (strongly positively correlated)
- sales_estimate_average_annual: 0.887 (strongly positively correlated)
- lowest_sales_estimate: 0.881 (strongly positively correlated)
- fnd6_newqv1300_teqq: 0.875 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
