---
field: operating_profit_max_guidance_qtr
dataset: analyst4
best_template: rank_level
best_sharpe: 0.92
best_fitness: 0.7
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1562
ann_vol: 0.0783
hit_rate: 0.5223
rolling_sharpe_min: -0.691
rolling_sharpe_max: 3.203
top_merge_partner: fnd2_a_flintasacmamtzcsrld
redundancy_cluster: 41
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.83
---
# operating_profit_max_guidance_qtr (analyst4)

*The maximum guidance value for Earnings Before Interest and Taxes.*

## Signal Profile
- `rank(operating_profit_max_guidance_qtr)`: S=0.92, F=0.70, T=2.1%, INFERIOR (TOP500)
- `rank(operating_profit_max_guidance_qtr / close)`: S=0.23, F=0.10, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(operating_profit_max_guidance_qtr, 5))`: S=0.64, F=0.27, T=33.6%, INFERIOR (TOP200)
- `-rank(operating_profit_max_guidance_qtr)`: S=-0.77, F=-0.48, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_max_guidance_qtr, 5))`: S=0.09, F=0.01, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(operating_profit_max_guidance_qtr, 63)`: S=0.77, F=0.38, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(operating_profit_max_guidance_qtr, 10)`: S=0.82, F=0.54, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_profit_max_guidance_qtr, 22))`: S=-0.11, F=-0.02, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_max_guidance_qtr)`: S=-0.92, F=-0.70, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_max_guidance_qtr / close)`: S=-0.23, F=-0.10, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.94, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+3.9%
  - 2020: S=0.21 (weak), ret=+1.4%
  - 2021: S=2.52 (strong), ret=+24.7%
  - 2022: S=-0.58 (negative), ret=-5.2%
  - 2023: S=1.71 (strong), ret=+11.1%

## Risk & Drawdown
- Max drawdown: 15.62% over 474 days (recovered)
- Annualized: return +7.3%, volatility 7.8% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.06, excess kurtosis +0.70

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.69, max 3.20, latest 1.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +6.18%; worst month: -5.78%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.07
- Sideways: S=1.91
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_profit_max_guidance_qtr, 5))` S=0.09, F=0.01, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * operating_profit_max_guidance_qtr)`: S=-0.92, F=-0.70, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_max_guidance_qtr / close)`: S=-0.23, F=-0.10, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_max_guidance_qtr, 5))`: S=0.09, F=0.01, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_profit_max_guidance_qtr)` | TOP500 | 0.94 | 0.70 | 15.6% | 80% | mixed |
| `rank(operating_profit_max_guidance_qtr)` | TOP3000 | 1.02 | 0.62 | 10.7% | 80% | all-weather |
| `rank(operating_profit_max_guidance_qtr)` | TOP1000 | 0.79 | 0.48 | 10.8% | 100% | mixed |
| `rank(operating_profit_max_guidance_qtr)` | TOP200 | 0.46 | 0.29 | 29.7% | 60% | bear-only |
| `rank(ts_delta(operating_profit_max_guidance_qtr, 5))` | TOP200 | 0.66 | 0.27 | 14.4% | 60% | bear-only |
| `rank(operating_profit_max_guidance_qtr / close)` | TOP500 | 0.23 | 0.10 | 31.7% | 60% | bull-only |
| `rank(operating_profit_max_guidance_qtr / close)` | TOP3000 | 0.16 | 0.06 | 50.0% | 80% | bull-only |
| `rank(operating_profit_max_guidance_qtr / close)` | TOP200 | 0.17 | 0.06 | 32.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- min_ebit_guidance: 0.999 (strongly positively correlated)
- anl4_flag_erbfintax: -0.455 (moderately negatively correlated)
- sales_min_guidance_value: 0.351 (weakly positively correlated)
- correlation_last_360_days_spy: 0.341 (weakly positively correlated)
- fnd2_a_sbcpnargmsptawervl: 0.334 (weakly positively correlated)

Redundancy cluster #41: 2 similar fields, mean |rho| 0.999 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_flintasacmamtzcsrld | fundamental2 | -0.06 | 1.39 | +0.42 | -0.52 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.13 | 1.35 | +0.41 | -0.45 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.07 | 1.30 | +0.37 | -0.82 | yes |
| news_open_vol | news12 | -0.01 | 1.32 | +0.39 | -0.56 | yes |
| fnd2_q_flintasamt1expyfour | fundamental2 | +0.01 | 1.29 | +0.35 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
