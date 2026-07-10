import json
import zipfile

import pytest

from vienna_rentals import kaggle_io

# ---------- executable resolution ---------- #


def test_kaggle_executable_returns_resolved_path(monkeypatch):
    monkeypatch.setattr(kaggle_io.shutil, "which", lambda executable: "/usr/local/bin/kaggle")

    assert kaggle_io._kaggle_executable() == "/usr/local/bin/kaggle"


def test_kaggle_executable_raises_when_cli_is_missing(monkeypatch):
    monkeypatch.setattr(kaggle_io.shutil, "which", lambda executable: None)

    with pytest.raises(FileNotFoundError, match="kaggle CLI executable"):
        kaggle_io._kaggle_executable()


# ---------- zip extraction ---------- #


def test_extract_single_csv_unpacks_and_removes_archive(tmp_path):
    archive = tmp_path / "full_history.csv.zip"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("full_history.csv", "Ad ID\n1\n")

    extracted = kaggle_io._extract_single_csv(archive, "full_history.csv", tmp_path)

    assert extracted.read_text() == "Ad ID\n1\n"
    assert not archive.exists()


def test_extract_single_csv_rejects_archive_without_the_file(tmp_path):
    archive = tmp_path / "full_history.csv.zip"
    with zipfile.ZipFile(archive, "w") as zf:
        zf.writestr("something_else.csv", "x\n")

    with pytest.raises(FileNotFoundError, match="not found in downloaded archive"):
        kaggle_io._extract_single_csv(archive, "full_history.csv", tmp_path)


# ---------- anti-shrink guard ---------- #


def _csv(tmp_path, content):
    path = tmp_path / "data.csv"
    path.write_text(content)
    return path


def test_check_not_shrinking_rejects_a_halved_file(tmp_path, monkeypatch):
    path = _csv(tmp_path, "tiny")
    monkeypatch.setattr(kaggle_io, "get_published_file_size", lambda slug, name: 1_000_000)

    with pytest.raises(RuntimeError, match="data loss"):
        kaggle_io.check_not_shrinking(path, "user/dataset")


def test_check_not_shrinking_accepts_a_growing_file(tmp_path, monkeypatch):
    path = _csv(tmp_path, "x" * 100)
    monkeypatch.setattr(kaggle_io, "get_published_file_size", lambda slug, name: 90)

    kaggle_io.check_not_shrinking(path, "user/dataset")  # must not raise


def test_check_not_shrinking_allows_first_publication(tmp_path, monkeypatch):
    path = _csv(tmp_path, "x")
    monkeypatch.setattr(kaggle_io, "get_published_file_size", lambda slug, name: None)

    kaggle_io.check_not_shrinking(path, "user/dataset")  # must not raise


# ---------- metadata normalization ---------- #


def test_normalize_metadata_converts_info_format(tmp_path):
    metadata_file = tmp_path / "dataset-metadata.json"
    metadata_file.write_text(json.dumps({"info": {"title": "My Data", "subtitle": "sub"}}))

    kaggle_io._normalize_metadata_file(metadata_file, "user/dataset")

    normalized = json.loads(metadata_file.read_text())
    assert normalized["id"] == "user/dataset"
    assert normalized["title"] == "My Data"
    assert normalized["subtitle"] == "sub"


def test_normalize_metadata_leaves_expected_format_alone(tmp_path):
    metadata_file = tmp_path / "dataset-metadata.json"
    original = {"id": "user/dataset", "title": "My Data"}
    metadata_file.write_text(json.dumps(original))

    kaggle_io._normalize_metadata_file(metadata_file, "user/dataset")

    assert json.loads(metadata_file.read_text()) == original
