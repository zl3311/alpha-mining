---
field: anl4_bvps_high
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.58
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1912
ann_vol: 0.0902
hit_rate: 0.4794
rolling_sharpe_min: -2.328
rolling_sharpe_max: 2.456
redundancy_cluster: 12
negated_best_sharpe: 0.58
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: -0.02
---
# anl4_bvps_high (analyst4)

*Book value - the highest estimation, per share*

## Signal Profile
- `rank(anl4_bvps_high)`: S=0.24, F=0.09, T=1.7%, INFERIOR (TOP1000)
- `rank(anl4_bvps_high / close)`: S=0.60, F=0.39, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_bvps_high, 5))`: S=0.35, F=0.08, T=36.5%, INFERIOR (TOP3000)
- `-rank(anl4_bvps_high)`: S=-0.24, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_high, 5))`: S=0.25, F=0.08, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_high, 22)`: S=0.31, F=0.09, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_high, 10)`: S=-0.46, F=-0.30, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_high, 22))`: S=0.11, F=0.02, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_high)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_high / close)`: S=0.58, F=0.43, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.86 (negative), ret=-5.9%
  - 2020: S=0.35 (weak), ret=+4.8%
  - 2021: S=1.44 (moderate), ret=+11.2%
  - 2022: S=2.34 (strong), ret=+15.4%
  - 2023: S=0.10 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 19.12% over 741 days (recovered)
- Annualized: return +5.3%, volatility 9.0% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.92, excess kurtosis +4.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.33, max 2.46, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.66%; worst month: -5.08%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.60
- Sideways: S=-0.82
- Bear: S=-0.03

## Negated Direction
Best negated: `rank(-1 * anl4_bvps_high / close)` S=0.58, F=0.43, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_bvps_high)`: S=-0.06, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_high / close)`: S=0.58, F=0.43, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_high, 5))`: S=0.25, F=0.08, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_bvps_high / close)` | TOP3000 | 0.59 | 0.39 | 19.1% | 80% | mixed |
| `rank(anl4_bvps_high / close)` | TOP1000 | 0.28 | 0.14 | 19.8% | 80% | mixed |
| `rank(anl4_bvps_high)` | TOP1000 | 0.22 | 0.09 | 19.0% | 80% | bull-only |
| `rank(ts_delta(anl4_bvps_high, 5))` | TOP3000 | 0.38 | 0.08 | 9.6% | 40% | mixed |
| `rank(anl4_bvps_high)` | TOP3000 | 0.16 | 0.05 | 25.4% | 60% | bull-only |
| `rank(ts_delta(anl4_bvps_high, 5))` | TOP1000 | 0.23 | 0.05 | 13.8% | 60% | mixed |
| `rank(ts_delta(anl4_bvps_high, 5))` | TOP500 | 0.16 | 0.04 | 21.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_bvps_median: 1.000 (strongly positively correlated)
- anl4_bvps_mean: 1.000 (strongly positively correlated)
- anl4_bvps_low: 0.998 (strongly positively correlated)
- est_bookvalue_ps: 0.914 (strongly positively correlated)
- book_value_per_share_reported_value: 0.894 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
