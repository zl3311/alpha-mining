---
field: sales_max_guidance_quarterly
dataset: analyst4
best_template: rank_level
best_sharpe: 1.05
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0329
ann_vol: 0.0353
hit_rate: 0.5328
rolling_sharpe_min: -0.382
rolling_sharpe_max: 2.125
top_merge_partner: fn_liab_fair_val_l2_a
negated_best_sharpe: 0.41
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.64
---
# sales_max_guidance_quarterly (analyst4)

*The maximum guidance value for sales.*

## Signal Profile
- `rank(sales_max_guidance_quarterly)`: S=1.05, F=0.57, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_max_guidance_quarterly / close)`: S=0.66, F=0.42, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(sales_max_guidance_quarterly, 5))`: S=0.17, F=0.03, T=35.8%, INFERIOR (TOP1000)
- `-rank(sales_max_guidance_quarterly)`: S=-0.68, F=-0.35, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_max_guidance_quarterly, 5))`: S=0.13, F=0.03, T=33.0%, INFERIOR (TOP3000)
- `-ts_zscore(sales_max_guidance_quarterly, 63)`: S=0.65, F=0.31, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(sales_max_guidance_quarterly, 10)`: S=0.74, F=0.39, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_max_guidance_quarterly, 22))`: S=-0.07, F=-0.01, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_quarterly)`: S=0.41, F=0.21, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_quarterly / close)`: S=0.26, F=0.11, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.06, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+2.1%
  - 2020: S=1.37 (moderate), ret=+4.0%
  - 2021: S=1.66 (strong), ret=+6.1%
  - 2022: S=0.87 (moderate), ret=+3.5%
  - 2023: S=0.75 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 3.29% over 147 days (not yet recovered, ongoing at window end)
- Annualized: return +3.8%, volatility 3.5% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew +0.11, excess kurtosis +0.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.38, max 2.12, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +2.77%; worst month: -1.30%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.22
- Sideways: S=0.41
- Bear: S=2.73

## Negated Direction
Best negated: `rank(-1 * sales_max_guidance_quarterly)` S=0.41, F=0.21, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * sales_max_guidance_quarterly)`: S=0.41, F=0.21, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_max_guidance_quarterly / close)`: S=0.26, F=0.11, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_max_guidance_quarterly, 5))`: S=0.13, F=0.03, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_max_guidance_quarterly)` | TOP3000 | 1.06 | 0.57 | 3.3% | 100% | mixed |
| `rank(sales_max_guidance_quarterly)` | TOP500 | 0.83 | 0.52 | 8.4% | 80% | mixed |
| `rank(sales_max_guidance_quarterly / close)` | TOP500 | 0.67 | 0.42 | 15.4% | 60% | mixed |
| `rank(sales_max_guidance_quarterly)` | TOP1000 | 0.70 | 0.35 | 6.9% | 80% | bear-only |
| `rank(sales_max_guidance_quarterly / close)` | TOP3000 | 0.47 | 0.24 | 25.4% | 80% | bull-only |
| `rank(sales_max_guidance_quarterly / close)` | TOP1000 | 0.33 | 0.14 | 26.0% | 60% | bull-only |
| `rank(ts_delta(sales_max_guidance_quarterly, 5))` | TOP1000 | 0.17 | 0.03 | 13.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- sales_max_guidance_value: 0.579 (moderately positively correlated)
- operating_profit_before_depr_amort_max_guidance_qtr: 0.530 (moderately positively correlated)
- operating_profit_before_depr_amort_min_guidance_qtr: 0.525 (moderately positively correlated)
- fnd6_tlcf: 0.433 (moderately positively correlated)
- sales_min_guidance_quarterly: 0.373 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_liab_fair_val_l2_a | fundamental2 | -0.00 | 1.58 | +0.40 | -0.98 | yes |
| fnd6_ivaco | fundamental_investment | -0.14 | 1.83 | +0.48 | +0.77 | yes |
| fn_derivative_fair_value_of_derivative_asset_a | fundamental2 | -0.09 | 1.54 | +0.47 | +0.38 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.04 | 1.55 | +0.47 | +0.80 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.05 | 1.60 | +0.45 | -0.15 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
