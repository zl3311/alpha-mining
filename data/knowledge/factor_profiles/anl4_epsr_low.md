---
field: anl4_epsr_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2095
ann_vol: 0.1021
hit_rate: 0.5085
rolling_sharpe_min: -2.267
rolling_sharpe_max: 2.916
redundancy_cluster: 13
negated_best_sharpe: 0.22
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.46
---
# anl4_epsr_low (analyst4)

*GAAP Earnings per share - The lowest estimation*

## Signal Profile
- `rank(anl4_epsr_low)`: S=0.33, F=0.19, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_epsr_low / close)`: S=0.68, F=0.51, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_epsr_low, 5))`: S=0.03, F=0.00, T=37.0%, INFERIOR (TOP1000)
- `-rank(anl4_epsr_low)`: S=-0.20, F=-0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_low, 5))`: S=0.09, F=0.01, T=35.5%, INFERIOR (TOP3000)
- `ts_zscore(anl4_epsr_low, 22)`: S=0.09, F=0.01, T=35.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_epsr_low, 10)`: S=-0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_epsr_low, 22))`: S=-0.26, F=-0.07, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_low)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_low / close)`: S=0.22, F=0.11, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.67, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-0.5%
  - 2020: S=-1.71 (negative), ret=-11.7%
  - 2021: S=1.83 (strong), ret=+21.0%
  - 2022: S=1.88 (strong), ret=+27.4%
  - 2023: S=-0.30 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 20.95% over 755 days (recovered)
- Annualized: return +6.8%, volatility 10.2% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.03, excess kurtosis +1.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.27, max 2.92, latest -0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.35%; worst month: -4.21%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.33
- Sideways: S=0.40
- Bear: S=-2.47

## Negated Direction
Best negated: `rank(-1 * anl4_epsr_low / close)` S=0.22, F=0.11, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_epsr_low)`: S=0.04, F=0.01, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_epsr_low / close)`: S=0.22, F=0.11, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_epsr_low, 5))`: S=0.09, F=0.01, T=35.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_epsr_low / close)` | TOP3000 | 0.67 | 0.51 | 20.9% | 40% | bull-only |
| `rank(anl4_epsr_low)` | TOP3000 | 0.32 | 0.19 | 40.0% | 60% | bull-only |
| `rank(anl4_epsr_low / close)` | TOP1000 | 0.25 | 0.14 | 27.2% | 60% | bull-only |
| `rank(anl4_epsr_low)` | TOP1000 | 0.19 | 0.09 | 37.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_epsr_mean: 0.990 (strongly positively correlated)
- anl4_median_epsreported: 0.989 (strongly positively correlated)
- est_epsr: 0.979 (strongly positively correlated)
- anl4_epsr_high: 0.969 (strongly positively correlated)
- anl4_qfd1_az_wol_spe: 0.959 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
