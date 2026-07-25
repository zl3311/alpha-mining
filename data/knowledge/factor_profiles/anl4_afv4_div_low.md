---
field: anl4_afv4_div_low
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.51
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1083
ann_vol: 0.0705
hit_rate: 0.4858
rolling_sharpe_min: -1.463
rolling_sharpe_max: 1.453
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: 0.06
---
# anl4_afv4_div_low (analyst4)

*Dividend - The lowest estimation for the annual forecast*

## Signal Profile
- `rank(anl4_afv4_div_low)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP1000)
- `rank(anl4_afv4_div_low / close)`: S=0.22, F=0.09, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_div_low, 5))`: S=0.35, F=0.09, T=35.0%, INFERIOR (TOP500)
- `-rank(anl4_afv4_div_low)`: S=0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_low, 5))`: S=0.51, F=0.21, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_low, 63)`: S=0.45, F=0.14, T=20.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_low, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_low, 22))`: S=-0.35, F=-0.11, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_low)`: S=0.16, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_low / close)`: S=0.20, F=0.10, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.33, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.7%
  - 2020: S=1.01 (moderate), ret=+6.5%
  - 2021: S=0.27 (weak), ret=+2.2%
  - 2022: S=-1.14 (negative), ret=-7.9%
  - 2023: S=1.23 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 10.83% over 521 days (recovered)
- Annualized: return +2.3%, volatility 7.0% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.61, excess kurtosis +3.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 1.45, latest 1.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +7.03%; worst month: -3.57%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.98
- Sideways: S=-0.22
- Bear: S=0.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_div_low, 5))` S=0.51, F=0.21, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_div_low)`: S=0.16, F=0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_low / close)`: S=0.20, F=0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_low, 5))`: S=0.51, F=0.21, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_afv4_div_low, 5))` | TOP500 | 0.33 | 0.09 | 10.8% | 80% | mixed |
| `rank(anl4_afv4_div_low / close)` | TOP1000 | 0.21 | 0.09 | 20.5% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_div_low, 5))` | TOP1000 | 0.30 | 0.07 | 7.8% | 40% | mixed |
| `rank(ts_delta(anl4_afv4_div_low, 5))` | TOP3000 | 0.27 | 0.05 | 9.0% | 80% | all-weather |
| `rank(anl4_afv4_div_low / close)` | TOP3000 | 0.11 | 0.04 | 20.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfv4_div_mean: 0.260 (weakly positively correlated)
- est_dividend_ps: 0.245 (weakly positively correlated)
- news_short_interest: -0.160 (weakly negatively correlated)
- fnd6_donr: 0.151 (weakly positively correlated)
- anl4_cff_value: -0.150 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
