---
field: fn_proceeds_from_issuance_of_debt_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0416
ann_vol: 0.0258
hit_rate: 0.5077
rolling_sharpe_min: -1.6
rolling_sharpe_max: 2.647
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.06
---
# fn_proceeds_from_issuance_of_debt_q (fundamental2)

*The cash inflow during the period from additional borrowings in aggregate debt. Includes proceeds from short-term and long-term debt.*

## Signal Profile
- `rank(fn_proceeds_from_issuance_of_debt_q)`: S=0.50, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(fn_proceeds_from_issuance_of_debt_q / close)`: S=0.65, F=0.24, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_proceeds_from_issuance_of_debt_q, 5))`: S=-0.06, F=-0.01, T=36.1%, INFERIOR (TOP3000)
- `-rank(fn_proceeds_from_issuance_of_debt_q)`: S=-0.30, F=-0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_q, 5))`: S=0.59, F=0.32, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_proceeds_from_issuance_of_debt_q, 63)`: S=0.14, F=0.03, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fn_proceeds_from_issuance_of_debt_q, 10)`: S=-0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_proceeds_from_issuance_of_debt_q, 22))`: S=0.23, F=0.06, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_q)`: S=0.19, F=0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_q / close)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.30 (negative), ret=-2.9%
  - 2020: S=-0.11 (negative), ret=-0.3%
  - 2021: S=1.76 (strong), ret=+4.6%
  - 2022: S=0.72 (moderate), ret=+1.7%
  - 2023: S=1.93 (strong), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 4.16% over 824 days (recovered)
- Annualized: return +1.6%, volatility 2.6% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.18, excess kurtosis +1.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.60, max 2.65, latest 1.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +1.76%; worst month: -1.70%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.70
- Sideways: S=0.29
- Bear: S=-0.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_q, 5))` S=0.59, F=0.32, INFERIOR
Direction gap: -0.06 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_proceeds_from_issuance_of_debt_q)`: S=0.19, F=0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_proceeds_from_issuance_of_debt_q / close)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_proceeds_from_issuance_of_debt_q, 5))`: S=0.59, F=0.32, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_proceeds_from_issuance_of_debt_q / close)` | TOP3000 | 0.64 | 0.24 | 4.2% | 60% | mixed |
| `rank(fn_proceeds_from_issuance_of_debt_q / close)` | TOP1000 | 0.47 | 0.17 | 4.0% | 80% | mixed |
| `rank(fn_proceeds_from_issuance_of_debt_q)` | TOP3000 | 0.49 | 0.17 | 7.3% | 60% | bull-only |
| `rank(fn_proceeds_from_issuance_of_debt_q)` | TOP1000 | 0.30 | 0.09 | 4.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_ltrmdmrepoplay5: 0.540 (moderately positively correlated)
- anl4_totassets_high: 0.525 (moderately positively correlated)
- est_tot_assets: 0.525 (moderately positively correlated)
- anl4_totassets_median: 0.524 (moderately positively correlated)
- anl4_totassets_mean: 0.524 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
