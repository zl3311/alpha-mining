---
field: anl4_totgw_number
dataset: analyst4
best_template: ts_mean
best_sharpe: 1.04
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0706
ann_vol: 0.0592
hit_rate: 0.515
rolling_sharpe_min: -0.48
rolling_sharpe_max: 2.834
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.14
---
# anl4_totgw_number (analyst4)

*Total Goodwill - number of estimations*

## Signal Profile
- `rank(anl4_totgw_number)`: S=0.71, F=0.41, T=3.7%, INFERIOR (TOP500)
- `rank(anl4_totgw_number / close)`: S=0.50, F=0.30, T=3.2%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_totgw_number, 5))`: S=-0.38, F=-0.11, T=37.0%, INFERIOR (TOP3000)
- `-rank(anl4_totgw_number)`: S=-0.70, F=-0.36, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_number, 5))`: S=0.90, F=0.58, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_totgw_number, 63)`: S=0.27, F=0.09, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_totgw_number, 10)`: S=1.04, F=0.72, T=3.0%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_totgw_number, 22))`: S=-0.53, F=-0.27, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_number)`: S=-0.26, F=-0.11, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_number / close)`: S=-0.50, F=-0.30, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.2%
  - 2020: S=1.91 (strong), ret=+11.1%
  - 2021: S=0.53 (moderate), ret=+3.4%
  - 2022: S=-0.29 (negative), ret=-2.1%
  - 2023: S=1.66 (strong), ret=+8.1%

## Risk & Drawdown
- Max drawdown: 7.06% over 485 days (recovered)
- Annualized: return +4.2%, volatility 5.9% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew -0.08, excess kurtosis +1.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.83, latest 1.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.93%; worst month: -3.76%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.08
- Sideways: S=0.41
- Bear: S=0.62

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_totgw_number, 5))` S=0.90, F=0.58, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_totgw_number)`: S=-0.26, F=-0.11, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_totgw_number / close)`: S=-0.50, F=-0.30, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_totgw_number, 5))`: S=0.90, F=0.58, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_totgw_number)` | TOP500 | 0.71 | 0.41 | 7.1% | 80% | all-weather |
| `rank(anl4_totgw_number)` | TOP1000 | 0.71 | 0.36 | 11.1% | 80% | mixed |
| `rank(anl4_totgw_number / close)` | TOP200 | 0.51 | 0.30 | 15.6% | 60% | all-weather |
| `rank(anl4_totgw_number)` | TOP200 | 0.26 | 0.11 | 10.8% | 40% | mixed |
| `rank(anl4_totgw_number / close)` | TOP500 | 0.24 | 0.10 | 20.1% | 40% | mixed |
| `rank(anl4_totgw_number)` | TOP3000 | 0.10 | 0.02 | 8.5% | 80% | weak |

## Correlation Notes
Top correlates:
- anl4_totassets_number: 0.470 (moderately positively correlated)
- anl4_cfi_number: 0.318 (weakly positively correlated)
- min_ebit_guidance: 0.272 (weakly positively correlated)
- operating_profit_max_guidance_qtr: 0.271 (weakly positively correlated)
- anl4_cfo_number: 0.249 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
