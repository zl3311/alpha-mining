---
field: enterprise_value
dataset: fundamental6
cluster: fundamental6_valuation
coverage: 0.5
community_alphas: 39787
best_template: rank_neg_delta
best_sharpe: 1.41
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1033
ann_vol: 0.0742
hit_rate: 0.4802
rolling_sharpe_min: -1.256
rolling_sharpe_max: 1.739
negated_best_sharpe: 1.41
negated_best_template: rank_neg_delta
negated_best_fitness: 0.79
n_negated_sims: 10
direction_gap: 0.74
---
# enterprise_value (fundamental6)

*Enterprise Value*

## Signal Profile
- `rank(enterprise_value)`: S=0.23, F=0.11, T=3.0%, INFERIOR (TOP3000)
- `rank(enterprise_value / close)`: S=0.29, F=0.12, T=3.6%, INFERIOR (TOP1000)
- `rank(ts_delta(enterprise_value, 5))`: S=-0.79, F=-0.36, T=38.8%, INFERIOR (TOP200)
- `-rank(enterprise_value)`: S=-0.09, F=-0.03, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(enterprise_value, 5))`: S=1.41, F=0.79, T=36.9%, INFERIOR (TOP3000)
- `-ts_zscore(enterprise_value, 63)`: S=0.67, F=0.46, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(enterprise_value, 10)`: S=0.20, F=0.09, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(enterprise_value, 22))`: S=-0.88, F=-0.50, T=26.0%, INFERIOR (TOP3000)
- `rank(-1 * enterprise_value)`: S=-0.23, F=-0.11, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * enterprise_value / close)`: S=-0.31, F=-0.11, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+4.6%
  - 2020: S=-0.31 (negative), ret=-2.3%
  - 2021: S=0.69 (moderate), ret=+6.5%
  - 2022: S=0.38 (weak), ret=+3.4%
  - 2023: S=-0.39 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 10.33% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.1%, volatility 7.4% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.21, excess kurtosis +2.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 1.74, latest -0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +4.98%; worst month: -5.33%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.34
- Sideways: S=0.39
- Bear: S=-2.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(enterprise_value, 5))` S=1.41, F=0.79, INFERIOR
Direction gap: +0.74 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * enterprise_value)`: S=-0.23, F=-0.11, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * enterprise_value / close)`: S=-0.31, F=-0.11, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(enterprise_value, 5))`: S=1.41, F=0.79, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(enterprise_value / close)` | TOP1000 | 0.28 | 0.12 | 10.3% | 60% | bull-only |
| `rank(enterprise_value)` | TOP3000 | 0.23 | 0.11 | 40.2% | 80% | bull-only |
| `rank(enterprise_value / close)` | TOP3000 | 0.31 | 0.11 | 12.7% | 80% | bull-only |
| `rank(enterprise_value / close)` | TOP500 | 0.16 | 0.06 | 20.5% | 80% | bull-only |
| `rank(enterprise_value)` | TOP1000 | 0.09 | 0.03 | 40.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_loxdr: 0.863 (strongly positively correlated)
- total_goodwill_amount: 0.804 (strongly positively correlated)
- cashflow_dividends: 0.803 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.803 (strongly positively correlated)
- fnd6_newqv1300_loxdrq: 0.796 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
