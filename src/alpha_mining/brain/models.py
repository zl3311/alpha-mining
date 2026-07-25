"""
Pydantic models for BRAIN API objects.

Covers the simulation lifecycle: config -> submission -> polling -> results.
All models are immutable (frozen) for safety in async contexts.
"""

from __future__ import annotations

from datetime import UTC, datetime
from enum import Enum

from pydantic import BaseModel, Field

from .constants import (
    DEFAULT_SIM_SETTINGS,
    AlphaLanguage,
    Neutralization,
    Region,
    Universe,
)


class SimulationStatus(str, Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    DONE = "DONE"
    FAILED = "FAILED"
    ERROR = "ERROR"


class SimulationConfig(BaseModel, frozen=True):
    """Configuration for a single BRAIN simulation submission."""

    expression: str = Field(description="Alpha code (Python by default, or FASTEXPR)")
    language: AlphaLanguage = Field(default=AlphaLanguage(DEFAULT_SIM_SETTINGS["language"]))
    region: Region = Field(default=Region(DEFAULT_SIM_SETTINGS["region"]))
    universe: Universe = Field(default=Universe(DEFAULT_SIM_SETTINGS["universe"]))
    delay: int = Field(default=DEFAULT_SIM_SETTINGS["delay"], ge=0)
    decay: int = Field(default=DEFAULT_SIM_SETTINGS["decay"], ge=0)
    truncation: float = Field(default=DEFAULT_SIM_SETTINGS["truncation"], ge=0.0, le=1.0)
    neutralization: Neutralization = Field(
        default=Neutralization(DEFAULT_SIM_SETTINGS["neutralization"])
    )
    nan_handling: str = Field(default=DEFAULT_SIM_SETTINGS["nanHandling"])
    pasteurization: str = Field(default=DEFAULT_SIM_SETTINGS["pasteurization"])

    def to_api_payload(self) -> dict:
        """Convert to the JSON body expected by POST /simulations."""
        return {
            "regular": self.expression,
            "type": "REGULAR",
            "settings": {
                "instrumentType": "EQUITY",
                "region": self.region.value,
                "universe": self.universe.value,
                "delay": self.delay,
                "decay": self.decay,
                "truncation": self.truncation,
                "neutralization": self.neutralization.value,
                "nanHandling": self.nan_handling,
                "unitHandling": "VERIFY",
                "pasteurization": self.pasteurization,
                "language": self.language.value,
                "visualization": False,
            },
        }


class CheckResult(BaseModel, frozen=True):
    """A single check from the BRAIN validation pipeline."""

    name: str
    result: str  # "PASS" or "FAIL"
    value: float | None = None
    limit: float | None = None


class AlphaMetrics(BaseModel, frozen=True):
    """In-sample (IS) metrics returned by BRAIN after simulation."""

    sharpe: float = 0.0
    fitness: float = 0.0
    turnover: float = 0.0
    returns: float = 0.0
    drawdown: float = 0.0
    margin: float = 0.0
    checks: list[CheckResult] = Field(default_factory=list)

    @property
    def all_checks_pass(self) -> bool:
        return all(c.result == "PASS" for c in self.checks)

    @property
    def self_correlation(self) -> float | None:
        """Extract self-correlation value from checks if present."""
        for c in self.checks:
            if c.name == "SELF_CORRELATION" and c.value is not None:
                return c.value
        return None

    @property
    def passes_submission_gates(self) -> bool:
        """Heuristic check against known submission thresholds (USA TOP3000)."""
        return (
            self.sharpe >= 1.25
            and self.fitness >= 1.0
            and 0.01 <= self.turnover <= 0.70
            and self.all_checks_pass
        )

    def fitness_score(self) -> float:
        """Compute the BRAIN fitness formula."""
        import math

        return math.sqrt(abs(self.returns) / max(self.turnover, 0.125)) * self.sharpe


class SimulationResult(BaseModel, frozen=True):
    """Full result of a BRAIN simulation run."""

    config: SimulationConfig
    alpha_id: str = ""
    status: SimulationStatus = SimulationStatus.PENDING
    metrics: AlphaMetrics | None = None
    error_message: str = ""
    platform_url: str = ""
    raw_response: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @property
    def succeeded(self) -> bool:
        return self.status == SimulationStatus.DONE and self.metrics is not None

    @property
    def submittable(self) -> bool:
        return self.succeeded and self.metrics.passes_submission_gates
