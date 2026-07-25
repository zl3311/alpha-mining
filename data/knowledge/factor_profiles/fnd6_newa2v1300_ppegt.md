---
field: fnd6_newa2v1300_ppegt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.03
best_fitness: 0.88
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0912
ann_vol: 0.0885
hit_rate: 0.4858
rolling_sharpe_min: -1.268
rolling_sharpe_max: 2.871
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.54
---
# fnd6_newa2v1300_ppegt (fundamental6)

*Property, Plant and Equipment - Total (Gross)*

## Signal Profile
- `rank(fnd6_newa2v1300_ppegt)`: S=0.72, F=0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_ppegt / close)`: S=1.03, F=0.88, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_ppegt, 5))`: S=0.46, F=0.20, T=41.4%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_ppegt)`: S=-0.33, F=-0.20, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ppegt, 5))`: S=0.49, F=0.21, T=39.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_ppegt, 63)`: S=0.40, F=0.23, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_ppegt, 10)`: S=-0.06, F=-0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_ppegt, 22))`: S=0.91, F=0.67, T=19.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppegt)`: S=-0.72, F=-0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppegt / close)`: S=-1.03, F=-0.88, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-1.0%
  - 2020: S=0.27 (weak), ret=+2.6%
  - 2021: S=1.91 (strong), ret=+23.0%
  - 2022: S=1.73 (strong), ret=+15.9%
  - 2023: S=0.74 (moderate), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 9.12% over 426 days (recovered)
- Annualized: return +9.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.52, excess kurtosis +3.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 2.87, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +10.65%; worst month: -3.75%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.18
- Sideways: S=0.20
- Bear: S=-1.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_ppegt, 5))` S=0.49, F=0.21, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_ppegt)`: S=-0.72, F=-0.62, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_ppegt / close)`: S=-1.03, F=-0.88, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_ppegt, 5))`: S=0.49, F=0.21, T=39.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_ppegt / close)` | TOP3000 | 1.02 | 0.88 | 9.1% | 80% | bull-only |
| `rank(fnd6_newa2v1300_ppegt)` | TOP3000 | 0.72 | 0.62 | 32.5% | 80% | bull-only |
| `rank(fnd6_newa2v1300_ppegt / close)` | TOP1000 | 0.48 | 0.31 | 13.6% | 40% | bull-only |
| `rank(fnd6_newa2v1300_ppegt)` | TOP1000 | 0.32 | 0.20 | 36.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_ppegt, 5))` | TOP1000 | 0.46 | 0.20 | 34.2% | 60% | mixed |
| `rank(fnd6_newa2v1300_ppegt / close)` | TOP500 | 0.24 | 0.12 | 30.6% | 40% | bull-only |
| `rank(fnd6_newa2v1300_ppegt)` | TOP500 | 0.09 | 0.03 | 52.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ppeveb: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.985 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.982 (strongly positively correlated)
- fnd6_mfma1_dp: 0.982 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.973 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.90 | +0.72 | -0.61 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.74 | +0.72 | -0.34 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.69 | +0.67 | -0.70 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.58 | +0.56 | -0.66 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.55 | +0.53 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
