---
field: cash_st
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.61
best_fitness: 0.39
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 13
max_drawdown: 0.1222
ann_vol: 0.0836
hit_rate: 0.4915
rolling_sharpe_min: -0.811
rolling_sharpe_max: 2.402
redundancy_cluster: 31
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.55
---
# cash_st (fundamental6)

*Cash and Short-Term Investments*

## Signal Profile
- `rank(cash_st)`: S=0.54, F=0.31, T=1.9%, INFERIOR (TOP3000)
- `rank(cash_st / close)`: S=0.61, F=0.39, T=3.1%, INFERIOR (TOP500)
- `rank(ts_delta(cash_st, 5))`: S=0.49, F=0.20, T=38.0%, INFERIOR (TOP200)
- `ts_decay_linear(rank(cash_st), 5)`: S=0.54, F=0.31, T=1.8%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(cash_st), ts_std_dev(returns,20)<0.01)`: S=0.53, F=0.30, T=2.5%, INFERIOR (TOP3000)
- `-rank(cash_st)`: S=-0.27, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_st, 5))`: S=-0.48, F=-0.19, T=38.0%, INFERIOR (TOP3000)
- `ts_zscore(cash_st, 22)`: S=0.29, F=0.08, T=37.9%, INFERIOR (TOP3000)
- `ts_mean(cash_st, 10)`: S=0.48, F=0.28, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(cash_st, 22))`: S=0.09, F=0.01, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * cash_st)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * cash_st / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/28P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.61, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.27 (weak), ret=+1.5%
  - 2020: S=-0.04 (negative), ret=-0.4%
  - 2021: S=0.37 (weak), ret=+4.6%
  - 2022: S=2.13 (strong), ret=+12.9%
  - 2023: S=1.50 (moderate), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 12.22% over 370 days (recovered)
- Annualized: return +5.1%, volatility 8.4% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.54, excess kurtosis +4.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.40, latest 1.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.49%; worst month: -7.71%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.73
- Sideways: S=-0.32
- Bear: S=-1.09

## Negated Direction
Best negated: `rank(-1 * cash_st)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * cash_st)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * cash_st / close)`: S=-0.19, F=-0.08, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_st, 5))`: S=-0.48, F=-0.19, T=38.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash_st / close)` | TOP500 | 0.61 | 0.39 | 12.2% | 80% | bull-only |
| `rank(cash_st)` | TOP3000 | 0.54 | 0.31 | 24.9% | 80% | bull-only |
| `rank(cash_st / close)` | TOP1000 | 0.53 | 0.31 | 10.1% | 100% | mixed |
| `ts_decay_linear(rank(cash_st), 5)` | TOP3000 | 0.54 | 0.31 | 24.9% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(cash_st), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.53 | 0.30 | 24.4% | 80% | bull-only |
| `rank(cash_st / close)` | TOP3000 | 0.45 | 0.23 | 12.8% | 80% | mixed |
| `rank(ts_delta(cash_st, 5))` | TOP200 | 0.49 | 0.20 | 36.1% | 60% | mixed |
| `rank(ts_delta(cash_st, 5))` | TOP500 | 0.53 | 0.19 | 15.9% | 80% | all-weather |
| `rank(cash_st)` | TOP1000 | 0.27 | 0.12 | 27.2% | 60% | bull-only |
| `rank(ts_delta(cash_st, 5))` | TOP3000 | 0.46 | 0.12 | 9.0% | 60% | mixed |
| `rank(cash_st)` | TOP500 | 0.20 | 0.08 | 35.3% | 60% | bull-only |
| `rank(cash_st / close)` | TOP200 | 0.20 | 0.08 | 23.1% | 80% | bull-only |
| `rank(ts_delta(cash_st, 5))` | TOP1000 | 0.24 | 0.05 | 12.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_cheq: 1.000 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.979 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.950 (strongly positively correlated)
- fnd6_ch: 0.927 (strongly positively correlated)
- fnd6_newa2v1300_stkco: 0.819 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
