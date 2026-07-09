"""Command-line entry point for the pipeline steps.

Usage: vienna-rentals <command>

Commands:
    scrape         Scrape willhaben and merge results into the listings store.
    filter         Filter the store to personal preferences (check_these.csv).
    notify         Update the README table and send Telegram notifications.
    kaggle         Publish the full listings store (without Ad ID) to Kaggle.
    test-telegram  Send a test message to the Telegram channel.
"""

import argparse
import logging

import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")


def cmd_scrape() -> None:
    from vienna_rentals import scraper, storage

    listings = scraper.scrape_all_listings()
    storage.merge_listings(listings)


def cmd_filter() -> None:
    from vienna_rentals import filtering, storage

    filtered = filtering.filter_listings(storage.load_listings())
    filtering.save_filtered(filtered)
    print(f"There are {len(filtered)} listings that match your requirements.")


def cmd_notify() -> None:
    from vienna_rentals import config, readme, telegram

    filtered = pd.read_csv(config.FILTERED_CSV)
    recent = readme.prepare_recent_listings(filtered)

    old_links = readme.read_previous_links()  # snapshot before the table is rewritten
    readme.update_readme(recent)

    new_listings = telegram.select_new_listings(recent, old_links)
    telegram.send_notifications(new_listings)


def cmd_kaggle() -> None:
    from vienna_rentals import kaggle_export

    kaggle_export.publish_to_kaggle()


def cmd_test_telegram() -> None:
    import os

    import requests

    api_token = os.getenv("BOT_API_KEY")
    channel_id = os.getenv("CHANNEL_ID")
    response = requests.post(
        f"https://api.telegram.org/bot{api_token}/sendMessage",
        data={"chat_id": channel_id, "text": "Test message from bot", "parse_mode": "Markdown"},
        timeout=30,
    )
    if response.ok:
        print("Message sent successfully.")
    else:
        raise RuntimeError(f"Failed to send message. Response: {response.text}")


COMMANDS = {
    "scrape": cmd_scrape,
    "filter": cmd_filter,
    "notify": cmd_notify,
    "kaggle": cmd_kaggle,
    "test-telegram": cmd_test_telegram,
}


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="vienna-rentals", description="Vienna rental listings pipeline."
    )
    parser.add_argument("command", choices=COMMANDS)
    args = parser.parse_args()
    COMMANDS[args.command]()


if __name__ == "__main__":
    main()
