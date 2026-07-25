---
field: fnd6_cshpri
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1296
ann_vol: 0.0654
hit_rate: 0.4988
rolling_sharpe_min: -0.87
rolling_sharpe_max: 2.635
redundancy_cluster: 31
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.38
---
# fnd6_cshpri (fundamental6)

*Common Shares Used to Calculate Earnings Per Share - Basic*

## Signal Profile
- `rank(fnd6_cshpri)`: S=0.24, F=0.09, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd6_cshpri / close)`: S=0.54, F=0.29, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_cshpri, 5))`: S=0.42, F=0.19, T=33.5%, INFERIOR (TOP500)
- `-rank(fnd6_cshpri)`: S=-0.24, F=-0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshpri, 5))`: S=0.16, F=0.04, T=34.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cshpri, 22)`: S=0.54, F=0.38, T=25.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cshpri, 10)`: S=0.18, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cshpri, 22))`: S=-0.90, F=-0.67, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshpri)`: S=-0.24, F=-0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshpri / close)`: S=-0.37, F=-0.17, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.40 (weak), ret=+1.7%
  - 2020: S=0.63 (moderate), ret=+4.8%
  - 2021: S=-0.54 (negative), ret=-4.5%
  - 2022: S=2.38 (strong), ret=+14.5%
  - 2023: S=0.18 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 12.96% over 342 days (recovered)
- Annualized: return +3.6%, volatility 6.5% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.49, excess kurtosis +2.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 2.63, latest 0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.25%; worst month: -3.72%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.88
- Sideways: S=-0.49
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cshpri, 5))` S=0.16, F=0.04, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cshpri)`: S=-0.24, F=-0.09, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cshpri / close)`: S=-0.37, F=-0.17, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cshpri, 5))`: S=0.16, F=0.04, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cshpri / close)` | TOP500 | 0.55 | 0.29 | 13.0% | 80% | mixed |
| `rank(ts_delta(fnd6_cshpri, 5))` | TOP500 | 0.41 | 0.19 | 36.8% | 60% | mixed |
| `rank(fnd6_cshpri / close)` | TOP1000 | 0.38 | 0.17 | 11.0% | 80% | all-weather |
| `rank(fnd6_cshpri / close)` | TOP200 | 0.34 | 0.16 | 22.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_cshpri, 5))` | TOP200 | 0.23 | 0.09 | 48.4% | 80% | weak |
| `rank(fnd6_cshpri)` | TOP1000 | 0.24 | 0.09 | 14.7% | 60% | bull-only |
| `rank(fnd6_cshpri)` | TOP3000 | 0.21 | 0.06 | 10.3% | 80% | bull-only |
| `rank(fnd6_cshpri)` | TOP500 | 0.17 | 0.06 | 24.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_cshfd: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_csho: 0.992 (strongly positively correlated)
- fnd6_mfma1_csho: 0.992 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.981 (strongly positively correlated)
- fnd6_newa1v1300_cshi: 0.976 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
