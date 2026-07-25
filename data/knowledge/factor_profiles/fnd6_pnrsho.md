---
field: fnd6_pnrsho
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.89
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.3498
ann_vol: 0.2129
hit_rate: 0.4931
rolling_sharpe_min: -0.917
rolling_sharpe_max: 2.656
top_merge_partner: fn_comp_options_exercisable_number_a
negated_best_sharpe: 0.26
negated_best_template: neg_rank
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.63
---
# fnd6_pnrsho (fundamental6)

*Nonred Pfd Shares Outs (000)*

## Signal Profile
- `rank(fnd6_pnrsho)`: S=0.64, F=0.51, T=3.1%, INFERIOR (TOP200)
- `rank(fnd6_pnrsho / close)`: S=0.64, F=0.51, T=3.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_pnrsho, 5))`: S=0.89, F=0.78, T=24.5%, INFERIOR (TOP3000)
- `-rank(fnd6_pnrsho)`: S=0.26, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pnrsho, 5))`: S=-0.13, F=-0.05, T=17.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_pnrsho, 22)`: S=-0.43, F=-0.31, T=6.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pnrsho, 10)`: S=-0.78, F=-0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pnrsho, 22))`: S=0.61, F=0.66, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pnrsho)`: S=0.26, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pnrsho / close)`: S=0.25, F=0.08, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.88, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.78 (moderate), ret=+14.9%
  - 2020: S=0.70 (moderate), ret=+15.5%
  - 2021: S=2.20 (strong), ret=+44.7%
  - 2022: S=1.49 (moderate), ret=+25.8%
  - 2023: S=-0.36 (negative), ret=-8.8%

## Risk & Drawdown
- Max drawdown: 34.98% over 512 days (not yet recovered, ongoing at window end)
- Annualized: return +18.8%, volatility 21.3% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +2.75, excess kurtosis +38.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 2.66, latest -0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +22.68%; worst month: -16.25%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.72
- Sideways: S=0.56
- Bear: S=1.36

## Negated Direction
Best negated: `-rank(fnd6_pnrsho)` S=0.26, F=0.08, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_pnrsho)`: S=0.26, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pnrsho / close)`: S=0.25, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pnrsho, 5))`: S=-0.13, F=-0.05, T=17.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_pnrsho, 5))` | TOP3000 | 0.88 | 0.78 | 35.0% | 80% | all-weather |
| `rank(fnd6_pnrsho / close)` | TOP200 | 0.63 | 0.51 | 14.4% | 60% | all-weather |
| `rank(fnd6_pnrsho)` | TOP200 | 0.63 | 0.51 | 14.6% | 60% | all-weather |
| `rank(ts_delta(fnd6_pnrsho, 5))` | TOP500 | 0.35 | 0.25 | 45.3% | 60% | bull-only |
| `rank(fnd6_pnrsho / close)` | TOP3000 | 0.48 | 0.18 | 8.9% | 80% | bear-only |
| `rank(ts_delta(fnd6_pnrsho, 5))` | TOP200 | 0.33 | 0.17 | 19.9% | 60% | bull-only |
| `rank(fnd6_pnrsho)` | TOP3000 | 0.47 | 0.17 | 8.7% | 80% | bear-only |
| `rank(fnd6_pnrsho)` | TOP500 | 0.19 | 0.06 | 14.5% | 80% | mixed |
| `rank(fnd6_pnrsho / close)` | TOP500 | 0.20 | 0.06 | 15.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_invfg: 0.170 (weakly positively correlated)
- fnd6_newqv1300_invtq: 0.165 (weakly positively correlated)
- inventory: 0.165 (weakly positively correlated)
- fnd6_newa1v1300_invt: 0.157 (weakly positively correlated)
- fnd6_newqv1300_invwipq: 0.152 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_comp_options_exercisable_number_a | fundamental2 | -0.03 | 1.26 | +0.38 | -0.82 | yes |
| growth_potential_rank_derivative | model16 | -0.05 | 1.28 | +0.40 | -0.32 | yes |
| analyst_revision_rank_derivative | model16 | -0.05 | 1.31 | +0.38 | -0.33 | yes |
| relative_valuation_rank_derivative | model16 | -0.05 | 1.31 | +0.38 | -0.33 | yes |
| earnings_certainty_rank_derivative | model16 | -0.05 | 1.31 | +0.38 | -0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
