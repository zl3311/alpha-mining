---
field: rel_ret_comp
dataset: pv13
best_template: rank_neg_delta
best_sharpe: 1.06
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 25
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.154
ann_vol: 0.0882
hit_rate: 0.5093
rolling_sharpe_min: -1.151
rolling_sharpe_max: 2.564
negated_best_sharpe: 1.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.51
---
# rel_ret_comp (pv13)

*Averaged one-day return of the competing companies*

## Signal Profile
- `rank(rel_ret_comp)`: S=0.55, F=0.14, T=72.0%, INFERIOR (TOP200)
- `rank(rel_ret_comp / close)`: S=0.12, F=0.01, T=72.4%, INFERIOR (TOP3000)
- `rank(ts_delta(rel_ret_comp, 5))`: S=0.25, F=0.04, T=76.6%, INFERIOR (TOP200)
- `-rank(rel_ret_comp)`: S=-0.16, F=-0.02, T=71.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_comp, 5))`: S=1.06, F=0.23, T=78.1%, INFERIOR (TOP3000)
- `ts_zscore(rel_ret_comp, 22)`: S=0.43, F=0.07, T=71.1%, INFERIOR (TOP3000)
- `ts_mean(rel_ret_comp, 10)`: S=0.42, F=0.13, T=23.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rel_ret_comp, 22))`: S=-0.05, F=0.00, T=71.8%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_comp)`: S=0.41, F=0.06, T=72.9%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_comp / close)`: S=0.11, F=0.01, T=73.5%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 24F/1P
- LOW_FITNESS: 25F/0P
- LOW_SHARPE: 25F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.44 (strong), ret=+14.2%
  - 2020: S=0.67 (moderate), ret=+5.7%
  - 2021: S=0.86 (moderate), ret=+9.7%
  - 2022: S=-0.34 (negative), ret=-3.4%
  - 2023: S=-0.36 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 15.40% over 778 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 8.8% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.07, excess kurtosis +2.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.56, latest -0.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +6.66%; worst month: -5.43%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.05
- Sideways: S=0.93
- Bear: S=0.86

## Negated Direction
Best negated: `rank(-1 * ts_delta(rel_ret_comp, 5))` S=1.06, F=0.23, INFERIOR
Direction gap: +0.51 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * rel_ret_comp)`: S=0.41, F=0.06, T=72.9%, INFERIOR (TOP3000)
- `rank(-1 * rel_ret_comp / close)`: S=0.11, F=0.01, T=73.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rel_ret_comp, 5))`: S=1.06, F=0.23, T=78.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rel_ret_comp)` | TOP200 | 0.55 | 0.14 | 15.4% | 60% | mixed |
| `rank(ts_delta(rel_ret_comp, 5))` | TOP200 | 0.24 | 0.04 | 21.1% | 80% | weak |

## Correlation Notes
Top correlates:
- rel_ret_all: 0.351 (weakly positively correlated)
- fnd6_recco: -0.189 (weakly negatively correlated)
- fn_comp_options_grants_weighted_avg_a: -0.184 (weakly negatively correlated)
- rel_ret_part: 0.139 (weakly positively correlated)
- fnd6_txpd: -0.137 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
