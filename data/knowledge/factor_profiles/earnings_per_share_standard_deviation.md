---
field: earnings_per_share_standard_deviation
dataset: analyst4
best_template: rank_level
best_sharpe: 1.18
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1112
ann_vol: 0.0598
hit_rate: 0.5231
rolling_sharpe_min: -1.27
rolling_sharpe_max: 1.976
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.8
---
# earnings_per_share_standard_deviation (analyst4)

*Earnings per share - standard deviation of estimations*

## Signal Profile
- `rank(earnings_per_share_standard_deviation)`: S=1.18, F=0.73, T=4.6%, INFERIOR (TOP3000)
- `rank(earnings_per_share_standard_deviation / close)`: S=0.53, F=0.36, T=7.4%, INFERIOR (TOP200)
- `rank(ts_delta(earnings_per_share_standard_deviation, 5))`: S=0.29, F=0.06, T=38.8%, INFERIOR (TOP500)
- `-rank(earnings_per_share_standard_deviation)`: S=-0.33, F=-0.12, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_standard_deviation, 5))`: S=0.38, F=0.12, T=38.4%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_standard_deviation, 22)`: S=0.65, F=0.21, T=33.2%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_standard_deviation, 10)`: S=0.12, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_standard_deviation, 22))`: S=0.57, F=0.20, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_standard_deviation)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_standard_deviation / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+2.9%
  - 2020: S=-0.32 (negative), ret=-1.6%
  - 2021: S=-0.00 (negative), ret=-0.0%
  - 2022: S=0.09 (weak), ret=+0.5%
  - 2023: S=0.98 (moderate), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 11.12% over 919 days (recovered)
- Annualized: return +1.7%, volatility 6.0% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.43, excess kurtosis +3.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 1.98, latest 1.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +3.26%; worst month: -2.81%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.94
- Sideways: S=-0.19
- Bear: S=0.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_standard_deviation, 5))` S=0.38, F=0.12, INFERIOR
Direction gap: -0.80 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_standard_deviation)`: S=-0.25, F=-0.11, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_standard_deviation / close)`: S=-0.53, F=-0.36, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_standard_deviation, 5))`: S=0.38, F=0.12, T=38.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(earnings_per_share_standard_deviation, 5))` | TOP500 | 0.28 | 0.06 | 11.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_credit_ratings: -0.198 (weakly negatively correlated)
- earnings_per_share_maximum: 0.141 (weakly positively correlated)
- fnd6_newa1v1300_ano: 0.140 (weakly positively correlated)
- min_net_debt_guidance: 0.118 (weakly positively correlated)
- max_net_debt_guidance: 0.118 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
