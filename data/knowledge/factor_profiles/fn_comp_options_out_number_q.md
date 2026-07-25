---
field: fn_comp_options_out_number_q
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.52
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.3027
ann_vol: 0.1435
hit_rate: 0.5053
rolling_sharpe_min: -1.102
rolling_sharpe_max: 2.598
negated_best_sharpe: 0.25
negated_best_template: neg_rank_level
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.27
---
# fn_comp_options_out_number_q (fundamental2)

*Number of options outstanding, including both vested and non-vested options.*

## Signal Profile
- `rank(fn_comp_options_out_number_q)`: S=0.20, F=0.09, T=2.1%, INFERIOR (TOP200)
- `rank(fn_comp_options_out_number_q / close)`: S=0.28, F=0.16, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_options_out_number_q, 5))`: S=0.25, F=0.09, T=36.4%, INFERIOR (TOP500)
- `-rank(fn_comp_options_out_number_q)`: S=-0.07, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_number_q, 5))`: S=0.16, F=0.04, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_out_number_q, 63)`: S=0.31, F=0.15, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_out_number_q, 10)`: S=0.12, F=0.09, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_out_number_q, 22))`: S=0.52, F=0.29, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_q)`: S=0.25, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_q / close)`: S=0.17, F=0.06, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.42 (weak), ret=+3.4%
  - 2020: S=1.94 (strong), ret=+26.0%
  - 2021: S=0.46 (weak), ret=+6.8%
  - 2022: S=-0.98 (negative), ret=-17.6%
  - 2023: S=0.20 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 30.27% over 1022 days (not yet recovered, ongoing at window end)
- Annualized: return +4.4%, volatility 14.3% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.30, excess kurtosis +2.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 2.60, latest 0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +11.92%; worst month: -6.98%
Positive months: 48%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.55
- Sideways: S=0.20
- Bear: S=1.31

## Negated Direction
Best negated: `rank(-1 * fn_comp_options_out_number_q)` S=0.25, F=0.10, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_out_number_q)`: S=0.25, F=0.10, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_number_q / close)`: S=0.17, F=0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_number_q, 5))`: S=0.16, F=0.04, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_out_number_q / close)` | TOP200 | 0.30 | 0.16 | 30.3% | 80% | bear-only |
| `rank(fn_comp_options_out_number_q / close)` | TOP500 | 0.26 | 0.12 | 25.4% | 60% | mixed |
| `rank(ts_delta(fn_comp_options_out_number_q, 5))` | TOP500 | 0.26 | 0.09 | 29.2% | 60% | bull-only |
| `rank(fn_comp_options_out_number_q)` | TOP200 | 0.23 | 0.09 | 25.9% | 60% | bear-only |
| `rank(fn_comp_options_out_number_q)` | TOP500 | 0.19 | 0.07 | 18.5% | 60% | mixed |
| `rank(fn_comp_options_out_number_q / close)` | TOP1000 | 0.11 | 0.03 | 30.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_antidilutive_securities_excl_from_eps_a: 0.606 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_q: 0.600 (moderately positively correlated)
- fnd6_newa2v1300_optexd: 0.569 (moderately positively correlated)
- fnd6_optex: 0.566 (moderately positively correlated)
- fnd6_cshtrq: 0.542 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
