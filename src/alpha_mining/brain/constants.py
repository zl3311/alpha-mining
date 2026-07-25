"""
BRAIN API constants: endpoints, operator vocabulary, enums, and default parameters.

The operator vocabulary is used by LLM prompts to constrain formula generation
to valid BRAIN Fast Expression syntax. Organized by category per the BRAIN docs.
"""

from enum import Enum

# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

BASE_URL = "https://api.worldquantbrain.com"

ENDPOINTS = {
    "auth": f"{BASE_URL}/authentication",
    "simulations": f"{BASE_URL}/simulations",
    "alphas": f"{BASE_URL}/alphas",
    "users_self": f"{BASE_URL}/users/self",
    "data_fields": f"{BASE_URL}/data-fields",
}


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------


class Region(str, Enum):
    USA = "USA"
    EUR = "EUR"
    ASI = "ASI"
    JPN = "JPN"
    CHN = "CHN"
    KOR = "KOR"
    GLB = "GLB"


class Universe(str, Enum):
    TOP200 = "TOP200"
    TOP500 = "TOP500"
    TOP1000 = "TOP1000"
    TOP2000 = "TOP2000"
    TOP3000 = "TOP3000"


class Neutralization(str, Enum):
    NONE = "NONE"
    MARKET = "MARKET"
    SECTOR = "SECTOR"
    INDUSTRY = "INDUSTRY"
    SUBINDUSTRY = "SUBINDUSTRY"


class NanHandling(str, Enum):
    OFF = "OFF"
    ON = "ON"


class Pasteurization(str, Enum):
    OFF = "OFF"
    ON = "ON"


class AlphaLanguage(str, Enum):
    FASTEXPR = "FASTEXPR"
    EXPRESSION = "EXPRESSION"
    PYTHON = "PYTHON"


# ---------------------------------------------------------------------------
# Default Simulation Parameters
# ---------------------------------------------------------------------------

DEFAULT_SIM_SETTINGS = {
    "instrumentType": "EQUITY",
    "region": Region.USA.value,
    "universe": Universe.TOP3000.value,
    "delay": 1,
    "decay": 6,
    "truncation": 0.08,
    "neutralization": Neutralization.SUBINDUSTRY.value,
    "nanHandling": NanHandling.OFF.value,
    "unitHandling": "VERIFY",
    "pasteurization": Pasteurization.ON.value,
    "language": AlphaLanguage.FASTEXPR.value,
    "visualization": False,
}


# ---------------------------------------------------------------------------
# Operator Vocabulary (BRAIN Fast Expression Language)
# ---------------------------------------------------------------------------

PRICE_VOLUME_FIELDS = [
    "open", "high", "low", "close", "volume", "vwap",
    "returns", "adv20", "adv60", "cap",
]

CROSS_SECTIONAL_OPS = {
    "rank(x)": "Rank values across the universe at a single time step (0 to 1).",
    "reverse(x)": "Reverse the rank (equivalent to -1 * rank(x)).",
    "zscore(x)": "Z-score normalize across the universe.",
    "scale(x)": "Scale so that sum of absolute values equals 1.",
    "normalize(x)": "Normalize to zero mean and unit standard deviation.",
    "quantile(x)": "Assign quantile buckets across the universe.",
    "rank_by_side(x)": "Rank separately for long and short sides.",
}

TIME_SERIES_OPS = {
    "ts_rank(x, d)": "Time-series rank over window d.",
    "ts_delta(x, d)": "x[t] - x[t-d].",
    "ts_mean(x, d)": "Rolling mean over d days.",
    "ts_sum(x, d)": "Rolling sum over d days.",
    "ts_std_dev(x, d)": "Rolling standard deviation over d days.",
    "ts_min(x, d)": "Rolling minimum over d days.",
    "ts_max(x, d)": "Rolling maximum over d days.",
    "ts_arg_max(x, d)": "Day of max within d-day window (0 to d-1).",
    "ts_arg_min(x, d)": "Day of min within d-day window (0 to d-1).",
    "ts_decay_linear(x, d)": "Linearly-weighted moving average over d days.",
    "ts_decay_exp_window(x, d, factor)": "Exponentially-weighted moving average.",
    "ts_product(x, d)": "Rolling product over d days.",
    "ts_skewness(x, d)": "Rolling skewness over d days.",
    "ts_kurtosis(x, d)": "Rolling kurtosis over d days.",
    "ts_moment(x, d, k)": "Rolling k-th moment over d days.",
    "ts_entropy(x, d)": "Rolling entropy over d days.",
    "ts_corr(x, y, d)": "Rolling Pearson correlation over d days.",
    "ts_covariance(x, y, d)": "Rolling covariance between x and y over d days.",
    "ts_regression(y, x, d, lag, rettype)": "Rolling regression; rettype: 0=resid, 1=beta, 2=alpha.",
    "ts_zscore(x, d)": "Time-series z-score over window d.",
    "ts_delay(x, d)": "Lag x by d days.",
    "ts_backfill(x, d)": "Forward-fill NaN values up to d days.",
}

GROUP_OPS = {
    "group_neutralize(x, group)": "Demean within group (sector/industry/subindustry).",
    "group_rank(x, group)": "Rank within group.",
    "group_scale(x, group)": "Scale within group to sum-abs = 1.",
    "group_zscore(x, group)": "Z-score within group.",
    "group_backfill(x, group, d)": "Forward-fill NaN within group up to d days.",
}

GROUP_FIELDS = ["sector", "industry", "subindustry", "country", "exchange"]

LOGICAL_OPS = {
    "if_else(cond, then, else)": "Conditional: if cond > 0 return then, else return else.",
    "trade_when(cond, alpha, exit_cond)": "Hold alpha when cond is true; exit on exit_cond.",
}

ARITHMETIC_OPS = [
    "+", "-", "*", "/", "**",
    "abs(x)", "log(x)", "sign(x)", "sqrt(x)",
    "min(x, y)", "max(x, y)",
    "signed_power(x, e)",
]

DATA_QUALITY_OPS = {
    "winsorize(x)": "Cap extreme values at percentile thresholds.",
    "ts_backfill(x, d)": "Forward-fill missing values up to d days.",
    "pasteurize(x)": "Replace NaN with 0.",
}


def get_operator_vocabulary_text() -> str:
    """Format the full operator vocabulary as text for LLM prompts."""
    lines = ["# BRAIN Fast Expression Operator Vocabulary\n"]

    lines.append("## Price/Volume Data Fields")
    lines.append(", ".join(PRICE_VOLUME_FIELDS))
    lines.append("")

    for section_name, ops in [
        ("Cross-Sectional Operators", CROSS_SECTIONAL_OPS),
        ("Time-Series Operators", TIME_SERIES_OPS),
        ("Group Operators", GROUP_OPS),
        ("Logical Operators", LOGICAL_OPS),
        ("Data Quality Operators", DATA_QUALITY_OPS),
    ]:
        lines.append(f"## {section_name}")
        for sig, desc in ops.items():
            lines.append(f"- {sig}: {desc}")
        lines.append("")

    lines.append("## Group Fields")
    lines.append(", ".join(GROUP_FIELDS))
    lines.append("")

    lines.append("## Arithmetic")
    lines.append(", ".join(ARITHMETIC_OPS))

    return "\n".join(lines)
