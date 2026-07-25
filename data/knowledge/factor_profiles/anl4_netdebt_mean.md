---
field: anl4_netdebt_mean
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.53
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.0923
ann_vol: 0.0636
hit_rate: 0.4834
rolling_sharpe_min: -1.156
rolling_sharpe_max: 1.658
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.17
---
# anl4_netdebt_mean (analyst4)

*Net debt - mean of estimations*

## Signal Profile
- `rank(anl4_netdebt_mean)`: S=0.00, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(anl4_netdebt_mean / close)`: S=0.36, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netdebt_mean, 5))`: S=0.44, F=0.14, T=35.8%, INFERIOR (TOP500)
- `-rank(anl4_netdebt_mean)`: S=0.13, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_mean, 5))`: S=0.53, F=0.23, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_mean, 63)`: S=0.25, F=0.07, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_mean, 10)`: S=-0.37, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_mean, 22))`: S=-0.70, F=-0.34, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_mean)`: S=0.23, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_mean / close)`: S=0.15, F=0.05, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+2.3%
  - 2020: S=0.36 (weak), ret=+2.8%
  - 2021: S=0.40 (weak), ret=+2.4%
  - 2022: S=0.69 (moderate), ret=+5.2%
  - 2023: S=-0.32 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 9.23% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 6.4% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.18, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 1.66, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +3.78%; worst month: -4.89%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.27
- Sideways: S=-0.02
- Bear: S=-1.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netdebt_mean, 5))` S=0.53, F=0.23, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_mean)`: S=0.23, F=0.09, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_mean / close)`: S=0.15, F=0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_mean, 5))`: S=0.53, F=0.23, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netdebt_mean / close)` | TOP3000 | 0.36 | 0.15 | 9.2% | 80% | bull-only |
| `rank(ts_delta(anl4_netdebt_mean, 5))` | TOP500 | 0.45 | 0.14 | 16.4% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_netdebt_median: 1.000 (strongly positively correlated)
- anl4_netdebt_high: 0.997 (strongly positively correlated)
- anl4_netdebt_low: 0.997 (strongly positively correlated)
- est_netdebt: 0.921 (strongly positively correlated)
- net_debt_reported_value: 0.887 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
