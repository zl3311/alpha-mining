---
type: "submit-candidate"
alpha_id: "rKlo39p1"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.13
fitness: 2.22
turnover: 0.1071
self_corr_max: 0.6262
self_corr_method: "brain_correlations_self_endpoint"
neutralization: "SUBINDUSTRY"
decay: 6
family: "tlcf_event_magnitude_buzz_blend"
session: "20260709-001"
brain_url: "https://platform.worldquantbrain.com/alpha/rKlo39p1"
queued: "2026-07-09"
long_term_value: "MEDIUM"
---

# Submit rKlo39p1 (Tax Loss Carryforward Event-Magnitude + Leverage + Ivaco + Drlt + Buzz)

EXCELLENT grade, self-corr PASS at 0.6262 (auto-pass, comfortably under 0.7,
no Sharpe premium needed) vs top peer `d5Q3ZmWv` (S=2.97). All 6 other computable
BRAIN checks PASS; `SELF_CORRELATION` on `/check` had not resolved to an explicit
verdict at verification time (recommend a final `/check` re-poll before submitting
to confirm it now reads PASS explicitly, though the underlying correlation value
from `/correlations/self` already satisfies the auto-pass rule).

Per `submission-priority-long-term.md`: self-corr in the 0.6-0.7 band = LOW-to-MEDIUM
long-term value tier (lower than the two other EXCELLENT candidates currently queued
in the same consolidation: `2rLRzov8` at 0.6495 and `wpl5eP5v` at 0.6676 — this candidate
has the lowest self-corr of the three). Submit after any <0.6 candidate is available;
ahead of 2rLRzov8/wpl5eP5v if submission order is FIFO-by-corr.

First alpha in the book to use `fnd6_tlcf` (Tax Loss Carry Forward) as an event field.

## Post-Submission

Submitted by the human on 2026-07-10. BRAIN confirms `status: ACTIVE`, all
checks PASS.
