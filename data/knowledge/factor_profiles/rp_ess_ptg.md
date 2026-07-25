---
field: rp_ess_ptg
dataset: news18
best_template: rank_delta
best_sharpe: 0.57
best_fitness: 0.1
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1169
ann_vol: 0.0765
hit_rate: 0.519
rolling_sharpe_min: -0.586
rolling_sharpe_max: 2.188
negated_best_sharpe: 0.37
negated_best_template: neg_rank
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.2
---
# rp_ess_ptg (news18)

*Event sentiment score of price target news*

## Signal Profile
- `rank(rp_ess_ptg)`: S=-0.16, F=-0.02, T=130.1%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_ess_ptg, 5))`: S=0.57, F=0.10, T=146.2%, INFERIOR (TOP500)
- `-rank(rp_ess_ptg)`: S=0.37, F=0.07, T=115.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_ptg, 5))`: S=-0.18, F=-0.01, T=159.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_ptg, 63)`: S=0.27, F=0.03, T=117.4%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_ptg, 10)`: S=-0.12, F=-0.04, T=10.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_ptg, 22))`: S=0.25, F=0.02, T=126.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ptg)`: S=0.16, F=0.02, T=130.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ptg / close)`: S=0.01, F=0.00, T=131.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.56 (moderate), ret=+5.4%
  - 2020: S=-0.10 (negative), ret=-0.8%
  - 2021: S=0.81 (moderate), ret=+6.2%
  - 2022: S=1.45 (moderate), ret=+8.8%
  - 2023: S=0.58 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 11.69% over 313 days (recovered)
- Annualized: return +4.5%, volatility 7.6% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +1.48, excess kurtosis +16.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.59, max 2.19, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.69%; worst month: -4.86%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.08
- Sideways: S=-0.36
- Bear: S=0.33

## Negated Direction
Best negated: `-rank(rp_ess_ptg)` S=0.37, F=0.07, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_ptg)`: S=0.16, F=0.02, T=130.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_ptg / close)`: S=0.01, F=0.00, T=131.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_ptg, 5))`: S=-0.18, F=-0.01, T=159.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_ptg, 5))` | TOP500 | 0.59 | 0.10 | 11.7% | 80% | mixed |
| `rank(ts_delta(rp_ess_ptg, 5))` | TOP1000 | 0.58 | 0.09 | 12.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_prsho: 0.227 (weakly positively correlated)
- rp_nip_ptg: 0.160 (weakly positively correlated)
- fnd6_pstkl: 0.128 (weakly positively correlated)
- fnd6_pstkrv: 0.126 (weakly positively correlated)
- rp_nip_equity: 0.122 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
