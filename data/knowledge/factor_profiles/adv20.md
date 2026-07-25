---
field: adv20
dataset: pv1
best_template: ts_zscore
best_sharpe: 0.62
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bear-only
n_variations_with_pnl: 8
max_drawdown: 0.2052
ann_vol: 0.0721
hit_rate: 0.5004
rolling_sharpe_min: -2.006
rolling_sharpe_max: 3.289
negated_best_sharpe: -0.11
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.03
n_negated_sims: 4
direction_gap: -0.73
---
# adv20 (pv1)

*Average daily volume in past 20 days*

## Signal Profile
- `rank(adv20)`: S=0.37, F=0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_delta(adv20, 5))`: S=0.48, F=0.14, T=23.7%, INFERIOR (TOP3000)
- `-rank(adv20)`: S=-0.14, F=-0.04, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(adv20, 5))`: S=-0.48, F=-0.14, T=23.7%, INFERIOR (TOP3000)
- `ts_zscore(adv20, 22)`: S=0.62, F=0.25, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(adv20, 10)`: S=0.09, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(adv20, 22))`: S=0.57, F=0.22, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * adv20)`: S=-0.37, F=-0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * adv20 / close)`: S=-0.11, F=-0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.37 (moderate), ret=+5.5%
  - 2020: S=2.27 (strong), ret=+13.9%
  - 2021: S=-0.37 (negative), ret=-3.1%
  - 2022: S=-0.66 (negative), ret=-6.0%
  - 2023: S=0.39 (weak), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 20.52% over 1046 days (not yet recovered, ongoing at window end)
- Annualized: return +2.7%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.22, excess kurtosis +0.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.01, max 3.29, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.10%; worst month: -4.50%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.86
- Sideways: S=0.76
- Bear: S=1.38

## Negated Direction
Best negated: `rank(-1 * adv20 / close)` S=-0.11, F=-0.03, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * adv20)`: S=-0.37, F=-0.17, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * adv20 / close)`: S=-0.11, F=-0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(adv20, 5))`: S=-0.48, F=-0.14, T=23.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(adv20)` | TOP3000 | 0.37 | 0.17 | 20.5% | 60% | bear-only |
| `rank(adv20)` | TOP200 | 0.33 | 0.15 | 23.2% | 60% | mixed |
| `rank(ts_delta(adv20, 5))` | TOP1000 | 0.45 | 0.14 | 7.6% | 80% | weak |
| `rank(ts_delta(adv20, 5))` | TOP3000 | 0.48 | 0.14 | 5.5% | 60% | mixed |
| `rank(ts_delta(adv20, 5))` | TOP200 | 0.32 | 0.10 | 25.2% | 80% | mixed |
| `rank(ts_delta(adv20, 5))` | TOP500 | 0.31 | 0.09 | 10.9% | 80% | weak |
| `rank(adv20)` | TOP500 | 0.16 | 0.05 | 25.3% | 60% | bear-only |
| `rank(adv20)` | TOP1000 | 0.14 | 0.04 | 27.7% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_cshtr: 0.818 (strongly positively correlated)
- news_open_vol: 0.806 (strongly positively correlated)
- implied_volatility_mean_skew_90: -0.716 (strongly negatively correlated)
- implied_volatility_mean_skew_60: -0.713 (strongly negatively correlated)
- implied_volatility_mean_skew_360: -0.712 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
