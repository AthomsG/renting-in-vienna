import pandas as pd
import pytest

from vienna_rentals import kaggle_export
from vienna_rentals.models import Listing


def _store(n=3):
    records = [Listing(ad_id=str(i), description=f"flat {i}").to_record() for i in range(n)]
    return pd.DataFrame(records)


def test_prepare_export_drops_internal_and_constant_columns():
    export = kaggle_export.prepare_export(_store())

    for dropped in ("Ad ID", "Description", "Address", "State", "District"):
        assert dropped not in export.columns
    assert "Price" in export.columns
    assert "Location" in export.columns


def test_prepare_export_keeps_all_rows():
    store = _store(5)

    export = kaggle_export.prepare_export(store)

    assert len(export) == len(store)


def test_prepare_export_tolerates_missing_columns():
    # Should not raise even if a column is already absent
    export = kaggle_export.prepare_export(pd.DataFrame({"Price": [1, 2]}))

    assert list(export.columns) == ["Price"]


def test_kaggle_executable_returns_resolved_path(monkeypatch):
    monkeypatch.setattr(kaggle_export.shutil, "which", lambda executable: "/usr/local/bin/kaggle")

    assert kaggle_export._kaggle_executable() == "/usr/local/bin/kaggle"


def test_kaggle_executable_raises_when_cli_is_missing(monkeypatch):
    monkeypatch.setattr(kaggle_export.shutil, "which", lambda executable: None)

    with pytest.raises(FileNotFoundError, match="kaggle CLI executable"):
        kaggle_export._kaggle_executable()
