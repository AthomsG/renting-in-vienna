"""The cumulative listing history and new-listing detection.

``full_history.csv``, stored in a private Kaggle dataset, is the pipeline's
only state: an append-only log of every listing ever scraped. Each run
downloads it, appends the listings it hasn't seen before, and uploads it back.
Nothing is ever updated in place or deleted, so the file can only grow.

A scraped ad counts as *new* when its Ad ID does not appear among the history
rows published within the dedup window (default 30 days). Matching against the
full history instead would be wrong: willhaben may recycle Ad IDs over long
horizons, and a recycled ID is a genuinely different apartment that deserves a
row and a notification. The window is safe because the scraper only returns
ads published in the last two days — an ad we already recorded is always well
inside it.

History rows whose Published Date cannot be parsed are conservatively treated
as recent: a suppressed notification is a smaller failure than a duplicate row
and a duplicate message.
"""

import logging
from pathlib import Path

import pandas as pd

from vienna_rentals.models import Listing

logger = logging.getLogger(__name__)

AD_ID_COLUMN = Listing.CSV_COLUMNS["ad_id"]
PUBLISHED_COLUMN = Listing.CSV_COLUMNS["published_date"]
CSV_COLUMNS = list(Listing.CSV_COLUMNS.values())


def load_history(path: Path) -> pd.DataFrame:
    """Load the history CSV, validating that the expected schema is present."""
    history = pd.read_csv(path, dtype={AD_ID_COLUMN: str})

    missing = [column for column in CSV_COLUMNS if column not in history.columns]
    if missing:
        raise ValueError(
            f"History file {path} is missing expected columns: {', '.join(missing)}. "
            "Refusing to continue with a malformed history."
        )

    logger.info("Loaded history: %d rows.", len(history))
    return history


def listings_to_frame(listings: list[Listing]) -> pd.DataFrame:
    """Convert listings to a DataFrame with the canonical history columns."""
    frame = pd.DataFrame([listing.to_record() for listing in listings], columns=CSV_COLUMNS)
    frame[AD_ID_COLUMN] = frame[AD_ID_COLUMN].astype(str)
    return frame


def recently_seen_ids(
    history: pd.DataFrame, window_days: int, now: pd.Timestamp | None = None
) -> set[str]:
    """Return the Ad IDs of history rows published within the dedup window.

    Rows with unparseable dates are included (treated as recent) so that a
    corrupt date can never cause a listing to be re-appended and re-notified.
    """
    if history.empty:
        return set()

    now = now if now is not None else pd.Timestamp.now(tz="UTC")
    cutoff = now - pd.Timedelta(days=window_days)

    published = pd.to_datetime(history[PUBLISHED_COLUMN], errors="coerce", utc=True)
    recent = (published >= cutoff) | published.isna()
    return set(history.loc[recent, AD_ID_COLUMN].astype(str))


def select_new_listings(
    scraped: list[Listing],
    history: pd.DataFrame,
    window_days: int,
    now: pd.Timestamp | None = None,
) -> list[Listing]:
    """Return the scraped listings not yet in the recent history, deduplicated.

    The same ad can appear on multiple result pages of one scrape, so the
    batch itself is deduplicated by Ad ID as well (first occurrence wins).
    """
    seen = recently_seen_ids(history, window_days, now)

    new_listings: list[Listing] = []
    batch_ids: set[str] = set()
    for listing in scraped:
        ad_id = str(listing.ad_id)
        if ad_id in seen or ad_id in batch_ids:
            continue
        batch_ids.add(ad_id)
        new_listings.append(listing)

    logger.info(
        "%d of %d scraped listings are new (dedup window: %d days).",
        len(new_listings),
        len(scraped),
        window_days,
    )
    return new_listings


def append_listings(history: pd.DataFrame, new_listings: list[Listing]) -> pd.DataFrame:
    """Append new listings to the history, guaranteeing append-only growth."""
    combined = pd.concat([history, listings_to_frame(new_listings)], ignore_index=True)

    if len(combined) != len(history) + len(new_listings):
        raise RuntimeError(
            f"Appending {len(new_listings)} listings to {len(history)} history rows "
            f"produced {len(combined)} rows. Refusing to continue."
        )

    return combined
