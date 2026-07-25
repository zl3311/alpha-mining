---
field: fnd6_txndbl
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 1.06
best_fitness: 1.05
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0968
ann_vol: 0.0827
hit_rate: 0.4818
rolling_sharpe_min: -0.887
rolling_sharpe_max: 2.797
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.83
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_txndbl (fundamental6)

*Net Deferred Tax Liability*

## Signal Profile
- `rank(fnd6_txndbl)`: S=0.70, F=0.54, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txndbl / close)`: S=0.93, F=0.73, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txndbl, 5))`: S=-0.14, F=-0.03, T=41.4%, INFERIOR (TOP1000)
- `-rank(fnd6_txndbl)`: S=-0.24, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndbl, 5))`: S=0.83, F=0.46, T=41.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txndbl, 63)`: S=1.06, F=1.05, T=19.6%, AVERAGE (TOP3000)
- `ts_mean(fnd6_txndbl, 10)`: S=0.06, F=0.01, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txndbl, 22))`: S=0.12, F=0.03, T=19.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbl)`: S=-0.70, F=-0.54, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbl / close)`: S=-0.93, F=-0.73, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.22 (negative), ret=-0.9%
  - 2020: S=0.31 (weak), ret=+2.6%
  - 2021: S=1.67 (strong), ret=+20.1%
  - 2022: S=1.54 (strong), ret=+13.3%
  - 2023: S=0.51 (moderate), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 9.68% over 101 days (recovered)
- Annualized: return +7.6%, volatility 8.3% (fraction of booksize)
- Hit rate: 48.2% positive days
- Tail shape: skew +0.35, excess kurtosis +3.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 2.80, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.05%; worst month: -2.81%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.90
- Sideways: S=0.32
- Bear: S=-1.11

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txndbl, 5))` S=0.83, F=0.46, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txndbl)`: S=-0.70, F=-0.54, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndbl / close)`: S=-0.93, F=-0.73, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndbl, 5))`: S=0.83, F=0.46, T=41.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txndbl / close)` | TOP3000 | 0.92 | 0.73 | 9.7% | 80% | bull-only |
| `rank(fnd6_txndbl)` | TOP3000 | 0.69 | 0.54 | 26.4% | 80% | bull-only |
| `rank(fnd6_txndbl / close)` | TOP1000 | 0.40 | 0.25 | 20.2% | 40% | bull-only |
| `rank(fnd6_txndbl)` | TOP1000 | 0.24 | 0.12 | 37.3% | 60% | bull-only |
| `rank(fnd6_txndbl / close)` | TOP500 | 0.19 | 0.09 | 36.9% | 40% | bull-only |
| `rank(fnd6_txndbl)` | TOP500 | 0.08 | 0.02 | 52.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txndba: 0.986 (strongly positively correlated)
- fn_def_tax_liab_a: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.950 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.943 (strongly positively correlated)
- debt_lt: 0.943 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.38 | 1.73 | +0.70 | -0.29 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.57 | +0.65 | -0.67 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.79 | +0.61 | -0.62 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.55 | +0.61 | -0.62 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.44 | +0.52 | -0.91 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
