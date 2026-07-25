---
field: fnd6_ppeveb
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.12
best_fitness: 0.91
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0907
ann_vol: 0.0885
hit_rate: 0.4891
rolling_sharpe_min: -1.324
rolling_sharpe_max: 2.849
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.75
---
# fnd6_ppeveb (fundamental6)

*Property, Plant, and Equipment - Ending Balance (Schedule V)*

## Signal Profile
- `rank(fnd6_ppeveb)`: S=0.73, F=0.63, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_ppeveb / close)`: S=1.02, F=0.87, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ppeveb, 5))`: S=0.70, F=0.38, T=41.5%, INFERIOR (TOP1000)
- `-rank(fnd6_ppeveb)`: S=-0.34, F=-0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ppeveb, 5))`: S=0.37, F=0.14, T=40.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ppeveb, 63)`: S=0.33, F=0.17, T=21.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ppeveb, 10)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ppeveb, 22))`: S=1.12, F=0.91, T=19.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ppeveb)`: S=-0.73, F=-0.63, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ppeveb / close)`: S=-1.02, F=-0.87, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.21 (negative), ret=-1.1%
  - 2020: S=0.25 (weak), ret=+2.4%
  - 2021: S=1.89 (strong), ret=+22.9%
  - 2022: S=1.73 (strong), ret=+15.9%
  - 2023: S=0.77 (moderate), ret=+4.0%

## Risk & Drawdown
- Max drawdown: 9.07% over 426 days (recovered)
- Annualized: return +9.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +0.51, excess kurtosis +3.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.32, max 2.85, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +10.67%; worst month: -3.77%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.18
- Sideways: S=0.24
- Bear: S=-1.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ppeveb, 5))` S=0.37, F=0.14, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_ppeveb)`: S=-0.73, F=-0.63, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ppeveb / close)`: S=-1.02, F=-0.87, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ppeveb, 5))`: S=0.37, F=0.14, T=40.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ppeveb / close)` | TOP3000 | 1.02 | 0.87 | 9.1% | 80% | bull-only |
| `rank(fnd6_ppeveb)` | TOP3000 | 0.72 | 0.63 | 32.5% | 80% | bull-only |
| `rank(ts_delta(fnd6_ppeveb, 5))` | TOP1000 | 0.71 | 0.38 | 33.7% | 80% | mixed |
| `rank(fnd6_ppeveb / close)` | TOP1000 | 0.47 | 0.31 | 13.8% | 40% | bull-only |
| `rank(fnd6_ppeveb)` | TOP1000 | 0.33 | 0.21 | 36.9% | 40% | bull-only |
| `rank(fnd6_ppeveb / close)` | TOP500 | 0.24 | 0.12 | 30.5% | 40% | bull-only |
| `rank(fnd6_ppeveb)` | TOP500 | 0.09 | 0.03 | 52.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_ppegt: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.985 (strongly positively correlated)
- fnd6_newa1v1300_dp: 0.982 (strongly positively correlated)
- fnd6_mfma1_dp: 0.981 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.973 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.90 | +0.72 | -0.60 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.74 | +0.71 | -0.34 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.68 | +0.67 | -0.70 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.23 | 1.58 | +0.56 | -0.66 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.54 | +0.53 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
