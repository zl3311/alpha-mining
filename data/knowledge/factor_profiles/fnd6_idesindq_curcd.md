---
field: fnd6_idesindq_curcd
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.9
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.154
ann_vol: 0.1031
hit_rate: 0.5271
rolling_sharpe_min: -0.473
rolling_sharpe_max: 2.463
top_merge_partner: news_open_vol
redundancy_cluster: 47
negated_best_sharpe: 0.11
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.79
---
# fnd6_idesindq_curcd (fundamental6)

*ISO Currency Code - Company Annual Market*

## Signal Profile
- `rank(fnd6_idesindq_curcd)`: S=0.90, F=0.78, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_idesindq_curcd / close)`: S=0.29, F=0.14, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_idesindq_curcd, 5))`: S=0.49, F=0.35, T=3.5%, INFERIOR (TOP3000)
- `-rank(fnd6_idesindq_curcd)`: S=-0.67, F=-0.57, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_idesindq_curcd, 5))`: S=0.11, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_idesindq_curcd, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_idesindq_curcd, 10)`: S=0.67, F=0.57, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_idesindq_curcd, 22))`: S=-0.08, F=-0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idesindq_curcd)`: S=-0.04, F=-0.01, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idesindq_curcd / close)`: S=-0.29, F=-0.14, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 2F/16P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.89, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+6.8%
  - 2020: S=0.90 (moderate), ret=+9.7%
  - 2021: S=0.00 (weak), ret=+0.0%
  - 2022: S=1.79 (strong), ret=+15.9%
  - 2023: S=1.79 (strong), ret=+12.8%

## Risk & Drawdown
- Max drawdown: 15.40% over 523 days (recovered)
- Annualized: return +9.2%, volatility 10.3% (fraction of booksize)
- Hit rate: 52.7% positive days
- Tail shape: skew -0.10, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.47, max 2.46, latest 1.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +5.07%; worst month: -6.23%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.49
- Sideways: S=0.73
- Bear: S=0.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_idesindq_curcd, 5))` S=0.11, F=0.04, INFERIOR
Direction gap: -0.79 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_idesindq_curcd)`: S=-0.04, F=-0.01, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_idesindq_curcd / close)`: S=-0.29, F=-0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_idesindq_curcd, 5))`: S=0.11, F=0.04, T=3.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_idesindq_curcd)` | TOP3000 | 0.89 | 0.78 | 15.4% | 100% | all-weather |
| `rank(fnd6_idesindq_curcd)` | TOP1000 | 0.67 | 0.57 | 22.5% | 100% | mixed |
| `rank(ts_delta(fnd6_idesindq_curcd, 5))` | TOP3000 | 0.47 | 0.35 | 25.6% | 60% | mixed |
| `rank(fnd6_idesindq_curcd)` | TOP500 | 0.32 | 0.25 | 56.0% | 100% | mixed |
| `rank(ts_delta(fnd6_idesindq_curcd, 5))` | TOP500 | 0.34 | 0.20 | 32.1% | 60% | bull-only |
| `rank(fnd6_idesindq_curcd / close)` | TOP200 | 0.30 | 0.14 | 21.9% | 80% | mixed |
| `rank(fnd6_idesindq_curcd / close)` | TOP500 | 0.25 | 0.11 | 27.6% | 80% | bear-only |
| `rank(fnd6_idesindq_curcd / close)` | TOP1000 | 0.17 | 0.07 | 33.4% | 40% | bear-only |
| `rank(ts_delta(fnd6_idesindq_curcd, 5))` | TOP200 | 0.10 | 0.04 | 30.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_adesinda_curcd: 0.956 (strongly positively correlated)
- cashflow_per_share_min_guidance_quarterly: -0.246 (weakly negatively correlated)
- cashflow_per_share_max_guidance_quarterly: -0.246 (weakly negatively correlated)
- implied_volatility_call_270 - implied_volatility_put_270: 0.229 (weakly positively correlated)
- reporting_currency_code_9: 0.229 (weakly positively correlated)

Redundancy cluster #47: 2 similar fields, mean |rho| 0.956 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.18 | 1.39 | +0.46 | +0.31 | yes |
| systematic_risk_last_360_days | model51 | -0.05 | 1.39 | +0.37 | -0.70 | yes |
| anl4_bvps_value | analyst4 | -0.01 | 1.26 | +0.36 | -0.81 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.13 | 1.38 | +0.44 | +0.28 | yes |
| news_low_exc_stddev | news12 | -0.07 | 1.31 | +0.38 | -0.60 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
