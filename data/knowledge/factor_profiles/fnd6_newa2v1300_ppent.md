---
field: fnd6_newa2v1300_ppent
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.99
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0821
ann_vol: 0.0829
hit_rate: 0.4834
rolling_sharpe_min: -1.257
rolling_sharpe_max: 2.801
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.54
---
# fnd6_newa2v1300_ppent (fundamental6)

*Property, Plant and Equipment - Total (Net)*

## Signal Profile
- `rank(fnd6_newa2v1300_ppent)`: S=0.73, F=0.60, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_ppent / close)`: S=0.99, F=0.80, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_ppent, 5))`: S=-0.20, F=-0.06, T=34.2%, INFERIOR (TOP500)
- `-rank(fnd6_newa2v1300_ppent)`: S=-0.36, F=-0.22, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ppent, 5))`: S=0.45, F=0.16, T=36.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_ppent, 63)`: S=0.57, F=0.35, T=19.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_ppent, 10)`: S=0.07, F=0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_ppent, 22))`: S=0.05, F=0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppent)`: S=-0.73, F=-0.60, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppent / close)`: S=-0.99, F=-0.80, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.99, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.33 (negative), ret=-1.6%
  - 2020: S=0.51 (moderate), ret=+4.6%
  - 2021: S=1.83 (strong), ret=+20.6%
  - 2022: S=1.36 (moderate), ret=+11.1%
  - 2023: S=0.94 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 8.21% over 422 days (recovered)
- Annualized: return +8.2%, volatility 8.3% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.57, excess kurtosis +2.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.80, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.83%; worst month: -3.69%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.98
- Sideways: S=0.31
- Bear: S=-0.90

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_ppent, 5))` S=0.45, F=0.16, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_ppent)`: S=-0.73, F=-0.60, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppent / close)`: S=-0.99, F=-0.80, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ppent, 5))`: S=0.45, F=0.16, T=36.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_ppent / close)` | TOP3000 | 0.99 | 0.80 | 8.2% | 80% | bull-only |
| `rank(fnd6_newa2v1300_ppent)` | TOP3000 | 0.72 | 0.60 | 28.6% | 80% | bull-only |
| `rank(fnd6_newa2v1300_ppent / close)` | TOP1000 | 0.54 | 0.37 | 12.0% | 40% | bull-only |
| `rank(fnd6_newa2v1300_ppent)` | TOP1000 | 0.35 | 0.22 | 32.3% | 60% | bull-only |
| `rank(fnd6_newa2v1300_ppent / close)` | TOP500 | 0.32 | 0.18 | 24.2% | 40% | bull-only |
| `rank(fnd6_newa2v1300_ppent)` | TOP500 | 0.13 | 0.05 | 45.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ppentq: 0.986 (strongly positively correlated)
- ppent: 0.986 (strongly positively correlated)
- fnd6_ppeveb: 0.985 (strongly positively correlated)
- fnd6_newa2v1300_ppegt: 0.985 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.978 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 1.88 | +0.70 | -0.51 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.63 | +0.64 | -0.62 | yes |
| anl4_rd_exp_flag | analyst4 | -0.27 | 1.65 | +0.62 | -0.12 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.53 | +0.54 | -0.51 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.48 | +0.49 | -0.98 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
