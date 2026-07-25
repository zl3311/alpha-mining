---
field: fnd6_fatn
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.65
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.2907
ann_vol: 0.1094
hit_rate: 0.515
rolling_sharpe_min: -2.112
rolling_sharpe_max: 2.521
negated_best_sharpe: 0.03
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.62
---
# fnd6_fatn (fundamental6)

*Property, Plant, and Equipment - Natural Resources at Cost*

## Signal Profile
- `rank(fnd6_fatn)`: S=0.65, F=0.49, T=2.7%, INFERIOR (TOP3000)
- `rank(fnd6_fatn / close)`: S=0.65, F=0.49, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_fatn, 5))`: S=0.61, F=0.39, T=7.0%, INFERIOR (TOP3000)
- `-rank(fnd6_fatn)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatn, 5))`: S=0.06, F=0.01, T=6.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fatn, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_fatn, 10)`: S=0.37, F=0.25, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fatn, 22))`: S=0.16, F=0.06, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatn)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatn / close)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.63 (negative), ret=-17.4%
  - 2020: S=0.11 (weak), ret=+1.3%
  - 2021: S=1.82 (strong), ret=+20.6%
  - 2022: S=1.73 (strong), ret=+18.9%
  - 2023: S=1.38 (moderate), ret=+12.0%

## Risk & Drawdown
- Max drawdown: 29.07% over 828 days (recovered)
- Annualized: return +7.2%, volatility 10.9% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.09, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.11, max 2.52, latest 1.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.28%; worst month: -6.75%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.89
- Sideways: S=0.13
- Bear: S=0.97

## Negated Direction
Best negated: `-rank(fnd6_fatn)` S=0.03, F=0.01, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_fatn)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatn / close)`: S=0.03, F=0.01, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatn, 5))`: S=0.06, F=0.01, T=6.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fatn / close)` | TOP3000 | 0.66 | 0.49 | 29.1% | 80% | all-weather |
| `rank(fnd6_fatn)` | TOP3000 | 0.66 | 0.49 | 29.1% | 80% | all-weather |
| `rank(ts_delta(fnd6_fatn, 5))` | TOP3000 | 0.60 | 0.39 | 9.4% | 80% | mixed |
| `rank(ts_delta(fnd6_fatn, 5))` | TOP200 | 0.08 | 0.03 | 34.7% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fscore_bfl_value: 0.223 (weakly positively correlated)
- anl4_qf_az_cfps_median: 0.208 (weakly positively correlated)
- anl4_qfd1_az_cfps_median: 0.208 (weakly positively correlated)
- anl4_qf_az_cfps_mean: 0.208 (weakly positively correlated)
- cashflow_per_share_average: 0.208 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
