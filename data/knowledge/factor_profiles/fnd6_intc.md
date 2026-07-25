---
field: fnd6_intc
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 1.32
best_fitness: 1.47
best_universe: TOP3000
grade: AVERAGE
submittability: needs_upgrade
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0778
ann_vol: 0.0456
hit_rate: 0.5206
rolling_sharpe_min: -1.069
rolling_sharpe_max: 2.691
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 36
negated_best_sharpe: 1.32
negated_best_template: neg_rank_value_norm
negated_best_fitness: 1.47
n_negated_sims: 10
direction_gap: 0.49
---
# fnd6_intc (fundamental6)

*Interest Capitalized*

## Signal Profile
- `rank(fnd6_intc)`: S=0.72, F=0.38, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_intc / close)`: S=0.83, F=0.45, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_intc, 5))`: S=0.21, F=0.09, T=19.4%, INFERIOR (TOP200)
- `-rank(fnd6_intc)`: S=-0.21, F=-0.07, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_intc, 5))`: S=-0.23, F=-0.10, T=19.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_intc, 63)`: S=-0.13, F=-0.07, T=13.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_intc, 10)`: S=0.20, F=0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_intc, 22))`: S=0.27, F=0.14, T=18.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_intc)`: S=1.29, F=1.41, T=3.4%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_intc / close)`: S=1.32, F=1.47, T=3.5%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 26F/6P
- LOW_SHARPE: 26F/6P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.81, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.41 (weak), ret=+1.2%
  - 2020: S=0.48 (weak), ret=+1.9%
  - 2021: S=1.64 (strong), ret=+8.6%
  - 2022: S=0.69 (moderate), ret=+4.1%
  - 2023: S=0.66 (moderate), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 7.78% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +3.7%, volatility 4.6% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.07, excess kurtosis +0.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 2.69, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +3.52%; worst month: -2.38%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.30
- Sideways: S=2.00
- Bear: S=-1.93

## Negated Direction
Best negated: `rank(-1 * fnd6_intc / close)` S=1.32, F=1.47, AVERAGE
Direction gap: +0.49 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_intc)`: S=1.29, F=1.41, T=3.4%, AVERAGE (TOP3000)
- `rank(-1 * fnd6_intc / close)`: S=1.32, F=1.47, T=3.5%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_intc, 5))`: S=-0.23, F=-0.10, T=19.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_intc / close)` | TOP3000 | 0.81 | 0.45 | 7.8% | 100% | bull-only |
| `rank(fnd6_intc)` | TOP3000 | 0.71 | 0.38 | 7.7% | 100% | bull-only |
| `rank(fnd6_intc / close)` | TOP1000 | 0.30 | 0.12 | 11.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_intc, 5))` | TOP200 | 0.21 | 0.09 | 27.5% | 40% | bull-only |
| `rank(fnd6_intc)` | TOP1000 | 0.21 | 0.07 | 12.1% | 40% | bull-only |
| `rank(ts_delta(fnd6_intc, 5))` | TOP500 | 0.13 | 0.04 | 29.5% | 40% | bull-only |
| `rank(ts_delta(fnd6_intc, 5))` | TOP1000 | 0.15 | 0.04 | 32.0% | 40% | mixed |

## Correlation Notes
Top correlates:
- est_ebitda: 0.766 (strongly positively correlated)
- est_cashflow_op: 0.760 (strongly positively correlated)
- anl4_medianepsbfam: 0.759 (strongly positively correlated)
- anl4_ebitda_mean: 0.759 (strongly positively correlated)
- fnd6_newa2v1300_txdb: 0.759 (strongly positively correlated)

Redundancy cluster #36: 4 similar fields, mean |rho| 0.734 (representative: anl4_fcf_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.30 | 1.43 | +0.51 | +0.39 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.35 | +0.41 | -0.68 | yes |
| news_open_vol | news12 | -0.14 | 1.30 | +0.38 | -0.94 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.27 | 1.23 | +0.42 | -0.52 | yes |
| rp_ess_revenue | news18 | -0.23 | 1.26 | +0.37 | -0.85 | yes |

## Actionability
Needs grade upgrade. Try decay_linear wrap, value normalization, or blend with complementary factor.
Untried templates: decay_linear, trade_when
