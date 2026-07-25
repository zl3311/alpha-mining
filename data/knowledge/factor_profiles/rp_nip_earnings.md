---
field: rp_nip_earnings
dataset: news18
best_template: rank_neg_delta
best_sharpe: 0.53
best_fitness: 0.07
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.0869
ann_vol: 0.0665
hit_rate: 0.5036
rolling_sharpe_min: -1.513
rolling_sharpe_max: 2.178
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: 0.12
---
# rp_nip_earnings (news18)

*News impact projection of earnings news*

## Signal Profile
- `rank(rp_nip_earnings)`: S=0.04, F=0.00, T=111.5%, INFERIOR (TOP500)
- `rank(rp_nip_earnings / close)`: S=-0.14, F=-0.01, T=112.8%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_earnings, 5))`: S=0.41, F=0.06, T=142.3%, INFERIOR (TOP500)
- `-rank(rp_nip_earnings)`: S=0.13, F=0.01, T=121.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_earnings, 5))`: S=0.53, F=0.07, T=163.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_earnings, 63)`: S=0.34, F=0.04, T=129.8%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_earnings, 10)`: S=-0.12, F=-0.02, T=18.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_earnings, 22))`: S=-0.26, F=-0.02, T=131.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_earnings)`: S=0.16, F=0.01, T=139.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_earnings / close)`: S=0.23, F=0.03, T=132.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/19P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.41, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+3.0%
  - 2020: S=0.36 (weak), ret=+2.6%
  - 2021: S=0.46 (weak), ret=+3.3%
  - 2022: S=1.67 (strong), ret=+10.7%
  - 2023: S=-1.50 (negative), ret=-6.3%

## Risk & Drawdown
- Max drawdown: 8.69% over 331 days (not yet recovered, ongoing at window end)
- Annualized: return +2.7%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.21, excess kurtosis +2.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.18, latest -1.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.37%; worst month: -5.54%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.39
- Sideways: S=-0.87
- Bear: S=0.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_earnings, 5))` S=0.53, F=0.07, INFERIOR
Direction gap: +0.12 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_earnings)`: S=0.16, F=0.01, T=139.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_earnings / close)`: S=0.23, F=0.03, T=132.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_earnings, 5))`: S=0.53, F=0.07, T=163.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_nip_earnings, 5))` | TOP500 | 0.41 | 0.06 | 8.7% | 80% | all-weather |

## Correlation Notes
Top correlates:
- rp_nip_insider: 0.132 (weakly positively correlated)
- rp_ess_mna: 0.108 (weakly positively correlated)
- rp_nip_ptg: 0.098 (weakly positively correlated)
- fnd6_zipcode: -0.096 (weakly negatively correlated)
- max_net_income_guidance: -0.093 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
