---
field: fnd6_adesinda_curcd
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.83
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.2024
ann_vol: 0.1029
hit_rate: 0.5279
rolling_sharpe_min: -0.814
rolling_sharpe_max: 2.41
top_merge_partner: max_adjusted_net_profit_guidance
redundancy_cluster: 47
negated_best_sharpe: 0.01
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.82
---
# fnd6_adesinda_curcd (fundamental6)

*ISO Currency Code - Company Annual Market*

## Signal Profile
- `rank(fnd6_adesinda_curcd)`: S=0.83, F=0.69, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_adesinda_curcd / close)`: S=0.35, F=0.19, T=2.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_adesinda_curcd, 5))`: S=0.57, F=0.42, T=4.4%, INFERIOR (TOP3000)
- `-rank(fnd6_adesinda_curcd)`: S=-0.71, F=-0.61, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_adesinda_curcd, 5))`: S=0.02, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_adesinda_curcd, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_adesinda_curcd, 10)`: S=0.69, F=0.59, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_adesinda_curcd, 22))`: S=-0.55, F=-0.51, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_adesinda_curcd)`: S=0.01, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_adesinda_curcd / close)`: S=-0.35, F=-0.19, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 3F/15P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.82, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.50 (weak), ret=+5.5%
  - 2020: S=0.49 (weak), ret=+5.4%
  - 2021: S=0.15 (weak), ret=+1.8%
  - 2022: S=1.80 (strong), ret=+16.1%
  - 2023: S=1.76 (strong), ret=+12.6%

## Risk & Drawdown
- Max drawdown: 20.24% over 571 days (recovered)
- Annualized: return +8.5%, volatility 10.3% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew -0.01, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.81, max 2.41, latest 1.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +4.99%; worst month: -9.32%
Positive months: 71%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.68
- Sideways: S=0.56
- Bear: S=0.39

## Negated Direction
Best negated: `rank(-1 * fnd6_adesinda_curcd)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.82 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_adesinda_curcd)`: S=0.01, F=0.00, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_adesinda_curcd / close)`: S=-0.35, F=-0.19, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_adesinda_curcd, 5))`: S=0.02, F=0.00, T=3.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_adesinda_curcd)` | TOP3000 | 0.82 | 0.69 | 20.2% | 100% | mixed |
| `rank(fnd6_adesinda_curcd)` | TOP1000 | 0.70 | 0.61 | 25.0% | 100% | mixed |
| `rank(ts_delta(fnd6_adesinda_curcd, 5))` | TOP3000 | 0.55 | 0.42 | 28.9% | 60% | bull-only |
| `rank(fnd6_adesinda_curcd)` | TOP500 | 0.42 | 0.38 | 58.1% | 100% | mixed |
| `rank(ts_delta(fnd6_adesinda_curcd, 5))` | TOP500 | 0.50 | 0.37 | 31.5% | 60% | bull-only |
| `rank(fnd6_adesinda_curcd / close)` | TOP200 | 0.36 | 0.19 | 20.0% | 100% | mixed |
| `rank(fnd6_adesinda_curcd / close)` | TOP500 | 0.35 | 0.18 | 25.3% | 80% | bear-only |
| `rank(fnd6_adesinda_curcd / close)` | TOP1000 | 0.20 | 0.08 | 31.9% | 40% | bear-only |
| `rank(ts_delta(fnd6_adesinda_curcd, 5))` | TOP1000 | 0.06 | 0.02 | 36.9% | 20% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_idesindq_curcd: 0.956 (strongly positively correlated)
- implied_volatility_mean_skew_720: 0.255 (weakly positively correlated)
- implied_volatility_mean_skew_1080: 0.252 (weakly positively correlated)
- implied_volatility_mean_skew_360: 0.252 (weakly positively correlated)
- implied_volatility_call_270 - implied_volatility_put_270: 0.247 (weakly positively correlated)

Redundancy cluster #47: 2 similar fields, mean |rho| 0.956 (representative: fnd6_idesindq_curcd). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_profit_guidance | analyst4 | -0.15 | 1.25 | +0.42 | -0.20 | yes |
| news_open_vol | news12 | -0.20 | 1.34 | +0.41 | +0.18 | yes |
| max_adjusted_eps_guidance_2 | analyst4 | -0.09 | 1.20 | +0.38 | -0.29 | yes |
| fnd2_a_sbcpnargmpmtwopsffesip | fundamental2 | -0.12 | 1.26 | +0.40 | +0.42 | yes |
| systematic_risk_last_360_days | model51 | -0.05 | 1.33 | +0.32 | -0.78 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
