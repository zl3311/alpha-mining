---
field: fnd6_txtubtxtr
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.94
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.134
ann_vol: 0.088
hit_rate: 0.5126
rolling_sharpe_min: -1.328
rolling_sharpe_max: 2.847
redundancy_cluster: 13
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.51
---
# fnd6_txtubtxtr (fundamental6)

*Impact on Effective Tax Rate*

## Signal Profile
- `rank(fnd6_txtubtxtr)`: S=0.56, F=0.38, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txtubtxtr / close)`: S=0.79, F=0.59, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubtxtr, 5))`: S=0.16, F=0.05, T=31.7%, INFERIOR (TOP500)
- `-rank(fnd6_txtubtxtr)`: S=-0.36, F=-0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubtxtr, 5))`: S=0.43, F=0.23, T=22.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txtubtxtr, 63)`: S=0.94, F=0.92, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubtxtr, 10)`: S=0.51, F=0.35, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubtxtr, 22))`: S=0.77, F=0.51, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubtxtr)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubtxtr / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.2%
  - 2020: S=-0.77 (negative), ret=-5.0%
  - 2021: S=1.76 (strong), ret=+20.2%
  - 2022: S=1.52 (strong), ret=+18.3%
  - 2023: S=0.03 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 13.40% over 529 days (recovered)
- Annualized: return +6.9%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.12, excess kurtosis +2.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 2.85, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.80%; worst month: -3.34%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.31
- Sideways: S=0.77
- Bear: S=-2.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubtxtr, 5))` S=0.43, F=0.23, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_txtubtxtr)`: S=-0.08, F=-0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubtxtr / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubtxtr, 5))`: S=0.43, F=0.23, T=22.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubtxtr / close)` | TOP3000 | 0.78 | 0.59 | 13.4% | 80% | bull-only |
| `rank(fnd6_txtubtxtr)` | TOP3000 | 0.55 | 0.38 | 25.8% | 60% | bull-only |
| `rank(fnd6_txtubtxtr / close)` | TOP1000 | 0.49 | 0.33 | 14.0% | 40% | bull-only |
| `rank(fnd6_txtubtxtr)` | TOP1000 | 0.34 | 0.21 | 23.6% | 40% | bull-only |
| `rank(fnd6_txtubtxtr / close)` | TOP200 | 0.18 | 0.08 | 35.5% | 80% | bull-only |
| `rank(fnd6_txtubtxtr / close)` | TOP500 | 0.16 | 0.07 | 27.3% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubtxtr, 5))` | TOP500 | 0.16 | 0.05 | 29.4% | 60% | bull-only |
| `rank(fnd6_txtubtxtr)` | TOP200 | 0.07 | 0.02 | 46.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: 0.949 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.927 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.927 (strongly positively correlated)
- ebitda: 0.927 (strongly positively correlated)
- fnd6_txtubbegin: 0.923 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
