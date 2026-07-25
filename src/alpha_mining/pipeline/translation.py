"""
Formula translation stage: convert hypotheses to BRAIN Fast Expression formulas.

Uses the LLM with the full operator vocabulary to generate valid
BRAIN expressions from natural-language alpha hypotheses.
"""

from __future__ import annotations

import logging
import re
from typing import TYPE_CHECKING

from ..llm.prompts import SYSTEM_ALPHA_RESEARCHER, build_translation_prompt

if TYPE_CHECKING:
    from ..llm.provider import LLMProvider
    from .hypothesis import AlphaHypothesis

logger = logging.getLogger(__name__)


def translate_hypothesis(
    hypothesis: AlphaHypothesis,
    llm: LLMProvider,
    *,
    few_shot_examples: list[dict] | None = None,
) -> str | None:
    """
    Translate an alpha hypothesis into a BRAIN Fast Expression formula.

    Args:
        hypothesis: The alpha hypothesis to translate.
        llm: Configured LLM provider instance.
        few_shot_examples: Optional successful formula examples.

    Returns:
        Formula string if successful, None if translation fails.
    """
    prompt = build_translation_prompt(
        mechanism=hypothesis.mechanism,
        predicted_sign=hypothesis.predicted_sign,
        time_horizon=hypothesis.time_horizon,
        relevant_fields=hypothesis.relevant_fields,
        few_shot_examples=few_shot_examples,
    )

    try:
        response = llm.complete(
            prompt,
            system=SYSTEM_ALPHA_RESEARCHER,
            temperature=0.3,
            max_tokens=512,
        )
    except Exception as e:
        logger.error("Formula translation LLM call failed: %s", e)
        return None

    formula = _clean_formula(response.content)

    if not formula:
        logger.warning("Empty formula returned for hypothesis: %s", hypothesis.mechanism[:80])
        return None

    logger.info("Translated: %s -> %s", hypothesis.mechanism[:60], formula[:80])
    return formula


def translate_direct(
    description: str,
    llm: LLMProvider,
) -> str | None:
    """
    Translate a free-form alpha description directly to a formula.

    Useful for interactive use via Cursor chat -- describe what you want
    and get a BRAIN expression back.
    """
    from ..brain.constants import get_operator_vocabulary_text

    prompt = (
        f"{get_operator_vocabulary_text()}\n\n"
        f"Translate the following alpha idea into a BRAIN Fast Expression formula. "
        f"Return ONLY the formula string.\n\n"
        f"Idea: {description}"
    )

    try:
        response = llm.complete(
            prompt,
            system=SYSTEM_ALPHA_RESEARCHER,
            temperature=0.3,
            max_tokens=512,
        )
        return _clean_formula(response.content)
    except Exception as e:
        logger.error("Direct translation failed: %s", e)
        return None


def _clean_formula(raw: str) -> str:
    """Strip markdown fences, quotes, and whitespace from LLM formula output."""
    text = raw.strip()
    if "```" in text:
        match = re.search(r"```\w*\n?(.*?)```", text, re.DOTALL)
        if match:
            text = match.group(1).strip()

    text = text.strip("`\"'")

    lines = text.strip().split("\n")
    if lines:
        text = lines[0].strip()

    return text
