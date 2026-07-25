---
field: anl4_netdebt_high
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.32
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0922
ann_vol: 0.0637
hit_rate: 0.4883
rolling_sharpe_min: -1.105
rolling_sharpe_max: 1.658
negated_best_sharpe: 0.32
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.03
---
# anl4_netdebt_high (analyst4)

*Net debt - the highest estimation*

## Signal Profile
- `rank(anl4_netdebt_high)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(anl4_netdebt_high / close)`: S=0.35, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netdebt_high, 5))`: S=0.23, F=0.05, T=35.3%, INFERIOR (TOP500)
- `-rank(anl4_netdebt_high)`: S=0.17, F=0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_high, 5))`: S=0.18, F=0.05, T=34.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_netdebt_high, 63)`: S=0.24, F=0.07, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_netdebt_high, 10)`: S=-0.36, F=-0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netdebt_high, 22))`: S=-0.57, F=-0.25, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_high)`: S=0.29, F=0.13, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_high / close)`: S=0.32, F=0.16, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+1.8%
  - 2020: S=0.30 (weak), ret=+2.4%
  - 2021: S=0.40 (weak), ret=+2.4%
  - 2022: S=0.76 (moderate), ret=+5.6%
  - 2023: S=-0.28 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 9.22% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 6.4% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.19, excess kurtosis +1.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 1.66, latest -0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +3.88%; worst month: -5.06%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.28
- Sideways: S=-0.05
- Bear: S=-1.30

## Negated Direction
Best negated: `rank(-1 * anl4_netdebt_high / close)` S=0.32, F=0.16, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netdebt_high)`: S=0.29, F=0.13, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netdebt_high / close)`: S=0.32, F=0.16, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netdebt_high, 5))`: S=0.18, F=0.05, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netdebt_high / close)` | TOP3000 | 0.35 | 0.15 | 9.2% | 80% | bull-only |
| `rank(ts_delta(anl4_netdebt_high, 5))` | TOP500 | 0.23 | 0.05 | 18.9% | 40% | bull-only |
| `rank(ts_delta(anl4_netdebt_high, 5))` | TOP1000 | 0.23 | 0.05 | 18.5% | 60% | weak |
| `rank(ts_delta(anl4_netdebt_high, 5))` | TOP3000 | 0.17 | 0.03 | 14.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_netdebt_median: 0.998 (strongly positively correlated)
- anl4_netdebt_mean: 0.997 (strongly positively correlated)
- anl4_netdebt_low: 0.992 (strongly positively correlated)
- est_netdebt: 0.920 (strongly positively correlated)
- net_debt_reported_value: 0.886 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
