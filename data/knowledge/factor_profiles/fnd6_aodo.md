---
field: fnd6_aodo
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1043
ann_vol: 0.0747
hit_rate: 0.4874
rolling_sharpe_min: -1.114
rolling_sharpe_max: 2.297
redundancy_cluster: 1
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.08
---
# fnd6_aodo (fundamental6)

*Other Assets excluding Discontinued Operations*

## Signal Profile
- `rank(fnd6_aodo)`: S=0.46, F=0.29, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_aodo / close)`: S=0.66, F=0.41, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_aodo, 5))`: S=-0.34, F=-0.15, T=37.0%, INFERIOR (TOP200)
- `-rank(fnd6_aodo)`: S=-0.29, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aodo, 5))`: S=0.58, F=0.28, T=34.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_aodo, 22)`: S=-0.29, F=-0.12, T=31.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aodo, 10)`: S=0.05, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aodo, 22))`: S=-0.14, F=-0.03, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aodo)`: S=-0.10, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aodo / close)`: S=-0.29, F=-0.15, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.36 (negative), ret=-1.6%
  - 2020: S=-0.31 (negative), ret=-2.5%
  - 2021: S=1.17 (moderate), ret=+11.9%
  - 2022: S=1.55 (strong), ret=+12.5%
  - 2023: S=0.83 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 10.43% over 289 days (recovered)
- Annualized: return +4.9%, volatility 7.5% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.43, excess kurtosis +3.33

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.30, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.55%; worst month: -3.08%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.70
- Sideways: S=0.67
- Bear: S=-2.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_aodo, 5))` S=0.58, F=0.28, INFERIOR
Direction gap: -0.08 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_aodo)`: S=-0.10, F=-0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aodo / close)`: S=-0.29, F=-0.15, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aodo, 5))`: S=0.58, F=0.28, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_aodo / close)` | TOP3000 | 0.65 | 0.41 | 10.4% | 60% | bull-only |
| `rank(fnd6_aodo / close)` | TOP1000 | 0.49 | 0.33 | 17.3% | 60% | bull-only |
| `rank(fnd6_aodo)` | TOP3000 | 0.45 | 0.29 | 31.3% | 80% | bull-only |
| `rank(fnd6_aodo)` | TOP1000 | 0.28 | 0.16 | 35.6% | 60% | bull-only |
| `rank(fnd6_aodo / close)` | TOP500 | 0.29 | 0.15 | 32.8% | 80% | bull-only |
| `rank(fnd6_aodo / close)` | TOP200 | 0.08 | 0.03 | 43.4% | 80% | bull-only |
| `rank(fnd6_aodo)` | TOP500 | 0.09 | 0.03 | 51.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_aox: 0.998 (strongly positively correlated)
- fnd6_newa1v1300_ao: 0.993 (strongly positively correlated)
- fnd6_newqv1300_altoq: 0.985 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.961 (strongly positively correlated)
- fnd6_mfma2_revt: 0.956 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
