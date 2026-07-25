---
field: implied_volatility_put_120
dataset: option8
best_template: rank_delta
best_sharpe: 1.65
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0517
ann_vol: 0.0516
hit_rate: 0.5287
rolling_sharpe_min: -1.158
rolling_sharpe_max: 3.601
top_merge_partner: current_ratio
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.65
---
# implied_volatility_put_120 (option8)

*At-the-money implied volatility of put options with 120 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_120)`: S=0.27, F=0.19, T=7.0%, INFERIOR (TOP200)
- `rank(implied_volatility_put_120 / close)`: S=0.10, F=0.03, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_120, 5))`: S=1.65, F=0.63, T=57.6%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_120)`: S=-0.12, F=-0.05, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_120, 5))`: S=-1.65, F=-0.63, T=57.6%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_120, 22)`: S=1.04, F=0.50, T=30.1%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_120, 10)`: S=-0.09, F=-0.04, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_120, 22))`: S=1.01, F=0.42, T=32.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_120)`: S=-0.03, F=-0.01, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_120 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+2.9%
  - 2020: S=2.43 (strong), ret=+10.6%
  - 2021: S=1.86 (strong), ret=+11.3%
  - 2022: S=3.23 (strong), ret=+21.8%
  - 2023: S=-1.23 (negative), ret=-4.5%

## Risk & Drawdown
- Max drawdown: 5.17% over 364 days (not yet recovered, ongoing at window end)
- Annualized: return +8.6%, volatility 5.2% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +1.20, excess kurtosis +8.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 3.60, latest -1.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.99%; worst month: -2.10%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.40
- Sideways: S=1.07
- Bear: S=1.33

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_120 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_120)`: S=-0.03, F=-0.01, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_120 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_120, 5))`: S=-1.65, F=-0.63, T=57.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_120, 5))` | TOP3000 | 1.66 | 0.63 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_120, 5))` | TOP1000 | 1.11 | 0.46 | 5.2% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_120, 5))` | TOP500 | 0.93 | 0.38 | 7.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_120, 5))` | TOP200 | 0.78 | 0.35 | 13.2% | 60% | mixed |
| `rank(implied_volatility_put_120)` | TOP200 | 0.28 | 0.19 | 73.7% | 60% | bear-only |
| `rank(implied_volatility_put_120)` | TOP500 | 0.19 | 0.10 | 74.9% | 40% | bear-only |
| `rank(implied_volatility_put_120)` | TOP1000 | 0.13 | 0.05 | 69.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_150: 0.978 (strongly positively correlated)
- implied_volatility_put_90: 0.961 (strongly positively correlated)
- implied_volatility_put_180: 0.945 (strongly positively correlated)
- implied_volatility_mean_120: 0.938 (strongly positively correlated)
- implied_volatility_mean_150: 0.926 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| current_ratio | fundamental6 | -0.05 | 2.27 | +0.61 | +0.25 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.02 | 2.21 | +0.55 | +0.71 | yes |
| fnd6_itci | fundamental_tax_credit | +0.05 | 2.52 | +0.52 | -0.21 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | +0.09 | 2.16 | +0.50 | -0.39 | yes |
| fnd6_ivaco | fundamental_investment | -0.07 | 2.19 | +0.53 | +0.58 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
