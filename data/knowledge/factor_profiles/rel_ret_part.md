---
field: rel_ret_part
dataset: pv13
best_template: rank_neg_delta
best_sharpe: 0.88
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1762
ann_vol: 0.0769
hit_rate: 0.4955
rolling_sharpe_min: -1.761
rolling_sharpe_max: 1.577
negated_best_sharpe: 0.88
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.55
---
# rel_ret_part (pv13)

*Averaged one-day return of the instrument's partners*

## Signal Profile
- `rank(rel_ret_part)`: S=0.14, F=0.02, T=72.5%, INFERIOR (TOP200)
- `rank(rel_ret_part / close)`: S=-0.34, F=-0.05, T=73.0%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_ret_part, 5))`: S=-0.17, F=-0.02, T=78.0%, INFERIOR (TOP200)
- `-rank(rel_ret_part)`: S=0.35, F=0.05, T=73.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_part, 5))`: S=0.88, F=0.16, T=78.6%, INFERIOR (TOP3000)
- `-ts_zscore(rel_ret_part, 63)`: S=0.29, F=0.04, T=71.2%, INFERIOR (TOP3000)
- `ts_mean(rel_ret_part, 10)`: S=0.33, F=0.08, T=23.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_ret_part, 22))`: S=-0.10, F=-0.01, T=73.2%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_part)`: S=0.59, F=0.09, T=73.7%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_part / close)`: S=0.39, F=0.05, T=74.0%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 24F/1P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.73 (negative), ret=-3.5%
  - 2020: S=-1.18 (negative), ret=-7.9%
  - 2021: S=0.58 (moderate), ret=+6.1%
  - 2022: S=1.06 (moderate), ret=+8.7%
  - 2023: S=0.37 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 17.62% over 1078 days (recovered)
- Annualized: return +1.2%, volatility 7.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.20, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 1.58, latest 0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.78%; worst month: -6.50%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.73
- Sideways: S=0.19
- Bear: S=-0.42

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_ret_part, 5))` S=0.88, F=0.16, INFERIOR
Direction gap: +0.55 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rel_ret_part)`: S=0.59, F=0.09, T=73.7%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_part / close)`: S=0.39, F=0.05, T=74.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_part, 5))`: S=0.88, F=0.16, T=78.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_ret_part)` | TOP200 | 0.15 | 0.02 | 17.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- rel_ret_all: 0.319 (weakly positively correlated)
- rel_ret_comp: 0.139 (weakly positively correlated)
- fnd6_recco: -0.123 (weakly negatively correlated)
- research_development_max_guidance: 0.103 (weakly positively correlated)
- min_research_development_expense_guidance_2: 0.103 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
