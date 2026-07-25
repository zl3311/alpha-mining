---
field: net_income_total_2
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.3
best_fitness: 0.19
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3115
ann_vol: 0.1138
hit_rate: 0.4972
rolling_sharpe_min: -3.722
rolling_sharpe_max: 2.21
negated_best_sharpe: 0.3
negated_best_template: neg_rank_level
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.09
---
# net_income_total_2 (analyst4)

*Net profit- announced financial value for annual data*

## Signal Profile
- `rank(net_income_total_2)`: S=0.12, F=0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(net_income_total_2 / close)`: S=0.27, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(net_income_total_2, 5))`: S=0.24, F=0.05, T=36.0%, INFERIOR (TOP1000)
- `-rank(net_income_total_2)`: S=0.02, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_income_total_2, 5))`: S=0.12, F=0.02, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(net_income_total_2, 63)`: S=0.39, F=0.15, T=21.2%, INFERIOR (TOP3000)
- `ts_mean(net_income_total_2, 10)`: S=-0.05, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(net_income_total_2, 22))`: S=0.04, F=0.01, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * net_income_total_2)`: S=0.30, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * net_income_total_2 / close)`: S=0.19, F=0.09, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.4%
  - 2020: S=-2.47 (negative), ret=-16.7%
  - 2021: S=0.83 (moderate), ret=+11.2%
  - 2022: S=1.21 (moderate), ret=+20.2%
  - 2023: S=-0.20 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 31.15% over 832 days (recovered)
- Annualized: return +2.9%, volatility 11.4% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew -0.03, excess kurtosis +1.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.72, max 2.21, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.99%; worst month: -6.80%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.78
- Sideways: S=0.69
- Bear: S=-3.64

## Negated Direction
Best negated: `rank(-1 * net_income_total_2)` S=0.30, F=0.19, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * net_income_total_2)`: S=0.30, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * net_income_total_2 / close)`: S=0.19, F=0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_income_total_2, 5))`: S=0.12, F=0.02, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_income_total_2 / close)` | TOP3000 | 0.25 | 0.13 | 31.1% | 60% | bull-only |
| `rank(net_income_total_2 / close)` | TOP1000 | 0.12 | 0.05 | 32.8% | 60% | bull-only |
| `rank(ts_delta(net_income_total_2, 5))` | TOP1000 | 0.24 | 0.05 | 16.5% | 80% | bull-only |
| `rank(net_income_total_2)` | TOP3000 | 0.11 | 0.04 | 42.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pretax_income_total: 0.995 (strongly positively correlated)
- net_income_adjusted: 0.987 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.982 (strongly positively correlated)
- fnd6_ci: 0.977 (strongly positively correlated)
- earnings_per_share_reported: 0.965 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
