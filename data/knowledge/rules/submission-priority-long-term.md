---
rule: "Submit lowest self-corr EXCELLENT+ alphas first to maximize cumulative points"
category: "rule"
severity: "strategic"
discovered: "20260622-001"
confidence: "high"
evidence: "Each submitted alpha becomes a peer in future self-corr checks; lower-corr submissions consume less correlation budget and preserve capacity for more total submissions over time."
---

# Submission Priority: Long-Term Point Maximization

## Principle

The goal of alpha mining is to **maximize total account points over time**, not
just per-session output. Each submission consumes part of the finite correlation
budget (the 0.7 threshold against the existing book). The optimal strategy
minimizes correlation budget consumption per point gained.

## Priority Ordering (when multiple submittable candidates exist)

1. **Primary: lowest self-corr first.** A submission at self-corr=0.25 barely
   constrains future candidates. A submission at self-corr=0.65 may block
   similar future alphas from passing the 0.7 threshold. Submit low-corr first
   to preserve optionality.

2. **Secondary: grade descending.** Only EXCELLENT+ (SPECTACULAR, EXCELLENT)
   candidates warrant prioritized promotion — they yield the most points per
   submission slot. GOOD/AVERAGE alphas are still worth submitting for point
   grinding but should not displace EXCELLENT+ candidates in the queue.

3. **Tertiary: Sharpe descending.** Tie-breaker within same grade tier.

## Highlight Rule

Flag any candidate meeting ALL of these as **HIGH LONG-TERM VALUE**:
- Grade: EXCELLENT or SPECTACULAR
- Self-corr (BRAIN check): PASS with value < 0.4
- All 7 computable BRAIN checks: PASS

These are the most valuable long-term assets. They contribute high points AND
minimally constrain future submissions. Always submit them first and note them
prominently in session reports and book entries for future reference.

## Why This Works

BRAIN's self-corr is measured against the FULL submitted book. Adding a new alpha
at corr=0.3 raises the "floor" for future alphas by very little. Adding one at
corr=0.65 raises it substantially — every future alpha in a similar family now
faces a tighter constraint. Over 20-50 submissions, the cumulative effect of
always choosing low-corr-first can mean 5-10+ additional submittable alphas
compared to a naive highest-Sharpe-first approach.

## Barely-Passing Is Still Worth Submitting

Even EXCELLENT+ alphas with self-corr in the 0.6-0.7 range (barely passing) are
worth submitting — they still yield points. But they should be submitted AFTER
all lower-corr candidates in the queue, preserving optionality in case a future
session discovers a lower-corr variant in the same family.

## Decision Table

| Grade | Self-Corr (BRAIN) | Priority | Long-Term Value | Action |
|-------|-------------------|----------|-----------------|--------|
| SPECTACULAR | any (PASS) | high | HIGH | Submit immediately |
| EXCELLENT & < 0.4 | < 0.4 | high | HIGH | Submit first, flag for reference |
| EXCELLENT & 0.4–0.6 | 0.4–0.6 | medium | MEDIUM | Submit after HIGH candidates |
| EXCELLENT & 0.6–0.7 | 0.6–0.7 | medium | LOW | Submit last among EXCELLENT; barely passing |
| GOOD & < 0.4 | < 0.4 | medium | MEDIUM | Point grinder, submit if no EXCELLENT queued |
| GOOD & >= 0.4 | >= 0.4 | low | LOW | Submit only if nothing better available |
| AVERAGE | any | low | LOW | Deprioritize unless points quota is urgent |
