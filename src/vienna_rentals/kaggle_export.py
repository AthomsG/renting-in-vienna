"""Publish the cumulative listings store to Kaggle.

The published dataset is the full, unfiltered history of every Vienna
apartment ever scraped, with the ``Ad ID`` column removed. Several guards
make sure the dataset can only ever grow:
- the store is append-only and deduplicated by Ad ID (see storage.py),
- the export must clear an absolute row-count floor,
- the new CSV must not be drastically smaller than the published one.
Any violation aborts the publish (and fails the workflow).
"""

import json
import logging
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

import pandas as pd

from vienna_rentals import config, storage

logger = logging.getLogger(__name__)


def setup_kaggle_credentials() -> None:
    """Make Kaggle API credentials available to the CLI and SDK.

    The key is exposed both ways because Kaggle CLI 2.x uses different auth
    per endpoint: reads accept the legacy kaggle.json (username + key), but
    the blob upload used by 'datasets version' only accepts the key as a
    bearer token taken from the KAGGLE_API_TOKEN environment variable —
    with only kaggle.json it fails with 'Authentication required'.
    """
    kaggle_username = os.getenv("KAGGLE_USERNAME")
    kaggle_key = os.getenv("KAGGLE_API_KEY")
    if not kaggle_username or not kaggle_key:
        raise ValueError("KAGGLE_USERNAME and/or KAGGLE_API_KEY environment variables are not set.")

    os.environ["KAGGLE_API_TOKEN"] = kaggle_key  # inherited by the CLI subprocess

    kaggle_config_dir = Path("~/.kaggle").expanduser()
    kaggle_config_dir.mkdir(parents=True, exist_ok=True)
    kaggle_json_path = kaggle_config_dir / "kaggle.json"
    kaggle_json_path.write_text(json.dumps({"username": kaggle_username, "key": kaggle_key}))
    kaggle_json_path.chmod(0o600)
    logger.info("Kaggle API credentials set up successfully.")


def prepare_export(df: pd.DataFrame) -> pd.DataFrame:
    """Strip the ad identifier before publication."""
    return df.drop(columns=[storage.AD_ID_COLUMN])


def get_published_file_size(dataset_slug: str, filename: str) -> int | None:
    """Return the size in bytes of ``filename`` in the published dataset,
    or None if it cannot be determined (e.g. first publication)."""
    try:
        # deferred: importing kaggle authenticates, which needs kaggle.json
        from kaggle.api.kaggle_api_extended import KaggleApi

        api = KaggleApi()
        api.authenticate()
        result = api.dataset_list_files(dataset_slug)
        for f in result.files:
            if f.name == filename:
                return getattr(f, "total_bytes", None) or getattr(f, "size", None)
    except Exception as e:
        logger.warning("Could not determine published file size: %s", e)
    return None


def _normalize_metadata_file(metadata_file: Path, dataset_slug: str) -> None:
    """Rewrite the downloaded metadata into the format ``datasets version``
    expects.

    Kaggle CLI 2.x downloads metadata as ``{"info": {...}}`` but its own
    ``datasets version`` command requires a top-level ``id`` key, failing
    with "ID or slug must be specified in the metadata" otherwise. The
    page metadata (title, subtitle, ...) is carried over so a version bump
    does not blank it out.
    """
    meta = json.loads(metadata_file.read_text())
    if "id" in meta:
        return  # already in the expected format

    info = meta.get("info", {})
    normalized = {"id": dataset_slug}
    for key in ("title", "subtitle", "description", "keywords", "licenses"):
        if info.get(key) is not None:
            normalized[key] = info[key]
    metadata_file.write_text(json.dumps(normalized, indent=2))


def _kaggle_executable() -> str:
    executable = shutil.which("kaggle")
    if executable is None:
        raise FileNotFoundError("The kaggle CLI executable was not found on PATH.")
    return executable


def update_kaggle_dataset(dataset_folder: Path, dataset_slug: str, version_notes: str) -> None:
    """Create a new version of the Kaggle dataset from ``dataset_folder``."""
    kaggle = _kaggle_executable()
    subprocess.run(
        [kaggle, "datasets", "metadata", dataset_slug, "-p", str(dataset_folder)],
        check=True,
    )

    metadata_file = dataset_folder / "dataset-metadata.json"
    if not metadata_file.exists():
        raise FileNotFoundError(f"Metadata file {metadata_file} not found!")
    _normalize_metadata_file(metadata_file, dataset_slug)

    logger.info("Creating a new version of the dataset...")
    subprocess.run(
        [kaggle, "datasets", "version", "-p", str(dataset_folder), "-m", version_notes],
        check=True,
    )
    logger.info("Dataset updated successfully.")


def publish_to_kaggle() -> None:
    """Export the full listings store (without Ad ID) as a new dataset version."""
    dataset_slug = os.getenv("KAGGLE_DATASET_SLUG")
    if not dataset_slug:
        raise ValueError("KAGGLE_DATASET_SLUG environment variable is not set.")

    setup_kaggle_credentials()

    listings = storage.load_listings()
    if len(listings) < config.MIN_PUBLISH_ROWS:
        raise RuntimeError(
            f"Export has only {len(listings)} rows (floor is {config.MIN_PUBLISH_ROWS}). "
            "This looks like data loss upstream. Aborting publish."
        )

    export = prepare_export(listings)
    if len(export) != len(listings):
        raise RuntimeError(
            f"Export changed the row count ({len(listings)} -> {len(export)}). Aborting publish."
        )

    with tempfile.TemporaryDirectory() as tmp_dir:
        dataset_folder = Path(tmp_dir)
        csv_path = dataset_folder / config.KAGGLE_DATASET_CSV_NAME
        export.to_csv(csv_path, index=False)

        new_size = csv_path.stat().st_size
        published_size = get_published_file_size(dataset_slug, config.KAGGLE_DATASET_CSV_NAME)
        if published_size and new_size < 0.5 * published_size:
            raise RuntimeError(
                f"New CSV ({new_size} bytes) is less than half the published one "
                f"({published_size} bytes). This looks like data loss. Aborting publish."
            )

        update_kaggle_dataset(
            dataset_folder,
            dataset_slug,
            version_notes=f"Automated update: {len(export)} listings.",
        )
