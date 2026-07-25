---
field: unsystematic_risk_last_360_days
dataset: model51
cluster: model51_risk_systematic
coverage: 0.937
community_alphas: 10178
best_template: ts_zscore
best_sharpe: 1.37
best_fitness: 0.7
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 23
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0574
ann_vol: 0.0503
hit_rate: 0.5223
rolling_sharpe_min: -0.865
rolling_sharpe_max: 2.909
top_merge_partner: rp_ess_dividends
negated_best_sharpe: 0.06
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -1.31
---
# unsystematic_risk_last_360_days (model51)

*The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 360 calendar days*

## Signal Profile
- `rank(unsystematic_risk_last_360_days)`: S=0.41, F=0.31, T=13.8%, INFERIOR (TOP200)
- `rank(unsystematic_risk_last_360_days / close)`: S=0.04, F=0.01, T=11.2%, INFERIOR (TOP3000)
- `rank(ts_delta(unsystematic_risk_last_360_days, 5))`: S=1.31, F=0.43, T=62.4%, INFERIOR (TOP3000)
- `-rank(unsystematic_risk_last_360_days)`: S=-0.01, F=0.00, T=12.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_360_days, 5))`: S=-1.31, F=-0.43, T=62.4%, INFERIOR (TOP3000)
- `ts_zscore(unsystematic_risk_last_360_days, 22)`: S=1.37, F=0.70, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(unsystematic_risk_last_360_days, 10)`: S=-0.14, F=-0.08, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(unsystematic_risk_last_360_days, 22))`: S=1.38, F=0.65, T=35.6%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_360_days)`: S=0.06, F=0.02, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_360_days / close)`: S=0.00, F=0.00, T=13.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/0P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 19F/4P
- LOW_SUB_UNIVERSE_SHARPE: 8F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.82 (negative), ret=-2.5%
  - 2020: S=1.59 (strong), ret=+7.5%
  - 2021: S=2.10 (strong), ret=+12.0%
  - 2022: S=2.11 (strong), ret=+13.8%
  - 2023: S=0.39 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 5.74% over 461 days (recovered)
- Annualized: return +6.6%, volatility 5.0% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +1.40, excess kurtosis +14.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.86, max 2.91, latest 0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.99%; worst month: -1.97%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.89
- Sideways: S=0.76
- Bear: S=1.14

## Negated Direction
Best negated: `rank(-1 * unsystematic_risk_last_360_days)` S=0.06, F=0.02, INFERIOR
Direction gap: -1.31 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * unsystematic_risk_last_360_days)`: S=0.06, F=0.02, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_360_days / close)`: S=0.00, F=0.00, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_360_days, 5))`: S=-1.31, F=-0.43, T=62.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(unsystematic_risk_last_360_days, 5))` | TOP3000 | 1.31 | 0.43 | 5.7% | 80% | all-weather |
| `rank(ts_delta(unsystematic_risk_last_360_days, 5))` | TOP1000 | 1.02 | 0.36 | 8.3% | 80% | mixed |
| `rank(unsystematic_risk_last_360_days)` | TOP200 | 0.42 | 0.31 | 54.1% | 60% | bear-only |
| `rank(ts_delta(unsystematic_risk_last_360_days, 5))` | TOP200 | 0.75 | 0.30 | 14.9% | 100% | mixed |
| `rank(ts_delta(unsystematic_risk_last_360_days, 5))` | TOP500 | 0.58 | 0.17 | 10.3% | 60% | bull-only |
| `rank(unsystematic_risk_last_360_days)` | TOP500 | 0.18 | 0.08 | 56.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_360: 0.776 (strongly positively correlated)
- implied_volatility_mean_270: 0.776 (strongly positively correlated)
- implied_volatility_mean_180: 0.740 (strongly positively correlated)
- implied_volatility_mean_720: 0.736 (strongly positively correlated)
- implied_volatility_mean_1080: 0.731 (strongly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_dividends | news18 | -0.03 | 1.91 | +0.51 | -0.73 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.04 | 1.91 | +0.46 | -0.41 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.04 | 1.91 | +0.46 | -0.41 | yes |
| max_net_income_guidance | analyst4 | +0.00 | 1.81 | +0.49 | +0.69 | yes |
| min_net_income_guidance | analyst4 | +0.00 | 1.81 | +0.49 | +0.68 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
