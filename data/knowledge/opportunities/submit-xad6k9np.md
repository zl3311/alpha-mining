---
type: "submit-candidate"
alpha_id: "xAd6K9Np"
status: "SUBMITTED"
priority: "high"
submitted: "2026-07-19"
grade: "EXCELLENT"
sharpe: 1.91
fitness: 2.02
turnover: 0.1199
self_corr_max: 0.6826
neutralization: "SUBINDUSTRY"
decay: 6
family: "accrued_liab_curr_event_magnitude_leverage_blend"
session: "20260718-001"
brain_url: "https://platform.worldquantbrain.com/alpha/xAd6K9Np"
queued: "2026-07-18"
---

# Submit xAd6K9Np (Current Accrued Event-Magnitude + Leverage + IVACO + FCF + Buzz)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_accrued_liab_curr_q / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_ivaco / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Why submittable

- **All 8 BRAIN checks PASS**, including SELF_CORRELATION confirmed
  AUTHORITATIVELY via `/alphas/xAd6K9Np/check`:
  `{result: PASS, value: 0.6826, limit: 0.7}` vs `wpl5eP5v`.
- Grade EXCELLENT, S=1.91, F=2.02, T=12.0%. SUBINDUSTRY, decay=6.
- Uses two fields never in the book: `fn_accrued_liab_curr_q` and `anl4_fcf_flag`.
- Distinct from ACTIVE accrued sibling `ZYpjKeKx` (total accrued + analyst flags);
  corr vs that sibling only ~0.579.

## Caveat

- Self-corr margin is thin (~0.017 under 0.70). Submit sooner rather than later
  if more event-magnitude family members are added to the book first.
- Per long-term submission strategy: EXCELLENT with self-corr < 0.4 is preferred
  for correlation budget; this is still valuable but not "HIGH LONG-TERM VALUE"
  by that bar. Prefer submitting lower-corr PENDING candidates first if any remain.

## Platform URL

https://platform.worldquantbrain.com/alpha/xAd6K9Np
