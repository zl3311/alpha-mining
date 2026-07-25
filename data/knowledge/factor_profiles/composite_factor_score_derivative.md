---
field: composite_factor_score_derivative
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.9
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.534
ann_vol: 0.1945
hit_rate: 0.5126
rolling_sharpe_min: -1.885
rolling_sharpe_max: 3.396
redundancy_cluster: 43
negated_best_sharpe: 0.9
negated_best_template: neg_rank_level
negated_best_fitness: 0.63
n_negated_sims: 4
direction_gap: 0.13
---
# composite_factor_score_derivative (model16)

*Momentum score based on analyst revisions; intraday variant*

## Signal Profile
- `rank(composite_factor_score_derivative)`: S=-0.02, F=0.00, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(composite_factor_score_derivative, 5))`: S=0.77, F=0.56, T=28.2%, INFERIOR (TOP200)
- `-rank(composite_factor_score_derivative)`: S=0.47, F=0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(composite_factor_score_derivative, 5))`: S=0.73, F=0.33, T=25.2%, INFERIOR (TOP3000)
- `-ts_zscore(composite_factor_score_derivative, 63)`: S=0.20, F=0.07, T=22.6%, INFERIOR (TOP3000)
- `ts_mean(composite_factor_score_derivative, 10)`: S=-0.37, F=-0.19, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(composite_factor_score_derivative, 22))`: S=-0.48, F=-0.32, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * composite_factor_score_derivative)`: S=0.90, F=0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * composite_factor_score_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/15P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+10.4%
  - 2020: S=3.04 (strong), ret=+57.0%
  - 2021: S=-0.56 (negative), ret=-13.1%
  - 2022: S=0.76 (moderate), ret=+17.7%
  - 2023: S=0.24 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 53.40% over 1029 days (recovered)
- Annualized: return +15.4%, volatility 19.4% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.31, excess kurtosis +3.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.40, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +20.49%; worst month: -13.92%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.42
- Sideways: S=0.45
- Bear: S=1.59

## Negated Direction
Best negated: `rank(-1 * composite_factor_score_derivative)` S=0.90, F=0.63, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * composite_factor_score_derivative)`: S=0.90, F=0.63, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * composite_factor_score_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(composite_factor_score_derivative, 5))`: S=0.73, F=0.33, T=25.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(composite_factor_score_derivative, 5))` | TOP200 | 0.79 | 0.56 | 53.4% | 80% | mixed |
| `rank(ts_delta(composite_factor_score_derivative, 5))` | TOP500 | 0.24 | 0.08 | 60.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- multi_factor_acceleration_score_derivative: 1.000 (strongly positively correlated)
- multi_factor_static_score_derivative: 0.997 (strongly positively correlated)
- growth_potential_rank_derivative: 0.996 (strongly positively correlated)
- cashflow_efficiency_rank_derivative: 0.994 (strongly positively correlated)
- analyst_revision_rank_derivative: 0.990 (strongly positively correlated)

Redundancy cluster #43: 8 similar fields, mean |rho| 0.995 (representative: relative_valuation_rank_derivative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
