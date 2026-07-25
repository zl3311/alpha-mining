---
field: fnd6_stkcpa
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1609
ann_vol: 0.081
hit_rate: 0.5101
rolling_sharpe_min: -1.187
rolling_sharpe_max: 3.684
redundancy_cluster: 83
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.03
---
# fnd6_stkcpa (fundamental6)

*After-tax stock compensation*

## Signal Profile
- `rank(fnd6_stkcpa)`: S=0.48, F=0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_stkcpa / close)`: S=0.64, F=0.41, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_stkcpa, 5))`: S=0.37, F=0.18, T=29.5%, INFERIOR (TOP500)
- `-rank(fnd6_stkcpa)`: S=-0.08, F=-0.02, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_stkcpa, 5))`: S=0.63, F=0.36, T=41.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_stkcpa, 63)`: S=0.66, F=0.58, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_stkcpa, 10)`: S=0.48, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_stkcpa, 22))`: S=0.38, F=0.20, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_stkcpa)`: S=-0.48, F=-0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_stkcpa / close)`: S=-0.64, F=-0.41, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.64, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.2%
  - 2020: S=2.09 (strong), ret=+15.0%
  - 2021: S=2.01 (strong), ret=+11.5%
  - 2022: S=-0.35 (negative), ret=-3.7%
  - 2023: S=0.28 (weak), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 16.09% over 634 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.37, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 3.68, latest 0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +5.55%; worst month: -5.04%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.29
- Sideways: S=-0.10
- Bear: S=1.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_stkcpa, 5))` S=0.63, F=0.36, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_stkcpa)`: S=-0.48, F=-0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_stkcpa / close)`: S=-0.64, F=-0.41, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_stkcpa, 5))`: S=0.63, F=0.36, T=41.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_stkcpa / close)` | TOP3000 | 0.64 | 0.41 | 16.1% | 60% | mixed |
| `rank(fnd6_stkcpa / close)` | TOP1000 | 0.60 | 0.34 | 10.7% | 80% | all-weather |
| `rank(fnd6_stkcpa)` | TOP3000 | 0.48 | 0.27 | 22.1% | 80% | bull-only |
| `rank(fnd6_stkcpa / close)` | TOP500 | 0.42 | 0.20 | 12.1% | 80% | mixed |
| `rank(ts_delta(fnd6_stkcpa, 5))` | TOP500 | 0.37 | 0.18 | 36.5% | 60% | weak |
| `rank(ts_delta(fnd6_stkcpa, 5))` | TOP200 | 0.32 | 0.17 | 46.6% | 60% | bull-only |
| `rank(fnd6_stkcpa)` | TOP500 | 0.14 | 0.04 | 20.2% | 80% | bull-only |
| `rank(fnd6_stkcpa / close)` | TOP200 | 0.13 | 0.03 | 16.3% | 60% | weak |
| `rank(fnd6_stkcpa)` | TOP200 | 0.10 | 0.02 | 21.9% | 40% | bull-only |
| `rank(fnd6_stkcpa)` | TOP1000 | 0.09 | 0.02 | 20.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.906 (strongly positively correlated)
- fn_comp_not_rec_a: 0.869 (strongly positively correlated)
- fnd6_newa2v1300_xrd: 0.819 (strongly positively correlated)
- est_sga: 0.791 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.774 (strongly positively correlated)

Redundancy cluster #83: 3 similar fields, mean |rho| 0.764 (representative: fnd2_a_alsbcmpexrsus). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
