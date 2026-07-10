"""Transformations from the raw history to the public Kaggle dataset.

The public dataset contains only Vienna apartments (State "Wien", Property
Type "Wohnung" — the raw history also carries a tail of other states and
apartment subtypes), enriched with a binary ``Wohn-Ticket`` column (adverts
reserved for holders of Vienna's social-housing ticket, spelled "Wohnticket",
"Wohn-Ticket", or "wohn ticket" in listing descriptions) and stripped of
internal or constant columns: ``Ad ID`` (internal identifier), ``Description``
and ``Address`` (free text), ``State`` (constant after the filter) and
``District`` (duplicates the district in ``Location``).
"""

import logging
import re

import pandas as pd

from vienna_rentals import config
from vienna_rentals.models import Listing

logger = logging.getLogger(__name__)

DESCRIPTION_COLUMN = Listing.CSV_COLUMNS["description"]
STATE_COLUMN = Listing.CSV_COLUMNS["state"]
PROPERTY_TYPE_COLUMN = Listing.CSV_COLUMNS["property_type"]

WOHN_TICKET_PATTERN = re.compile(r"wohn[\s\-]?ticket", re.IGNORECASE)

PUBLISHED_STATE = "wien"  # matched case-insensitively; the data contains both spellings
PUBLISHED_PROPERTY_TYPE = "Wohnung"

COLUMNS_TO_DROP = [
    Listing.CSV_COLUMNS["ad_id"],
    Listing.CSV_COLUMNS["description"],
    Listing.CSV_COLUMNS["address"],
    Listing.CSV_COLUMNS["state"],
    Listing.CSV_COLUMNS["district"],
]


def add_wohn_ticket_column(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with a 0/1 ``Wohn-Ticket`` column derived from the description."""
    df = df.copy()
    df[config.WOHN_TICKET_COLUMN] = (
        df[DESCRIPTION_COLUMN].fillna("").astype(str).str.contains(WOHN_TICKET_PATTERN).astype(int)
    )
    return df


def select_vienna_apartments(history: pd.DataFrame) -> pd.DataFrame:
    """Keep only rows for apartments (Wohnung) located in Vienna."""
    in_vienna = (
        history[STATE_COLUMN].fillna("").astype(str).str.strip().str.lower() == PUBLISHED_STATE
    )
    is_apartment = (
        history[PROPERTY_TYPE_COLUMN].fillna("").astype(str).str.strip() == PUBLISHED_PROPERTY_TYPE
    )
    return history[in_vienna & is_apartment]


def prepare_public_export(history: pd.DataFrame) -> pd.DataFrame:
    """Build the public dataset: filter to Vienna apartments, enrich with
    Wohn-Ticket, drop internal columns."""
    filtered = select_vienna_apartments(history)
    export = add_wohn_ticket_column(filtered).drop(columns=COLUMNS_TO_DROP, errors="ignore")

    if len(export) != len(filtered):
        raise RuntimeError(
            f"Export changed the row count ({len(filtered)} -> {len(export)}). Refusing to publish."
        )

    logger.info(
        "Prepared public export: %d of %d history rows, %d flagged Wohn-Ticket.",
        len(export),
        len(history),
        int(export[config.WOHN_TICKET_COLUMN].sum()),
    )
    return export
