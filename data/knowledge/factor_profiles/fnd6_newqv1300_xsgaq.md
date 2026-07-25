---
field: fnd6_newqv1300_xsgaq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2564
ann_vol: 0.0983
hit_rate: 0.5182
rolling_sharpe_min: -2.8
rolling_sharpe_max: 2.715
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 13
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.48
---
# fnd6_newqv1300_xsgaq (fundamental6)

*Selling, General and Administrative Expenses*

## Signal Profile
- `rank(fnd6_newqv1300_xsgaq)`: S=0.82, F=0.66, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_xsgaq / close)`: S=0.63, F=0.40, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_xsgaq, 5))`: S=0.34, F=0.10, T=37.0%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_xsgaq)`: S=-0.38, F=-0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xsgaq, 5))`: S=0.34, F=0.07, T=37.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_xsgaq, 22)`: S=0.10, F=0.02, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_xsgaq, 10)`: S=0.20, F=0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_xsgaq, 22))`: S=0.38, F=0.13, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xsgaq)`: S=-0.82, F=-0.66, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xsgaq / close)`: S=-0.63, F=-0.40, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.82, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.07 (moderate), ret=+5.3%
  - 2020: S=-1.15 (negative), ret=-8.0%
  - 2021: S=1.11 (moderate), ret=+17.1%
  - 2022: S=1.76 (strong), ret=+18.4%
  - 2023: S=0.92 (moderate), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 25.64% over 600 days (recovered)
- Annualized: return +8.0%, volatility 9.8% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.06, excess kurtosis +2.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.80, max 2.71, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.63%; worst month: -5.40%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.06
- Sideways: S=1.24
- Bear: S=-2.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_xsgaq, 5))` S=0.34, F=0.07, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_xsgaq)`: S=-0.82, F=-0.66, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xsgaq / close)`: S=-0.63, F=-0.40, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xsgaq, 5))`: S=0.34, F=0.07, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_xsgaq)` | TOP3000 | 0.82 | 0.66 | 25.6% | 80% | bull-only |
| `rank(fnd6_newqv1300_xsgaq / close)` | TOP3000 | 0.63 | 0.40 | 9.7% | 80% | mixed |
| `rank(fnd6_newqv1300_xsgaq / close)` | TOP1000 | 0.49 | 0.30 | 11.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_xsgaq)` | TOP1000 | 0.37 | 0.23 | 35.6% | 80% | bull-only |
| `rank(fnd6_newqv1300_xsgaq / close)` | TOP500 | 0.31 | 0.16 | 21.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_xsgaq, 5))` | TOP500 | 0.35 | 0.10 | 14.1% | 40% | mixed |
| `rank(fnd6_newqv1300_xsgaq)` | TOP500 | 0.14 | 0.06 | 49.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_xsgaq / close)` | TOP200 | 0.09 | 0.02 | 26.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- sga_expense: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.971 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.971 (strongly positively correlated)
- assets_curr: 0.971 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.46 | 1.75 | +0.75 | -0.13 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.34 | 1.41 | +0.59 | -0.96 | yes |
| anl4_rd_exp_flag | analyst4 | -0.31 | 1.57 | +0.54 | -0.97 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.28 | 1.46 | +0.51 | -0.87 | yes |
| max_adjusted_eps_guidance_2 | analyst4 | -0.23 | 1.30 | +0.49 | -0.93 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
