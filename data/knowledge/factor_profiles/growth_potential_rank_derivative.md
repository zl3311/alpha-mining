---
field: growth_potential_rank_derivative
dataset: model16
best_template: rank_delta
best_sharpe: 0.86
best_fitness: 0.66
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.534
ann_vol: 0.1952
hit_rate: 0.5166
rolling_sharpe_min: -1.885
rolling_sharpe_max: 3.599
top_merge_partner: fnd6_currencyqv1300_curcd
redundancy_cluster: 43
negated_best_sharpe: 0.88
negated_best_template: neg_rank_level
negated_best_fitness: 0.62
n_negated_sims: 4
direction_gap: 0.02
---
# growth_potential_rank_derivative (model16)

*Composite growth score qualifying the stock’s expected medium‑term growth potential*

## Signal Profile
- `rank(growth_potential_rank_derivative)`: S=0.00, F=0.00, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(growth_potential_rank_derivative, 5))`: S=0.86, F=0.66, T=28.1%, INFERIOR (TOP200)
- `-rank(growth_potential_rank_derivative)`: S=0.44, F=0.28, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(growth_potential_rank_derivative, 5))`: S=0.71, F=0.32, T=24.8%, INFERIOR (TOP3000)
- `-ts_zscore(growth_potential_rank_derivative, 63)`: S=0.16, F=0.05, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(growth_potential_rank_derivative, 10)`: S=-0.35, F=-0.17, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(growth_potential_rank_derivative, 22))`: S=-0.45, F=-0.29, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * growth_potential_rank_derivative)`: S=0.88, F=0.62, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * growth_potential_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/15P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.47 (moderate), ret=+19.6%
  - 2020: S=3.04 (strong), ret=+57.0%
  - 2021: S=-0.56 (negative), ret=-13.1%
  - 2022: S=0.76 (moderate), ret=+17.7%
  - 2023: S=0.24 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 53.40% over 1029 days (recovered)
- Annualized: return +17.3%, volatility 19.5% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.30, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.60, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +20.49%; worst month: -13.92%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.46
- Sideways: S=0.68
- Bear: S=1.62

## Negated Direction
Best negated: `rank(-1 * growth_potential_rank_derivative)` S=0.88, F=0.62, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * growth_potential_rank_derivative)`: S=0.88, F=0.62, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * growth_potential_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(growth_potential_rank_derivative, 5))`: S=0.71, F=0.32, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(growth_potential_rank_derivative, 5))` | TOP200 | 0.89 | 0.66 | 53.4% | 80% | mixed |
| `rank(ts_delta(growth_potential_rank_derivative, 5))` | TOP500 | 0.31 | 0.11 | 60.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- multi_factor_static_score_derivative: 0.999 (strongly positively correlated)
- cashflow_efficiency_rank_derivative: 0.997 (strongly positively correlated)
- multi_factor_acceleration_score_derivative: 0.996 (strongly positively correlated)
- composite_factor_score_derivative: 0.996 (strongly positively correlated)
- analyst_revision_rank_derivative: 0.995 (strongly positively correlated)

Redundancy cluster #43: 8 similar fields, mean |rho| 0.995 (representative: relative_valuation_rank_derivative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_currencyqv1300_curcd | fundamental6 | -0.23 | 1.49 | +0.53 | -0.78 | yes |
| reporting_currency_code_9 | analyst4 | -0.33 | 1.44 | +0.55 | -0.20 | yes |
| operating_expense | fundamental6 | -0.28 | 1.36 | +0.47 | -0.84 | yes |
| fnd6_newqv1300_xoprq | fundamental6 | -0.28 | 1.36 | +0.47 | -0.84 | yes |
| fnd6_cld5 | fundamental6 | -0.22 | 1.40 | +0.44 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
