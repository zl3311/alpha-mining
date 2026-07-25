---
field: fn_comp_options_grants_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.92
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0964
ann_vol: 0.0488
hit_rate: 0.4955
rolling_sharpe_min: -1.487
rolling_sharpe_max: 2.531
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: 0.44
---
# fn_comp_options_grants_a (fundamental2)

*Net number of share options (or share units) granted during the period.*

## Signal Profile
- `rank(fn_comp_options_grants_a)`: S=0.28, F=0.11, T=1.8%, INFERIOR (TOP200)
- `rank(fn_comp_options_grants_a / close)`: S=0.48, F=0.21, T=1.6%, INFERIOR (TOP500)
- `rank(ts_delta(fn_comp_options_grants_a, 5))`: S=-0.51, F=-0.25, T=33.7%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_grants_a)`: S=-0.11, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_a, 5))`: S=0.92, F=0.71, T=31.8%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_options_grants_a, 22)`: S=-0.29, F=-0.17, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_grants_a, 10)`: S=-0.92, F=-1.21, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_grants_a, 22))`: S=-0.07, F=-0.02, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_a)`: S=-0.33, F=-0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_a / close)`: S=-0.48, F=-0.21, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.16 (moderate), ret=+3.7%
  - 2020: S=2.08 (strong), ret=+9.7%
  - 2021: S=-0.80 (negative), ret=-4.6%
  - 2022: S=0.04 (weak), ret=+0.2%
  - 2023: S=0.48 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 9.64% over 1051 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 4.9% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.38, excess kurtosis +1.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 2.53, latest 0.49

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +4.54%; worst month: -2.48%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.07
- Sideways: S=-0.19
- Bear: S=1.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_options_grants_a, 5))` S=0.92, F=0.71, INFERIOR
Direction gap: +0.44 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_comp_options_grants_a)`: S=-0.33, F=-0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_grants_a / close)`: S=-0.48, F=-0.21, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_grants_a, 5))`: S=0.92, F=0.71, T=31.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_options_grants_a / close)` | TOP500 | 0.48 | 0.21 | 9.6% | 80% | mixed |
| `rank(fn_comp_options_grants_a / close)` | TOP200 | 0.36 | 0.17 | 17.5% | 80% | mixed |
| `rank(fn_comp_options_grants_a)` | TOP200 | 0.26 | 0.11 | 16.4% | 60% | mixed |
| `rank(fn_comp_options_grants_a)` | TOP500 | 0.32 | 0.11 | 7.5% | 80% | mixed |
| `rank(fn_comp_options_grants_a / close)` | TOP1000 | 0.30 | 0.10 | 12.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_optgr: 0.672 (moderately positively correlated)
- fn_comp_options_out_number_a: 0.637 (moderately positively correlated)
- fnd6_sstk: 0.564 (moderately positively correlated)
- fnd6_optosey: 0.562 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.516 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
