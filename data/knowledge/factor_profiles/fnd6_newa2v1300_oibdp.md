---
field: fnd6_newa2v1300_oibdp
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.58
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2407
ann_vol: 0.121
hit_rate: 0.5004
rolling_sharpe_min: -2.182
rolling_sharpe_max: 2.409
redundancy_cluster: 13
negated_best_sharpe: 0.21
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_newa2v1300_oibdp (fundamental6)

*Operating Income Before Depreciation*

## Signal Profile
- `rank(fnd6_newa2v1300_oibdp)`: S=0.31, F=0.18, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_oibdp / close)`: S=0.58, F=0.44, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_oibdp, 5))`: S=0.62, F=0.36, T=34.7%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_oibdp)`: S=-0.13, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oibdp, 5))`: S=-0.67, F=-0.40, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_oibdp, 63)`: S=-0.06, F=-0.01, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_oibdp, 10)`: S=0.17, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_oibdp, 22))`: S=0.12, F=0.03, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oibdp)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oibdp / close)`: S=0.15, F=0.07, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.1%
  - 2020: S=-1.22 (negative), ret=-11.0%
  - 2021: S=1.20 (moderate), ret=+18.0%
  - 2022: S=1.48 (moderate), ret=+25.2%
  - 2023: S=0.19 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 24.07% over 771 days (recovered)
- Annualized: return +7.0%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.02, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.18, max 2.41, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.24%; worst month: -5.01%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.12
- Sideways: S=0.70
- Bear: S=-2.94

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_oibdp)` S=0.21, F=0.11, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_oibdp)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oibdp / close)`: S=0.15, F=0.07, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oibdp, 5))`: S=-0.67, F=-0.40, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_oibdp / close)` | TOP3000 | 0.58 | 0.44 | 24.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oibdp, 5))` | TOP200 | 0.62 | 0.36 | 25.7% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_oibdp, 5))` | TOP1000 | 0.66 | 0.30 | 14.4% | 80% | mixed |
| `rank(fnd6_newa2v1300_oibdp / close)` | TOP1000 | 0.31 | 0.19 | 28.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_oibdp)` | TOP3000 | 0.30 | 0.18 | 41.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oibdp, 5))` | TOP500 | 0.27 | 0.10 | 19.7% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_oibdp, 5))` | TOP3000 | 0.27 | 0.07 | 10.2% | 80% | mixed |
| `rank(fnd6_newa2v1300_oibdp)` | TOP1000 | 0.12 | 0.05 | 45.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ebitda: 1.000 (strongly positively correlated)
- ebitda: 1.000 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.987 (strongly positively correlated)
- cashflow_op: 0.987 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
