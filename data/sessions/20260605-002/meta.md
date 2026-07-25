---
id: "20260605-002"
date: "2026-06-05"
strategy: "INFRASTRUCTURE"
research_question: "Build sweep analysis tooling, factor knowledge base, and PnL backfill infrastructure"
budget_used: 0
budget_cap: null
trigger: "manual"
gate_passers: 0
submissions: 1
status: "productive"
tags:
  - "sweep_analysis"
  - "factor_profiles"
  - "pnl_backfill"
  - "infrastructure"
---

# Session 20260605-002: Sweep Analysis, Factor KB, and PnL Infrastructure

## What Was Built

### 1. Sweep Analysis Tooling (`local/sweep_analysis/`)

Extracted and analyzed 21,442 mono-factor sweep results from the HF server.

**Scripts:**
- `extract_sweep.py` -- Pulls all sweep/cluster-tagged results, parses expressions into field/template/dataset/universe, extracts BRAIN check results, saves to `sweep_data.csv`
- `analyze_sweep.py` -- 5-layer analysis:
  - 2a: Dataset landscape (signal density by dataset)
  - 2b: Template effectiveness (rank vs delta vs value-norm by dataset)
  - 2c: Field ranking (top fields per dataset, global top-20)
  - 2d: Universe sensitivity (TOP200 vs TOP3000 signal scaling)
  - 2e: Check failure analysis (submittability gap)
- `fetch_pnl.py` -- Fetches daily PnL from BRAIN API with manifest-based cache, rate limit handling, concurrency support
- `analyze_pnl.py` -- Temporal decomposition, inter-factor correlation, regime analysis, complementarity scoring
- `generate_factor_profiles.py` -- Generates structured factor profile markdown files
- `upload_pnl_to_hf.py` -- Uploads local PnL cache to HF Storage Bucket

**Key findings:**
- fundamental6 and analyst4 are the productive datasets; option9/model16/pv1/socialmedia are dead
- `rank(F/close)` wins for fundamentals; `rank_delta` wins for options; analyst flags prefer raw `rank(F)`
- Signals scale broadly (TOP3000 best for fundamentals); news signals concentrated in TOP200
- 172 gate-passers but only 30 pass all BRAIN checks (CONCENTRATED_WEIGHT blocks 21%, LOW_SUB_UNIVERSE_SHARPE blocks 31%)
- `fnd6_itci`, `sales_estimate_count`, `anl4_ptp_flag` are the most consistent factors (100% positive years, all-weather regime)
- `anl4_epsr_flag` is the top complementary factor (negatively correlated with fundamental value fields)

### 2. Factor Profile Knowledge Base (`data/knowledge/factor_profiles/`)

1,072 structured markdown profiles with YAML frontmatter for every field with Sharpe >= 0.5. Each contains:
- Signal profile across templates (rank, delta, value-norm, decay, trade_when)
- BRAIN check failure summary
- Temporal behavior (yearly Sharpe breakdown, consistency)
- Regime profile (bull/sideways/bear Sharpe)
- Correlation notes (top 5 correlates)
- Actionability assessment (submittability, untried templates)

### 3. PnL Backfill Infrastructure (HF Server + GHA)

**Architecture**: Metadata in SQLite `pnl_metadata` table; bulk PnL data in an HF Storage Bucket (`<hf-user>/alpha-mining-pnl`).

**Server changes** (`server/` submodule):
- `pnl_metadata` table replaces old `pnl_cache` (18k rows vs would-have-been 22M)
- `pnl_storage.py` -- HF bucket upload/download via `huggingface_hub`
- `pnl_backfill.py` -- Background worker with batch stop on rate limit, consecutive failure detection
- `routers/pnl.py` -- POST /v1/pnl/backfill, GET /v1/pnl/status, GET /v1/pnl/{id}, POST /v1/pnl/seed-metadata
- `brain_client.py` -- Fixed: empty 200 handling (genuine empty vs rate limit), Retry-After float parsing
- `self_correlation.py` -- Updated to read PnL from bucket instead of DB

**GHA workflow** (`.github/workflows/hourly-pnl-backfill.yml`):
- Hourly cron at :15, wakes Space, triggers backfill, logs status
- Default limit: 2,000/hour (matches BRAIN's PnL rate limit)

**BRAIN rate limits discovered:**
- PnL endpoint: 2,000/hour (separate counter from simulations)
- Auth endpoint: 5/minute
- Simulation endpoints: separate per-minute limits
- BRAIN returns 200+empty body as a **long-poll** signal (Retry-After header); must retry.
  See `data/knowledge/rules/pnl-long-poll-required.md` for corrected understanding.

**State as of 2026-06-05 (OUTDATED — see correction below):**
- 9,606 alphas with PnL data (ok)
- 9,855 alphas marked empty — **CORRECTION (2026-07-05):** these were falsely marked
  empty due to missing long-poll retry logic. All alphas have PnL regardless of grade.
  Fixed in server commit `c2b4c04`.
- 0 errors, 2 pending (new sims)

### 4. Alpha Submission

- **npWYoqQz** submitted and ACTIVE: SPECTACULAR F=3.02, self-corr 0.456 (SAFE)
  - IV-dlto-itci-netdebt MARKET hybrid
  - Highest fitness ever in the project

## Pending Actions for Next Session

1. **Rerun analysis with full PnL data** -- `analyze_pnl.py` and `generate_factor_profiles.py` were run with 50 alphas; rerun with all 9,606 for comprehensive profiles
2. **Submit remaining SPECTACULAR candidates** from PR #30: gJ3wPdlK (F=2.84), d5QeRVvw (F=2.51), Vk8qOqV8 (F=2.84)
3. **Merge PR #30**, close PR #21 (duplicate)
4. **Fix bucket access from server** -- `seed-metadata` endpoint fails because `huggingface_hub` bucket API needs debugging on HF Space
5. **Deep-dive data analysis** -- the sweep data and PnL corpus are ready for the next phase of factor intuition building
