---
field: fnd6_dd
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.95
best_fitness: 0.74
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1973
ann_vol: 0.1003
hit_rate: 0.4874
rolling_sharpe_min: -1.044
rolling_sharpe_max: 3.715
top_merge_partner: anl4_afv4_dts_spe
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.39
---
# fnd6_dd (fundamental6)

*Debt - Debentures*

## Signal Profile
- `rank(fnd6_dd)`: S=0.13, F=0.03, T=2.9%, INFERIOR (TOP500)
- `rank(fnd6_dd / close)`: S=0.17, F=0.05, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dd, 5))`: S=0.95, F=0.74, T=15.6%, INFERIOR (TOP500)
- `-rank(fnd6_dd)`: S=-0.09, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd, 5))`: S=0.34, F=0.19, T=12.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd, 63)`: S=0.50, F=0.51, T=8.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd, 10)`: S=-0.07, F=-0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd, 22))`: S=0.11, F=0.04, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd)`: S=0.55, F=0.34, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd / close)`: S=0.56, F=0.35, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.99 (strong), ret=+29.9%
  - 2020: S=0.87 (moderate), ret=+7.7%
  - 2021: S=-0.19 (negative), ret=-2.5%
  - 2022: S=0.40 (weak), ret=+3.5%
  - 2023: S=0.93 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 19.73% over 1084 days (recovered)
- Annualized: return +9.4%, volatility 10.0% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.18, excess kurtosis +5.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 3.71, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +10.41%; worst month: -7.20%
Positive months: 62%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.10
- Sideways: S=2.27
- Bear: S=-0.45

## Negated Direction
Best negated: `rank(-1 * fnd6_dd / close)` S=0.56, F=0.35, INFERIOR
Direction gap: -0.39 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dd)`: S=0.55, F=0.34, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd / close)`: S=0.56, F=0.35, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd, 5))`: S=0.34, F=0.19, T=12.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dd, 5))` | TOP500 | 0.94 | 0.74 | 19.7% | 80% | mixed |
| `rank(ts_delta(fnd6_dd, 5))` | TOP200 | 0.39 | 0.24 | 31.2% | 60% | bull-only |
| `rank(fnd6_dd / close)` | TOP500 | 0.16 | 0.05 | 13.6% | 60% | bull-only |
| `rank(fnd6_dd)` | TOP500 | 0.12 | 0.03 | 15.0% | 60% | bull-only |
| `rank(fnd6_dd / close)` | TOP3000 | 0.09 | 0.02 | 17.8% | 60% | bull-only |
| `rank(fnd6_dd)` | TOP1000 | 0.09 | 0.02 | 18.0% | 80% | bull-only |
| `rank(fnd6_dd / close)` | TOP1000 | 0.09 | 0.02 | 17.4% | 80% | bull-only |
| `rank(fnd6_dd)` | TOP3000 | 0.09 | 0.02 | 18.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dvpa: 0.377 (weakly positively correlated)
- fnd6_lifr: 0.370 (weakly positively correlated)
- fnd6_lno: 0.359 (weakly positively correlated)
- fnd6_esopnr: 0.314 (weakly positively correlated)
- pv13_revere_term: 0.309 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.22 | 1.55 | +0.55 | +0.72 | yes |
| anl4_rd_exp_flag | analyst4 | -0.13 | 1.49 | +0.46 | -0.16 | yes |
| sharesout | pv1 | -0.12 | 1.48 | +0.45 | +0.29 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.12 | 1.36 | +0.42 | -0.28 | yes |
| fnd2_unrgtxbnfinregfprtxps | fundamental2 | -0.04 | 1.30 | +0.36 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
