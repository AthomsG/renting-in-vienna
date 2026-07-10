import pandas as pd
import pytest

from vienna_rentals import config, history, pipeline
from vienna_rentals.config import Settings
from vienna_rentals.models import Listing

SETTINGS = Settings(
    kaggle_username="user",
    kaggle_api_key="key",
    private_dataset_slug="user/private",
    public_dataset_slug="user/public",
    telegram_bot_token="token",
    telegram_channel_id="channel",
)


def _notifiable_listing(ad_id):
    """A scraped listing that passes every personal-preference filter."""
    return Listing(
        ad_id=ad_id,
        description="Nice flat",
        location="Wien, 05. Bezirk, Margareten",
        postcode="1050",
        price="600",
        rooms="2",
        size="48",
        state="Wien",
        district="Margareten",
        property_type="Wohnung",
        published_date=pd.Timestamp.now(tz="UTC").isoformat(),
        rent="600",
    )


@pytest.fixture
def harness(monkeypatch, tmp_path):
    """Stub out all external systems and record what the pipeline does."""
    calls = []

    known = history.listings_to_frame(
        [Listing(ad_id="already-known", published_date=pd.Timestamp.now(tz="UTC").isoformat())]
    )
    history_csv = tmp_path / config.HISTORY_CSV_NAME
    known.to_csv(history_csv, index=False)

    scraped: list[Listing] = []

    monkeypatch.setattr(pipeline.kaggle_io, "configure_credentials", lambda settings: None)
    monkeypatch.setattr(
        pipeline.kaggle_io,
        "download_dataset_csv",
        lambda slug, filename, dest: calls.append(("download", slug)) or history_csv,
    )
    monkeypatch.setattr(pipeline.scraper, "scrape_all_listings", lambda: list(scraped))
    monkeypatch.setattr(
        pipeline.kaggle_io,
        "publish_csv_version",
        lambda csv, slug, version_notes: calls.append(("publish", slug, csv.name)),
    )
    monkeypatch.setattr(
        pipeline.telegram,
        "send_notifications",
        lambda listings, settings: calls.append(("telegram", len(listings))),
    )
    monkeypatch.setattr(config, "MIN_PUBLISH_ROWS", 1)

    return {"calls": calls, "scraped": scraped}


def test_happy_path_publishes_state_then_public_then_notifies(harness):
    harness["scraped"].extend([_notifiable_listing("new-1"), _notifiable_listing("new-2")])

    pipeline.run(SETTINGS)

    assert harness["calls"] == [
        ("download", "user/private"),
        ("publish", "user/private", config.HISTORY_CSV_NAME),
        ("publish", "user/public", config.PUBLIC_CSV_NAME),
        ("telegram", 2),
    ]


def test_nothing_new_publishes_and_notifies_nothing(harness):
    harness["scraped"].append(_notifiable_listing("already-known"))

    pipeline.run(SETTINGS)

    assert harness["calls"] == [("download", "user/private")]


def test_dry_run_has_no_side_effects(harness):
    harness["scraped"].append(_notifiable_listing("new-1"))

    pipeline.run(SETTINGS, dry_run=True)

    assert harness["calls"] == [("download", "user/private")]


def test_skip_telegram_still_publishes_both_datasets(harness):
    harness["scraped"].append(_notifiable_listing("new-1"))

    pipeline.run(SETTINGS, skip_telegram=True)

    assert ("publish", "user/private", config.HISTORY_CSV_NAME) in harness["calls"]
    assert ("publish", "user/public", config.PUBLIC_CSV_NAME) in harness["calls"]
    assert not any(call[0] == "telegram" for call in harness["calls"])


def test_empty_scrape_aborts_the_run(harness):
    with pytest.raises(RuntimeError, match="no listings at all"):
        pipeline.run(SETTINGS)

    assert not any(call[0] == "publish" for call in harness["calls"])


def test_missing_telegram_credentials_fail_before_any_work(harness):
    harness["scraped"].append(_notifiable_listing("new-1"))
    incomplete = Settings(
        kaggle_username="user",
        kaggle_api_key="key",
        private_dataset_slug="user/private",
        public_dataset_slug="user/public",
    )

    with pytest.raises(ValueError, match="BOT_API_KEY"):
        pipeline.run(incomplete)

    assert harness["calls"] == []
