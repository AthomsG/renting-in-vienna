"""Persistence of the cumulative listings store.

``listings/rental_data.csv`` is an append-only history of every listing ever
scraped, keyed by ``Ad ID``: new adverts are appended, adverts seen again are
refreshed in place, and rows are never removed. This file is the
deduplication source for the Kaggle export.
"""

import logging

import pandas as pd

from vienna_rentals import config
from vienna_rentals.models import Listing

logger = logging.getLogger(__name__)

AD_ID_COLUMN = Listing.CSV_COLUMNS["ad_id"]
CSV_COLUMNS = list(Listing.CSV_COLUMNS.values())


def load_listings() -> pd.DataFrame:
    """Load the cumulative listings store (empty frame if it doesn't exist yet)."""
    if not config.LISTINGS_CSV.exists():
        return pd.DataFrame(columns=CSV_COLUMNS)
    return pd.read_csv(config.LISTINGS_CSV, dtype={AD_ID_COLUMN: str})


def merge_listings(new_listings: list[Listing]) -> pd.DataFrame:
    """Merge freshly scraped listings into the cumulative store.

    Existing adverts are updated with their latest values; adverts no longer
    online are kept. Returns the updated store.
    """
    existing = load_listings()
    scraped = pd.DataFrame([listing.to_record() for listing in new_listings])
    if not scraped.empty:
        scraped[AD_ID_COLUMN] = scraped[AD_ID_COLUMN].astype(str)

    combined = pd.concat([existing, scraped], ignore_index=True)
    combined = combined.drop_duplicates(subset=AD_ID_COLUMN, keep="last")

    if len(combined) < len(existing):
        raise RuntimeError(
            f"Merge would shrink the listings store ({len(existing)} -> {len(combined)} rows). "
            "Refusing to save."
        )

    config.LISTINGS_CSV.parent.mkdir(parents=True, exist_ok=True)
    combined.to_csv(config.LISTINGS_CSV, index=False)
    logger.info(
        "Listings store updated: %d rows (%d before merge, %d scraped).",
        len(combined),
        len(existing),
        len(scraped),
    )
    return combined
