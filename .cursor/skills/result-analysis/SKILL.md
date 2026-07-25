---
name: result-analysis
description: >-
  Analyze simulation results from the HF server. Filter gate-passers, run
  BRAIN checks, compute self-correlation, and produce submission viability
  verdicts. Trigger on: analyze, results, gate-passer, viability, check.
---

# Result Analysis — Gate-Passer Evaluation

Analyze simulation results, filter candidates, run validation checks, and
produce actionable verdicts on submission viability.

## Step 1: Filter Gate-Passers

First make sure the batch is finished (poll to completion):

```bash
uv run python3 scripts/hf_poll.py --tag <session_tag>
```

Then query the HF server for gate-passers from this session's tag:

```bash
uv run python3 scripts/hf_query.py --gate-passers --tag <session_tag>
```

(`--tag` filters by a substring of `tags_json`; it works with `--gate-passers`
and `--new-24h`.)

Apply minimum thresholds:
- Sharpe >= 1.25
- Fitness >= 1.0
- Turnover between 1% and 70%

If no candidates pass all three, the round produced no gate-passers.
Document the best metrics achieved and return to signal generation with
updated context.

## Step 2: Auto-Classify Family

For each gate-passer, extract the mechanism family from the expression text:

| Field Prefix | Family |
|-------------|--------|
| `fnd6_*` | fundamental (balance sheet / income statement) |
| `anl4_*` | analyst (estimates, revisions, flags) |
| `scl12_*` | sentiment (social, buzz, scores) |
| `opt8_*` / `implied_volatility_*` | options (IV, skew, spreads) |
| `open`, `close`, `volume`, `returns`, `adv*` | price-volume (PV) |
| `mdl16_*` / `mdl51_*` | model (quantitative scores) |
| `nws12_*` / `nws18_*` | news (events, sentiment) |
| Mixed prefixes | blend |

Cross-reference with `data/factors/` to check if this field has been seen before.
If a factor file exists, note its known mechanism and prior results.

## Step 3: BRAIN Checks

For each gate-passer, run the BRAIN submission checks:

```bash
uv run python3 scripts/brain_check.py --alpha-ids <id1> <id2> ...
```

The checks BRAIN returns are:
1. **LOW_SHARPE** — Sharpe ratio too low (min ~1.25)
2. **LOW_FITNESS** — Fitness too low (min 1.0)
3. **LOW_TURNOVER** — Turnover too low
4. **HIGH_TURNOVER** — Turnover too high (max 0.70)
5. **CONCENTRATED_WEIGHT** — Position weights too concentrated
6. **LOW_SUB_UNIVERSE_SHARPE** — Sub-universe Sharpe too low
7. **SELF_CORRELATION** — Too correlated with the existing book
8. **MATCHES_COMPETITION** — Too similar to public examples

### CRITICAL: "ALL PASS" from brain_check does NOT include self-correlation

`scripts/brain_check.py` reads `GET /alphas/{id}` (alpha detail). On that payload,
`SELF_CORRELATION` is often stuck at `PENDING` even after the dedicated
`GET /alphas/{id}/check` endpoint has already resolved PASS/FAIL. `brain_check.py`
only counts explicit `FAIL`s, so it reports "ALL PASS" even when self-corr is
still unverified on the detail view.
**Never treat a brain_check "ALL PASS" as evidence that self-corr is acceptable.**
Self-corr MUST be verified in Step 4 via `--brain-check` (polls `/check` until
terminal) or `--vs-book` (local PnL fallback) against the CURRENT book before any
candidate is called submittable. See `data/knowledge/rules/self-corr-check-long-poll.md`.

Record which of the 7 computable checks pass/fail. A candidate must pass all of
them AND clear the Step 4 self-corr gate to be viable for submission.

## Step 4: Self-Correlation (the binding gate)

This is the REAL submission gate, not Step 3. BRAIN's self-correlation check uses
a **TWO-GATE system** (not a simple threshold):

### How BRAIN's Self-Correlation Check Actually Works

1. **Gate 1 (correlation threshold):** Is max PnL correlation > 0.7 against ANY
   submitted alpha in the user's book?
2. **Gate 2 (Sharpe premium):** If Gate 1 triggered, is the candidate's Sharpe
   >= 1.10× the max Sharpe among all peers with correlation > 0.7?

Decision logic:
- No peer exceeds 0.7 correlation → **auto-PASS** regardless of Sharpe
- Peers exceed 0.7 BUT candidate Sharpe >= 1.1× max peer Sharpe → **PASS** (Sharpe premium override)
- Peers exceed 0.7 AND candidate Sharpe < 1.1× max peer Sharpe → **FAIL**

### Preferred path: BRAIN API verification (authoritative)

Poll `GET /alphas/{id}/check` until `SELF_CORRELATION` is terminal
(`PASS` / `FAIL` / `ERROR`). This is GET-only (`POST` returns 405). Under peak
load expect empty-body long-poll, multi-minute PENDING, and transient 502/429:

```bash
uv run python3 scripts/pnl_correlation.py --alphas <id1> <id2> --brain-check
# raise budget under load (default 900s)
uv run python3 scripts/pnl_correlation.py --alphas <id1> --brain-check --max-wait-seconds 1800
```

For a full correlation breakdown (shows which book entries trigger Gate 1):

```bash
uv run python3 scripts/pnl_correlation.py --alphas <id1> <id2> --brain-corr
```

This is the **only authoritative** self-corr verification. Always prefer this
over local PnL computation when BRAIN API access is available. Trust terminal
`result`, not `value` alone (Sharpe premium). Never coerce `PENDING`/`TIMEOUT`
to FAIL — re-poll later.

### Cloud agent path (uses server-computed self-corr)

The HF server computes self-corr for every gate-passer as part of its worker
pipeline and stores it in `jobs.self_corr`. The server book is synced nightly
from `data/book/*.md` via `scripts/sync_server_book.py`.

Read it from the `--gate-passers` output (self-corr is included automatically):

```bash
uv run python3 scripts/hf_query.py --gate-passers --tag <session_tag> --self-corr-check
```

If `self_corr` is NULL / UNCHECKED, it means the server hasn't computed it yet
(the worker processes gate-passers in order). Wait for the batch to complete or
fall back to the BRAIN API path above (preferred) or local path below.

### Local PnL path (fallback pre-filter only)

```bash
uv run python3 scripts/pnl_correlation.py --alphas <id1> <id2> --vs-book
```

`pnl_correlation.py` reads ACTIVE entries from `data/book/*.md` (PENDING entries
are excluded — they are candidates, not yet submitted), fetches PnL curves from
the BRAIN API, and computes Pearson correlation on daily returns over a 4-year
window.

**WARNING: Local PnL correlation underestimates BRAIN's self-corr when alphas
share raw data fields** (e.g. same `implied_volatility_*` or `fnd6_*` inputs).
BRAIN likely correlates at the position/weight level, producing a 1.45–1.6×
multiplier over return-level correlation. See
`data/knowledge/rules/self-corr-pnl-gap.md` for evidence and multiplier table.

Use local PnL as a quick pre-filter only:
- PnL corr < 0.35 (shared fields) or < 0.60 (no shared fields): likely SAFE
- PnL corr > 0.50 (shared fields) or > 0.70 (no shared fields): likely BLOCKED
- Between: inconclusive — must use `--brain-check` for authoritative answer

### Thresholds summary

| Check Method | SAFE | Inconclusive | BLOCKED |
|-------------|------|--------------|---------|
| `--brain-check` (authoritative) | result=PASS | — | result=FAIL |
| `--brain-corr` (raw correlation) | max corr < 0.7 | corr > 0.7 but Sharpe premium unclear | corr > 0.7, Sharpe < 1.1× peer |
| `--vs-book` (local PnL, no shared fields) | < 0.60 | 0.60–0.70 | > 0.70 |
| `--vs-book` (local PnL, shared fields) | < 0.35 | 0.35–0.50 | > 0.50 |

Record the measured max self-corr and check result; written to the book entry as
`self_corr_max` and gates whether a `submit-*.md` queue entry is created (Step 8).

## Step 5: Greedy De-Duplication & Long-Term Priority Ordering

When multiple candidates pass, de-duplicate to avoid wasting submission slots
on correlated signals:

1. Sort all passing candidates by |Sharpe| descending.
2. Initialize the "keep" set as empty.
3. For each candidate (highest Sharpe first):
   a. Compute max |correlation| vs every alpha already in the "keep" set.
   b. Compute max |correlation| vs every alpha in the submitted book.
   c. If BOTH max values < 0.70, add to the "keep" set.
   d. Otherwise, mark as REDUNDANT (unless candidate Sharpe >= 1.1× peer Sharpe).

This greedy algorithm ensures maximum diversity in the final candidate set.

### Submission Order: Minimize Correlation Budget Consumption

After de-duplication, assign **submission priority** within the keep set using
a long-term point-maximization strategy:

1. **Primary sort: lowest self-corr ascending.** Each submitted alpha becomes a
   new peer in future self-corr checks. A submission at self-corr=0.3 leaves far
   more correlation headroom for future alphas than one at self-corr=0.65. Submit
   the least-correlated candidates first to preserve the book's capacity.

2. **Secondary sort: grade descending (SPECTACULAR > EXCELLENT > GOOD).**
   Among candidates with similar self-corr, prefer higher grade for more points
   per submission. Only EXCELLENT+ candidates warrant prioritized promotion.

3. **Tertiary sort: Sharpe descending.** Tie-breaker within same grade tier.

**Highlight rule:** Flag any EXCELLENT+ candidate with self-corr < 0.4 as
`priority: high` — these are the most valuable long-term assets because they
contribute points while minimally constraining future submissions. Mark them
clearly in session notes and book entries for future reference even if not
submitted immediately.

## Step 6: Verdict

For each candidate, assign a verdict:

| Verdict | Criteria |
|---------|----------|
| **SAFE** | All 7 computable BRAIN checks pass AND `--brain-check` returns result=PASS |
| **RISKY** | All 7 computable BRAIN checks pass AND BRAIN check unavailable (e.g. cloud path with server-computed corr only), but local/server self-corr in inconclusive range |
| **BLOCKED** | Any BRAIN check fails OR `--brain-check` returns result=FAIL |
| **REDUNDANT** | Passed checks but correlated with a higher-Sharpe keeper |

## Output

Produce a ranked table:

```
| Rank | Alpha ID | Expression (truncated) | Sharpe | Fitness | Family | Max Self-Corr | Verdict |
|------|----------|----------------------|--------|---------|--------|---------------|---------|
| 1    | ABC123   | rank(fnd6_drlt/cl...) | 2.41   | 2.85    | fund   | 0.42          | SAFE    |
| 2    | DEF456   | ts_decay_linear(r...) | 2.15   | 2.10    | blend  | 0.58          | RISKY   |
| ...  | ...      | ...                   | ...    | ...     | ...    | ...           | ...     |
```

For each SAFE or RISKY candidate, also provide:
- Full expression string
- Platform URL: `https://platform.worldquantbrain.com/alpha/<alpha_id>`
- Recommended submission order (lowest self-corr first, then grade descending,
  then Sharpe descending — see Step 5 priority ordering)
- Risk assessment (what could cause rejection despite passing checks)
- **Long-term value flag**: mark EXCELLENT+ candidates with self-corr < 0.4 as
  "HIGH LONG-TERM VALUE" — these maximize cumulative points by preserving
  correlation headroom for future submissions

## Step 7: Label Candidate on BRAIN + Record PENDING

CRITICAL: alphas simulated through the HF queue exist on the BRAIN platform but
have NO name/tags/description until you label them. A local `data/book/<id>.md`
does NOT propagate to the platform. For every SAFE or RISKY candidate:

1. Create `data/book/<id>.md` with `status: PENDING` and frontmatter including
   `name`, `tags`, `family`, `expression`, `neutralization`, `decay`,
   `self_corr_max`, and `brain_url` (see `experiment-reporting` template).

2. Push that metadata to the BRAIN platform (metadata only, does NOT submit):
   ```bash
   uv run python3 scripts/brain_metadata.py --alpha-id <id> --from-book data/book/<id>.md
   ```
   Or with explicit flags:
   ```bash
   uv run python3 scripts/brain_metadata.py --alpha-id <id> \
     --name "<name>" --tags "tag1,tag2" --desc "<mechanism summary>"
   ```

3. Leave the official submit to the human (local mode) — `brain_metadata.py`
   never submits. Cloud automation NEVER submits.

## Step 8: Add to the submission queue

For every SAFE/RISKY candidate (verified self-corr in Step 4), create a queue
entry at `data/knowledge/opportunities/submit-<alpha_id_lowercase>.md`. This is
the single surface the human reviews each day to decide what to submit. Schema:

```markdown
---
type: "submit-candidate"
alpha_id: "<id>"
status: "QUEUED"            # QUEUED | SUBMITTED | REJECTED
priority: "<high|medium|low>"
grade: "<SPECTACULAR|EXCELLENT|GOOD|AVERAGE>"
sharpe: <value>
fitness: <value>
turnover: <value>
self_corr_max: <measured vs current book>
neutralization: "<MARKET|SUBINDUSTRY|INDUSTRY>"
decay: <value>
family: "<mechanism family>"
session: "YYYYMMDD-NNN"
brain_url: "https://platform.worldquantbrain.com/alpha/<id>"
queued: "YYYY-MM-DD"
long_term_value: "<HIGH|MEDIUM|LOW>"
---
```

### Priority & Long-Term Value Assignment

Assign `priority` and `long_term_value` based on the cumulative-points strategy
(see `data/knowledge/rules/submission-priority-long-term.md`):

| Grade | Self-Corr | Priority | Long-Term Value |
|-------|-----------|----------|-----------------|
| SPECTACULAR, any corr (PASS) | any | high | HIGH |
| EXCELLENT+ & self-corr < 0.4 | < 0.4 | high | HIGH |
| EXCELLENT+ & self-corr 0.4–0.6 | 0.4–0.6 | medium | MEDIUM |
| EXCELLENT+ & self-corr 0.6–0.7 | 0.6–0.7 | medium | LOW |
| GOOD & self-corr < 0.4 | < 0.4 | medium | MEDIUM |
| GOOD & self-corr >= 0.4 | >= 0.4 | low | LOW |
| AVERAGE (any) | any | low | LOW |

**Rationale**: Low self-corr + high grade = maximum cumulative points over time.
These alphas both contribute their own points AND minimally constrain future
submissions. Always submit them first.

# Submit <alpha_id> (<short family>)

## Expression
`<full FASTEXPR expression>`

## Why submittable
- Self-corr <value> vs current book (<SAFE|RISKY>); all computable BRAIN checks pass.
- Grade <grade>, S=<>, F=<>.

## Reviewer action
Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/<id>.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
```

Only create a queue entry when self-corr was actually measured this session
(never on a `brain_check` "ALL PASS" alone). Cloud automation writes `QUEUED`;
the human flips the status after acting on the platform.

Query the open queue any time with:
```bash
uv run python3 scripts/parse_frontmatter.py --dir data/knowledge/opportunities \
  --filter "status=QUEUED" --field alpha_id,grade,self_corr_max,brain_url
```

## Iteration Signal

If this round produced:
- **0 gate-passers**: Signal generation needs a strategy pivot. Recommend changing mode or target.
- **Gate-passers but all BLOCKED**: Identify the blocking reason. If self-corr, recommend MARKET neutralization or different family. If check failure, recommend REFINE mode.
- **SAFE or RISKY candidates**: Session is productive. Continue iterating if budget allows, or proceed to recording.
