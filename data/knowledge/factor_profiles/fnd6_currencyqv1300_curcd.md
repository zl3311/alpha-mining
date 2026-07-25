---
field: fnd6_currencyqv1300_curcd
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.96
best_fitness: 1.2
best_universe: TOP200
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.2187
ann_vol: 0.2054
hit_rate: 0.4704
rolling_sharpe_min: -0.599
rolling_sharpe_max: 2.264
top_merge_partner: relative_valuation_rank_derivative
negated_best_sharpe: 0.03
negated_best_template: neg_rank_level
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.93
---
# fnd6_currencyqv1300_curcd (fundamental6)

*ISO Currency Code - Company Annual Market*

## Signal Profile
- `rank(fnd6_currencyqv1300_curcd)`: S=0.23, F=0.14, T=7.4%, INFERIOR (TOP1000)
- `rank(fnd6_currencyqv1300_curcd / close)`: S=0.30, F=0.15, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_currencyqv1300_curcd, 5))`: S=0.96, F=1.20, T=12.2%, AVERAGE (TOP200)
- `-rank(fnd6_currencyqv1300_curcd)`: S=-0.23, F=-0.14, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_currencyqv1300_curcd, 5))`: S=-0.54, F=-0.40, T=22.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_currencyqv1300_curcd, 22)`: S=-0.25, F=-0.15, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_currencyqv1300_curcd, 10)`: S=0.35, F=0.25, T=6.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_currencyqv1300_curcd, 22))`: S=1.07, F=1.05, T=13.9%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_currencyqv1300_curcd)`: S=0.03, F=0.01, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_currencyqv1300_curcd / close)`: S=-0.21, F=-0.09, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/9P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+12.0%
  - 2020: S=-0.22 (negative), ret=-4.2%
  - 2021: S=2.06 (strong), ret=+67.0%
  - 2022: S=1.01 (moderate), ret=+19.7%
  - 2023: S=0.28 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 21.87% over 86 days (recovered)
- Annualized: return +19.7%, volatility 20.5% (fraction of booksize)
- Hit rate: 47.0% positive days
- Tail shape: skew +0.43, excess kurtosis +17.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.26, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +16.69%; worst month: -14.92%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.73
- Sideways: S=0.83
- Bear: S=0.36

## Negated Direction
Best negated: `rank(-1 * fnd6_currencyqv1300_curcd)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_currencyqv1300_curcd)`: S=0.03, F=0.01, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_currencyqv1300_curcd / close)`: S=-0.21, F=-0.09, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_currencyqv1300_curcd, 5))`: S=-0.54, F=-0.40, T=22.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_currencyqv1300_curcd, 5))` | TOP200 | 0.96 | 1.20 | 21.9% | 80% | mixed |
| `rank(ts_delta(fnd6_currencyqv1300_curcd, 5))` | TOP3000 | 0.87 | 0.54 | 29.0% | 80% | all-weather |
| `rank(ts_delta(fnd6_currencyqv1300_curcd, 5))` | TOP500 | 0.50 | 0.37 | 40.2% | 100% | all-weather |
| `rank(ts_delta(fnd6_currencyqv1300_curcd, 5))` | TOP1000 | 0.48 | 0.25 | 31.0% | 80% | mixed |
| `rank(fnd6_currencyqv1300_curcd / close)` | TOP200 | 0.31 | 0.15 | 21.8% | 80% | mixed |
| `rank(fnd6_currencyqv1300_curcd)` | TOP1000 | 0.24 | 0.14 | 55.7% | 60% | mixed |
| `rank(fnd6_currencyqv1300_curcd / close)` | TOP500 | 0.21 | 0.09 | 30.3% | 80% | bear-only |
| `rank(fnd6_currencyqv1300_curcd / close)` | TOP1000 | 0.13 | 0.04 | 36.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.498 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.472 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.472 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.463 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.463 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| relative_valuation_rank_derivative | model16 | -0.23 | 1.52 | +0.56 | -0.75 | yes |
| earnings_certainty_rank_derivative | model16 | -0.23 | 1.52 | +0.56 | -0.75 | yes |
| analyst_revision_rank_derivative | model16 | -0.23 | 1.52 | +0.56 | -0.75 | yes |
| growth_potential_rank_derivative | model16 | -0.23 | 1.49 | +0.53 | -0.78 | yes |
| multi_factor_static_score_derivative | model16 | -0.23 | 1.45 | +0.49 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
