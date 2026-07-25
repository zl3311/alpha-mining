---
field: fnd6_xaccq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.98
best_fitness: 0.76
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0859
ann_vol: 0.0774
hit_rate: 0.5012
rolling_sharpe_min: -0.824
rolling_sharpe_max: 2.714
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.52
---
# fnd6_xaccq (fundamental6)

*Accrued Expenses*

## Signal Profile
- `rank(fnd6_xaccq)`: S=0.82, F=0.70, T=4.1%, INFERIOR (TOP3000)
- `rank(fnd6_xaccq / close)`: S=0.98, F=0.76, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xaccq, 5))`: S=0.15, F=0.03, T=40.8%, INFERIOR (TOP3000)
- `-rank(fnd6_xaccq)`: S=-0.51, F=-0.38, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xaccq, 5))`: S=0.46, F=0.18, T=42.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_xaccq, 22)`: S=0.33, F=0.12, T=41.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xaccq, 10)`: S=0.51, F=0.36, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xaccq, 22))`: S=0.36, F=0.13, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xaccq)`: S=-0.39, F=-0.26, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xaccq / close)`: S=-0.55, F=-0.39, T=6.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.97, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.8%
  - 2020: S=0.83 (moderate), ret=+7.0%
  - 2021: S=1.95 (strong), ret=+18.8%
  - 2022: S=0.83 (moderate), ret=+5.7%
  - 2023: S=0.68 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 8.59% over 476 days (recovered)
- Annualized: return +7.5%, volatility 7.7% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.32, excess kurtosis +2.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.82, max 2.71, latest 0.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.08%; worst month: -4.12%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.49
- Sideways: S=-0.09
- Bear: S=0.14

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_xaccq, 5))` S=0.46, F=0.18, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_xaccq)`: S=-0.39, F=-0.26, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xaccq / close)`: S=-0.55, F=-0.39, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xaccq, 5))`: S=0.46, F=0.18, T=42.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xaccq / close)` | TOP3000 | 0.97 | 0.76 | 8.6% | 100% | mixed |
| `rank(fnd6_xaccq)` | TOP3000 | 0.82 | 0.70 | 25.3% | 80% | bull-only |
| `rank(fnd6_xaccq / close)` | TOP1000 | 0.72 | 0.57 | 9.3% | 100% | bull-only |
| `rank(fnd6_xaccq / close)` | TOP500 | 0.55 | 0.39 | 18.1% | 60% | bull-only |
| `rank(fnd6_xaccq)` | TOP1000 | 0.50 | 0.38 | 31.1% | 60% | bull-only |
| `rank(fnd6_xaccq)` | TOP500 | 0.39 | 0.26 | 37.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_xaccq, 5))` | TOP3000 | 0.15 | 0.03 | 21.1% | 40% | bear-only |
| `rank(fnd6_xaccq)` | TOP200 | 0.05 | 0.02 | 46.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xacc: 0.958 (strongly positively correlated)
- fnd6_newqv1300_lcoq: 0.925 (strongly positively correlated)
- fnd6_xopr: 0.924 (strongly positively correlated)
- liabilities_curr: 0.918 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.918 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.85 | +0.67 | -0.70 | yes |
| rp_ess_revenue | news18 | -0.30 | 1.54 | +0.57 | -0.65 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.26 | 1.42 | +0.45 | -0.92 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.14 | 1.46 | +0.49 | -0.46 | yes |
| anl4_rd_exp_flag | analyst4 | -0.18 | 1.54 | +0.52 | +0.12 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
