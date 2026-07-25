"""
Hypothesis generation stage: extract alpha hypotheses from paper content.

Takes structured markdown from the extraction stage and uses the LLM
to identify tradeable alpha hypotheses with economic mechanisms.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from pydantic import BaseModel, Field

from ..llm.prompts import SYSTEM_ALPHA_RESEARCHER, build_hypothesis_prompt

if TYPE_CHECKING:
    from ..llm.provider import LLMProvider

logger = logging.getLogger(__name__)


class AlphaHypothesis(BaseModel):
    """A single alpha hypothesis extracted from a research paper."""

    mechanism: str = Field(description="Economic mechanism driving the alpha")
    predicted_sign: str = Field(description="Expected return direction: positive or negative")
    time_horizon: str = Field(description="Expected holding period")
    relevant_fields: list[str] = Field(default_factory=list, description="Data fields needed")
    confidence: str = Field(default="medium", description="Confidence level: high/medium/low")


class HypothesisList(BaseModel):
    """Container for multiple hypotheses (for structured LLM output)."""

    hypotheses: list[AlphaHypothesis] = Field(default_factory=list)


def generate_hypotheses(
    paper_content: str,
    llm: LLMProvider,
    *,
    few_shot_examples: list[dict] | None = None,
) -> list[AlphaHypothesis]:
    """
    Extract alpha hypotheses from paper content using the LLM.

    Args:
        paper_content: Structured markdown from the extraction stage.
        llm: Configured LLM provider instance.
        few_shot_examples: Optional top-performing examples for the prompt.

    Returns:
        List of extracted hypotheses.
    """
    prompt = build_hypothesis_prompt(paper_content, few_shot_examples)

    try:
        result = llm.complete_structured(
            prompt,
            HypothesisList,
            system=SYSTEM_ALPHA_RESEARCHER,
            temperature=0.5,
        )
        logger.info("Generated %d hypotheses from paper content", len(result.hypotheses))
        return result.hypotheses
    except Exception as e:
        logger.error("Hypothesis generation failed: %s", e)
        return []
