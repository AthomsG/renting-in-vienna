import pandas as pd
import pytest
import requests

from vienna_rentals import telegram
from vienna_rentals.config import Settings

SETTINGS = Settings(telegram_bot_token="token", telegram_channel_id="channel")


def _listings(rows):
    """Build a notification frame; rows are (link, hours_ago) tuples."""
    now = pd.Timestamp.now(tz="UTC")
    return pd.DataFrame(
        [
            {
                "Link": link,
                "Published Date": now - pd.Timedelta(hours=hours_ago),
                "Location": "Wien, 05. Bezirk, Margareten",
                "Rent (€)": "600",
                "Size (m²)": "48",
                "Rooms": "2",
            }
            for link, hours_ago in rows
        ]
    )


class _FakeResponse:
    def __init__(self, ok=True):
        self._ok = ok

    def raise_for_status(self):
        if not self._ok:
            raise requests.HTTPError("boom")


def test_sends_one_message_per_listing_oldest_first(monkeypatch):
    sent = []
    monkeypatch.setattr(
        telegram.requests,
        "post",
        lambda url, data, timeout: sent.append(data) or _FakeResponse(),
    )

    telegram.send_notifications(_listings([("newer", 1), ("older", 5)]), SETTINGS)

    assert len(sent) == 2
    assert "older" in sent[0]["text"]
    assert "newer" in sent[1]["text"]


def test_message_contains_the_listing_details(monkeypatch):
    sent = []
    monkeypatch.setattr(
        telegram.requests,
        "post",
        lambda url, data, timeout: sent.append(data) or _FakeResponse(),
    )

    telegram.send_notifications(_listings([("https://example.org/ad", 1)]), SETTINGS)

    text = sent[0]["text"]
    assert "https://example.org/ad" in text
    assert "600" in text
    assert "48" in text
    assert sent[0]["parse_mode"] == "HTML"


def test_empty_frame_sends_nothing(monkeypatch):
    monkeypatch.setattr(
        telegram.requests,
        "post",
        lambda *args, **kwargs: pytest.fail("must not send anything"),
    )

    telegram.send_notifications(_listings([]).head(0), SETTINGS)


def test_missing_credentials_raise_before_sending():
    with pytest.raises(ValueError, match="BOT_API_KEY"):
        telegram.send_notifications(_listings([("a", 1)]), Settings())


def test_failed_sends_are_reported_at_the_end(monkeypatch):
    responses = iter([_FakeResponse(ok=False), _FakeResponse(ok=True)])
    sent = []
    monkeypatch.setattr(
        telegram.requests,
        "post",
        lambda url, data, timeout: sent.append(data) or next(responses),
    )

    with pytest.raises(RuntimeError, match="1 of 2"):
        telegram.send_notifications(_listings([("a", 2), ("b", 1)]), SETTINGS)

    # The failure of the first message did not stop the second.
    assert len(sent) == 2
