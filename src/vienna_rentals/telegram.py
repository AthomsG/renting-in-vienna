"""Telegram notifications for new listings.

New listings are detected by comparing the freshly generated README table
against the links that were in it before:
1. 'New links' are links in the new table but not the old one.
2. The most recent 'Published Date' among the old listings is the cutoff.
3. Only new links published after that cutoff are sent - really nice deals
   have short lifespans, so stale ones aren't worth a notification.
"""

import logging
import os

import pandas as pd
import requests

logger = logging.getLogger(__name__)


def select_new_listings(recent: pd.DataFrame, old_links: list[str]) -> pd.DataFrame:
    """Return the listings from ``recent`` that deserve a notification."""
    new_links = [link for link in recent["Link"] if link not in old_links]
    old_listings = recent[recent["Link"].isin(old_links)]

    if not old_listings.empty:
        max_old_published_date = old_listings["Published Date"].max()
    else:
        max_old_published_date = pd.Timestamp("1900-01-01", tz="UTC")

    new_listings = recent[
        (recent["Link"].isin(new_links)) & (recent["Published Date"] > max_old_published_date)
    ]
    return new_listings.sort_values(by="Published Date", ascending=True)


def send_notifications(new_listings: pd.DataFrame) -> None:
    """Send one Telegram message per new listing to the channel."""
    api_token = os.getenv("BOT_API_KEY")
    channel_id = os.getenv("CHANNEL_ID")
    if not api_token or not channel_id:
        logger.error("BOT_API_KEY and/or CHANNEL_ID environment variables are not set.")
        return

    telegram_url = f"https://api.telegram.org/bot{api_token}/sendMessage"

    for _, row in new_listings.iterrows():
        formatted_date = row["Published Date"].strftime("%b %d, %H:%M")
        message = (
            f"🗓 <b>Published</b>: {formatted_date}\n\n"
            f"🏙 <b>District</b>: {row['Location']}\n"
            f"💰 <b>Rent</b>: {row['Rent (€)']} €\n"
            f"📏 <b>Size</b>: {row['Size (m²)']} m²\n"
            f"🛏 <b>Rooms</b>: {row['Rooms']} rooms\n"
            f"<a href='{row['Link']}'>🔗 Link</a>"
        )
        message_data = {
            "chat_id": channel_id,
            "text": message,
            "parse_mode": "HTML",
        }
        try:
            response = requests.post(telegram_url, data=message_data, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error("Failed to send message for listing %s: %s", row["Link"], e)

    logger.info("Sent %d Telegram notifications.", len(new_listings))
