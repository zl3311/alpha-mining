---
field: unsystematic_risk_last_60_days
dataset: model51
best_template: rank_ts_rank
best_sharpe: 1.09
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0659
ann_vol: 0.0591
hit_rate: 0.5069
rolling_sharpe_min: -0.75
rolling_sharpe_max: 2.874
top_merge_partner: anl4_afv4_dts_spe
negated_best_sharpe: 0.09
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -1.0
---
# unsystematic_risk_last_60_days (model51)

*The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 60 calendar days*

## Signal Profile
- `rank(unsystematic_risk_last_60_days)`: S=0.32, F=0.19, T=16.4%, INFERIOR (TOP200)
- `rank(unsystematic_risk_last_60_days / close)`: S=0.05, F=0.01, T=12.1%, INFERIOR (TOP3000)
- `rank(ts_delta(unsystematic_risk_last_60_days, 5))`: S=1.02, F=0.34, T=53.9%, INFERIOR (TOP3000)
- `-rank(unsystematic_risk_last_60_days)`: S=-0.04, F=-0.01, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_60_days, 5))`: S=-1.02, F=-0.34, T=53.9%, INFERIOR (TOP3000)
- `ts_zscore(unsystematic_risk_last_60_days, 22)`: S=1.04, F=0.48, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(unsystematic_risk_last_60_days, 10)`: S=-0.12, F=-0.06, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(unsystematic_risk_last_60_days, 22))`: S=1.09, F=0.49, T=32.1%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_60_days)`: S=0.09, F=0.03, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_60_days / close)`: S=0.06, F=0.01, T=14.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.5%
  - 2020: S=0.04 (weak), ret=+0.2%
  - 2021: S=1.30 (moderate), ret=+9.9%
  - 2022: S=2.39 (strong), ret=+17.0%
  - 2023: S=0.39 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 6.59% over 196 days (recovered)
- Annualized: return +6.0%, volatility 5.9% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.49, excess kurtosis +11.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 2.87, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.46%; worst month: -2.59%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.31
- Sideways: S=1.57
- Bear: S=0.22

## Negated Direction
Best negated: `rank(-1 * unsystematic_risk_last_60_days)` S=0.09, F=0.03, INFERIOR
Direction gap: -1.00 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * unsystematic_risk_last_60_days)`: S=0.09, F=0.03, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_60_days / close)`: S=0.06, F=0.01, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_60_days, 5))`: S=-1.02, F=-0.34, T=53.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(unsystematic_risk_last_60_days, 5))` | TOP3000 | 1.01 | 0.34 | 6.6% | 100% | mixed |
| `rank(ts_delta(unsystematic_risk_last_60_days, 5))` | TOP1000 | 0.91 | 0.34 | 10.7% | 60% | bull-only |
| `rank(unsystematic_risk_last_60_days)` | TOP200 | 0.33 | 0.19 | 53.7% | 60% | bear-only |
| `rank(ts_delta(unsystematic_risk_last_60_days, 5))` | TOP500 | 0.41 | 0.11 | 19.6% | 60% | bull-only |
| `rank(unsystematic_risk_last_60_days)` | TOP500 | 0.12 | 0.04 | 58.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- unsystematic_risk_last_90_days: 0.668 (moderately positively correlated)
- unsystematic_risk_last_360_days: 0.499 (moderately positively correlated)
- implied_volatility_put_60: 0.428 (moderately positively correlated)
- correlation_last_60_days_spy: -0.417 (moderately negatively correlated)
- implied_volatility_mean_120: 0.414 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.13 | 1.47 | +0.46 | -0.54 | yes |
| fnd6_fopo | fundamental6 | -0.01 | 1.48 | +0.40 | -0.84 | yes |
| fn_derivative_notional_amount_q | fundamental2 | -0.05 | 1.47 | +0.43 | -0.50 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.03 | 1.42 | +0.40 | -0.69 | yes |
| sharesout | pv1 | -0.04 | 1.41 | +0.37 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
