---
field: fnd2_itxreclstatelocalitxes
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.68
best_fitness: 0.55
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.486
ann_vol: 0.2109
hit_rate: 0.4753
rolling_sharpe_min: -1.518
rolling_sharpe_max: 3.84
negated_best_sharpe: 0.48
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.2
---
# fnd2_itxreclstatelocalitxes (fundamental2)

*Amount of the difference between reported income tax expense (benefit) and expected income tax expense (benefit) computed by applying the domestic federal statutory income tax rates to pretax income (loss) from continuing operations attributable to state and local income tax expense (benefit).*

## Signal Profile
- `rank(fnd2_itxreclstatelocalitxes)`: S=0.43, F=0.23, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd2_itxreclstatelocalitxes / close)`: S=0.47, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_itxreclstatelocalitxes, 5))`: S=0.68, F=0.55, T=21.6%, INFERIOR (TOP200)
- `-rank(fnd2_itxreclstatelocalitxes)`: S=0.01, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_itxreclstatelocalitxes, 5))`: S=-0.54, F=-0.32, T=29.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_itxreclstatelocalitxes, 22)`: S=-0.29, F=-0.17, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_itxreclstatelocalitxes, 10)`: S=-0.52, F=-0.31, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_itxreclstatelocalitxes, 22))`: S=0.10, F=0.03, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreclstatelocalitxes)`: S=0.48, F=0.31, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreclstatelocalitxes / close)`: S=0.35, F=0.19, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.68, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.11 (weak), ret=+1.8%
  - 2020: S=-0.73 (negative), ret=-15.2%
  - 2021: S=1.78 (strong), ret=+42.9%
  - 2022: S=0.69 (moderate), ret=+12.3%
  - 2023: S=1.23 (moderate), ret=+28.0%

## Risk & Drawdown
- Max drawdown: 48.60% over 886 days (recovered)
- Annualized: return +14.2%, volatility 21.1% (fraction of booksize)
- Hit rate: 47.5% positive days
- Tail shape: skew +0.37, excess kurtosis +5.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.52, max 3.84, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +31.10%; worst month: -13.29%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.21
- Sideways: S=0.75
- Bear: S=-0.00

## Negated Direction
Best negated: `rank(-1 * fnd2_itxreclstatelocalitxes)` S=0.48, F=0.31, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_itxreclstatelocalitxes)`: S=0.48, F=0.31, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_itxreclstatelocalitxes / close)`: S=0.35, F=0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_itxreclstatelocalitxes, 5))`: S=-0.54, F=-0.32, T=29.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_itxreclstatelocalitxes, 5))` | TOP200 | 0.68 | 0.55 | 48.6% | 80% | mixed |
| `rank(fnd2_itxreclstatelocalitxes / close)` | TOP3000 | 0.46 | 0.25 | 14.4% | 80% | bull-only |
| `rank(fnd2_itxreclstatelocalitxes)` | TOP3000 | 0.42 | 0.23 | 22.1% | 80% | bull-only |
| `rank(ts_delta(fnd2_itxreclstatelocalitxes, 5))` | TOP500 | 0.33 | 0.15 | 27.5% | 60% | mixed |
| `rank(ts_delta(fnd2_itxreclstatelocalitxes, 5))` | TOP1000 | 0.32 | 0.13 | 29.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.293 (weakly positively correlated)
- fnd2_ebitdm: 0.281 (weakly positively correlated)
- anl4_cfi_low: -0.263 (weakly negatively correlated)
- anl4_cfi_median: -0.258 (weakly negatively correlated)
- min_stock_option_expense_guidance: 0.258 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
