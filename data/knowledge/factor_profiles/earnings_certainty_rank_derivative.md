---
field: earnings_certainty_rank_derivative
dataset: model16
best_template: rank_delta
best_sharpe: 0.91
best_fitness: 0.72
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.534
ann_vol: 0.195
hit_rate: 0.519
rolling_sharpe_min: -1.885
rolling_sharpe_max: 3.741
top_merge_partner: fnd6_currencyqv1300_curcd
redundancy_cluster: 43
negated_best_sharpe: 0.87
negated_best_template: neg_rank_level
negated_best_fitness: 0.6
n_negated_sims: 4
direction_gap: -0.04
---
# earnings_certainty_rank_derivative (model16)

*Measures the sustainability and certainty of earnings quality*

## Signal Profile
- `rank(earnings_certainty_rank_derivative)`: S=0.08, F=0.03, T=3.3%, INFERIOR (TOP200)
- `rank(earnings_certainty_rank_derivative / close)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_certainty_rank_derivative, 5))`: S=0.91, F=0.72, T=28.1%, INFERIOR (TOP200)
- `-rank(earnings_certainty_rank_derivative)`: S=0.43, F=0.27, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_certainty_rank_derivative, 5))`: S=0.70, F=0.31, T=24.8%, INFERIOR (TOP3000)
- `-ts_zscore(earnings_certainty_rank_derivative, 63)`: S=-0.07, F=-0.01, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(earnings_certainty_rank_derivative, 10)`: S=-0.34, F=-0.17, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_certainty_rank_derivative, 22))`: S=-0.44, F=-0.28, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * earnings_certainty_rank_derivative)`: S=0.87, F=0.60, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_certainty_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/16P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.93, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.82 (strong), ret=+24.0%
  - 2020: S=3.04 (strong), ret=+57.0%
  - 2021: S=-0.56 (negative), ret=-13.1%
  - 2022: S=0.76 (moderate), ret=+17.7%
  - 2023: S=0.24 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 53.40% over 1029 days (recovered)
- Annualized: return +18.2%, volatility 19.5% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.29, excess kurtosis +3.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.74, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +20.49%; worst month: -13.92%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.56
- Sideways: S=0.74
- Bear: S=1.59

## Negated Direction
Best negated: `rank(-1 * earnings_certainty_rank_derivative)` S=0.87, F=0.60, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * earnings_certainty_rank_derivative)`: S=0.87, F=0.60, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_certainty_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_certainty_rank_derivative, 5))`: S=0.70, F=0.31, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(earnings_certainty_rank_derivative, 5))` | TOP200 | 0.93 | 0.72 | 53.4% | 80% | all-weather |
| `rank(ts_delta(earnings_certainty_rank_derivative, 5))` | TOP500 | 0.31 | 0.12 | 60.0% | 80% | mixed |
| `rank(earnings_certainty_rank_derivative)` | TOP200 | 0.09 | 0.03 | 56.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- relative_valuation_rank_derivative: 1.000 (strongly positively correlated)
- analyst_revision_rank_derivative: 1.000 (strongly positively correlated)
- cashflow_efficiency_rank_derivative: 0.996 (strongly positively correlated)
- growth_potential_rank_derivative: 0.995 (strongly positively correlated)
- multi_factor_static_score_derivative: 0.994 (strongly positively correlated)

Redundancy cluster #43: 8 similar fields, mean |rho| 0.995 (representative: relative_valuation_rank_derivative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_currencyqv1300_curcd | fundamental6 | -0.23 | 1.52 | +0.56 | -0.75 | yes |
| fnd6_cld5 | fundamental6 | -0.22 | 1.45 | +0.48 | -0.88 | yes |
| reporting_currency_code_9 | analyst4 | -0.33 | 1.48 | +0.55 | -0.12 | yes |
| fnd6_xrent | fundamental6 | -0.30 | 1.41 | +0.47 | -0.84 | yes |
| operating_expense | fundamental6 | -0.29 | 1.41 | +0.47 | -0.81 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
