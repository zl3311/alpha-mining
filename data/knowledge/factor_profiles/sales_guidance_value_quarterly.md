---
field: sales_guidance_value_quarterly
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.54
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.141
ann_vol: 0.0948
hit_rate: 0.4761
rolling_sharpe_min: -0.701
rolling_sharpe_max: 1.732
redundancy_cluster: 1
negated_best_sharpe: 0.54
negated_best_template: neg_rank_level
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: -0.22
---
# sales_guidance_value_quarterly (analyst4)

*Sales - guidance value*

## Signal Profile
- `rank(sales_guidance_value_quarterly)`: S=0.53, F=0.35, T=1.1%, INFERIOR (TOP3000)
- `rank(sales_guidance_value_quarterly / close)`: S=0.59, F=0.39, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_guidance_value_quarterly, 5))`: S=0.82, F=0.36, T=35.5%, INFERIOR (TOP1000)
- `-rank(sales_guidance_value_quarterly)`: S=0.03, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_guidance_value_quarterly, 5))`: S=-0.12, F=-0.03, T=33.0%, INFERIOR (TOP3000)
- `ts_zscore(sales_guidance_value_quarterly, 22)`: S=0.76, F=0.42, T=39.0%, INFERIOR (TOP3000)
- `ts_mean(sales_guidance_value_quarterly, 10)`: S=-0.84, F=-1.07, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_guidance_value_quarterly, 22))`: S=-0.02, F=0.00, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value_quarterly)`: S=0.54, F=0.46, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value_quarterly / close)`: S=0.29, F=0.17, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.30 (weak), ret=+2.2%
  - 2020: S=-0.01 (negative), ret=-0.1%
  - 2021: S=0.77 (moderate), ret=+8.3%
  - 2022: S=1.18 (moderate), ret=+11.3%
  - 2023: S=0.77 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 14.10% over 245 days (recovered)
- Annualized: return +5.5%, volatility 9.5% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +0.57, excess kurtosis +2.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 1.73, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.35%; worst month: -5.27%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=-0.05
- Bear: S=-1.14

## Negated Direction
Best negated: `rank(-1 * sales_guidance_value_quarterly)` S=0.54, F=0.46, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_guidance_value_quarterly)`: S=0.54, F=0.46, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * sales_guidance_value_quarterly / close)`: S=0.29, F=0.17, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_guidance_value_quarterly, 5))`: S=-0.12, F=-0.03, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_guidance_value_quarterly / close)` | TOP3000 | 0.58 | 0.39 | 14.1% | 80% | bull-only |
| `rank(ts_delta(sales_guidance_value_quarterly, 5))` | TOP1000 | 0.82 | 0.36 | 10.0% | 80% | bull-only |
| `rank(sales_guidance_value_quarterly)` | TOP3000 | 0.52 | 0.35 | 28.5% | 80% | bull-only |
| `rank(sales_guidance_value_quarterly / close)` | TOP1000 | 0.23 | 0.12 | 30.3% | 60% | bull-only |
| `rank(sales_guidance_value_quarterly / close)` | TOP500 | 0.17 | 0.07 | 37.8% | 60% | bull-only |
| `rank(ts_delta(sales_guidance_value_quarterly, 5))` | TOP3000 | 0.16 | 0.03 | 16.0% | 40% | bull-only |
| `rank(ts_delta(sales_guidance_value_quarterly, 5))` | TOP200 | 0.11 | 0.03 | 33.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- total_assets_amount: 0.887 (strongly positively correlated)
- sales_estimate_minimum: 0.881 (strongly positively correlated)
- sales_estimate_minimum_quarterly: 0.881 (strongly positively correlated)
- sales_estimate_median_quarterly: 0.881 (strongly positively correlated)
- sales_estimate_median_value: 0.881 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
