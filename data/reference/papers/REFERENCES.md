# Paper references

This directory previously held full-text markdown conversions of the papers the mining
pipeline drew on. Those conversions were **removed before this repository was published**
and replaced with citations, for two reasons:

1. Redistributing full paper text is a copyright problem, and every paper here is freely
   available from arXiv anyway.
2. The 101 Formulaic Alphas paper is a special case. Its own text states that the
   formulae in Appendix A are proprietary to WorldQuant LLC, reproduced with permission,
   and that *"WorldQuant LLC retains all rights, title and interest in and to the formulae
   and code included in Appendix A hereof and any and all copyrights therefor."* That
   permission was granted to the paper's author and publisher, not to this repository.

If you want to run the paper-ingestion pipeline (`python3 -m alpha_mining --ingest <pdf>`),
download the PDFs yourself from the links below and drop them in this directory. The
pipeline converts them locally; `.gitignore` keeps PDFs and extracted images out of git.

## Foundational

- **101 Formulaic Alphas** — Zura Kakushadze (2015). [arXiv:1601.00991](https://arxiv.org/abs/1601.00991).
  Published in Wilmott Magazine. Defines the formulaic alpha DSL paradigm and reports
  empirical properties (holding periods, turnover, correlation structure). Appendix A is
  WorldQuant LLC property, as noted above.

## LLM-driven alpha mining

- **QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining** — Han, Zhang, Li,
  Yang et al. (2026). [arXiv:2602.07085](https://arxiv.org/abs/2602.07085).
  Trajectory-level mutation and crossover with semantic consistency between hypothesis,
  formula, and code. The closest published analogue to this project's approach.
- **AlphaAgent** (2025). [arXiv:2502.16789](https://arxiv.org/abs/2502.16789).
  Decay-aware alpha generation with regularized exploration.
- **LLM-MCTS for Formulaic Factor Mining** (2025). [arXiv:2505.11122](https://arxiv.org/abs/2505.11122).
  LLM as generative engine for symbolic alphas, with MCTS guided by backtest feedback.
- **Chain-of-Alpha** (2025). [arXiv:2508.06312](https://arxiv.org/abs/2508.06312).
  Addresses the inefficiency of LLM + MCTS approaches.

## Adjacent

- **TradingAgents: Multi-Agents LLM Financial Trading Framework** — Xiao, Sun, Luo, Wang
  (2024). [arXiv:2412.20138](https://arxiv.org/abs/2412.20138).
  Multi-agent debate for trade decisioning rather than formulaic alpha mining; included
  because its agent-orchestration patterns informed the skill design here.

## Further reading

- Awesome-LLM-Quantitative-Trading-Papers: <https://github.com/Tom-roujiang/Awesome-LLM-Quantitative-Trading-Papers>

See `context/llm_alpha_mining_context.md` for how these papers relate to each other and
to the design of this pipeline.
