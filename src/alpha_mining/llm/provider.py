"""
Provider-agnostic LLM wrapper built on litellm.

Provides structured output parsing (Pydantic models), retry logic,
token usage tracking, and cost estimation. Supports any provider
litellm supports: OpenAI, Anthropic, Fireworks, Ollama, etc.
"""

from __future__ import annotations

import json
import logging
from typing import TypeVar

import litellm
from pydantic import BaseModel

from ..config import Settings

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseModel)

litellm.drop_params = True


class LLMUsage(BaseModel):
    """Token usage and cost for a single LLM call."""

    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    cost_usd: float = 0.0


class LLMResponse(BaseModel):
    """Wrapper around a single LLM completion response."""

    content: str = ""
    usage: LLMUsage = LLMUsage()
    model: str = ""


class LLMProvider:
    """
    Thin wrapper around litellm for alpha mining workflows.

    Handles model routing, API key injection, structured output parsing,
    and usage tracking. Stateless across calls -- safe for concurrent use.

    Usage:
        provider = LLMProvider(settings)
        response = provider.complete("Generate an alpha hypothesis for momentum.")
        hypothesis = provider.complete_structured(prompt, AlphaHypothesis)
    """

    def __init__(self, settings: Settings) -> None:
        self._model = settings.llm_model
        self._api_key = settings.llm_api_key or None
        self._total_usage = LLMUsage()

        if self._api_key:
            litellm.api_key = self._api_key

    @property
    def total_usage(self) -> LLMUsage:
        return self._total_usage

    def complete(
        self,
        prompt: str,
        *,
        system: str = "",
        temperature: float = 0.7,
        max_tokens: int = 4096,
    ) -> LLMResponse:
        """Send a completion request and return the response text."""
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        try:
            response = litellm.completion(
                model=self._model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                api_key=self._api_key,
            )
        except Exception as e:
            logger.error("LLM completion failed: %s", e)
            raise

        content = response.choices[0].message.content or ""
        usage_data = response.usage
        cost = litellm.completion_cost(completion_response=response) if usage_data else 0.0

        usage = LLMUsage(
            prompt_tokens=getattr(usage_data, "prompt_tokens", 0),
            completion_tokens=getattr(usage_data, "completion_tokens", 0),
            total_tokens=getattr(usage_data, "total_tokens", 0),
            cost_usd=cost,
        )
        self._accumulate_usage(usage)

        logger.debug(
            "LLM call: %d tokens, $%.4f [%s]",
            usage.total_tokens,
            usage.cost_usd,
            self._model,
        )

        return LLMResponse(content=content, usage=usage, model=self._model)

    def complete_structured(
        self,
        prompt: str,
        response_model: type[T],
        *,
        system: str = "",
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ) -> T:
        """
        Send a completion request and parse the response into a Pydantic model.

        Instructs the LLM to return JSON matching the model schema, then validates.
        Falls back to extracting JSON from markdown code blocks if needed.
        """
        schema_json = json.dumps(response_model.model_json_schema(), indent=2)
        structured_prompt = (
            f"{prompt}\n\n"
            f"Respond ONLY with valid JSON matching this schema:\n"
            f"```json\n{schema_json}\n```"
        )

        response = self.complete(
            structured_prompt,
            system=system,
            temperature=temperature,
            max_tokens=max_tokens,
        )

        return _parse_model(response.content, response_model)

    def _accumulate_usage(self, usage: LLMUsage) -> None:
        self._total_usage = LLMUsage(
            prompt_tokens=self._total_usage.prompt_tokens + usage.prompt_tokens,
            completion_tokens=self._total_usage.completion_tokens + usage.completion_tokens,
            total_tokens=self._total_usage.total_tokens + usage.total_tokens,
            cost_usd=self._total_usage.cost_usd + usage.cost_usd,
        )


def _parse_model(text: str, model_class: type[T]) -> T:
    """Parse LLM output into a Pydantic model, handling markdown fences."""
    cleaned = text.strip()

    if "```" in cleaned:
        start = cleaned.find("```")
        first_newline = cleaned.find("\n", start)
        end = cleaned.find("```", first_newline)
        if first_newline != -1 and end != -1:
            cleaned = cleaned[first_newline + 1 : end].strip()

    return model_class.model_validate_json(cleaned)
