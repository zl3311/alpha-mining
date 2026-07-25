---
field: earnings_per_share_nongaap_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.43
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2545
ann_vol: 0.1022
hit_rate: 0.5045
rolling_sharpe_min: -3.074
rolling_sharpe_max: 3.006
negated_best_sharpe: 0.33
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.1
---
# earnings_per_share_nongaap_value (analyst4)

*Non-GAAP Earnings Per Share - Actual Value*

## Signal Profile
- `rank(earnings_per_share_nongaap_value)`: S=0.16, F=0.06, T=2.3%, INFERIOR (TOP1000)
- `rank(earnings_per_share_nongaap_value / close)`: S=0.43, F=0.25, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_nongaap_value, 5))`: S=-0.16, F=-0.02, T=36.9%, INFERIOR (TOP1000)
- `-rank(earnings_per_share_nongaap_value)`: S=-0.16, F=-0.06, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_nongaap_value, 5))`: S=0.27, F=0.07, T=36.5%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_nongaap_value, 22)`: S=-0.19, F=-0.04, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_nongaap_value, 10)`: S=0.04, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_nongaap_value, 22))`: S=-0.02, F=0.00, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_nongaap_value)`: S=0.28, F=0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_nongaap_value / close)`: S=0.33, F=0.21, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.22 (weak), ret=+0.9%
  - 2020: S=-2.69 (negative), ret=-17.8%
  - 2021: S=1.88 (strong), ret=+21.5%
  - 2022: S=1.39 (moderate), ret=+21.3%
  - 2023: S=-0.56 (negative), ret=-4.9%

## Risk & Drawdown
- Max drawdown: 25.45% over 765 days (recovered)
- Annualized: return +4.3%, volatility 10.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.08, excess kurtosis +1.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.07, max 3.01, latest -0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.94%; worst month: -5.89%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.94
- Sideways: S=0.43
- Bear: S=-2.94

## Negated Direction
Best negated: `rank(-1 * earnings_per_share_nongaap_value / close)` S=0.33, F=0.21, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * earnings_per_share_nongaap_value)`: S=0.28, F=0.15, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_nongaap_value / close)`: S=0.33, F=0.21, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_nongaap_value, 5))`: S=0.27, F=0.07, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(earnings_per_share_nongaap_value / close)` | TOP3000 | 0.42 | 0.25 | 25.4% | 60% | bull-only |
| `rank(earnings_per_share_nongaap_value / close)` | TOP1000 | 0.30 | 0.17 | 28.1% | 60% | bull-only |
| `rank(earnings_per_share_nongaap_value)` | TOP1000 | 0.15 | 0.06 | 38.6% | 60% | bull-only |
| `rank(earnings_per_share_nongaap_value)` | TOP3000 | 0.12 | 0.04 | 43.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- actual_eps_value_quarterly: 0.976 (strongly positively correlated)
- fnd6_newqv1300_oepsxq: 0.945 (strongly positively correlated)
- fnd6_cptmfmq_opepsq: 0.945 (strongly positively correlated)
- fnd6_cptnewqv1300_opepsq: 0.945 (strongly positively correlated)
- fnd6_newqv1300_oepf12: 0.944 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
