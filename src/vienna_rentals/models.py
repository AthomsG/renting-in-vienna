"""Data model for a rental listing."""

from dataclasses import dataclass, fields
from typing import Any, ClassVar

# Maps willhaben attribute names to Listing field names.
ATTRIBUTE_TO_FIELD = {
    "LOCATION": "location",
    "POSTCODE": "postcode",
    "PRICE": "price",
    "NUMBER_OF_ROOMS": "rooms",
    "ESTATE_SIZE": "size",
    "STATE": "state",
    "DISTRICT": "district",
    "LOCATION_QUALITY": "location_quality",
    "FLOOR": "floor",
    "PROPERTY_TYPE": "property_type",
    "PUBLISHED_String": "published_date",
    "RENT/PER_MONTH_LETTINGS": "rent",
    "ADDRESS": "address",
}


@dataclass(slots=True)
class Listing:
    """A single rental advert as returned by the willhaben search API."""

    ad_id: str
    description: str = "N/A"
    location: str = "N/A"
    postcode: str = "N/A"
    price: str = "N/A"
    rooms: str = "N/A"
    size: str = "N/A"
    state: str = "N/A"
    district: str = "N/A"
    location_quality: str = "N/A"
    floor: str = "N/A"
    property_type: str = "N/A"
    published_date: str = "N/A"
    rent: str = "N/A"
    address: str = "N/A"

    # CSV column name for each field, in column order.
    CSV_COLUMNS: ClassVar[dict[str, str]] = {
        "ad_id": "Ad ID",
        "description": "Description",
        "location": "Location",
        "postcode": "Postcode",
        "price": "Price",
        "rooms": "Rooms",
        "size": "Size (m²)",
        "state": "State",
        "district": "District",
        "location_quality": "Location Quality",
        "floor": "Floor",
        "property_type": "Property Type",
        "published_date": "Published Date",
        "rent": "Rent (€)",
        "address": "Address",
    }

    @classmethod
    def from_advert(cls, advert: dict[str, Any]) -> "Listing":
        """Build a Listing from one advert entry of the search API payload."""
        values: dict[str, str] = {"ad_id": advert.get("id", "N/A")}
        if description := advert.get("description"):
            values["description"] = description

        for attribute in advert.get("attributes", {}).get("attribute", []):
            field = ATTRIBUTE_TO_FIELD.get(attribute.get("name"))
            if field:
                values[field] = ", ".join(attribute.get("values", []))

        return cls(**values)

    def to_record(self) -> dict[str, str]:
        """Return the listing as a CSV-column-keyed dict."""
        return {self.CSV_COLUMNS[f.name]: getattr(self, f.name) for f in fields(self)}
