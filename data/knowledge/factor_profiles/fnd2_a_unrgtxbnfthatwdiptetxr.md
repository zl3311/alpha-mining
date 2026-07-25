---
field: fnd2_a_unrgtxbnfthatwdiptetxr
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.55
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2803
ann_vol: 0.143
hit_rate: 0.5304
rolling_sharpe_min: -0.686
rolling_sharpe_max: 2.294
negated_best_sharpe: 0.28
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.27
---
# fnd2_a_unrgtxbnfthatwdiptetxr (fundamental2)

*The total amount of unrecognized tax benefits that, if recognized, would affect the effective tax rate.*

## Signal Profile
- `rank(fnd2_a_unrgtxbnfthatwdiptetxr)`: S=-0.01, F=0.00, T=0.6%, INFERIOR (TOP3000)
- `rank(fnd2_a_unrgtxbnfthatwdiptetxr / close)`: S=0.47, F=0.21, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))`: S=0.55, F=0.26, T=33.8%, INFERIOR (TOP3000)
- `-rank(fnd2_a_unrgtxbnfthatwdiptetxr)`: S=-0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))`: S=-0.50, F=-0.24, T=31.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_unrgtxbnfthatwdiptetxr, 22)`: S=0.27, F=0.13, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_unrgtxbnfthatwdiptetxr, 10)`: S=0.30, F=0.14, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_unrgtxbnfthatwdiptetxr, 22))`: S=0.40, F=0.19, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfthatwdiptetxr)`: S=0.28, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfthatwdiptetxr / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.68 (negative), ret=-8.3%
  - 2020: S=0.83 (moderate), ret=+13.5%
  - 2021: S=1.15 (moderate), ret=+17.4%
  - 2022: S=0.19 (weak), ret=+2.7%
  - 2023: S=1.03 (moderate), ret=+12.5%

## Risk & Drawdown
- Max drawdown: 28.03% over 480 days (recovered)
- Annualized: return +7.7%, volatility 14.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.11, excess kurtosis +7.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 2.29, latest 1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.51%; worst month: -11.77%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.45
- Sideways: S=-0.51
- Bear: S=1.47

## Negated Direction
Best negated: `rank(-1 * fnd2_a_unrgtxbnfthatwdiptetxr)` S=0.28, F=0.13, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_unrgtxbnfthatwdiptetxr)`: S=0.28, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_unrgtxbnfthatwdiptetxr / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))`: S=-0.50, F=-0.24, T=31.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))` | TOP3000 | 0.54 | 0.26 | 28.0% | 80% | mixed |
| `rank(ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))` | TOP200 | 0.47 | 0.26 | 22.2% | 80% | mixed |
| `rank(fnd2_a_unrgtxbnfthatwdiptetxr / close)` | TOP3000 | 0.45 | 0.21 | 7.8% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))` | TOP1000 | 0.45 | 0.19 | 19.0% | 80% | mixed |
| `rank(ts_delta(fnd2_a_unrgtxbnfthatwdiptetxr, 5))` | TOP500 | 0.44 | 0.19 | 21.1% | 80% | mixed |
| `rank(fnd2_a_unrgtxbnfthatwdiptetxr / close)` | TOP1000 | 0.22 | 0.09 | 11.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- news_atr14: 0.115 (weakly positively correlated)
- fnd2_dfdtxasoprlcarryfwd: -0.111 (weakly negatively correlated)
- anl4_afv4_eps_number: -0.109 (weakly negatively correlated)
- fn_comp_options_grants_fair_value_a: 0.107 (weakly positively correlated)
- fn_liab_fair_val_a: -0.104 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
