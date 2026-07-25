---
field: anl4_qfv4_div_mean
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1521
ann_vol: 0.0697
hit_rate: 0.5142
rolling_sharpe_min: -2.279
rolling_sharpe_max: 2.18
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.09
---
# anl4_qfv4_div_mean (analyst4)

*Dividend per share - mean of estimations*

## Signal Profile
- `rank(anl4_qfv4_div_mean)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qfv4_div_mean / close)`: S=0.47, F=0.26, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfv4_div_mean, 5))`: S=0.48, F=0.15, T=35.1%, INFERIOR (TOP500)
- `-rank(anl4_qfv4_div_mean)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_mean, 5))`: S=-0.13, F=-0.03, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfv4_div_mean, 22)`: S=0.34, F=0.10, T=32.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfv4_div_mean, 10)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfv4_div_mean, 22))`: S=0.39, F=0.13, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_mean)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_mean / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.93 (negative), ret=-5.5%
  - 2020: S=-0.04 (negative), ret=-0.3%
  - 2021: S=1.72 (strong), ret=+11.5%
  - 2022: S=-0.24 (negative), ret=-1.7%
  - 2023: S=1.53 (strong), ret=+12.7%

## Risk & Drawdown
- Max drawdown: 15.21% over 764 days (recovered)
- Annualized: return +3.4%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +1.63, excess kurtosis +18.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.28, max 2.18, latest 1.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.77%; worst month: -4.26%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.48
- Sideways: S=0.38
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * anl4_qfv4_div_mean / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfv4_div_mean)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfv4_div_mean / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfv4_div_mean, 5))`: S=-0.13, F=-0.03, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_qfv4_div_mean, 5))` | TOP500 | 0.49 | 0.15 | 15.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- est_dividend_ps: 0.991 (strongly positively correlated)
- rp_ess_credit_ratings: 0.298 (weakly positively correlated)
- anl4_qf_az_hgih_vid: 0.292 (weakly positively correlated)
- anl4_qfd1_az_hgih_vid: 0.292 (weakly positively correlated)
- anl4_afv4_div_low: 0.260 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
