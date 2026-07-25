---
field: fnd6_optex
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.89
best_fitness: 0.75
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: all-weather
n_variations_with_pnl: 12
max_drawdown: 0.0909
ann_vol: 0.0991
hit_rate: 0.5142
rolling_sharpe_min: -0.338
rolling_sharpe_max: 2.852
top_merge_partner: anl4_fcf_mean
negated_best_sharpe: -0.11
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.03
n_negated_sims: 4
direction_gap: -1.0
---
# fnd6_optex (fundamental6)

*Options Exercisable (000)*

## Signal Profile
- `rank(fnd6_optex)`: S=0.82, F=0.64, T=3.5%, INFERIOR (TOP200)
- `rank(fnd6_optex / close)`: S=0.89, F=0.75, T=3.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optex, 5))`: S=0.97, F=0.69, T=36.8%, INFERIOR (TOP1000)
- `-rank(fnd6_optex)`: S=-0.37, F=-0.13, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optex, 5))`: S=-0.73, F=-0.43, T=40.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optex, 63)`: S=0.47, F=0.34, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optex, 10)`: S=0.51, F=0.30, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optex, 22))`: S=0.75, F=0.51, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optex)`: S=-0.13, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optex / close)`: S=-0.11, F=-0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+0.9%
  - 2020: S=2.76 (strong), ret=+28.6%
  - 2021: S=0.28 (weak), ret=+2.6%
  - 2022: S=0.07 (weak), ret=+0.9%
  - 2023: S=1.14 (moderate), ret=+10.6%

## Risk & Drawdown
- Max drawdown: 9.09% over 216 days (recovered)
- Annualized: return +8.9%, volatility 9.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.29, excess kurtosis +2.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.34, max 2.85, latest 1.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.93%; worst month: -4.99%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.63
- Sideways: S=0.30
- Bear: S=1.73

## Negated Direction
Best negated: `rank(-1 * fnd6_optex / close)` S=-0.11, F=-0.03, INFERIOR
Direction gap: -1.00 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optex)`: S=-0.13, F=-0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optex / close)`: S=-0.11, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optex, 5))`: S=-0.73, F=-0.43, T=40.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optex / close)` | TOP200 | 0.90 | 0.75 | 9.1% | 100% | all-weather |
| `rank(ts_delta(fnd6_optex, 5))` | TOP1000 | 0.97 | 0.69 | 24.8% | 80% | all-weather |
| `rank(fnd6_optex)` | TOP200 | 0.83 | 0.64 | 12.6% | 80% | all-weather |
| `rank(fnd6_optex / close)` | TOP500 | 0.75 | 0.48 | 14.2% | 80% | mixed |
| `rank(ts_delta(fnd6_optex, 5))` | TOP3000 | 0.73 | 0.43 | 27.1% | 80% | mixed |
| `rank(fnd6_optex)` | TOP500 | 0.69 | 0.39 | 10.9% | 100% | mixed |
| `rank(fnd6_optex / close)` | TOP1000 | 0.53 | 0.28 | 13.7% | 60% | bear-only |
| `rank(ts_delta(fnd6_optex, 5))` | TOP500 | 0.44 | 0.25 | 44.2% | 60% | mixed |
| `rank(fnd6_optex)` | TOP1000 | 0.37 | 0.13 | 8.9% | 40% | weak |
| `rank(ts_delta(fnd6_optex, 5))` | TOP200 | 0.23 | 0.12 | 34.3% | 60% | weak |
| `rank(fnd6_optex)` | TOP3000 | 0.15 | 0.03 | 21.5% | 60% | bear-only |
| `rank(fnd6_optex / close)` | TOP3000 | 0.12 | 0.03 | 32.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_optexd: 0.836 (strongly positively correlated)
- fnd6_optosey: 0.611 (moderately positively correlated)
- fnd6_cshtrq: 0.582 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_q: 0.571 (moderately positively correlated)
- fn_comp_options_out_number_q: 0.566 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_fcf_mean | analyst4 | -0.18 | 1.40 | +0.49 | -0.94 | yes |
| anl4_fcf_median | analyst4 | -0.18 | 1.41 | +0.49 | -0.94 | yes |
| implied_volatility_mean_skew_150 | option8 | -0.20 | 1.38 | +0.48 | -0.97 | yes |
| anl4_fcf_low | analyst4 | -0.21 | 1.38 | +0.47 | -0.93 | yes |
| fnd2_a_lhdiprtsg | fundamental2 | -0.17 | 1.37 | +0.47 | -0.96 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
