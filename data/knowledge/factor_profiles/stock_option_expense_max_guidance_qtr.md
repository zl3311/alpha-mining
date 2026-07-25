---
field: stock_option_expense_max_guidance_qtr
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 1.09
best_fitness: 1.16
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2615
ann_vol: 0.1375
hit_rate: 0.4583
rolling_sharpe_min: -1.883
rolling_sharpe_max: 1.934
negated_best_sharpe: 1.09
negated_best_template: neg_rank_level
negated_best_fitness: 1.16
n_negated_sims: 10
direction_gap: 0.68
---
# stock_option_expense_max_guidance_qtr (analyst4)

*Stock option expense - maximum guidance value*

## Signal Profile
- `rank(stock_option_expense_max_guidance_qtr)`: S=0.07, F=0.02, T=4.4%, INFERIOR (TOP200)
- `rank(stock_option_expense_max_guidance_qtr / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(stock_option_expense_max_guidance_qtr, 5))`: S=0.41, F=0.28, T=3.6%, INFERIOR (TOP200)
- `-rank(stock_option_expense_max_guidance_qtr)`: S=1.08, F=1.14, T=0.9%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(stock_option_expense_max_guidance_qtr, 5))`: S=0.22, F=0.10, T=3.6%, INFERIOR (TOP3000)
- `-ts_zscore(stock_option_expense_max_guidance_qtr, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(stock_option_expense_max_guidance_qtr, 10)`: S=-1.07, F=-1.13, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(stock_option_expense_max_guidance_qtr, 22))`: S=0.11, F=0.04, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * stock_option_expense_max_guidance_qtr)`: S=1.09, F=1.16, T=0.9%, AVERAGE (TOP3000)
- `rank(-1 * stock_option_expense_max_guidance_qtr / close)`: S=0.08, F=0.02, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 26F/4P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/17P
- LOW_TURNOVER: 11F/21P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.38, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.92 (moderate), ret=+13.0%
  - 2020: S=-1.34 (negative), ret=-15.5%
  - 2021: S=0.88 (moderate), ret=+16.4%
  - 2022: S=0.66 (moderate), ret=+8.6%
  - 2023: S=0.44 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 26.15% over 539 days (recovered)
- Annualized: return +5.3%, volatility 13.8% (fraction of booksize)
- Hit rate: 45.8% positive days
- Tail shape: skew +1.65, excess kurtosis +25.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.88, max 1.93, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +11.16%; worst month: -8.38%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.24
- Sideways: S=0.33
- Bear: S=-2.11

## Negated Direction
Best negated: `rank(-1 * stock_option_expense_max_guidance_qtr)` S=1.09, F=1.16, AVERAGE
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * stock_option_expense_max_guidance_qtr)`: S=1.09, F=1.16, T=0.9%, AVERAGE (TOP3000)
- `rank(-1 * stock_option_expense_max_guidance_qtr / close)`: S=0.08, F=0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(stock_option_expense_max_guidance_qtr, 5))`: S=0.22, F=0.10, T=3.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(stock_option_expense_max_guidance_qtr, 5))` | TOP200 | 0.38 | 0.28 | 26.2% | 80% | bull-only |
| `rank(ts_delta(stock_option_expense_max_guidance_qtr, 5))` | TOP500 | 0.40 | 0.25 | 40.3% | 60% | bull-only |
| `rank(ts_delta(stock_option_expense_max_guidance_qtr, 5))` | TOP3000 | 0.29 | 0.16 | 42.5% | 40% | bull-only |
| `rank(stock_option_expense_max_guidance_qtr)` | TOP200 | 0.07 | 0.02 | 46.7% | 60% | bull-only |
| `rank(stock_option_expense_max_guidance_qtr / close)` | TOP3000 | 0.07 | 0.02 | 52.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_stock_option_expense_guidance: 1.000 (strongly positively correlated)
- fnd6_itcb: 0.853 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.721 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.721 (strongly positively correlated)
- min_total_assets_guidance: 0.721 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
