---
field: anl4_cff_low
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.9
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.4516
ann_vol: 0.1536
hit_rate: 0.5069
rolling_sharpe_min: -1.57
rolling_sharpe_max: 2.931
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.65
---
# anl4_cff_low (analyst4)

*Cash Flow From Financing - The lowest estimation*

## Signal Profile
- `rank(anl4_cff_low)`: S=0.10, F=0.04, T=2.8%, INFERIOR (TOP200)
- `rank(anl4_cff_low / close)`: S=0.13, F=0.05, T=2.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_low, 5))`: S=-0.29, F=-0.06, T=37.2%, INFERIOR (TOP3000)
- `-rank(anl4_cff_low)`: S=0.13, F=0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_low, 5))`: S=0.90, F=0.37, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cff_low, 63)`: S=0.25, F=0.07, T=18.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_low, 10)`: S=-0.25, F=-0.12, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_low, 22))`: S=-1.26, F=-0.81, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_low)`: S=0.13, F=0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_low / close)`: S=0.15, F=0.05, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.14, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.54 (moderate), ret=+5.6%
  - 2020: S=2.04 (strong), ret=+24.3%
  - 2021: S=-0.26 (negative), ret=-4.9%
  - 2022: S=-1.03 (negative), ret=-21.6%
  - 2023: S=0.71 (moderate), ret=+6.8%

## Risk & Drawdown
- Max drawdown: 45.16% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +2.1%, volatility 15.4% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.20, excess kurtosis +3.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.93, latest 0.73

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.53%; worst month: -11.94%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.53
- Sideways: S=0.40
- Bear: S=2.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cff_low, 5))` S=0.90, F=0.37, INFERIOR
Direction gap: +0.65 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * anl4_cff_low)`: S=0.13, F=0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_low / close)`: S=0.15, F=0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_low, 5))`: S=0.90, F=0.37, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cff_low / close)` | TOP200 | 0.14 | 0.05 | 45.2% | 60% | bear-only |
| `rank(anl4_cff_low)` | TOP200 | 0.11 | 0.04 | 47.5% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cff_median: 0.992 (strongly positively correlated)
- est_cashflow_fin: 0.946 (strongly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: 0.818 (strongly positively correlated)
- anl4_cff_value: 0.795 (strongly positively correlated)
- financing_cashflow_reported_value: 0.795 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
