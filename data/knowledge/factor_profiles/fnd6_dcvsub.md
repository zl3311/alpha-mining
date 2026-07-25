---
field: fnd6_dcvsub
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.16
best_fitness: 1.41
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.2622
ann_vol: 0.0921
hit_rate: 0.4453
rolling_sharpe_min: -2.221
rolling_sharpe_max: 2.544
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 1.41
n_negated_sims: 10
direction_gap: 1.04
---
# fnd6_dcvsub (fundamental6)

*Debt - Subordinated Convertible*

## Signal Profile
- `rank(fnd6_dcvsub)`: S=-0.13, F=-0.06, T=3.5%, INFERIOR (TOP500)
- `rank(fnd6_dcvsub / close)`: S=-0.14, F=-0.06, T=3.5%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_dcvsub, 5))`: S=0.12, F=0.04, T=4.6%, INFERIOR (TOP200)
- `-rank(fnd6_dcvsub)`: S=0.56, F=0.51, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvsub, 5))`: S=1.16, F=1.41, T=9.6%, AVERAGE (TOP3000)
- `-ts_zscore(fnd6_dcvsub, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_dcvsub, 10)`: S=-0.19, F=-0.10, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dcvsub, 22))`: S=-0.69, F=-0.55, T=7.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsub)`: S=0.51, F=0.35, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsub / close)`: S=0.51, F=0.35, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 24F/8P
- LOW_FITNESS: 27F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.12, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.09 (negative), ret=-0.6%
  - 2020: S=-1.45 (negative), ret=-13.3%
  - 2021: S=1.63 (strong), ret=+20.7%
  - 2022: S=-0.27 (negative), ret=-2.5%
  - 2023: S=0.15 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 26.22% over 960 days (recovered)
- Annualized: return +1.1%, volatility 9.2% (fraction of booksize)
- Hit rate: 44.5% positive days
- Tail shape: skew +0.30, excess kurtosis +3.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.22, max 2.54, latest 0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.07%; worst month: -6.49%
Positive months: 47%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.59
- Sideways: S=-0.14
- Bear: S=-1.39

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dcvsub, 5))` S=1.16, F=1.41, AVERAGE
Direction gap: +1.04 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_dcvsub)`: S=0.51, F=0.35, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dcvsub / close)`: S=0.51, F=0.35, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dcvsub, 5))`: S=1.16, F=1.41, T=9.6%, AVERAGE (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dcvsub, 5))` | TOP200 | 0.12 | 0.04 | 26.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_rea: 0.633 (moderately positively correlated)
- fnd6_itcb: 0.489 (moderately positively correlated)
- min_stock_option_expense_guidance: 0.448 (moderately positively correlated)
- stock_option_expense_max_guidance_qtr: 0.448 (moderately positively correlated)
- fnd6_dvpa: 0.431 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
