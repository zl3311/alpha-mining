---
field: anl4_totassets_std
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.67
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1451
ann_vol: 0.1373
hit_rate: 0.5126
rolling_sharpe_min: -0.27
rolling_sharpe_max: 2.678
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.23
---
# anl4_totassets_std (analyst4)

*Total Assets - standard deviation of estimations*

## Signal Profile
- `rank(anl4_totassets_std)`: S=0.48, F=0.23, T=4.7%, INFERIOR (TOP3000)
- `rank(anl4_totassets_std / close)`: S=0.31, F=0.12, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_totassets_std, 5))`: S=0.67, F=0.34, T=36.1%, INFERIOR (TOP200)
- `-rank(anl4_totassets_std)`: S=-0.04, F=-0.01, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_std, 5))`: S=0.44, F=0.11, T=39.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_totassets_std, 22)`: S=0.37, F=0.12, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_totassets_std, 10)`: S=-0.11, F=-0.03, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totassets_std, 22))`: S=0.35, F=0.13, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_std)`: S=-0.48, F=-0.23, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_std / close)`: S=-0.31, F=-0.12, T=4.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.68, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-1.3%
  - 2020: S=0.08 (weak), ret=+1.3%
  - 2021: S=1.33 (moderate), ret=+16.9%
  - 2022: S=1.88 (strong), ret=+25.9%
  - 2023: S=0.20 (weak), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 14.51% over 441 days (recovered)
- Annualized: return +9.3%, volatility 13.7% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.45, excess kurtosis +2.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.27, max 2.68, latest 0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +11.09%; worst month: -5.97%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.16
- Sideways: S=0.13
- Bear: S=0.74

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totassets_std, 5))` S=0.44, F=0.11, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_totassets_std)`: S=-0.48, F=-0.23, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totassets_std / close)`: S=-0.31, F=-0.12, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totassets_std, 5))`: S=0.44, F=0.11, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_totassets_std, 5))` | TOP200 | 0.68 | 0.34 | 14.5% | 80% | all-weather |
| `rank(anl4_totassets_std)` | TOP3000 | 0.47 | 0.23 | 14.4% | 60% | bull-only |
| `rank(anl4_totassets_std)` | TOP200 | 0.34 | 0.20 | 40.6% | 60% | bull-only |
| `rank(anl4_totassets_std / close)` | TOP3000 | 0.31 | 0.12 | 16.0% | 60% | mixed |
| `rank(anl4_totassets_std / close)` | TOP500 | 0.23 | 0.09 | 25.4% | 60% | mixed |
| `rank(anl4_totassets_std)` | TOP500 | 0.20 | 0.08 | 27.1% | 60% | bull-only |
| `rank(anl4_totassets_std / close)` | TOP1000 | 0.16 | 0.05 | 17.5% | 60% | mixed |
| `rank(ts_delta(anl4_totassets_std, 5))` | TOP500 | 0.19 | 0.05 | 20.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- historical_volatility_120: 0.117 (weakly positively correlated)
- fn_derivative_fair_value_of_derivative_liability_q: -0.109 (weakly negatively correlated)
- fnd6_newqv1300_anoq: -0.098 (weakly negatively correlated)
- historical_volatility_60: 0.094 (weakly positively correlated)
- fn_repurchased_shares_q: 0.093 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
