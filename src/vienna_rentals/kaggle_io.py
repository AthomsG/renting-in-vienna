"""Kaggle transport: credentials, dataset download, and dataset publishing.

This module knows nothing about listings — it moves CSV files between the
local filesystem and Kaggle datasets. Data-integrity decisions (what may be
published) belong to the pipeline; the one guard that lives here,
:func:`check_not_shrinking`, is transport-level because it compares against
the currently *published* file size.
"""

import json
import logging
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from vienna_rentals.config import Settings

logger = logging.getLogger(__name__)


def configure_credentials(settings: Settings) -> None:
    """Make Kaggle API credentials available to the CLI and SDK.

    The key is exposed both ways because Kaggle CLI 2.x uses different auth
    per endpoint: reads accept the legacy kaggle.json (username + key), but
    the blob upload used by 'datasets version' only accepts the key as a
    bearer token taken from the KAGGLE_API_TOKEN environment variable —
    with only kaggle.json it fails with 'Authentication required'.
    """
    settings.ensure("kaggle_username", "kaggle_api_key")

    os.environ["KAGGLE_API_TOKEN"] = settings.kaggle_api_key  # inherited by CLI subprocesses

    kaggle_config_dir = Path("~/.kaggle").expanduser()
    kaggle_config_dir.mkdir(parents=True, exist_ok=True)
    kaggle_json_path = kaggle_config_dir / "kaggle.json"
    kaggle_json_path.write_text(
        json.dumps({"username": settings.kaggle_username, "key": settings.kaggle_api_key})
    )
    kaggle_json_path.chmod(0o600)
    logger.info("Kaggle API credentials set up successfully.")


def _kaggle_executable() -> str:
    executable = shutil.which("kaggle")
    if executable is None:
        raise FileNotFoundError("The kaggle CLI executable was not found on PATH.")
    return executable


def _extract_single_csv(archive: Path, filename: str, dest_dir: Path) -> Path:
    """Extract ``filename`` from a downloaded zip archive into ``dest_dir``."""
    with zipfile.ZipFile(archive) as zf:
        if filename not in zf.namelist():
            raise FileNotFoundError(
                f"{filename} not found in downloaded archive {archive.name} "
                f"(contains: {', '.join(zf.namelist())})."
            )
        zf.extract(filename, dest_dir)
    archive.unlink()
    return dest_dir / filename


def download_dataset_csv(dataset_slug: str, filename: str, dest_dir: Path) -> Path:
    """Download one CSV file from a Kaggle dataset into ``dest_dir``.

    Depending on file size, the Kaggle CLI delivers either the file itself or
    a ``<filename>.zip`` archive; both cases are handled.
    """
    kaggle = _kaggle_executable()
    try:
        subprocess.run(
            [
                kaggle,
                "datasets",
                "download",
                "-d",
                dataset_slug,
                "-f",
                filename,
                "-p",
                str(dest_dir),
            ],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Could not download {filename} from {dataset_slug}. If the dataset does "
            "not exist yet, seed it first (see the 'seed' command)."
        ) from e

    csv_path = dest_dir / filename
    archive_path = dest_dir / f"{filename}.zip"
    if not csv_path.exists() and archive_path.exists():
        csv_path = _extract_single_csv(archive_path, filename, dest_dir)

    if not csv_path.exists() or csv_path.stat().st_size == 0:
        raise RuntimeError(f"Download of {filename} from {dataset_slug} produced no data.")

    logger.info(
        "Downloaded %s (%d bytes) from %s.", filename, csv_path.stat().st_size, dataset_slug
    )
    return csv_path


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


def check_not_shrinking(csv_path: Path, dataset_slug: str) -> None:
    """Abort if the CSV is drastically smaller than the currently published one."""
    new_size = csv_path.stat().st_size
    published_size = get_published_file_size(dataset_slug, csv_path.name)
    if published_size and new_size < 0.5 * published_size:
        raise RuntimeError(
            f"New {csv_path.name} ({new_size} bytes) is less than half the published one "
            f"({published_size} bytes) in {dataset_slug}. This looks like data loss. "
            "Aborting publish."
        )


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


def publish_version(dataset_folder: Path, dataset_slug: str, version_notes: str) -> None:
    """Create a new version of an existing Kaggle dataset from ``dataset_folder``."""
    kaggle = _kaggle_executable()
    subprocess.run(
        [kaggle, "datasets", "metadata", dataset_slug, "-p", str(dataset_folder)],
        check=True,
    )

    metadata_file = dataset_folder / "dataset-metadata.json"
    if not metadata_file.exists():
        raise FileNotFoundError(f"Metadata file {metadata_file} not found!")
    _normalize_metadata_file(metadata_file, dataset_slug)

    logger.info("Creating a new version of %s...", dataset_slug)
    subprocess.run(
        [kaggle, "datasets", "version", "-p", str(dataset_folder), "-m", version_notes],
        check=True,
    )
    logger.info("Dataset %s updated successfully.", dataset_slug)


def publish_csv_version(csv_source: Path, dataset_slug: str, version_notes: str) -> None:
    """Publish a single CSV as a new version of ``dataset_slug``, with the
    anti-shrink guard applied first."""
    check_not_shrinking(csv_source, dataset_slug)
    with tempfile.TemporaryDirectory() as tmp_dir:
        dataset_folder = Path(tmp_dir)
        shutil.copy2(csv_source, dataset_folder / csv_source.name)
        publish_version(dataset_folder, dataset_slug, version_notes)


def create_private_dataset(csv_source: Path, dataset_slug: str, title: str) -> None:
    """Create ``dataset_slug`` as a new *private* dataset containing one CSV.

    Used once, by the ``seed`` command, to bootstrap the history dataset.
    """
    kaggle = _kaggle_executable()
    with tempfile.TemporaryDirectory() as tmp_dir:
        dataset_folder = Path(tmp_dir)
        shutil.copy2(csv_source, dataset_folder / csv_source.name)

        metadata = {
            "id": dataset_slug,
            "title": title,
            "licenses": [{"name": "CC0-1.0"}],
        }
        (dataset_folder / "dataset-metadata.json").write_text(json.dumps(metadata, indent=2))

        # 'kaggle datasets create' is private by default; no --public flag here.
        subprocess.run(
            [kaggle, "datasets", "create", "-p", str(dataset_folder)],
            check=True,
        )
    logger.info("Private dataset %s created.", dataset_slug)
