---
type: "submit-candidate"
alpha_id: "YP0bLdzA"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.32
fitness: 2.22
turnover: 0.1066
self_corr_max: 0.673
neutralization: "SUBINDUSTRY"
decay: 6
family: "fair_val_liab_event_magnitude_leverage_blend"
session: "20260711-001"
brain_url: "https://platform.worldquantbrain.com/alpha/YP0bLdzA"
queued: "2026-07-11"
---

# Submit YP0bLdzA (Fair-Value-Liability Event-Magnitude + Leverage + Gross-Income-Revision + Investing-Activities Blend)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Why submittable

- All 7 computable BRAIN checks PASS (verified via `/alphas/{id}/check`).
- Grade EXCELLENT, S=2.32, F=2.22, T=10.66%. SUBINDUSTRY, decay=6.
- Max correlation vs the full 44-alpha ACTIVE universe (39 main book + 5 recently
  human-submitted alphas awaiting consolidation from PRs #80-84): **0.673** vs
  `WjGVJ7bN` — comfortably below the 0.70 auto-pass threshold, no Sharpe premium
  needed. Next-highest peer is 0.561 (`d5Q3ZmWv`).
- Uses two genuinely fresh fields never in the book before this session:
  `fn_liab_fair_val_l2_q` (fundamental2, Level-2 fair-value liabilities) and
  `anl4_gric_flag` (analyst4, gross-income revision flag).

## Caveat (read before submitting)

BRAIN's authoritative `/alphas/{id}/check` and `/correlations/self` endpoints
returned `SELF_CORRELATION: PENDING` throughout the discovery session — polling
timed out consistently across 6+ attempts spanning ~90 minutes, including for
control queries against already-ACTIVE alphas, suggesting a general
async-computation lag rather than an issue specific to this candidate. The
0.673 verdict above is from local 4-year daily PnL return correlation, the
standard fallback method. **Recommend a fresh `/alphas/YP0bLdzA/check` poll
immediately before submission** to confirm the authoritative PASS.

## Reviewer action

**Done.** Submitted 2026-07-11; confirmed ACTIVE on BRAIN (all 7 checks PASS).
`data/book/YP0bLdzA.md` flipped to `status: ACTIVE`.
