---
id: "20260707-001"
date: "2026-07-07"
strategy: "EXPLOIT"
trigger: "manual (user-initiated, no budget constraint, find minimal EXCELLENT+ submittable; do not submit, present + draft PR)"
status: "complete"
budget: "unlimited"
budget_used: 0
target: "EXCELLENT+ submittable (minimal viable candidate, satisfice)"
research_question: "Can the 24h queue's novel negated-direction gate-passers (negated-tax, negated-enterprise-value, itci-event-magnitude-leverage) clear BRAIN checks + the 0.7 self-corr gate?"
opportunity: "negation-blend-candidates.md + book-saturation negation direction"
gate_passers: 6
submittable_candidates: 1
submissions: 1
submitted: ["2rLRzov8"]
submitted_date: "2026-07-08"
best_alpha: "2rLRzov8"
best_grade: "EXCELLENT"
best_sharpe: 2.06
best_fitness: 2.13
best_self_corr: 0.6495
best_self_corr_peer: "O0ZOJbaq"
best_self_corr_result: "PASS"
best_verdict: "SUBMITTED"
candidates:
  - id: "2rLRzov8"
    grade: "EXCELLENT"
    sharpe: 2.06
    fitness: 2.13
    self_corr_value: 0.6495
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "1Yd65kmJ"
    grade: "SPECTACULAR"
    sharpe: 2.62
    fitness: 2.74
    self_corr_value: 0.997
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "VkPnWlMb"
    grade: "EXCELLENT"
    sharpe: 2.37
    fitness: 2.18
    self_corr_value: 0.939
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
  - id: "RR8Xg8wb"
    grade: "EXCELLENT"
    sharpe: 2.31
    fitness: 2.07
    self_corr_value: 0.941
    self_corr_result: "FAIL"
    verdict: "BLOCKED"
---

# Session 20260707-001: EXPLOIT — Negated-Direction Gate-Passer Verification

## Context Assessment

- Book: 39 ACTIVE + 11 PENDING across 47+ families
- Self-corr wall: 0.7 threshold + 1.10x Sharpe premium escape
- Recent 24h gate-passers contain several novel negated-direction EXCELLENT/SPECTACULAR
  candidates NOT in the book, aligned with the book-saturation rule's negation-direction
  recommendation (5x more independent dimensions than positive-only).
- 20260706-001 (HYPOTHESIS negation-blend) submitted ZYpjKeKx (accrued-liab event-magnitude).
- 20260706-002 (EXPLORE structurally novel templates) was interrupted (in_progress, no results recorded).
- Server: healthy (52811 results, idle worker, budget 4952).

## Outcome

**Submittable candidate found and subsequently submitted:**
[2rLRzov8](https://platform.worldquantbrain.com/alpha/2rLRzov8) — EXCELLENT,
S=2.06, F=2.13, T=12.8%, BRAIN self-corr **PASS** (0.6495 vs `O0ZOJbaq`, below 0.7
auto-pass). All 7 computable BRAIN checks pass. The user submitted it on
2026-07-08; BRAIN reports `ACTIVE`, and the book and queue records are reconciled.

Verification-only session (0 new simulations): the 24h gate-passer queue already
contained novel negated-direction EXCELLENT/SPECTACULAR candidates from the
interrupted 20260706-002 session. This session ran authoritative BRAIN self-corr
checks and identified the one SAFE candidate.

## Strategy

EXPLOIT. The 24h queue already contains novel negated-direction gate-passers from
genuinely new mechanism families (negated-tax `fnd6_txw`/`fnd6_txdbca`, negated
enterprise-value, itci-event-magnitude-leverage). Per the decision tree, EXPLOIT
applies when a new gate-passer is from a genuinely new family. These are negated-
direction families (book has no negated-tax or negated-EV entries), which the
book-saturation rule explicitly identifies as the highest-value remaining territory.

Approach:
1. Run BRAIN 8-check + authoritative self-corr (`pnl_correlation --brain-check`) on
   the top novel candidates from the 24h queue.
2. If any candidate is SAFE (all checks pass + self-corr PASS) at EXCELLENT+, stop
   (satisfice) and present.
3. If self-corr FAILS, run REFINE mutations to decorrelate (swap intraday component,
   shift correlation peer via an extra factor, change neutralization/decay) — applying
   the O0ZOJbaq lesson (add a factor to shift the top peer to a lower-Sharpe book entry
   so Sharpe premium escape becomes trivial).
4. If the negated-tax/EV family is structurally blocked, pivot to the itci-event-
   magnitude-leverage family (1Yd65kmJ SPECTACULAR S=2.62 F=2.74 T=3.5%).

## Candidate Pool (24h queue, not in book, EXCELLENT+, novel negated direction)

| Alpha ID | Grade | S | F | T | Family | Expression (truncated) |
|----------|-------|---|---|---|--------|------------------------|
| 1Yd65kmJ | SPECTACULAR | 2.62 | 2.74 | 3.5% | itci_event_magnitude_neg_leverage | rank(abs(ts_delta(fnd6_itci/close,5))) + rank(-1*equity/assets) + rank(fnd6_drlt/close) |
| VkPnWlMb | EXCELLENT | 2.37 | 2.18 | 17.0% | negated_tax_intraday | rank(-1*fnd6_txw) + rank(anl4_ptpr_flag) + rank(open/close-1) |
| RR8Xg8wb | EXCELLENT | 2.31 | 2.07 | 17.6% | negated_deferred_tax_intraday | rank(-1*fnd6_txdbca/close) + rank(anl4_ptpr_flag) + rank(open/close-1) |
| 2rLRzov8 | EXCELLENT | 2.06 | 2.13 | 12.8% | negated_enterprise_value_blend | rank(-1*enterprise_value/close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(fnd6_drlt) + rank(open/close-1) |
| YP0XZxav | EXCELLENT | 2.02 | 2.22 | 5.4% | itci_event_magnitude_netdebt | rank(abs(ts_delta(fnd6_itci/close,5))) + rank(anl4_netdebt_flag) |
| JjOmZ9rn | EXCELLENT | 1.90 | 2.19 | 14.1% | negated_enterprise_value_blend | rank(-1*enterprise_value/close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(open/close-1) |
| 88QrdQ7z | EXCELLENT | 1.82 | 2.15 | 11.7% | negated_enterprise_value_blend | rank(-1*enterprise_value/close) + rank(anl4_netdebt_flag) + rank(fnd6_cshtr) + rank(open/close-1) |
| xAkXAYZJ | EXCELLENT | 1.74 | 2.01 | 11.2% | dpactq_event_magnitude_flags | rank(abs(ts_delta(fnd6_newqv1300_dpactq/close,3))) + rank(anl4_bvps_flag) + rank(anl4_cfi_flag) |

## Excluded (saturated / dead)

- `fnd6_txbcof` + anl4_cfi_flag (CONCENTRATED_WEIGHT structural block — confirmed 20260706-001)
- IV270 call-put spread standalone (self-corr dead zone unless Sharpe > 2.002)
- `rel_ret_cust` + `anl4_ptpr_flag` + open/close (claimed by GrLJLGN5 PENDING)
- `anl4_ptpr_flag` + open/close saturated core (without a novel anchor)
- Accrued-liab event-magnitude (ZYpjKeKx just submitted)
