---
field: rp_nip_technical
dataset: news18
best_template: ts_zscore
best_sharpe: 0.63
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.2956
ann_vol: 0.1694
hit_rate: 0.1636
rolling_sharpe_min: -1.909
rolling_sharpe_max: 1.908
negated_best_sharpe: 0.53
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 4
direction_gap: -0.1
---
# rp_nip_technical (news18)

*News impact projection based on technical analysis*

## Signal Profile
- `rank(rp_nip_technical)`: S=0.38, F=0.15, T=39.4%, INFERIOR (TOP1000)
- `rank(rp_nip_technical / close)`: S=-0.02, F=0.00, T=47.5%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-rank(rp_nip_technical)`: S=-0.38, F=-0.15, T=39.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_zscore(rp_nip_technical, 22)`: S=0.63, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_technical, 10)`: S=-0.29, F=-0.13, T=45.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_technical, 22))`: S=0.38, F=0.25, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_technical)`: S=0.12, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_technical / close)`: S=0.53, F=0.22, T=81.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 3F/18P
- LOW_FITNESS: 14F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/8P
- LOW_TURNOVER: 7F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.37, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.58 (negative), ret=-13.5%
  - 2020: S=1.77 (strong), ret=+23.5%
  - 2021: S=1.08 (moderate), ret=+18.4%
  - 2022: S=-0.76 (negative), ret=-10.9%
  - 2023: S=0.99 (moderate), ret=+13.2%

## Risk & Drawdown
- Max drawdown: 29.56% over 595 days (not yet recovered, ongoing at window end)
- Annualized: return +6.3%, volatility 16.9% (fraction of booksize)
- Hit rate: 16.4% positive days
- Tail shape: skew -5.25, excess kurtosis +131.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.91, max 1.91, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +9.57%; worst month: -15.53%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.12
- Sideways: S=-0.61
- Bear: S=1.06

## Negated Direction
Best negated: `rank(-1 * rp_nip_technical / close)` S=0.53, F=0.22, INFERIOR
Direction gap: -0.10 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_nip_technical)`: S=0.12, F=0.03, T=70.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_technical / close)`: S=0.53, F=0.22, T=81.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_technical)` | TOP1000 | 0.37 | 0.15 | 29.6% | 60% | all-weather |
| `rank(rp_nip_technical)` | TOP500 | 0.29 | 0.14 | 21.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- rp_css_technical: -0.331 (weakly negatively correlated)
- rel_ret_part: 0.090 (weakly positively correlated)
- parkinson_volatility_90: 0.087 (weakly positively correlated)
- parkinson_volatility_30: 0.086 (weakly positively correlated)
- pcr_oi_180: 0.083 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
