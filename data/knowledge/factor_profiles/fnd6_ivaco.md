---
field: fnd6_ivaco
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.37
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0312
ann_vol: 0.0313
hit_rate: 0.5263
rolling_sharpe_min: -0.722
rolling_sharpe_max: 3.706
top_merge_partner: fn_assets_fair_val_l2_q
negated_best_sharpe: 0.25
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -1.12
---
# fnd6_ivaco (fundamental6)

*Investing Activities - Other*

## Signal Profile
- `rank(fnd6_ivaco)`: S=1.34, F=0.74, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_ivaco / close)`: S=1.37, F=0.80, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ivaco, 5))`: S=0.52, F=0.30, T=31.0%, INFERIOR (TOP200)
- `-rank(fnd6_ivaco)`: S=-0.55, F=-0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivaco, 5))`: S=-0.19, F=-0.06, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ivaco, 63)`: S=0.37, F=0.19, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivaco, 10)`: S=0.07, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivaco, 22))`: S=-0.75, F=-0.50, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaco)`: S=0.25, F=0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaco / close)`: S=0.12, F=0.02, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 30F/2P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.35 (negative), ret=-0.7%
  - 2020: S=1.33 (moderate), ret=+3.2%
  - 2021: S=2.54 (strong), ret=+8.1%
  - 2022: S=1.89 (strong), ret=+8.5%
  - 2023: S=0.59 (moderate), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 3.12% over 268 days (recovered)
- Annualized: return +4.2%, volatility 3.1% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.02, excess kurtosis +2.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 3.71, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +2.35%; worst month: -1.50%
Positive months: 71%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.86
- Sideways: S=0.69
- Bear: S=0.28

## Negated Direction
Best negated: `rank(-1 * fnd6_ivaco)` S=0.25, F=0.06, INFERIOR
Direction gap: -1.12 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_ivaco)`: S=0.25, F=0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivaco / close)`: S=0.12, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivaco, 5))`: S=-0.19, F=-0.06, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ivaco / close)` | TOP3000 | 1.35 | 0.80 | 3.1% | 80% | mixed |
| `rank(fnd6_ivaco)` | TOP3000 | 1.32 | 0.74 | 2.9% | 80% | mixed |
| `rank(fnd6_ivaco / close)` | TOP1000 | 0.78 | 0.34 | 4.7% | 60% | mixed |
| `rank(ts_delta(fnd6_ivaco, 5))` | TOP200 | 0.51 | 0.30 | 24.9% | 40% | mixed |
| `rank(fnd6_ivaco)` | TOP1000 | 0.55 | 0.19 | 4.1% | 60% | bull-only |
| `rank(fnd6_ivaco / close)` | TOP200 | 0.36 | 0.15 | 8.1% | 80% | weak |
| `rank(fnd6_ivaco)` | TOP200 | 0.29 | 0.11 | 7.5% | 80% | weak |
| `rank(ts_delta(fnd6_ivaco, 5))` | TOP3000 | 0.31 | 0.10 | 17.7% | 60% | all-weather |
| `rank(ts_delta(fnd6_ivaco, 5))` | TOP500 | 0.20 | 0.07 | 38.9% | 80% | mixed |
| `rank(ts_delta(fnd6_ivaco, 5))` | TOP1000 | 0.09 | 0.02 | 41.5% | 60% | weak |

## Correlation Notes
Top correlates:
- eps_min_guidance_quarterly: 0.664 (moderately positively correlated)
- eps_max_guidance_quarterly: 0.664 (moderately positively correlated)
- min_capital_expenditure_guidance: 0.651 (moderately positively correlated)
- max_capital_expenditure_guidance: 0.650 (moderately positively correlated)
- max_reported_eps_guidance: 0.642 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_assets_fair_val_l2_q | fundamental2 | -0.18 | 1.98 | +0.63 | -0.46 | yes |
| implied_volatility_call_720 | option8 | -0.16 | 2.25 | +0.67 | +0.94 | yes |
| implied_volatility_call_1080 | option8 | -0.16 | 2.28 | +0.67 | +0.99 | yes |
| implied_volatility_put_1080 | option8 | -0.13 | 2.05 | +0.66 | +0.73 | yes |
| implied_volatility_mean_720 | option8 | -0.17 | 2.16 | +0.66 | +0.83 | yes |

## Actionability
Already in submitted book (alpha: ['1YJagrVk']).
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
