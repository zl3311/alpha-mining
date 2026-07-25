---
field: fnd6_prcl
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.86
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2485
ann_vol: 0.1419
hit_rate: 0.4664
rolling_sharpe_min: -0.759
rolling_sharpe_max: 1.32
negated_best_sharpe: 0.86
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.51
---
# fnd6_prcl (fundamental6)

*Price Low - Annual*

## Signal Profile
- `rank(fnd6_prcl)`: S=0.08, F=0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_prcl / close)`: S=0.18, F=0.08, T=4.1%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_prcl, 5))`: S=-0.01, F=0.00, T=33.6%, INFERIOR (TOP3000)
- `-rank(fnd6_prcl)`: S=0.03, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prcl, 5))`: S=0.86, F=0.41, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_prcl, 63)`: S=0.21, F=0.06, T=18.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_prcl, 10)`: S=0.10, F=0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_prcl, 22))`: S=0.35, F=0.14, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcl)`: S=0.32, F=0.17, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcl / close)`: S=0.04, F=0.01, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.16, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+4.6%
  - 2020: S=0.18 (weak), ret=+3.5%
  - 2021: S=-0.15 (negative), ret=-2.4%
  - 2022: S=0.19 (weak), ret=+2.8%
  - 2023: S=0.37 (weak), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 24.85% over 1299 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 14.2% (fraction of booksize)
- Hit rate: 46.6% positive days
- Tail shape: skew +1.04, excess kurtosis +7.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.76, max 1.32, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +7.26%; worst month: -5.80%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.16
- Sideways: S=-0.37
- Bear: S=-0.59

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_prcl, 5))` S=0.86, F=0.41, INFERIOR
Direction gap: +0.51 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_prcl)`: S=0.32, F=0.17, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_prcl / close)`: S=0.04, F=0.01, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_prcl, 5))`: S=0.86, F=0.41, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_prcl / close)` | TOP1000 | 0.16 | 0.08 | 24.9% | 80% | bull-only |
| `rank(fnd6_prcl / close)` | TOP500 | 0.08 | 0.03 | 35.7% | 60% | bull-only |
| `rank(fnd6_prcl)` | TOP3000 | 0.08 | 0.02 | 46.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_prcc: 0.867 (strongly positively correlated)
- fn_oth_comp_fair_value_a: 0.755 (strongly positively correlated)
- fnd6_optprcgr: 0.754 (strongly positively correlated)
- fnd6_newa1v1300_bkvlps: 0.722 (strongly positively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: 0.722 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
