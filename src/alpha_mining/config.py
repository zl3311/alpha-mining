"""
Global configuration loaded from environment variables / .env file.

Uses Pydantic Settings to validate and type-check all config values at startup.
LLM-related fields are optional (not needed for Phase 1 BRAIN-only workflows).

Every credential defaults to the empty string so that importing any module in this
package succeeds without a `.env` file. Code that actually needs a credential is
responsible for checking it and failing with a useful message -- see
`BrainClient._authenticate`. This keeps the offline parts of the codebase (local
FASTEXPR evaluator, prescreener, prefilter, frontmatter tooling) and the test suite
usable on a fresh clone with no account.
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(_PROJECT_ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # BRAIN platform credentials
    brain_email: str = Field(default="", description="WorldQuant BRAIN login email")
    brain_password: str = Field(default="", description="WorldQuant BRAIN password")

    # LLM provider (optional for Phase 1)
    llm_model: str = Field(
        default="openai/gpt-4o",
        description="litellm model string, e.g. openai/gpt-4o, anthropic/claude-sonnet-4-20250514",
    )
    llm_api_key: str = Field(default="", description="API key for the LLM provider")

    # Storage
    db_path: Path = Field(
        default=_PROJECT_ROOT / "data" / "alpha_mining.db",
        description="Path to the SQLite database",
    )

    # Datalab (Marker) document parsing
    datalab_api_key: str = Field(default="", description="Datalab API key for Marker PDF parsing")

    # BRAIN concurrency and budget
    max_concurrent_sims: int = Field(
        default=3, ge=1, le=10, description="Max concurrent BRAIN simulations"
    )
    daily_sim_budget: int = Field(
        default=5000, ge=1, description="Max simulations per calendar day (EST)"
    )


def get_settings() -> Settings:
    """Return a cached Settings instance. Call once at startup."""
    return Settings()
