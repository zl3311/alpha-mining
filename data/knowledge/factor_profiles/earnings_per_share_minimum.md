---
field: earnings_per_share_minimum
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.81
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1067
ann_vol: 0.034
hit_rate: 0.5174
rolling_sharpe_min: -2.436
rolling_sharpe_max: 2.062
negated_best_sharpe: 0.23
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.58
---
# earnings_per_share_minimum (analyst4)

*Earnings per share - The lowest estimation*

## Signal Profile
- `rank(earnings_per_share_minimum)`: S=0.38, F=0.23, T=1.3%, INFERIOR (TOP3000)
- `rank(earnings_per_share_minimum / close)`: S=0.81, F=0.64, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_minimum, 5))`: S=0.19, F=0.03, T=35.9%, INFERIOR (TOP3000)
- `-rank(earnings_per_share_minimum)`: S=-0.16, F=-0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_minimum, 5))`: S=0.23, F=0.04, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_minimum, 22)`: S=0.35, F=0.09, T=34.6%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_minimum, 10)`: S=-0.11, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_minimum, 22))`: S=0.06, F=0.01, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_minimum)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_minimum / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+1.8%
  - 2020: S=-1.67 (negative), ret=-5.2%
  - 2021: S=0.83 (moderate), ret=+2.9%
  - 2022: S=0.92 (moderate), ret=+4.0%
  - 2023: S=-0.14 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 10.67% over 1083 days (recovered)
- Annualized: return +0.6%, volatility 3.4% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.16, excess kurtosis +0.82

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.44, max 2.06, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.66%; worst month: -1.74%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.42
- Sideways: S=1.08
- Bear: S=-1.93

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_minimum, 5))` S=0.23, F=0.04, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_minimum)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_minimum / close)`: S=-0.03, F=-0.01, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_minimum, 5))`: S=0.23, F=0.04, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(earnings_per_share_minimum, 5))` | TOP3000 | 0.18 | 0.03 | 10.7% | 60% | bull-only |
| `rank(ts_delta(earnings_per_share_minimum, 5))` | TOP200 | 0.11 | 0.02 | 17.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_maximum: 0.725 (strongly positively correlated)
- earnings_per_share_median_value: 0.579 (moderately positively correlated)
- income: 0.569 (moderately positively correlated)
- fnd6_mfmq_ibcomq: 0.569 (moderately positively correlated)
- fnd6_newqv1300_cibegniq: 0.561 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
