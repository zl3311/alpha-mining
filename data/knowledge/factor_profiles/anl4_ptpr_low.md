---
field: anl4_ptpr_low
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.42
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2892
ann_vol: 0.1082
hit_rate: 0.5085
rolling_sharpe_min: -3.492
rolling_sharpe_max: 2.105
negated_best_sharpe: 0.42
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.12
---
# anl4_ptpr_low (analyst4)

*Reported Pretax Income - The Lowest Estimation*

## Signal Profile
- `rank(anl4_ptpr_low)`: S=0.14, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptpr_low / close)`: S=0.30, F=0.15, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptpr_low, 5))`: S=0.23, F=0.05, T=36.8%, INFERIOR (TOP500)
- `-rank(anl4_ptpr_low)`: S=0.11, F=0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_low, 5))`: S=-0.23, F=-0.05, T=36.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ptpr_low, 63)`: S=-0.13, F=-0.03, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptpr_low, 10)`: S=-0.09, F=-0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptpr_low, 22))`: S=-0.19, F=-0.04, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_low)`: S=0.35, F=0.21, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_low / close)`: S=0.42, F=0.26, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.00 (negative), ret=-0.0%
  - 2020: S=-2.70 (negative), ret=-18.5%
  - 2021: S=0.89 (moderate), ret=+10.6%
  - 2022: S=1.48 (moderate), ret=+23.0%
  - 2023: S=0.04 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 28.92% over 827 days (recovered)
- Annualized: return +3.2%, volatility 10.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.15, excess kurtosis +1.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.49, max 2.10, latest -0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.05%; worst month: -6.43%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.73
- Bear: S=-3.59

## Negated Direction
Best negated: `rank(-1 * anl4_ptpr_low / close)` S=0.42, F=0.26, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ptpr_low)`: S=0.35, F=0.21, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_low / close)`: S=0.42, F=0.26, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_low, 5))`: S=-0.23, F=-0.05, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptpr_low / close)` | TOP3000 | 0.29 | 0.15 | 28.9% | 60% | bull-only |
| `rank(anl4_ptpr_low)` | TOP3000 | 0.14 | 0.05 | 42.3% | 60% | bull-only |
| `rank(ts_delta(anl4_ptpr_low, 5))` | TOP500 | 0.23 | 0.05 | 19.3% | 60% | weak |
| `rank(ts_delta(anl4_ptpr_low, 5))` | TOP1000 | 0.16 | 0.03 | 17.4% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_ptpr_mean: 0.998 (strongly positively correlated)
- anl4_ptpr_median: 0.998 (strongly positively correlated)
- est_ptpr: 0.970 (strongly positively correlated)
- anl4_ptp_low: 0.948 (strongly positively correlated)
- anl4_netprofit_low: 0.945 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
