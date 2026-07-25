---
field: fnd6_mfma2_revt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.02
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.101
ann_vol: 0.0885
hit_rate: 0.5053
rolling_sharpe_min: -1.155
rolling_sharpe_max: 2.634
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.16
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.86
---
# fnd6_mfma2_revt (fundamental6)

*Revenue - Total*

## Signal Profile
- `rank(fnd6_mfma2_revt)`: S=0.66, F=0.53, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_mfma2_revt / close)`: S=1.02, F=0.87, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma2_revt, 5))`: S=0.43, F=0.22, T=33.6%, INFERIOR (TOP200)
- `-rank(fnd6_mfma2_revt)`: S=-0.34, F=-0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_revt, 5))`: S=-0.40, F=-0.20, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma2_revt, 63)`: S=0.03, F=0.00, T=20.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma2_revt, 10)`: S=0.12, F=0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma2_revt, 22))`: S=0.09, F=0.02, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_revt)`: S=0.16, F=0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_revt / close)`: S=0.03, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.9%
  - 2020: S=0.13 (weak), ret=+1.3%
  - 2021: S=1.60 (strong), ret=+18.8%
  - 2022: S=1.91 (strong), ret=+17.9%
  - 2023: S=1.48 (moderate), ret=+7.0%

## Risk & Drawdown
- Max drawdown: 10.10% over 238 days (recovered)
- Annualized: return +9.0%, volatility 8.8% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.45, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.63, latest 1.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +10.10%; worst month: -3.64%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.43
- Sideways: S=0.41
- Bear: S=-1.45

## Negated Direction
Best negated: `rank(-1 * fnd6_mfma2_revt)` S=0.16, F=0.08, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma2_revt)`: S=0.16, F=0.08, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_revt / close)`: S=0.03, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_revt, 5))`: S=-0.40, F=-0.20, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma2_revt / close)` | TOP3000 | 1.02 | 0.87 | 10.1% | 80% | bull-only |
| `rank(fnd6_mfma2_revt)` | TOP3000 | 0.66 | 0.53 | 32.1% | 80% | bull-only |
| `rank(fnd6_mfma2_revt / close)` | TOP1000 | 0.61 | 0.45 | 14.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_revt, 5))` | TOP200 | 0.43 | 0.22 | 39.5% | 80% | mixed |
| `rank(fnd6_mfma2_revt)` | TOP1000 | 0.33 | 0.21 | 37.3% | 60% | bull-only |
| `rank(fnd6_mfma2_revt / close)` | TOP500 | 0.34 | 0.20 | 26.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_revt, 5))` | TOP500 | 0.23 | 0.08 | 61.7% | 40% | mixed |
| `rank(ts_delta(fnd6_mfma2_revt, 5))` | TOP1000 | 0.27 | 0.08 | 38.8% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma2_revt, 5))` | TOP3000 | 0.21 | 0.05 | 15.9% | 80% | weak |
| `rank(fnd6_mfma2_revt)` | TOP500 | 0.11 | 0.04 | 48.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_sale: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_revt: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.989 (strongly positively correlated)
- sales: 0.989 (strongly positively correlated)
- fnd6_cptnewqv1300_saleq: 0.989 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.35 | 1.78 | +0.75 | -0.42 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.90 | +0.72 | -0.33 | yes |
| rp_ess_revenue | news18 | -0.37 | 1.69 | +0.67 | -0.59 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.59 | +0.57 | -0.57 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.32 | 1.55 | +0.53 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
