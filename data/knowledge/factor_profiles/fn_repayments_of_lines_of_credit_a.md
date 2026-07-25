---
field: fn_repayments_of_lines_of_credit_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.94
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.084
ann_vol: 0.0553
hit_rate: 0.4931
rolling_sharpe_min: -1.28
rolling_sharpe_max: 2.258
redundancy_cluster: 1
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 0.6
n_negated_sims: 10
direction_gap: 0.34
---
# fn_repayments_of_lines_of_credit_a (fundamental2)

*Amount of cash outflow for payment of an obligation from a lender, including but not limited to, letter of credit, standby letter of credit and revolving credit arrangements.*

## Signal Profile
- `rank(fn_repayments_of_lines_of_credit_a)`: S=0.33, F=0.15, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_repayments_of_lines_of_credit_a / close)`: S=0.60, F=0.31, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repayments_of_lines_of_credit_a, 5))`: S=0.25, F=0.10, T=24.2%, INFERIOR (TOP200)
- `-rank(fn_repayments_of_lines_of_credit_a)`: S=-0.16, F=-0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_a, 5))`: S=0.94, F=0.60, T=29.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_repayments_of_lines_of_credit_a, 22)`: S=-0.36, F=-0.20, T=19.9%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_lines_of_credit_a, 10)`: S=0.06, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_lines_of_credit_a, 22))`: S=-0.64, F=-0.44, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_a)`: S=-0.16, F=-0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_a / close)`: S=-0.32, F=-0.14, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+0.9%
  - 2020: S=0.01 (weak), ret=+0.1%
  - 2021: S=0.66 (moderate), ret=+4.8%
  - 2022: S=1.95 (strong), ret=+10.0%
  - 2023: S=0.03 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 8.40% over 161 days (recovered)
- Annualized: return +3.2%, volatility 5.5% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.57, excess kurtosis +3.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.26, latest 0.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.61%; worst month: -2.19%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.66
- Sideways: S=0.48
- Bear: S=-1.82

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_a, 5))` S=0.94, F=0.60, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_repayments_of_lines_of_credit_a)`: S=-0.16, F=-0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_lines_of_credit_a / close)`: S=-0.32, F=-0.14, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_lines_of_credit_a, 5))`: S=0.94, F=0.60, T=29.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_lines_of_credit_a / close)` | TOP3000 | 0.58 | 0.31 | 8.4% | 100% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_a)` | TOP3000 | 0.33 | 0.15 | 28.0% | 80% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_a / close)` | TOP1000 | 0.32 | 0.14 | 16.0% | 60% | bull-only |
| `rank(ts_delta(fn_repayments_of_lines_of_credit_a, 5))` | TOP200 | 0.25 | 0.10 | 25.3% | 60% | mixed |
| `rank(ts_delta(fn_repayments_of_lines_of_credit_a, 5))` | TOP3000 | 0.25 | 0.08 | 25.0% | 60% | weak |
| `rank(fn_repayments_of_lines_of_credit_a)` | TOP1000 | 0.15 | 0.06 | 32.8% | 60% | bull-only |
| `rank(fn_repayments_of_lines_of_credit_a / close)` | TOP500 | 0.13 | 0.04 | 33.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_at: 0.916 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.915 (strongly positively correlated)
- fnd6_newa1v1300_lse: 0.915 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.914 (strongly positively correlated)
- assets: 0.913 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
