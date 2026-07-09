import pandas as pd
import pytest

from vienna_rentals import config, storage
from vienna_rentals.models import Listing


@pytest.fixture
def store_path(tmp_path, monkeypatch):
    """Point the listings store at an isolated temp file."""
    path = tmp_path / "rental_data.csv"
    monkeypatch.setattr(config, "LISTINGS_CSV", path)
    return path


def test_load_listings_returns_empty_frame_when_missing(store_path):
    df = storage.load_listings()

    assert df.empty
    assert list(df.columns) == list(Listing.CSV_COLUMNS.values())


def test_merge_appends_new_listings(store_path):
    storage.merge_listings([Listing(ad_id="1", price="500")])
    storage.merge_listings([Listing(ad_id="2", price="600")])

    stored = storage.load_listings()
    assert set(stored["Ad ID"]) == {"1", "2"}
    assert len(stored) == 2


def test_merge_refreshes_existing_ad_in_place(store_path):
    storage.merge_listings([Listing(ad_id="1", price="500")])
    storage.merge_listings([Listing(ad_id="1", price="999")])

    stored = storage.load_listings()
    assert len(stored) == 1
    assert stored.iloc[0]["Price"] == 999


def test_merge_keeps_delisted_ads(store_path):
    storage.merge_listings([Listing(ad_id="1"), Listing(ad_id="2")])
    # Second scrape no longer contains ad 1
    storage.merge_listings([Listing(ad_id="2"), Listing(ad_id="3")])

    stored = storage.load_listings()
    assert set(stored["Ad ID"]) == {"1", "2", "3"}


def test_merge_refuses_to_shrink_the_store(store_path, monkeypatch):
    # A corrupt existing store with duplicate Ad IDs: deduping it during a
    # merge would drop rows, which the guard must refuse.
    def fake_load():
        return pd.DataFrame(
            [
                Listing(ad_id="1").to_record(),
                Listing(ad_id="1").to_record(),
                Listing(ad_id="2").to_record(),
            ]
        )

    monkeypatch.setattr(storage, "load_listings", fake_load)

    with pytest.raises(RuntimeError, match="shrink"):
        storage.merge_listings([Listing(ad_id="1")])


def test_ad_id_read_as_string_preserves_leading_values(store_path):
    storage.merge_listings([Listing(ad_id="007")])

    stored = storage.load_listings()
    assert stored.iloc[0]["Ad ID"] == "007"
