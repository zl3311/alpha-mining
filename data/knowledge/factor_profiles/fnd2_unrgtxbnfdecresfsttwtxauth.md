---
field: fnd2_unrgtxbnfdecresfsttwtxauth
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.61
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0463
ann_vol: 0.0333
hit_rate: 0.5093
rolling_sharpe_min: -1.186
rolling_sharpe_max: 2.288
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.21
---
# fnd2_unrgtxbnfdecresfsttwtxauth (fundamental2)

*Amount of decrease in unrecognized tax benefits resulting from settlements with taxing authorities.*

## Signal Profile
- `rank(fnd2_unrgtxbnfdecresfsttwtxauth)`: S=0.10, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_unrgtxbnfdecresfsttwtxauth / close)`: S=0.40, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unrgtxbnfdecresfsttwtxauth, 5))`: S=0.10, F=0.02, T=33.9%, INFERIOR (TOP3000)
- `-rank(fnd2_unrgtxbnfdecresfsttwtxauth)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfdecresfsttwtxauth, 5))`: S=0.61, F=0.29, T=33.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_unrgtxbnfdecresfsttwtxauth, 22)`: S=-0.68, F=-0.57, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_unrgtxbnfdecresfsttwtxauth, 10)`: S=-0.36, F=-0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unrgtxbnfdecresfsttwtxauth, 22))`: S=0.17, F=0.05, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdecresfsttwtxauth)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdecresfsttwtxauth / close)`: S=-0.24, F=-0.07, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.38, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.53 (strong), ret=+4.4%
  - 2020: S=-0.60 (negative), ret=-2.0%
  - 2021: S=1.25 (moderate), ret=+4.7%
  - 2022: S=0.68 (moderate), ret=+2.2%
  - 2023: S=-1.02 (negative), ret=-3.1%

## Risk & Drawdown
- Max drawdown: 4.63% over 412 days (recovered)
- Annualized: return +1.3%, volatility 3.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.03, excess kurtosis +1.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.29, latest -1.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +2.57%; worst month: -2.12%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.21
- Sideways: S=1.14
- Bear: S=-2.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_unrgtxbnfdecresfsttwtxauth, 5))` S=0.61, F=0.29, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_unrgtxbnfdecresfsttwtxauth)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdecresfsttwtxauth / close)`: S=-0.24, F=-0.07, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfdecresfsttwtxauth, 5))`: S=0.61, F=0.29, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_unrgtxbnfdecresfsttwtxauth / close)` | TOP3000 | 0.38 | 0.13 | 4.6% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfdecresfsttwtxauth / close)` | TOP1000 | 0.22 | 0.07 | 6.9% | 60% | bull-only |
| `rank(ts_delta(fnd2_unrgtxbnfdecresfsttwtxauth, 5))` | TOP3000 | 0.12 | 0.02 | 29.0% | 60% | mixed |
| `rank(fnd2_unrgtxbnfdecresfsttwtxauth)` | TOP3000 | 0.09 | 0.02 | 11.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubsettle: 0.564 (moderately positively correlated)
- fnd2_unrgtxbnfdcfpprdtxpss: 0.563 (moderately positively correlated)
- fn_taxes_payable_q: 0.560 (moderately positively correlated)
- fn_unrecognized_tax_benefits_a: 0.548 (moderately positively correlated)
- fnd2_a_ltrmdmrepoplay5: 0.542 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
