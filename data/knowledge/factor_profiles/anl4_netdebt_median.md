---
field: anl4_netdebt_median
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.49
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0919
ann_vol: 0.0638
hit_rate: 0.4842
rolling_sharpe_min: -1.145
rolling_sharpe_max: 1.654
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: 0.14
---
# anl4_netdebt_median (analyst4)

*Net Debt - median of estimations*

## Signal Profile
- `rank(anl4_netdebt_median)`: S=0.00, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(anl4_netdebt_median / close)`: S=0.35, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netdebt_median, 5))`: S=0.38, F=0.11, T=35.6%, INFERIOR (TOP500)
- `-rank(anl4_netdebt_median)`: S=0.13, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_median, 5))`: S=0.49, F=0.21, T=33.6%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_median, 63)`: S=0.21, F=0.05, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_median, 10)`: S=-0.39, F=-0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_median, 22))`: S=-0.71, F=-0.35, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_median)`: S=0.26, F=0.11, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_median / close)`: S=0.21, F=0.08, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+2.3%
  - 2020: S=0.31 (weak), ret=+2.5%
  - 2021: S=0.39 (weak), ret=+2.4%
  - 2022: S=0.70 (moderate), ret=+5.3%
  - 2023: S=-0.32 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 9.19% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 6.4% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.19, excess kurtosis +1.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 1.65, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +3.80%; worst month: -4.92%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.26
- Sideways: S=-0.04
- Bear: S=-1.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netdebt_median, 5))` S=0.49, F=0.21, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_median)`: S=0.26, F=0.11, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_median / close)`: S=0.21, F=0.08, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_median, 5))`: S=0.49, F=0.21, T=33.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netdebt_median / close)` | TOP3000 | 0.35 | 0.15 | 9.2% | 80% | bull-only |
| `rank(ts_delta(anl4_netdebt_median, 5))` | TOP500 | 0.39 | 0.11 | 19.3% | 40% | weak |

## Correlation Notes
Top correlates:
- anl4_netdebt_mean: 1.000 (strongly positively correlated)
- anl4_netdebt_high: 0.998 (strongly positively correlated)
- anl4_netdebt_low: 0.997 (strongly positively correlated)
- est_netdebt: 0.920 (strongly positively correlated)
- net_debt_reported_value: 0.886 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
