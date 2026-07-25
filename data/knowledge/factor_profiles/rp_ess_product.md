---
field: rp_ess_product
dataset: news18
best_template: rank_level
best_sharpe: 0.75
best_fitness: 0.15
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0935
ann_vol: 0.0709
hit_rate: 0.5296
rolling_sharpe_min: -0.571
rolling_sharpe_max: 2.559
negated_best_sharpe: 0.18
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.57
---
# rp_ess_product (news18)

*Event sentiment score of product and service-related news*

## Signal Profile
- `rank(rp_ess_product)`: S=0.75, F=0.15, T=128.4%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_ess_product, 5))`: S=0.06, F=0.00, T=138.0%, INFERIOR (TOP3000)
- `-rank(rp_ess_product)`: S=-0.75, F=-0.15, T=128.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_product, 5))`: S=-0.06, F=0.00, T=138.0%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_product, 22)`: S=0.35, F=0.05, T=128.8%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_product, 10)`: S=0.38, F=0.10, T=25.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_product, 22))`: S=0.19, F=0.02, T=135.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_product)`: S=0.11, F=0.01, T=139.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_product / close)`: S=0.18, F=0.02, T=130.0%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.00 (moderate), ret=+5.4%
  - 2020: S=0.85 (moderate), ret=+6.0%
  - 2021: S=0.86 (moderate), ret=+6.4%
  - 2022: S=1.59 (strong), ret=+12.5%
  - 2023: S=-0.47 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 9.35% over 297 days (not yet recovered, ongoing at window end)
- Annualized: return +5.5%, volatility 7.1% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.03, excess kurtosis +1.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.56, latest -0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.60%; worst month: -4.00%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.40
- Sideways: S=1.04
- Bear: S=0.90

## Negated Direction
Best negated: `rank(-1 * rp_ess_product / close)` S=0.18, F=0.02, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_product)`: S=0.11, F=0.01, T=139.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_product / close)`: S=0.18, F=0.02, T=130.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_product, 5))`: S=-0.06, F=0.00, T=138.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_product)` | TOP1000 | 0.78 | 0.15 | 9.3% | 80% | mixed |
| `rank(rp_ess_product)` | TOP500 | 0.36 | 0.05 | 11.6% | 60% | mixed |
| `rank(rp_ess_product)` | TOP200 | 0.25 | 0.03 | 15.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- reporting_currency_code_9: -0.160 (weakly negatively correlated)
- sales_min_guidance_quarterly: 0.143 (weakly positively correlated)
- fnd6_cld4: -0.137 (weakly negatively correlated)
- fnd6_cld5: -0.131 (weakly negatively correlated)
- anl4_tbve_ft: -0.121 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
