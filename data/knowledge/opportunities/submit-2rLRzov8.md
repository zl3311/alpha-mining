---
type: "submit-candidate"
alpha_id: "2rLRzov8"
status: "SUBMITTED"
submitted: "2026-07-08"
priority: "medium"
grade: "EXCELLENT"
sharpe: 2.06
fitness: 2.13
turnover: 0.128
self_corr_max: 0.6495
self_corr_peer: "O0ZOJbaq"
neutralization: "SUBINDUSTRY"
decay: 6
family: "negated_enterprise_value_blend"
session: "20260706-002"
verified_session: "20260707-001"
brain_url: "https://platform.worldquantbrain.com/alpha/2rLRzov8"
queued: "2026-07-07"
long_term_value: "LOW"
---

# Submit 2rLRzov8 (Negated Enterprise-Value Blend)

## Expression
`ts_decay_linear(rank(-1 * enterprise_value / close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close - 1), 5)`

## Why submittable
- Self-corr 0.6495 vs current book; BRAIN authoritative `/check`: **PASS** (below 0.7
  auto-pass threshold, no Sharpe premium required).
- Top peer O0ZOJbaq (S=2.36, corr 0.6495): auto-PASS.
- All 7 computable BRAIN checks PASS.
- Grade EXCELLENT, S=2.06, F=2.13, T=12.8%.
- Novel negated-direction family (no negated-EV entry in book) — aligns with the
  book-saturation rule's negation diversification axis.

## Long-term value
LOW — self-corr in the 0.6–0.7 band. Submittable and SAFE, but consumes more
correlation headroom than a < 0.4 candidate would. Submit when a slot is open and
no higher-priority (< 0.4 self-corr) EXCELLENT+ candidate is queued.

## Reviewer action
Submitted on 2026-07-08. Status flipped to SUBMITTED; `data/book/2rLRzov8.md`
flipped to ACTIVE.
