---
field: fnd6_ch
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.37
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1423
ann_vol: 0.0853
hit_rate: 0.5053
rolling_sharpe_min: -1.084
rolling_sharpe_max: 2.411
redundancy_cluster: 31
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.01
---
# fnd6_ch (fundamental6)

*Cash*

## Signal Profile
- `rank(fnd6_ch)`: S=0.53, F=0.30, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_ch / close)`: S=0.59, F=0.37, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_ch, 5))`: S=-0.15, F=-0.03, T=36.0%, INFERIOR (TOP3000)
- `-rank(fnd6_ch)`: S=-0.32, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ch, 5))`: S=0.60, F=0.29, T=34.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_ch, 22)`: S=0.45, F=0.26, T=26.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ch, 10)`: S=0.20, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ch, 22))`: S=-0.27, F=-0.10, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ch)`: S=-0.32, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ch / close)`: S=-0.58, F=-0.35, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.9%
  - 2020: S=-0.47 (negative), ret=-4.3%
  - 2021: S=0.35 (weak), ret=+4.5%
  - 2022: S=1.93 (strong), ret=+13.1%
  - 2023: S=2.14 (strong), ret=+9.9%

## Risk & Drawdown
- Max drawdown: 14.23% over 259 days (recovered)
- Annualized: return +5.1%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.58, excess kurtosis +4.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.41, latest 2.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +8.26%; worst month: -6.81%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.51
- Sideways: S=0.06
- Bear: S=-1.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ch, 5))` S=0.60, F=0.29, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_ch)`: S=-0.32, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ch / close)`: S=-0.58, F=-0.35, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ch, 5))`: S=0.60, F=0.29, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ch / close)` | TOP500 | 0.60 | 0.37 | 14.2% | 80% | bull-only |
| `rank(fnd6_ch / close)` | TOP1000 | 0.58 | 0.35 | 9.9% | 100% | bull-only |
| `rank(fnd6_ch)` | TOP3000 | 0.53 | 0.30 | 25.2% | 80% | bull-only |
| `rank(fnd6_ch / close)` | TOP3000 | 0.55 | 0.30 | 9.3% | 80% | mixed |
| `rank(fnd6_ch)` | TOP1000 | 0.32 | 0.16 | 26.8% | 80% | bull-only |
| `rank(fnd6_ch)` | TOP500 | 0.17 | 0.06 | 37.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_che: 0.978 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.942 (strongly positively correlated)
- fnd6_mfmq_cheq: 0.927 (strongly positively correlated)
- cash_st: 0.927 (strongly positively correlated)
- fnd6_newa2v1300_stkco: 0.879 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
