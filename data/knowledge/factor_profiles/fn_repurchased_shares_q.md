---
field: fn_repurchased_shares_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0432
ann_vol: 0.0313
hit_rate: 0.5126
rolling_sharpe_min: -0.887
rolling_sharpe_max: 2.845
top_merge_partner: rp_nip_credit_ratings
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.44
---
# fn_repurchased_shares_q (fundamental2)

*Number of shares that have been repurchased during the period.*

## Signal Profile
- `rank(fn_repurchased_shares_q)`: S=0.59, F=0.26, T=1.3%, INFERIOR (TOP3000)
- `rank(fn_repurchased_shares_q / close)`: S=0.83, F=0.38, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repurchased_shares_q, 5))`: S=0.61, F=0.31, T=36.0%, INFERIOR (TOP200)
- `-rank(fn_repurchased_shares_q)`: S=-0.19, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_q, 5))`: S=-0.09, F=-0.02, T=34.8%, INFERIOR (TOP3000)
- `ts_zscore(fn_repurchased_shares_q, 22)`: S=-0.24, F=-0.08, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fn_repurchased_shares_q, 10)`: S=-0.72, F=-0.55, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repurchased_shares_q, 22))`: S=-0.29, F=-0.09, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_q)`: S=0.28, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_q / close)`: S=0.39, F=0.16, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.1%
  - 2020: S=0.38 (weak), ret=+1.3%
  - 2021: S=2.12 (strong), ret=+7.1%
  - 2022: S=0.92 (moderate), ret=+2.9%
  - 2023: S=0.57 (moderate), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 4.32% over 596 days (not yet recovered, ongoing at window end)
- Annualized: return +2.6%, volatility 3.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.22, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 2.85, latest 0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +2.58%; worst month: -1.80%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.52
- Sideways: S=0.17
- Bear: S=-0.29

## Negated Direction
Best negated: `rank(-1 * fn_repurchased_shares_q / close)` S=0.39, F=0.16, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repurchased_shares_q)`: S=0.28, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_repurchased_shares_q / close)`: S=0.39, F=0.16, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repurchased_shares_q, 5))`: S=-0.09, F=-0.02, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repurchased_shares_q / close)` | TOP3000 | 0.84 | 0.38 | 4.3% | 100% | mixed |
| `rank(ts_delta(fn_repurchased_shares_q, 5))` | TOP200 | 0.61 | 0.31 | 14.5% | 80% | mixed |
| `rank(fn_repurchased_shares_q)` | TOP3000 | 0.59 | 0.26 | 7.4% | 80% | bull-only |
| `rank(ts_delta(fn_repurchased_shares_q, 5))` | TOP1000 | 0.38 | 0.12 | 13.5% | 80% | all-weather |
| `rank(fn_repurchased_shares_q)` | TOP1000 | 0.18 | 0.05 | 12.2% | 40% | bull-only |
| `rank(fn_repurchased_shares_q / close)` | TOP1000 | 0.19 | 0.05 | 7.9% | 40% | bull-only |
| `rank(ts_delta(fn_repurchased_shares_q, 5))` | TOP3000 | 0.24 | 0.05 | 16.9% | 60% | all-weather |
| `rank(ts_delta(fn_repurchased_shares_q, 5))` | TOP500 | 0.09 | 0.02 | 21.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_rvndm: 0.601 (moderately positively correlated)
- fn_intangible_assets_accum_amort_a: 0.595 (moderately positively correlated)
- fnd2_asdm: 0.593 (moderately positively correlated)
- fnd6_xpr: 0.591 (moderately positively correlated)
- fnd2_dfctrbplancstrg: 0.591 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_nip_credit_ratings | news18 | -0.05 | 1.28 | +0.32 | -0.77 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.16 | 1.55 | +0.39 | +0.52 | yes |
| rp_ess_revenue | news18 | -0.24 | 1.18 | +0.29 | -0.81 | yes |
| anl4_epsr_flag | analyst4 | -0.22 | 1.47 | +0.29 | -0.80 | yes |
| cashflow_per_share_minimum | analyst4 | +0.07 | 1.14 | +0.29 | -0.82 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
