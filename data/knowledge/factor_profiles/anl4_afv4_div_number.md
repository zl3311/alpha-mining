---
field: anl4_afv4_div_number
dataset: analyst4
best_template: ts_zscore
best_sharpe: 1.32
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.2206
ann_vol: 0.0946
hit_rate: 0.4785
rolling_sharpe_min: -1.623
rolling_sharpe_max: 3.2
negated_best_sharpe: 0.81
negated_best_template: neg_rank_level
negated_best_fitness: 0.55
n_negated_sims: 10
direction_gap: -0.51
---
# anl4_afv4_div_number (analyst4)

*Number of estimations for Dividend per share - annually*

## Signal Profile
- `rank(anl4_afv4_div_number)`: S=0.15, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(anl4_afv4_div_number / close)`: S=0.37, F=0.19, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_div_number, 5))`: S=-0.11, F=-0.01, T=35.4%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_div_number)`: S=0.24, F=0.07, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_number, 5))`: S=0.21, F=0.06, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_number, 63)`: S=1.32, F=0.82, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_number, 10)`: S=-0.09, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_number, 22))`: S=-0.66, F=-0.33, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_number)`: S=0.81, F=0.55, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_number / close)`: S=0.09, F=0.02, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.37, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-1.2%
  - 2020: S=1.88 (strong), ret=+20.3%
  - 2021: S=-0.17 (negative), ret=-1.7%
  - 2022: S=-0.25 (negative), ret=-2.5%
  - 2023: S=0.27 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 22.06% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +3.5%, volatility 9.5% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.52, excess kurtosis +1.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.62, max 3.20, latest 0.43

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.67%; worst month: -6.08%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.45
- Sideways: S=-0.49
- Bear: S=2.14

## Negated Direction
Best negated: `rank(-1 * anl4_afv4_div_number)` S=0.81, F=0.55, INFERIOR
Direction gap: -0.51 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_div_number)`: S=0.81, F=0.55, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_number / close)`: S=0.09, F=0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_number, 5))`: S=0.21, F=0.06, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_div_number / close)` | TOP3000 | 0.37 | 0.19 | 22.1% | 40% | mixed |
| `rank(anl4_afv4_div_number / close)` | TOP1000 | 0.32 | 0.14 | 16.9% | 60% | mixed |
| `rank(anl4_afv4_div_number / close)` | TOP500 | 0.21 | 0.07 | 16.4% | 40% | mixed |
| `rank(anl4_afv4_div_number)` | TOP3000 | 0.13 | 0.03 | 9.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- option_breakeven_1080: -0.952 (strongly negatively correlated)
- option_breakeven_720: -0.952 (strongly negatively correlated)
- option_breakeven_360: -0.951 (strongly negatively correlated)
- call_breakeven_1080: -0.950 (strongly negatively correlated)
- call_breakeven_720: -0.950 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
