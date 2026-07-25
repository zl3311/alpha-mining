---
field: sales_min_guidance_value
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.52
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 5
max_drawdown: 0.1499
ann_vol: 0.0674
hit_rate: 0.5077
rolling_sharpe_min: -1.487
rolling_sharpe_max: 2.494
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.07
---
# sales_min_guidance_value (analyst4)

*Minimum sales guidance for the annual period.*

## Signal Profile
- `rank(sales_min_guidance_value)`: S=0.45, F=0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(sales_min_guidance_value / close)`: S=0.45, F=0.22, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(sales_min_guidance_value, 5))`: S=0.00, F=0.00, T=33.3%, INFERIOR (TOP200)
- `-rank(sales_min_guidance_value)`: S=-0.08, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_min_guidance_value, 5))`: S=0.00, F=0.00, T=33.3%, INFERIOR (TOP3000)
- `-ts_zscore(sales_min_guidance_value, 63)`: S=0.18, F=0.04, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(sales_min_guidance_value, 10)`: S=0.04, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_min_guidance_value, 22))`: S=-0.69, F=-0.26, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_value)`: S=0.52, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_value / close)`: S=0.37, F=0.18, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+5.3%
  - 2020: S=-0.26 (negative), ret=-1.6%
  - 2021: S=1.32 (moderate), ret=+12.7%
  - 2022: S=-0.58 (negative), ret=-3.9%
  - 2023: S=0.47 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 14.99% over 309 days (recovered)
- Annualized: return +3.0%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.14, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 2.49, latest 0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +4.38%; worst month: -5.27%
Positive months: 59%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.37
- Sideways: S=1.23
- Bear: S=-0.12

## Negated Direction
Best negated: `rank(-1 * sales_min_guidance_value)` S=0.52, F=0.30, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * sales_min_guidance_value)`: S=0.52, F=0.30, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_value / close)`: S=0.37, F=0.18, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_min_guidance_value, 5))`: S=0.00, F=0.00, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_min_guidance_value / close)` | TOP500 | 0.45 | 0.22 | 15.0% | 60% | weak |
| `rank(sales_min_guidance_value)` | TOP3000 | 0.46 | 0.16 | 7.9% | 80% | all-weather |
| `rank(sales_min_guidance_value)` | TOP500 | 0.30 | 0.11 | 11.9% | 80% | weak |
| `rank(sales_min_guidance_value / close)` | TOP1000 | 0.14 | 0.04 | 12.9% | 60% | weak |
| `rank(sales_min_guidance_value / close)` | TOP3000 | 0.17 | 0.04 | 18.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- sales_min_guidance_quarterly: 0.683 (moderately positively correlated)
- sales_max_guidance_value: 0.472 (moderately positively correlated)
- anl4_capex_flag: 0.470 (moderately positively correlated)
- anl4_fcf_flag: 0.459 (moderately positively correlated)
- correlation_last_360_days_spy: 0.443 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
