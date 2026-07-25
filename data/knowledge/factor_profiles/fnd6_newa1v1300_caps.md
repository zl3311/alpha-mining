---
field: fnd6_newa1v1300_caps
dataset: fundamental6
best_template: rank_level
best_sharpe: 1.01
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0754
ann_vol: 0.0481
hit_rate: 0.519
rolling_sharpe_min: -0.921
rolling_sharpe_max: 2.754
top_merge_partner: net_profit_adjusted_min_guidance
redundancy_cluster: 17
negated_best_sharpe: 0.55
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.46
---
# fnd6_newa1v1300_caps (fundamental6)

*Capital Surplus/Share Premium Reserve*

## Signal Profile
- `rank(fnd6_newa1v1300_caps)`: S=1.01, F=0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_caps / close)`: S=0.42, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_caps, 5))`: S=0.32, F=0.14, T=35.2%, INFERIOR (TOP500)
- `-rank(fnd6_newa1v1300_caps)`: S=-0.21, F=-0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_caps, 5))`: S=0.55, F=0.24, T=35.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_caps, 22)`: S=0.45, F=0.28, T=27.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_caps, 10)`: S=0.16, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_caps, 22))`: S=-0.25, F=-0.10, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_caps)`: S=-1.01, F=-0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_caps / close)`: S=-0.42, F=-0.21, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.77 (moderate), ret=+2.4%
  - 2020: S=0.08 (weak), ret=+0.3%
  - 2021: S=1.35 (moderate), ret=+9.4%
  - 2022: S=1.59 (strong), ret=+7.7%
  - 2023: S=1.06 (moderate), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 7.54% over 157 days (recovered)
- Annualized: return +4.9%, volatility 4.8% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.22, excess kurtosis +2.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 2.75, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.11%; worst month: -1.82%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.58
- Sideways: S=1.41
- Bear: S=-1.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_caps, 5))` S=0.55, F=0.24, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_caps)`: S=-1.01, F=-0.63, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_caps / close)`: S=-0.42, F=-0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_caps, 5))`: S=0.55, F=0.24, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_caps)` | TOP3000 | 1.01 | 0.63 | 7.5% | 100% | bull-only |
| `rank(fnd6_newa1v1300_caps / close)` | TOP3000 | 0.42 | 0.21 | 16.9% | 80% | mixed |
| `rank(fnd6_newa1v1300_caps / close)` | TOP200 | 0.32 | 0.15 | 16.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_caps, 5))` | TOP500 | 0.33 | 0.14 | 38.6% | 80% | mixed |
| `rank(fnd6_newa1v1300_caps)` | TOP1000 | 0.20 | 0.07 | 15.6% | 60% | bull-only |
| `rank(fnd6_newa1v1300_caps / close)` | TOP500 | 0.21 | 0.06 | 14.2% | 40% | bull-only |
| `rank(fnd6_newa1v1300_caps / close)` | TOP1000 | 0.17 | 0.05 | 10.4% | 80% | mixed |
| `rank(fnd6_newa1v1300_caps)` | TOP200 | 0.10 | 0.03 | 26.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_capsq: 0.962 (strongly positively correlated)
- fnd6_fopox: 0.853 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.787 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.785 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.784 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| net_profit_adjusted_min_guidance | analyst4 | -0.21 | 1.46 | +0.45 | -0.87 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.20 | 1.50 | +0.49 | -0.14 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.17 | 1.47 | +0.47 | -0.41 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.02 | 1.41 | +0.40 | -0.88 | yes |
| anl4_epsr_flag | analyst4 | -0.17 | 1.61 | +0.43 | -0.55 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
