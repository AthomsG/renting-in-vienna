"""Client for the willhaben search API."""

import logging
import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

import requests
from tqdm import tqdm

from vienna_rentals import config
from vienna_rentals.models import Listing

logger = logging.getLogger(__name__)


def get_total_pages(session: requests.Session) -> int:
    """Determine how many result pages the current search parameters yield."""
    try:
        response = session.get(
            config.WILLHABEN_SEARCH_URL,
            headers=config.WILLHABEN_HEADERS,
            params=config.SEARCH_PARAMS,
            timeout=config.REQUEST_TIMEOUT,
        )
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error("Error fetching total pages: %s", e)
        return 0

    data = response.json()
    rows_found = data.get("rowsFound", 0)
    rows_returned = data.get("rowsReturned", 0)
    if rows_returned == 0:
        logger.error("API returned rowsReturned=0.")
        return 0

    total_pages = -(-rows_found // rows_returned)  # ceiling division
    logger.info(
        "Total rows found: %d, rows per page: %d, total pages: %d",
        rows_found,
        rows_returned,
        total_pages,
    )
    return total_pages


def fetch_page(session: requests.Session, page: int) -> dict[str, Any] | None:
    """Fetch one result page, retrying on rate limits, timeouts, and errors."""
    params = {**config.SEARCH_PARAMS, "page": str(page)}

    for attempt in range(config.MAX_RETRIES + 1):
        try:
            response = session.get(
                config.WILLHABEN_SEARCH_URL,
                headers=config.WILLHABEN_HEADERS,
                params=params,
                timeout=config.REQUEST_TIMEOUT,
            )
            if response.status_code == 429:
                logger.warning("Rate limited on page %d; waiting 5 seconds.", page)
                time.sleep(5)
                continue
            response.raise_for_status()
            return response.json()
        except requests.Timeout:
            logger.warning(
                "Timeout on page %d (attempt %d/%d).", page, attempt + 1, config.MAX_RETRIES + 1
            )
        except requests.RequestException as e:
            logger.warning(
                "Error fetching page %d (attempt %d/%d): %s",
                page,
                attempt + 1,
                config.MAX_RETRIES + 1,
                e,
            )
            time.sleep(1)

    logger.error("Failed to fetch page %d after %d retries.", page, config.MAX_RETRIES)
    return None


def parse_page(data: dict[str, Any]) -> list[Listing]:
    """Extract the listings from one page of API results."""
    adverts = data.get("advertSummaryList", {}).get("advertSummary", [])
    return [Listing.from_advert(advert) for advert in adverts]


def scrape_all_listings() -> list[Listing]:
    """Scrape every result page, in polite batches, and return all listings."""
    listings: list[Listing] = []

    with requests.Session() as session:
        total_pages = get_total_pages(session)
        if total_pages == 0:
            logger.warning("No pages to scrape.")
            return listings

        for batch_start in range(1, total_pages + 1, config.PAGE_BATCH_SIZE):
            batch_end = min(batch_start + config.PAGE_BATCH_SIZE - 1, total_pages)
            with ThreadPoolExecutor(max_workers=config.MAX_WORKERS) as executor:
                futures = [
                    executor.submit(fetch_page, session, page)
                    for page in range(batch_start, batch_end + 1)
                ]
                progress = tqdm(
                    as_completed(futures),
                    total=len(futures),
                    desc=f"Scraping pages {batch_start}-{batch_end}",
                )
                for future in progress:
                    if data := future.result():
                        listings.extend(parse_page(data))

            if batch_end < total_pages:
                wait_time = random.randint(10, 20)
                logger.info(
                    "Scraped pages %d-%d; pausing %d seconds.", batch_start, batch_end, wait_time
                )
                time.sleep(wait_time)

    logger.info("Scraped %d listings in total.", len(listings))
    return listings
