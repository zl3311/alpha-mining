---
field: fnd6_newqv1300_stkcpaq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.88
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.3653
ann_vol: 0.2434
hit_rate: 0.5296
rolling_sharpe_min: -0.314
rolling_sharpe_max: 1.955
top_merge_partner: fn_liab_fair_val_l1_q
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.82
---
# fnd6_newqv1300_stkcpaq (fundamental6)

*After-tax stock compensation*

## Signal Profile
- `rank(fnd6_newqv1300_stkcpaq)`: S=0.50, F=0.32, T=6.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_stkcpaq / close)`: S=0.71, F=0.55, T=9.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_stkcpaq, 5))`: S=0.88, F=0.62, T=42.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_stkcpaq)`: S=-0.05, F=-0.01, T=9.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_stkcpaq, 5))`: S=-0.29, F=-0.12, T=49.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_stkcpaq, 22)`: S=0.38, F=0.22, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_stkcpaq, 10)`: S=0.54, F=0.43, T=6.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_stkcpaq, 22))`: S=0.88, F=0.79, T=22.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcpaq)`: S=0.06, F=0.02, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcpaq / close)`: S=-0.34, F=-0.20, T=10.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+9.3%
  - 2020: S=0.26 (weak), ret=+5.5%
  - 2021: S=1.67 (strong), ret=+56.9%
  - 2022: S=-0.13 (negative), ret=-2.9%
  - 2023: S=1.64 (strong), ret=+35.0%

## Risk & Drawdown
- Max drawdown: 36.53% over 598 days (recovered)
- Annualized: return +21.2%, volatility 24.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +1.93, excess kurtosis +30.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.31, max 1.96, latest 1.57

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +30.37%; worst month: -20.45%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.50
- Sideways: S=1.26
- Bear: S=0.89

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_stkcpaq)` S=0.06, F=0.02, INFERIOR
Direction gap: -0.82 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_stkcpaq)`: S=0.06, F=0.02, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_stkcpaq / close)`: S=-0.34, F=-0.20, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_stkcpaq, 5))`: S=-0.29, F=-0.12, T=49.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_stkcpaq, 5))` | TOP3000 | 0.87 | 0.62 | 36.5% | 80% | mixed |
| `rank(fnd6_newqv1300_stkcpaq / close)` | TOP1000 | 0.72 | 0.55 | 12.7% | 100% | all-weather |
| `rank(ts_delta(fnd6_newqv1300_stkcpaq, 5))` | TOP200 | 0.63 | 0.41 | 38.4% | 60% | weak |
| `rank(fnd6_newqv1300_stkcpaq)` | TOP3000 | 0.50 | 0.32 | 32.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_stkcpaq / close)` | TOP3000 | 0.40 | 0.23 | 23.6% | 80% | mixed |
| `rank(fnd6_newqv1300_stkcpaq / close)` | TOP500 | 0.36 | 0.20 | 19.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_mibt: -0.152 (weakly negatively correlated)
- news_close_vol: 0.150 (weakly positively correlated)
- pcr_vol_all: -0.147 (weakly negatively correlated)
- fnd6_mibn: -0.146 (weakly negatively correlated)
- fnd6_newqv1300_aociotherq: 0.142 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_liab_fair_val_l1_q | fundamental2 | -0.07 | 1.25 | +0.38 | -0.55 | yes |
| pv13_revere_key_sector_total | pv13 | -0.03 | 1.23 | +0.35 | -0.57 | yes |
| growth_potential_rank_derivative | model16 | +0.07 | 1.19 | +0.31 | -0.67 | yes |
| fn_avg_diluted_sharesout_adj_a | fundamental2 | -0.03 | 1.25 | +0.36 | +0.35 | yes |
| fnd2_propplteqflublgland | fundamental2 | -0.04 | 1.21 | +0.34 | -0.24 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
