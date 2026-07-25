---
field: fnd2_a_seniornotes
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 1.2
best_fitness: 0.97
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0849
ann_vol: 0.0602
hit_rate: 0.4883
rolling_sharpe_min: -1.087
rolling_sharpe_max: 2.202
redundancy_cluster: 12
negated_best_sharpe: 1.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.97
n_negated_sims: 10
direction_gap: 0.62
---
# fnd2_a_seniornotes (fundamental2)

*Including the current and noncurrent portions, carrying value as of the balance sheet date of Notes with the highest claim on the assets of the issuer in case of bankruptcy or liquidation (with maturities initially due after 1 year or beyond the operating cycle if longer). Senior note holders are paid off in full before any payments are made to junior note holders.*

## Signal Profile
- `rank(fnd2_a_seniornotes)`: S=0.11, F=0.03, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_seniornotes / close)`: S=0.58, F=0.30, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_seniornotes, 5))`: S=-0.66, F=-0.37, T=33.4%, INFERIOR (TOP3000)
- `-rank(fnd2_a_seniornotes)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_seniornotes, 5))`: S=1.20, F=0.97, T=32.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_seniornotes, 63)`: S=0.19, F=0.11, T=14.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_seniornotes, 10)`: S=0.09, F=0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_seniornotes, 22))`: S=-0.94, F=-0.77, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_seniornotes)`: S=0.30, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_seniornotes / close)`: S=0.03, F=0.00, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+2.4%
  - 2020: S=0.85 (moderate), ret=+7.0%
  - 2021: S=1.01 (moderate), ret=+4.9%
  - 2022: S=0.55 (moderate), ret=+3.1%
  - 2023: S=-0.11 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 8.49% over 413 days (recovered)
- Annualized: return +3.4%, volatility 6.0% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.81, excess kurtosis +3.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.20, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.07%; worst month: -3.47%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.22
- Sideways: S=-0.06
- Bear: S=0.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_seniornotes, 5))` S=1.20, F=0.97, INFERIOR
Direction gap: +0.62 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd2_a_seniornotes)`: S=0.30, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_seniornotes / close)`: S=0.03, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_seniornotes, 5))`: S=1.20, F=0.97, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_seniornotes / close)` | TOP3000 | 0.57 | 0.30 | 8.5% | 80% | mixed |
| `rank(fnd2_a_seniornotes / close)` | TOP1000 | 0.22 | 0.07 | 11.3% | 60% | bull-only |
| `rank(fnd2_a_seniornotes)` | TOP3000 | 0.09 | 0.03 | 19.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_q_seniornotes: 0.945 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.880 (strongly positively correlated)
- fn_op_lease_min_pay_due_a: 0.871 (strongly positively correlated)
- fn_proceeds_from_issuance_of_debt_a: 0.869 (strongly positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.865 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
