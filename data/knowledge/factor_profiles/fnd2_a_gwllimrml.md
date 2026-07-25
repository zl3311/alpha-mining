---
field: fnd2_a_gwllimrml
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.91
best_fitness: 0.99
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2549
ann_vol: 0.2376
hit_rate: 0.4915
rolling_sharpe_min: -0.842
rolling_sharpe_max: 2.147
negated_best_sharpe: 0.25
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.66
---
# fnd2_a_gwllimrml (fundamental2)

*Amount of loss from the write-down of an asset representing the future economic benefits arising from other assets acquired in a business combination that are not individually identified and separately recognized.*

## Signal Profile
- `rank(fnd2_a_gwllimrml)`: S=0.46, F=0.17, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_gwllimrml / close)`: S=0.47, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_gwllimrml, 5))`: S=0.79, F=0.71, T=23.6%, INFERIOR (TOP1000)
- `-rank(fnd2_a_gwllimrml)`: S=0.22, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_gwllimrml, 5))`: S=-0.63, F=-0.51, T=23.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_gwllimrml, 22)`: S=0.91, F=0.99, T=6.5%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_gwllimrml, 10)`: S=0.10, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_gwllimrml, 22))`: S=0.69, F=0.62, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_gwllimrml)`: S=0.22, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_gwllimrml / close)`: S=0.25, F=0.08, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.57 (strong), ret=+24.8%
  - 2020: S=0.46 (weak), ret=+10.1%
  - 2021: S=-0.33 (negative), ret=-5.5%
  - 2022: S=0.45 (weak), ret=+7.1%
  - 2023: S=1.48 (moderate), ret=+56.0%

## Risk & Drawdown
- Max drawdown: 25.49% over 1050 days (recovered)
- Annualized: return +18.9%, volatility 23.8% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +11.59, excess kurtosis +276.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.84, max 2.15, latest 1.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +46.26%; worst month: -8.62%
Positive months: 62%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.03
- Sideways: S=1.19
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * fnd2_a_gwllimrml / close)` S=0.25, F=0.08, INFERIOR
Direction gap: -0.66 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_gwllimrml)`: S=0.22, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_gwllimrml / close)`: S=0.25, F=0.08, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_gwllimrml, 5))`: S=-0.63, F=-0.51, T=23.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_gwllimrml, 5))` | TOP1000 | 0.79 | 0.71 | 25.5% | 80% | mixed |
| `rank(ts_delta(fnd2_a_gwllimrml, 5))` | TOP3000 | 0.75 | 0.53 | 24.4% | 100% | all-weather |
| `rank(ts_delta(fnd2_a_gwllimrml, 5))` | TOP200 | 0.35 | 0.24 | 28.2% | 40% | all-weather |
| `rank(fnd2_a_gwllimrml / close)` | TOP3000 | 0.47 | 0.19 | 8.5% | 60% | all-weather |
| `rank(fnd2_a_gwllimrml)` | TOP3000 | 0.46 | 0.17 | 7.8% | 60% | all-weather |
| `rank(ts_delta(fnd2_a_gwllimrml, 5))` | TOP500 | 0.15 | 0.05 | 31.8% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd2_propplteqflublgland: 0.276 (weakly positively correlated)
- anl4_bvps_number: 0.254 (weakly positively correlated)
- fnd6_tfvce: 0.212 (weakly positively correlated)
- fn_assets_fair_val_l3_a: 0.190 (weakly positively correlated)
- fn_amortization_of_intangible_assets_a: 0.177 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
