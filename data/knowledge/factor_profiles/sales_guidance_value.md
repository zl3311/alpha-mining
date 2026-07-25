---
field: sales_guidance_value
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.63
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2663
ann_vol: 0.1223
hit_rate: 0.515
rolling_sharpe_min: -2.813
rolling_sharpe_max: 2.313
negated_best_sharpe: 0.63
negated_best_template: neg_rank_level
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: 0.13
---
# sales_guidance_value (analyst4)

*Sales - Guidance value for the annual period*

## Signal Profile
- `rank(sales_guidance_value)`: S=0.50, F=0.35, T=1.2%, INFERIOR (TOP3000)
- `rank(sales_guidance_value / close)`: S=0.48, F=0.27, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_guidance_value, 5))`: S=0.37, F=0.11, T=35.2%, INFERIOR (TOP500)
- `-rank(sales_guidance_value)`: S=-0.09, F=-0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_guidance_value, 5))`: S=-0.28, F=-0.09, T=32.6%, INFERIOR (TOP3000)
- `ts_zscore(sales_guidance_value, 22)`: S=0.62, F=0.30, T=35.7%, INFERIOR (TOP3000)
- `ts_mean(sales_guidance_value, 10)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_guidance_value, 22))`: S=0.16, F=0.04, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value)`: S=0.63, F=0.57, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value / close)`: S=0.37, F=0.23, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.49, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.30 (weak), ret=+2.1%
  - 2020: S=-2.40 (negative), ret=-19.2%
  - 2021: S=1.40 (moderate), ret=+18.8%
  - 2022: S=1.70 (strong), ret=+29.3%
  - 2023: S=-0.13 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 26.63% over 779 days (recovered)
- Annualized: return +6.0%, volatility 12.2% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew -0.01, excess kurtosis +1.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.81, max 2.31, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.62%; worst month: -5.18%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.91
- Sideways: S=0.85
- Bear: S=-3.05

## Negated Direction
Best negated: `rank(-1 * sales_guidance_value)` S=0.63, F=0.57, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * sales_guidance_value)`: S=0.63, F=0.57, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value / close)`: S=0.37, F=0.23, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_guidance_value, 5))`: S=-0.28, F=-0.09, T=32.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_guidance_value)` | TOP3000 | 0.49 | 0.35 | 26.6% | 60% | bull-only |
| `rank(sales_guidance_value / close)` | TOP3000 | 0.47 | 0.27 | 11.9% | 40% | bull-only |
| `rank(ts_delta(sales_guidance_value, 5))` | TOP500 | 0.37 | 0.11 | 18.0% | 60% | mixed |
| `rank(ts_delta(sales_guidance_value, 5))` | TOP1000 | 0.39 | 0.11 | 21.2% | 80% | bull-only |
| `rank(ts_delta(sales_guidance_value, 5))` | TOP200 | 0.28 | 0.09 | 37.8% | 40% | bull-only |
| `rank(sales_guidance_value / close)` | TOP1000 | 0.14 | 0.06 | 18.4% | 60% | bull-only |
| `rank(sales_guidance_value)` | TOP1000 | 0.08 | 0.03 | 36.5% | 60% | bull-only |
| `rank(ts_delta(sales_guidance_value, 5))` | TOP3000 | 0.12 | 0.02 | 20.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfv4_eps_high: 0.935 (strongly positively correlated)
- est_eps: 0.935 (strongly positively correlated)
- anl4_netprofit_low: 0.933 (strongly positively correlated)
- net_income_total_2: 0.933 (strongly positively correlated)
- pretax_income_total: 0.932 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
