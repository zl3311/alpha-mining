---
field: fnd2_a_provisionfordbflact
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.58
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0673
ann_vol: 0.0489
hit_rate: 0.4891
rolling_sharpe_min: -1.623
rolling_sharpe_max: 1.85
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.21
---
# fnd2_a_provisionfordbflact (fundamental2)

*Provision For Doubtful Accounts In Period*

## Signal Profile
- `rank(fnd2_a_provisionfordbflact)`: S=0.27, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_provisionfordbflact / close)`: S=0.35, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_provisionfordbflact, 5))`: S=-0.19, F=-0.06, T=34.7%, INFERIOR (TOP3000)
- `-rank(fnd2_a_provisionfordbflact)`: S=0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_provisionfordbflact, 5))`: S=0.58, F=0.32, T=32.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_provisionfordbflact, 63)`: S=0.13, F=0.07, T=14.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_provisionfordbflact, 10)`: S=0.37, F=0.20, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_provisionfordbflact, 22))`: S=-0.04, F=-0.01, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_provisionfordbflact)`: S=0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_provisionfordbflact / close)`: S=-0.05, F=-0.01, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+2.0%
  - 2020: S=0.09 (weak), ret=+0.6%
  - 2021: S=0.93 (moderate), ret=+4.5%
  - 2022: S=-0.12 (negative), ret=-0.5%
  - 2023: S=0.47 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 6.73% over 591 days (not yet recovered, ongoing at window end)
- Annualized: return +1.7%, volatility 4.9% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +1.16, excess kurtosis +9.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.62, max 1.85, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +4.17%; worst month: -2.89%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.28
- Sideways: S=-0.10
- Bear: S=-0.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_provisionfordbflact, 5))` S=0.58, F=0.32, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_provisionfordbflact)`: S=0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_provisionfordbflact / close)`: S=-0.05, F=-0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_provisionfordbflact, 5))`: S=0.58, F=0.32, T=32.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_provisionfordbflact / close)` | TOP3000 | 0.35 | 0.13 | 6.7% | 80% | mixed |
| `rank(fnd2_a_provisionfordbflact / close)` | TOP500 | 0.28 | 0.12 | 9.4% | 60% | bull-only |
| `rank(fnd2_a_provisionfordbflact)` | TOP3000 | 0.27 | 0.09 | 17.7% | 80% | bull-only |
| `rank(fnd2_a_provisionfordbflact)` | TOP500 | 0.06 | 0.02 | 21.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_allowance_for_doubtful_accounts_receivable_a: 0.804 (strongly positively correlated)
- fn_allowance_for_doubtful_accounts_receivable_q: 0.803 (strongly positively correlated)
- fnd2_oprlsfmpdcurr: 0.791 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.787 (strongly positively correlated)
- fnd6_xopr: 0.785 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
