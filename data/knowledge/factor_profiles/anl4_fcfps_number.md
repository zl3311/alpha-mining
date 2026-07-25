---
field: anl4_fcfps_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.52
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1393
ann_vol: 0.0812
hit_rate: 0.5069
rolling_sharpe_min: -1.228
rolling_sharpe_max: 2.631
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.12
---
# anl4_fcfps_number (analyst4)

*Free Cash Flow per Share - number of estimations*

## Signal Profile
- `rank(anl4_fcfps_number)`: S=0.43, F=0.23, T=4.4%, INFERIOR (TOP200)
- `rank(anl4_fcfps_number / close)`: S=0.23, F=0.10, T=2.3%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_fcfps_number, 5))`: S=0.28, F=0.08, T=35.9%, INFERIOR (TOP3000)
- `-rank(anl4_fcfps_number)`: S=-0.42, F=-0.16, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_number, 5))`: S=0.40, F=0.15, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_fcfps_number, 63)`: S=-0.10, F=-0.02, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_fcfps_number, 10)`: S=0.52, F=0.25, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_fcfps_number, 22))`: S=0.49, F=0.24, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_number)`: S=0.08, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_number / close)`: S=-0.06, F=-0.01, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.01 (negative), ret=-5.8%
  - 2020: S=2.48 (strong), ret=+19.0%
  - 2021: S=0.83 (moderate), ret=+6.8%
  - 2022: S=0.04 (weak), ret=+0.4%
  - 2023: S=-0.55 (negative), ret=-4.3%

## Risk & Drawdown
- Max drawdown: 13.93% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +3.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.21, excess kurtosis +3.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 2.63, latest -0.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.79%; worst month: -5.86%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.20
- Sideways: S=0.36
- Bear: S=-0.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_fcfps_number, 5))` S=0.40, F=0.15, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_fcfps_number)`: S=0.08, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_fcfps_number / close)`: S=-0.06, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_fcfps_number, 5))`: S=0.40, F=0.15, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_fcfps_number)` | TOP200 | 0.41 | 0.23 | 13.9% | 60% | mixed |
| `rank(anl4_fcfps_number)` | TOP1000 | 0.41 | 0.16 | 7.8% | 60% | mixed |
| `rank(anl4_fcfps_number)` | TOP3000 | 0.36 | 0.11 | 6.8% | 60% | mixed |
| `rank(anl4_fcfps_number / close)` | TOP1000 | 0.23 | 0.10 | 23.9% | 40% | bear-only |
| `rank(ts_delta(anl4_fcfps_number, 5))` | TOP3000 | 0.29 | 0.08 | 15.3% | 80% | mixed |
| `rank(anl4_fcfps_number / close)` | TOP3000 | 0.14 | 0.05 | 34.4% | 60% | bear-only |
| `rank(ts_delta(anl4_fcfps_number, 5))` | TOP200 | 0.15 | 0.04 | 41.1% | 60% | mixed |
| `rank(anl4_fcfps_number / close)` | TOP200 | 0.10 | 0.03 | 20.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- max_reported_eps_guidance_2: 0.291 (weakly positively correlated)
- min_reported_eps_guidance: 0.289 (weakly positively correlated)
- eps_max_guidance_quarterly: 0.289 (weakly positively correlated)
- eps_min_guidance_quarterly: 0.288 (weakly positively correlated)
- unsystematic_risk_last_30_days: -0.287 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
