---
field: earnings_per_share_maximum
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1116
ann_vol: 0.035
hit_rate: 0.5126
rolling_sharpe_min: -2.33
rolling_sharpe_max: 2.073
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.53
---
# earnings_per_share_maximum (analyst4)

*Earnings per share - The highest estimation*

## Signal Profile
- `rank(earnings_per_share_maximum)`: S=0.44, F=0.28, T=1.2%, INFERIOR (TOP3000)
- `rank(earnings_per_share_maximum / close)`: S=1.01, F=0.85, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_maximum, 5))`: S=0.15, F=0.02, T=35.5%, INFERIOR (TOP3000)
- `-rank(earnings_per_share_maximum)`: S=-0.18, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_maximum, 5))`: S=0.48, F=0.16, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_maximum, 22)`: S=0.36, F=0.09, T=35.0%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_maximum, 10)`: S=-0.09, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_maximum, 22))`: S=0.38, F=0.13, T=14.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_maximum)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_maximum / close)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.15, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.21 (negative), ret=-0.5%
  - 2020: S=-1.85 (negative), ret=-6.6%
  - 2021: S=1.28 (moderate), ret=+4.6%
  - 2022: S=1.44 (moderate), ret=+6.0%
  - 2023: S=-0.29 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 11.16% over 1148 days (recovered)
- Annualized: return +0.5%, volatility 3.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.24, excess kurtosis +0.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.33, max 2.07, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.22%; worst month: -1.91%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.78
- Sideways: S=0.23
- Bear: S=-1.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_maximum, 5))` S=0.48, F=0.16, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_maximum)`: S=0.02, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_maximum / close)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_maximum, 5))`: S=0.48, F=0.16, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(earnings_per_share_maximum, 5))` | TOP3000 | 0.15 | 0.02 | 11.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_minimum: 0.725 (strongly positively correlated)
- put_breakeven_1080: 0.615 (moderately positively correlated)
- low: 0.615 (moderately positively correlated)
- put_breakeven_720: 0.614 (moderately positively correlated)
- put_breakeven_270: 0.614 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
