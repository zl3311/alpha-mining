---
field: fnd6_fopo
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.06
best_fitness: 0.73
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 38
regime_profile: all-weather
n_variations_with_pnl: 11
max_drawdown: 0.0753
ann_vol: 0.0558
hit_rate: 0.5263
rolling_sharpe_min: -0.292
rolling_sharpe_max: 2.264
top_merge_partner: est_rd_expense
redundancy_cluster: 31
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 11
direction_gap: -0.48
---
# fnd6_fopo (fundamental6)

*Funds from Operations - Other*

## Signal Profile
- `rank(fnd6_fopo)`: S=1.09, F=0.69, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_fopo / close)`: S=1.06, F=0.73, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_fopo, 5))`: S=0.31, F=0.12, T=34.1%, INFERIOR (TOP500)
- `ts_decay_linear(rank(fnd6_fopo), 5)`: S=1.09, F=0.69, T=1.4%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_fopo), ts_std_dev(returns,20)<0.01)`: S=0.98, F=0.59, T=2.2%, INFERIOR (TOP3000)
- `-rank(fnd6_fopo)`: S=-0.98, F=-0.61, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fopo, 5))`: S=0.58, F=0.26, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fopo, 63)`: S=0.64, F=0.40, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fopo, 10)`: S=0.77, F=0.47, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fopo, 22))`: S=-0.20, F=-0.06, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopo)`: S=-0.98, F=-0.61, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopo / close)`: S=-1.05, F=-0.70, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/25P
- LOW_FITNESS: 38F/0P
- LOW_SHARPE: 38F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/21P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.08, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.57 (strong), ret=+6.3%
  - 2020: S=1.47 (moderate), ret=+9.0%
  - 2021: S=0.37 (weak), ret=+2.5%
  - 2022: S=0.47 (weak), ret=+2.4%
  - 2023: S=1.92 (strong), ret=+9.3%

## Risk & Drawdown
- Max drawdown: 7.53% over 237 days (recovered)
- Annualized: return +6.0%, volatility 5.6% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.34, excess kurtosis +1.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.29, max 2.26, latest 1.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +4.10%; worst month: -3.02%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.37
- Sideways: S=1.00
- Bear: S=0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fopo, 5))` S=0.58, F=0.26, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_fopo)`: S=-0.98, F=-0.61, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopo / close)`: S=-1.05, F=-0.70, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fopo, 5))`: S=0.58, F=0.26, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fopo / close)` | TOP500 | 1.08 | 0.73 | 7.5% | 100% | all-weather |
| `rank(fnd6_fopo / close)` | TOP1000 | 1.06 | 0.70 | 6.9% | 80% | all-weather |
| `rank(fnd6_fopo)` | TOP3000 | 1.10 | 0.69 | 8.9% | 100% | bull-only |
| `rank(fnd6_fopo)` | TOP500 | 1.02 | 0.69 | 10.3% | 80% | bull-only |
| `ts_decay_linear(rank(fnd6_fopo), 5)` | TOP3000 | 1.09 | 0.69 | 8.9% | 100% | bull-only |
| `rank(fnd6_fopo)` | TOP1000 | 0.98 | 0.61 | 9.2% | 100% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_fopo), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.99 | 0.59 | 8.7% | 100% | bull-only |
| `rank(fnd6_fopo / close)` | TOP3000 | 0.86 | 0.54 | 10.5% | 80% | all-weather |
| `rank(fnd6_fopo / close)` | TOP200 | 0.59 | 0.33 | 11.1% | 80% | mixed |
| `rank(fnd6_fopo)` | TOP200 | 0.42 | 0.21 | 17.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_fopo, 5))` | TOP500 | 0.30 | 0.12 | 31.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_stkco: 0.818 (strongly positively correlated)
- fnd6_newqv1300_stkcoq: 0.752 (strongly positively correlated)
- fnd6_ch: 0.726 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.716 (strongly positively correlated)
- fnd6_newa1v1300_csho: 0.714 (strongly positively correlated)

Redundancy cluster #31: 14 similar fields, mean |rho| 0.799 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| est_rd_expense | analyst4 | -0.11 | 1.64 | +0.53 | -0.61 | yes |
| funds_from_operations_max_guidance | analyst4 | -0.07 | 1.61 | +0.49 | -0.96 | yes |
| min_funds_from_operations_guidance | analyst4 | -0.07 | 1.61 | +0.48 | -0.95 | yes |
| anl4_epsr_flag | analyst4 | -0.24 | 1.74 | +0.56 | +0.79 | yes |
| anl4_capex_high | analyst4 | -0.19 | 1.58 | +0.50 | -0.01 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
