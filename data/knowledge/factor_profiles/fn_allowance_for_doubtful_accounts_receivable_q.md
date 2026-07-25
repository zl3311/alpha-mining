---
field: fn_allowance_for_doubtful_accounts_receivable_q
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.43
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0842
ann_vol: 0.0686
hit_rate: 0.4899
rolling_sharpe_min: -0.859
rolling_sharpe_max: 1.976
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.13
---
# fn_allowance_for_doubtful_accounts_receivable_q (fundamental2)

*For an unclassified balance sheet, a valuation allowance for receivables due a company that are expected to be uncollectible.*

## Signal Profile
- `rank(fn_allowance_for_doubtful_accounts_receivable_q)`: S=0.37, F=0.18, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_allowance_for_doubtful_accounts_receivable_q / close)`: S=0.40, F=0.19, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))`: S=0.40, F=0.13, T=35.6%, INFERIOR (TOP3000)
- `-rank(fn_allowance_for_doubtful_accounts_receivable_q)`: S=-0.23, F=-0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))`: S=0.30, F=0.11, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(fn_allowance_for_doubtful_accounts_receivable_q, 22)`: S=0.43, F=0.21, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fn_allowance_for_doubtful_accounts_receivable_q, 10)`: S=0.15, F=0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_allowance_for_doubtful_accounts_receivable_q, 22))`: S=-0.02, F=0.00, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_q)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_q / close)`: S=-0.15, F=-0.05, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.47 (weak), ret=+2.3%
  - 2020: S=0.10 (weak), ret=+0.9%
  - 2021: S=0.61 (moderate), ret=+4.7%
  - 2022: S=0.84 (moderate), ret=+5.1%
  - 2023: S=0.10 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 8.42% over 273 days (recovered)
- Annualized: return +2.7%, volatility 6.9% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.94, excess kurtosis +7.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 1.98, latest 0.23

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.93%; worst month: -5.10%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.29
- Sideways: S=-0.07
- Bear: S=-1.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))` S=0.30, F=0.11, INFERIOR
Direction gap: -0.13 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_q)`: S=0.01, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_allowance_for_doubtful_accounts_receivable_q / close)`: S=-0.15, F=-0.05, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))`: S=0.30, F=0.11, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_allowance_for_doubtful_accounts_receivable_q / close)` | TOP3000 | 0.40 | 0.19 | 8.4% | 100% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_q)` | TOP3000 | 0.36 | 0.18 | 25.2% | 80% | bull-only |
| `rank(ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))` | TOP3000 | 0.43 | 0.13 | 23.5% | 80% | all-weather |
| `rank(fn_allowance_for_doubtful_accounts_receivable_q / close)` | TOP200 | 0.23 | 0.12 | 24.9% | 40% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_q / close)` | TOP1000 | 0.26 | 0.12 | 16.7% | 60% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_q)` | TOP1000 | 0.22 | 0.10 | 30.6% | 60% | bull-only |
| `rank(fn_allowance_for_doubtful_accounts_receivable_q / close)` | TOP500 | 0.14 | 0.05 | 27.4% | 40% | bull-only |
| `rank(ts_delta(fn_allowance_for_doubtful_accounts_receivable_q, 5))` | TOP200 | 0.13 | 0.03 | 36.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_allowance_for_doubtful_accounts_receivable_a: 0.942 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.889 (strongly positively correlated)
- fnd2_a_flintasamt1expnext12m: 0.883 (strongly positively correlated)
- fn_interest_paid_net_a: 0.880 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.879 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
