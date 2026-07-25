---
field: fnd6_newqv1300_xoprq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.84
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2798
ann_vol: 0.1093
hit_rate: 0.5215
rolling_sharpe_min: -2.982
rolling_sharpe_max: 2.658
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 13
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_newqv1300_xoprq (fundamental6)

*Operating Expense - Total*

## Signal Profile
- `rank(fnd6_newqv1300_xoprq)`: S=0.84, F=0.72, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_xoprq / close)`: S=0.93, F=0.71, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_xoprq, 5))`: S=0.10, F=0.02, T=38.1%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_xoprq)`: S=-0.42, F=-0.28, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xoprq, 5))`: S=0.69, F=0.21, T=37.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_xoprq, 63)`: S=0.13, F=0.02, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_xoprq, 10)`: S=0.17, F=0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_xoprq, 22))`: S=-0.24, F=-0.06, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xoprq)`: S=-0.84, F=-0.72, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xoprq / close)`: S=-0.93, F=-0.71, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+4.2%
  - 2020: S=-1.67 (negative), ret=-11.9%
  - 2021: S=1.29 (moderate), ret=+20.8%
  - 2022: S=1.78 (strong), ret=+23.5%
  - 2023: S=1.00 (moderate), ret=+8.2%

## Risk & Drawdown
- Max drawdown: 27.98% over 744 days (recovered)
- Annualized: return +9.2%, volatility 10.9% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.04, excess kurtosis +2.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.98, max 2.66, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.93%; worst month: -5.21%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=1.31
- Bear: S=-2.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_xoprq, 5))` S=0.69, F=0.21, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_xoprq)`: S=-0.84, F=-0.72, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xoprq / close)`: S=-0.93, F=-0.71, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xoprq, 5))`: S=0.69, F=0.21, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_xoprq)` | TOP3000 | 0.84 | 0.72 | 28.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_xoprq / close)` | TOP3000 | 0.92 | 0.71 | 9.1% | 100% | mixed |
| `rank(fnd6_newqv1300_xoprq / close)` | TOP1000 | 0.65 | 0.46 | 11.9% | 100% | bull-only |
| `rank(fnd6_newqv1300_xoprq / close)` | TOP500 | 0.53 | 0.35 | 18.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_xoprq)` | TOP1000 | 0.42 | 0.28 | 32.1% | 60% | bull-only |
| `rank(fnd6_newqv1300_xoprq)` | TOP500 | 0.23 | 0.11 | 40.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_xoprq / close)` | TOP200 | 0.12 | 0.04 | 28.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_xoprq, 5))` | TOP500 | 0.12 | 0.02 | 16.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- operating_expense: 1.000 (strongly positively correlated)
- fnd6_newqv1300_icaptq: 0.987 (strongly positively correlated)
- invested_capital: 0.987 (strongly positively correlated)
- fnd6_newqv1300_acoq: 0.975 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.975 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.68 | +0.65 | -0.94 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.44 | 1.71 | +0.72 | -0.19 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.37 | 1.45 | +0.61 | -0.97 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.31 | 1.49 | +0.54 | -0.89 | yes |
| max_adjusted_eps_guidance_2 | analyst4 | -0.25 | 1.32 | +0.49 | -0.95 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
