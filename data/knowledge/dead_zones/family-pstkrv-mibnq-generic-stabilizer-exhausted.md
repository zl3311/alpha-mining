---
category: "dead_zone"
entity_type: "family"
family: "pstkrv_mibnq_event_magnitude_generic_stabilizer"
discovered: "20260715-003"
revised: "20260719-001 (narrowed -- pstkrv + leverage-free proven skeleton is NOT dead; N1rlJ7mq is ACTIVE)"
expressions_tested: 55
best_sharpe: 2.15
best_fitness: 3.06
best_self_corr: 0.725
status: "partial_dead_end"
confidence: "medium"
---

# Family: `fnd6_pstkrv` / `fnd6_newqv1300_mibnq` Event-Magnitude + Any Generic Stabilizer

> **Scope correction (20260719-001).** This file originally marked the
> `ivaco + drlt + analyst4_flag + buzz*(-ret)` skeleton on `fnd6_pstkrv` as
> CONFIRMED BLOCKED at 0.796. That 0.796 was `oml0kV52`'s value, misattributed
> to `N1rlJ7mq` from a shared platform reading — see
> `data/knowledge/rules/pstkrv-family-multiplier-exception.md`. `N1rlJ7mq` is
> authoritatively **0.6903 PASS** and is now ACTIVE in the book. The dead-end
> finding below still holds for the *fresh-substitute* and *IV90* legs, and for
> `mibnq`, but **not** for `pstkrv` + the proven leverage-free skeleton.

## Scope

The event-magnitude anchors `fnd6_pstkrv` (preferred-stock redemption value)
and `fnd6_newqv1300_mibnq` (minority interest) — both validated as fresh,
individually-decorrelated anchors in session `20260715-002`/`003` — combined
with ANY secondary stabilizer leg strong enough to lift fitness to GOOD or
above.

## Why dead

Session `20260715-003` tested 14+ distinct secondary-leg families across 5
rounds (55 simulations total, following on from session `20260715-002`'s 46
simulations on the same anchors — 101 combined):

| Secondary leg(s) | Best fitness reached | Self-corr result |
|---|---|---|
| `ivaco + drlt + analyst4_flag + buzz*(-ret)` (the proven skeleton) | 2.07-3.06 | **NOT BLOCKED on `pstkrv`** — `N1rlJ7mq` is 0.6903 PASS, ACTIVE (BRAIN `/check`, session 20260719-001). Blocked on `min_net_debt_guidance` (`oml0kV52`, 0.796) |
| `volume/adv20`, `sales_estimate_count`, `historical_volatility_90`, `pv13_ustomergraphrank_hub_rank`, `fnd6_fopo/fopox`, buzz LEVEL (fresh substitutes) | 0.11-0.92 | N/A — never reached gate-pass fitness |
| `-ts_zscore` sparse fields (`fn_goodwill_acquired_during_period_a`, `fn_comp_options_grants_fair_value_a`), any `rank()`-wrapped blend | 0.01-0.68 | N/A — never reached gate-pass fitness |
| IV90 call-put spread (options family) | 2.45-3.06 | **estimated BLOCKED** (0.725-0.824, local) |
| Second weak anchor (`pstkrv` + `mibnq` combined, no other leg) | 0.01-0.45 | N/A — never reached gate-pass fitness |
| No secondary leg (pure anchor alone) | 0.17 (INFERIOR) | **SAFE** (0.496) |

## The pattern

The anchor alone is genuinely decorrelated (self-corr 0.496) but far too weak
to submit (Sharpe 0.43). Every secondary leg tested that was strong enough to
lift fitness into GOOD+/EXCELLENT territory ALSO belonged to a family already
well-represented in the 47-alpha ACTIVE book (fundamental6 stabilizers,
analyst4 flags, buzz-reversal, options/IV spreads), and correlation followed
that family's existing correlation profile almost regardless of which
specific field was chosen from it. Secondary legs that were genuinely fresh
(no existing book representation) were uniformly too weak to lift fitness
past AVERAGE.

## Rule

Do not test further *novel* secondary-leg substitutions on `fnd6_pstkrv` or
`fnd6_newqv1300_mibnq` event-magnitude anchors expecting a different
outcome — 101 combined simulations across two sessions found nothing that was
both fresh and strong enough. The genuinely fresh legs were all too weak to
reach gate-pass fitness, and the strong ones (IV90 spreads) correlated.

Two carve-outs from the original blanket rule:

- The proven `ivaco + drlt + analyst4_flag + buzz*(-ret)` skeleton on
  `fnd6_pstkrv` is submittable (`N1rlJ7mq`, 0.6903 PASS, ACTIVE) — this
  file's original 0.796 BLOCKED entry for it was a misattribution.
- `mibnq` remains unsolved; nothing on that anchor has cleared the gates.

If revisited beyond those, the required approach is a genuinely different
OPERATOR-TREE STRUCTURE (not another additive `rank(anchor) +
rank(stabilizer)` blend), not another field swap within the same architecture.
