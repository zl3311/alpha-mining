---
field: sales_min_guidance_quarterly
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.84
best_fitness: 0.58
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1054
ann_vol: 0.0718
hit_rate: 0.5279
rolling_sharpe_min: -1.027
rolling_sharpe_max: 2.886
top_merge_partner: fnd2_a_flintasacmamtzcsrld
negated_best_sharpe: 0.73
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.11
---
# sales_min_guidance_quarterly (analyst4)

*Minimum guidance value for Sales*

## Signal Profile
- `rank(sales_min_guidance_quarterly)`: S=1.00, F=0.53, T=1.0%, INFERIOR (TOP3000)
- `rank(sales_min_guidance_quarterly / close)`: S=0.84, F=0.58, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(sales_min_guidance_quarterly, 5))`: S=0.20, F=0.03, T=36.1%, INFERIOR (TOP1000)
- `-rank(sales_min_guidance_quarterly)`: S=-0.59, F=-0.28, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_min_guidance_quarterly, 5))`: S=0.73, F=0.19, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(sales_min_guidance_quarterly, 63)`: S=0.88, F=0.48, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(sales_min_guidance_quarterly, 10)`: S=0.57, F=0.27, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_min_guidance_quarterly, 22))`: S=-0.06, F=-0.01, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_quarterly)`: S=-1.00, F=-0.53, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_quarterly / close)`: S=-0.58, F=-0.29, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.91 (strong), ret=+8.7%
  - 2020: S=0.63 (moderate), ret=+4.6%
  - 2021: S=1.65 (strong), ret=+16.1%
  - 2022: S=-0.37 (negative), ret=-2.4%
  - 2023: S=0.50 (moderate), ret=+3.0%

## Risk & Drawdown
- Max drawdown: 10.54% over 167 days (recovered)
- Annualized: return +6.1%, volatility 7.2% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew +0.04, excess kurtosis +1.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 2.89, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +5.56%; worst month: -5.54%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.10
- Sideways: S=0.98
- Bear: S=0.50

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_min_guidance_quarterly, 5))` S=0.73, F=0.19, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_min_guidance_quarterly)`: S=-1.00, F=-0.53, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * sales_min_guidance_quarterly / close)`: S=-0.58, F=-0.29, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_min_guidance_quarterly, 5))`: S=0.73, F=0.19, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_min_guidance_quarterly / close)` | TOP500 | 0.85 | 0.58 | 10.5% | 80% | mixed |
| `rank(sales_min_guidance_quarterly)` | TOP3000 | 1.01 | 0.53 | 3.3% | 100% | mixed |
| `rank(sales_min_guidance_quarterly)` | TOP500 | 0.77 | 0.46 | 8.7% | 80% | mixed |
| `rank(sales_min_guidance_quarterly / close)` | TOP3000 | 0.58 | 0.29 | 19.1% | 80% | bull-only |
| `rank(sales_min_guidance_quarterly)` | TOP1000 | 0.60 | 0.28 | 6.8% | 80% | bear-only |
| `rank(sales_min_guidance_quarterly / close)` | TOP1000 | 0.40 | 0.17 | 18.6% | 60% | bull-only |
| `rank(ts_delta(sales_min_guidance_quarterly, 5))` | TOP1000 | 0.20 | 0.03 | 8.7% | 80% | bear-only |

## Correlation Notes
Top correlates:
- sales_min_guidance_value: 0.683 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.431 (moderately positively correlated)
- fnd6_newqv1300_ivstq: 0.409 (moderately positively correlated)
- fn_comp_not_rec_q: 0.395 (weakly positively correlated)
- fn_debt_instrument_interest_rate_stated_percentage_q: -0.381 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_flintasacmamtzcsrld | fundamental2 | -0.19 | 1.43 | +0.46 | -0.72 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.20 | 1.34 | +0.47 | -0.60 | yes |
| fnd6_optprcby | fundamental6 | -0.19 | 1.45 | +0.45 | -0.58 | yes |
| fnd6_optprcwa | fundamental6 | -0.19 | 1.34 | +0.46 | -0.48 | yes |
| fnd2_a_bnsacqproformarvn | fundamental2 | -0.14 | 1.50 | +0.38 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
