---
field: est_dividend_ps
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.1619
ann_vol: 0.0693
hit_rate: 0.5174
rolling_sharpe_min: -2.522
rolling_sharpe_max: 2.114
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.09
---
# est_dividend_ps (analyst4)

*Dividend per share - average of estimations*

## Signal Profile
- `rank(est_dividend_ps)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(est_dividend_ps / close)`: S=0.47, F=0.26, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(est_dividend_ps, 5))`: S=0.45, F=0.13, T=35.1%, INFERIOR (TOP500)
- `-rank(est_dividend_ps)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_dividend_ps, 5))`: S=-0.17, F=-0.04, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(est_dividend_ps, 22)`: S=0.28, F=0.07, T=32.9%, INFERIOR (TOP3000)
- `ts_mean(est_dividend_ps, 10)`: S=0.08, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(est_dividend_ps, 22))`: S=0.48, F=0.17, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * est_dividend_ps)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * est_dividend_ps / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.74 (negative), ret=-4.3%
  - 2020: S=-0.51 (negative), ret=-3.0%
  - 2021: S=1.75 (strong), ret=+11.6%
  - 2022: S=-0.19 (negative), ret=-1.3%
  - 2023: S=1.51 (strong), ret=+12.6%

## Risk & Drawdown
- Max drawdown: 16.19% over 780 days (recovered)
- Annualized: return +3.2%, volatility 6.9% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +1.59, excess kurtosis +19.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.52, max 2.11, latest 1.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.77%; worst month: -4.26%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.37
- Sideways: S=0.50
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * est_dividend_ps / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * est_dividend_ps)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * est_dividend_ps / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_dividend_ps, 5))`: S=-0.17, F=-0.04, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(est_dividend_ps, 5))` | TOP500 | 0.46 | 0.13 | 16.2% | 40% | mixed |
| `rank(ts_delta(est_dividend_ps, 5))` | TOP3000 | 0.35 | 0.07 | 11.6% | 40% | mixed |
| `rank(ts_delta(est_dividend_ps, 5))` | TOP200 | 0.17 | 0.04 | 22.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_qfv4_div_mean: 0.991 (strongly positively correlated)
- rp_ess_credit_ratings: 0.302 (weakly positively correlated)
- anl4_qf_az_hgih_vid: 0.282 (weakly positively correlated)
- anl4_qfd1_az_hgih_vid: 0.282 (weakly positively correlated)
- anl4_afv4_div_low: 0.245 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
