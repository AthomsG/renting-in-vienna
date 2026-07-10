"""One end-to-end pipeline run: scrape → dedupe → persist → publish → notify.

The pipeline is stateless by design: its only state is ``full_history.csv`` in
a private Kaggle dataset, downloaded at the start of every run and re-uploaded
with the new listings appended. Nothing is written to the git repository, so
runs stay cheap and the history stays out of version control.

Step ordering is deliberate:

1. The private history is persisted *before* any user-visible side effect.
   A corrupted or lost history breaks everything downstream, so state safety
   comes first. The trade-off (notifications are at-most-once: if a later
   step fails, its listings are never re-notified because the next run sees
   them as already known) is acceptable — a rare missed message beats
   duplicate spam and duplicate history rows.
2. The public dataset is rebuilt from the full history on every publication,
   so a failed public upload heals itself on the next successful run.
3. Telegram runs last: it is the least critical step and its failures still
   fail the workflow run, which is alerting enough.

If the scrape returns nothing new, the run exits without creating Kaggle
dataset versions or sending messages.
"""

import logging
import tempfile
from pathlib import Path

from vienna_rentals import config, filtering, history, kaggle_io, scraper, telegram, transform
from vienna_rentals.config import Settings

logger = logging.getLogger(__name__)


def run(settings: Settings, *, skip_telegram: bool = False, dry_run: bool = False) -> None:
    """Execute one full pipeline run."""
    settings.ensure(*Settings.KAGGLE_FIELDS)
    if not skip_telegram:
        settings.ensure(*Settings.TELEGRAM_FIELDS)

    kaggle_io.configure_credentials(settings)

    with tempfile.TemporaryDirectory() as tmp_dir:
        work_dir = Path(tmp_dir)

        history_csv = kaggle_io.download_dataset_csv(
            settings.private_dataset_slug, config.HISTORY_CSV_NAME, work_dir
        )
        known = history.load_history(history_csv)

        scraped = scraper.scrape_all_listings()
        if not scraped:
            # The search always yields hundreds of ads; zero means the API or
            # the scraper is broken, not that Vienna ran out of apartments.
            raise RuntimeError("Scrape returned no listings at all. Aborting run.")

        new_listings = history.select_new_listings(scraped, known, settings.dedup_window_days)
        if not new_listings:
            logger.info("No new listings this run; nothing to publish or notify.")
            return

        updated = history.append_listings(known, new_listings)
        if len(updated) < config.MIN_PUBLISH_ROWS:
            raise RuntimeError(
                f"History has only {len(updated)} rows (floor is {config.MIN_PUBLISH_ROWS}). "
                "This looks like data loss upstream. Aborting run."
            )

        if dry_run:
            logger.info(
                "[dry run] Would append %d listings (history: %d -> %d rows), "
                "publish both datasets, and notify Telegram.",
                len(new_listings),
                len(known),
                len(updated),
            )
            return

        # 1. Persist state: the updated history back to the private dataset.
        updated_csv = work_dir / config.HISTORY_CSV_NAME
        updated.to_csv(updated_csv, index=False)
        kaggle_io.publish_csv_version(
            updated_csv,
            settings.private_dataset_slug,
            version_notes=f"Automated update: +{len(new_listings)} listings "
            f"({len(updated)} total).",
        )

        # 2. Rebuild and publish the public dataset from the full history.
        export = transform.prepare_public_export(updated)
        export_csv = work_dir / config.PUBLIC_CSV_NAME
        export.to_csv(export_csv, index=False)
        kaggle_io.publish_csv_version(
            export_csv,
            settings.public_dataset_slug,
            version_notes=f"Automated update: {len(export)} listings.",
        )

        # 3. Notify about the new listings that match the personal preferences.
        if skip_telegram:
            logger.info("Telegram notifications skipped by request.")
        else:
            matching = filtering.filter_listings(history.listings_to_frame(new_listings))
            telegram.send_notifications(matching, settings)

    logger.info("Pipeline run complete: %d new listings.", len(new_listings))
