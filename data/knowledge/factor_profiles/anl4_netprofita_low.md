---
field: anl4_netprofita_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.246
ann_vol: 0.0909
hit_rate: 0.4988
rolling_sharpe_min: -3.243
rolling_sharpe_max: 2.473
negated_best_sharpe: 0.22
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.23
---
# anl4_netprofita_low (analyst4)

*Adjusted net income - the lowest estimation*

## Signal Profile
- `rank(anl4_netprofita_low)`: S=0.26, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_low / close)`: S=0.45, F=0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofita_low, 5))`: S=0.13, F=0.02, T=35.8%, INFERIOR (TOP200)
- `-rank(anl4_netprofita_low)`: S=-0.03, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_low, 5))`: S=0.22, F=0.04, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofita_low, 22)`: S=-0.03, F=0.00, T=35.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_low, 10)`: S=0.03, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_low, 22))`: S=0.15, F=0.03, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_low)`: S=-0.03, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_low / close)`: S=-0.14, F=-0.05, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+1.7%
  - 2020: S=-2.45 (negative), ret=-14.8%
  - 2021: S=1.02 (moderate), ret=+11.5%
  - 2022: S=1.81 (strong), ret=+22.8%
  - 2023: S=-0.20 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 24.60% over 812 days (recovered)
- Annualized: return +4.0%, volatility 9.1% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.03, excess kurtosis +1.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.24, max 2.47, latest -0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.89%; worst month: -4.38%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.13
- Sideways: S=0.92
- Bear: S=-3.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofita_low, 5))` S=0.22, F=0.04, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofita_low)`: S=-0.03, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_low / close)`: S=-0.14, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_low, 5))`: S=0.22, F=0.04, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofita_low / close)` | TOP3000 | 0.44 | 0.26 | 24.6% | 60% | bull-only |
| `rank(anl4_netprofita_low)` | TOP3000 | 0.25 | 0.13 | 39.8% | 60% | bull-only |
| `rank(anl4_netprofita_low / close)` | TOP1000 | 0.13 | 0.05 | 29.3% | 60% | bull-only |
| `rank(ts_delta(anl4_netprofita_low, 5))` | TOP200 | 0.13 | 0.02 | 27.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_netprofita_mean: 0.996 (strongly positively correlated)
- anl4_netprofita_median: 0.995 (strongly positively correlated)
- est_netprofit_adj: 0.988 (strongly positively correlated)
- anl4_netprofita_high: 0.986 (strongly positively correlated)
- anl4_netprofit_mean: 0.984 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
