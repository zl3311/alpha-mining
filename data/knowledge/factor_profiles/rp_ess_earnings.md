---
field: rp_ess_earnings
dataset: news18
best_template: rank_delta
best_sharpe: 0.46
best_fitness: 0.08
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.1753
ann_vol: 0.0917
hit_rate: 0.5134
rolling_sharpe_min: -1.588
rolling_sharpe_max: 2.178
negated_best_sharpe: -0.07
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.53
---
# rp_ess_earnings (news18)

*Event sentiment score of earnings news*

## Signal Profile
- `rank(rp_ess_earnings)`: S=0.25, F=0.04, T=95.6%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_earnings, 5))`: S=0.46, F=0.08, T=128.4%, INFERIOR (TOP200)
- `-rank(rp_ess_earnings)`: S=-0.29, F=-0.04, T=117.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_earnings, 5))`: S=-0.42, F=-0.05, T=159.8%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_earnings, 63)`: S=-0.16, F=-0.01, T=122.8%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_earnings, 10)`: S=0.22, F=0.07, T=17.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_earnings, 22))`: S=0.15, F=0.01, T=126.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_earnings)`: S=-0.07, F=0.00, T=132.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_earnings / close)`: S=-0.21, F=-0.02, T=134.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/18P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.16 (strong), ret=+17.6%
  - 2020: S=-0.48 (negative), ret=-5.2%
  - 2021: S=1.00 (moderate), ret=+10.1%
  - 2022: S=-0.44 (negative), ret=-3.9%
  - 2023: S=0.35 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 17.53% over 506 days (recovered)
- Annualized: return +4.2%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.08, excess kurtosis +4.10

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.18, latest 0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.61%; worst month: -6.86%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.21
- Sideways: S=1.00
- Bear: S=0.27

## Negated Direction
Best negated: `rank(-1 * rp_ess_earnings)` S=-0.07, F=0.00, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_earnings)`: S=-0.07, F=0.00, T=132.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_earnings / close)`: S=-0.21, F=-0.02, T=134.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_earnings, 5))`: S=-0.42, F=-0.05, T=159.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_earnings, 5))` | TOP200 | 0.46 | 0.08 | 17.5% | 60% | weak |
| `rank(ts_delta(rp_ess_earnings, 5))` | TOP3000 | 0.41 | 0.05 | 13.5% | 80% | weak |
| `rank(rp_ess_earnings)` | TOP1000 | 0.30 | 0.04 | 14.6% | 60% | bull-only |
| `rank(rp_ess_earnings)` | TOP200 | 0.27 | 0.04 | 18.4% | 60% | weak |

## Correlation Notes
Top correlates:
- rp_ess_business: 0.175 (weakly positively correlated)
- rp_nip_equity: 0.119 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_a: 0.114 (weakly positively correlated)
- fnd6_pstkrv: 0.106 (weakly positively correlated)
- fnd6_pstkl: 0.105 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
