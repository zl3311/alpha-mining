---
field: est_sga
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.99
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1001
ann_vol: 0.0704
hit_rate: 0.481
rolling_sharpe_min: -1.563
rolling_sharpe_max: 2.701
redundancy_cluster: 33
negated_best_sharpe: 0.99
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.42
---
# est_sga (analyst4)

*SGA - mean of estimations*

## Signal Profile
- `rank(est_sga)`: S=0.48, F=0.31, T=1.0%, INFERIOR (TOP3000)
- `rank(est_sga / close)`: S=0.57, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(est_sga, 5))`: S=-0.28, F=-0.06, T=36.3%, INFERIOR (TOP1000)
- `-rank(est_sga)`: S=-0.19, F=-0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_sga, 5))`: S=0.99, F=0.44, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(est_sga, 22)`: S=0.66, F=0.27, T=34.6%, INFERIOR (TOP3000)
- `ts_mean(est_sga, 10)`: S=-0.04, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_sga, 22))`: S=0.18, F=0.04, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * est_sga)`: S=-0.20, F=-0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * est_sga / close)`: S=-0.26, F=-0.11, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.31 (negative), ret=-1.6%
  - 2020: S=1.12 (moderate), ret=+8.6%
  - 2021: S=1.12 (moderate), ret=+7.7%
  - 2022: S=0.06 (weak), ret=+0.5%
  - 2023: S=0.63 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 10.01% over 577 days (not yet recovered, ongoing at window end)
- Annualized: return +4.0%, volatility 7.0% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.41, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 2.70, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.38%; worst month: -4.29%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.80
- Sideways: S=-0.42
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_sga, 5))` S=0.99, F=0.44, INFERIOR
Direction gap: +0.42 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_sga)`: S=-0.20, F=-0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * est_sga / close)`: S=-0.26, F=-0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_sga, 5))`: S=0.99, F=0.44, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_sga / close)` | TOP3000 | 0.56 | 0.32 | 10.0% | 80% | mixed |
| `rank(est_sga)` | TOP3000 | 0.48 | 0.31 | 30.8% | 80% | bull-only |
| `rank(est_sga / close)` | TOP1000 | 0.28 | 0.12 | 10.0% | 60% | bull-only |
| `rank(est_sga / close)` | TOP500 | 0.26 | 0.11 | 16.7% | 60% | bull-only |
| `rank(est_sga)` | TOP500 | 0.20 | 0.09 | 48.0% | 60% | bull-only |
| `rank(est_sga)` | TOP1000 | 0.18 | 0.08 | 34.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- selling_general_admin_expense_reported_value: 0.966 (strongly positively correlated)
- selling_general_admin_expense_actual_value: 0.966 (strongly positively correlated)
- selling_general_admin_expense: 0.947 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.898 (strongly positively correlated)
- fnd6_newqv1300_lseq: 0.893 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
