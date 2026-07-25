---
field: fnd6_newa1v1300_lct
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0862
ann_vol: 0.0808
hit_rate: 0.4858
rolling_sharpe_min: -0.932
rolling_sharpe_max: 2.707
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.38
---
# fnd6_newa1v1300_lct (fundamental6)

*Current Liabilities - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_lct)`: S=0.67, F=0.54, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_lct / close)`: S=0.91, F=0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_lct, 5))`: S=0.36, F=0.16, T=33.9%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_lct)`: S=-0.34, F=-0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lct, 5))`: S=0.53, F=0.21, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_lct, 63)`: S=0.01, F=0.00, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_lct, 10)`: S=0.05, F=0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_lct, 22))`: S=0.66, F=0.41, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lct)`: S=-0.67, F=-0.54, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lct / close)`: S=-0.91, F=-0.70, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.91, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.4%
  - 2020: S=0.36 (weak), ret=+3.2%
  - 2021: S=1.71 (strong), ret=+17.5%
  - 2022: S=1.57 (strong), ret=+13.1%
  - 2023: S=0.47 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 8.62% over 484 days (recovered)
- Annualized: return +7.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.51, excess kurtosis +2.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 2.71, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.87%; worst month: -4.05%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.09
- Sideways: S=0.20
- Bear: S=-1.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_lct, 5))` S=0.53, F=0.21, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_lct)`: S=-0.67, F=-0.54, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lct / close)`: S=-0.91, F=-0.70, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lct, 5))`: S=0.53, F=0.21, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_lct / close)` | TOP3000 | 0.91 | 0.70 | 8.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lct)` | TOP3000 | 0.67 | 0.54 | 31.3% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lct / close)` | TOP1000 | 0.50 | 0.33 | 12.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lct)` | TOP1000 | 0.33 | 0.20 | 34.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_lct, 5))` | TOP200 | 0.35 | 0.16 | 47.1% | 40% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_lct, 5))` | TOP1000 | 0.38 | 0.15 | 40.1% | 60% | all-weather |
| `rank(fnd6_newa1v1300_lct / close)` | TOP500 | 0.21 | 0.09 | 24.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_lct, 5))` | TOP500 | 0.20 | 0.07 | 37.6% | 40% | mixed |
| `rank(fnd6_newa1v1300_lct)` | TOP500 | 0.06 | 0.02 | 51.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptmfmq_lctq: 0.989 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.989 (strongly positively correlated)
- liabilities_curr: 0.989 (strongly positively correlated)
- fnd6_newa1v1300_lco: 0.981 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.977 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.56 | +0.65 | -0.69 | yes |
| anl4_epsr_flag | analyst4 | -0.34 | 1.82 | +0.64 | -0.66 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.41 | +0.50 | -0.89 | yes |
| max_gross_income_guidance | analyst4 | -0.21 | 1.40 | +0.50 | -0.72 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.17 | 1.44 | +0.49 | -0.65 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
