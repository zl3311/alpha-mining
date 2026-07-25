---
field: rp_nip_inverstor
dataset: news18
cluster: news18_news
coverage: 0.5
community_alphas: 2240
best_template: rank_delta
best_sharpe: 0.36
best_fitness: 0.12
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.4884
ann_vol: 0.3082
hit_rate: 0.3555
rolling_sharpe_min: -1.109
rolling_sharpe_max: 2.011
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 4
direction_gap: 0.02
---
# rp_nip_inverstor (news18)

*News impact projection of investor relations news*

## Signal Profile
- `rank(rp_nip_inverstor)`: S=0.43, F=0.09, T=163.8%, INFERIOR (TOP3000)
- `rank(rp_nip_inverstor / close)`: S=-0.49, F=-0.12, T=159.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_inverstor, 5))`: S=0.36, F=0.12, T=107.3%, INFERIOR (TOP500)
- `-rank(rp_nip_inverstor)`: S=0.41, F=0.09, T=164.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_inverstor, 5))`: S=0.38, F=0.12, T=144.1%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_inverstor, 63)`: S=0.38, F=0.08, T=168.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_inverstor, 10)`: S=-0.15, F=-0.02, T=35.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_inverstor, 22))`: S=-0.66, F=-0.18, T=168.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_inverstor)`: S=-0.43, F=-0.09, T=163.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_inverstor / close)`: S=-0.30, F=-0.05, T=159.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.92 (negative), ret=-23.4%
  - 2020: S=-0.15 (negative), ret=-5.0%
  - 2021: S=0.70 (moderate), ret=+21.0%
  - 2022: S=1.14 (moderate), ret=+40.6%
  - 2023: S=0.91 (moderate), ret=+21.7%

## Risk & Drawdown
- Max drawdown: 48.84% over 1117 days (recovered)
- Annualized: return +11.2%, volatility 30.8% (fraction of booksize)
- Hit rate: 35.5% positive days
- Tail shape: skew +0.14, excess kurtosis +19.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.01, latest 0.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +17.83%; worst month: -12.55%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.02
- Sideways: S=-0.53
- Bear: S=0.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_inverstor, 5))` S=0.38, F=0.12, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_inverstor)`: S=-0.43, F=-0.09, T=163.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_inverstor / close)`: S=-0.30, F=-0.05, T=159.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_inverstor, 5))`: S=0.38, F=0.12, T=144.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_inverstor, 5))` | TOP500 | 0.36 | 0.12 | 48.8% | 60% | mixed |
| `rank(rp_nip_inverstor)` | TOP3000 | 0.43 | 0.09 | 31.4% | 60% | bull-only |
| `rank(ts_delta(rp_nip_inverstor, 5))` | TOP200 | 0.11 | 0.02 | 58.1% | 40% | weak |
| `rank(rp_nip_inverstor)` | TOP500 | 0.16 | 0.02 | 33.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cisecgl: 0.127 (weakly positively correlated)
- news_vol_stddev: 0.126 (weakly positively correlated)
- fnd6_fiao: 0.124 (weakly positively correlated)
- fnd6_newa2v1300_reuna: -0.118 (weakly negatively correlated)
- fnd6_newa2v1300_re: -0.118 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
