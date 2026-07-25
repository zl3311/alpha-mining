"""
Local market data: download, cache, and serve OHLCV + derived fields
from yfinance for alpha pre-screening.

Data is cached as parquet in data/local_cache/ with a 7-day TTL.
Derived fields (returns, adv20, vwap proxy) are computed on load.

The module provides a MarketData object holding aligned DataFrames
(stocks as columns, dates as index) that the evaluator consumes.
"""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

_CACHE_DIR = Path(__file__).resolve().parents[3] / "data" / "local_cache"
_CACHE_TTL_DAYS = 7

_US_TICKERS_FALLBACK = [
    "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "GOOG", "META", "BRK-B", "TSLA", "UNH",
    "XOM", "JNJ", "JPM", "V", "PG", "MA", "HD", "AVGO", "CVX", "MRK",
    "ABBV", "LLY", "PEP", "KO", "COST", "TMO", "MCD", "WMT", "CSCO", "CRM",
    "ACN", "ABT", "LIN", "DHR", "AMD", "ADBE", "TXN", "NEE", "PM", "WFC",
    "BMY", "RTX", "UPS", "HON", "QCOM", "ORCL", "T", "MS", "LOW", "SCHW",
    "AMGN", "GS", "ELV", "BA", "SBUX", "CAT", "IBM", "BLK", "INTU", "DE",
    "ISRG", "GILD", "MDLZ", "ADP", "PLD", "SYK", "GE", "MMC", "ADI", "VRTX",
    "TJX", "BKNG", "LRCX", "CI", "CB", "ZTS", "PANW", "NOW", "REGN", "MO",
    "SO", "DUK", "CME", "BSX", "PGR", "MMM", "KLAC", "FIS", "EOG", "SLB",
    "HUM", "ATVI", "CL", "ICE", "MCK", "APD", "SHW", "NOC", "MPC", "FDX",
    "PYPL", "NXPI", "MAR", "SNPS", "ETN", "PH", "CDNS", "PXD", "MRNA", "AIG",
    "GM", "F", "NFLX", "DIS", "INTC", "CMCSA", "VZ", "COP", "DOW", "USB",
    "PSX", "VLO", "EMR", "AEP", "D", "EXC", "SRE", "XEL", "WEC", "ES",
    "MCHP", "ANET", "FTNT", "DXCM", "CARR", "BKR", "OXY", "HAL", "DVN", "FANG",
    "KMI", "WMB", "OKE", "LNG", "TRGP", "APA", "MRO", "CTRA", "EQT", "AR",
    "GD", "LMT", "HII", "TDG", "HWM", "SPR", "LHX", "LDOS", "BAH", "SAIC",
    "WM", "RSG", "WCN", "CLH", "GFL", "SRCL", "ECOL", "US", "MEG", "CWST",
    "PAYX", "FAST", "POOL", "WSO", "SWK", "ROK", "AME", "IEX", "NDSN", "RBC",
    "NKE", "LULU", "TPR", "RL", "CPRI", "VFC", "PVH", "HBI", "UAA", "GIII",
    "MSCI", "SPGI", "MCO", "VRSK", "FDS", "TRI", "INFO", "DNB", "WK", "ROPER",
]


@dataclass
class MarketData:
    """Aligned stock-panel DataFrames for local alpha evaluation."""

    open: pd.DataFrame = field(repr=False)
    high: pd.DataFrame = field(repr=False)
    low: pd.DataFrame = field(repr=False)
    close: pd.DataFrame = field(repr=False)
    volume: pd.DataFrame = field(repr=False)
    returns: pd.DataFrame = field(repr=False)
    vwap: pd.DataFrame = field(repr=False)
    adv20: pd.DataFrame = field(repr=False)
    adv60: pd.DataFrame = field(repr=False)
    cap: pd.DataFrame = field(repr=False)
    sector: dict[str, str] = field(default_factory=dict, repr=False)
    industry: dict[str, str] = field(default_factory=dict, repr=False)
    tickers: list[str] = field(default_factory=list)
    date_range: str = ""

    def __repr__(self) -> str:
        n_stocks = len(self.tickers)
        n_days = len(self.close) if not self.close.empty else 0
        return f"MarketData({n_stocks} stocks, {n_days} days, {self.date_range})"


def _get_cache_path(region: str, universe: int) -> Path:
    return _CACHE_DIR / f"{region}_top{universe}.parquet"


def _cache_is_fresh(path: Path) -> bool:
    if not path.exists():
        return False
    age_days = (time.time() - path.stat().st_mtime) / 86400
    return age_days < _CACHE_TTL_DAYS


def _discover_tickers_us(universe: int) -> list[str]:
    """Get US tickers via yfinance screener, falling back to hardcoded list."""
    try:
        import yfinance as yf

        sc = yf.Screener()
        sc.set_default_body({"size": min(universe, 250), "offset": 0, "query": "eq(region, \"us\")"})
        result = sc.response
        symbols = [q["symbol"] for q in result.get("quotes", [])]
        if len(symbols) >= 50:
            logger.info("Discovered %d US tickers via screener", len(symbols))
            return symbols[:universe]
    except Exception as e:
        logger.debug("Screener failed, using fallback tickers: %s", e)

    return _US_TICKERS_FALLBACK[:universe]


def load_market_data(
    region: str = "us",
    universe: int = 200,
    years: int = 5,
    refresh: bool = False,
) -> MarketData:
    """
    Load OHLCV data for local screening. Downloads from yfinance on first call,
    then caches as parquet. Returns a MarketData object with aligned DataFrames.

    Args:
        region: Market region (currently 'us' supported).
        universe: Number of stocks (top N, approximated from available tickers).
        years: Years of history to download.
        refresh: Force re-download even if cache exists.
    """
    import yfinance as yf

    _CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = _get_cache_path(region, universe)

    if not refresh and _cache_is_fresh(cache_path):
        logger.info("Loading cached data from %s", cache_path)
        return _load_from_cache(cache_path)

    tickers = _discover_tickers_us(universe)
    logger.info("Downloading %d tickers, %d years of history...", len(tickers), years)

    end = pd.Timestamp.now()
    start = end - pd.DateOffset(years=years)

    raw = yf.download(
        tickers,
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d"),
        progress=False,
        group_by="ticker",
        auto_adjust=True,
        threads=True,
    )

    if raw.empty:
        raise RuntimeError("yfinance returned empty data -- check network or tickers")

    ohlcv = _reshape_yf_data(raw, tickers)

    sector_map = {}
    industry_map = {}
    for t in tickers[:50]:
        try:
            info = yf.Ticker(t).fast_info
            sector_map[t] = getattr(info, "sector", "Unknown") if hasattr(info, "sector") else "Unknown"
            industry_map[t] = getattr(info, "industry", "Unknown") if hasattr(info, "industry") else "Unknown"
        except Exception:
            sector_map[t] = "Unknown"
            industry_map[t] = "Unknown"

    meta = pd.DataFrame({
        "sector_json": [pd.Series(sector_map).to_json()],
        "industry_json": [pd.Series(industry_map).to_json()],
    })
    meta_path = cache_path.with_suffix(".meta.parquet")
    meta.to_parquet(meta_path)

    ohlcv.to_parquet(cache_path)
    logger.info("Cached %d stocks x %d days to %s", ohlcv.shape[1] // 5, len(ohlcv), cache_path)

    return _build_market_data(ohlcv, sector_map, industry_map)


def _reshape_yf_data(raw: pd.DataFrame, tickers: list[str]) -> pd.DataFrame:
    """Reshape yfinance multi-ticker download into a flat OHLCV panel."""
    frames = {}
    for col_type in ["Open", "High", "Low", "Close", "Volume"]:
        try:
            if isinstance(raw.columns, pd.MultiIndex):
                df = raw.xs(col_type, level=1, axis=1) if col_type in raw.columns.get_level_values(1) else raw[col_type]
            else:
                df = raw[col_type]
            frames[col_type.lower()] = df
        except (KeyError, TypeError):
            pass

    if not frames:
        raise RuntimeError("Could not extract OHLCV from yfinance data")

    combined = pd.concat(frames, axis=1)
    combined = combined.dropna(how="all")
    return combined


def _load_from_cache(cache_path: Path) -> MarketData:
    """Load MarketData from cached parquet file."""
    import json

    df = pd.read_parquet(cache_path)

    sector_map = {}
    industry_map = {}
    meta_path = cache_path.with_suffix(".meta.parquet")
    if meta_path.exists():
        meta = pd.read_parquet(meta_path)
        try:
            sector_map = json.loads(meta["sector_json"].iloc[0])
        except Exception:
            pass
        try:
            industry_map = json.loads(meta["industry_json"].iloc[0])
        except Exception:
            pass

    # Handle legacy cache files that embed metadata in the OHLCV frame
    for col in ("sector_json", "industry_json"):
        if col in df.columns:
            if not sector_map and col == "sector_json":
                try:
                    sector_map = json.loads(df[col].iloc[0])
                except Exception:
                    pass
            if not industry_map and col == "industry_json":
                try:
                    industry_map = json.loads(df[col].iloc[0])
                except Exception:
                    pass
            df = df.drop(columns=[col])

    return _build_market_data(df, sector_map, industry_map)


def _build_market_data(
    combined: pd.DataFrame,
    sector_map: dict[str, str],
    industry_map: dict[str, str],
) -> MarketData:
    """Build MarketData from the combined OHLCV DataFrame."""
    def _extract(col_type: str) -> pd.DataFrame:
        try:
            if isinstance(combined.columns, pd.MultiIndex):
                return combined[col_type]
            cols = [c for c in combined.columns if c[0] == col_type] if isinstance(combined.columns[0], tuple) else combined.filter(like=col_type)
            return cols
        except (KeyError, TypeError):
            return pd.DataFrame(index=combined.index)

    close = _extract("close")
    open_ = _extract("open")
    high = _extract("high")
    low = _extract("low")
    vol = _extract("volume")

    for df in [close, open_, high, low, vol]:
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.droplevel(0) if len(df.columns.names) > 1 else df.columns

    tickers = list(close.columns)
    min_coverage = 0.5
    good_cols = close.notna().mean() > min_coverage
    tickers = [t for t in tickers if good_cols.get(t, False)]

    close = close[tickers]
    open_ = open_[tickers]
    high = high[tickers]
    low = low[tickers]
    vol = vol[tickers]

    returns = close.pct_change()
    vwap = (high + low + close) / 3
    adv20 = vol.rolling(20).mean()
    adv60 = vol.rolling(60).mean()
    cap = close * vol.rolling(20).mean()

    date_range = f"{close.index[0].strftime('%Y-%m-%d')} to {close.index[-1].strftime('%Y-%m-%d')}"

    return MarketData(
        open=open_, high=high, low=low, close=close, volume=vol,
        returns=returns, vwap=vwap, adv20=adv20, adv60=adv60, cap=cap,
        sector=sector_map, industry=industry_map,
        tickers=tickers, date_range=date_range,
    )
