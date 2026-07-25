---
field: cashflow_efficiency_rank_derivative
dataset: model16
best_template: neg_rank_level
best_sharpe: 0.87
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.5339
ann_vol: 0.1952
hit_rate: 0.5134
rolling_sharpe_min: -1.885
rolling_sharpe_max: 3.396
top_merge_partner: reporting_currency_code_9
redundancy_cluster: 43
negated_best_sharpe: 0.87
negated_best_template: neg_rank_level
negated_best_fitness: 0.6
n_negated_sims: 4
direction_gap: 0.09
---
# cashflow_efficiency_rank_derivative (model16)

*Ranks stocks by their ability to generate cash flows and operational profitability*

## Signal Profile
- `rank(cashflow_efficiency_rank_derivative)`: S=-0.04, F=-0.01, T=3.3%, INFERIOR (TOP200)
- `rank(cashflow_efficiency_rank_derivative / close)`: S=0.05, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_efficiency_rank_derivative, 5))`: S=0.78, F=0.57, T=28.1%, INFERIOR (TOP200)
- `-rank(cashflow_efficiency_rank_derivative)`: S=0.45, F=0.29, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_efficiency_rank_derivative, 5))`: S=0.69, F=0.30, T=25.0%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_efficiency_rank_derivative, 63)`: S=-0.09, F=-0.02, T=22.5%, INFERIOR (TOP3000)
- `ts_mean(cashflow_efficiency_rank_derivative, 10)`: S=-0.34, F=-0.17, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_efficiency_rank_derivative, 22))`: S=-0.46, F=-0.30, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_efficiency_rank_derivative)`: S=0.87, F=0.60, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_efficiency_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/16P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.90 (moderate), ret=+11.9%
  - 2020: S=3.04 (strong), ret=+57.0%
  - 2021: S=-0.56 (negative), ret=-13.1%
  - 2022: S=0.76 (moderate), ret=+17.7%
  - 2023: S=0.24 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 53.39% over 1029 days (recovered)
- Annualized: return +15.7%, volatility 19.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.31, excess kurtosis +3.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.40, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +20.49%; worst month: -13.92%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.41
- Sideways: S=0.55
- Bear: S=1.55

## Negated Direction
Best negated: `rank(-1 * cashflow_efficiency_rank_derivative)` S=0.87, F=0.60, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * cashflow_efficiency_rank_derivative)`: S=0.87, F=0.60, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_efficiency_rank_derivative / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_efficiency_rank_derivative, 5))`: S=0.69, F=0.30, T=25.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_efficiency_rank_derivative, 5))` | TOP200 | 0.81 | 0.57 | 53.4% | 80% | mixed |
| `rank(ts_delta(cashflow_efficiency_rank_derivative, 5))` | TOP500 | 0.27 | 0.09 | 60.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- multi_factor_static_score_derivative: 0.998 (strongly positively correlated)
- growth_potential_rank_derivative: 0.997 (strongly positively correlated)
- analyst_revision_rank_derivative: 0.996 (strongly positively correlated)
- relative_valuation_rank_derivative: 0.996 (strongly positively correlated)
- earnings_certainty_rank_derivative: 0.996 (strongly positively correlated)

Redundancy cluster #43: 8 similar fields, mean |rho| 0.995 (representative: relative_valuation_rank_derivative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| reporting_currency_code_9 | analyst4 | -0.33 | 1.36 | +0.54 | -0.34 | yes |
| fnd6_currencyqv1300_curcd | fundamental6 | -0.23 | 1.43 | +0.47 | -0.81 | yes |
| fnd6_newqv1300_xoprq | fundamental6 | -0.28 | 1.28 | +0.44 | -0.87 | yes |
| operating_expense | fundamental6 | -0.28 | 1.28 | +0.44 | -0.87 | yes |
| fnd6_newqv1300_invrmq | fundamental6 | -0.26 | 1.29 | +0.48 | -0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
