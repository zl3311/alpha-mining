---
name: signal-generation
description: >-
  Generate candidate alpha expressions based on the chosen strategy. Includes
  hypothesis-driven design, directed mutation, template grids, crossover, and
  targeted refinement. Trigger on: generate, brainstorm, mutate, crossover,
  candidate, expression design.
---

# Signal Generation — Expression Design

Generate candidate alpha expressions based on the strategy selected by
`mining-session`. Each mode has different generation logic.

## Pre-Generation Checks

Before generating ANY expressions:

1. Read `data/knowledge/rules/` — hard constraints that disqualify expressions.
2. Read `data/knowledge/dead_zones/` — datasets/fields/families to avoid.
3. Verify the target dataset fields exist in `data/reference/brain_data_catalog.md`.
4. Check operator naming against the gotchas table in AGENTS.md (e.g., `ts_delay`
   not `delay`, `ts_corr` not `correlation`).
5. Read prior coverage from `data/factors/` (one file per factor) to avoid
   re-discovering already-known signals.

**Deprecated — do NOT read or write:** `data/reference/factor_inventory.json`,
`data/reference/hypothesis_backlog.md`,
`data/reference/brain_availability_matrix.md`, and anything under
`data/experiments/`. These are V1 artifacts superseded by `data/factors/`,
`data/book/`, `data/knowledge/`, and `data/sessions/`. Reading them yields stale
state.

## Mode: HYPOTHESIS

Triggered when a high-priority opportunity exists in `data/knowledge/opportunities/`.

1. Read the target opportunity file completely.
2. Read `.cursor/skills/econ-reasoning/SKILL.md` for mechanism analysis framework.
3. Identify the economic mechanism: what market friction or behavioral bias is
   being exploited? What is the predicted sign (long or short the factor)?
4. Design 10-20 expressions that test the mechanism. Vary:
   - Transformation: raw rank, delta, ratio-to-close, z-score
   - Time horizon: d=1, 5, 10, 22
   - Interaction: standalone vs blended with volume or complementary factor
   - Neutralization: MARKET vs SUBINDUSTRY
5. For each expression, state:
   - Expression string (valid FASTEXPR)
   - Predicted sign (positive = long high values)
   - Expected time horizon (how quickly should signal decay?)
   - Mechanism link (which part of the hypothesis does this test?)

## Mode: EXPLOIT

Triggered when a gate-passer from a **genuinely new mechanism family** exists
(not IV-spread, not analyst revision, not fundamental blend). Only apply EXPLOIT
to families with zero representation in `data/factors/` or `data/book/`.

Apply these 8 directed mutations to the base gate-passer expression:

### 1. Operator Swap
Replace core operators with alternatives of similar semantics:
- `ts_mean` ↔ `ts_decay_linear`
- `rank` ↔ `zscore` ↔ `scale`
- `ts_delta` ↔ `ts_pct_change`
- `ts_sum` ↔ `ts_mean`
- `ts_std_dev` ↔ `ts_av_diff`

### 2. Window Sweep
For every time-series operator in the expression, try windows:
d = 3, 5, 10, 20, 40

### 3. Normalization Wrap
Add or remove an outer wrapper:
- Add `rank(...)` to unwrapped expression
- Add `zscore(...)` to unwrapped expression
- Remove `rank()` if already present (test raw signal)
- Try `scale(...)` for unit normalization

### 4. Interaction Add
Multiply or blend with a complementary signal:
- `signal * rank(volume/adv20)` — volume amplification
- `signal + rank(new_factor)` — factor blend
- `signal * rank(1/cap)` — size tilt
- `signal * (1 + rank(buzz))` — sentiment boost

### 5. Sign Flip
If the mechanism supports bidirectional interpretation:
- Negate the entire expression: `rank(-1 * original)`
- Negate only the anchor component

### 6. Complexity Reduce
Simplify nested expressions:
- Remove redundant `rank(rank(...))` → `rank(...)`
- Reduce 4-factor blend to top-2 by removing weakest components
- Replace compound operator with simpler equivalent

### 7. Neutralization Change
Try different neutralization settings:
- MARKET (broad market-neutral)
- SUBINDUSTRY (industry-neutral, often improves Sharpe but raises turnover)
- INDUSTRY (middle ground)
- None (long-only signal, rarely works on BRAIN)

### 8. Decay Sweep
Try different decay settings on the platform:
- decay = 0 (no smoothing, highest turnover)
- decay = 5 (light smoothing)
- decay = 6 (default sweet spot)
- decay = 8 (moderate smoothing)
- decay = 10 (heavy smoothing, lowest turnover)

## Mode: EXPLORE

Triggered as the DEFAULT strategy when the book is near saturation. The goal is
to discover structurally novel alpha expressions — not to re-apply known templates
to new fields (that phase is complete).

**Before generating:** Read `data/knowledge/rules/novelty-required.md` and
`data/knowledge/patterns/` to understand what structures are already proven.
At least 50% of your candidates MUST use templates that differ structurally
from anything in `data/factors/` or `data/knowledge/patterns/`.

### Novel Transformation Templates

These are expression structures that have NOT been systematically tested.
Each represents a different economic hypothesis about how signals combine:

**Conditional / regime-aware:**
- `trade_when(ts_std_dev(returns, 20) > 0.02, signal, ts_std_dev(returns, 20) < 0.01)`
- `trade_when(volume > 2 * adv20, rank(F), volume < 0.5 * adv20)`
- `trade_when(ts_delta(close, 5) < 0, rank(F), ts_delta(close, 5) > 0)`

**Inter-field ratios (value within same dataset):**
- `rank(F1 / F2)` — e.g. `rank(cashflow_op / debt)`, `rank(ebitda / assets)`
- `rank(ts_delta(F1, 5) / ts_std_dev(F1, 20))` — signal-to-noise ratio
- `rank((F1 - F2) / (F1 + F2))` — normalized difference

**Multi-horizon spreads (momentum acceleration / deceleration):**
- `ts_delta(rank(F), 5) - ts_delta(rank(F), 22)` — short vs long momentum
- `zscore(F, 10) - zscore(F, 60)` — regime divergence
- `rank(ts_mean(F, 5) - ts_mean(F, 22))` — moving average crossover

**Directional gating (signal × direction of another):**
- `rank(F) * sign(ts_delta(G, 5))` — F only when G is rising
- `rank(F) * (2 * (ts_delta(close, 5) > 0) - 1)` — F conditional on price direction
- `rank(F) * rank(ts_delta(volume, 5))` — F amplified by volume momentum

**Dynamic correlation / beta:**
- `rank(ts_corr(F, returns, 20))` — stocks whose F co-moves with returns
- `rank(ts_corr(F, volume, 20))` — volume-signal coupling
- `rank(ts_corr(F1, F2, 20))` — inter-factor alignment as alpha

**Non-linear combinations:**
- `rank(F) * rank(F)` — convex weighting of extremes
- `rank(max(F1, F2) - min(F1, F2))` — dispersion between factors
- `rank(abs(ts_delta(F, 5)))` — magnitude regardless of direction

### Cross-Family Interaction Grid

These combine signals from DIFFERENT mechanism families. Each row is a novel
interaction with distinct economic logic:

| Interaction | Expression | Mechanism |
|-------------|-----------|-----------|
| sentiment × options | `rank(scl12_buzz) * rank(IV_call_270 - IV_put_270)` | Attention amplifies vol signal |
| news × fundamental | `rank(news_indx_perf) * rank(ts_delta(ebitda, 1))` | News validates earnings change |
| guidance × options | `rank(max_net_debt_guidance / close) + zscore(ts_mean(IV_call_270 - IV_put_270, 22))` | Guidance + market pricing |
| analyst × sentiment | `rank(anl4_ptp_flag) * rank(-1 * snt_value)` | Revision confirmed by negative buzz |
| options × reversal | `rank(IV_call_270 - IV_put_270) * rank(-1 * returns)` | Vol skew on oversold stocks |
| fundamental × momentum | `rank(cashflow_op / debt) * rank(ts_delta(close, 22))` | Quality with momentum confirmation |
| sentiment × reversal | `rank(-1 * scl12_buzz) * rank(-1 * returns)` | Contrarian on unloved losers |
| guidance × analyst | `rank(min_net_debt_guidance) * rank(anl4_cfi_flag)` | Double-confirmation of outlook |

### Legacy Template Grid (lower priority)

Cross proven transforms against fields — use sparingly (max 20% of budget):

**Transforms** (rows):
- `rank(F)`
- `rank(F / close)`
- `rank(ts_delta(F, 5))`
- `ts_zscore(F, 22)`
- `rank(ts_delta(F, 5) / close)`
- `ts_decay_linear(rank(F), 5)`

**Fields** (columns): Select from `data/reference/brain_data_catalog.md`,
filtering OUT anything listed in `data/knowledge/dead_zones/`. Only use this
grid for fields with zero coverage in `data/factors/`.

## Mode: RECOMBINE

Triggered when 2+ gate-passers exist from **UNEXPLOITED** distinct mechanism
families (families not already well-represented in the book).

### Crossover Blending

1. Select top 2-3 gate-passers from DISTINCT families (e.g., one fundamental,
   one analyst, one sentiment).
2. Decompose each into components:
   - **Anchor**: the primary predictive factor (e.g., `rank(fnd6_drlt/close)`)
   - **Dynamic**: the time-varying transformation (e.g., `ts_delta(F, 5)`)
   - **Stabilizer**: the noise-reduction element (e.g., `* rank(buzz)`, decay)
3. Build new blends by mixing components across families:
   - A's anchor + B's dynamic + C's stabilizer
   - A's anchor + B's anchor (equal weight: `rank(A) + rank(B)`)
   - A's full signal + C's stabilizer
4. Apply the blend template from `data/knowledge/patterns/blend-template.md`
   if it exists.

## Mode: REFINE

Triggered when a gate-passer fails specific BRAIN checks.

### Targeted Fixes

| Check Failure | Fix Strategy |
|---------------|-------------|
| CONCENTRATED_WEIGHT | Simplify expression; add `rank()` wrapper; reduce to fewer factors |
| LOW_SUB_UNIVERSE_SHARPE | Add `* rank(buzz)` or `* rank(volume/adv20)` to broaden coverage |
| HIGH_TURNOVER | Increase decay (try 8, 10, 12); add `ts_decay_linear(..., 5)` wrapper |
| LOW_FITNESS | Increase decay OR remove high-turnover components |
| SELF_CORRELATION | Switch neutralization to MARKET; remove shared components with book |
| LOW_SHARPE | Not a refinement target — discard and move on |
| INCONSISTENCY | Check yearly breakdown; add `trade_when` for regime filtering |

Apply only the fix relevant to the specific failure. Do not over-modify — change
one thing at a time to isolate the effect.

### REFINE anti-patterns (cause wasted sims)

- **Do NOT add `+ rank(buzz)` (or any unitless term) to a `group_neutralize(...)`
  output.** `group_neutralize` preserves the input's unit (e.g. price), and
  adding a unitless `rank()` triggers a BRAIN unit error ("Incompatible unit for
  input of add"). It returns status WARNING and wastes a slot. Use a MULTIPLIER
  instead: `group_neutralize(x, g) * (1 + rank(buzz))`. (Lesson: 20260604-001.)
- **Do NOT keep mutating a family that hits the SAME check failure 3+ times.**
  If `CONCENTRATED_WEIGHT` (or `LOW_SUB_UNIVERSE_SHARPE`) fails across every variant, it is a
  structural block — pivot to a different template. (Lesson: `group_neutralize(IV
  spread)` was always blocked; `zscore(ts_mean(IV spread, 22))` broke through.)

## Output Format

For each candidate expression, provide:

```
EXPRESSION: <valid FASTEXPR string>
MECHANISM: <1-line description of predicted economic mechanism>
SIGN: <positive = long high values / negative = short high values>
DECAY: <recommended platform decay setting>
NEUTRALIZATION: <MARKET / SUBINDUSTRY / INDUSTRY>
PRIORITY: <1-5, where 5 = most likely to gate-pass>
```
