"""
Async BRAIN API client for authentication, simulation, and alpha retrieval.

Uses httpx with cookie persistence for session management. Implements:
- HTTP Basic auth with biometric challenge handling
- Concurrent simulation submission with configurable semaphore
- Polling with exponential backoff
- Rate limit handling (HTTP 429, SIMULATION_LIMIT_EXCEEDED)
- Daily simulation budget tracking

Reference: RussellDash332/WQ-Brain for endpoint semantics,
           autobrain-sim for Retry-After patterns.
"""

from __future__ import annotations

import asyncio
import logging
import time

import httpx

from ..config import Settings
from .constants import BASE_URL, ENDPOINTS
from .models import (
    AlphaMetrics,
    CheckResult,
    SimulationConfig,
    SimulationResult,
    SimulationStatus,
)

logger = logging.getLogger(__name__)

_POLL_INTERVAL = 10  # seconds between simulation status checks
_MAX_POLL_ATTEMPTS = 60  # ~10 minutes max wait per simulation
_BACKOFF_BASE = 2.0
_BACKOFF_MAX = 120.0


class BrainAuthError(Exception):
    """Raised when BRAIN authentication fails or session expires."""


class BrainSimulationError(Exception):
    """Raised when a simulation submission or polling fails."""


class BrainRateLimitError(Exception):
    """Raised when hitting rate limits (429 or SIMULATION_LIMIT_EXCEEDED)."""


class BrainClient:
    """
    Async client for the WorldQuant BRAIN API.

    Manages a persistent httpx session with cookie-based auth.
    Concurrency is bounded by a semaphore to respect platform slot limits.

    Usage:
        async with BrainClient(settings) as client:
            result = await client.simulate(SimulationConfig(expression="rank(close)"))
            print(result.metrics.sharpe)
    """

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._semaphore = asyncio.Semaphore(settings.max_concurrent_sims)
        self._client: httpx.AsyncClient | None = None
        self._authenticated = False
        self._daily_count = 0
        self._daily_date: str = ""

    async def __aenter__(self) -> BrainClient:
        self._client = httpx.AsyncClient(
            base_url=BASE_URL,
            timeout=httpx.Timeout(30.0, connect=10.0),
            follow_redirects=True,
        )
        await self._authenticate()
        return self

    async def __aexit__(self, *exc) -> None:
        if self._client:
            await self._client.aclose()
            self._client = None
        self._authenticated = False

    # ------------------------------------------------------------------
    # Authentication
    # ------------------------------------------------------------------

    async def _authenticate(self) -> None:
        """
        Authenticate via HTTP Basic to POST /authentication.
        Handles biometric/Persona challenge if required.
        """
        email = self._settings.brain_email
        password = self._settings.brain_password
        if not email or not password:
            missing = " and ".join(
                name for name, value in (("BRAIN_EMAIL", email), ("BRAIN_PASSWORD", password))
                if not value
            )
            raise BrainAuthError(
                f"{missing} not set. Copy .env.example to .env and fill in your "
                "WorldQuant BRAIN credentials."
            )

        r = await self._client.post(
            ENDPOINTS["auth"],
            auth=(email, password),
        )

        if r.status_code == 401:
            raise BrainAuthError(f"Authentication failed (401). Check credentials for {email}.")

        data = r.json()

        if "user" not in data:
            if "inquiry" in data:
                logger.warning(
                    "Biometric challenge detected. Complete verification in browser, "
                    "then the Persona follow-up will be attempted."
                )
                persona_url = f"{r.url}/persona"
                r2 = await self._client.post(persona_url, json=data)
                if r2.status_code != 200:
                    raise BrainAuthError(
                        f"Persona verification failed ({r2.status_code}). "
                        "Complete biometric check at platform.worldquantbrain.com first."
                    )
            else:
                raise BrainAuthError(f"Unexpected auth response: {data}")

        self._authenticated = True
        logger.info("Authenticated as %s", email)

    async def _ensure_auth(self) -> None:
        if not self._authenticated:
            await self._authenticate()

    # ------------------------------------------------------------------
    # Simulation
    # ------------------------------------------------------------------

    async def simulate(self, config: SimulationConfig) -> SimulationResult:
        """
        Submit an alpha expression for simulation and wait for results.

        Respects the concurrency semaphore and daily budget.
        Returns a SimulationResult with metrics on success, or error details on failure.
        """
        await self._ensure_auth()
        self._check_daily_budget()

        async with self._semaphore:
            return await self._run_simulation(config)

    async def simulate_batch(
        self, configs: list[SimulationConfig]
    ) -> list[SimulationResult]:
        """Submit multiple simulations concurrently (bounded by semaphore)."""
        tasks = [self.simulate(cfg) for cfg in configs]
        return await asyncio.gather(*tasks, return_exceptions=False)

    async def _run_simulation(self, config: SimulationConfig) -> SimulationResult:
        payload = config.to_api_payload()
        logger.info("Submitting: %s", config.expression[:80])

        try:
            r = await self._post_with_retry(ENDPOINTS["simulations"], json=payload)
        except BrainRateLimitError:
            return SimulationResult(
                config=config,
                status=SimulationStatus.ERROR,
                error_message="Rate limited during submission",
            )

        location = r.headers.get("Location")
        if not location:
            body = r.json() if r.headers.get("content-type", "").startswith("application/json") else {}
            msg = body.get("message", body.get("detail", f"No Location header (HTTP {r.status_code})"))
            if "SIMULATION_LIMIT" in str(msg).upper():
                return SimulationResult(
                    config=config,
                    status=SimulationStatus.ERROR,
                    error_message=f"Simulation limit: {msg}",
                )
            return SimulationResult(
                config=config,
                status=SimulationStatus.FAILED,
                error_message=str(msg),
            )

        self._increment_daily_count()

        # Poll for completion
        poll_url = location if location.startswith("http") else f"{BASE_URL}{location}"
        return await self._poll_simulation(config, poll_url)

    async def _poll_simulation(
        self, config: SimulationConfig, poll_url: str
    ) -> SimulationResult:
        for attempt in range(_MAX_POLL_ATTEMPTS):
            await asyncio.sleep(_POLL_INTERVAL)

            try:
                r = await self._client.get(poll_url)
            except httpx.HTTPError as e:
                logger.warning("Poll error (attempt %d): %s", attempt, e)
                continue

            if r.status_code == 429:
                wait = _get_retry_after(r)
                logger.warning("Rate limited during poll, waiting %ds", wait)
                await asyncio.sleep(wait)
                continue

            data = r.json()

            if "alpha" in data:
                alpha_id = data["alpha"]
                if isinstance(alpha_id, str) and "/" in alpha_id:
                    alpha_id = alpha_id.split("/")[-1]
                return await self._fetch_alpha_result(config, str(alpha_id))

            progress = data.get("progress", 0)
            logger.debug("Simulation progress: %d%%", int(100 * progress))

            if "message" in data or "error" in data:
                msg = data.get("message", data.get("error", "Unknown error"))
                return SimulationResult(
                    config=config,
                    status=SimulationStatus.FAILED,
                    error_message=str(msg),
                    raw_response=data,
                )

        return SimulationResult(
            config=config,
            status=SimulationStatus.ERROR,
            error_message=f"Polling timed out after {_MAX_POLL_ATTEMPTS * _POLL_INTERVAL}s",
        )

    async def _fetch_alpha_result(
        self, config: SimulationConfig, alpha_id: str
    ) -> SimulationResult:
        url = f"{ENDPOINTS['alphas']}/{alpha_id}"
        r = await self._client.get(url)

        if r.status_code != 200:
            return SimulationResult(
                config=config,
                alpha_id=alpha_id,
                status=SimulationStatus.FAILED,
                error_message=f"Failed to fetch alpha {alpha_id}: HTTP {r.status_code}",
            )

        data = r.json()
        is_data = data.get("is", {})

        checks = []
        for c in is_data.get("checks", []):
            checks.append(
                CheckResult(
                    name=c.get("name", ""),
                    result=c.get("result", ""),
                    value=c.get("value"),
                    limit=c.get("limit"),
                )
            )

        metrics = AlphaMetrics(
            sharpe=float(is_data.get("sharpe", 0)),
            fitness=float(is_data.get("fitness", 0)),
            turnover=float(is_data.get("turnover", 0)),
            returns=float(is_data.get("returns", 0)),
            drawdown=float(is_data.get("drawdown", 0)),
            margin=float(is_data.get("margin", 0)),
            checks=checks,
        )

        platform_url = f"https://platform.worldquantbrain.com/alpha/{alpha_id}"

        logger.info(
            "Simulation done: Sharpe=%.3f Fitness=%.3f Turnover=%.1f%% [%s]",
            metrics.sharpe,
            metrics.fitness,
            metrics.turnover * 100,
            config.expression[:60],
        )

        return SimulationResult(
            config=config,
            alpha_id=alpha_id,
            status=SimulationStatus.DONE,
            metrics=metrics,
            platform_url=platform_url,
            raw_response=data,
        )

    # ------------------------------------------------------------------
    # Alpha metadata (name, tags, description)
    # ------------------------------------------------------------------

    async def set_alpha_properties(
        self,
        alpha_id: str,
        *,
        name: str = "",
        tags: list[str] | None = None,
        color: str | None = None,
        description: str = "",
    ) -> dict:
        """
        Update alpha metadata on BRAIN via PATCH /alphas/{id}.

        Call after simulation completes to set name, tags, and description
        so the alpha is properly labeled on the platform.
        """
        await self._ensure_auth()
        payload: dict = {}
        if name:
            payload["name"] = name
        if tags is not None:
            payload["tags"] = tags
        if color:
            payload["color"] = color
        if description:
            payload["regular"] = {"description": description}

        if not payload:
            return {}

        url = f"{ENDPOINTS['alphas']}/{alpha_id}"
        r = await self._client.patch(url, json=payload)

        if r.status_code == 200:
            logger.info("Updated alpha %s properties: %s", alpha_id, list(payload.keys()))
            return r.json()
        else:
            logger.warning("Failed to update alpha %s: HTTP %s", alpha_id, r.status_code)
            return {"error": r.status_code, "detail": r.text[:200]}

    # ------------------------------------------------------------------
    # Alpha submission (for scoring)
    # ------------------------------------------------------------------

    async def submit_alpha(self, alpha_id: str) -> dict:
        """Submit a simulated alpha for official scoring/self-correlation checks."""
        await self._ensure_auth()
        url = f"{ENDPOINTS['alphas']}/{alpha_id}/submit"
        r = await self._client.post(url)

        for _ in range(30):
            await asyncio.sleep(5)
            r = await self._client.get(url)
            if r.status_code == 404:
                return {"status": "not_found", "message": "Alpha may already be submitted"}
            if r.content:
                data = r.json()
                is_data = data.get("is", {})
                for check in is_data.get("checks", []):
                    if check["name"] == "SELF_CORRELATION":
                        return {
                            "status": "completed",
                            "self_correlation_pass": check["result"] == "PASS",
                            "self_correlation_value": check.get("value"),
                        }
                return {"status": "completed", "data": data}

        return {"status": "timeout"}

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    async def _post_with_retry(
        self, url: str, max_retries: int = 3, **kwargs
    ) -> httpx.Response:
        """POST with exponential backoff on 429 and transient errors."""
        for attempt in range(max_retries):
            try:
                r = await self._client.post(url, **kwargs)
            except httpx.HTTPError as e:
                if attempt == max_retries - 1:
                    raise
                wait = min(_BACKOFF_BASE ** (attempt + 1), _BACKOFF_MAX)
                logger.warning("HTTP error (attempt %d): %s. Retrying in %ds", attempt, e, wait)
                await asyncio.sleep(wait)
                continue

            if r.status_code == 429:
                wait = _get_retry_after(r)
                logger.warning("Rate limited (429), waiting %ds", wait)
                if attempt == max_retries - 1:
                    raise BrainRateLimitError(f"Rate limited after {max_retries} attempts")
                await asyncio.sleep(wait)
                continue

            if r.status_code == 401:
                logger.info("Session expired, re-authenticating")
                self._authenticated = False
                await self._authenticate()
                continue

            return r

        raise BrainSimulationError(f"POST {url} failed after {max_retries} retries")

    def _check_daily_budget(self) -> None:
        today = _est_date_str()
        if self._daily_date != today:
            self._daily_date = today
            self._daily_count = 0

        if self._daily_count >= self._settings.daily_sim_budget:
            raise BrainRateLimitError(
                f"Daily simulation budget exhausted ({self._daily_count}/{self._settings.daily_sim_budget})"
            )

    def _increment_daily_count(self) -> None:
        today = _est_date_str()
        if self._daily_date != today:
            self._daily_date = today
            self._daily_count = 0
        self._daily_count += 1


def _get_retry_after(response: httpx.Response) -> int:
    """Extract Retry-After header or return a default backoff."""
    try:
        return int(response.headers.get("Retry-After", 60))
    except (ValueError, TypeError):
        return 60


def _est_date_str() -> str:
    """Return today's date in EST as a string for budget tracking."""
    from datetime import timedelta, timezone

    est = timezone(timedelta(hours=-5))
    return time.strftime("%Y-%m-%d", time.gmtime(time.time() + est.utcoffset(None).total_seconds()))
