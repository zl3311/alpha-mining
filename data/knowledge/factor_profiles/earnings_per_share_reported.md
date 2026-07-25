---
field: earnings_per_share_reported
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.31
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.2815
ann_vol: 0.1067
hit_rate: 0.502
rolling_sharpe_min: -3.517
rolling_sharpe_max: 2.46
negated_best_sharpe: 0.31
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.0
---
# earnings_per_share_reported (analyst4)

*Reported Earnings Per Share - Actual Value*

## Signal Profile
- `rank(earnings_per_share_reported)`: S=0.09, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(earnings_per_share_reported / close)`: S=0.31, F=0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_reported, 5))`: S=-0.01, F=0.00, T=34.9%, INFERIOR (TOP3000)
- `-rank(earnings_per_share_reported)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_reported, 5))`: S=0.30, F=0.07, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(earnings_per_share_reported, 63)`: S=0.18, F=0.04, T=20.5%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_reported, 10)`: S=0.15, F=0.05, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_reported, 22))`: S=-0.19, F=-0.05, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported)`: S=0.26, F=0.13, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported / close)`: S=0.31, F=0.17, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=-2.43 (negative), ret=-15.8%
  - 2021: S=0.93 (moderate), ret=+10.9%
  - 2022: S=1.28 (moderate), ret=+20.5%
  - 2023: S=-0.09 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 28.15% over 815 days (recovered)
- Annualized: return +3.1%, volatility 10.7% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.05, excess kurtosis +1.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.52, max 2.46, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.37%; worst month: -6.14%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=0.41
- Bear: S=-3.40

## Negated Direction
Best negated: `rank(-1 * earnings_per_share_reported / close)` S=0.31, F=0.17, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * earnings_per_share_reported)`: S=0.26, F=0.13, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_reported / close)`: S=0.31, F=0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_reported, 5))`: S=0.30, F=0.07, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_reported / close)` | TOP3000 | 0.29 | 0.16 | 28.1% | 60% | bull-only |
| `rank(earnings_per_share_reported)` | TOP3000 | 0.08 | 0.03 | 41.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_oprepsx: 0.972 (strongly positively correlated)
- fnd6_mfma2_opeps: 0.972 (strongly positively correlated)
- fnd6_newa2v1300_opeps: 0.971 (strongly positively correlated)
- pretax_income_total: 0.966 (strongly positively correlated)
- fnd6_newqv1300_oepf12: 0.965 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
