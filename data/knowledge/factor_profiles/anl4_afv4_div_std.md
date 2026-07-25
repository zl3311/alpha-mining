---
field: anl4_afv4_div_std
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.85
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.107
ann_vol: 0.064
hit_rate: 0.498
rolling_sharpe_min: -1.238
rolling_sharpe_max: 2.047
negated_best_sharpe: 0.85
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.36
---
# anl4_afv4_div_std (analyst4)

*Dividend per share - standard deviation of estimations*

## Signal Profile
- `rank(anl4_afv4_div_std)`: S=0.16, F=0.06, T=5.2%, INFERIOR (TOP200)
- `rank(anl4_afv4_div_std / close)`: S=0.49, F=0.24, T=3.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_div_std, 5))`: S=0.18, F=0.04, T=35.5%, INFERIOR (TOP200)
- `-rank(anl4_afv4_div_std)`: S=-0.08, F=-0.02, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_std, 5))`: S=0.85, F=0.30, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_std, 63)`: S=-0.22, F=-0.05, T=18.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_std, 10)`: S=-0.41, F=-0.20, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_std, 22))`: S=0.31, F=0.09, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_std)`: S=-0.08, F=-0.02, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_std / close)`: S=-0.49, F=-0.24, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.03 (negative), ret=-0.2%
  - 2020: S=0.35 (weak), ret=+2.0%
  - 2021: S=0.78 (moderate), ret=+5.9%
  - 2022: S=1.84 (strong), ret=+13.1%
  - 2023: S=-1.05 (negative), ret=-5.7%

## Risk & Drawdown
- Max drawdown: 10.70% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +3.1%, volatility 6.4% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.29, excess kurtosis +3.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 2.05, latest -1.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.40%; worst month: -2.89%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.05
- Sideways: S=0.46
- Bear: S=-1.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_div_std, 5))` S=0.85, F=0.30, INFERIOR
Direction gap: +0.36 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_div_std)`: S=-0.08, F=-0.02, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_std / close)`: S=-0.49, F=-0.24, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_std, 5))`: S=0.85, F=0.30, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_div_std / close)` | TOP1000 | 0.48 | 0.24 | 10.7% | 60% | bull-only |
| `rank(anl4_afv4_div_std / close)` | TOP500 | 0.37 | 0.17 | 12.1% | 60% | bull-only |
| `rank(anl4_afv4_div_std)` | TOP200 | 0.17 | 0.06 | 29.2% | 20% | bull-only |
| `rank(ts_delta(anl4_afv4_div_std, 5))` | TOP200 | 0.19 | 0.04 | 26.6% | 60% | mixed |
| `rank(anl4_afv4_div_std)` | TOP500 | 0.15 | 0.04 | 16.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_div_high: 0.721 (strongly positively correlated)
- anl4_afv4_div_median: 0.697 (moderately positively correlated)
- anl4_afv4_div_mean: 0.689 (moderately positively correlated)
- fnd6_newa1v1300_dv: 0.629 (moderately positively correlated)
- cashflow_dividends: 0.629 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
