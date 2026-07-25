---
field: fnd6_prstkc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.8
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1725
ann_vol: 0.0686
hit_rate: 0.5069
rolling_sharpe_min: -2.351
rolling_sharpe_max: 2.607
redundancy_cluster: 13
negated_best_sharpe: 0.87
negated_best_template: rank_neg_delta
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: 0.07
---
# fnd6_prstkc (fundamental6)

*Purchase of Common and Preferred Stock*

## Signal Profile
- `rank(fnd6_prstkc)`: S=0.50, F=0.29, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_prstkc / close)`: S=0.73, F=0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_prstkc, 5))`: S=0.31, F=0.13, T=33.9%, INFERIOR (TOP500)
- `-rank(fnd6_prstkc)`: S=-0.24, F=-0.11, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prstkc, 5))`: S=0.87, F=0.45, T=35.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_prstkc, 63)`: S=0.80, F=0.62, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prstkc, 10)`: S=0.26, F=0.12, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prstkc, 22))`: S=-0.07, F=-0.01, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prstkc)`: S=-0.50, F=-0.29, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prstkc / close)`: S=-0.73, F=-0.46, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+3.6%
  - 2020: S=-1.45 (negative), ret=-7.5%
  - 2021: S=1.37 (moderate), ret=+13.5%
  - 2022: S=1.74 (strong), ret=+14.4%
  - 2023: S=-0.03 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 17.25% over 744 days (recovered)
- Annualized: return +4.9%, volatility 6.9% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.11, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 2.61, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.06%; worst month: -2.60%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.06
- Sideways: S=0.62
- Bear: S=-2.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prstkc, 5))` S=0.87, F=0.45, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_prstkc)`: S=-0.50, F=-0.29, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prstkc / close)`: S=-0.73, F=-0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prstkc, 5))`: S=0.87, F=0.45, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prstkc / close)` | TOP3000 | 0.71 | 0.46 | 17.2% | 60% | bull-only |
| `rank(fnd6_prstkc)` | TOP3000 | 0.48 | 0.29 | 26.3% | 60% | bull-only |
| `rank(fnd6_prstkc / close)` | TOP1000 | 0.37 | 0.20 | 19.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_prstkc, 5))` | TOP500 | 0.30 | 0.13 | 37.8% | 80% | mixed |
| `rank(fnd6_prstkc)` | TOP1000 | 0.22 | 0.11 | 29.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xrent: 0.910 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.902 (strongly positively correlated)
- ebitda: 0.902 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.902 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.901 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
