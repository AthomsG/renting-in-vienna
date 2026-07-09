"""Dev utility: dump one raw willhaben API response to response_pretty.txt
so the payload structure can be inspected.

Run with: uv run python scripts/inspect_api.py
"""

import json

import requests

from vienna_rentals import config

response = requests.get(
    config.WILLHABEN_SEARCH_URL,
    headers=config.WILLHABEN_HEADERS,
    params=config.SEARCH_PARAMS,
    timeout=config.REQUEST_TIMEOUT,
)
print(f"response: {response}")

if response.ok:
    with open("response_pretty.txt", "w") as file:
        json.dump(response.json(), file, indent=4)
