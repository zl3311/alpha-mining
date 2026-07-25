"""
Pydantic models for the storage layer.

Represents the full workflow lineage:
  sessions -> papers (many-to-many) -> hypotheses -> alphas -> simulations -> results

Each entity has an integer PK (internal joins) and a globally unique entity_id
(external access across Cursor, web app, chatbot, MCP).
"""

from __future__ import annotations

from datetime import UTC, datetime

from pydantic import BaseModel, Field

from ..ids import generate_entity_id


class SessionRecord(BaseModel):
    """A unit of work: a Cursor chat, CLI invocation, periodic run, etc."""

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("session"))
    source: str = "manual"  # cursor, periodic, manual, batch, paper
    name: str = ""
    notes: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class PaperRecord(BaseModel):
    """A research paper ingested for hypothesis extraction. Independent entity."""

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("paper"))
    title: str = ""
    source_url: str = ""
    pdf_path: str = ""
    markdown_path: str = ""
    extracted_markdown: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class SessionPaperRecord(BaseModel):
    """Many-to-many link between sessions and papers."""

    session_id: int
    paper_id: int


class PaperImageRecord(BaseModel):
    """An image extracted from a paper via Marker. Stored as base64 for agent-friendly access."""

    id: int | None = None
    paper_id: int | None = None
    filename: str = ""
    content_type: str = "image/png"
    image_data_b64: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class HypothesisRecord(BaseModel):
    """
    An alpha hypothesis: an idea about a tradeable signal.

    Can originate from a paper, a conversation, or pure reasoning.
    Has optional FKs to both session (which produced it) and paper (which inspired it).
    """

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("hypothesis"))
    session_id: int | None = None
    paper_id: int | None = None
    mechanism: str = ""
    predicted_sign: str = ""  # "positive" or "negative"
    time_horizon: str = ""  # "intraday", "1-5 days", "5-20 days", "20+ days"
    relevant_fields: list[str] = Field(default_factory=list)
    confidence: str = ""  # "high", "medium", "low"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class AlphaRecord(BaseModel):
    """
    An alpha expression: a formula in BRAIN Fast Expression language.

    Pure identity -- no simulation config. One alpha can have many simulations
    with different configs (region, decay, etc.).
    """

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("alpha"))
    hypothesis_id: int | None = None
    name: str = ""
    expression: str = ""
    expression_hash: str = ""
    language: str = "FASTEXPR"  # FASTEXPR, PYTHON, EXPRESSION
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class SimulationRecord(BaseModel):
    """
    A single BRAIN simulation submission.

    Captures the specific config, status, BRAIN identifiers, and
    platform metadata (grade, classifications, stage).
    """

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("simulation"))
    alpha_id: int | None = None
    sim_config_json: str = "{}"
    status: str = "pending"  # pending, running, done, failed, error
    brain_alpha_id: str = ""
    platform_url: str = ""
    brain_grade: str = ""  # INFERIOR, MEDIOCRE, GOOD, EXCELLENT (assigned by BRAIN)
    brain_stage: str = ""  # IS, OS, PROD
    brain_status: str = ""  # UNSUBMITTED, SUBMITTED, etc.
    brain_classifications_json: str = "[]"  # e.g. [{"id": "DATA_USAGE:SINGLE_DATA_SET", "name": "..."}]
    brain_tags_json: str = "[]"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


class ResultRecord(BaseModel):
    """Backtest metrics from a BRAIN simulation. One per simulation."""

    id: int | None = None
    entity_id: str = Field(default_factory=lambda: generate_entity_id("result"))
    simulation_id: int | None = None
    sharpe: float = 0.0
    fitness: float = 0.0
    turnover: float = 0.0
    returns: float = 0.0
    drawdown: float = 0.0
    self_correlation: float | None = None
    checks_json: str = "[]"
    raw_response_json: str = "{}"
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @property
    def passes_gates(self) -> bool:
        return self.sharpe >= 1.25 and self.fitness >= 1.0 and 0.01 <= self.turnover <= 0.70


class SimBudgetRecord(BaseModel):
    """Daily simulation budget tracking (EST date)."""

    date_est: str
    count: int = 0
    last_updated: datetime = Field(default_factory=lambda: datetime.now(UTC))
