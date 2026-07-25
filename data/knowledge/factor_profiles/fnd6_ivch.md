---
field: fnd6_ivch
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.072
ann_vol: 0.0447
hit_rate: 0.4964
rolling_sharpe_min: -1.168
rolling_sharpe_max: 2.104
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_ivch (fundamental6)

*Increase in Investments*

## Signal Profile
- `rank(fnd6_ivch)`: S=0.32, F=0.11, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_ivch / close)`: S=0.42, F=0.16, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ivch, 5))`: S=0.26, F=0.09, T=34.0%, INFERIOR (TOP3000)
- `-rank(fnd6_ivch)`: S=-0.22, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivch, 5))`: S=0.16, F=0.06, T=28.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ivch, 63)`: S=0.66, F=0.56, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ivch, 10)`: S=0.30, F=0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ivch, 22))`: S=0.31, F=0.14, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivch)`: S=0.43, F=0.26, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivch / close)`: S=0.27, F=0.13, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.42, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.19 (negative), ret=-0.5%
  - 2020: S=-0.64 (negative), ret=-2.6%
  - 2021: S=1.27 (moderate), ret=+7.9%
  - 2022: S=0.89 (moderate), ret=+4.1%
  - 2023: S=0.12 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 7.20% over 575 days (recovered)
- Annualized: return +1.9%, volatility 4.5% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.15, excess kurtosis +1.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.10, latest 0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.34%; worst month: -2.62%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.96
- Sideways: S=0.79
- Bear: S=-1.73

## Negated Direction
Best negated: `rank(-1 * fnd6_ivch)` S=0.43, F=0.26, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_ivch)`: S=0.43, F=0.26, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ivch / close)`: S=0.27, F=0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ivch, 5))`: S=0.16, F=0.06, T=28.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ivch / close)` | TOP3000 | 0.42 | 0.16 | 7.2% | 60% | bull-only |
| `rank(fnd6_ivch / close)` | TOP1000 | 0.36 | 0.15 | 10.5% | 80% | bull-only |
| `rank(fnd6_ivch / close)` | TOP500 | 0.32 | 0.14 | 11.2% | 60% | bull-only |
| `rank(fnd6_ivch)` | TOP3000 | 0.33 | 0.11 | 12.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_ivch, 5))` | TOP3000 | 0.26 | 0.09 | 25.1% | 60% | all-weather |
| `rank(fnd6_ivch)` | TOP1000 | 0.21 | 0.07 | 15.9% | 80% | bull-only |
| `rank(fnd6_ivch)` | TOP500 | 0.15 | 0.04 | 17.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_siv: 0.894 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.763 (strongly positively correlated)
- cash: 0.756 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.754 (strongly positively correlated)
- fnd6_newa1v1300_aol2: 0.744 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
