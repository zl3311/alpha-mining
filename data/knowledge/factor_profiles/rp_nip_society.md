---
field: rp_nip_society
dataset: news18
best_template: ts_zscore
best_sharpe: 0.91
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.3875
ann_vol: 0.1934
hit_rate: 0.5223
rolling_sharpe_min: -1.548
rolling_sharpe_max: 1.642
negated_best_sharpe: 0.33
negated_best_template: neg_rank
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.58
---
# rp_nip_society (news18)

*News impact projection of society-related news*

## Signal Profile
- `rank(rp_nip_society)`: S=0.06, F=0.00, T=136.3%, INFERIOR (TOP200)
- `rank(rp_nip_society / close)`: S=-0.23, F=-0.04, T=128.0%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_society, 5))`: S=0.39, F=0.09, T=151.1%, INFERIOR (TOP500)
- `-rank(rp_nip_society)`: S=0.33, F=0.06, T=147.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_society, 5))`: S=0.21, F=0.03, T=152.4%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_society, 63)`: S=0.91, F=0.25, T=146.8%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_society, 10)`: S=0.34, F=0.09, T=31.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_society, 22))`: S=-0.44, F=-0.08, T=151.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_society)`: S=0.14, F=0.02, T=149.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_society / close)`: S=-0.20, F=-0.04, T=129.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.60 (strong), ret=+29.5%
  - 2020: S=0.88 (moderate), ret=+17.5%
  - 2021: S=-0.83 (negative), ret=-13.5%
  - 2022: S=-0.38 (negative), ret=-8.2%
  - 2023: S=0.77 (moderate), ret=+13.8%

## Risk & Drawdown
- Max drawdown: 38.75% over 1094 days (not yet recovered, ongoing at window end)
- Annualized: return +8.0%, volatility 19.3% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew -0.11, excess kurtosis +8.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.55, max 1.64, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +13.33%; worst month: -10.55%
Positive months: 58%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.15
- Sideways: S=1.07
- Bear: S=0.37

## Negated Direction
Best negated: `-rank(rp_nip_society)` S=0.33, F=0.06, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_nip_society)`: S=0.14, F=0.02, T=149.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_society / close)`: S=-0.20, F=-0.04, T=129.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_society, 5))`: S=0.21, F=0.03, T=152.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_society, 5))` | TOP500 | 0.41 | 0.09 | 38.8% | 60% | weak |

## Correlation Notes
Top correlates:
- rp_nip_legal: 0.229 (weakly positively correlated)
- beta_last_60_days_spy: -0.118 (weakly negatively correlated)
- rp_ess_legal: 0.110 (weakly positively correlated)
- fnd6_txds: -0.103 (weakly negatively correlated)
- systematic_risk_last_60_days: -0.098 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
