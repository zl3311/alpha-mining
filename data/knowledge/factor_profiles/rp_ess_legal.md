---
field: rp_ess_legal
dataset: news18
best_template: rank_delta
best_sharpe: 0.6
best_fitness: 0.2
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: weak
n_variations_with_pnl: 5
max_drawdown: 0.4055
ann_vol: 0.2582
hit_rate: 0.5134
rolling_sharpe_min: -1.158
rolling_sharpe_max: 1.808
negated_best_sharpe: 0.01
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.59
---
# rp_ess_legal (news18)

*Event sentiment score of legal news*

## Signal Profile
- `rank(rp_ess_legal)`: S=0.40, F=0.09, T=134.8%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_legal, 5))`: S=0.60, F=0.20, T=140.1%, INFERIOR (TOP200)
- `-rank(rp_ess_legal)`: S=0.01, F=0.00, T=144.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_legal, 5))`: S=0.01, F=0.00, T=148.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_legal, 63)`: S=0.09, F=0.01, T=143.1%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_legal, 10)`: S=-0.21, F=-0.05, T=29.4%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_legal, 22))`: S=0.11, F=0.01, T=147.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_legal)`: S=-0.37, F=-0.07, T=146.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_legal / close)`: S=-0.66, F=-0.21, T=135.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.60, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+5.9%
  - 2020: S=1.11 (moderate), ret=+28.8%
  - 2021: S=0.38 (weak), ret=+7.7%
  - 2022: S=0.07 (weak), ret=+2.5%
  - 2023: S=1.47 (moderate), ret=+31.6%

## Risk & Drawdown
- Max drawdown: 40.55% over 210 days (recovered)
- Annualized: return +15.6%, volatility 25.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.24, excess kurtosis +11.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 1.81, latest 1.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +17.39%; worst month: -14.24%
Positive months: 58%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.06
- Sideways: S=1.65
- Bear: S=0.33

## Negated Direction
Best negated: `-rank(rp_ess_legal)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_legal)`: S=-0.37, F=-0.07, T=146.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_legal / close)`: S=-0.66, F=-0.21, T=135.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_legal, 5))`: S=0.01, F=0.00, T=148.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_legal, 5))` | TOP200 | 0.60 | 0.20 | 40.6% | 100% | weak |
| `rank(ts_delta(rp_ess_legal, 5))` | TOP500 | 0.49 | 0.15 | 34.1% | 60% | mixed |
| `rank(rp_ess_legal)` | TOP200 | 0.42 | 0.09 | 31.5% | 60% | weak |
| `rank(rp_ess_legal)` | TOP3000 | 0.37 | 0.07 | 21.8% | 60% | mixed |
| `rank(ts_delta(rp_ess_legal, 5))` | TOP1000 | 0.26 | 0.05 | 40.4% | 60% | weak |

## Correlation Notes
Top correlates:
- parkinson_volatility_30: -0.142 (weakly negatively correlated)
- beta_last_60_days_spy: -0.141 (weakly negatively correlated)
- fnd6_recta: -0.132 (weakly negatively correlated)
- anl4_cff_value: -0.127 (weakly negatively correlated)
- financing_cashflow_reported_value: -0.127 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
