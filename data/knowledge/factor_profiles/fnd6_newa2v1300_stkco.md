---
field: fnd6_newa2v1300_stkco
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.65
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1029
ann_vol: 0.0853
hit_rate: 0.5004
rolling_sharpe_min: -0.571
rolling_sharpe_max: 2.029
redundancy_cluster: 31
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.32
---
# fnd6_newa2v1300_stkco (fundamental6)

*Stock Compensation Expense*

## Signal Profile
- `rank(fnd6_newa2v1300_stkco)`: S=0.59, F=0.34, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_stkco / close)`: S=0.59, F=0.37, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa2v1300_stkco, 5))`: S=0.01, F=0.00, T=32.1%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_stkco)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_stkco, 5))`: S=0.33, F=0.12, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_stkco, 63)`: S=0.40, F=0.22, T=19.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_stkco, 10)`: S=0.65, F=0.52, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_stkco, 22))`: S=-0.34, F=-0.15, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_stkco)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_stkco / close)`: S=-0.37, F=-0.18, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+4.6%
  - 2020: S=0.04 (weak), ret=+0.4%
  - 2021: S=0.27 (weak), ret=+3.0%
  - 2022: S=1.11 (moderate), ret=+8.5%
  - 2023: S=1.34 (moderate), ret=+8.6%

## Risk & Drawdown
- Max drawdown: 10.29% over 239 days (recovered)
- Annualized: return +5.1%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.47, excess kurtosis +2.84

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.03, latest 1.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +7.71%; worst month: -4.55%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.79
- Sideways: S=0.20
- Bear: S=-0.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_stkco, 5))` S=0.33, F=0.12, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_stkco)`: S=-0.05, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_stkco / close)`: S=-0.37, F=-0.18, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_stkco, 5))`: S=0.33, F=0.12, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_stkco / close)` | TOP500 | 0.60 | 0.37 | 10.3% | 100% | mixed |
| `rank(fnd6_newa2v1300_stkco)` | TOP3000 | 0.59 | 0.34 | 17.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_stkco / close)` | TOP3000 | 0.54 | 0.33 | 16.7% | 80% | mixed |
| `rank(fnd6_newa2v1300_stkco / close)` | TOP200 | 0.42 | 0.23 | 18.7% | 80% | mixed |
| `rank(fnd6_newa2v1300_stkco / close)` | TOP1000 | 0.37 | 0.18 | 7.9% | 100% | mixed |
| `rank(fnd6_newa2v1300_stkco)` | TOP500 | 0.16 | 0.05 | 37.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_stkcoq: 0.880 (strongly positively correlated)
- fnd6_ch: 0.879 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.876 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.824 (strongly positively correlated)
- fnd6_mfmq_cheq: 0.819 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
