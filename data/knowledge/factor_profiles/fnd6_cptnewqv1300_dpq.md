---
field: fnd6_cptnewqv1300_dpq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.79
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0923
ann_vol: 0.0847
hit_rate: 0.4753
rolling_sharpe_min: -1.229
rolling_sharpe_max: 2.524
redundancy_cluster: 1
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_cptnewqv1300_dpq (fundamental6)

*Depreciation and Amortization - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_dpq)`: S=0.68, F=0.54, T=2.4%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_dpq / close)`: S=0.79, F=0.58, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_dpq, 5))`: S=0.52, F=0.23, T=39.2%, INFERIOR (TOP200)
- `-rank(fnd6_cptnewqv1300_dpq)`: S=-0.32, F=-0.19, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_dpq, 5))`: S=0.94, F=0.36, T=38.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptnewqv1300_dpq, 22)`: S=0.41, F=0.15, T=40.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_dpq, 10)`: S=0.18, F=0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_dpq, 22))`: S=0.08, F=0.01, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_dpq)`: S=-0.68, F=-0.54, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_dpq / close)`: S=-0.79, F=-0.58, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.29 (negative), ret=-1.6%
  - 2020: S=0.36 (weak), ret=+3.4%
  - 2021: S=1.50 (moderate), ret=+17.1%
  - 2022: S=1.07 (moderate), ret=+8.4%
  - 2023: S=0.95 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 9.23% over 427 days (recovered)
- Annualized: return +6.7%, volatility 8.5% (fraction of booksize)
- Hit rate: 47.5% positive days
- Tail shape: skew +0.54, excess kurtosis +2.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 2.52, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.69%; worst month: -3.96%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.79
- Sideways: S=-0.04
- Bear: S=-0.97

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_dpq, 5))` S=0.94, F=0.36, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_dpq)`: S=-0.68, F=-0.54, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_dpq / close)`: S=-0.79, F=-0.58, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_dpq, 5))`: S=0.94, F=0.36, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptnewqv1300_dpq / close)` | TOP3000 | 0.79 | 0.58 | 9.2% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_dpq)` | TOP3000 | 0.68 | 0.54 | 29.2% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_dpq / close)` | TOP500 | 0.47 | 0.32 | 22.5% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_dpq / close)` | TOP1000 | 0.42 | 0.25 | 14.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_dpq, 5))` | TOP200 | 0.52 | 0.23 | 34.5% | 60% | bear-only |
| `rank(fnd6_cptnewqv1300_dpq)` | TOP1000 | 0.32 | 0.19 | 33.1% | 60% | bull-only |
| `rank(fnd6_cptnewqv1300_dpq)` | TOP500 | 0.21 | 0.11 | 40.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- depre_amort: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_dpq: 1.000 (strongly positively correlated)
- fnd6_mfma1_dp: 0.980 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.980 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
