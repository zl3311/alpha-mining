---
field: fnd6_dlcch
dataset: fundamental6
best_template: neg_rank
best_sharpe: 0.42
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.264
ann_vol: 0.1928
hit_rate: 0.5053
rolling_sharpe_min: -1.061
rolling_sharpe_max: 1.852
negated_best_sharpe: 0.42
negated_best_template: neg_rank
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.13
---
# fnd6_dlcch (fundamental6)

*Current Debt - Changes*

## Signal Profile
- `rank(fnd6_dlcch)`: S=0.06, F=0.01, T=2.9%, INFERIOR (TOP200)
- `rank(fnd6_dlcch / close)`: S=0.11, F=0.02, T=2.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dlcch, 5))`: S=0.29, F=0.12, T=33.0%, INFERIOR (TOP1000)
- `-rank(fnd6_dlcch)`: S=0.42, F=0.16, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dlcch, 5))`: S=-0.11, F=-0.03, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dlcch, 63)`: S=-0.12, F=-0.05, T=15.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dlcch, 10)`: S=-0.43, F=-0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dlcch, 22))`: S=-0.11, F=-0.03, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlcch)`: S=0.42, F=0.16, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlcch / close)`: S=0.39, F=0.14, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+1.8%
  - 2020: S=1.04 (moderate), ret=+21.6%
  - 2021: S=0.42 (weak), ret=+7.4%
  - 2022: S=0.18 (weak), ret=+4.7%
  - 2023: S=-0.70 (negative), ret=-8.6%

## Risk & Drawdown
- Max drawdown: 26.40% over 719 days (recovered)
- Annualized: return +5.5%, volatility 19.3% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.68, excess kurtosis +12.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 1.85, latest -0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +12.54%; worst month: -9.37%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.61
- Sideways: S=0.56
- Bear: S=-0.56

## Negated Direction
Best negated: `-rank(fnd6_dlcch)` S=0.42, F=0.16, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_dlcch)`: S=0.42, F=0.16, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dlcch / close)`: S=0.39, F=0.14, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dlcch, 5))`: S=-0.11, F=-0.03, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dlcch, 5))` | TOP1000 | 0.28 | 0.12 | 26.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_dlcch, 5))` | TOP500 | 0.17 | 0.07 | 37.1% | 40% | weak |
| `rank(ts_delta(fnd6_dlcch, 5))` | TOP3000 | 0.18 | 0.06 | 34.4% | 60% | weak |
| `rank(fnd6_dlcch / close)` | TOP500 | 0.10 | 0.02 | 19.3% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_invrm: 0.186 (weakly positively correlated)
- fnd6_newa1v1300_gdwl: 0.160 (weakly positively correlated)
- fn_comp_non_opt_nonvested_number_a: 0.140 (weakly positively correlated)
- fn_business_combination_assets_aquired_goodwill_a: 0.134 (weakly positively correlated)
- news_mov_vol: -0.129 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
