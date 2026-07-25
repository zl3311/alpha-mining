---
field: anl4_netprofita_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.6
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0867
ann_vol: 0.0269
hit_rate: 0.5093
rolling_sharpe_min: -2.687
rolling_sharpe_max: 3.299
negated_best_sharpe: 0.31
negated_best_template: rank_neg_delta
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.29
---
# anl4_netprofita_number (analyst4)

*Adjusted net income - number of estimations*

## Signal Profile
- `rank(anl4_netprofita_number)`: S=0.58, F=0.20, T=2.8%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_number / close)`: S=0.35, F=0.16, T=3.4%, INFERIOR (TOP500)
- `rank(ts_delta(anl4_netprofita_number, 5))`: S=0.51, F=0.12, T=35.8%, INFERIOR (TOP3000)
- `-rank(anl4_netprofita_number)`: S=-0.42, F=-0.15, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_number, 5))`: S=0.31, F=0.10, T=34.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofita_number, 22)`: S=0.47, F=0.15, T=36.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_number, 10)`: S=0.60, F=0.27, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_number, 22))`: S=-0.14, F=-0.03, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_number)`: S=-0.06, F=-0.01, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_number / close)`: S=-0.30, F=-0.14, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+1.3%
  - 2020: S=-1.65 (negative), ret=-4.3%
  - 2021: S=0.67 (moderate), ret=+2.1%
  - 2022: S=2.88 (strong), ret=+8.3%
  - 2023: S=0.07 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 8.67% over 862 days (recovered)
- Annualized: return +1.6%, volatility 2.7% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.18, excess kurtosis +1.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.69, max 3.30, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +1.80%; worst month: -2.56%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.07
- Sideways: S=0.46
- Bear: S=-0.95

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_netprofita_number, 5))` S=0.31, F=0.10, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_netprofita_number)`: S=-0.06, F=-0.01, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_number / close)`: S=-0.30, F=-0.14, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_number, 5))`: S=0.31, F=0.10, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_netprofita_number)` | TOP3000 | 0.57 | 0.20 | 8.7% | 80% | bull-only |
| `rank(anl4_netprofita_number / close)` | TOP500 | 0.36 | 0.16 | 22.6% | 80% | mixed |
| `rank(anl4_netprofita_number)` | TOP1000 | 0.44 | 0.15 | 11.3% | 80% | bull-only |
| `rank(anl4_netprofita_number / close)` | TOP200 | 0.32 | 0.14 | 22.3% | 60% | mixed |
| `rank(ts_delta(anl4_netprofita_number, 5))` | TOP3000 | 0.54 | 0.12 | 9.1% | 80% | mixed |
| `rank(anl4_netprofita_number / close)` | TOP1000 | 0.24 | 0.10 | 22.0% | 60% | bear-only |
| `rank(anl4_netprofita_number)` | TOP500 | 0.26 | 0.07 | 13.6% | 60% | bull-only |
| `rank(anl4_netprofita_number / close)` | TOP3000 | 0.10 | 0.03 | 35.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- cap: 0.632 (moderately positively correlated)
- anl4_netprofit_number: 0.615 (moderately positively correlated)
- sga_expense: 0.614 (moderately positively correlated)
- fnd6_newqv1300_xsgaq: 0.614 (moderately positively correlated)
- call_breakeven_360: 0.614 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
