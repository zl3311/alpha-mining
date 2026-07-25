---
field: pretax_income_max_guidance_qtr
dataset: analyst4
best_template: rank_level
best_sharpe: 0.84
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1872
ann_vol: 0.082
hit_rate: 0.5045
rolling_sharpe_min: -2.28
rolling_sharpe_max: 3.004
top_merge_partner: news_open_vol
redundancy_cluster: 52
negated_best_sharpe: 0.31
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.53
---
# pretax_income_max_guidance_qtr (analyst4)

*The maximum guidance value for Pretax income.*

## Signal Profile
- `rank(pretax_income_max_guidance_qtr)`: S=0.84, F=0.62, T=0.9%, INFERIOR (TOP3000)
- `rank(pretax_income_max_guidance_qtr / close)`: S=0.11, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pretax_income_max_guidance_qtr, 5))`: S=0.60, F=0.24, T=33.7%, INFERIOR (TOP200)
- `-rank(pretax_income_max_guidance_qtr)`: S=-0.14, F=-0.05, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_max_guidance_qtr, 5))`: S=-0.60, F=-0.24, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(pretax_income_max_guidance_qtr, 63)`: S=0.53, F=0.19, T=22.2%, INFERIOR (TOP3000)
- `ts_mean(pretax_income_max_guidance_qtr, 10)`: S=0.22, F=0.10, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(pretax_income_max_guidance_qtr, 22))`: S=-0.18, F=-0.05, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_max_guidance_qtr)`: S=0.31, F=0.21, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_max_guidance_qtr / close)`: S=0.20, F=0.08, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.64 (negative), ret=-9.7%
  - 2020: S=0.87 (moderate), ret=+8.5%
  - 2021: S=2.03 (strong), ret=+15.9%
  - 2022: S=1.22 (moderate), ret=+11.0%
  - 2023: S=1.22 (moderate), ret=+8.4%

## Risk & Drawdown
- Max drawdown: 18.72% over 737 days (recovered)
- Annualized: return +7.0%, volatility 8.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.40, excess kurtosis +2.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.28, max 3.00, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.62%; worst month: -3.78%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.64
- Sideways: S=0.84
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * pretax_income_max_guidance_qtr)` S=0.31, F=0.21, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pretax_income_max_guidance_qtr)`: S=0.31, F=0.21, T=8.9%, INFERIOR (TOP3000)
- `rank(-1 * pretax_income_max_guidance_qtr / close)`: S=0.20, F=0.08, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pretax_income_max_guidance_qtr, 5))`: S=-0.60, F=-0.24, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pretax_income_max_guidance_qtr)` | TOP3000 | 0.85 | 0.62 | 18.7% | 80% | mixed |
| `rank(pretax_income_max_guidance_qtr)` | TOP500 | 0.35 | 0.27 | 32.3% | 80% | bull-only |
| `rank(ts_delta(pretax_income_max_guidance_qtr, 5))` | TOP200 | 0.62 | 0.24 | 15.1% | 40% | bear-only |
| `rank(pretax_income_max_guidance_qtr)` | TOP1000 | 0.14 | 0.05 | 23.2% | 60% | bull-only |
| `rank(pretax_income_max_guidance_qtr / close)` | TOP3000 | 0.11 | 0.04 | 50.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_pretax_profit_guidance: 1.000 (strongly positively correlated)
- pretax_income_reported_min_guidance_qtr: 0.640 (moderately positively correlated)
- max_reported_pretax_income_guidance: 0.640 (moderately positively correlated)
- max_pretax_profit_guidance: 0.522 (moderately positively correlated)
- min_pretax_profit_guidance_2: 0.521 (moderately positively correlated)

Redundancy cluster #52: 2 similar fields, mean |rho| 1.0 (representative: min_pretax_profit_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.22 | 1.41 | +0.48 | -0.88 | yes |
| fnd6_txtubadjust | fundamental6 | -0.20 | 1.34 | +0.49 | -0.48 | yes |
| systematic_risk_last_60_days | model51 | -0.11 | 1.27 | +0.40 | -0.60 | yes |
| rp_ess_revenue | news18 | -0.13 | 1.31 | +0.42 | -0.34 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.14 | 1.30 | +0.44 | +0.33 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
