---
field: capex
dataset: fundamental6
cluster: fundamental6_cashflow
coverage: 0.5
community_alphas: 27541
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0823
ann_vol: 0.0726
hit_rate: 0.4842
rolling_sharpe_min: -1.261
rolling_sharpe_max: 2.688
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.47
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.36
---
# capex (fundamental6)

*Capital Expenditures*

## Signal Profile
- `rank(capex)`: S=0.62, F=0.43, T=1.2%, INFERIOR (TOP3000)
- `rank(capex / close)`: S=0.83, F=0.58, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(capex, 5))`: S=0.22, F=0.08, T=32.4%, INFERIOR (TOP200)
- `ts_decay_linear(rank(capex), 5)`: S=0.62, F=0.43, T=1.2%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(capex), ts_std_dev(returns,20)<0.01)`: S=0.56, F=0.36, T=2.1%, INFERIOR (TOP3000)
- `-rank(capex)`: S=-0.31, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capex, 5))`: S=0.47, F=0.23, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(capex, 63)`: S=0.44, F=0.24, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(capex, 10)`: S=0.19, F=0.08, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(capex, 22))`: S=-0.13, F=-0.03, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * capex)`: S=-0.15, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * capex / close)`: S=-0.41, F=-0.23, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/24P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.46 (negative), ret=-2.1%
  - 2020: S=0.76 (moderate), ret=+5.9%
  - 2021: S=1.73 (strong), ret=+16.7%
  - 2022: S=0.69 (moderate), ret=+4.7%
  - 2023: S=0.78 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 8.23% over 406 days (recovered)
- Annualized: return +6.0%, volatility 7.3% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.56, excess kurtosis +2.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.69, latest 0.86

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.45%; worst month: -3.32%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.58
- Sideways: S=0.25
- Bear: S=-0.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(capex, 5))` S=0.47, F=0.23, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * capex)`: S=-0.15, F=-0.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * capex / close)`: S=-0.41, F=-0.23, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capex, 5))`: S=0.47, F=0.23, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(capex / close)` | TOP3000 | 0.83 | 0.58 | 8.2% | 80% | bull-only |
| `rank(capex)` | TOP3000 | 0.62 | 0.43 | 23.9% | 80% | bull-only |
| `ts_decay_linear(rank(capex), 5)` | TOP3000 | 0.62 | 0.43 | 24.0% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(capex), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.55 | 0.36 | 23.5% | 60% | bull-only |
| `rank(capex / close)` | TOP1000 | 0.43 | 0.24 | 9.9% | 60% | bull-only |
| `rank(capex / close)` | TOP500 | 0.41 | 0.23 | 16.1% | 60% | bull-only |
| `rank(capex)` | TOP1000 | 0.30 | 0.16 | 27.5% | 60% | bull-only |
| `rank(ts_delta(capex, 5))` | TOP200 | 0.21 | 0.08 | 42.9% | 60% | mixed |
| `rank(capex)` | TOP500 | 0.14 | 0.06 | 36.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_capx: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_capx: 1.000 (strongly positively correlated)
- fnd6_capxv: 0.997 (strongly positively correlated)
- ppent: 0.970 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.970 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.31 | 1.44 | +0.55 | -0.48 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.72 | +0.55 | -0.45 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.24 | 1.29 | +0.46 | -0.97 | yes |
| min_gross_income_guidance | analyst4 | -0.16 | 1.29 | +0.42 | -0.47 | yes |
| max_gross_income_guidance | analyst4 | -0.15 | 1.30 | +0.41 | -0.48 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
