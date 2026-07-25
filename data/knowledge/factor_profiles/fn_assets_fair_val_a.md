---
field: fn_assets_fair_val_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.39
best_fitness: 1.3
best_universe: TOP500
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 12
max_drawdown: 0.2214
ann_vol: 0.1903
hit_rate: 0.5093
rolling_sharpe_min: -0.778
rolling_sharpe_max: 2.671
top_merge_partner: news_mins_3_pct_dn
negated_best_sharpe: -0.18
negated_best_template: rank_neg_delta
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -1.57
---
# fn_assets_fair_val_a (fundamental2)

*Asset Fair Value, Recurring, Total*

## Signal Profile
- `rank(fn_assets_fair_val_a)`: S=0.54, F=0.25, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_a / close)`: S=0.50, F=0.24, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_a, 5))`: S=1.39, F=1.30, T=30.5%, AVERAGE (TOP500)
- `-rank(fn_assets_fair_val_a)`: S=-0.27, F=-0.10, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_a, 5))`: S=-0.18, F=-0.05, T=32.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_a, 22)`: S=0.41, F=0.28, T=16.1%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_a, 10)`: S=0.51, F=0.27, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_a, 22))`: S=0.04, F=0.01, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_a)`: S=-0.54, F=-0.25, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_a / close)`: S=-0.50, F=-0.24, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 25F/1P
- LOW_SHARPE: 25F/1P
- LOW_SUB_UNIVERSE_SHARPE: 6F/17P
- LOW_TURNOVER: 3F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.40, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+17.8%
  - 2020: S=0.61 (moderate), ret=+10.8%
  - 2021: S=1.47 (moderate), ret=+32.9%
  - 2022: S=1.74 (strong), ret=+35.6%
  - 2023: S=2.31 (strong), ret=+33.1%

## Risk & Drawdown
- Max drawdown: 22.14% over 215 days (recovered)
- Annualized: return +26.6%, volatility 19.0% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.85, excess kurtosis +6.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.78, max 2.67, latest 2.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +22.91%; worst month: -11.19%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.13
- Sideways: S=1.06
- Bear: S=0.84

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_assets_fair_val_a, 5))` S=-0.18, F=-0.05, INFERIOR
Direction gap: -1.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_a)`: S=-0.54, F=-0.25, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_a / close)`: S=-0.50, F=-0.24, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_a, 5))`: S=-0.18, F=-0.05, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_assets_fair_val_a, 5))` | TOP500 | 1.40 | 1.30 | 22.1% | 100% | all-weather |
| `rank(ts_delta(fn_assets_fair_val_a, 5))` | TOP1000 | 0.94 | 0.65 | 24.9% | 100% | mixed |
| `rank(ts_delta(fn_assets_fair_val_a, 5))` | TOP200 | 0.42 | 0.25 | 35.6% | 80% | mixed |
| `rank(fn_assets_fair_val_a)` | TOP3000 | 0.56 | 0.25 | 14.0% | 80% | bull-only |
| `rank(fn_assets_fair_val_a / close)` | TOP3000 | 0.50 | 0.24 | 8.1% | 80% | mixed |
| `rank(fn_assets_fair_val_a / close)` | TOP500 | 0.40 | 0.19 | 10.0% | 80% | mixed |
| `rank(fn_assets_fair_val_a / close)` | TOP1000 | 0.30 | 0.12 | 8.7% | 80% | mixed |
| `rank(fn_assets_fair_val_a)` | TOP1000 | 0.27 | 0.10 | 13.8% | 80% | bull-only |
| `rank(fn_assets_fair_val_a)` | TOP500 | 0.26 | 0.10 | 18.6% | 60% | bull-only |
| `rank(fn_assets_fair_val_a / close)` | TOP200 | 0.22 | 0.09 | 27.3% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_a, 5))` | TOP3000 | 0.14 | 0.04 | 57.4% | 60% | mixed |
| `rank(fn_assets_fair_val_a)` | TOP200 | 0.10 | 0.03 | 29.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_l1_a: 0.375 (weakly positively correlated)
- min_free_cash_flow_per_share_guidance: 0.206 (weakly positively correlated)
- free_cash_flow_per_share_max_guidance: 0.206 (weakly positively correlated)
- fnd6_prchq: -0.197 (weakly negatively correlated)
- fnd2_a_unrgtxbnfitxpenlintacd: 0.181 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_3_pct_dn | news12 | -0.02 | 1.95 | +0.55 | -0.92 | yes |
| news_mins_4_pct_dn | news12 | -0.03 | 1.94 | +0.54 | -0.86 | yes |
| anl4_ptp_flag | analyst_revision | -0.00 | 2.00 | +0.56 | -0.48 | yes |
| fnd6_mrc1 | fundamental6 | -0.02 | 1.91 | +0.51 | -0.63 | yes |
| fnd6_mrct | fundamental6 | +0.03 | 2.05 | +0.52 | -0.38 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
