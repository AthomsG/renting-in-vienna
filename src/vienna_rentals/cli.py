"""Command-line entry point.

Usage: vienna-rentals <command>

Commands:
    run            Execute one full pipeline run (scrape, dedupe, publish, notify).
    seed           Bootstrap the private history dataset from a local CSV.
    test-telegram  Send a test message to the Telegram channel.
"""

import argparse
import logging
from pathlib import Path

from vienna_rentals.config import Settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def cmd_run(args: argparse.Namespace) -> None:
    from vienna_rentals import pipeline

    pipeline.run(
        Settings.from_env(),
        skip_telegram=args.skip_telegram,
        dry_run=args.dry_run,
    )


def cmd_seed(args: argparse.Namespace) -> None:
    from vienna_rentals import config, history, kaggle_io

    settings = Settings.from_env()
    settings.ensure("kaggle_username", "kaggle_api_key", "private_dataset_slug")

    csv_path = Path(args.csv)
    if csv_path.name != config.HISTORY_CSV_NAME:
        raise SystemExit(
            f"The seed file must be named {config.HISTORY_CSV_NAME} (got {csv_path.name}); "
            "the pipeline downloads it from the dataset by that exact name."
        )
    seeded = history.load_history(csv_path)  # validates the schema before uploading
    print(f"Seeding {settings.private_dataset_slug} with {len(seeded)} rows...")

    kaggle_io.configure_credentials(settings)
    kaggle_io.create_private_dataset(
        csv_path, settings.private_dataset_slug, title="Vienna Rentals - Full History"
    )
    print("Done. The pipeline can now run against this dataset.")


def cmd_test_telegram(args: argparse.Namespace) -> None:
    from vienna_rentals import telegram

    telegram.send_test_message(Settings.from_env())
    print("Message sent successfully.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vienna-rentals", description="Vienna rental listings pipeline."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Execute one full pipeline run.")
    run_parser.add_argument(
        "--skip-telegram",
        action="store_true",
        help="Run the pipeline without sending Telegram notifications.",
    )
    run_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Scrape and report what would happen, but publish and notify nothing.",
    )
    run_parser.set_defaults(handler=cmd_run)

    seed_parser = subparsers.add_parser(
        "seed", help="Create the private history dataset from a local full_history.csv."
    )
    seed_parser.add_argument("csv", help="Path to the full_history.csv to upload.")
    seed_parser.set_defaults(handler=cmd_seed)

    test_parser = subparsers.add_parser(
        "test-telegram", help="Send a test message to the Telegram channel."
    )
    test_parser.set_defaults(handler=cmd_test_telegram)

    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.handler(args)


if __name__ == "__main__":
    main()
