"""
Prompt templates for hypothesis extraction and formula translation.

Each template has slots for dynamic content (few-shot examples, paper text,
operator vocabulary). Templates use str.format() for simplicity.
"""

from ..brain.constants import get_operator_vocabulary_text

# ---------------------------------------------------------------------------
# System prompts
# ---------------------------------------------------------------------------

SYSTEM_ALPHA_RESEARCHER = """\
You are a quantitative researcher specializing in formulaic alpha discovery \
for equity markets. You have deep knowledge of factor investing, price-volume \
anomalies, and the WorldQuant BRAIN Fast Expression language.

You are methodical, precise, and skeptical of overfitting. When generating \
hypotheses, you always specify the economic mechanism, expected sign, and \
time horizon. When writing formulas, you use only operators from the provided \
vocabulary and validate that expressions are syntactically correct."""

# ---------------------------------------------------------------------------
# Hypothesis extraction from research papers
# ---------------------------------------------------------------------------

HYPOTHESIS_EXTRACTION_TEMPLATE = """\
Below is content extracted from a financial research paper. Your task is to \
identify tradeable alpha hypotheses that can be expressed as formulaic alphas \
on the WorldQuant BRAIN platform.

For each hypothesis, provide:
- mechanism: A 1-2 sentence description of the economic mechanism
- predicted_sign: Whether the factor predicts positive or negative returns ("positive" or "negative")
- time_horizon: Expected holding period ("intraday", "1-5 days", "5-20 days", "20+ days")
- relevant_fields: List of data fields needed (from: {fields})
- confidence: Your confidence this is a real anomaly vs. data mining artifact ("high", "medium", "low")

Focus on:
1. Anomalies with clear economic mechanisms (not just statistical patterns)
2. Factors expressible with price-volume data (close, open, high, low, volume, vwap, returns)
3. Holding periods under 20 days (BRAIN alphas are short-horizon)

Ignore:
- Factors requiring fundamental data we don't have
- Long-horizon (monthly+) effects
- Effects that have clearly decayed post-publication

{few_shot_examples}

--- PAPER CONTENT ---
{paper_content}
--- END PAPER CONTENT ---

Extract all viable hypotheses as a JSON array."""

# ---------------------------------------------------------------------------
# Formula translation
# ---------------------------------------------------------------------------

FORMULA_TRANSLATION_TEMPLATE = """\
Translate the following alpha hypothesis into a BRAIN Fast Expression formula.

{operator_vocabulary}

HYPOTHESIS:
- Mechanism: {mechanism}
- Predicted sign: {predicted_sign}
- Time horizon: {time_horizon}
- Relevant fields: {relevant_fields}

RULES:
1. Use ONLY operators and fields from the vocabulary above
2. The expression must be a single formula (no variable assignments)
3. Use rank() or zscore() for cross-sectional normalization
4. Use appropriate time-series windows matching the time horizon
5. Ensure the sign matches the predicted direction (multiply by -1 if needed)
6. Keep complexity reasonable (max 5-6 nested operators)
7. Handle potential NaN with pasteurize() if needed

{few_shot_examples}

Return ONLY the formula string, nothing else. Example format:
rank(ts_delta(close, 5)) * (-1)"""

# ---------------------------------------------------------------------------
# Few-shot example formatting
# ---------------------------------------------------------------------------

FEW_SHOT_HYPOTHESIS_TEMPLATE = """\
Example {index}:
Paper excerpt: "{excerpt}"
Hypothesis: {hypothesis}
Formula: {formula}
Result: Sharpe={sharpe:.2f}, Fitness={fitness:.2f}
---"""

FEW_SHOT_FORMULA_TEMPLATE = """\
Example {index}:
Hypothesis: {hypothesis}
Formula: {formula}
Sharpe: {sharpe:.2f}
---"""


def build_hypothesis_prompt(
    paper_content: str,
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build the hypothesis extraction prompt with optional few-shot examples."""
    from ..brain.constants import PRICE_VOLUME_FIELDS

    examples_text = ""
    if few_shot_examples:
        parts = []
        for i, ex in enumerate(few_shot_examples, 1):
            parts.append(FEW_SHOT_HYPOTHESIS_TEMPLATE.format(index=i, **ex))
        examples_text = "EXAMPLES OF SUCCESSFUL HYPOTHESES:\n" + "\n".join(parts)

    return HYPOTHESIS_EXTRACTION_TEMPLATE.format(
        fields=", ".join(PRICE_VOLUME_FIELDS),
        few_shot_examples=examples_text,
        paper_content=paper_content[:15000],  # cap to avoid token overflow
    )


def build_translation_prompt(
    mechanism: str,
    predicted_sign: str,
    time_horizon: str,
    relevant_fields: list[str],
    few_shot_examples: list[dict] | None = None,
) -> str:
    """Build the formula translation prompt with operator vocabulary."""
    examples_text = ""
    if few_shot_examples:
        parts = []
        for i, ex in enumerate(few_shot_examples, 1):
            parts.append(FEW_SHOT_FORMULA_TEMPLATE.format(index=i, **ex))
        examples_text = "EXAMPLES OF SUCCESSFUL FORMULAS:\n" + "\n".join(parts)

    return FORMULA_TRANSLATION_TEMPLATE.format(
        operator_vocabulary=get_operator_vocabulary_text(),
        mechanism=mechanism,
        predicted_sign=predicted_sign,
        time_horizon=time_horizon,
        relevant_fields=", ".join(relevant_fields),
        few_shot_examples=examples_text,
    )
