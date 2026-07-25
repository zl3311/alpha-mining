---
field: fnd6_itci
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 2.0
best_fitness: 1.8
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SUB_UNIVERSE_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 11
max_drawdown: 0.0405
ann_vol: 0.0506
hit_rate: 0.5401
rolling_sharpe_min: 0.586
rolling_sharpe_max: 3.918
top_merge_partner: rank(fnd6_acdo) + rank(open/close - 1)
negated_best_sharpe: 0.12
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -1.88
---
# fnd6_itci (fundamental6)

*Investment Tax Credit (Income Account)*

## Signal Profile
- `rank(fnd6_itci)`: S=1.88, F=1.65, T=2.1%, GOOD (TOP3000)
- `rank(fnd6_itci / close)`: S=2.00, F=1.80, T=2.2%, GOOD (TOP3000)
- `rank(ts_delta(fnd6_itci, 5))`: S=0.78, F=0.71, T=20.6%, INFERIOR (TOP200)
- `-rank(fnd6_itci)`: S=-0.59, F=-0.36, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_itci, 5))`: S=-0.26, F=-0.14, T=20.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_itci, 63)`: S=-0.17, F=-0.10, T=16.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_itci, 10)`: S=0.38, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_itci, 22))`: S=-0.08, F=-0.02, T=20.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itci)`: S=0.12, F=0.05, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itci / close)`: S=-0.23, F=-0.12, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/2P
- LOW_SHARPE: 30F/2P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 2.00, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.95 (moderate), ret=+3.5%
  - 2020: S=3.98 (strong), ret=+18.5%
  - 2021: S=1.72 (strong), ret=+10.4%
  - 2022: S=0.81 (moderate), ret=+4.5%
  - 2023: S=2.87 (strong), ret=+12.8%

## Risk & Drawdown
- Max drawdown: 4.05% over 162 days (recovered)
- Annualized: return +10.2%, volatility 5.1% (fraction of booksize)
- Hit rate: 54.0% positive days
- Tail shape: skew +0.22, excess kurtosis +1.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.59, max 3.92, latest 2.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.44%; worst month: -2.33%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.29
- Sideways: S=1.68
- Bear: S=3.06

## Negated Direction
Best negated: `rank(-1 * fnd6_itci)` S=0.12, F=0.05, INFERIOR
Direction gap: -1.88 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_itci)`: S=0.12, F=0.05, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_itci / close)`: S=-0.23, F=-0.12, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_itci, 5))`: S=-0.26, F=-0.14, T=20.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_itci / close)` | TOP3000 | 2.00 | 1.80 | 4.0% | 100% | all-weather |
| `rank(fnd6_itci)` | TOP3000 | 1.88 | 1.65 | 4.5% | 100% | all-weather |
| `rank(ts_delta(fnd6_itci, 5))` | TOP200 | 0.78 | 0.71 | 23.5% | 60% | mixed |
| `rank(fnd6_itci / close)` | TOP500 | 0.74 | 0.61 | 15.0% | 60% | bull-only |
| `rank(fnd6_itci)` | TOP500 | 0.62 | 0.48 | 17.1% | 60% | bull-only |
| `rank(fnd6_itci)` | TOP1000 | 0.58 | 0.36 | 10.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_itci, 5))` | TOP3000 | 0.62 | 0.35 | 32.4% | 100% | mixed |
| `rank(fnd6_itci / close)` | TOP1000 | 0.53 | 0.29 | 11.2% | 60% | mixed |
| `rank(ts_delta(fnd6_itci, 5))` | TOP1000 | 0.48 | 0.27 | 32.2% | 40% | bull-only |
| `rank(ts_delta(fnd6_itci, 5))` | TOP500 | 0.42 | 0.25 | 41.1% | 60% | bull-only |
| `rank(fnd6_itci / close)` | TOP200 | 0.23 | 0.12 | 22.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tlcf: 0.426 (moderately positively correlated)
- fnd6_newqv1300_capsq: 0.403 (moderately positively correlated)
- fnd6_newa1v1300_caps: 0.385 (weakly positively correlated)
- anl4_cff_flag: 0.375 (weakly positively correlated)
- anl4_cfo_flag: 0.373 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(fnd6_acdo) + rank(open/close - 1) | unknown | -0.06 | 2.78 | +0.76 | +0.81 | yes |
| implied_volatility_put_90 | option8 | +0.05 | 2.58 | +0.58 | -0.19 | yes |
| rank(fnd6_acdo) * rank(-1 * returns) | unknown | -0.05 | 2.58 | +0.57 | +0.84 | yes |
| implied_volatility_call_30 - implied_volatility_put_30 | option8 | +0.12 | 2.52 | +0.51 | -0.52 | yes |
| implied_volatility_put_120 | option8 | +0.05 | 2.52 | +0.52 | -0.21 | yes |

## Actionability
Already in submitted book (alpha: ['Jjnr7VOl', 'MPbgqZ7o', 'omnopQ9k']).
Blocked by LOW_SUB_UNIVERSE_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
