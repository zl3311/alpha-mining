---
field: fn_assets_fair_val_l3_a
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 1.03
best_fitness: 1.11
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2216
ann_vol: 0.2067
hit_rate: 0.5012
rolling_sharpe_min: -0.468
rolling_sharpe_max: 2.549
top_merge_partner: fnd6_mrcta
negated_best_sharpe: 0.31
negated_best_template: neg_rank_level
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.72
---
# fn_assets_fair_val_l3_a (fundamental2)

*Asset Fair Value, Recurring, Level 3*

## Signal Profile
- `rank(fn_assets_fair_val_l3_a)`: S=0.19, F=0.04, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_l3_a / close)`: S=0.21, F=0.05, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_l3_a, 5))`: S=1.02, F=0.90, T=26.9%, INFERIOR (TOP1000)
- `-rank(fn_assets_fair_val_l3_a)`: S=0.11, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l3_a, 5))`: S=-0.05, F=-0.01, T=14.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_l3_a, 22)`: S=0.40, F=0.25, T=9.1%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l3_a, 10)`: S=0.63, F=0.37, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l3_a, 22))`: S=1.03, F=1.11, T=16.6%, AVERAGE (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_a)`: S=0.31, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_a / close)`: S=0.31, F=0.14, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+3.5%
  - 2020: S=1.38 (moderate), ret=+28.3%
  - 2021: S=0.36 (weak), ret=+8.0%
  - 2022: S=0.55 (moderate), ret=+9.6%
  - 2023: S=2.39 (strong), ret=+54.1%

## Risk & Drawdown
- Max drawdown: 22.16% over 52 days (recovered)
- Annualized: return +21.1%, volatility 20.7% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +1.80, excess kurtosis +16.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.47, max 2.55, latest 2.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +23.60%; worst month: -11.77%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.02
- Sideways: S=1.08
- Bear: S=-0.47

## Negated Direction
Best negated: `rank(-1 * fn_assets_fair_val_l3_a)` S=0.31, F=0.14, INFERIOR
Direction gap: -0.72 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l3_a)`: S=0.31, F=0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l3_a / close)`: S=0.31, F=0.14, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l3_a, 5))`: S=-0.05, F=-0.01, T=14.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_assets_fair_val_l3_a, 5))` | TOP1000 | 1.02 | 0.90 | 22.2% | 100% | mixed |
| `rank(ts_delta(fn_assets_fair_val_l3_a, 5))` | TOP500 | 0.81 | 0.70 | 20.7% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l3_a, 5))` | TOP200 | 0.47 | 0.33 | 20.8% | 60% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l3_a, 5))` | TOP3000 | 0.26 | 0.11 | 39.4% | 80% | mixed |
| `rank(fn_assets_fair_val_l3_a / close)` | TOP3000 | 0.23 | 0.05 | 8.3% | 40% | mixed |
| `rank(fn_assets_fair_val_l3_a)` | TOP3000 | 0.21 | 0.04 | 8.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_gwllimrml: 0.190 (weakly positively correlated)
- pcr_oi_30: 0.188 (weakly positively correlated)
- pcr_oi_1080: 0.188 (weakly positively correlated)
- pcr_oi_720: 0.185 (weakly positively correlated)
- pcr_oi_all: 0.183 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_mrcta | fundamental6 | -0.11 | 1.48 | +0.45 | -0.89 | yes |
| fnd6_optosby | fundamental6 | +0.02 | 1.43 | +0.41 | -0.82 | yes |
| fnd6_ivst | fundamental6 | -0.07 | 1.41 | +0.38 | -0.90 | yes |
| fnd6_mrc1 | fundamental6 | -0.03 | 1.65 | +0.37 | -0.94 | yes |
| fnd6_cisecgl | fundamental6 | -0.04 | 1.45 | +0.43 | -0.23 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
