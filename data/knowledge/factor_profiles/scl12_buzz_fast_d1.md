---
field: scl12_buzz_fast_d1
dataset: socialmedia12
best_template: rank_level
best_sharpe: 0.51
best_fitness: 0.14
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2006
ann_vol: 0.0818
hit_rate: 0.5198
rolling_sharpe_min: -1.845
rolling_sharpe_max: 2.243
redundancy_cluster: 97
negated_best_sharpe: 0.25
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.26
---
# scl12_buzz_fast_d1 (socialmedia12)

*relative sentiment volume*

## Signal Profile
- `rank(scl12_buzz_fast_d1)`: S=0.51, F=0.14, T=56.3%, INFERIOR (TOP200)
- `rank(ts_delta(scl12_buzz_fast_d1, 5))`: S=0.17, F=0.03, T=62.8%, INFERIOR (TOP200)
- `-rank(scl12_buzz_fast_d1)`: S=0.25, F=0.04, T=51.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_buzz_fast_d1, 5))`: S=0.16, F=0.02, T=70.6%, INFERIOR (TOP3000)
- `ts_zscore(scl12_buzz_fast_d1, 22)`: S=0.23, F=0.03, T=60.7%, INFERIOR (TOP3000)
- `ts_mean(scl12_buzz_fast_d1, 10)`: S=-0.39, F=-0.19, T=20.0%, INFERIOR (TOP3000)
- `rank(ts_rank(scl12_buzz_fast_d1, 22))`: S=-0.01, F=0.00, T=65.6%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz_fast_d1)`: S=0.25, F=0.04, T=51.1%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz_fast_d1 / close)`: S=0.14, F=0.03, T=34.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- HIGH_TURNOVER: 7F/19P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.06 (weak), ret=+0.4%
  - 2020: S=0.35 (weak), ret=+2.5%
  - 2021: S=-0.98 (negative), ret=-9.4%
  - 2022: S=1.51 (strong), ret=+15.6%
  - 2023: S=1.87 (strong), ret=+11.3%

## Risk & Drawdown
- Max drawdown: 20.06% over 804 days (recovered)
- Annualized: return +4.2%, volatility 8.2% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.69, excess kurtosis +9.52

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.84, max 2.24, latest 1.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +9.86%; worst month: -8.38%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.37
- Sideways: S=0.56
- Bear: S=0.65

## Negated Direction
Best negated: `-rank(scl12_buzz_fast_d1)` S=0.25, F=0.04, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * scl12_buzz_fast_d1)`: S=0.25, F=0.04, T=51.1%, INFERIOR (TOP3000)
- `rank(-1 * scl12_buzz_fast_d1 / close)`: S=0.14, F=0.03, T=34.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(scl12_buzz_fast_d1, 5))`: S=0.16, F=0.02, T=70.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(scl12_buzz_fast_d1)` | TOP200 | 0.51 | 0.14 | 20.1% | 80% | mixed |
| `rank(ts_delta(scl12_buzz_fast_d1, 5))` | TOP200 | 0.14 | 0.03 | 23.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- scl12_buzz: 0.755 (strongly positively correlated)
- snt_buzz: -0.590 (moderately negatively correlated)
- news_vol_stddev: 0.354 (weakly positively correlated)
- implied_volatility_put_10: 0.335 (weakly positively correlated)
- implied_volatility_mean_10: 0.335 (weakly positively correlated)

Redundancy cluster #97: 2 similar fields, mean |rho| 0.755 (representative: scl12_buzz). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
