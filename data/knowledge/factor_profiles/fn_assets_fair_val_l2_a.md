---
field: fn_assets_fair_val_l2_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.12
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0556
ann_vol: 0.0379
hit_rate: 0.5101
rolling_sharpe_min: -0.417
rolling_sharpe_max: 2.251
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 21
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.92
---
# fn_assets_fair_val_l2_a (fundamental2)

*Asset Fair Value, Recurring, Level 2*

## Signal Profile
- `rank(fn_assets_fair_val_l2_a)`: S=0.83, F=0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_assets_fair_val_l2_a / close)`: S=1.12, F=0.65, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_assets_fair_val_l2_a, 5))`: S=0.77, F=0.49, T=31.9%, INFERIOR (TOP1000)
- `-rank(fn_assets_fair_val_l2_a)`: S=0.11, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l2_a, 5))`: S=-0.20, F=-0.07, T=30.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_assets_fair_val_l2_a, 22)`: S=0.63, F=0.54, T=14.3%, INFERIOR (TOP3000)
- `ts_mean(fn_assets_fair_val_l2_a, 10)`: S=0.00, F=0.00, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_assets_fair_val_l2_a, 22))`: S=0.43, F=0.25, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_a)`: S=0.20, F=0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_a / close)`: S=0.14, F=0.04, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.93 (moderate), ret=+2.6%
  - 2020: S=0.99 (moderate), ret=+3.7%
  - 2021: S=0.36 (weak), ret=+1.5%
  - 2022: S=1.79 (strong), ret=+6.9%
  - 2023: S=1.55 (strong), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 5.56% over 336 days (recovered)
- Annualized: return +4.2%, volatility 3.8% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.20, excess kurtosis +2.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.42, max 2.25, latest 1.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +2.58%; worst month: -2.40%
Positive months: 75%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.56
- Sideways: S=1.10
- Bear: S=0.71

## Negated Direction
Best negated: `rank(-1 * fn_assets_fair_val_l2_a)` S=0.20, F=0.07, INFERIOR
Direction gap: -0.92 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_assets_fair_val_l2_a)`: S=0.20, F=0.07, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_assets_fair_val_l2_a / close)`: S=0.14, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_assets_fair_val_l2_a, 5))`: S=-0.20, F=-0.07, T=30.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_assets_fair_val_l2_a / close)` | TOP3000 | 1.12 | 0.65 | 5.6% | 100% | all-weather |
| `rank(ts_delta(fn_assets_fair_val_l2_a, 5))` | TOP1000 | 0.77 | 0.49 | 25.8% | 100% | bull-only |
| `rank(fn_assets_fair_val_l2_a)` | TOP3000 | 0.84 | 0.44 | 11.8% | 80% | bull-only |
| `rank(ts_delta(fn_assets_fair_val_l2_a, 5))` | TOP3000 | 0.56 | 0.28 | 25.9% | 80% | mixed |
| `rank(ts_delta(fn_assets_fair_val_l2_a, 5))` | TOP500 | 0.27 | 0.10 | 37.2% | 80% | mixed |
| `rank(ts_delta(fn_assets_fair_val_l2_a, 5))` | TOP200 | 0.10 | 0.02 | 24.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_l2_q: 0.819 (strongly positively correlated)
- fnd6_newa1v1300_aol2: 0.633 (moderately positively correlated)
- fnd6_newqv1300_aol2q: 0.576 (moderately positively correlated)
- fn_liab_fair_val_l2_a: 0.563 (moderately positively correlated)
- fnd2_unrgtxbnfinregfcrps: 0.562 (moderately positively correlated)

Redundancy cluster #21: 2 similar fields, mean |rho| 0.819 (representative: fn_assets_fair_val_l2_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.08 | 1.68 | +0.52 | -0.35 | yes |
| est_rd_expense | analyst4 | -0.08 | 1.57 | +0.46 | -0.77 | yes |
| fnd6_rank | fundamental6 | -0.06 | 1.65 | +0.49 | +0.05 | yes |
| fnd6_ivaco | fundamental_investment | -0.11 | 1.82 | +0.47 | -0.22 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.01 | 1.61 | +0.47 | +0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
