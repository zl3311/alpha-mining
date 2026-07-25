---
field: fnd6_siv
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.54
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1014
ann_vol: 0.0447
hit_rate: 0.5134
rolling_sharpe_min: -1.855
rolling_sharpe_max: 2.569
redundancy_cluster: 50
negated_best_sharpe: 0.54
negated_best_template: neg_rank_level
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.18
---
# fnd6_siv (fundamental6)

*Sale of Investments*

## Signal Profile
- `rank(fnd6_siv)`: S=0.57, F=0.27, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_siv / close)`: S=0.72, F=0.36, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_siv, 5))`: S=0.42, F=0.22, T=31.4%, INFERIOR (TOP500)
- `-rank(fnd6_siv)`: S=-0.37, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_siv, 5))`: S=-0.06, F=-0.01, T=27.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_siv, 22)`: S=0.01, F=0.00, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_siv, 10)`: S=0.33, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_siv, 22))`: S=-0.18, F=-0.07, T=15.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_siv)`: S=0.54, F=0.37, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_siv / close)`: S=0.38, F=0.22, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.3%
  - 2020: S=-1.12 (negative), ret=-4.3%
  - 2021: S=1.41 (moderate), ret=+8.4%
  - 2022: S=1.64 (strong), ret=+8.6%
  - 2023: S=0.73 (moderate), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 10.14% over 770 days (recovered)
- Annualized: return +3.2%, volatility 4.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.02, excess kurtosis +1.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.85, max 2.57, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.61%; worst month: -2.03%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.84
- Sideways: S=1.22
- Bear: S=-2.42

## Negated Direction
Best negated: `rank(-1 * fnd6_siv)` S=0.54, F=0.37, INFERIOR
Direction gap: -0.18 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_siv)`: S=0.54, F=0.37, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_siv / close)`: S=0.38, F=0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_siv, 5))`: S=-0.06, F=-0.01, T=27.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_siv / close)` | TOP3000 | 0.71 | 0.36 | 10.1% | 80% | bull-only |
| `rank(fnd6_siv)` | TOP3000 | 0.57 | 0.27 | 13.7% | 80% | bull-only |
| `rank(fnd6_siv / close)` | TOP1000 | 0.48 | 0.24 | 13.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_siv, 5))` | TOP500 | 0.42 | 0.22 | 35.0% | 40% | mixed |
| `rank(fnd6_siv)` | TOP1000 | 0.35 | 0.16 | 17.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_siv, 5))` | TOP1000 | 0.33 | 0.14 | 21.9% | 60% | mixed |
| `rank(fnd6_siv / close)` | TOP500 | 0.07 | 0.02 | 22.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ivch: 0.894 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.829 (strongly positively correlated)
- fn_prepaid_expense_a: 0.823 (strongly positively correlated)
- invested_capital: 0.819 (strongly positively correlated)
- fnd6_newqv1300_icaptq: 0.819 (strongly positively correlated)

Redundancy cluster #50: 3 similar fields, mean |rho| 0.824 (representative: sales_estimate_stddev_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
