"""Reconstruct every listing ever scraped from the git history.

The old scraper overwrote ``listings/rental_data.csv`` on every run, so each
of the ~29k commits is a snapshot of a different (mostly 2-day) window. This
script walks every version of that file across the full git history, in commit
order, and deduplicates by Ad ID (latest snapshot wins) to produce a single
CSV containing the union of every listing the repo has ever seen.

Run with:  uv run python scripts/build_full_history.py [output.csv]
"""

import csv
import subprocess
import sys
from pathlib import Path

from tqdm import tqdm

from vienna_rentals import config
from vienna_rentals.models import Listing

TRACKED_PATH = "listings/rental_data.csv"
AD_ID_COLUMN = Listing.CSV_COLUMNS["ad_id"]
EXPECTED_COLUMNS = list(Listing.CSV_COLUMNS.values())
ZERO_SHA = "0" * 40


def unique_blobs_in_commit_order() -> list[str]:
    """Every distinct blob SHA of the tracked CSV, oldest commit first."""
    raw = subprocess.run(
        [
            "git",
            "log",
            "--all",
            "--reverse",
            "--no-renames",
            "--format=",
            "--raw",
            "--",
            TRACKED_PATH,
        ],
        cwd=config.REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout

    seen: set[str] = set()
    ordered: list[str] = []
    for line in raw.splitlines():
        if not line.startswith(":"):
            continue
        # ":100644 100644 <old> <new> M\tlistings/rental_data.csv"
        new_blob = line.split()[3]
        if new_blob == ZERO_SHA or new_blob in seen:
            continue
        seen.add(new_blob)
        ordered.append(new_blob)
    return ordered


def iter_blob_contents(blobs: list[str]):
    """Yield (sha, text) for each blob using a single git cat-file process."""
    proc = subprocess.Popen(
        ["git", "cat-file", "--batch"],
        cwd=config.REPO_ROOT,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    try:
        for sha in tqdm(blobs, desc="Reading snapshots"):
            proc.stdin.write(f"{sha}\n".encode())
            proc.stdin.flush()
            header = proc.stdout.readline().split()
            if len(header) != 3:  # "<sha> missing" or unexpected
                continue
            size = int(header[2])
            content = proc.stdout.read(size)
            proc.stdout.read(1)  # trailing newline after the object
            yield sha, content.decode("utf-8", errors="replace")
    finally:
        proc.stdin.close()
        proc.stdout.close()
        proc.wait()


def build_history(output_path: Path) -> int:
    blobs = unique_blobs_in_commit_order()
    print(f"Found {len(blobs)} distinct snapshots of {TRACKED_PATH}.")

    listings: dict[str, list[str]] = {}
    for _sha, text in iter_blob_contents(blobs):
        reader = csv.reader(text.splitlines())
        header = next(reader, None)
        if header != EXPECTED_COLUMNS:
            # Skip anything that isn't the raw listings schema (e.g. a stray
            # differently-shaped file) rather than corrupt the output.
            continue
        for row in reader:
            if len(row) != len(EXPECTED_COLUMNS):
                continue
            listings[row[0]] = row  # keyed by Ad ID; latest snapshot wins

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(EXPECTED_COLUMNS)
        writer.writerows(listings.values())

    return len(listings)


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else config.REPO_ROOT / "full_history.csv"
    count = build_history(output_path)
    print(f"Wrote {count} unique listings to {output_path}")


if __name__ == "__main__":
    main()
