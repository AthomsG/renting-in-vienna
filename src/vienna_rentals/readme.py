"""Maintain the 'Recent Active Listings' table in README.md.

The README doubles as a bulletin board: the links present in the previous
table are also how new listings are detected for Telegram notifications.
"""

import logging
import re
from urllib.parse import quote

import pandas as pd

from vienna_rentals import config

logger = logging.getLogger(__name__)

DISPLAY_COLUMNS = ["Rent (€)", "Size (m²)", "Rooms", "Location", "Link", "Published Date"]


def prepare_recent_listings(filtered: pd.DataFrame) -> pd.DataFrame:
    """Return the most recent listings, formatted for display."""
    df = filtered.copy()
    df["Published Date"] = pd.to_datetime(df["Published Date"], utc=True)
    df = df.sort_values(by="Published Date", ascending=False)

    recent = df.head(config.README_TABLE_SIZE)[DISPLAY_COLUMNS].copy()

    # "Wien, 05. Bezirk, Margareten" -> "05. Margareten" (see issue #1)
    recent["Location"] = recent["Location"].apply(
        lambda x: (
            f"{str(x).split(',')[1].split('.')[0]}. {str(x).split(',')[-1].strip()}"
            if isinstance(x, str)
            else "Unknown"
        )
    )
    # Encode special characters so the markdown links stay clickable
    recent["Link"] = recent["Link"].apply(lambda x: quote(x, safe="/:?=&%"))
    return recent


def read_previous_links() -> list[str]:
    """Extract the listing links currently published in the README table."""
    try:
        readme_contents = config.README_PATH.read_text()
    except FileNotFoundError:
        return []
    return re.findall(r"\[🔗\]\((.*?)\)", readme_contents)


def update_readme(recent: pd.DataFrame) -> None:
    """Rewrite the listings table in the README, leaving everything above it untouched."""
    table = recent.rename(
        columns={
            "Rent (€)": "💰 Rent (€)",
            "Size (m²)": "📏 Size (m²)",
            "Rooms": "🛏️ Rooms",
            "Location": "🏙️ District",
            "Published Date": "📅 Published Date",
        }
    )
    table["Link"] = table["Link"].apply(lambda x: f"[🔗]({x})")
    table["📅 Published Date"] = recent["Published Date"].dt.strftime("%b %d, %H:%M")

    markdown_table = table[
        ["💰 Rent (€)", "📏 Size (m²)", "🛏️ Rooms", "🏙️ District", "Link", "📅 Published Date"]
    ].to_markdown(index=False)

    readme_contents = config.README_PATH.read_text()
    if config.README_TABLE_MARKER in readme_contents:
        before_table = readme_contents.split(config.README_TABLE_MARKER)[0]
        before_table += config.README_TABLE_MARKER
    else:
        before_table = readme_contents + "\n" + config.README_TABLE_MARKER

    config.README_PATH.write_text(before_table + "\n" + markdown_table + "\n")
    logger.info("README updated with %d listings.", len(recent))
