---
type: "submit-candidate"
alpha_id: "O0Z6NE0b"
status: "SUBMITTED"
submitted: "2026-07-14"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.10
fitness: 2.02
turnover: 0.127
self_corr_max: 0.528
self_corr_method: "local_pnl_correlation (BRAIN /check PENDING, see caveat)"
self_corr_verdict: "SAFE (local estimate)"
neutralization: "MARKET"
decay: 6
family: "msaq_event_magnitude_market_neutral"
session: "20260713-001"
brain_url: "https://platform.worldquantbrain.com/alpha/O0Z6NE0b"
queued: "2026-07-13"
long_term_value: "MEDIUM"
---

# Submit O0Z6NE0b (msaq event-magnitude, market-neutral)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`

## Why submittable

- All 7 computable BRAIN checks PASS (`scripts/brain_check.py`).
- Local PnL self-corr 0.528 vs the 46-alpha ACTIVE book — comfortably below the
  0.70 threshold. BRAIN's authoritative `SELF_CORRELATION` sub-check was
  `PENDING` throughout the session (known platform latency, see
  `data/book/O0Z6NE0b.md` caveat), so a fresh `/check` poll was recommended
  before submitting. That is now moot: submitted 2026-07-14 and ACTIVE.
- Grade EXCELLENT, S=2.10, F=2.02, T=12.7%.
- Uses two never-before-used building blocks (`fnd6_newqv1300_msaq`,
  `anl4_ffo_flag`) and escapes the now-saturated event-magnitude family's
  `leverage + ivaco + buzz` skeleton via MARKET neutralization instead of the
  family's default SUBINDUSTRY — a genuinely new decorrelation lever for this
  family (see `data/knowledge/patterns/market-neutral-event-magnitude-escape.md`).

## Alternative (higher fitness, unverified correlation, not recommended first)

The identical expression under SUBINDUSTRY neutralization (`KP9V7YLz`,
EXCELLENT S=2.83 F=2.49) has higher standalone fitness but local self-corr
0.646 (RISKY) against the same family — likely fails the Sharpe premium
escape (top peer Sharpe ~2.6-2.7, requiring candidate S>=~2.9). Not queued;
only pursue if `O0Z6NE0b` is rejected and a higher-risk/higher-reward
alternative is wanted.

## Outcome

Submitted by the human on 2026-07-14. Confirmed **ACTIVE** on BRAIN
(`/alphas/O0Z6NE0b/check`: status ACTIVE, all computable checks PASS). See
`data/book/O0Z6NE0b.md` for the full post-submission record.
