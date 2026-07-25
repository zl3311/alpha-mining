---
field: fn_comp_options_grants_weighted_avg_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1552
ann_vol: 0.0933
hit_rate: 0.485
rolling_sharpe_min: -0.885
rolling_sharpe_max: 1.783
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.65
---
# fn_comp_options_grants_weighted_avg_a (fundamental2)

*Weighted average price at which grantees could have acquired the underlying shares with respect to stock options that were terminated.*

## Signal Profile
- `rank(fn_comp_options_grants_weighted_avg_a)`: S=0.10, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_comp_options_grants_weighted_avg_a / close)`: S=0.20, F=0.08, T=3.1%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_options_grants_weighted_avg_a, 5))`: S=0.07, F=0.01, T=33.5%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_grants_weighted_avg_a)`: S=0.13, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_weighted_avg_a, 5))`: S=0.17, F=0.05, T=32.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_grants_weighted_avg_a, 63)`: S=0.82, F=0.92, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_grants_weighted_avg_a, 10)`: S=0.14, F=0.08, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_grants_weighted_avg_a, 22))`: S=-0.48, F=-0.30, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_weighted_avg_a)`: S=0.13, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_weighted_avg_a / close)`: S=-0.21, F=-0.07, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+3.6%
  - 2020: S=-0.32 (negative), ret=-2.9%
  - 2021: S=0.83 (moderate), ret=+10.0%
  - 2022: S=-0.28 (negative), ret=-3.0%
  - 2023: S=0.22 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 15.52% over 701 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 9.3% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew +0.11, excess kurtosis +2.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 1.78, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.36%; worst month: -4.28%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.54
- Sideways: S=-0.01
- Bear: S=-1.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_grants_weighted_avg_a, 5))` S=0.17, F=0.05, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_options_grants_weighted_avg_a)`: S=0.13, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_weighted_avg_a / close)`: S=-0.21, F=-0.07, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_weighted_avg_a, 5))`: S=0.17, F=0.05, T=32.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_grants_weighted_avg_a / close)` | TOP200 | 0.20 | 0.08 | 15.5% | 60% | bull-only |
| `rank(fn_comp_options_grants_weighted_avg_a / close)` | TOP1000 | 0.21 | 0.07 | 11.3% | 80% | mixed |
| `rank(fn_comp_options_grants_weighted_avg_a / close)` | TOP3000 | 0.11 | 0.03 | 15.7% | 80% | mixed |
| `rank(fn_comp_options_grants_weighted_avg_a)` | TOP3000 | 0.10 | 0.02 | 21.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcgr: 0.563 (moderately positively correlated)
- fn_proceeds_from_issuance_of_debt_a: 0.558 (moderately positively correlated)
- fnd6_newa1v1300_icapt: 0.551 (moderately positively correlated)
- fnd6_newa2v1300_stkco: 0.550 (moderately positively correlated)
- fnd6_prcl: 0.534 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
