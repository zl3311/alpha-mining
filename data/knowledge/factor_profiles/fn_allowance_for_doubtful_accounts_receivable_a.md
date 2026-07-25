---
field: fn_allowance_for_doubtful_accounts_receivable_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0814
ann_vol: 0.0631
hit_rate: 0.4785
rolling_sharpe_min: -0.923
rolling_sharpe_max: 1.942
negated_best_sharpe: 0.26
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.2
---
# fn_allowance_for_doubtful_accounts_receivable_a (fundamental2)

*For an unclassified balance sheet, a valuation allowance for receivables due a company that are expected to be uncollectible.*

## Signal Profile
- `rank(fn_allowance_for_doubtful_accounts_receivable_a)`: S=0.35, F=0.16, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_allowance_for_doubtful_accounts_receivable_a / close)`: S=0.46, F=0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_allowance_for_doubtful_accounts_receivable_a, 5))`: S=0.08, F=0.02, T=33.8%, INFERIOR (TOP500)
- `-rank(fn_allowance_for_doubtful_accounts_receivable_a)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allowance_for_doubtful_accounts_receivable_a, 5))`: S=0.04, F=0.01, T=29.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_allowance_for_doubtful_accounts_receivable_a, 63)`: S=-0.28, F=-0.15, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_allowance_for_doubtful_accounts_receivable_a, 10)`: S=0.19, F=0.07, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_allowance_for_doubtful_accounts_receivable_a, 22))`: S=-0.62, F=-0.41, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_a)`: S=0.26, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_a / close)`: S=0.18, F=0.07, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+0.8%
  - 2020: S=-0.17 (negative), ret=-1.4%
  - 2021: S=0.78 (moderate), ret=+5.9%
  - 2022: S=1.50 (strong), ret=+9.3%
  - 2023: S=-0.10 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 8.14% over 245 days (recovered)
- Annualized: return +2.9%, volatility 6.3% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.67, excess kurtosis +3.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 1.94, latest 0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.52%; worst month: -3.70%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.54
- Sideways: S=-0.25
- Bear: S=-1.49

## Negated Direction
Best negated: `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_a)` S=0.26, F=0.14, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_a)`: S=0.26, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_a / close)`: S=0.18, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allowance_for_doubtful_accounts_receivable_a, 5))`: S=0.04, F=0.01, T=29.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_allowance_for_doubtful_accounts_receivable_a / close)` | TOP3000 | 0.46 | 0.22 | 8.1% | 60% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_a)` | TOP3000 | 0.34 | 0.16 | 24.5% | 60% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_a / close)` | TOP1000 | 0.12 | 0.04 | 21.2% | 60% | bull-only |
| `rank(ts_delta(fn_allowance_for_doubtful_accounts_receivable_a, 5))` | TOP500 | 0.07 | 0.02 | 40.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_allowance_for_doubtful_accounts_receivable_q: 0.942 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.903 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.903 (strongly positively correlated)
- fn_employee_related_liab_a: 0.902 (strongly positively correlated)
- fnd6_newa1v1300_ap: 0.901 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
