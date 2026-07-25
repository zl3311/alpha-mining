---
field: unsystematic_risk_last_90_days
dataset: model51
best_template: rank_ts_rank
best_sharpe: 1.13
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0667
ann_vol: 0.0595
hit_rate: 0.5296
rolling_sharpe_min: -0.676
rolling_sharpe_max: 3.192
top_merge_partner: rp_ess_dividends
negated_best_sharpe: 0.1
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -1.03
---
# unsystematic_risk_last_90_days (model51)

*The portion of return variance not explained by SPY (idiosyncratic risk), calculated as 1 minus R² over the last 90 calendar days*

## Signal Profile
- `rank(unsystematic_risk_last_90_days)`: S=0.43, F=0.31, T=15.2%, INFERIOR (TOP200)
- `rank(unsystematic_risk_last_90_days / close)`: S=0.04, F=0.01, T=11.6%, INFERIOR (TOP3000)
- `rank(ts_delta(unsystematic_risk_last_90_days, 5))`: S=1.32, F=0.50, T=54.8%, INFERIOR (TOP3000)
- `-rank(unsystematic_risk_last_90_days)`: S=-0.02, F=0.00, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_90_days, 5))`: S=-1.32, F=-0.50, T=54.8%, INFERIOR (TOP3000)
- `ts_zscore(unsystematic_risk_last_90_days, 22)`: S=0.98, F=0.44, T=30.4%, INFERIOR (TOP3000)
- `ts_mean(unsystematic_risk_last_90_days, 10)`: S=-0.13, F=-0.07, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_rank(unsystematic_risk_last_90_days, 22))`: S=1.13, F=0.51, T=32.7%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_90_days)`: S=0.10, F=0.03, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_90_days / close)`: S=0.06, F=0.01, T=14.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/0P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 21F/2P
- LOW_SUB_UNIVERSE_SHARPE: 5F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.32, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.60 (negative), ret=-2.0%
  - 2020: S=0.79 (moderate), ret=+4.2%
  - 2021: S=2.46 (strong), ret=+20.2%
  - 2022: S=2.02 (strong), ret=+13.5%
  - 2023: S=0.63 (moderate), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 6.67% over 173 days (recovered)
- Annualized: return +7.8%, volatility 5.9% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +0.05, excess kurtosis +6.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.68, max 3.19, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +5.09%; worst month: -2.75%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.75
- Sideways: S=0.90
- Bear: S=1.21

## Negated Direction
Best negated: `rank(-1 * unsystematic_risk_last_90_days)` S=0.10, F=0.03, INFERIOR
Direction gap: -1.03 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * unsystematic_risk_last_90_days)`: S=0.10, F=0.03, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * unsystematic_risk_last_90_days / close)`: S=0.06, F=0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(unsystematic_risk_last_90_days, 5))`: S=-1.32, F=-0.50, T=54.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(unsystematic_risk_last_90_days, 5))` | TOP3000 | 1.32 | 0.50 | 6.7% | 80% | all-weather |
| `rank(ts_delta(unsystematic_risk_last_90_days, 5))` | TOP200 | 0.92 | 0.44 | 10.7% | 80% | all-weather |
| `rank(ts_delta(unsystematic_risk_last_90_days, 5))` | TOP1000 | 1.01 | 0.41 | 7.7% | 80% | mixed |
| `rank(unsystematic_risk_last_90_days)` | TOP200 | 0.43 | 0.31 | 54.7% | 60% | bear-only |
| `rank(ts_delta(unsystematic_risk_last_90_days, 5))` | TOP500 | 0.62 | 0.21 | 12.3% | 60% | mixed |
| `rank(unsystematic_risk_last_90_days)` | TOP500 | 0.19 | 0.08 | 58.2% | 60% | bear-only |

## Correlation Notes
Top correlates:
- unsystematic_risk_last_60_days: 0.668 (moderately positively correlated)
- implied_volatility_mean_90: 0.568 (moderately positively correlated)
- implied_volatility_mean_120: 0.554 (moderately positively correlated)
- implied_volatility_mean_60: 0.549 (moderately positively correlated)
- unsystematic_risk_last_360_days: 0.547 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_dividends | news18 | -0.02 | 1.93 | +0.53 | -0.81 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.12 | 2.20 | +0.58 | -0.11 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.02 | 1.94 | +0.49 | -0.65 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.02 | 1.94 | +0.49 | -0.65 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.14 | 1.84 | +0.52 | -0.15 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
