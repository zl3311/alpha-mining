---
category: "dead_zone"
entity_type: "family"
family: "negated_fresh_fundamental6_blends"
discovered: "20260708-001"
expressions_tested: 34
best_sharpe: 0.96
best_fitness: 1.06
status: "dead_end"
confidence: "high"
---

# Negated Fresh Fundamental6 Blends — Dead End

Additive blends of negated fundamental6 fields whose raw fields are NOT in the
submitted book (fnd6_intc, fnd6_txw, fnd6_txdbca, fnd6_acqgdwl, fnd6_dcvsub),
with or without value-ratio anchors (enterprise_value/close, sales/close,
ebitda/close, operating_income/close), produce no signal.

## Evidence (session 20260708-001, 34 sims across 2 rounds)

Best: `ts_decay_linear(rank(sales / close) + rank(-1 * fnd6_intc / close) + rank(-1 * fnd6_txdbca), 5)` S=0.96 F=0.68 INFERIOR.

### Diagnostic standalone negated blocks (round 2)

| Expression | This session S | negation-asymmetry pattern claimed S |
|------------|---------------|---------------------------------------|
| `ts_decay_linear(rank(-1 * fnd6_intc / close), 5)` | **-0.82** | 1.32 |
| `ts_decay_linear(rank(-1 * fnd6_txdbca), 5)` | **0.36** | 1.06 |
| `ts_decay_linear(rank(-1 * fnd6_txw), 5)` | **0.53** | 0.89 |

The `negation-asymmetry-fundamentals` pattern's standalone Sharpes are STALE.
Under the current default config (decay=6, SUBINDUSTRY, TOP3000) these negated
blocks are INFERIOR, not GOOD. The original negation sweep (20260705) likely
used a different config, or the underlying data/coverage changed.

## Verdict

Do NOT build additive blends from negated fnd6_intc/txw/txdbca/acqgdwl/dcvsub.
The negation-asymmetry pattern needs re-validation before being trusted as a
building-block source. Enterprise_value/close + negated-fresh complements also
INFERIOR — the ev/close building block requires the saturated gap+analyst-flag
complements to reach EXCELLENT (which then fail self-corr).
