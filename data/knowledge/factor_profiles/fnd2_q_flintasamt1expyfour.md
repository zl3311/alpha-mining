---
field: fnd2_q_flintasamt1expyfour
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.81
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1437
ann_vol: 0.1188
hit_rate: 0.5174
rolling_sharpe_min: -0.91
rolling_sharpe_max: 2.245
top_merge_partner: parkinson_volatility_120
redundancy_cluster: 44
negated_best_sharpe: 0.81
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.79
n_negated_sims: 10
direction_gap: -0.12
---
# fnd2_q_flintasamt1expyfour (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 4th fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_q_flintasamt1expyfour)`: S=0.37, F=0.17, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_q_flintasamt1expyfour / close)`: S=0.46, F=0.22, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_q_flintasamt1expyfour, 5))`: S=0.93, F=0.51, T=36.3%, INFERIOR (TOP3000)
- `-rank(fnd2_q_flintasamt1expyfour)`: S=-0.04, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expyfour, 5))`: S=0.27, F=0.11, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_q_flintasamt1expyfour, 22)`: S=0.65, F=0.47, T=27.1%, INFERIOR (TOP3000)
- `ts_mean(fnd2_q_flintasamt1expyfour, 10)`: S=0.23, F=0.11, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_q_flintasamt1expyfour, 22))`: S=0.74, F=0.51, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expyfour)`: S=0.73, F=0.72, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expyfour / close)`: S=0.81, F=0.79, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.93, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.10 (weak), ret=+1.0%
  - 2020: S=1.92 (strong), ret=+23.5%
  - 2021: S=-0.16 (negative), ret=-2.0%
  - 2022: S=1.75 (strong), ret=+22.5%
  - 2023: S=0.91 (moderate), ret=+9.2%

## Risk & Drawdown
- Max drawdown: 14.37% over 328 days (recovered)
- Annualized: return +11.1%, volatility 11.9% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.84, excess kurtosis +7.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 2.25, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +9.24%; worst month: -6.67%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.53
- Sideways: S=0.62
- Bear: S=1.66

## Negated Direction
Best negated: `rank(-1 * fnd2_q_flintasamt1expyfour / close)` S=0.81, F=0.79, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_q_flintasamt1expyfour)`: S=0.73, F=0.72, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_q_flintasamt1expyfour / close)`: S=0.81, F=0.79, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_q_flintasamt1expyfour, 5))`: S=0.27, F=0.11, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_q_flintasamt1expyfour, 5))` | TOP3000 | 0.93 | 0.51 | 14.4% | 80% | all-weather |
| `rank(fnd2_q_flintasamt1expyfour / close)` | TOP3000 | 0.44 | 0.22 | 9.2% | 80% | mixed |
| `rank(fnd2_q_flintasamt1expyfour)` | TOP3000 | 0.35 | 0.17 | 18.3% | 60% | bull-only |
| `rank(ts_delta(fnd2_q_flintasamt1expyfour, 5))` | TOP1000 | 0.26 | 0.09 | 24.0% | 60% | mixed |
| `rank(fnd2_q_flintasamt1expyfour / close)` | TOP1000 | 0.15 | 0.05 | 17.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_q_flintasamt1expythree: 0.749 (strongly positively correlated)
- fnd2_q_flintasamt1expytwo: 0.676 (moderately positively correlated)
- fn_finite_lived_intangible_assets_net_q: 0.143 (weakly positively correlated)
- rp_nip_credit_ratings: 0.123 (weakly positively correlated)
- pcr_vol_180: 0.105 (weakly positively correlated)

Redundancy cluster #44: 2 similar fields, mean |rho| 0.749 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_120 | option8 | -0.03 | 1.29 | +0.36 | -0.75 | yes |
| fnd6_cld5 | fundamental6 | +0.04 | 1.31 | +0.35 | -0.83 | yes |
| anl4_fcf_median | analyst4 | -0.04 | 1.31 | +0.38 | -0.53 | yes |
| operating_profit_max_guidance_qtr | analyst4 | +0.01 | 1.29 | +0.35 | -0.76 | yes |
| net_debt_amount | analyst4 | -0.05 | 1.30 | +0.37 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
