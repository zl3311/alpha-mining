"""
Tests for the configuration module.

Covers Settings loading, default values, and validation.

These tests deliberately do not depend on a populated `.env` file. Every case
disables dotenv loading via `_env_file=None` and sets the variables it needs
explicitly, so the suite passes on a fresh clone with no credentials present.
"""

import pytest

from alpha_mining.config import Settings

# Every environment variable Settings reads. Cleared before each test so that
# a developer's real .env or exported shell vars cannot change the outcome.
_SETTINGS_ENV_VARS = [
    "BRAIN_EMAIL",
    "BRAIN_PASSWORD",
    "LLM_MODEL",
    "LLM_API_KEY",
    "DB_PATH",
    "DATALAB_API_KEY",
    "MAX_CONCURRENT_SIMS",
    "DAILY_SIM_BUDGET",
]


@pytest.fixture
def clean_env(monkeypatch):
    for name in _SETTINGS_ENV_VARS:
        monkeypatch.delenv(name, raising=False)
    return monkeypatch


def _settings(**overrides) -> Settings:
    """Build Settings without reading the project .env file."""
    return Settings(_env_file=None, **overrides)


class TestSettings:
    def test_loads_brain_email_from_env(self, clean_env):
        clean_env.setenv("BRAIN_EMAIL", "user@example.com")
        assert _settings().brain_email == "user@example.com"

    def test_constructs_with_no_env_at_all(self, clean_env):
        # A fresh clone has no .env. Importing and constructing Settings must still
        # work so that the offline code paths and the test suite remain usable.
        assert _settings().brain_email == ""

    def test_default_db_path(self, clean_env):
        assert "alpha_mining.db" in str(_settings(brain_email="user@example.com").db_path)

    def test_default_concurrent_sims(self, clean_env):
        assert _settings(brain_email="user@example.com").max_concurrent_sims == 3

    def test_default_daily_budget(self, clean_env):
        assert _settings(brain_email="user@example.com").daily_sim_budget == 5000

    def test_default_llm_model(self, clean_env):
        assert _settings(brain_email="user@example.com").llm_model == "openai/gpt-4o"

    def test_optional_keys_default_to_empty(self, clean_env):
        settings = _settings(brain_email="user@example.com")
        assert settings.brain_password == ""
        assert settings.llm_api_key == ""
        assert settings.datalab_api_key == ""

    def test_datalab_key_loaded_from_env(self, clean_env):
        clean_env.setenv("BRAIN_EMAIL", "user@example.com")
        clean_env.setenv("DATALAB_API_KEY", "test-datalab-key")
        assert _settings().datalab_api_key == "test-datalab-key"


class TestSettingsValidation:
    def test_concurrent_sims_bounds(self, clean_env):
        with pytest.raises(Exception):
            _settings(brain_email="user@example.com", max_concurrent_sims=0)

        with pytest.raises(Exception):
            _settings(brain_email="user@example.com", max_concurrent_sims=11)

    def test_daily_budget_lower_bound(self, clean_env):
        with pytest.raises(Exception):
            _settings(brain_email="user@example.com", daily_sim_budget=0)
