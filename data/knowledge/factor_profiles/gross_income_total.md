---
field: gross_income_total
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.64
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1661
ann_vol: 0.0979
hit_rate: 0.4955
rolling_sharpe_min: -1.266
rolling_sharpe_max: 2.721
redundancy_cluster: 1
negated_best_sharpe: 0.29
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.35
---
# gross_income_total (analyst4)

*Gross Income value on an annual basis*

## Signal Profile
- `rank(gross_income_total)`: S=0.34, F=0.21, T=1.1%, INFERIOR (TOP3000)
- `rank(gross_income_total / close)`: S=0.64, F=0.45, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(gross_income_total, 5))`: S=-0.02, F=0.00, T=35.4%, INFERIOR (TOP3000)
- `-rank(gross_income_total)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(gross_income_total, 5))`: S=0.32, F=0.10, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(gross_income_total, 22)`: S=0.67, F=0.30, T=40.9%, INFERIOR (TOP3000)
- `ts_mean(gross_income_total, 10)`: S=-0.08, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(gross_income_total, 22))`: S=0.05, F=0.01, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * gross_income_total)`: S=0.21, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * gross_income_total / close)`: S=0.29, F=0.18, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/1P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.36 (negative), ret=-2.1%
  - 2020: S=-0.76 (negative), ret=-7.5%
  - 2021: S=1.06 (moderate), ret=+14.0%
  - 2022: S=1.79 (strong), ret=+20.0%
  - 2023: S=1.08 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 16.61% over 827 days (recovered)
- Annualized: return +6.2%, volatility 9.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.30, excess kurtosis +2.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.72, latest 1.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.27%; worst month: -4.90%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.32
- Sideways: S=0.17
- Bear: S=-2.50

## Negated Direction
Best negated: `rank(-1 * gross_income_total / close)` S=0.29, F=0.18, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * gross_income_total)`: S=0.21, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * gross_income_total / close)`: S=0.29, F=0.18, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(gross_income_total, 5))`: S=0.32, F=0.10, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(gross_income_total / close)` | TOP3000 | 0.63 | 0.45 | 16.6% | 60% | bull-only |
| `rank(gross_income_total)` | TOP3000 | 0.33 | 0.21 | 46.1% | 80% | bull-only |
| `rank(gross_income_total / close)` | TOP1000 | 0.18 | 0.08 | 32.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_gric_value: 0.979 (strongly positively correlated)
- gross_income_reported_value: 0.979 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.969 (strongly positively correlated)
- actual_sales_value_annual: 0.958 (strongly positively correlated)
- fnd6_mfma2_revt: 0.952 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
