---
field: fnd6_newqv1300_stkcoq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.36
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.1012
ann_vol: 0.0797
hit_rate: 0.4866
rolling_sharpe_min: -0.821
rolling_sharpe_max: 1.906
redundancy_cluster: 31
negated_best_sharpe: -0.09
negated_best_template: neg_rank
negated_best_fitness: -0.02
n_negated_sims: 4
direction_gap: -0.68
---
# fnd6_newqv1300_stkcoq (fundamental6)

*Stock Compensation Expense*

## Signal Profile
- `rank(fnd6_newqv1300_stkcoq)`: S=0.52, F=0.28, T=3.6%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_stkcoq / close)`: S=0.59, F=0.36, T=4.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_stkcoq, 5))`: S=0.84, F=0.32, T=39.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_stkcoq)`: S=-0.09, F=-0.02, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_stkcoq, 5))`: S=-0.84, F=-0.32, T=39.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_stkcoq, 22)`: S=0.35, F=0.11, T=38.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_stkcoq, 10)`: S=0.35, F=0.20, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_stkcoq, 22))`: S=0.72, F=0.32, T=17.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcoq)`: S=-0.52, F=-0.28, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcoq / close)`: S=-0.31, F=-0.14, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/18P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.49 (moderate), ret=+7.7%
  - 2020: S=-0.19 (negative), ret=-1.7%
  - 2021: S=0.10 (weak), ret=+1.0%
  - 2022: S=1.28 (moderate), ret=+9.2%
  - 2023: S=1.10 (moderate), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 10.12% over 410 days (recovered)
- Annualized: return +4.8%, volatility 8.0% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.57, excess kurtosis +2.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.82, max 1.91, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +5.32%; worst month: -5.38%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.87
- Sideways: S=0.02
- Bear: S=-0.26

## Negated Direction
Best negated: `-rank(fnd6_newqv1300_stkcoq)` S=-0.09, F=-0.02, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_stkcoq)`: S=-0.52, F=-0.28, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcoq / close)`: S=-0.31, F=-0.14, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_stkcoq, 5))`: S=-0.84, F=-0.32, T=39.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_stkcoq / close)` | TOP500 | 0.60 | 0.36 | 10.1% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_stkcoq, 5))` | TOP3000 | 0.86 | 0.32 | 9.3% | 100% | mixed |
| `rank(ts_delta(fnd6_newqv1300_stkcoq, 5))` | TOP500 | 0.70 | 0.31 | 16.2% | 80% | mixed |
| `rank(fnd6_newqv1300_stkcoq)` | TOP3000 | 0.52 | 0.28 | 20.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_stkcoq, 5))` | TOP1000 | 0.73 | 0.28 | 13.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_stkcoq, 5))` | TOP200 | 0.45 | 0.18 | 16.2% | 60% | mixed |
| `rank(fnd6_newqv1300_stkcoq / close)` | TOP1000 | 0.34 | 0.15 | 9.1% | 80% | mixed |
| `rank(fnd6_newqv1300_stkcoq / close)` | TOP3000 | 0.31 | 0.14 | 24.1% | 60% | bear-only |
| `rank(fnd6_newqv1300_stkcoq / close)` | TOP200 | 0.25 | 0.10 | 18.8% | 80% | mixed |
| `rank(fnd6_newqv1300_stkcoq)` | TOP500 | 0.24 | 0.09 | 34.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_stkcoq)` | TOP1000 | 0.09 | 0.02 | 31.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_stkco: 0.880 (strongly positively correlated)
- fnd6_mfmq_cheq: 0.784 (strongly positively correlated)
- cash_st: 0.783 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.782 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.769 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative: fnd6_fopo). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
