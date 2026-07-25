---
category: "rule"
severity: "high"
discovered: "20260711-001"
confidence: "high"
evidence: "8+ anchor-field variants (acdo, dd1q, itci, cshtr, txw, txdbca, dltis, gric_flag-spread) on the {open/close-1 + ptpr_flag|netdebt_flag} 2-leg skeleton across sessions 20260614 through 20260711 all correlate 0.74-0.91 with existing book entries that share the exact same 2-leg skeleton verbatim"
---

# The `{open/close - 1} + {anl4_ptpr_flag | anl4_netdebt_flag}` Skeleton Is a Correlation Trap Regardless of the Third Leg

## The rule

Any expression built as `rank(FRESH_ANCHOR) + rank(open / close - 1) +
rank(anl4_ptpr_flag)` (or the `anl4_netdebt_flag` variant) will correlate
0.74-0.91 with multiple existing book entries — **regardless of how fresh or
economically distinct `FRESH_ANCHOR` is** — because several book entries
(`LLR0n261` = `acdo + open/close-1 + netdebt_flag`; `78w5d35x` and `O0ZOJbaq` =
`{itci|cshtr} + ptpr_flag + open/close-1 + ...`; `6Xzm6PQP`,
`np30Odjd`, `omVpwdqk`) already use this exact 2-leg skeleton with a different
third/fourth leg. The `open/close-1` overnight-gap component trades every
single day and dominates the daily return-timing pattern; two alphas sharing
it plus one analyst flag will correlate heavily no matter what else differs.

## Evidence (session 20260711-001)

Tested `fnd6_dltis` (debt issuance, never used before) and a multi-horizon
`anl4_gric_flag` spread (never used before) on this exact skeleton across 24
simulations (rounds 1-2). Every EXCELLENT+ result showed local PnL correlation
0.766-0.914 vs the book, confirmed via decomposition to be driven by the shared
skeleton, not the anchor:

| Candidate | Anchor | vs_book max | Peer (shares skeleton) |
|-----------|--------|-------------|------------------------|
| RR8Vz96o | dltis | 0.801 | 6Xzm6PQP |
| d50OzQNg | gric_flag spread | 0.770 | LLR0n261 |
| 3qR9JvXX | dltis + netdebt | 0.797 | LLR0n261 (literal 2/3-leg match) |
| j203MmjE | gric_flag + netdebt | 0.914 | LLR0n261 (near-exact match) |

Even MARKET neutralization (typically -0.10 to -0.20 corr) and swapping
`open/close-1` for `ts_mean(scl12_buzz,5)*(-1*returns)` (also already saturated,
see `flag-ret-correlation.md`) only reduced correlation to 0.74-0.77 — still
blocked, and Sharpe was insufficient for the premium escape in every case
tested (peer Sharpes 1.87-2.55 require candidate Sharpe 2.06-2.81, none of the
tested candidates cleared this).

## Implication for mining

- Do NOT treat "the anchor field is fresh/never-used" as sufficient evidence of
  low self-corr. Check whether the OTHER 2+ legs of the blend are shared
  verbatim with existing book entries first — if so, expect 0.7-0.9+
  correlation regardless of anchor novelty.
- This skeleton (`open/close-1 + {ptpr_flag|netdebt_flag}`) should be treated as
  fully saturated for EXCELLENT+ decorrelated submissions. Do not spend budget
  on new anchor-field variants of it.
- The escape route that DOES work: the `event-magnitude-abs-ts-delta` template
  (`abs(ts_delta(F/close,d)) + leverage + stabilizers`, NO `open/close-1`, NO
  analyst flag) — see `data/knowledge/patterns/event-magnitude-fresh-stabilizer.md`
  for how to further decorrelate WITHIN that family too.
