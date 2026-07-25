---
alpha_id: "xAd6K9Np"
name: "AccruedCurr EventMag + Lev + IVACO + FCF + Buzz"
status: "ACTIVE"
submitted: "2026-07-19"
grade: "EXCELLENT"
sharpe: 1.91
fitness: 2.02
turnover: 0.1199
returns: 0.1404
family: "accrued_liab_curr_event_magnitude_leverage_blend"
mechanism: "Event-magnitude on current accrued liabilities, blended with leverage premium, investing-activities-other stabilizer, fresh FCF-revision densifier, and buzz-reversal stabilizer"
fields:
  - "fn_accrued_liab_curr_q"
  - "equity"
  - "assets"
  - "fnd6_ivaco"
  - "anl4_fcf_flag"
  - "scl12_buzz"
  - "returns"
expression: "ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
region: "USA"
universe: "TOP3000"
self_corr_max: 0.6826
self_corr_peer: "wpl5eP5v"
self_corr_result: "PASS (AUTHORITATIVE — BRAIN /alphas/xAd6K9Np/check: SELF_CORRELATION {result: PASS, value: 0.6826, limit: 0.7}; local PnL vs-book max 0.683 matched)"
self_corr_method: "brain_api_check_endpoint (authoritative)"
session: "20260718-001"
brain_url: "https://platform.worldquantbrain.com/alpha/xAd6K9Np"
tags:
  - "fn_accrued_liab_curr_q"
  - "anl4_fcf_flag"
  - "event_magnitude"
  - "leverage_premium"
  - "buzz_stabilizer"
  - "session_20260718-001"
---

# xAd6K9Np — Current Accrued Liability Event-Magnitude + Leverage + IVACO + FCF Flag + Buzz

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)
```

## Mechanism

Five-factor blend extending the proven `event-magnitude-abs-ts-delta` template
to a fresh current-accrued anchor, with a never-before-used analyst densifier:

1. **Current accrued event magnitude** (`rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3)))`):
   Large short-horizon absolute changes in *current* accrued liabilities mark
   recognition/settlement events distinct from the total accrued stock already
   claimed by ACTIVE `ZYpjKeKx` (`fn_accrued_liab_q`).
2. **Leverage premium** (`rank(-1 * equity / assets)`).
3. **Investing-activities-other** (`rank(fnd6_ivaco / close)`): proven stabilizer
   in the event-magnitude family.
4. **FCF revision densifier** (`rank(anl4_fcf_flag)`): first book use; raw rank
   as sub-universe densifier / fresh stabilizer per
   `event-magnitude-fresh-stabilizer`.
5. **Buzz reversal** (`rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`).

## Self-Correlation Profile

- Authoritative BRAIN `/check`: PASS **0.6826** (limit 0.7).
- Top peer: `wpl5eP5v` (ppegtq event-magnitude, S=2.09) at ~0.683.
- Other notable: `rKlo39p1` (tlcf) ~0.678, `WjGVJ7bN` ~0.652, accrued sibling
  `ZYpjKeKx` only ~0.579 (stabilizer swap successfully decorrelated from the
  accrued analyst-flag recipe).
- Local PnL vs-book max 0.683 — matches authoritative within 0.001.

## BRAIN Checks

All 8 PASS (LOW_SHARPE, LOW_FITNESS, LOW_TURNOVER, HIGH_TURNOVER,
CONCENTRATED_WEIGHT, LOW_SUB_UNIVERSE_SHARPE 1.25≥0.83, SELF_CORRELATION,
MATCHES_COMPETITION).

## Post-Submission

Submitted by human 2026-07-19. BRAIN confirms `status: ACTIVE`, remaining
computable checks PASS (SELF_CORRELATION omitted on `/alphas/{id}` detail for
submitted alphas; pre-submission authoritative `/check` was PASS 0.6826).
