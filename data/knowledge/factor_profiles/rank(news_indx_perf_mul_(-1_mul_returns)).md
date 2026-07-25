---
field: rank(news_indx_perf * (-1 * returns))
dataset: news12
best_template: unknown
best_sharpe: 0.47
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 1
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.156
ann_vol: 0.0713
hit_rate: 0.5263
rolling_sharpe_min: -1.873
rolling_sharpe_max: 2.516
---
# rank(news_indx_perf * (-1 * returns)) (news12)


## Signal Profile
- No simulation data available

## Check Summary
- HIGH_TURNOVER: 1F/0P
- LOW_FITNESS: 1F/0P
- LOW_SHARPE: 1F/0P

## Temporal Behavior
Headline (unknown): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.36 (moderate), ret=+5.8%
  - 2020: S=0.51 (moderate), ret=+3.2%
  - 2021: S=-0.35 (negative), ret=-2.8%
  - 2022: S=0.72 (moderate), ret=+6.6%
  - 2023: S=0.59 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 15.60% over 1042 days (recovered)
- Annualized: return +3.4%, volatility 7.1% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.76, excess kurtosis +3.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.87, max 2.52, latest 0.56

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +4.17%; worst month: -5.44%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.25
- Sideways: S=1.52
- Bear: S=-1.40

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_indx_perf * (-1 * returns))` | TOP3000 | 0.47 | 0.08 | 15.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfmq_ibcomq: 0.693 (moderately positively correlated)
- income: 0.693 (moderately positively correlated)
- est_eps: 0.691 (moderately positively correlated)
- fnd6_newqv1300_cibegniq: 0.688 (moderately positively correlated)
- anl4_qfv4_eps_high: 0.685 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
