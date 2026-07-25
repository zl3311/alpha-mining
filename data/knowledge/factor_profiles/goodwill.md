---
field: goodwill
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.51
best_fitness: 0.27
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.171
ann_vol: 0.0799
hit_rate: 0.4972
rolling_sharpe_min: -2.051
rolling_sharpe_max: 2.184
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.27
---
# goodwill (fundamental6)

*Goodwill (net)*

## Signal Profile
- `rank(goodwill)`: S=0.35, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(goodwill / close)`: S=0.42, F=0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(goodwill, 5))`: S=-0.01, F=0.00, T=38.3%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(goodwill), 5)`: S=0.35, F=0.19, T=2.1%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(goodwill), ts_std_dev(returns,20)<0.01)`: S=0.27, F=0.12, T=2.6%, INFERIOR (TOP3000)
- `-rank(goodwill)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(goodwill, 5))`: S=0.24, F=0.06, T=37.7%, INFERIOR (TOP3000)
- `ts_zscore(goodwill, 22)`: S=0.51, F=0.27, T=38.1%, INFERIOR (TOP3000)
- `ts_mean(goodwill, 10)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(goodwill, 22))`: S=0.23, F=0.06, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * goodwill)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * goodwill / close)`: S=-0.12, F=-0.04, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/26P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.79 (moderate), ret=+3.2%
  - 2020: S=-0.96 (negative), ret=-6.3%
  - 2021: S=1.01 (moderate), ret=+12.0%
  - 2022: S=1.01 (moderate), ret=+9.4%
  - 2023: S=-0.49 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 17.10% over 551 days (recovered)
- Annualized: return +3.3%, volatility 8.0% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.17, excess kurtosis +2.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.05, max 2.18, latest -0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.27%; worst month: -3.64%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.71
- Sideways: S=0.61
- Bear: S=-2.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(goodwill, 5))` S=0.24, F=0.06, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * goodwill)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * goodwill / close)`: S=-0.12, F=-0.04, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(goodwill, 5))`: S=0.24, F=0.06, T=37.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(goodwill / close)` | TOP3000 | 0.41 | 0.22 | 17.1% | 60% | bull-only |
| `rank(goodwill)` | TOP3000 | 0.34 | 0.19 | 29.3% | 60% | bull-only |
| `ts_decay_linear(rank(goodwill), 5)` | TOP3000 | 0.34 | 0.19 | 29.4% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(goodwill), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.26 | 0.12 | 31.4% | 60% | bull-only |
| `rank(goodwill / close)` | TOP1000 | 0.11 | 0.04 | 21.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_gdwlq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_intanq: 0.975 (strongly positively correlated)
- fnd6_intan: 0.969 (strongly positively correlated)
- fnd6_newa1v1300_intano: 0.937 (strongly positively correlated)
- fnd6_am: 0.935 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
