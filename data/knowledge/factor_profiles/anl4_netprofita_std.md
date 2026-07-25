---
field: anl4_netprofita_std
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.88
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0949
ann_vol: 0.0502
hit_rate: 0.5223
rolling_sharpe_min: -1.354
rolling_sharpe_max: 3.182
top_merge_partner: fn_derivative_notional_amount_a
negated_best_sharpe: -0.38
negated_best_template: neg_rank
negated_best_fitness: -0.16
n_negated_sims: 4
direction_gap: -1.26
---
# anl4_netprofita_std (analyst4)

*Adjusted net income - std of estimations*

## Signal Profile
- `rank(anl4_netprofita_std)`: S=0.55, F=0.27, T=4.5%, INFERIOR (TOP3000)
- `rank(anl4_netprofita_std / close)`: S=0.46, F=0.22, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_netprofita_std, 5))`: S=0.91, F=0.31, T=39.2%, INFERIOR (TOP1000)
- `-rank(anl4_netprofita_std)`: S=-0.38, F=-0.16, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_std, 5))`: S=-0.72, F=-0.19, T=39.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_netprofita_std, 22)`: S=0.88, F=0.34, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_netprofita_std, 10)`: S=0.33, F=0.18, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_netprofita_std, 22))`: S=0.56, F=0.20, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_std)`: S=-0.55, F=-0.27, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_std / close)`: S=-0.46, F=-0.22, T=4.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/25P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.44 (weak), ret=+1.9%
  - 2020: S=-1.04 (negative), ret=-5.1%
  - 2021: S=2.13 (strong), ret=+10.9%
  - 2022: S=0.45 (weak), ret=+2.6%
  - 2023: S=2.66 (strong), ret=+11.7%

## Risk & Drawdown
- Max drawdown: 9.49% over 526 days (recovered)
- Annualized: return +4.5%, volatility 5.0% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew -0.16, excess kurtosis +1.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.35, max 3.18, latest 2.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +4.01%; worst month: -4.07%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.12
- Sideways: S=1.17
- Bear: S=0.34

## Negated Direction
Best negated: `-rank(anl4_netprofita_std)` S=-0.38, F=-0.16, INFERIOR
Direction gap: -1.26 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_netprofita_std)`: S=-0.55, F=-0.27, T=4.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_netprofita_std / close)`: S=-0.46, F=-0.22, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_netprofita_std, 5))`: S=-0.72, F=-0.19, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_netprofita_std, 5))` | TOP1000 | 0.89 | 0.31 | 9.5% | 80% | mixed |
| `rank(anl4_netprofita_std)` | TOP3000 | 0.55 | 0.27 | 13.0% | 80% | bull-only |
| `rank(ts_delta(anl4_netprofita_std, 5))` | TOP500 | 0.66 | 0.24 | 9.1% | 60% | weak |
| `rank(anl4_netprofita_std / close)` | TOP3000 | 0.45 | 0.22 | 8.3% | 100% | all-weather |
| `rank(anl4_netprofita_std / close)` | TOP1000 | 0.42 | 0.20 | 12.1% | 80% | mixed |
| `rank(ts_delta(anl4_netprofita_std, 5))` | TOP3000 | 0.71 | 0.19 | 8.7% | 60% | mixed |
| `rank(anl4_netprofita_std / close)` | TOP500 | 0.36 | 0.17 | 17.2% | 60% | bull-only |
| `rank(anl4_netprofita_std)` | TOP1000 | 0.38 | 0.16 | 14.4% | 80% | bull-only |
| `rank(anl4_netprofita_std)` | TOP500 | 0.29 | 0.12 | 22.5% | 80% | bull-only |
| `rank(ts_delta(anl4_netprofita_std, 5))` | TOP200 | 0.34 | 0.11 | 22.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_credit_ratings: -0.121 (weakly negatively correlated)
- rank(fnd6_acdo) * rank(volume/adv20): 0.114 (weakly positively correlated)
- earnings_per_share_minimum: -0.111 (weakly negatively correlated)
- earnings_per_share_median_value: -0.103 (weakly negatively correlated)
- historical_volatility_20: 0.097 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_derivative_notional_amount_a | fundamental2 | -0.01 | 1.28 | +0.37 | -0.79 | yes |
| fnd6_newqv1300_miiq | fundamental6 | -0.02 | 1.24 | +0.35 | -0.96 | yes |
| fn_treasury_stock_shares_a | fundamental2 | -0.06 | 1.29 | +0.39 | -0.42 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.03 | 1.27 | +0.38 | -0.45 | yes |
| fn_treasury_stock_shares_q | fundamental2 | -0.05 | 1.28 | +0.39 | -0.32 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
