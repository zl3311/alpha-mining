---
field: anl4_adjusted_netincome_ft
dataset: analyst4
cluster: analyst4_income_earnings
coverage: 0.8706
community_alphas: 43825
best_template: ts_mean
best_sharpe: 1.23
best_fitness: 1.38
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 35
regime_profile: bear-only
n_variations_with_pnl: 9
max_drawdown: 0.1479
ann_vol: 0.0734
hit_rate: 0.5255
rolling_sharpe_min: -1.293
rolling_sharpe_max: 2.375
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.77
---
# anl4_adjusted_netincome_ft (analyst4)

*Adjusted net income - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_adjusted_netincome_ft)`: S=0.76, F=0.51, T=2.8%, INFERIOR (TOP500)
- `rank(anl4_adjusted_netincome_ft / close)`: S=0.28, F=0.14, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_adjusted_netincome_ft, 5))`: S=0.33, F=0.17, T=33.8%, INFERIOR (TOP200)
- `ts_decay_linear(rank(anl4_adjusted_netincome_ft), 5)`: S=0.74, F=0.38, T=2.3%, INFERIOR (TOP3000)
- `-rank(anl4_adjusted_netincome_ft)`: S=-0.35, F=-0.14, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_adjusted_netincome_ft, 5))`: S=0.46, F=0.24, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_adjusted_netincome_ft, 63)`: S=-0.08, F=-0.02, T=17.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_adjusted_netincome_ft, 10)`: S=1.23, F=1.38, T=4.3%, AVERAGE (TOP3000)
- `rank(ts_rank(anl4_adjusted_netincome_ft, 22))`: S=-0.04, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_adjusted_netincome_ft)`: S=-0.35, F=-0.14, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_adjusted_netincome_ft / close)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/22P
- LOW_FITNESS: 34F/1P
- LOW_SHARPE: 35F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.67 (moderate), ret=+3.1%
  - 2020: S=1.09 (moderate), ret=+8.0%
  - 2021: S=0.93 (moderate), ret=+8.1%
  - 2022: S=-1.09 (negative), ret=-8.2%
  - 2023: S=2.25 (strong), ret=+16.1%

## Risk & Drawdown
- Max drawdown: 14.79% over 589 days (recovered)
- Annualized: return +5.5%, volatility 7.3% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.10, excess kurtosis +0.92

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.38, latest 2.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +5.31%; worst month: -7.88%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.62
- Sideways: S=1.44
- Bear: S=1.65

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_adjusted_netincome_ft, 5))` S=0.46, F=0.24, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_adjusted_netincome_ft)`: S=-0.35, F=-0.14, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_adjusted_netincome_ft / close)`: S=-0.06, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_adjusted_netincome_ft, 5))`: S=0.46, F=0.24, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_adjusted_netincome_ft)` | TOP500 | 0.75 | 0.51 | 14.8% | 80% | bear-only |
| `ts_decay_linear(rank(anl4_adjusted_netincome_ft), 5)` | TOP3000 | 0.74 | 0.38 | 10.1% | 80% | bear-only |
| `rank(anl4_adjusted_netincome_ft)` | TOP3000 | 0.72 | 0.36 | 10.1% | 80% | bear-only |
| `rank(ts_delta(anl4_adjusted_netincome_ft, 5))` | TOP200 | 0.33 | 0.17 | 37.8% | 40% | bull-only |
| `rank(anl4_adjusted_netincome_ft / close)` | TOP200 | 0.29 | 0.14 | 19.6% | 100% | mixed |
| `rank(anl4_adjusted_netincome_ft)` | TOP1000 | 0.36 | 0.14 | 16.5% | 40% | bear-only |
| `rank(anl4_adjusted_netincome_ft)` | TOP200 | 0.27 | 0.13 | 33.0% | 60% | bear-only |
| `rank(ts_delta(anl4_adjusted_netincome_ft, 5))` | TOP500 | 0.27 | 0.13 | 58.1% | 40% | weak |
| `rank(anl4_adjusted_netincome_ft / close)` | TOP500 | 0.09 | 0.02 | 32.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_epsr_flag: 0.560 (moderately positively correlated)
- earnings_per_share_average: -0.475 (moderately negatively correlated)
- anl4_qf_az_eps_mean: -0.475 (moderately negatively correlated)
- anl4_qfd1_azeps: -0.473 (moderately negatively correlated)
- anl4_qf_az_eps: -0.473 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
