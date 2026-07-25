---
field: anl4_afv4_div_high
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 1.43
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1544
ann_vol: 0.089
hit_rate: 0.4874
rolling_sharpe_min: -1.564
rolling_sharpe_max: 1.698
negated_best_sharpe: 1.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.62
n_negated_sims: 10
direction_gap: 1.21
---
# anl4_afv4_div_high (analyst4)

*Dividend per share - The highest estimation for the annual forecast.*

## Signal Profile
- `rank(anl4_afv4_div_high)`: S=-0.06, F=-0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_afv4_div_high / close)`: S=0.22, F=0.09, T=1.8%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_div_high, 5))`: S=-0.45, F=-0.10, T=36.7%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_div_high)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_high, 5))`: S=1.43, F=0.62, T=37.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_high, 63)`: S=0.32, F=0.09, T=19.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_high, 10)`: S=-0.08, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_high, 22))`: S=-0.87, F=-0.41, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_high)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_high / close)`: S=-0.22, F=-0.09, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.0%
  - 2020: S=-1.10 (negative), ret=-8.1%
  - 2021: S=0.58 (moderate), ret=+6.3%
  - 2022: S=1.47 (moderate), ret=+17.5%
  - 2023: S=-1.12 (negative), ret=-7.5%

## Risk & Drawdown
- Max drawdown: 15.44% over 568 days (recovered)
- Annualized: return +1.9%, volatility 8.9% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.17, excess kurtosis +2.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.56, max 1.70, latest -1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +8.05%; worst month: -4.90%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.55
- Sideways: S=-0.07
- Bear: S=-2.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_div_high, 5))` S=1.43, F=0.62, INFERIOR
Direction gap: +1.21 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_afv4_div_high)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_high / close)`: S=-0.22, F=-0.09, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_high, 5))`: S=1.43, F=0.62, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_div_high / close)` | TOP1000 | 0.21 | 0.09 | 15.4% | 60% | bull-only |
| `rank(anl4_afv4_div_high / close)` | TOP500 | 0.11 | 0.04 | 20.0% | 40% | bull-only |
| `rank(anl4_afv4_div_high / close)` | TOP3000 | 0.09 | 0.03 | 19.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_div_median: 0.998 (strongly positively correlated)
- anl4_afv4_div_mean: 0.997 (strongly positively correlated)
- anl4_af_div_value: 0.945 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.932 (strongly positively correlated)
- cashflow_dividends: 0.931 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
