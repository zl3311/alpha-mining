---
category: "rule"
severity: "critical"
discovered: "20260716-001"
revised: "20260719-001 (narrowed to leverage-bearing forms after N1rlJ7mq counterexample)"
confidence: "high"
supersedes: "the escape-route claim in overnight-gap-flag-skeleton-saturated.md ('the event-magnitude-abs-ts-delta template... NO open/close-1, NO analyst flag' is no longer a reliable escape)"
evidence: "4 independent anchor fields (fnd6_newqv1300_mibnq [session 20260715-002/003], min_net_debt_guidance [session 20260715-002], fnd6_cld2, fnd6_fopo [session 20260716-001]) land at local/authoritative self-corr 0.77-0.93 when -1*equity/assets is combined with 2+ of {fnd6_ivaco, fnd6_drlt, fnd6_fatl, any anl4_*_flag, ts_mean(scl12_buzz,d)*(-1*returns)}. Counterexample: N1rlJ7mq (fnd6_pstkrv, same set MINUS leverage) is authoritatively 0.6903 PASS and ACTIVE."
---

# Rule: The Classic Stabilizer Stack Is Blocked for ANY Anchor — but Only When the Leverage Leg Is Present

## The rule

The `{-1*equity/assets, fnd6_ivaco, fnd6_drlt, fnd6_fatl, any anl4_*_flag,
ts_mean(scl12_buzz,d)*(-1*returns)}` stabilizer set — the backbone of the
event-magnitude family that produced 8+ ACTIVE book alphas across sessions
20260604 through 20260715 — is confirmed BLOCKED (self-corr 0.77-0.93)
**regardless of which anchor field is used**, whenever `-1*equity/assets`
(leverage) appears alongside 2 or more of the remaining components. The block
is a property of the STACK, not of any particular "unlucky" anchor: it
reproduces on `fnd6_cld2` and `fnd6_fopo`, two independently-tested fresh
anchors.

**Dropping the leverage leg is what breaks the block.** The same stack minus
leverage has now cleared 0.70 twice, on two different anchors:

| Alpha | Anchor | Legs (no leverage) | Authoritative self-corr |
|-------|--------|--------------------|-------------------------|
| `N1rlJ7mq` | `fnd6_pstkrv` | ivaco + drlt + `anl4_fcf_flag` + buzz*(-ret) | **0.6903 PASS** (ACTIVE) |
| `aknmG1M6` | `fnd6_cld2`+`fnd6_fopo` | 2x ivaco + 2x buzz*(-ret) | **0.6181 PASS** (ACTIVE) |

So the earlier, broader form of this rule ("any 3+ components, blocked") is
too strong — `N1rlJ7mq` combines four of them and passes. Leverage is the
load-bearing correlate, which is consistent with both escape patterns in the
knowledge base (`market-neutral-event-magnitude-escape.md` and
`leverage-free-fresh-anchor-decorrelation.md`) independently converging on
dropping it.

## Evidence

| Session | Anchor | Stack | Local/Authoritative Self-Corr | Verdict |
|---------|--------|-------|-------------------------------|---------|
| 20260715-002 | `min_net_debt_guidance` (`oml0kV52`) | leverage+ivaco+drlt/fatl+flag+buzz | 0.796 (BRAIN-confirmed) | BLOCKED |
| 20260719-001 | `fnd6_pstkrv` (`N1rlJ7mq`) | ivaco+drlt+flag+buzz, **no leverage** | 0.6903 (BRAIN-confirmed) | **PASS — ACTIVE** |
| 20260715-003 | `fnd6_pstkrv`/`mibnq` | + IV90 options spread (novel) | 0.725-0.824 (local) | BLOCKED (est.) |
| 20260716-001 | `fnd6_cld2` | leverage+ivaco+drlt+buzz (full 5-leg) | 0.775 (local) | BLOCKED (est.) |
| 20260716-001 | `fnd6_fopo` (event-magnitude form) | leverage+ivaco+drlt+buzz | 0.926 (local) | BLOCKED (est.) |
| 20260716-001 | `fnd6_cld2`+`fnd6_fopo` (dual anchor) | leverage+ivaco+drlt+buzz | ~0.66-0.68 (local, MARKET neut) | RISKY, fitness dropped to GOOD |
| 20260716-001 | `fnd6_cld2`+`fnd6_fopo` | ivaco+drlt+buzz (leverage DROPPED) | 0.637-0.655 (local) | RISKY (best found) |
| 20260716-001 | `fnd6_cld2`+`fnd6_fopo` | 2x ivaco + 2x buzz (drlt+leverage DROPPED) | 0.618-0.643 (local) | RISKY (lowest found), F=2.03-2.26 EXCELLENT |

## Implication

- **Do not** assume a fresh anchor + the full classic stabilizer stack will
  decorrelate just because the anchor itself sits in a small/orthogonal
  redundancy cluster. The stack's shared legs dominate the correlation
  budget once the book is dense enough (47+ alphas), independent of anchor.
- **The decorrelation-preserving lever that DOES work**: drop `equity/assets`
  (leverage). Both confirmed escapes did this and nothing else in common —
  `aknmG1M6` additionally dropped `fnd6_drlt` and double-weighted the
  remaining `fnd6_ivaco` + `ts_mean(scl12_buzz,d)*(-1*returns)` across TWO
  fresh anchors (local 0.775-0.926 -> 0.618-0.655, F=2.0-2.26), while
  `N1rlJ7mq` kept `drlt` and the analyst flag on a single anchor and still
  reached 0.6903. Both are now BRAIN-confirmed PASS and ACTIVE, so this band
  is no longer merely "RISKY" — but 0.62-0.69 leaves thin margin, and an
  authoritative check per candidate is still required before submission.
  See pattern `leverage-free-fresh-anchor-decorrelation.md`.
- MARKET neutralization further reduces local corr (to ~0.66-0.68 from
  0.775-0.926) but costs enough fitness to drop the grade from EXCELLENT to
  GOOD (F 1.86-1.87) — not a viable path to EXCELLENT+ for this family
  specifically (consistent with `market-neut-tradeoff.md`'s general
  warning, now confirmed for this family too).
