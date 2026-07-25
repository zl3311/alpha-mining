---
scope: "family-negated-tax-ptpr-core"
discovered: "20260707-001"
expressions_tested: 3
best_sharpe: 2.37
best_self_corr: 0.941
status: "dead"
---

# Dead Zone: Negated-Tax + anl4_ptpr_flag + open/close Core

## Scope

Expressions of the form `ts_decay_linear(rank(-1 * fnd6_tx*) + rank(anl4_ptpr_flag)
+ rank(open/close - 1), d)` — negated tax/deferred-tax fields blended with the
`anl4_ptpr_flag` analyst-revision flag and the overnight-gap component.

## Why dead

Tested in 20260707-001 via authoritative BRAIN `/check`:

| Alpha | Negated field | Grade | S | F | Self-Corr | Verdict |
|-------|---------------|-------|---|---|-----------|---------|
| VkPnWlMb | fnd6_txw | EXCELLENT | 2.37 | 2.18 | 0.939 | FAIL |
| RR8Xg8wb | fnd6_txdbca/close | EXCELLENT | 2.31 | 2.07 | 0.941 | FAIL |
| Xgn6KdR8 | fnd6_intc/close | GOOD | 2.07 | 1.69 | ~0.94 (inferred) | FAIL |

All three hit a **~0.94 self-corr wall** against the book's ptpr+intraday cluster
(LLR0n261, O0ZOJbaq, O0pl2znv — all share `anl4_ptpr_flag + rank(open/close - 1)`).

## Mechanism of the block

Negating the fundamental anchor (`-1 * fnd6_txw` vs `fnd6_txw`) changes the
direction of the fundamental signal but does NOT change the correlation
contribution of the shared `anl4_ptpr_flag + open/close - 1` core. The correlation
is dominated by the shared analyst-flag + intraday components, not by the
fundamental anchor's sign.

## Escape route (proven)

Swap the shared analyst flag: replace `anl4_ptpr_flag` with `anl4_netdebt_flag`.
The negated-enterprise-value + netdebt blend (2rLRzov8) uses this escape and
reaches self-corr 0.6495 (PASS). See `data/knowledge/patterns/negated-ev-netdebt-blend.md`.

## Do not test again

Do not generate more `negated_fundamental + anl4_ptpr_flag + open/close - 1`
variants. The ptpr+intraday core is the wall, not the fundamental field. Further
negated-tax or negated-deferred-tax variants will repeat this 0.94 failure.
