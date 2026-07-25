---
category: "rule"
severity: "high"
discovered: "20260713-001"
confidence: "high"
evidence: "2 fresh anchor fields (fnd6_newqv1300_msaq, current_ratio) on the event-magnitude-abs-ts-delta template's standard leverage+ivaco+buzz stabilizer set both correlated 0.79-0.92 (local PnL) against the existing 6+-member family under SUBINDUSTRY, regardless of anchor field economic distinctness"
---

# The Event-Magnitude Family's `leverage(-1*equity/assets) + ivaco + buzz` Stabilizer Skeleton Is Now Fully Saturated

## The rule

Any expression built as `rank(abs(ts_delta(FRESH_ANCHOR/close,d))) + rank(-1*equity/assets)
+ rank(fnd6_ivaco/close) + rank(ts_mean(scl12_buzz,w)*(-1*returns)) [+ other legs]`
will correlate 0.79-0.92 (local PnL) with the existing event-magnitude family
under SUBINDUSTRY neutralization — **regardless of how economically distinct
the anchor field is** — because 6+ ACTIVE book entries (`0m8GV1Pp`, `le0gY6Ze`,
`wpl5eP5v`, `rKlo39p1`, `WjGVJ7bN`, `YP0bLdzA`) already share this exact
`leverage + ivaco + buzz` 3-leg stabilizer skeleton verbatim. This is the same
class of finding as `overnight-gap-flag-skeleton-saturated.md` (the
`open/close-1 + {ptpr_flag|netdebt_flag}` skeleton), but for the
event-magnitude family's stabilizer set instead of the overnight-gap family's
catalyst pair.

## Evidence (session 20260713-001)

| Candidate | Anchor | Stabilizers | Local corr vs family | Result |
|-----------|--------|-------------|----------------------|--------|
| `vRlY5MPd` | `fnd6_newqv1300_msaq` | leverage+ivaco+ffo_flag+buzz | 0.883 (BRAIN authoritative) | FAIL |
| `A1PLkE6W` | `fnd6_newqv1300_msaq` | leverage+drlt+ffo_flag+buzz | 0.789 (local) | BLOCKED |
| `gJMr9zAK` | `current_ratio` | leverage+ivaco+buzz (event-magnitude form) | 0.922 (local) | BLOCKED |

Notably, `current_ratio` (a liquidity ratio, economically unrelated to the
tax/debt/inventory/fair-value items already anchoring the family) correlated
**worse** (0.922) than `fnd6_newqv1300_msaq` (0.789-0.883, itself a mark-to-market
adjustment already somewhat economically adjacent to the family). This proves
the correlation driver is the **shared stabilizer skeleton**, not the anchor's
economic proximity — echoing the exact lesson from
`overnight-gap-flag-skeleton-saturated.md`.

## Escape routes tried

1. **Remove `leverage` from the blend, keep `ivaco + drlt`**: preserves GOOD-grade
   fitness (F~1.70) with improved but still uncomfortably-thin correlation
   (~0.59 local). See `P03PGeex`.
2. **Remove `leverage` AND `ivaco`**: fitness collapses to INFERIOR (F<=0.67).
   Leverage and ivaco together are load-bearing for fitness in this family, not
   just decoration.
3. **MARKET neutralization on the leverage-free `ivaco+drlt+ffo_flag+buzz`
   blend** (proven effective): dropped correlation from 0.646 (RISKY, SUBINDUSTRY)
   to 0.528 (SAFE) at a moderate fitness cost (F 2.49 -> 2.02, still EXCELLENT).
   See pattern `market-neutral-event-magnitude-escape.md` and alpha `O0Z6NE0b`.

## Implication for mining

- Do NOT treat a fresh/economically-distinct anchor field as sufficient
  evidence of low self-corr on the event-magnitude template. Check whether the
  stabilizer legs (`leverage`, `ivaco`, `buzz`) are shared verbatim with 3+
  existing family members first.
- This skeleton should be treated as fully saturated under SUBINDUSTRY for new
  EXCELLENT+ decorrelated submissions. New anchors will reliably reproduce
  strong aggregate metrics but will not clear self-corr without a structural
  change (drop a shared leg, or switch neutralization).
- The MARKET-neutralization escape (removing `leverage` first, since MARKET
  otherwise kills the leverage-premium component per `leverage-premium.md`)
  is the proven working escape route — see the companion pattern file.
