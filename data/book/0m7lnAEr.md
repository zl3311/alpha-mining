---
alpha_id: "0m7lnAEr"
name: "volgated_iv_event_breadth_blend"
tags:
  - "options_iv_spread"
  - "event_magnitude"
  - "analyst_revision"
  - "sentiment_breadth"
  - "volatility_regime"
  - "session_20260617-001"
  - "excellent"
submitted: "2026-06-17"
session: "20260617-001"
grade: "EXCELLENT"
sharpe: 2.08
fitness: 2.01
turnover: 0.148
expression: "trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 10)) + rank(fnd6_itci / close) + rank(fnd6_acdo) + rank(anl4_netdebt_flag) + rank(ts_mean(scl12_buzz, 5)) + rank(open / close - 1), 5), ts_std_dev(returns, 20) < 0.01)"
family: "iv_event_breadth_volregime"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.5480
self_corr_peer: "LLR0n261"
self_corr_method: "brain_check_authoritative"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/0m7lnAEr"
---

# Alpha: 0m7lnAEr — Volatility-Gated IV/Event Breadth Blend

## Expression

```
trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 10)) + rank(fnd6_itci / close) + rank(fnd6_acdo) + rank(anl4_netdebt_flag) + rank(ts_mean(scl12_buzz, 5)) + rank(open / close - 1), 5), ts_std_dev(returns, 20) < 0.01)
```

## Mechanism

A six-leg cross-family blend, smoothed with `ts_decay_linear` and traded only in
elevated realized-volatility regimes:

1. **Options-implied skew** (`ts_mean(IV_call_270 - IV_put_270, 10)`): forward
   risk pricing from the long-dated call/put spread.
2. **Tax-credit event value** (`fnd6_itci / close`): the strong event/value anchor.
3. **Discontinued-ops accrual quality** (`fnd6_acdo`).
4. **Analyst net-debt revision** (`anl4_netdebt_flag`).
5. **Social attention breadth** (`ts_mean(scl12_buzz, 5)`): 100%-coverage
   stabilizer (raw level, NOT the banned `buzz * (-1*returns)` reversal driver).
6. **Intraday dislocation** (`open / close - 1`): dense, all-cap breadth term.

## Why submittable (verified 2026-06-17)

- EXCELLENT grade, S=2.08, F=2.01, turnover 14.8%.
- All 8 computable BRAIN checks PASS (authoritative `/check`).
- Authoritative BRAIN SELF_CORRELATION PASS at **0.548** vs `LLR0n261`
  (limit 0.70; no peer exceeds the threshold, so no Sharpe-premium escape needed).

## Discovery path (REFINE)

Originated from sweep gate-passer `e7rwP2wd` (IV270 + itci*2 + acdo + netdebt,
SPECTACULAR S=2.36 F=2.66) which had clean self-corr (0.614) but failed
`LOW_SUB_UNIVERSE_SHARPE` (0.62 vs 1.02). Adding dense breadth legs (buzz,
open/close) lifted sub-universe Sharpe but raised the bar in lockstep with the
higher overall Sharpe. The **volatility-regime gate** (`trade_when ts_std_dev`)
was the key fix: it concentrates exposure into high-volatility periods where the
liquid sub-universe Sharpe is strong, passing `LOW_SUB_UNIVERSE_SHARPE` while
preserving EXCELLENT grade and lowering self-corr (0.61 -> 0.55, fewer trades).

## Self-Correlation Profile

| Book Alpha | Corr |
|------------|------|
| LLR0n261 | 0.548 |
| Jjnr7VOl | 0.416 |
| npWYoqQz | 0.374 |
| xAR9Ybjp | 0.344 |
| vR56vdYd | 0.337 |

## Post-Submission

SUBMITTED 2026-06-17 via `--submit-alpha`. BRAIN returned SELF_CORRELATION PASS
(0.548). Status ACTIVE.
