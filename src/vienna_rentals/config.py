"""Central configuration.

Constants that describe *what* the pipeline does (API endpoints, filter
preferences, safety thresholds) live at module level. Everything that varies
between environments — credentials and dataset slugs — is read from
environment variables into an immutable :class:`Settings` object, so a missing
variable fails loudly with a complete list of what's absent instead of halfway
through a run.
"""

import os
from dataclasses import dataclass
from typing import ClassVar

# ---------- willhaben API ---------- #

WILLHABEN_SEARCH_URL = (
    "https://www.willhaben.at/webapi/iad/search/atz/seo/immobilien/"
    "mietwohnungen/mietwohnung-angebote"
)
WILLHABEN_HEADERS = {
    "accept": "application/json",
    "x-wh-client": "api@willhaben.at;responsive_web;server;1.0.0;desktop",
}
SEARCH_PARAMS = {
    "page": "1",
    "rows": "1000",
    "areaId": "900",  # Wien
    "PROPERTY_TYPE": "3",  # Wohnung
    "periode": "2",  # posted in the last 2 days
}

REQUEST_TIMEOUT = 5  # seconds
MAX_RETRIES = 3
MAX_WORKERS = 10
PAGE_BATCH_SIZE = 50

# ---------- History / deduplication ---------- #

HISTORY_CSV_NAME = "full_history.csv"
# A scraped ad counts as already-seen only if its Ad ID appears in a history
# row published within this many days. willhaben may recycle Ad IDs over long
# horizons, so matching against the full history would silently swallow
# genuinely new listings. The scraper only returns ads published in the last
# two days (see SEARCH_PARAMS), so any window comfortably above that is safe.
DEFAULT_DEDUP_WINDOW_DAYS = 30

# ---------- Public Kaggle export ---------- #

PUBLIC_CSV_NAME = "vienna_rental_listings.csv"
WOHN_TICKET_COLUMN = "Wohn-Ticket"
# Refuse to publish if the history has fewer rows than this (protects against
# publishing an accidentally truncated dataset).
MIN_PUBLISH_ROWS = 100

# ---------- Filter preferences (what lands in the Telegram channel) ---------- #

MIN_PRICE = 400
MAX_PRICE = 800
MIN_ROOMS = 2
PROPERTY_TYPE = "Wohnung"
MAX_LISTING_AGE_DAYS = 1
ALLOWED_DISTRICTS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17}

LISTING_BASE_URL = "https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/"


@dataclass(frozen=True, slots=True)
class Settings:
    """Environment-driven runtime settings.

    All credential fields are optional at construction time so that each CLI
    command can demand exactly the variables it needs via :meth:`ensure`
    (e.g. ``test-telegram`` should not require Kaggle credentials).
    """

    kaggle_username: str | None = None
    kaggle_api_key: str | None = None
    private_dataset_slug: str | None = None
    public_dataset_slug: str | None = None
    telegram_bot_token: str | None = None
    telegram_channel_id: str | None = None
    dedup_window_days: int = DEFAULT_DEDUP_WINDOW_DAYS

    # Field name -> environment variable it is read from.
    ENV_VARS: ClassVar[dict[str, str]] = {
        "kaggle_username": "KAGGLE_USERNAME",
        "kaggle_api_key": "KAGGLE_API_KEY",
        "private_dataset_slug": "PRIVATE_KAGGLE_DATASET_SLUG",
        "public_dataset_slug": "KAGGLE_DATASET_SLUG",
        "telegram_bot_token": "BOT_API_KEY",
        "telegram_channel_id": "CHANNEL_ID",
    }

    KAGGLE_FIELDS: ClassVar[tuple[str, ...]] = (
        "kaggle_username",
        "kaggle_api_key",
        "private_dataset_slug",
        "public_dataset_slug",
    )
    TELEGRAM_FIELDS: ClassVar[tuple[str, ...]] = ("telegram_bot_token", "telegram_channel_id")

    @classmethod
    def from_env(cls) -> "Settings":
        """Build settings from the environment (empty strings count as unset)."""
        values = {field: os.getenv(env_var) or None for field, env_var in cls.ENV_VARS.items()}

        raw_window = os.getenv("DEDUP_WINDOW_DAYS")
        if raw_window is not None:
            try:
                window = int(raw_window)
            except ValueError:
                raise ValueError(
                    f"DEDUP_WINDOW_DAYS must be an integer, got {raw_window!r}."
                ) from None
            if window <= 0:
                raise ValueError(f"DEDUP_WINDOW_DAYS must be positive, got {window}.")
            values["dedup_window_days"] = window

        return cls(**values)

    def ensure(self, *field_names: str) -> None:
        """Raise a single, complete error if any of the given fields are unset."""
        missing = [self.ENV_VARS[name] for name in field_names if getattr(self, name) is None]
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(sorted(missing))}."
            )
