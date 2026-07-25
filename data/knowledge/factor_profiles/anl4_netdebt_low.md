---
field: anl4_netdebt_low
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.62
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.0912
ann_vol: 0.063
hit_rate: 0.4858
rolling_sharpe_min: -1.124
rolling_sharpe_max: 1.682
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.27
---
# anl4_netdebt_low (analyst4)

*Net debt - the lowest estimation*

## Signal Profile
- `rank(anl4_netdebt_low)`: S=0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(anl4_netdebt_low / close)`: S=0.39, F=0.17, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netdebt_low, 5))`: S=0.21, F=0.05, T=35.2%, INFERIOR (TOP500)
- `-rank(anl4_netdebt_low)`: S=0.16, F=0.04, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_low, 5))`: S=0.35, F=0.13, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_low, 63)`: S=0.62, F=0.27, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_low, 10)`: S=-0.39, F=-0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_low, 22))`: S=-0.89, F=-0.50, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_low)`: S=0.24, F=0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_low / close)`: S=0.22, F=0.09, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.70 (moderate), ret=+2.9%
  - 2020: S=0.39 (weak), ret=+3.0%
  - 2021: S=0.40 (weak), ret=+2.4%
  - 2022: S=0.69 (moderate), ret=+5.2%
  - 2023: S=-0.37 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 9.12% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.4%, volatility 6.3% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.17, excess kurtosis +1.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 1.68, latest -0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +3.77%; worst month: -4.67%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.29
- Sideways: S=0.01
- Bear: S=-1.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netdebt_low, 5))` S=0.35, F=0.13, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_low)`: S=0.24, F=0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_low / close)`: S=0.22, F=0.09, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_low, 5))`: S=0.35, F=0.13, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netdebt_low / close)` | TOP3000 | 0.38 | 0.17 | 9.1% | 80% | bull-only |
| `rank(ts_delta(anl4_netdebt_low, 5))` | TOP500 | 0.20 | 0.05 | 19.7% | 60% | mixed |
| `rank(anl4_netdebt_low / close)` | TOP500 | 0.07 | 0.02 | 11.6% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_netdebt_mean: 0.997 (strongly positively correlated)
- anl4_netdebt_median: 0.997 (strongly positively correlated)
- anl4_netdebt_high: 0.992 (strongly positively correlated)
- est_netdebt: 0.916 (strongly positively correlated)
- net_debt_reported_value: 0.884 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
