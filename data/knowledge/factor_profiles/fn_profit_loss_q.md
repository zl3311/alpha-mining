---
field: fn_profit_loss_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.97
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1752
ann_vol: 0.0822
hit_rate: 0.4939
rolling_sharpe_min: -2.484
rolling_sharpe_max: 2.096
negated_best_sharpe: 0.97
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: 0.74
---
# fn_profit_loss_q (fundamental2)

*The consolidated profit or loss for the period, net of income taxes, including the portion attributable to the noncontrolling interest.*

## Signal Profile
- `rank(fn_profit_loss_q)`: S=0.17, F=0.06, T=2.4%, INFERIOR (TOP1000)
- `rank(fn_profit_loss_q / close)`: S=0.23, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_profit_loss_q, 5))`: S=-0.20, F=-0.05, T=35.6%, INFERIOR (TOP1000)
- `-rank(fn_profit_loss_q)`: S=-0.17, F=-0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_profit_loss_q, 5))`: S=0.97, F=0.58, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_profit_loss_q, 63)`: S=-0.38, F=-0.12, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_profit_loss_q, 10)`: S=0.03, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_profit_loss_q, 22))`: S=0.03, F=0.00, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_q)`: S=-0.09, F=-0.02, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_q / close)`: S=-0.12, F=-0.03, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.23, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.40 (negative), ret=-1.8%
  - 2020: S=-1.88 (negative), ret=-9.4%
  - 2021: S=0.86 (moderate), ret=+9.2%
  - 2022: S=1.59 (strong), ret=+18.4%
  - 2023: S=-1.23 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 17.52% over 1072 days (recovered)
- Annualized: return +1.9%, volatility 8.2% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew -0.01, excess kurtosis +1.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.48, max 2.10, latest -1.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.71%; worst month: -5.23%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.42
- Sideways: S=0.25
- Bear: S=-2.85

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_profit_loss_q, 5))` S=0.97, F=0.58, INFERIOR
Direction gap: +0.74 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fn_profit_loss_q)`: S=-0.09, F=-0.02, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_profit_loss_q / close)`: S=-0.12, F=-0.03, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_profit_loss_q, 5))`: S=0.97, F=0.58, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_profit_loss_q / close)` | TOP3000 | 0.22 | 0.10 | 31.4% | 40% | bull-only |
| `rank(fn_profit_loss_q / close)` | TOP1000 | 0.23 | 0.10 | 17.5% | 40% | bull-only |
| `rank(fn_profit_loss_q)` | TOP1000 | 0.17 | 0.06 | 23.7% | 40% | bull-only |
| `rank(fn_profit_loss_q)` | TOP3000 | 0.12 | 0.04 | 35.3% | 40% | bull-only |
| `rank(fn_profit_loss_q / close)` | TOP500 | 0.12 | 0.03 | 22.0% | 40% | bull-only |
| `rank(fn_profit_loss_q)` | TOP500 | 0.09 | 0.02 | 26.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_oiadpq: 0.863 (strongly positively correlated)
- operating_income: 0.863 (strongly positively correlated)
- ebit_reported_value: 0.858 (strongly positively correlated)
- anl4_ebit_value: 0.858 (strongly positively correlated)
- pretax_income_standalone_value: 0.857 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
