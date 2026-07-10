import pandas as pd
import pytest

from vienna_rentals import history
from vienna_rentals.models import Listing

NOW = pd.Timestamp("2026-07-10T12:00:00Z")
WINDOW = 30


def _history_frame(rows):
    """Build a history frame; rows are (ad_id, published_iso) tuples."""
    return pd.DataFrame(
        [Listing(ad_id=ad_id, published_date=published).to_record() for ad_id, published in rows]
    )


def _listing(ad_id, days_ago=1):
    published = (NOW - pd.Timedelta(days=days_ago)).isoformat()
    return Listing(ad_id=ad_id, published_date=published)


# ---------- select_new_listings ---------- #


def test_unseen_listing_is_new():
    frame = _history_frame([("1", "2026-07-09T10:00:00Z")])

    new = history.select_new_listings([_listing("2")], frame, WINDOW, now=NOW)

    assert [listing.ad_id for listing in new] == ["2"]


def test_recently_seen_listing_is_not_new():
    frame = _history_frame([("1", "2026-07-09T10:00:00Z")])

    new = history.select_new_listings([_listing("1")], frame, WINDOW, now=NOW)

    assert new == []


def test_recycled_ad_id_outside_window_counts_as_new():
    # The same Ad ID last appeared months ago: willhaben recycled it for a
    # different apartment, so it must be treated as new.
    frame = _history_frame([("1", "2026-01-01T10:00:00Z")])

    new = history.select_new_listings([_listing("1")], frame, WINDOW, now=NOW)

    assert [listing.ad_id for listing in new] == ["1"]


def test_unparseable_history_date_is_treated_as_seen():
    # A corrupt date must never cause a duplicate append/notification.
    frame = _history_frame([("1", "N/A")])

    new = history.select_new_listings([_listing("1")], frame, WINDOW, now=NOW)

    assert new == []


def test_batch_duplicates_are_collapsed_to_first_occurrence():
    frame = _history_frame([])

    new = history.select_new_listings([_listing("1"), _listing("1")], frame, WINDOW, now=NOW)

    assert len(new) == 1


def test_empty_history_accepts_everything():
    empty = pd.DataFrame(columns=history.CSV_COLUMNS)

    new = history.select_new_listings([_listing("1"), _listing("2")], empty, WINDOW, now=NOW)

    assert len(new) == 2


# ---------- append_listings ---------- #


def test_append_grows_history_by_exactly_the_new_rows():
    frame = _history_frame([("1", "2026-07-09T10:00:00Z")])

    combined = history.append_listings(frame, [_listing("2"), _listing("3")])

    assert len(combined) == 3
    assert set(combined["Ad ID"]) == {"1", "2", "3"}


def test_append_nothing_returns_history_unchanged():
    frame = _history_frame([("1", "2026-07-09T10:00:00Z")])

    combined = history.append_listings(frame, [])

    assert len(combined) == 1


def test_append_preserves_existing_rows_verbatim():
    frame = _history_frame([("1", "2026-07-09T10:00:00Z")])

    combined = history.append_listings(frame, [_listing("2")])

    assert combined.iloc[0]["Published Date"] == "2026-07-09T10:00:00Z"


# ---------- load_history ---------- #


def test_load_history_reads_ad_ids_as_strings(tmp_path):
    path = tmp_path / "full_history.csv"
    _history_frame([("007", "2026-07-09T10:00:00Z")]).to_csv(path, index=False)

    loaded = history.load_history(path)

    assert loaded.iloc[0]["Ad ID"] == "007"


def test_load_history_rejects_missing_columns(tmp_path):
    path = tmp_path / "full_history.csv"
    pd.DataFrame({"Ad ID": ["1"], "Price": ["500"]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="missing expected columns"):
        history.load_history(path)
