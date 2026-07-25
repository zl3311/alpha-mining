---
field: rp_ess_partner
dataset: news18
best_template: rank_delta
best_sharpe: 0.59
best_fitness: 0.14
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1706
ann_vol: 0.1179
hit_rate: 0.4955
rolling_sharpe_min: -1.493
rolling_sharpe_max: 1.797
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.24
---
# rp_ess_partner (news18)

*Event sentiment score of partnership news*

## Signal Profile
- `rank(rp_ess_partner)`: S=0.17, F=0.02, T=110.5%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_partner, 5))`: S=0.59, F=0.14, T=127.6%, INFERIOR (TOP200)
- `-rank(rp_ess_partner)`: S=-0.01, F=0.00, T=128.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_partner, 5))`: S=0.23, F=0.03, T=139.7%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_partner, 63)`: S=0.29, F=0.06, T=100.0%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_partner, 10)`: S=0.27, F=0.11, T=25.8%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_partner, 22))`: S=0.39, F=0.06, T=138.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_partner)`: S=0.35, F=0.05, T=138.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_partner / close)`: S=0.26, F=0.04, T=124.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/3P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.82 (moderate), ret=+8.4%
  - 2020: S=-0.38 (negative), ret=-5.0%
  - 2021: S=0.10 (weak), ret=+1.1%
  - 2022: S=1.67 (strong), ret=+22.1%
  - 2023: S=0.78 (moderate), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 17.06% over 750 days (recovered)
- Annualized: return +6.9%, volatility 11.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.29, excess kurtosis +2.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 1.80, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.88%; worst month: -9.28%
Positive months: 49%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.77
- Sideways: S=0.02
- Bear: S=0.96

## Negated Direction
Best negated: `rank(-1 * rp_ess_partner)` S=0.35, F=0.05, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_partner)`: S=0.35, F=0.05, T=138.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_partner / close)`: S=0.26, F=0.04, T=124.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_partner, 5))`: S=0.23, F=0.03, T=139.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_partner, 5))` | TOP200 | 0.59 | 0.14 | 17.1% | 80% | all-weather |
| `rank(ts_delta(rp_ess_partner, 5))` | TOP500 | 0.36 | 0.06 | 24.9% | 80% | mixed |
| `rank(rp_ess_partner)` | TOP200 | 0.17 | 0.02 | 26.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- pcr_oi_150: 0.109 (weakly positively correlated)
- news_tot_ticks: 0.092 (weakly positively correlated)
- fnd6_ivao: -0.091 (weakly negatively correlated)
- fnd6_currencyqv1300_curcd: 0.089 (weakly positively correlated)
- anl4_netprofita_number: 0.089 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
