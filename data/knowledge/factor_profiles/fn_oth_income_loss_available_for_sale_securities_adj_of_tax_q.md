---
field: fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.57
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 6
max_drawdown: 0.0835
ann_vol: 0.0397
hit_rate: 0.5223
rolling_sharpe_min: -1.551
rolling_sharpe_max: 1.994
negated_best_sharpe: 0.56
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.01
---
# fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q (fundamental2)

*Amount after tax and reclassification adjustments, of appreciation (loss) in value of unsold available-for-sale securities. Excludes amounts related to other than temporary impairment (OTTI) loss.*

## Signal Profile
- `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)`: S=0.48, F=0.17, T=2.5%, INFERIOR (TOP3000)
- `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q / close)`: S=0.52, F=0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 5))`: S=0.13, F=0.03, T=35.3%, INFERIOR (TOP1000)
- `-rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)`: S=0.40, F=0.14, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 5))`: S=0.12, F=0.03, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 63)`: S=0.27, F=0.09, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 10)`: S=-0.61, F=-0.33, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 22))`: S=0.57, F=0.29, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)`: S=0.56, F=0.25, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q / close)`: S=0.53, F=0.23, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.38 (moderate), ret=+3.6%
  - 2020: S=0.67 (moderate), ret=+2.1%
  - 2021: S=0.45 (weak), ret=+1.6%
  - 2022: S=-0.39 (negative), ret=-1.9%
  - 2023: S=0.99 (moderate), ret=+4.8%

## Risk & Drawdown
- Max drawdown: 8.35% over 898 days (recovered)
- Annualized: return +2.1%, volatility 4.0% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.10, excess kurtosis +2.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 1.99, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +2.79%; worst month: -2.06%
Positive months: 54%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.46
- Sideways: S=0.90
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)` S=0.56, F=0.25, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)`: S=0.56, F=0.25, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q / close)`: S=0.53, F=0.23, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 5))`: S=0.12, F=0.03, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q / close)` | TOP3000 | 0.53 | 0.21 | 8.3% | 80% | weak |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)` | TOP3000 | 0.49 | 0.17 | 9.9% | 80% | weak |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q)` | TOP200 | 0.26 | 0.10 | 11.4% | 80% | mixed |
| `rank(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q / close)` | TOP200 | 0.16 | 0.05 | 10.3% | 60% | mixed |
| `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 5))` | TOP1000 | 0.13 | 0.03 | 26.3% | 60% | bear-only |
| `rank(ts_delta(fn_oth_income_loss_available_for_sale_securities_adj_of_tax_q, 5))` | TOP200 | 0.10 | 0.02 | 40.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_chech: -0.237 (weakly negatively correlated)
- cashflow: -0.233 (weakly negatively correlated)
- anl4_totgw_number: -0.211 (weakly negatively correlated)
- anl4_cfo_number: -0.206 (weakly negatively correlated)
- fn_debt_instrument_interest_rate_stated_percentage_q: 0.197 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
