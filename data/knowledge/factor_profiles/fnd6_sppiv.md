---
field: fnd6_sppiv
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.46
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.1193
ann_vol: 0.0858
hit_rate: 0.5158
rolling_sharpe_min: -0.787
rolling_sharpe_max: 2.102
negated_best_sharpe: 0.65
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.19
---
# fnd6_sppiv (fundamental6)

*Sale of Property, Plant and Equipment and Investments - Gain (Loss)*

## Signal Profile
- `rank(fnd6_sppiv)`: S=0.43, F=0.23, T=2.8%, INFERIOR (TOP200)
- `rank(fnd6_sppiv / close)`: S=0.39, F=0.20, T=2.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_sppiv, 5))`: S=0.40, F=0.20, T=32.0%, INFERIOR (TOP500)
- `-rank(fnd6_sppiv)`: S=0.37, F=0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sppiv, 5))`: S=0.06, F=0.01, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_sppiv, 22)`: S=0.46, F=0.48, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_sppiv, 10)`: S=0.16, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_sppiv, 22))`: S=-0.38, F=-0.21, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppiv)`: S=0.61, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppiv / close)`: S=0.65, F=0.26, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.11 (moderate), ret=+6.3%
  - 2020: S=1.52 (strong), ret=+11.6%
  - 2021: S=-0.02 (negative), ret=-0.2%
  - 2022: S=-0.03 (negative), ret=-0.3%
  - 2023: S=0.17 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 11.93% over 577 days (not yet recovered, ongoing at window end)
- Annualized: return +3.8%, volatility 8.6% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.56, excess kurtosis +5.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.79, max 2.10, latest 0.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.35%; worst month: -6.93%
Positive months: 58%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.29
- Sideways: S=0.81
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * fnd6_sppiv / close)` S=0.65, F=0.26, INFERIOR
Direction gap: +0.19 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_sppiv)`: S=0.61, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppiv / close)`: S=0.65, F=0.26, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sppiv, 5))`: S=0.06, F=0.01, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_sppiv)` | TOP200 | 0.44 | 0.23 | 11.9% | 60% | weak |
| `rank(ts_delta(fnd6_sppiv, 5))` | TOP500 | 0.39 | 0.20 | 41.8% | 60% | bull-only |
| `rank(fnd6_sppiv / close)` | TOP200 | 0.40 | 0.20 | 12.1% | 40% | weak |

## Correlation Notes
Top correlates:
- anl4_af_div_value: -0.411 (moderately negatively correlated)
- fnd6_loxdr: -0.409 (moderately negatively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.408 (moderately positively correlated)
- cash_flow_from_financing: 0.404 (moderately positively correlated)
- fnd6_newa1v1300_dv: -0.403 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
