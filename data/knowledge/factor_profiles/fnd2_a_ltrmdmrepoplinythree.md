---
field: fnd2_a_ltrmdmrepoplinythree
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.66
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.059
ann_vol: 0.0413
hit_rate: 0.5093
rolling_sharpe_min: -0.71
rolling_sharpe_max: 2.139
redundancy_cluster: 34
negated_best_sharpe: 0.66
negated_best_template: neg_rank_level
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: -0.14
---
# fnd2_a_ltrmdmrepoplinythree (fundamental2)

*Amount of long-term debt payable, sinking fund requirements, and other securities issued that are redeemable by holder at fixed or determinable prices and dates maturing in the 3rd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_ltrmdmrepoplinythree)`: S=0.33, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_ltrmdmrepoplinythree / close)`: S=0.80, F=0.41, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))`: S=0.63, F=0.37, T=31.9%, INFERIOR (TOP500)
- `-rank(fnd2_a_ltrmdmrepoplinythree)`: S=-0.11, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))`: S=0.31, F=0.15, T=27.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_ltrmdmrepoplinythree, 63)`: S=0.49, F=0.37, T=14.6%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_ltrmdmrepoplinythree, 10)`: S=0.13, F=0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_ltrmdmrepoplinythree, 22))`: S=-0.51, F=-0.30, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinythree)`: S=0.66, F=0.44, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinythree / close)`: S=0.46, F=0.27, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.00 (weak), ret=+0.0%
  - 2020: S=0.88 (moderate), ret=+5.0%
  - 2021: S=0.54 (moderate), ret=+2.1%
  - 2022: S=1.67 (strong), ret=+6.0%
  - 2023: S=0.83 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 5.90% over 248 days (recovered)
- Annualized: return +3.2%, volatility 4.1% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.61, excess kurtosis +3.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.71, max 2.14, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +3.90%; worst month: -1.94%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.97
- Sideways: S=0.59
- Bear: S=-0.29

## Negated Direction
Best negated: `rank(-1 * fnd2_a_ltrmdmrepoplinythree)` S=0.66, F=0.44, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_ltrmdmrepoplinythree)`: S=0.66, F=0.44, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_ltrmdmrepoplinythree / close)`: S=0.46, F=0.27, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))`: S=0.31, F=0.15, T=27.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_ltrmdmrepoplinythree / close)` | TOP3000 | 0.78 | 0.41 | 5.9% | 100% | mixed |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))` | TOP500 | 0.65 | 0.37 | 27.0% | 80% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplinythree / close)` | TOP1000 | 0.39 | 0.16 | 7.4% | 60% | bull-only |
| `rank(fnd2_a_ltrmdmrepoplinythree)` | TOP3000 | 0.32 | 0.12 | 11.8% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))` | TOP3000 | 0.28 | 0.09 | 20.3% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_ltrmdmrepoplinythree, 5))` | TOP1000 | 0.22 | 0.06 | 31.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_ltrmdmrepoplinyfour: 0.834 (strongly positively correlated)
- fn_interest_paid_net_a: 0.817 (strongly positively correlated)
- fnd6_intpn: 0.805 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.800 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.795 (strongly positively correlated)

Redundancy cluster #34: 4 similar fields, mean |rho| 0.713 (representative: fn_derivative_notional_amount_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
