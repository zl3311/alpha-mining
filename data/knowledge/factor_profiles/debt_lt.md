---
field: debt_lt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.2
best_fitness: 1.06
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0773
ann_vol: 0.0817
hit_rate: 0.5061
rolling_sharpe_min: -0.646
rolling_sharpe_max: 2.857
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.81
---
# debt_lt (fundamental6)

*Long-Term Debt - Total*

## Signal Profile
- `rank(debt_lt)`: S=0.88, F=0.74, T=1.6%, INFERIOR (TOP3000)
- `rank(debt_lt / close)`: S=1.20, F=1.06, T=1.9%, AVERAGE (TOP3000)
- `rank(ts_delta(debt_lt, 5))`: S=-0.27, F=-0.06, T=37.8%, INFERIOR (TOP1000)
- `ts_decay_linear(rank(debt_lt), 5)`: S=0.88, F=0.74, T=1.6%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(debt_lt), ts_std_dev(returns,20)<0.01)`: S=0.82, F=0.66, T=2.3%, INFERIOR (TOP3000)
- `-rank(debt_lt)`: S=-0.35, F=-0.20, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(debt_lt, 5))`: S=0.39, F=0.09, T=37.9%, INFERIOR (TOP3000)
- `-ts_zscore(debt_lt, 63)`: S=0.63, F=0.24, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(debt_lt, 10)`: S=0.29, F=0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(debt_lt, 22))`: S=0.08, F=0.01, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * debt_lt)`: S=-0.88, F=-0.74, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * debt_lt / close)`: S=-1.20, F=-1.06, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/31P
- LOW_FITNESS: 35F/2P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/21P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.20, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.97 (moderate), ret=+4.3%
  - 2020: S=0.80 (moderate), ret=+7.8%
  - 2021: S=1.75 (strong), ret=+19.2%
  - 2022: S=1.63 (strong), ret=+12.4%
  - 2023: S=0.88 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 7.73% over 90 days (recovered)
- Annualized: return +9.8%, volatility 8.2% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.50, excess kurtosis +3.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.65, max 2.86, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.98%; worst month: -2.92%
Positive months: 66%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.03
- Sideways: S=0.71
- Bear: S=-0.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(debt_lt, 5))` S=0.39, F=0.09, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * debt_lt)`: S=-0.88, F=-0.74, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * debt_lt / close)`: S=-1.20, F=-1.06, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(debt_lt, 5))`: S=0.39, F=0.09, T=37.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(debt_lt / close)` | TOP3000 | 1.20 | 1.06 | 7.7% | 100% | bull-only |
| `rank(debt_lt)` | TOP3000 | 0.87 | 0.74 | 20.7% | 80% | bull-only |
| `ts_decay_linear(rank(debt_lt), 5)` | TOP3000 | 0.88 | 0.74 | 20.7% | 80% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(debt_lt), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.81 | 0.66 | 20.8% | 80% | bull-only |
| `rank(debt_lt / close)` | TOP1000 | 0.62 | 0.44 | 13.0% | 80% | bull-only |
| `rank(debt_lt / close)` | TOP500 | 0.47 | 0.31 | 19.1% | 60% | bull-only |
| `rank(debt_lt)` | TOP1000 | 0.34 | 0.20 | 28.1% | 60% | bull-only |
| `rank(debt_lt)` | TOP500 | 0.20 | 0.10 | 41.7% | 60% | bull-only |
| `rank(debt_lt / close)` | TOP200 | 0.11 | 0.04 | 29.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_dlttq: 1.000 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 1.000 (strongly positively correlated)
- debt: 0.991 (strongly positively correlated)
- fnd6_newa1v1300_dltt: 0.990 (strongly positively correlated)
- fnd6_newqv1300_lltq: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 2.08 | +0.88 | -0.84 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.86 | +0.66 | -0.55 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.78 | +0.58 | -0.83 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.24 | 1.73 | +0.53 | -0.85 | yes |
| implied_volatility_mean_10 | option8 | -0.08 | 1.76 | +0.54 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
