# LLM-Driven Alpha Mining: Context Brief

> Reference document for an LLM-based alpha mining agent. Compiled as background for a side project building automated formulaic-alpha discovery on the WorldQuant BRAIN platform. All citations link to primary sources.

---

## 1. Problem framing

An **alpha** in the WorldQuant tradition is a deterministic function from past market data to a vector of stock weights, rebalanced at some cadence (typically daily). Long-positive weights, short-negative; magnitudes encode conviction. Dot the weight vector with the next period's returns and you get the daily P&L. Formally, alpha generation is the search problem:

> Find functions `f: HistoricalData → ℝ^N` such that `corr(f(D_t), R_{t+1})` is positive, persistent, and uncorrelated with the existing book of factors.

The bet underpinning the WorldQuant approach (Tulchinsky's framing): the marginal alpha is small (low individual Sharpe, often barely surviving costs), but uncorrelated to existing alphas, and so adds incremental Sharpe to the meta-portfolio. WorldQuant claims a library of ~4 million alphas combined into trading strategies — the "Alpha Factory" model.

The **research funnel inversion** thesis (Two Sigma, 2026): LLMs are widening the top of the funnel — generating hypotheses is now cheap, so the bottleneck shifts from idea generation to evaluation. This makes the LLM × backtester loop the natural unit of automation.
- Source: <https://www.twosigma.com/articles/ai-in-investment-management-2026-outlook-part-i/>
- Caveat (also from Two Sigma Part II): backtests that predate the LLM's knowledge cutoff are suspect, since the model implicitly "knows" about regime shifts. <https://www.twosigma.com/articles/ai-in-investment-management-2026-outlook-part-ii/>

---

## 2. The formulaic alpha tradition

### Canonical reference: 101 Formulaic Alphas

Kakushadze (2016), "101 Formulaic Alphas," arxiv [1601.00991](https://arxiv.org/abs/1601.00991), published in Wilmott Magazine, with WorldQuant's express permission. Empirical properties of the 101 alphas:

- Average holding period: 0.6–6.4 days
- Average pairwise correlation: 15.9% (median 14.3%)
- Returns strongly correlated with volatility
- Turnover has poor explanatory power for alpha correlations
- Mostly price-volume based: `close, open, high, low, volume, vwap`, daily close-to-close returns
- Some use fundamentals (market cap) and industry classifications (GICS, BICS, NAICS, SIC) for industry-neutralization

### Structural patterns the paper popularised

The paper's own formulae are WorldQuant LLC property (see
`data/reference/papers/REFERENCES.md`) and are not reproduced here. The recurring
*shapes*, illustrated with equivalent expressions written for this project:

```
rank(ts_arg_min(high, 20))                    # cross-sectional rank of a timing statistic
-1 * ts_corr(rank(close), rank(adv20), 15)    # negated rank-space correlation
rank(vwap - ts_mean(vwap, 5)) / rank(vwap)    # normalised deviation ratio
```

Read the paper directly at [arXiv:1601.00991](https://arxiv.org/abs/1601.00991) for the
canonical library.

### The DSL: BRAIN Fast Expression language

Alphas are formulaic expressions over price-volume primitives and a fixed operator library. Operator categories:

- **Cross-sectional**: `rank(x)`, `zscore(x)`, `quantile(x)`, `normalize(x)`, `scale(x)` — operate across the universe at a single time
- **Time-series**: `ts_rank(x, d)`, `ts_delta(x, d)`, `ts_mean(x, d)`, `ts_sum(x, d)`, `ts_arg_max(x, d)`, `ts_decay_linear(x, d)`, `ts_delay(x, d)` — operate along the time axis with window `d`
- **Group operators**: `group_neutralize(x, group)`, `group_rank(x, group)`, `group_scale(x, group)`, `group_backfill(x, group, d)` — apply within sector/industry/subindustry/country groups
- **Logical**: `and`, `or`, `not(x)`, `if_else(condition, then, else)`, `trade_when(condition, alpha, exit_condition)` — control flow
- **Data quality**: `winsorize(x)`, `ts_backfill(x, d)` — handle outliers and missing values

The expression language is intentionally restrictive — no arbitrary Python, no neural nets inside BRAIN. This pushes alphas toward interpretability and bounds the overfitting risk.

---

## 3. The WorldQuant BRAIN platform

### What it is

Web-based simulation platform for building and testing alphas. Free to register globally. Hosts ~85,000+ data fields, hundreds of operators, a custom backtesting simulator, and the leaderboard infrastructure.

- Platform URL: <https://platform.worldquantbrain.com>
- Marketing page: <https://www.worldquant.com/brain/>
- Consultant Program: <https://platform.worldquantbrain.com/consultant-program/>

### Scoring

Each submitted alpha is individually scored using a function that weights **Sharpe ratio**, **turnover**, and a custom **fitness** metric:

```
fitness = sqrt(abs(returns) / max(turnover, 0.125)) * sharpe
```

Aggregate scoring at the user level rewards baskets of alphas with strong **and uncorrelated** returns. Daily score cap: 2,000 points. Scores refresh daily at 3 AM EST. Backtest window typically 5+ years.

Submission gates (community-observed; vary by universe):
- Minimum Sharpe ~1.25 (US TOP3000)
- Minimum fitness ~1.0
- Maximum turnover ~70%
- Drawdown caps
- **Self-correlation < 0.7** against your previously submitted alphas — this is the operational bottleneck after ~100 submissions

### Tiers

| Tier | Concurrent sims | API access | Typical compensation |
|------|----------------|------------|----------------------|
| Bronze (1k pts) | 3 | Unofficial wrappers only | None |
| Silver (5k pts) | 3 | Unofficial wrappers only | None |
| Gold (10k pts) | 3 | Unofficial wrappers only | Consultant invitation eligible |
| Master (Consultant) | 10 | Official `wqb` Python SDK + multi-sim | ~$2,000+/quarter |
| Grandmaster (Consultant) | 10 | Official `wqb` Python SDK + multi-sim | ~$8,000+/quarter |

Source for tier details: <https://platform.worldquantbrain.com/consultant-program/>

Concurrency numbers source: <https://deepwiki.com/xiegengcai/world-quant-brain/3-alpha-generation-and-simulation>

### API mechanics

- Endpoint: `https://api.worldquantbrain.com`
- Auth: `POST /authentication` with HTTP Basic credentials, then reuse the returned
  **session cookie** on subsequent calls. If the response omits a `user` object, the
  account requires a Persona biometric challenge, handled by posting to the returned
  `{auth_url}/persona`. See `src/alpha_mining/brain/client.py` for the implementation —
  earlier drafts of this document described a JWT exchange, which is not what the API does.
- Simulation is async: POST alpha + config (region, universe, neutralization, decay, truncation), get job ID, poll until done.
- Per-simulation wall clock: ~30–60s (small universe, 5y) up to 2–5 min (large universe, full history).
- Practical throughput (free tier, 3 slots, 24/7 saturated): ~2,000–5,000 alpha evaluations per day.

### Ownership

Alphas submitted to BRAIN become WorldQuant's property per the BRAIN Agreement. The deal: free industrial-grade backtester + path to part-time income; in exchange, IP belongs to them. Acceptable for skill-building and as a portfolio project; not suitable for proprietary signal development.

### Competitions

- **International Quant Championship (IQC)**: university-team-based, March–September, no submission cap, free entry. <https://www.worldquant.com/brain/iqc/>
- **WorldQuant Challenge / Global Alphathon**: open to individuals, prize pool up to $100k. <https://www.worldquant.com/brain/>

---

## 4. Academic frontier: LLM-driven alpha mining

Chronological progression of the literature:

| Year | Paper | Key contribution |
|------|-------|------------------|
| 2016 | 101 Formulaic Alphas (arxiv [1601.00991](https://arxiv.org/abs/1601.00991)) | Canonical formulaic alpha library; defines the DSL paradigm |
| 2023 | AlphaGPT | Human-in-the-loop LLM alpha mining |
| 2024 | FAMA | LLM in-context learning from existing factor library; chain-of-experience |
| 2025-02 | AlphaAgent (arxiv [2502.16789](https://arxiv.org/abs/2502.16789)) | Closed-loop LLM mining with regularization to counteract alpha decay; 11.0% annual excess on CSI 500 (IR=1.5), 8.74% on S&P 500 (IR=1.05) post-cost over 2021–2024 |
| 2025-05 | LLM-MCTS for Formulaic Factor Mining (arxiv [2505.11122](https://arxiv.org/abs/2505.11122)) | LLM as generative engine for symbolic alphas, MCTS guided by backtest feedback |
| 2025-08 | Chain-of-Alpha (arxiv [2508.06312](https://arxiv.org/abs/2508.06312)) | Addresses inefficiency of LLM+MCTS approaches |
| 2026-02 | QuantaAlpha (arxiv [2602.07085](https://arxiv.org/abs/2602.07085)) | Trajectory-level mutation/crossover; semantic consistency across hypothesis/formula/code; on CSI 300 with GPT-5.2: IC 0.1501, ARR 27.75%, MDD 7.98%; transfers to S&P 500 with 137% cumulative excess over 4 years |

Adjacent / related:
- **AlphaQuanter** (HKUST) — tool-orchestrated agentic RL for stock trading
- **Alpha-R1** (Finstep, SJTU, Dec 2025) — alpha screening with LLM reasoning via RL
- **RD-Agent** (Microsoft) — multi-agent framework decoupling research and development stages
- **TradingAgents** (UCLA/MIT, arxiv [2412.20138](https://arxiv.org/abs/2412.20138)) — multi-agent debate framework (less relevant to formulaic alpha mining, more to trade decisioning)

Curated reading list: **Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers** at <https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers>

### Methodological caveats from the literature

1. **Alpha decay**: McLean & Pontiff (2016) — published anomalies show ~58% post-publication decay. Paper-derived signals must be re-validated on recent OOS data.
2. **Crowding**: many LLM-generated alphas converge on similar regions of formula space. AlphaAgent and QuantaAlpha both add explicit redundancy/complexity controls.
3. **LLM contamination**: pre-trained LLMs may implicitly know about historical regime shifts (pandemic, AI boom). Backtests in those windows are suspect.
4. **Reported numbers are usually optimistic**: most papers test on small symbol universes over short windows, with limited post-cost analysis.

---

## 5. Production hedge fund context

How institutional players are deploying LLMs in research workflows. Useful for understanding the production frontier rather than only academic toy systems.

- **Two Sigma**: AI-first internal mandate, "operational alpha" framing. All employees expected to integrate frontier LLMs across research, infra, compliance.
- **Bridgewater AIA Labs**: 17-person Greg Jensen lab, replicating Ray Dalio's macro process end-to-end via LLM-heavy workflow. Already trading client capital on AWS EKS.
- **Balyasny (BAM)**: private "BAM ChatGPT" hosted on Azure connecting 10 data pipes; live for all 2,000 staff; "Deep Research" bot indexes 5M documents.
- **D.E. Shaw**: federated Assistants–LLM Gateway–DocLab stack; desk-level customization with central governance (PII stripping, prompt logging).
- **Numerai**: rebuilding for autonomous research with MCP interface — agents will create models, submit predictions, run validation, and monitor performance end-to-end.
- **Citadel**: aborted Seattle AI lab — top AI scientists couldn't win discretionary PM trust. Cautionary tale on cultural integration.

Common architectural patterns: air-gapped models (Point72 in Azure V-Net); human-in-the-loop veto on every trading decision; provenance/audit logging tied to every retrieval.

Source: <https://resonanzcapital.com/insights/ai-use-by-hedge-funds-made-tangible-from-lego-bots-to-alpha-assistants>

---

## 6. Open-source ecosystem

### BRAIN API clients (community wrappers, free-tier compatible)

- **RussellDash332/WQ-Brain** — clean reference for auth/submission flow. <https://github.com/RussellDash332/WQ-Brain>
- **AbnerTeng/WorldQuant-Brain** — upstream most others fork from
- **pyworldquant** (PyPI) — pip-installable wrapper
- **zhutoutoutousan/worldquant-miner** — full LLM-driven mining system with Ollama, Docker, daily-rate-limit-aware orchestration. <https://github.com/zhutoutoutousan/worldquant-miner>

### Reference architecture: Brainiac

**jdhruv1503/Brainiac** at <https://github.com/jdhruv1503/Brainiac> (48 stars, 20 forks, 5 commits — small project, useful as template not turnkey tool).

Pipeline:

```
Research PDFs
    ↓ LlamaParse (PDF → markdown extraction)
Structured paper content
    ↓ LangChain + DeepInfra LLM (hypothesis extraction)
Alpha hypothesis (natural language)
    ↓ LLM prompt (Fast Expression translation)
BRAIN Fast Expression formula
    ↓ LlamaIndex RAG (BRAIN dataset retrieval)
Formula + dataset config
    ↓ RussellDash332/WQ-Brain client (BRAIN API)
Backtest results → SQLite (Simulation/alphas/alpha_results.db)
```

Stack: LangChain (orchestration), LlamaParse (PDF parsing), LlamaIndex (RAG), DeepInfra (LLM inference), SQLite (persistence).

**Honest assessment**: README claims "agentic RL framework" but the actual code is stateless LLM prompting with retry logic — no policy gradient, no value function, no reward feedback loop. Self-correlation gating (the actual operational bottleneck) is missing. USA datasets and continuous learning are listed as future enhancements.

The architecturally interesting bet: **research-paper-driven generation** rather than blind formula-space exploration. Higher prior on signal quality, automatic interpretability, less crowding sensitivity. Trade-off: most published anomalies have decayed.

### Broader awesome lists

- **wilsonfreitas/awesome-quant** — most comprehensive index of quant libraries; growing AI-quant-agents section. <https://github.com/wilsonfreitas/awesome-quant>
- **kennethleungty/Finance-LLMs** — financial services LLM applications. <https://github.com/kennethleungty/Finance-LLMs>
- **adlnlp/FinLLMs** — survey paper resources. <https://github.com/adlnlp/FinLLMs>
- **LLMQuant** organization — open-source AI4Quant infrastructure including data-mcp (MCP server for financial data). <https://github.com/LLMQuant>

---

## 7. Suggested architecture for the side project

### Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. CORPUS                                                        │
│    SSRN papers + 101 alphas + textbook anomalies (Fama-French,  │
│    momentum, post-earnings drift, low-vol, accruals, ...)        │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. EXTRACTION (LlamaParse / Marker / MinerU)                     │
│    PDF → structured markdown; preserve tables, equations         │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. HYPOTHESIS GENERATION (LLM via Fireworks)                     │
│    Paper → list of (mechanism, predicted sign, time horizon,     │
│    relevant data fields)                                         │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. FORMULA TRANSLATION (LLM with operator vocabulary in prompt) │
│    Hypothesis → Fast Expression formula                          │
│    Validate syntactically against grammar before submission      │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. PRE-FILTERS                                                   │
│    - Complexity bound (operator count, depth)                    │
│    - Static analysis: type checks, NaN safety                    │
│    - Optional local rank-IC prescreen on price-volume fields     │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 6. BRAIN BACKTEST (free tier: 3 concurrent sims)                 │
│    Submit, poll, retrieve metrics                                │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 7. EVALUATION + STORAGE (SQLite or DuckDB)                       │
│    Persist (paper_id, hypothesis, formula, IC, Sharpe,           │
│    turnover, fitness, drawdown, correlation_against_book)        │
└────────────────────────────┬────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│ 8. FEEDBACK LOOP                                                 │
│    a. In-context RL: replay top-quartile (paper, formula,        │
│       result) tuples as few-shot examples for next generation    │
│    b. Optional: instruction-tune small open model on              │
│       successful trajectories (Fireworks fine-tuning)            │
└─────────────────────────────────────────────────────────────────┘
```

**How this differs from what was actually built.** Two corrections worth recording, since
the design above was written before implementation:

- **Self-correlation cannot be a pre-filter.** It needs a realised PnL series, which only
  exists after a backtest, so it moved to step 6.5 (`scripts/pnl_correlation.py` plus
  BRAIN's authoritative `/alphas/{id}/check`). `src/alpha_mining/pipeline/prefilter.py`
  does syntax and complexity checks only. This turned out to be the single most
  consequential difference: because the gate is post-backtest, every candidate costs a
  simulation before you learn whether it is admissible.
- **Step 8's feedback loop stayed in-context.** No fine-tuning happened. The "memory"
  that made iteration work is the file-based knowledge base under `data/knowledge/`,
  read by the agent at the start of each session, not a trained policy.

### Concrete next steps

1. Register on BRAIN. Manually submit 5–10 alphas via web UI to internalize operator semantics and what "good" looks like empirically.
2. Fork RussellDash332/WQ-Brain. Verify auth + submission round-trip with a hardcoded alpha from the 101 paper.
3. Build the minimum viable pipeline: hardcoded paper → hypothesis → formula → BRAIN backtest, end-to-end, no agent loop.
4. Add self-correlation gating against submitted alphas — highest-leverage missing piece in Brainiac.
5. Add the in-context RL loop: log all (paper, formula, result) tuples; sample top-quartile for few-shot prompting on the next generation. No GPU, no actual training, but meaningfully better than stateless prompting.
6. Target: 10,000 BRAIN points / Gold tier as the project milestone. This is concrete, externally validated, and directly demonstrates the system works.
7. Optional stretch: instruction-tune a small open model (Llama 3 8B or similar) on successful trajectories using Fireworks fine-tuning.

### What makes this approach distinctive

- The pipeline is genuinely novel — most LLM-finance side projects are sentiment analysis or earnings call summarization, not closed-loop alpha mining.
- BRAIN tier is a hard, externally-validated metric rather than a self-reported backtest.
- Sits at the intersection of LLM/agent infrastructure and quantitative finance.
- Connects to the recent academic frontier (cite QuantaAlpha, AlphaAgent, Chain-of-Alpha as influences).

---

## 8. Open research directions

Genuine open problems where a contribution is plausible:

- **Multi-objective alpha selection**: existing fitness function is scalar (Sharpe-weighted). Pareto-optimal selection over (Sharpe, turnover, complexity, decay rate, correlation) is an open MORL problem. Direct connection to MOBORL-style preference-conditioned policies.
- **Decay-aware generation**: most LLM mining frameworks score on backtest IC; very few explicitly model post-publication decay or alpha lifetime. AlphaAgent gestures at this with regularized exploration but doesn't fully solve it.
- **Cross-market transfer**: QuantaAlpha shows factors mined on CSI 300 transfer to S&P 500. Why? What invariants does the LLM capture? This is an interesting interpretability question.
- **Symbolic vs. neural alpha trade-off**: formulaic alphas are interpretable but expressively limited. When does a small neural network outperform symbolic, and at what interpretability cost?
- **LLM contamination control**: how do you robustly evaluate LLM-generated alphas on backtests covering windows in the training data? Possible approaches: synthetic regime construction, time-truncated evaluation, distribution-shift stress tests.

---

## 9. Key URLs (consolidated)

### Platform and competitions
- BRAIN platform: <https://platform.worldquantbrain.com>
- BRAIN marketing: <https://www.worldquant.com/brain/>
- IQC 2026: <https://www.worldquant.com/brain/iqc/>
- IQC Guidelines: <https://www.worldquant.com/brain/iqc-guidelines/>
- Consultant Program: <https://platform.worldquantbrain.com/consultant-program/>
- BRAIN API base: `https://api.worldquantbrain.com`

### Foundational papers
- 101 Formulaic Alphas: <https://arxiv.org/abs/1601.00991>
- AlphaAgent: <https://arxiv.org/abs/2502.16789>
- LLM-MCTS: <https://arxiv.org/abs/2505.11122>
- Chain-of-Alpha: <https://arxiv.org/abs/2508.06312>
- QuantaAlpha: <https://arxiv.org/abs/2602.07085>
- TradingAgents: <https://arxiv.org/abs/2412.20138>

### Reference repos
- RussellDash332/WQ-Brain: <https://github.com/RussellDash332/WQ-Brain>
- jdhruv1503/Brainiac: <https://github.com/jdhruv1503/Brainiac>
- zhutoutoutousan/worldquant-miner: <https://github.com/zhutoutoutousan/worldquant-miner>
- Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers: <https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers>
- wilsonfreitas/awesome-quant: <https://github.com/wilsonfreitas/awesome-quant>
- LLMQuant org: <https://github.com/LLMQuant>

### Industry context
- Two Sigma 2026 outlook Part I: <https://www.twosigma.com/articles/ai-in-investment-management-2026-outlook-part-i/>
- Two Sigma 2026 outlook Part II: <https://www.twosigma.com/articles/ai-in-investment-management-2026-outlook-part-ii/>
- Resonanz Capital hedge fund AI deep-dive: <https://resonanzcapital.com/insights/ai-use-by-hedge-funds-made-tangible-from-lego-bots-to-alpha-assistants>
