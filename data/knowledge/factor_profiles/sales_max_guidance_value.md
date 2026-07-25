---
field: sales_max_guidance_value
dataset: analyst4
best_template: rank_level
best_sharpe: 0.48
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0783
ann_vol: 0.0387
hit_rate: 0.5142
rolling_sharpe_min: -1.775
rolling_sharpe_max: 2.391
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.13
---
# sales_max_guidance_value (analyst4)

*Maximum guidance value for annual sales*

## Signal Profile
- `rank(sales_max_guidance_value)`: S=0.48, F=0.18, T=1.1%, INFERIOR (TOP3000)
- `rank(sales_max_guidance_value / close)`: S=0.27, F=0.11, T=2.2%, INFERIOR (TOP500)
- `rank(ts_delta(sales_max_guidance_value, 5))`: S=0.22, F=0.06, T=32.9%, INFERIOR (TOP200)
- `-rank(sales_max_guidance_value)`: S=-0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_max_guidance_value, 5))`: S=-0.22, F=-0.06, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(sales_max_guidance_value, 63)`: S=0.18, F=0.05, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(sales_max_guidance_value, 10)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_max_guidance_value, 22))`: S=-0.40, F=-0.14, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_value)`: S=0.35, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_value / close)`: S=0.27, F=0.12, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.49, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+0.7%
  - 2020: S=-0.81 (negative), ret=-2.4%
  - 2021: S=1.61 (strong), ret=+8.1%
  - 2022: S=0.22 (weak), ret=+1.0%
  - 2023: S=0.53 (moderate), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 7.83% over 650 days (recovered)
- Annualized: return +1.9%, volatility 3.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.03, excess kurtosis +1.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.39, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.69%; worst month: -2.26%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.28
- Sideways: S=-0.40
- Bear: S=0.37

## Negated Direction
Best negated: `rank(-1 * sales_max_guidance_value)` S=0.35, F=0.17, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_max_guidance_value)`: S=0.35, F=0.17, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_value / close)`: S=0.27, F=0.12, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_max_guidance_value, 5))`: S=-0.22, F=-0.06, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_max_guidance_value)` | TOP3000 | 0.49 | 0.18 | 7.8% | 80% | mixed |
| `rank(sales_max_guidance_value)` | TOP500 | 0.31 | 0.12 | 12.5% | 80% | weak |
| `rank(sales_max_guidance_value / close)` | TOP500 | 0.27 | 0.11 | 22.0% | 60% | bull-only |
| `rank(sales_max_guidance_value / close)` | TOP3000 | 0.20 | 0.06 | 28.1% | 80% | bull-only |
| `rank(ts_delta(sales_max_guidance_value, 5))` | TOP200 | 0.23 | 0.06 | 32.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcf_flag: 0.642 (moderately positively correlated)
- anl4_tot_gw_ft: 0.614 (moderately positively correlated)
- anl4_fcfps_flag: 0.588 (moderately positively correlated)
- anl4_totassets_flag: 0.586 (moderately positively correlated)
- sales_max_guidance_quarterly: 0.579 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
