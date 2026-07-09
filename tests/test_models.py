from vienna_rentals.models import Listing


def _advert(**attributes):
    """Build a minimal willhaben advert payload with the given attributes."""
    return {
        "id": "12345",
        "description": "Nice flat",
        "attributes": {
            "attribute": [{"name": name, "values": values} for name, values in attributes.items()]
        },
    }


def test_from_advert_maps_attributes_to_fields():
    advert = _advert(
        PRICE=["750.5"],
        NUMBER_OF_ROOMS=["2"],
        ESTATE_SIZE=["48"],
        STATE=["Wien"],
        LOCATION=["Wien, 05. Bezirk, Margareten"],
        PROPERTY_TYPE=["Wohnung"],
        PUBLISHED_String=["2026-07-09T14:17:00Z"],
    )

    listing = Listing.from_advert(advert)

    assert listing.ad_id == "12345"
    assert listing.description == "Nice flat"
    assert listing.price == "750.5"
    assert listing.rooms == "2"
    assert listing.size == "48"
    assert listing.state == "Wien"
    assert listing.location == "Wien, 05. Bezirk, Margareten"
    assert listing.property_type == "Wohnung"
    assert listing.published_date == "2026-07-09T14:17:00Z"


def test_from_advert_defaults_missing_fields_to_na():
    listing = Listing.from_advert({"id": "999", "attributes": {"attribute": []}})

    assert listing.ad_id == "999"
    assert listing.description == "N/A"
    assert listing.rent == "N/A"
    assert listing.address == "N/A"


def test_from_advert_joins_multivalue_attributes():
    listing = Listing.from_advert(_advert(LOCATION=["Wien", "05. Bezirk", "Margareten"]))

    assert listing.location == "Wien, 05. Bezirk, Margareten"


def test_to_record_uses_csv_column_names_in_order():
    record = Listing(ad_id="1", price="500").to_record()

    assert list(record.keys()) == list(Listing.CSV_COLUMNS.values())
    assert record["Ad ID"] == "1"
    assert record["Price"] == "500"
    assert record["Size (m²)"] == "N/A"
