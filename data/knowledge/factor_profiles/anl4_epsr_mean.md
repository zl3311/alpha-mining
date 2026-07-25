---
field: anl4_epsr_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1776
ann_vol: 0.1001
hit_rate: 0.5093
rolling_sharpe_min: -1.776
rolling_sharpe_max: 2.978
redundancy_cluster: 13
negated_best_sharpe: 0.42
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.36
---
# anl4_epsr_mean (analyst4)

*GAAP Earnings per share - mean of estimations*

## Signal Profile
- `rank(anl4_epsr_mean)`: S=0.35, F=0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_epsr_mean / close)`: S=0.78, F=0.62, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_epsr_mean, 5))`: S=-0.04, F=0.00, T=36.4%, INFERIOR (TOP1000)
- `-rank(anl4_epsr_mean)`: S=-0.20, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_mean, 5))`: S=0.42, F=0.09, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_epsr_mean, 22)`: S=-0.06, F=-0.01, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsr_mean, 10)`: S=0.01, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_epsr_mean, 22))`: S=-0.13, F=-0.02, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_mean)`: S=-0.35, F=-0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_mean / close)`: S=-0.78, F=-0.62, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.00 (negative), ret=-0.0%
  - 2020: S=-1.35 (negative), ret=-9.9%
  - 2021: S=1.88 (strong), ret=+21.4%
  - 2022: S=2.09 (strong), ret=+29.2%
  - 2023: S=-0.34 (negative), ret=-3.1%

## Risk & Drawdown
- Max drawdown: 17.76% over 546 days (recovered)
- Annualized: return +7.7%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.03, excess kurtosis +1.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.78, max 2.98, latest -0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.58%; worst month: -5.02%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.52
- Sideways: S=0.26
- Bear: S=-2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_epsr_mean, 5))` S=0.42, F=0.09, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_epsr_mean)`: S=-0.35, F=-0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_mean / close)`: S=-0.78, F=-0.62, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_mean, 5))`: S=0.42, F=0.09, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsr_mean / close)` | TOP3000 | 0.77 | 0.62 | 17.8% | 40% | bull-only |
| `rank(anl4_epsr_mean)` | TOP3000 | 0.34 | 0.21 | 39.5% | 60% | bull-only |
| `rank(anl4_epsr_mean / close)` | TOP1000 | 0.27 | 0.16 | 24.2% | 60% | bull-only |
| `rank(anl4_epsr_mean)` | TOP1000 | 0.19 | 0.09 | 36.8% | 60% | bull-only |
| `rank(anl4_epsr_mean)` | TOP500 | 0.08 | 0.03 | 35.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_median_epsreported: 1.000 (strongly positively correlated)
- est_epsr: 0.992 (strongly positively correlated)
- anl4_epsr_high: 0.992 (strongly positively correlated)
- anl4_epsr_low: 0.990 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.969 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
