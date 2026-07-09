import pandas as pd
import pytest

from vienna_rentals import filtering
from vienna_rentals.models import Listing


def _recent_iso():
    return pd.Timestamp.now(tz="UTC").isoformat()


def _row(**overrides):
    """A listing that passes every filter, with individual fields overridable."""
    base = Listing(
        ad_id="1",
        description="Nice flat",
        location="Wien, 05. Bezirk, Margareten",
        postcode="1050",
        price="600",
        rooms="2",
        size="48",
        state="Wien",
        district="Margareten",
        property_type="Wohnung",
        published_date=_recent_iso(),
        rent="600",
    ).to_record()
    base.update(overrides)
    return base


def _frame(rows):
    return pd.DataFrame(rows)


def test_passing_listing_is_kept_and_gets_a_link():
    result = filtering.filter_listings(_frame([_row()]))

    assert len(result) == 1
    assert result.iloc[0]["Link"].startswith("https://www.willhaben.at/iad/immobilien")
    assert result.iloc[0]["Link"].endswith("-1/")


@pytest.mark.parametrize(
    "overrides",
    [
        {"Price": "300"},  # below MIN_PRICE
        {"Price": "900"},  # above MAX_PRICE
        {"Rooms": "1"},  # below MIN_ROOMS
        {"State": "Niederösterreich"},  # wrong state
        {"Property Type": "Haus"},  # wrong property type
        {"Location": "Wien, 13. Bezirk, Hietzing"},  # excluded district
        {"Published Date": "2000-01-01T00:00:00Z"},  # too old
    ],
)
def test_listing_is_filtered_out(overrides):
    result = filtering.filter_listings(_frame([_row(**overrides)]))

    assert result.empty


def test_only_matching_rows_survive_in_a_mixed_batch():
    rows = [
        _row(**{"Ad ID": "1"}),
        _row(**{"Ad ID": "2", "Price": "2000"}),  # too expensive
        _row(**{"Ad ID": "3"}),
    ]

    result = filtering.filter_listings(_frame(rows))

    assert set(result["Ad ID"]) == {"1", "3"}
