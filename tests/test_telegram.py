import pandas as pd

from vienna_rentals import telegram


def _recent(rows):
    """Build a recent-listings frame; rows are (link, hours_ago) tuples."""
    now = pd.Timestamp.now(tz="UTC")
    return pd.DataFrame(
        [
            {"Link": link, "Published Date": now - pd.Timedelta(hours=hours_ago)}
            for link, hours_ago in rows
        ]
    )


def test_new_link_newer_than_old_listings_is_selected():
    recent = _recent([("old", 5), ("new", 1)])

    selected = telegram.select_new_listings(recent, old_links=["old"])

    assert list(selected["Link"]) == ["new"]


def test_new_but_older_than_all_old_listings_is_skipped():
    # 'new' is genuinely new, but published before the freshest old listing,
    # so it is not worth a notification (nice deals have short lifespans).
    recent = _recent([("old", 1), ("new", 5)])

    selected = telegram.select_new_listings(recent, old_links=["old"])

    assert selected.empty


def test_all_selected_and_sorted_ascending_when_no_old_links():
    recent = _recent([("b", 1), ("a", 3)])

    selected = telegram.select_new_listings(recent, old_links=[])

    assert list(selected["Link"]) == ["a", "b"]


def test_links_already_published_are_never_reselected():
    recent = _recent([("old", 1)])

    selected = telegram.select_new_listings(recent, old_links=["old"])

    assert selected.empty
