---
field: fnd6_optgr
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.92
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1973
ann_vol: 0.0592
hit_rate: 0.4947
rolling_sharpe_min: -2.461
rolling_sharpe_max: 2.669
negated_best_sharpe: 0.92
negated_best_template: rank_neg_delta
negated_best_fitness: 0.75
n_negated_sims: 10
direction_gap: 0.43
---
# fnd6_optgr (fundamental6)

*Options - Granted*

## Signal Profile
- `rank(fnd6_optgr)`: S=0.28, F=0.08, T=2.5%, INFERIOR (TOP1000)
- `rank(fnd6_optgr / close)`: S=0.37, F=0.15, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_optgr, 5))`: S=-0.28, F=-0.16, T=20.8%, INFERIOR (TOP200)
- `-rank(fnd6_optgr)`: S=-0.28, F=-0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optgr, 5))`: S=0.92, F=0.75, T=28.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optgr, 63)`: S=0.49, F=0.38, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optgr, 10)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optgr, 22))`: S=0.19, F=0.07, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optgr)`: S=-0.23, F=-0.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optgr / close)`: S=-0.37, F=-0.15, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.18 (moderate), ret=+5.3%
  - 2020: S=1.67 (strong), ret=+10.5%
  - 2021: S=-1.14 (negative), ret=-6.9%
  - 2022: S=-0.56 (negative), ret=-3.9%
  - 2023: S=1.14 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 19.73% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 5.9% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.44, excess kurtosis +3.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.46, max 2.67, latest 1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.13%; worst month: -3.93%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.10
- Sideways: S=0.21
- Bear: S=1.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optgr, 5))` S=0.92, F=0.75, INFERIOR
Direction gap: +0.43 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_optgr)`: S=-0.23, F=-0.07, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optgr / close)`: S=-0.37, F=-0.15, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optgr, 5))`: S=0.92, F=0.75, T=28.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optgr / close)` | TOP500 | 0.37 | 0.15 | 19.7% | 60% | mixed |
| `rank(fnd6_optgr / close)` | TOP1000 | 0.35 | 0.13 | 13.4% | 60% | bear-only |
| `rank(fnd6_optgr)` | TOP1000 | 0.28 | 0.08 | 9.2% | 60% | weak |
| `rank(fnd6_optgr)` | TOP500 | 0.22 | 0.07 | 16.0% | 60% | weak |
| `rank(fnd6_optgr / close)` | TOP200 | 0.15 | 0.05 | 27.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_optosey: 0.742 (strongly positively correlated)
- fn_comp_options_grants_a: 0.672 (moderately positively correlated)
- fn_comp_options_out_number_a: 0.614 (moderately positively correlated)
- fnd6_sstk: 0.482 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.464 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
