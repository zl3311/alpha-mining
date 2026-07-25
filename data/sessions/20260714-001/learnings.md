---
id: "20260714-001-learnings"
session: "20260714-001"
category: "refinement"
confidence: "high"
actionable: true
---

# Learnings: Session 20260714-001

## What Worked

- Re-checking a candidate after BRAIN's asynchronous self-correlation
  computation resolved changed the verdict from locally RISKY to
  authoritatively SAFE.
- The candidate's Sharpe premium was sufficient to clear the correlation
  override even though its maximum self-correlation exceeded 0.70.

## What Did Not Change

- The candidate remains a high-correlation use of the account's limited
  correlation budget. The BRAIN pass establishes eligibility, not high
  long-term value.

## Mechanism Insight

`fnd6_newqv1300_msaq` event magnitude measures large changes in accumulated
other-comprehensive-income marketable-security adjustments. Combining that
event signal with investing-activity, deferred-revenue, FFO-revision, and
buzz-reversal stabilizers produces strong aggregate performance, but overlaps
materially with the now-ACTIVE MARKET-neutral MSAQ sibling. BRAIN's premium
rule is therefore essential to its viability.
