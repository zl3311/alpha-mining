---
field: fn_comp_options_out_intrinsic_value_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.53
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.2026
ann_vol: 0.0925
hit_rate: 0.5109
rolling_sharpe_min: -1.338
rolling_sharpe_max: 2.438
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.2
---
# fn_comp_options_out_intrinsic_value_a (fundamental2)

*The intrinsic value of a stock option is the amount by which the market value of the underlying stock exceeds the exercise price of the option.*

## Signal Profile
- `rank(fn_comp_options_out_intrinsic_value_a)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP200)
- `rank(fn_comp_options_out_intrinsic_value_a / close)`: S=0.33, F=0.16, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_options_out_intrinsic_value_a, 5))`: S=0.28, F=0.12, T=26.1%, INFERIOR (TOP200)
- `-rank(fn_comp_options_out_intrinsic_value_a)`: S=0.24, F=0.09, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_intrinsic_value_a, 5))`: S=0.53, F=0.25, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_options_out_intrinsic_value_a, 22)`: S=-0.17, F=-0.07, T=20.4%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_out_intrinsic_value_a, 10)`: S=-0.23, F=-0.16, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_out_intrinsic_value_a, 22))`: S=0.04, F=0.01, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_intrinsic_value_a)`: S=0.22, F=0.08, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_intrinsic_value_a / close)`: S=0.10, F=0.02, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.32, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.11 (negative), ret=-0.6%
  - 2020: S=2.31 (strong), ret=+20.2%
  - 2021: S=0.24 (weak), ret=+2.6%
  - 2022: S=-0.72 (negative), ret=-8.4%
  - 2023: S=0.10 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 20.26% over 799 days (not yet recovered, ongoing at window end)
- Annualized: return +3.0%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.01, excess kurtosis +2.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 2.44, latest 0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.06%; worst month: -4.30%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.46
- Sideways: S=-0.39
- Bear: S=0.79

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_out_intrinsic_value_a, 5))` S=0.53, F=0.25, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_out_intrinsic_value_a)`: S=0.22, F=0.08, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_intrinsic_value_a / close)`: S=0.10, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_intrinsic_value_a, 5))`: S=0.53, F=0.25, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_out_intrinsic_value_a / close)` | TOP200 | 0.32 | 0.16 | 20.3% | 60% | mixed |
| `rank(ts_delta(fn_comp_options_out_intrinsic_value_a, 5))` | TOP200 | 0.28 | 0.12 | 29.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_optexd: 0.643 (moderately positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.574 (moderately positively correlated)
- fnd6_optex: 0.529 (moderately positively correlated)
- fn_comp_options_out_number_q: 0.506 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.446 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
