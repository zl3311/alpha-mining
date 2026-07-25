---
field: anl4_gric_std
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.85
best_fitness: 0.85
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1188
ann_vol: 0.0777
hit_rate: 0.5271
rolling_sharpe_min: -1.025
rolling_sharpe_max: 2.784
top_merge_partner: parkinson_volatility_120
redundancy_cluster: 32
negated_best_sharpe: 0.04
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.81
---
# anl4_gric_std (analyst4)

*Gross income - std of estimations*

## Signal Profile
- `rank(anl4_gric_std)`: S=0.86, F=0.63, T=4.4%, INFERIOR (TOP3000)
- `rank(anl4_gric_std / close)`: S=0.60, F=0.46, T=6.4%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_gric_std, 5))`: S=0.15, F=0.02, T=39.2%, INFERIOR (TOP3000)
- `-rank(anl4_gric_std)`: S=-0.69, F=-0.49, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_std, 5))`: S=0.04, F=0.00, T=39.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_gric_std, 22)`: S=0.01, F=0.00, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_gric_std, 10)`: S=0.85, F=0.85, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_gric_std, 22))`: S=-0.14, F=-0.03, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_std)`: S=-0.59, F=-0.41, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_std / close)`: S=-0.55, F=-0.36, T=5.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.86, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.10 (negative), ret=-0.5%
  - 2020: S=-0.18 (negative), ret=-1.2%
  - 2021: S=1.44 (moderate), ret=+14.6%
  - 2022: S=1.63 (strong), ret=+14.8%
  - 2023: S=0.76 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 11.88% over 313 days (recovered)
- Annualized: return +6.7%, volatility 7.8% (fraction of booksize)
- Hit rate: 52.7% positive days
- Tail shape: skew -0.05, excess kurtosis +0.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 2.78, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.18%; worst month: -4.60%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.16
- Sideways: S=1.26
- Bear: S=-2.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_gric_std, 5))` S=0.04, F=0.00, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_gric_std)`: S=-0.59, F=-0.41, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_gric_std / close)`: S=-0.55, F=-0.36, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_gric_std, 5))`: S=0.04, F=0.00, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_gric_std)` | TOP3000 | 0.86 | 0.63 | 11.9% | 60% | bull-only |
| `rank(anl4_gric_std)` | TOP200 | 0.64 | 0.53 | 28.8% | 80% | bull-only |
| `rank(anl4_gric_std)` | TOP1000 | 0.68 | 0.49 | 14.3% | 80% | bull-only |
| `rank(anl4_gric_std / close)` | TOP200 | 0.61 | 0.46 | 24.8% | 80% | bull-only |
| `rank(anl4_gric_std / close)` | TOP1000 | 0.63 | 0.43 | 11.3% | 80% | mixed |
| `rank(anl4_gric_std)` | TOP500 | 0.59 | 0.41 | 18.3% | 80% | bull-only |
| `rank(anl4_gric_std / close)` | TOP3000 | 0.62 | 0.38 | 11.9% | 80% | mixed |
| `rank(anl4_gric_std / close)` | TOP500 | 0.55 | 0.36 | 12.8% | 80% | bull-only |
| `rank(ts_delta(anl4_gric_std, 5))` | TOP3000 | 0.14 | 0.02 | 12.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- median_sales_estimate: 0.880 (strongly positively correlated)
- highest_sales_estimate: 0.880 (strongly positively correlated)
- sales_estimate_average_annual: 0.880 (strongly positively correlated)
- lowest_sales_estimate: 0.876 (strongly positively correlated)
- fnd6_newqv1300_acoq: 0.872 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_120 | option8 | -0.28 | 1.46 | +0.56 | -0.25 | yes |
| fnd6_txtubadjust | fundamental6 | -0.17 | 1.32 | +0.47 | -0.85 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.35 | 1.62 | +0.62 | -0.60 | no |
| sharesout | pv1 | -0.18 | 1.46 | +0.43 | -0.72 | yes |
| rp_ess_revenue | news18 | -0.13 | 1.32 | +0.43 | -0.73 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
