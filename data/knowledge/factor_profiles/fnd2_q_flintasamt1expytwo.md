---
field: fnd2_q_flintasamt1expytwo
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.65
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.1749
ann_vol: 0.1188
hit_rate: 0.502
rolling_sharpe_min: -1.657
rolling_sharpe_max: 1.881
negated_best_sharpe: 0.65
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.59
n_negated_sims: 10
direction_gap: 0.02
---
# fnd2_q_flintasamt1expytwo (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 2nd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_q_flintasamt1expytwo)`: S=0.34, F=0.16, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_q_flintasamt1expytwo / close)`: S=0.37, F=0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_q_flintasamt1expytwo, 5))`: S=0.46, F=0.18, T=36.3%, INFERIOR (TOP3000)
- `-rank(fnd2_q_flintasamt1expytwo)`: S=0.00, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expytwo, 5))`: S=0.02, F=0.00, T=34.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_q_flintasamt1expytwo, 22)`: S=0.46, F=0.28, T=27.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_q_flintasamt1expytwo, 10)`: S=0.20, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_q_flintasamt1expytwo, 22))`: S=0.63, F=0.42, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expytwo)`: S=0.56, F=0.51, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expytwo / close)`: S=0.65, F=0.59, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.77 (negative), ret=-6.8%
  - 2020: S=0.62 (moderate), ret=+7.4%
  - 2021: S=0.90 (moderate), ret=+11.7%
  - 2022: S=0.45 (weak), ret=+6.1%
  - 2023: S=0.75 (moderate), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 17.49% over 560 days (not yet recovered, ongoing at window end)
- Annualized: return +5.3%, volatility 11.9% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.60, excess kurtosis +5.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 1.88, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +14.15%; worst month: -7.18%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.75
- Sideways: S=0.24
- Bear: S=1.78

## Negated Direction
Best negated: `rank(-1 * fnd2_q_flintasamt1expytwo / close)` S=0.65, F=0.59, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_q_flintasamt1expytwo)`: S=0.56, F=0.51, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expytwo / close)`: S=0.65, F=0.59, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expytwo, 5))`: S=0.02, F=0.00, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_q_flintasamt1expytwo, 5))` | TOP3000 | 0.45 | 0.18 | 17.5% | 80% | bear-only |
| `rank(fnd2_q_flintasamt1expytwo / close)` | TOP3000 | 0.36 | 0.16 | 8.8% | 100% | bull-only |
| `rank(ts_delta(fnd2_q_flintasamt1expytwo, 5))` | TOP500 | 0.39 | 0.16 | 43.0% | 80% | mixed |
| `rank(fnd2_q_flintasamt1expytwo)` | TOP3000 | 0.33 | 0.16 | 22.3% | 60% | bull-only |
| `rank(ts_delta(fnd2_q_flintasamt1expytwo, 5))` | TOP1000 | 0.38 | 0.15 | 23.5% | 80% | mixed |
| `rank(ts_delta(fnd2_q_flintasamt1expytwo, 5))` | TOP200 | 0.13 | 0.04 | 67.1% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd2_q_flintasamt1expythree: 0.813 (strongly positively correlated)
- fnd2_q_flintasamt1expyfour: 0.676 (moderately positively correlated)
- rp_nip_credit_ratings: 0.126 (weakly positively correlated)
- fn_finite_lived_intangible_assets_gross_q: 0.110 (weakly positively correlated)
- fn_income_taxes_paid_q: 0.105 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
