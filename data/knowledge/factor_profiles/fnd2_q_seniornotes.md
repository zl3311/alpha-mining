---
field: fnd2_q_seniornotes
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1029
ann_vol: 0.0632
hit_rate: 0.4931
rolling_sharpe_min: -0.902
rolling_sharpe_max: 2.484
redundancy_cluster: 12
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.22
---
# fnd2_q_seniornotes (fundamental2)

*Including the current and noncurrent portions, carrying value as of the balance sheet date of Notes with the highest claim on the assets of the issuer in case of bankruptcy or liquidation (with maturities initially due after 1 year or beyond the operating cycle if longer). Senior note holders are paid off in full before any payments are made to junior note holders.*

## Signal Profile
- `rank(fnd2_q_seniornotes)`: S=0.07, F=0.01, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_q_seniornotes / close)`: S=0.57, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_q_seniornotes, 5))`: S=0.42, F=0.21, T=35.4%, INFERIOR (TOP200)
- `-rank(fnd2_q_seniornotes)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_seniornotes, 5))`: S=-0.37, F=-0.14, T=36.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_q_seniornotes, 63)`: S=-0.05, F=-0.01, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(fnd2_q_seniornotes, 10)`: S=0.11, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_q_seniornotes, 22))`: S=-0.54, F=-0.25, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_seniornotes)`: S=0.35, F=0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_seniornotes / close)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=1.28 (moderate), ret=+10.5%
  - 2021: S=0.71 (moderate), ret=+3.6%
  - 2022: S=-0.10 (negative), ret=-0.6%
  - 2023: S=0.50 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 10.29% over 391 days (recovered)
- Annualized: return +3.5%, volatility 6.3% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.76, excess kurtosis +3.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.48, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +4.37%; worst month: -4.74%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.95
- Sideways: S=-0.19
- Bear: S=0.87

## Negated Direction
Best negated: `rank(-1 * fnd2_q_seniornotes)` S=0.35, F=0.17, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_q_seniornotes)`: S=0.35, F=0.17, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_seniornotes / close)`: S=-0.08, F=-0.02, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_seniornotes, 5))`: S=-0.37, F=-0.14, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_q_seniornotes / close)` | TOP3000 | 0.56 | 0.31 | 10.3% | 80% | all-weather |
| `rank(ts_delta(fnd2_q_seniornotes, 5))` | TOP200 | 0.42 | 0.21 | 34.9% | 80% | mixed |
| `rank(ts_delta(fnd2_q_seniornotes, 5))` | TOP500 | 0.39 | 0.15 | 18.1% | 80% | mixed |
| `rank(ts_delta(fnd2_q_seniornotes, 5))` | TOP3000 | 0.38 | 0.13 | 17.3% | 60% | mixed |
| `rank(fnd2_q_seniornotes / close)` | TOP1000 | 0.28 | 0.11 | 12.4% | 60% | mixed |
| `rank(fnd2_q_seniornotes / close)` | TOP500 | 0.07 | 0.02 | 19.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_seniornotes: 0.945 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.876 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.873 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.867 (strongly positively correlated)
- fn_proceeds_from_issuance_of_debt_a: 0.851 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
