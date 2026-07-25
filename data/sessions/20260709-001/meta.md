---
id: "20260709-001"
date: "2026-07-09"
strategy: "EXPLORE"
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
status: "complete"
budget: "unlimited"
budget_used: 59
rounds: 5
simulations: 59
gate_passers: 17
submissions: 1
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
research_question: "Do genuinely novel operator-tree shapes (directional gating, multi-horizon spread, non-linear magnitude x level) on low-community-usage fundamental fields (tlcf, mrct, dcvsub, acqgdwl, prepaid_expense) yield decorrelated EXCELLENT+ alphas, per novelty-required.md?"
best_alpha: "rKlo39p1"
best_grade: "EXCELLENT"
best_sharpe: 2.13
best_fitness: 2.22
best_self_corr: 0.6262
best_self_corr_result: "PASS"
submitted: ["rKlo39p1"]
submitted_date: "2026-07-10"
outcome: "Found EXCELLENT submittable candidate rKlo39p1 (self-corr PASS 0.6262). Presented + draft PR opened (not submitted by agent); user submitted manually 2026-07-10. BRAIN confirms status ACTIVE, all checks PASS."
candidates:
  - id: "rKlo39p1"
    grade: "EXCELLENT"
    sharpe: 2.13
    fitness: 2.22
    self_corr_value: 0.6262
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
tags:
  - "session_20260709-001"
  - "EXPLORE"
---

# Session 20260709-001: EXPLORE — Novel Tree Shapes on Low-Usage Fundamental Fields

## Outcome

**Found:** [rKlo39p1](https://platform.worldquantbrain.com/alpha/rKlo39p1) —
EXCELLENT, S=2.13, F=2.22, T=10.7%, self-corr **PASS 0.6262** (auto-pass, no
Sharpe premium needed) vs top peer `d5Q3ZmWv`. All 6 other computable BRAIN
checks PASS. **NOT submitted** (per user instruction) — labeled on BRAIN
(metadata only), recorded as PENDING in `data/book/rKlo39p1.md`, queued in
`data/knowledge/opportunities/submit-rklo39p1.md`, and presented to the user
via draft PR.

Discovered via a 5-round pivot: rounds 1-2 (33 sims) tested genuinely novel
operator-tree shapes (directional gating, multi-horizon spread, non-linear
convex, dispersion, flag×sentiment) on low-usage fields per
`novelty-required.md` — all failed to clear GOOD grade. Round 3 pivoted to
extend the PROVEN `event-magnitude-novel-fields` template to those same fields;
`fnd6_tlcf` and `fnd6_dcvsub` both showed promise. Round 4 refined the `tlcf`
recipe and found that adding a `buzz-stabilizer` 5th factor lifts it from GOOD
(F=1.79, confirmed self-corr PASS 0.6372) to EXCELLENT (F=2.22) at effectively
no self-corr cost (0.6262).

## Context Assessment (Phase 0)

- Book: 39 ACTIVE + 11 PENDING (per `data/book/`) across 47+ mechanism families.
- **3 open draft PRs not yet merged** carry unmerged knowledge + submittable candidates:
  - PR #79 (20260705-001, negation-blend EXPLORE) — GrLJLGN5 QUEUED
  - PR #80 (20260707-001, EXPLOIT verification) — `2rLRzov8` EXCELLENT self-corr PASS 0.6495, LOW long-term value, NOT submitted
  - PR #81 (20260708-001, EXPLORE event-magnitude) — `wpl5eP5v` EXCELLENT self-corr PASS 0.6676, LOW long-term value, NOT submitted
  - These already satisfy "submittable EXCELLENT+, not submitted, draft PR" from prior sessions. This session pursues an independent NEW candidate as requested, additive to those.
- Local uncommitted stale artifacts found on `main` at session start: `data/book/ZYpjKeKx.md` status update (PENDING→ACTIVE, user submitted manually 2026-07-06) and two abandoned/incomplete session dirs (`20260705-001`, `20260706-002`, both `in_progress` with no results.md — orphaned, no PR). Left as-is; not this session's scope to fix, noted for follow-up.
- HF server: healthy, 52891 results, 0 pending, budget 5000, worker idle.
- 24h gate-passers: 47 results, all from the `event-magnitude-novel-fields` family (ppegtq/drc/dd1q/cshtr variants) — already claimed by `wpl5eP5v` (PR #81, unmerged). No genuinely new family → EXPLOIT does not trigger.
- `negation-blend-candidates.md` (priority high, status "untested" — stale, was substantially tested in session 20260706-001) → HYPOTHESIS mode partially satisfied already; remaining untested leads (`fnd6_acqgdwl`, `fnd6_dcvsub` negated) folded into this session's field list instead of re-running full HYPOTHESIS.

## Strategy

EXPLORE (default; per decision tree, no unclaimed new-family gate-passer exists for EXPLOIT,
no 2+ unexploited-family gate-passers for RECOMBINE). Per `novelty-required.md`, target
structurally novel operator-tree shapes (not just new fields in old templates):

1. **Directional gating**: `rank(F) * sign(ts_delta(G, d))`
2. **Multi-horizon spread**: `rank(ts_delta(F, 5) - ts_delta(F, 22))`
3. **Non-linear magnitude x level**: `rank(F) * rank(abs(ts_delta(F, d)))`
4. **Control baseline** (legacy, <=50% budget): `product-interaction-blend` template applied to new fields, for comparison.

Field selection: low-community-usage fundamental6/fundamental2 fields (alphaCount 400-1400,
vs typical fundamental6 median ~8000+) not yet in the book: `fnd6_tlcf` (tax loss carryforward,
419), `fnd6_mrct` (rental commitments, 1380), `fnd6_dcvsub` (convertible subs debt, 583),
`fnd6_acqgdwl` (acquired goodwill, 1317), `fn_prepaid_expense_q` (518).

## Excluded / Dead Zones Respected

- `fnd6_txbcof` + analyst blends — CONCENTRATED_WEIGHT structural block
- Negated-tax (`txw`/`txdbca`/`intc`) + `anl4_ptpr_flag` + `open/close-1` — 0.94 self-corr wall (PR #80 dead zone, unmerged but confirmed)
- Additive negated-fresh-fundamental6 blends with value-ratio anchors (`intc`/`txw`/`txdbca`/`acqgdwl`/`dcvsub`) — INFERIOR, 34 sims (PR #81 dead zone, unmerged but confirmed). This session uses gating/spread/non-linear templates instead, not additive blends, to avoid re-triggering this dead zone.
- `rank(F1/F2)` inter-field fundamental ratios — dead (S=0.26)
- `rank(ts_corr(fundamental, returns, d))` dynamic correlation — dead (S=1.00)
- `drc`/`cshtr` event-magnitude — self-corr FAIL vs itci family
- Dual-event-magnitude blends — cancel, AVERAGE
- `model16`/`model51`/`news12`/`news18` datasets — standalone dead (pre-priced scores / turnover kills fitness)
- `pv_reversal`, `cogs` families — saturated / self-corr blocked
