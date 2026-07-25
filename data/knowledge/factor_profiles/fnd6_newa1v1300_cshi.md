---
field: fnd6_newa1v1300_cshi
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.36
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1348
ann_vol: 0.0686
hit_rate: 0.5036
rolling_sharpe_min: -0.796
rolling_sharpe_max: 2.738
redundancy_cluster: 31
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.11
---
# fnd6_newa1v1300_cshi (fundamental6)

*Common Shares Issued*

## Signal Profile
- `rank(fnd6_newa1v1300_cshi)`: S=0.30, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_cshi / close)`: S=0.62, F=0.36, T=2.6%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_cshi, 5))`: S=-0.11, F=-0.03, T=28.8%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_cshi)`: S=-0.25, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cshi, 5))`: S=0.51, F=0.25, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_cshi, 22)`: S=0.24, F=0.13, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_cshi, 10)`: S=0.10, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_cshi, 22))`: S=-1.07, F=-0.87, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshi)`: S=-0.25, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshi / close)`: S=-0.41, F=-0.20, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+3.8%
  - 2020: S=0.54 (moderate), ret=+4.3%
  - 2021: S=-0.44 (negative), ret=-3.8%
  - 2022: S=2.40 (strong), ret=+15.5%
  - 2023: S=0.25 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 13.48% over 340 days (recovered)
- Annualized: return +4.3%, volatility 6.9% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.57, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.74, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.48%; worst month: -3.27%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.18
- Sideways: S=-0.48
- Bear: S=-0.17

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_cshi, 5))` S=0.51, F=0.25, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_cshi)`: S=-0.25, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cshi / close)`: S=-0.41, F=-0.20, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cshi, 5))`: S=0.51, F=0.25, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_cshi / close)` | TOP500 | 0.62 | 0.36 | 13.5% | 80% | mixed |
| `rank(fnd6_newa1v1300_cshi / close)` | TOP1000 | 0.41 | 0.20 | 11.3% | 80% | mixed |
| `rank(fnd6_newa1v1300_cshi / close)` | TOP200 | 0.38 | 0.19 | 22.5% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cshi)` | TOP3000 | 0.30 | 0.11 | 10.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cshi)` | TOP1000 | 0.24 | 0.10 | 16.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cshi)` | TOP500 | 0.17 | 0.06 | 28.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_csho: 0.982 (strongly positively correlated)
- fnd6_mfma1_csho: 0.982 (strongly positively correlated)
- fnd6_cshpri: 0.976 (strongly positively correlated)
- fnd6_newa1v1300_cshfd: 0.976 (strongly positively correlated)
- fnd6_newqv1300_csh12q: 0.957 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
