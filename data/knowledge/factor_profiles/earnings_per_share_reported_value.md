---
field: earnings_per_share_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.31
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3823
ann_vol: 0.1091
hit_rate: 0.4996
rolling_sharpe_min: -4.577
rolling_sharpe_max: 2.949
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: 0.12
---
# earnings_per_share_reported_value (analyst4)

*Reported Earnings Per Share - Actual Value*

## Signal Profile
- `rank(earnings_per_share_reported_value)`: S=0.21, F=0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(earnings_per_share_reported_value / close)`: S=0.31, F=0.16, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_reported_value, 5))`: S=-0.03, F=0.00, T=36.1%, INFERIOR (TOP200)
- `-rank(earnings_per_share_reported_value)`: S=-0.16, F=-0.06, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_reported_value, 5))`: S=0.43, F=0.09, T=36.0%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_reported_value, 22)`: S=-0.30, F=-0.07, T=37.2%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_reported_value, 10)`: S=0.22, F=0.10, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_reported_value, 22))`: S=0.12, F=0.02, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported_value)`: S=-0.21, F=-0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported_value / close)`: S=-0.31, F=-0.16, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.08 (negative), ret=-0.3%
  - 2020: S=-3.96 (negative), ret=-27.1%
  - 2021: S=1.58 (strong), ret=+17.9%
  - 2022: S=1.84 (strong), ret=+29.8%
  - 2023: S=-0.37 (negative), ret=-4.0%

## Risk & Drawdown
- Max drawdown: 38.23% over 847 days (recovered)
- Annualized: return +3.3%, volatility 10.9% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.16, excess kurtosis +1.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.58, max 2.95, latest -0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.83%; worst month: -10.18%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.55
- Bear: S=-3.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_reported_value, 5))` S=0.43, F=0.09, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * earnings_per_share_reported_value)`: S=-0.21, F=-0.09, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported_value / close)`: S=-0.31, F=-0.16, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_reported_value, 5))`: S=0.43, F=0.09, T=36.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_reported_value / close)` | TOP3000 | 0.30 | 0.16 | 38.2% | 40% | bull-only |
| `rank(earnings_per_share_reported_value)` | TOP3000 | 0.20 | 0.09 | 42.8% | 60% | bull-only |
| `rank(earnings_per_share_reported_value)` | TOP1000 | 0.15 | 0.06 | 38.5% | 60% | bull-only |
| `rank(earnings_per_share_reported_value / close)` | TOP1000 | 0.15 | 0.06 | 32.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_epsr_value: 1.000 (strongly positively correlated)
- eps: 0.991 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.991 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.991 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.991 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
