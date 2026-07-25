---
field: anl4_bvps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.63
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1948
ann_vol: 0.0892
hit_rate: 0.481
rolling_sharpe_min: -2.368
rolling_sharpe_max: 2.434
redundancy_cluster: 12
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: -0.07
---
# anl4_bvps_low (analyst4)

*Book value - the lowest estimation, per share*

## Signal Profile
- `rank(anl4_bvps_low)`: S=0.27, F=0.11, T=1.7%, INFERIOR (TOP1000)
- `rank(anl4_bvps_low / close)`: S=0.63, F=0.42, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_bvps_low, 5))`: S=0.56, F=0.19, T=36.9%, INFERIOR (TOP1000)
- `-rank(anl4_bvps_low)`: S=-0.27, F=-0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_low, 5))`: S=-0.20, F=-0.05, T=33.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_low, 22)`: S=0.75, F=0.36, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_low, 10)`: S=-0.47, F=-0.31, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_low, 22))`: S=0.55, F=0.24, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_low)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_low / close)`: S=0.56, F=0.40, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.93 (negative), ret=-6.3%
  - 2020: S=0.35 (weak), ret=+4.8%
  - 2021: S=1.45 (moderate), ret=+11.3%
  - 2022: S=2.31 (strong), ret=+14.9%
  - 2023: S=0.37 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 19.48% over 744 days (recovered)
- Annualized: return +5.5%, volatility 8.9% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.93, excess kurtosis +5.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.37, max 2.43, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.31%; worst month: -5.07%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.62
- Sideways: S=-0.74
- Bear: S=-0.04

## Negated Direction
Best negated: `rank(-1 * anl4_bvps_low / close)` S=0.56, F=0.40, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_bvps_low)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_low / close)`: S=0.56, F=0.40, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_low, 5))`: S=-0.20, F=-0.05, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_bvps_low / close)` | TOP3000 | 0.62 | 0.42 | 19.5% | 80% | mixed |
| `rank(ts_delta(anl4_bvps_low, 5))` | TOP1000 | 0.57 | 0.19 | 9.5% | 80% | all-weather |
| `rank(anl4_bvps_low / close)` | TOP1000 | 0.31 | 0.16 | 20.2% | 80% | mixed |
| `rank(ts_delta(anl4_bvps_low, 5))` | TOP3000 | 0.59 | 0.16 | 9.2% | 80% | mixed |
| `rank(anl4_bvps_low)` | TOP1000 | 0.24 | 0.11 | 18.2% | 80% | bull-only |
| `rank(ts_delta(anl4_bvps_low, 5))` | TOP500 | 0.31 | 0.09 | 18.2% | 60% | mixed |
| `rank(anl4_bvps_low)` | TOP3000 | 0.17 | 0.06 | 25.5% | 60% | bull-only |
| `rank(ts_delta(anl4_bvps_low, 5))` | TOP200 | 0.20 | 0.05 | 20.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_bvps_mean: 0.999 (strongly positively correlated)
- anl4_bvps_median: 0.999 (strongly positively correlated)
- anl4_bvps_high: 0.998 (strongly positively correlated)
- est_bookvalue_ps: 0.910 (strongly positively correlated)
- book_value_per_share_reported_value: 0.893 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
