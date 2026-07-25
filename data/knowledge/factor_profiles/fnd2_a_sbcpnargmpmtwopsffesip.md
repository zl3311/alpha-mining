---
field: fnd2_a_sbcpnargmpmtwopsffesip
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.7
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1506
ann_vol: 0.0934
hit_rate: 0.5215
rolling_sharpe_min: -0.701
rolling_sharpe_max: 2.488
top_merge_partner: reporting_currency_code_9
negated_best_sharpe: 0.06
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.81
---
# fnd2_a_sbcpnargmpmtwopsffesip (fundamental2)

*The number of shares under options that were cancelled during the reporting period as a result of occurrence of a terminating event specified in contractual agreements pertaining to the stock option plan.*

## Signal Profile
- `rank(fnd2_a_sbcpnargmpmtwopsffesip)`: S=0.87, F=0.70, T=1.8%, INFERIOR (TOP200)
- `rank(fnd2_a_sbcpnargmpmtwopsffesip / close)`: S=0.57, F=0.33, T=1.7%, INFERIOR (TOP500)
- `rank(ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))`: S=0.71, F=0.44, T=33.2%, INFERIOR (TOP3000)
- `-rank(fnd2_a_sbcpnargmpmtwopsffesip)`: S=-0.58, F=-0.29, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))`: S=0.06, F=0.02, T=17.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_sbcpnargmpmtwopsffesip, 22)`: S=0.06, F=0.02, T=12.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_sbcpnargmpmtwopsffesip, 10)`: S=0.18, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_sbcpnargmpmtwopsffesip, 22))`: S=0.68, F=0.60, T=16.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmpmtwopsffesip)`: S=-0.87, F=-0.70, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmpmtwopsffesip / close)`: S=-0.52, F=-0.32, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.86, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.27 (negative), ret=-1.8%
  - 2020: S=2.18 (strong), ret=+22.4%
  - 2021: S=-0.17 (negative), ret=-1.8%
  - 2022: S=1.15 (moderate), ret=+11.5%
  - 2023: S=1.39 (moderate), ret=+9.0%

## Risk & Drawdown
- Max drawdown: 15.06% over 360 days (recovered)
- Annualized: return +8.0%, volatility 9.3% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.27, excess kurtosis +2.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.49, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.46%; worst month: -5.09%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.95
- Sideways: S=-0.14
- Bear: S=1.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))` S=0.06, F=0.02, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_sbcpnargmpmtwopsffesip)`: S=-0.87, F=-0.70, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_sbcpnargmpmtwopsffesip / close)`: S=-0.52, F=-0.32, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))`: S=0.06, F=0.02, T=17.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_sbcpnargmpmtwopsffesip)` | TOP200 | 0.86 | 0.70 | 15.1% | 60% | all-weather |
| `rank(ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))` | TOP3000 | 0.72 | 0.44 | 24.1% | 60% | mixed |
| `rank(fnd2_a_sbcpnargmpmtwopsffesip / close)` | TOP500 | 0.55 | 0.33 | 15.7% | 80% | mixed |
| `rank(fnd2_a_sbcpnargmpmtwopsffesip / close)` | TOP200 | 0.51 | 0.32 | 13.8% | 60% | all-weather |
| `rank(fnd2_a_sbcpnargmpmtwopsffesip)` | TOP500 | 0.55 | 0.31 | 12.8% | 60% | mixed |
| `rank(fnd2_a_sbcpnargmpmtwopsffesip / close)` | TOP1000 | 0.52 | 0.29 | 14.7% | 80% | bear-only |
| `rank(fnd2_a_sbcpnargmpmtwopsffesip)` | TOP1000 | 0.58 | 0.29 | 10.0% | 80% | bear-only |
| `rank(ts_delta(fnd2_a_sbcpnargmpmtwopsffesip, 5))` | TOP500 | 0.33 | 0.18 | 67.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_options_forfeitures_and_expirations_a: 0.653 (moderately positively correlated)
- fn_comp_options_grants_a: 0.331 (weakly positively correlated)
- reporting_currency_code_9: -0.297 (weakly negatively correlated)
- fnd6_sstk: 0.269 (weakly positively correlated)
- fn_income_from_equity_investments_a: -0.260 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| reporting_currency_code_9 | analyst4 | -0.30 | 1.37 | +0.51 | -0.69 | yes |
| anl4_tot_gw_ft | analyst4 | -0.25 | 1.53 | +0.49 | -0.84 | yes |
| fnd6_cld4 | fundamental6 | -0.22 | 1.58 | +0.47 | -0.85 | yes |
| fnd6_dn | fundamental6 | -0.18 | 1.36 | +0.47 | -0.80 | yes |
| net_debt_amount | analyst4 | -0.18 | 1.36 | +0.47 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
