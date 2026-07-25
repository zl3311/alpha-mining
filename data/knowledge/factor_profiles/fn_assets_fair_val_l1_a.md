---
field: fn_assets_fair_val_l1_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.5
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.2763
ann_vol: 0.1691
hit_rate: 0.5206
rolling_sharpe_min: -1.413
rolling_sharpe_max: 2.226
negated_best_sharpe: 0.04
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.74
---
# fn_assets_fair_val_l1_a (fundamental2)

*Asset Fair Value, Recurring, Level 1*

## Signal Profile
- `rank(fn_assets_fair_val_l1_a)`: S=0.11, F=0.02, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_l1_a / close)`: S=0.14, F=0.05, T=1.9%, INFERIOR (TOP200)
- `rank(ts_delta(fn_assets_fair_val_l1_a, 5))`: S=0.78, F=0.50, T=31.8%, INFERIOR (TOP1000)
- `-rank(fn_assets_fair_val_l1_a)`: S=0.04, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l1_a, 5))`: S=-0.65, F=-0.38, T=32.0%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_l1_a, 22)`: S=-0.07, F=-0.02, T=15.4%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l1_a, 10)`: S=0.10, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l1_a, 22))`: S=0.50, F=0.34, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_a)`: S=0.04, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_a / close)`: S=0.06, F=0.01, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.92 (moderate), ret=+12.8%
  - 2020: S=0.10 (weak), ret=+1.7%
  - 2021: S=1.28 (moderate), ret=+22.3%
  - 2022: S=0.42 (weak), ret=+7.6%
  - 2023: S=1.14 (moderate), ret=+19.1%

## Risk & Drawdown
- Max drawdown: 27.63% over 654 days (recovered)
- Annualized: return +13.0%, volatility 16.9% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.51, excess kurtosis +4.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 2.23, latest 1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +13.38%; worst month: -8.47%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.22
- Sideways: S=0.74
- Bear: S=-0.76

## Negated Direction
Best negated: `-rank(fn_assets_fair_val_l1_a)` S=0.04, F=0.01, INFERIOR
Direction gap: -0.74 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l1_a)`: S=0.04, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l1_a / close)`: S=0.06, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l1_a, 5))`: S=-0.65, F=-0.38, T=32.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_assets_fair_val_l1_a, 5))` | TOP1000 | 0.77 | 0.50 | 27.6% | 100% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l1_a, 5))` | TOP500 | 0.58 | 0.36 | 27.6% | 80% | bull-only |
| `rank(fn_assets_fair_val_l1_a / close)` | TOP200 | 0.16 | 0.05 | 25.4% | 60% | bull-only |
| `rank(fn_assets_fair_val_l1_a)` | TOP200 | 0.11 | 0.02 | 25.6% | 60% | bull-only |
| `rank(fn_assets_fair_val_l1_a)` | TOP3000 | 0.12 | 0.02 | 12.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_a: 0.375 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinytwo: 0.180 (weakly positively correlated)
- fnd6_txtubpospinc: 0.141 (weakly positively correlated)
- fnd6_newa2v1300_txp: 0.137 (weakly positively correlated)
- fnd6_newa2v1300_txdb: 0.137 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
