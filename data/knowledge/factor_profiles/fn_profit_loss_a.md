---
field: fn_profit_loss_a
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.51
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.1805
ann_vol: 0.1408
hit_rate: 0.5142
rolling_sharpe_min: -0.816
rolling_sharpe_max: 1.567
negated_best_sharpe: 0.51
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: 0.23
---
# fn_profit_loss_a (fundamental2)

*The consolidated profit or loss for the period, net of income taxes, including the portion attributable to the noncontrolling interest.*

## Signal Profile
- `rank(fn_profit_loss_a)`: S=-0.08, F=-0.02, T=1.6%, INFERIOR (TOP1000)
- `rank(fn_profit_loss_a / close)`: S=0.09, F=0.02, T=1.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_profit_loss_a, 5))`: S=0.24, F=0.08, T=34.1%, INFERIOR (TOP3000)
- `-rank(fn_profit_loss_a)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_profit_loss_a, 5))`: S=0.16, F=0.06, T=25.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_profit_loss_a, 22)`: S=-0.03, F=-0.01, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fn_profit_loss_a, 10)`: S=-0.30, F=-0.14, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_profit_loss_a, 22))`: S=0.28, F=0.13, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_a)`: S=0.48, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_a / close)`: S=0.51, F=0.35, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/1P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+11.0%
  - 2020: S=0.39 (weak), ret=+5.8%
  - 2021: S=0.43 (weak), ret=+5.7%
  - 2022: S=-0.23 (negative), ret=-3.2%
  - 2023: S=-0.17 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 18.05% over 149 days (recovered)
- Annualized: return +3.5%, volatility 14.1% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.01, excess kurtosis +6.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.82, max 1.57, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +7.22%; worst month: -7.64%
Positive months: 52%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.40
- Sideways: S=0.90
- Bear: S=0.38

## Negated Direction
Best negated: `rank(-1 * fn_profit_loss_a / close)` S=0.51, F=0.35, INFERIOR
Direction gap: +0.23 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_profit_loss_a)`: S=0.48, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_a / close)`: S=0.51, F=0.35, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_profit_loss_a, 5))`: S=0.16, F=0.06, T=25.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_profit_loss_a, 5))` | TOP3000 | 0.25 | 0.08 | 18.1% | 60% | weak |

## Correlation Notes
Top correlates:
- fn_comprehensive_income_net_of_tax_a: 0.411 (moderately positively correlated)
- news_eod_vwap: 0.201 (weakly positively correlated)
- news_eod_high: 0.201 (weakly positively correlated)
- news_eod_low: 0.200 (weakly positively correlated)
- option_breakeven_10: 0.199 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
