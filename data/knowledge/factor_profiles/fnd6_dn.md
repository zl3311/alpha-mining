---
field: fnd6_dn
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.114
ann_vol: 0.076
hit_rate: 0.5158
rolling_sharpe_min: -1.145
rolling_sharpe_max: 2.631
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.1
negated_best_template: neg_rank_level
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.8
---
# fnd6_dn (fundamental6)

*Debt - Notes*

## Signal Profile
- `rank(fnd6_dn)`: S=0.69, F=0.47, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_dn / close)`: S=0.90, F=0.67, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dn, 5))`: S=0.64, F=0.36, T=31.5%, INFERIOR (TOP500)
- `-rank(fnd6_dn)`: S=-0.36, F=-0.20, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dn, 5))`: S=-0.17, F=-0.06, T=23.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dn, 63)`: S=-0.25, F=-0.14, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dn, 10)`: S=0.36, F=0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dn, 22))`: S=0.25, F=0.09, T=20.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dn)`: S=0.10, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dn / close)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.16 (moderate), ret=+4.0%
  - 2020: S=-0.04 (negative), ret=-0.2%
  - 2021: S=1.41 (moderate), ret=+13.9%
  - 2022: S=1.35 (moderate), ret=+14.2%
  - 2023: S=0.26 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 11.40% over 160 days (recovered)
- Annualized: return +6.8%, volatility 7.6% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew -0.05, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.63, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.93%; worst month: -3.97%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=1.52
- Bear: S=-2.19

## Negated Direction
Best negated: `rank(-1 * fnd6_dn)` S=0.10, F=0.04, INFERIOR
Direction gap: -0.80 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dn)`: S=0.10, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dn / close)`: S=0.06, F=0.02, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dn, 5))`: S=-0.17, F=-0.06, T=23.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dn / close)` | TOP3000 | 0.89 | 0.67 | 11.4% | 80% | bull-only |
| `rank(fnd6_dn)` | TOP3000 | 0.68 | 0.47 | 18.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_dn, 5))` | TOP500 | 0.64 | 0.36 | 30.7% | 80% | all-weather |
| `rank(fnd6_dn / close)` | TOP1000 | 0.52 | 0.35 | 18.0% | 60% | bull-only |
| `rank(fnd6_dn)` | TOP1000 | 0.35 | 0.20 | 27.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_dn, 5))` | TOP200 | 0.38 | 0.19 | 24.4% | 80% | mixed |
| `rank(ts_delta(fnd6_dn, 5))` | TOP1000 | 0.41 | 0.18 | 28.1% | 60% | mixed |
| `rank(fnd6_dn / close)` | TOP500 | 0.20 | 0.10 | 38.0% | 40% | bull-only |
| `rank(fnd6_dn)` | TOP500 | 0.07 | 0.02 | 45.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: 0.926 (strongly positively correlated)
- ebitda: 0.922 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.922 (strongly positively correlated)
- fnd6_fatp: 0.922 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.922 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.51 | 1.88 | +0.86 | -0.82 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.36 | 1.62 | +0.67 | -0.92 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.40 | 1.53 | +0.64 | -0.85 | yes |
| rp_ess_revenue | news18 | -0.29 | 1.47 | +0.58 | -0.81 | yes |
| news_open_vol | news12 | -0.32 | 1.55 | +0.63 | -0.29 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
