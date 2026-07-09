"""Central configuration: paths, API settings, and filter preferences."""

from pathlib import Path

# ---------- Paths (repo-relative, resolved from the package location) ---------- #

REPO_ROOT = Path(__file__).resolve().parents[2]

LISTINGS_CSV = REPO_ROOT / "listings" / "rental_data.csv"
FILTERED_CSV = REPO_ROOT / "check_these.csv"
README_PATH = REPO_ROOT / "README.md"

# ---------- willhaben API ---------- #

WILLHABEN_SEARCH_URL = (
    "https://www.willhaben.at/webapi/iad/search/atz/seo/immobilien/"
    "mietwohnungen/mietwohnung-angebote"
)
WILLHABEN_HEADERS = {
    "accept": "application/json",
    "x-wh-client": "api@willhaben.at;responsive_web;server;1.0.0;desktop",
}
SEARCH_PARAMS = {
    "page": "1",
    "rows": "1000",
    "areaId": "900",  # Wien
    "PROPERTY_TYPE": "3",  # Wohnung
    "periode": "2",  # posted in the last 2 days
}

REQUEST_TIMEOUT = 5  # seconds
MAX_RETRIES = 3
MAX_WORKERS = 10
PAGE_BATCH_SIZE = 50

# ---------- Filter preferences (edit these to change what lands in check_these.csv) ---------- #

MIN_PRICE = 400
MAX_PRICE = 800
MIN_ROOMS = 2
PROPERTY_TYPE = "Wohnung"
MAX_LISTING_AGE_DAYS = 1
ALLOWED_DISTRICTS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17}

LISTING_BASE_URL = "https://www.willhaben.at/iad/immobilien/d/mietwohnungen/wien/"

# ---------- README ---------- #

README_TABLE_MARKER = "## Recent Active Listings\n"
README_TABLE_SIZE = 20

# ---------- Kaggle ---------- #

KAGGLE_DATASET_CSV_NAME = "vienna_rental_listings.csv"
# Refuse to publish if the export has fewer rows than this (protects against
# publishing an accidentally truncated dataset).
MIN_PUBLISH_ROWS = 100
