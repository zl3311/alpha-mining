---
field: fnd6_txtubpospinc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.8
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1174
ann_vol: 0.0619
hit_rate: 0.5117
rolling_sharpe_min: -1.77
rolling_sharpe_max: 2.601
redundancy_cluster: 13
negated_best_sharpe: 0.7
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.1
---
# fnd6_txtubpospinc (fundamental6)

*Increase - Prior Tax Positions*

## Signal Profile
- `rank(fnd6_txtubpospinc)`: S=0.65, F=0.39, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txtubpospinc / close)`: S=0.80, F=0.50, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubpospinc, 5))`: S=0.11, F=0.02, T=37.6%, INFERIOR (TOP1000)
- `-rank(fnd6_txtubpospinc)`: S=-0.30, F=-0.14, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubpospinc, 5))`: S=0.70, F=0.36, T=41.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubpospinc, 22)`: S=0.18, F=0.09, T=22.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubpospinc, 10)`: S=0.33, F=0.17, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubpospinc, 22))`: S=-0.09, F=-0.02, T=21.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospinc)`: S=-0.65, F=-0.39, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospinc / close)`: S=-0.80, F=-0.50, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.2%
  - 2020: S=-0.81 (negative), ret=-3.6%
  - 2021: S=1.48 (moderate), ret=+13.1%
  - 2022: S=1.46 (moderate), ret=+11.2%
  - 2023: S=0.89 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 11.74% over 565 days (recovered)
- Annualized: return +4.9%, volatility 6.2% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.03, excess kurtosis +3.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 2.60, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.49%; worst month: -2.75%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.78
- Sideways: S=1.00
- Bear: S=-2.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubpospinc, 5))` S=0.70, F=0.36, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubpospinc)`: S=-0.65, F=-0.39, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubpospinc / close)`: S=-0.80, F=-0.50, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubpospinc, 5))`: S=0.70, F=0.36, T=41.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubpospinc / close)` | TOP3000 | 0.80 | 0.50 | 11.7% | 80% | bull-only |
| `rank(fnd6_txtubpospinc)` | TOP3000 | 0.64 | 0.39 | 17.3% | 80% | bull-only |
| `rank(fnd6_txtubpospinc / close)` | TOP1000 | 0.43 | 0.24 | 12.3% | 60% | bull-only |
| `rank(fnd6_txtubpospinc / close)` | TOP500 | 0.30 | 0.15 | 25.4% | 40% | bull-only |
| `rank(fnd6_txtubpospinc)` | TOP1000 | 0.29 | 0.14 | 20.2% | 60% | bull-only |
| `rank(fnd6_txtubpospinc)` | TOP500 | 0.14 | 0.05 | 34.4% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubpospinc, 5))` | TOP1000 | 0.11 | 0.02 | 35.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txtubtxtr: 0.905 (strongly positively correlated)
- fnd6_xrent: 0.893 (strongly positively correlated)
- fnd6_txfo: 0.887 (strongly positively correlated)
- fnd6_mrc2: 0.886 (strongly positively correlated)
- fnd6_txtubbegin: 0.884 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
