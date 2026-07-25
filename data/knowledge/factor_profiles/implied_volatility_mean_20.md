---
field: implied_volatility_mean_20
dataset: option8
best_template: rank_delta
best_sharpe: 1.07
best_fitness: 0.56
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1413
ann_vol: 0.11
hit_rate: 0.5198
rolling_sharpe_min: -0.487
rolling_sharpe_max: 2.828
top_merge_partner: sharesout
redundancy_cluster: 15
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.09
---
# implied_volatility_mean_20 (option8)

*The average of IvCall20 and IvPut20*

## Signal Profile
- `rank(implied_volatility_mean_20)`: S=0.37, F=0.31, T=10.0%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_20 / close)`: S=0.11, F=0.04, T=5.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_20, 5))`: S=1.07, F=0.56, T=42.0%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_20)`: S=-0.16, F=-0.08, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_20, 5))`: S=-1.19, F=-0.39, T=56.0%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_20, 22)`: S=0.99, F=0.47, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_20, 10)`: S=-0.10, F=-0.05, T=5.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_20, 22))`: S=0.89, F=0.36, T=33.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_20)`: S=-0.06, F=-0.02, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_20 / close)`: S=-0.02, F=0.00, T=8.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.07, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+2.5%
  - 2020: S=0.84 (moderate), ret=+7.5%
  - 2021: S=0.81 (moderate), ret=+10.8%
  - 2022: S=2.28 (strong), ret=+32.5%
  - 2023: S=0.49 (weak), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 14.13% over 213 days (recovered)
- Annualized: return +11.8%, volatility 11.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.61, excess kurtosis +4.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.49, max 2.83, latest 0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.00%; worst month: -5.98%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.66
- Sideways: S=0.79
- Bear: S=0.62

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_20 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.09 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_20)`: S=-0.06, F=-0.02, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_20 / close)`: S=-0.02, F=0.00, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_20, 5))`: S=-1.19, F=-0.39, T=56.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_20, 5))` | TOP200 | 1.07 | 0.56 | 14.1% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_mean_20, 5))` | TOP1000 | 1.22 | 0.54 | 8.3% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_mean_20, 5))` | TOP3000 | 1.20 | 0.39 | 4.9% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_20, 5))` | TOP500 | 0.84 | 0.33 | 11.5% | 80% | mixed |
| `rank(implied_volatility_mean_20)` | TOP200 | 0.38 | 0.31 | 72.5% | 60% | bear-only |
| `rank(implied_volatility_mean_20)` | TOP500 | 0.24 | 0.14 | 74.7% | 60% | bear-only |
| `rank(implied_volatility_mean_20)` | TOP1000 | 0.17 | 0.08 | 68.1% | 40% | bear-only |
| `rank(implied_volatility_mean_20)` | TOP3000 | 0.07 | 0.02 | 71.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_20: 0.985 (strongly positively correlated)
- implied_volatility_mean_10: 0.782 (strongly positively correlated)
- implied_volatility_put_10: 0.781 (strongly positively correlated)
- implied_volatility_call_10: 0.767 (strongly positively correlated)
- implied_volatility_call_20: 0.653 (moderately positively correlated)

Redundancy cluster #15: 5 similar fields, mean |rho| 0.853 (representative: implied_volatility_put_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| sharesout | pv1 | -0.06 | 1.53 | +0.46 | -0.91 | yes |
| news_mins_4_chg | news12 | -0.04 | 1.55 | +0.47 | -0.51 | yes |
| fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q | fundamental2 | -0.06 | 1.62 | +0.47 | -0.23 | yes |
| sales_ps | fundamental_value | -0.05 | 1.55 | +0.48 | +0.60 | yes |
| fnd6_cld4 | fundamental6 | -0.02 | 1.56 | +0.45 | -0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
