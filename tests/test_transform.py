import pandas as pd
import pytest

from vienna_rentals import transform
from vienna_rentals.models import Listing


def _frame(descriptions, **overrides):
    """Vienna-apartment listings (they pass the export filter) with optional overrides."""
    fields = {"state": "Wien", "property_type": "Wohnung", **overrides}
    return pd.DataFrame(
        [
            Listing(ad_id=str(i), description=description, **fields).to_record()
            for i, description in enumerate(descriptions)
        ]
    )


# ---------- Wohn-Ticket ---------- #


@pytest.mark.parametrize(
    "description",
    [
        "Direktvergabe nur mit gültigem Wohnticket",
        "Gemeindewohnung, Wohn-Ticket erforderlich",
        "Nur mit wohn ticket",
        "NUR MIT WOHNTICKET (VMD 30.09.2026)",
    ],
)
def test_wohn_ticket_spelling_variants_are_flagged(description):
    result = transform.add_wohn_ticket_column(_frame([description]))

    assert result.iloc[0]["Wohn-Ticket"] == 1


def test_regular_listing_is_not_flagged():
    result = transform.add_wohn_ticket_column(_frame(["Schöne 2-Zimmer-Wohnung im 7. Bezirk"]))

    assert result.iloc[0]["Wohn-Ticket"] == 0


def test_missing_description_is_not_flagged():
    frame = _frame(["irrelevant"])
    frame["Description"] = None

    result = transform.add_wohn_ticket_column(frame)

    assert result.iloc[0]["Wohn-Ticket"] == 0


# ---------- Vienna-apartment filter ---------- #


def test_non_vienna_listings_are_dropped():
    frame = pd.concat(
        [_frame(["in Wien"]), _frame(["anderswo"], state="Niederösterreich")],
        ignore_index=True,
    )

    export = transform.prepare_public_export(frame)

    assert len(export) == 1


def test_lowercase_wien_is_kept():
    # The historical data contains a handful of rows with State spelled "wien".
    export = transform.prepare_public_export(_frame(["a"], state="wien"))

    assert len(export) == 1


def test_non_apartment_property_types_are_dropped():
    frame = pd.concat(
        [_frame(["Wohnung"]), _frame(["Dachgeschoß"], property_type="Dachgeschoßwohnung")],
        ignore_index=True,
    )

    export = transform.prepare_public_export(frame)

    assert len(export) == 1


# ---------- export shape ---------- #


def test_export_drops_internal_constant_and_redundant_columns():
    export = transform.prepare_public_export(_frame(["a", "b"]))

    for dropped in (
        "Ad ID",
        "Description",
        "Address",
        "State",
        "District",
        "Property Type",
        "Price",
        "Postcode",
    ):
        assert dropped not in export.columns
    assert "Rent (€)" in export.columns
    assert "Location" in export.columns
    assert "Wohn-Ticket" in export.columns


def test_export_keeps_all_vienna_apartment_rows():
    frame = _frame(["a", "b", "c", "d", "e"])

    export = transform.prepare_public_export(frame)

    assert len(export) == len(frame)


def test_export_derives_wohn_ticket_before_dropping_description():
    export = transform.prepare_public_export(_frame(["Wohnticket nötig", "normale Wohnung"]))

    assert list(export["Wohn-Ticket"]) == [1, 0]
