---
field: fnd6_txndba
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0939
ann_vol: 0.0833
hit_rate: 0.4834
rolling_sharpe_min: -1.202
rolling_sharpe_max: 2.809
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_txndba (fundamental6)

*Net Deferred Tax Asset*

## Signal Profile
- `rank(fnd6_txndba)`: S=0.70, F=0.54, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txndba / close)`: S=0.93, F=0.73, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txndba, 5))`: S=0.56, F=0.28, T=41.3%, INFERIOR (TOP1000)
- `-rank(fnd6_txndba)`: S=-0.33, F=-0.19, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndba, 5))`: S=0.44, F=0.22, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txndba, 22)`: S=0.33, F=0.17, T=25.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txndba, 10)`: S=0.19, F=0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txndba, 22))`: S=-0.04, F=-0.01, T=19.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndba)`: S=-0.15, F=-0.06, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndba / close)`: S=-0.33, F=-0.19, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.47 (negative), ret=-2.1%
  - 2020: S=0.32 (weak), ret=+2.7%
  - 2021: S=1.69 (strong), ret=+20.6%
  - 2022: S=1.58 (strong), ret=+13.5%
  - 2023: S=0.63 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 9.39% over 269 days (recovered)
- Annualized: return +7.7%, volatility 8.3% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.43, excess kurtosis +3.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.81, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.02%; worst month: -2.86%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.99
- Sideways: S=0.19
- Bear: S=-1.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txndba, 5))` S=0.44, F=0.22, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txndba)`: S=-0.15, F=-0.06, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txndba / close)`: S=-0.33, F=-0.19, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txndba, 5))`: S=0.44, F=0.22, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txndba / close)` | TOP3000 | 0.92 | 0.73 | 9.4% | 80% | bull-only |
| `rank(fnd6_txndba)` | TOP3000 | 0.69 | 0.54 | 26.8% | 80% | bull-only |
| `rank(fnd6_txndba / close)` | TOP1000 | 0.54 | 0.37 | 17.3% | 40% | bull-only |
| `rank(ts_delta(fnd6_txndba, 5))` | TOP1000 | 0.56 | 0.28 | 28.5% | 100% | mixed |
| `rank(fnd6_txndba)` | TOP1000 | 0.32 | 0.19 | 36.2% | 40% | bull-only |
| `rank(fnd6_txndba / close)` | TOP500 | 0.32 | 0.19 | 35.3% | 40% | bull-only |
| `rank(fnd6_txndba)` | TOP500 | 0.14 | 0.06 | 53.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txndbl: 0.986 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.950 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.946 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.945 (strongly positively correlated)
- debt_lt: 0.945 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.36 | 1.71 | +0.69 | -0.23 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.56 | +0.64 | -0.61 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.80 | +0.62 | -0.53 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.27 | 1.54 | +0.60 | -0.55 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.43 | +0.51 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
