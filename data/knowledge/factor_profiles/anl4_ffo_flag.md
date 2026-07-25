---
field: anl4_ffo_flag
dataset: analyst4
best_template: rank_delta
best_sharpe: 1.35
best_fitness: 1.39
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2098
ann_vol: 0.1337
hit_rate: 0.5093
rolling_sharpe_min: -0.891
rolling_sharpe_max: 4.092
top_merge_partner: news_mins_3_pct_dn
negated_best_sharpe: 0.58
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.77
---
# anl4_ffo_flag (analyst4)

*Funds from Operation - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_ffo_flag)`: S=0.61, F=0.36, T=36.2%, INFERIOR (TOP200)
- `rank(anl4_ffo_flag / close)`: S=0.22, F=0.10, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_ffo_flag, 5))`: S=1.35, F=1.39, T=17.1%, AVERAGE (TOP3000)
- `-rank(anl4_ffo_flag)`: S=0.32, F=0.22, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ffo_flag, 5))`: S=0.46, F=0.29, T=4.5%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ffo_flag, 22)`: S=-0.26, F=-0.09, T=2.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_ffo_flag, 10)`: S=-0.38, F=-0.28, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ffo_flag, 22))`: S=-0.01, F=0.00, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ffo_flag)`: S=0.58, F=0.32, T=40.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ffo_flag / close)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/10P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.34, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.87 (moderate), ret=+14.2%
  - 2020: S=0.52 (moderate), ret=+7.6%
  - 2021: S=1.00 (moderate), ret=+13.8%
  - 2022: S=3.83 (strong), ret=+41.6%
  - 2023: S=1.29 (moderate), ret=+10.4%

## Risk & Drawdown
- Max drawdown: 20.98% over 378 days (recovered)
- Annualized: return +17.9%, volatility 13.4% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +2.84, excess kurtosis +37.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 4.09, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +13.52%; worst month: -5.67%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=3.05
- Sideways: S=0.85
- Bear: S=0.24

## Negated Direction
Best negated: `rank(-1 * anl4_ffo_flag)` S=0.58, F=0.32, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_ffo_flag)`: S=0.58, F=0.32, T=40.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ffo_flag / close)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ffo_flag, 5))`: S=0.46, F=0.29, T=4.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_ffo_flag, 5))` | TOP3000 | 1.34 | 1.39 | 21.0% | 100% | mixed |
| `rank(anl4_ffo_flag)` | TOP200 | 0.61 | 0.36 | 23.4% | 80% | bear-only |
| `rank(ts_delta(anl4_ffo_flag, 5))` | TOP500 | 0.51 | 0.34 | 32.0% | 60% | bull-only |
| `rank(anl4_ffo_flag)` | TOP3000 | 0.30 | 0.15 | 11.7% | 80% | bull-only |
| `rank(anl4_ffo_flag / close)` | TOP200 | 0.23 | 0.10 | 24.3% | 80% | mixed |
| `rank(ts_delta(anl4_ffo_flag, 5))` | TOP200 | 0.07 | 0.02 | 32.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_customized_eps_guidance: 0.462 (moderately positively correlated)
- max_total_goodwill_guidance: 0.462 (moderately positively correlated)
- min_share_buyback_guidance: 0.462 (moderately positively correlated)
- max_share_buyback_guidance: 0.462 (moderately positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.462 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_3_pct_dn | news12 | +0.02 | 1.89 | +0.52 | -0.58 | yes |
| anl4_rd_exp_flag | analyst4 | -0.18 | 1.85 | +0.51 | -0.63 | yes |
| news_mins_4_pct_dn | news12 | +0.00 | 1.84 | +0.50 | -0.52 | yes |
| implied_volatility_put_10 | option8 | -0.04 | 1.89 | +0.56 | +0.30 | yes |
| anl4_netprofit_flag | analyst4 | -0.04 | 1.88 | +0.54 | +0.83 | yes |

## Actionability
Cataloged as active factor but not yet in submitted book.
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
