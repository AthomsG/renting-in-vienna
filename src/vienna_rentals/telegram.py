"""Telegram notifications for new listings.

Which listings are "new" is decided upstream by Ad-ID deduplication against
the history (see history.py); this module only formats and delivers messages.
Individual send failures don't stop the remaining messages, but any failure
raises at the end so the workflow run is visibly red.
"""

import logging

import pandas as pd
import requests

from vienna_rentals.config import Settings

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT = 30  # seconds


def format_message(row: pd.Series) -> str:
    """Render one listing as a Telegram HTML message."""
    formatted_date = row["Published Date"].strftime("%b %d, %H:%M")
    return (
        f"🗓 <b>Published</b>: {formatted_date}\n\n"
        f"🏙 <b>District</b>: {row['Location']}\n"
        f"💰 <b>Rent</b>: {row['Rent (€)']} €\n"
        f"📏 <b>Size</b>: {row['Size (m²)']} m²\n"
        f"🛏 <b>Rooms</b>: {row['Rooms']} rooms\n"
        f"<a href='{row['Link']}'>🔗 Link</a>"
    )


def send_notifications(listings: pd.DataFrame, settings: Settings) -> None:
    """Send one message per listing to the channel, oldest first."""
    settings.ensure("telegram_bot_token", "telegram_channel_id")

    if listings.empty:
        logger.info("No listings to notify about.")
        return

    telegram_url = f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage"
    failures = 0

    for _, row in listings.sort_values(by="Published Date").iterrows():
        message_data = {
            "chat_id": settings.telegram_channel_id,
            "text": format_message(row),
            "parse_mode": "HTML",
        }
        try:
            response = requests.post(telegram_url, data=message_data, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
        except requests.RequestException as e:
            failures += 1
            logger.error("Failed to send message for listing %s: %s", row["Link"], e)

    sent = len(listings) - failures
    logger.info("Sent %d of %d Telegram notifications.", sent, len(listings))
    if failures:
        raise RuntimeError(f"{failures} of {len(listings)} Telegram notifications failed.")


def send_test_message(settings: Settings) -> None:
    """Send a plain test message to verify the bot token and channel ID."""
    settings.ensure("telegram_bot_token", "telegram_channel_id")

    response = requests.post(
        f"https://api.telegram.org/bot{settings.telegram_bot_token}/sendMessage",
        data={"chat_id": settings.telegram_channel_id, "text": "Test message from bot"},
        timeout=REQUEST_TIMEOUT,
    )
    if not response.ok:
        raise RuntimeError(f"Failed to send message. Response: {response.text}")
    logger.info("Test message sent successfully.")
