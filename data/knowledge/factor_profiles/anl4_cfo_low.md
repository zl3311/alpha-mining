---
field: anl4_cfo_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2192
ann_vol: 0.0969
hit_rate: 0.5069
rolling_sharpe_min: -2.293
rolling_sharpe_max: 2.808
redundancy_cluster: 13
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.49
---
# anl4_cfo_low (analyst4)

*Cash Flow From Operations - The lowest estimation*

## Signal Profile
- `rank(anl4_cfo_low)`: S=0.41, F=0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(anl4_cfo_low / close)`: S=0.66, F=0.47, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_cfo_low, 5))`: S=0.00, F=0.00, T=34.3%, INFERIOR (TOP200)
- `ts_decay_linear(rank(anl4_cfo_low), 5)`: S=0.41, F=0.26, T=1.5%, INFERIOR (TOP3000)
- `-rank(anl4_cfo_low)`: S=-0.19, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_low, 5))`: S=0.17, F=0.03, T=37.3%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfo_low, 63)`: S=0.02, F=0.00, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfo_low, 10)`: S=0.18, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfo_low, 22))`: S=-0.14, F=-0.03, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_low)`: S=-0.19, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_low / close)`: S=-0.28, F=-0.14, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/34P
- LOW_FITNESS: 35F/0P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.55 (negative), ret=-2.5%
  - 2020: S=-1.96 (negative), ret=-13.8%
  - 2021: S=1.72 (strong), ret=+20.9%
  - 2022: S=1.82 (strong), ret=+24.5%
  - 2023: S=0.24 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 21.92% over 1044 days (recovered)
- Annualized: return +6.3%, volatility 9.7% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.18, excess kurtosis +1.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.29, max 2.81, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.74%; worst month: -4.22%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.61
- Sideways: S=0.10
- Bear: S=-2.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfo_low, 5))` S=0.17, F=0.03, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cfo_low)`: S=-0.19, F=-0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfo_low / close)`: S=-0.28, F=-0.14, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfo_low, 5))`: S=0.17, F=0.03, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfo_low / close)` | TOP3000 | 0.65 | 0.47 | 21.9% | 60% | bull-only |
| `ts_decay_linear(rank(anl4_cfo_low), 5)` | TOP3000 | 0.40 | 0.26 | 35.9% | 60% | bull-only |
| `rank(anl4_cfo_low)` | TOP3000 | 0.40 | 0.26 | 35.6% | 60% | bull-only |
| `rank(anl4_cfo_low / close)` | TOP1000 | 0.27 | 0.14 | 24.0% | 40% | bull-only |
| `rank(anl4_cfo_low)` | TOP1000 | 0.18 | 0.08 | 36.4% | 60% | bull-only |
| `rank(anl4_cfo_low)` | TOP500 | 0.10 | 0.04 | 46.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cfo_mean: 0.992 (strongly positively correlated)
- anl4_cfo_median: 0.992 (strongly positively correlated)
- anl4_cfo_high: 0.978 (strongly positively correlated)
- est_cashflow_op: 0.975 (strongly positively correlated)
- anl4_ebit_mean: 0.956 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
