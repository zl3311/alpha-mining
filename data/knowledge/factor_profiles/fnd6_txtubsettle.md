---
field: fnd6_txtubsettle
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.44
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1658
ann_vol: 0.0719
hit_rate: 0.498
rolling_sharpe_min: -2.785
rolling_sharpe_max: 2.223
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: 0.16
---
# fnd6_txtubsettle (fundamental6)

*Settlements with Tax Authorities*

## Signal Profile
- `rank(fnd6_txtubsettle)`: S=0.41, F=0.20, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_txtubsettle / close)`: S=0.46, F=0.24, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubsettle, 5))`: S=0.33, F=0.13, T=38.2%, INFERIOR (TOP3000)
- `-rank(fnd6_txtubsettle)`: S=-0.35, F=-0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubsettle, 5))`: S=0.60, F=0.29, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubsettle, 22)`: S=0.44, F=0.31, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubsettle, 10)`: S=0.11, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubsettle, 22))`: S=0.14, F=0.04, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsettle)`: S=-0.35, F=-0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsettle / close)`: S=-0.41, F=-0.21, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+1.1%
  - 2020: S=-1.97 (negative), ret=-9.2%
  - 2021: S=1.22 (moderate), ret=+10.9%
  - 2022: S=1.08 (moderate), ret=+10.8%
  - 2023: S=0.38 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 16.58% over 794 days (recovered)
- Annualized: return +3.2%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.01, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.79, max 2.22, latest 0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.94%; worst month: -3.53%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.70
- Sideways: S=1.16
- Bear: S=-3.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubsettle, 5))` S=0.60, F=0.29, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubsettle)`: S=-0.35, F=-0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubsettle / close)`: S=-0.41, F=-0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubsettle, 5))`: S=0.60, F=0.29, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubsettle / close)` | TOP3000 | 0.45 | 0.24 | 16.6% | 80% | bull-only |
| `rank(fnd6_txtubsettle / close)` | TOP1000 | 0.40 | 0.21 | 18.4% | 80% | bull-only |
| `rank(fnd6_txtubsettle)` | TOP3000 | 0.40 | 0.20 | 19.1% | 80% | bull-only |
| `rank(fnd6_txtubsettle)` | TOP1000 | 0.34 | 0.17 | 21.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_txtubsettle, 5))` | TOP3000 | 0.33 | 0.13 | 34.4% | 80% | bear-only |
| `rank(fnd6_txtubsettle / close)` | TOP500 | 0.14 | 0.05 | 24.2% | 60% | bull-only |
| `rank(fnd6_txtubsettle)` | TOP500 | 0.09 | 0.03 | 26.7% | 40% | bull-only |
| `rank(ts_delta(fnd6_txtubsettle, 5))` | TOP500 | 0.11 | 0.03 | 46.6% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: 0.926 (strongly positively correlated)
- fnd6_txtubsoflimit: 0.921 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.915 (strongly positively correlated)
- net_income_total_2: 0.914 (strongly positively correlated)
- fnd6_xrent: 0.914 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
