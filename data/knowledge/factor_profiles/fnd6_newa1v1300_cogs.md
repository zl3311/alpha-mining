---
field: fnd6_newa1v1300_cogs
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.19
best_fitness: 1.03
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0861
ann_vol: 0.0786
hit_rate: 0.4931
rolling_sharpe_min: -1.179
rolling_sharpe_max: 2.815
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.62
---
# fnd6_newa1v1300_cogs (fundamental6)

*Cost of Goods Sold*

## Signal Profile
- `rank(fnd6_newa1v1300_cogs)`: S=0.80, F=0.67, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_cogs / close)`: S=1.19, F=1.03, T=1.4%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_cogs, 5))`: S=-0.15, F=-0.03, T=35.9%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_cogs)`: S=-0.41, F=-0.26, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cogs, 5))`: S=0.57, F=0.32, T=35.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_cogs, 63)`: S=0.37, F=0.18, T=20.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_cogs, 10)`: S=0.08, F=0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_cogs, 22))`: S=0.23, F=0.08, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cogs)`: S=0.28, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cogs / close)`: S=0.12, F=0.04, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.18, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-0.8%
  - 2020: S=0.54 (moderate), ret=+5.2%
  - 2021: S=1.83 (strong), ret=+18.2%
  - 2022: S=2.14 (strong), ret=+16.4%
  - 2023: S=1.43 (moderate), ret=+6.6%

## Risk & Drawdown
- Max drawdown: 8.61% over 491 days (recovered)
- Annualized: return +9.3%, volatility 7.9% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.60, excess kurtosis +3.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.18, max 2.81, latest 1.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +8.52%; worst month: -3.56%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.43
- Sideways: S=0.42
- Bear: S=-0.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_cogs, 5))` S=0.57, F=0.32, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_cogs)`: S=0.28, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_cogs / close)`: S=0.12, F=0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_cogs, 5))`: S=0.57, F=0.32, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_cogs / close)` | TOP3000 | 1.18 | 1.03 | 8.6% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cogs)` | TOP3000 | 0.79 | 0.67 | 28.0% | 80% | bull-only |
| `rank(fnd6_newa1v1300_cogs / close)` | TOP1000 | 0.70 | 0.52 | 11.7% | 100% | bull-only |
| `rank(fnd6_newa1v1300_cogs / close)` | TOP500 | 0.46 | 0.28 | 18.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cogs)` | TOP1000 | 0.40 | 0.26 | 31.3% | 60% | bull-only |
| `rank(fnd6_newa1v1300_cogs)` | TOP500 | 0.19 | 0.09 | 35.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_cogsq: 0.985 (strongly positively correlated)
- fnd6_newqv1300_cogsq: 0.985 (strongly positively correlated)
- cogs: 0.985 (strongly positively correlated)
- fnd6_newa1v1300_ap: 0.972 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.970 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 2.04 | +0.86 | -0.34 | yes |
| rp_ess_revenue | news18 | -0.38 | 1.79 | +0.61 | -0.53 | yes |
| anl4_rd_exp_flag | analyst4 | -0.28 | 1.79 | +0.61 | -0.31 | yes |
| anl4_cfo_flag | analyst4 | -0.06 | 1.67 | +0.49 | -0.94 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.27 | 1.74 | +0.56 | +0.35 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
