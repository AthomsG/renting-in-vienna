import pytest

from vienna_rentals.config import Settings


def _clear_env(monkeypatch):
    for env_var in [*Settings.ENV_VARS.values(), "DEDUP_WINDOW_DAYS"]:
        monkeypatch.delenv(env_var, raising=False)


def test_from_env_reads_all_variables(monkeypatch):
    _clear_env(monkeypatch)
    monkeypatch.setenv("KAGGLE_USERNAME", "user")
    monkeypatch.setenv("KAGGLE_API_KEY", "key")
    monkeypatch.setenv("PRIVATE_KAGGLE_DATASET_SLUG", "user/private")
    monkeypatch.setenv("KAGGLE_DATASET_SLUG", "user/public")
    monkeypatch.setenv("BOT_API_KEY", "token")
    monkeypatch.setenv("CHANNEL_ID", "channel")

    settings = Settings.from_env()

    assert settings.kaggle_username == "user"
    assert settings.private_dataset_slug == "user/private"
    assert settings.public_dataset_slug == "user/public"
    assert settings.telegram_bot_token == "token"
    assert settings.dedup_window_days == 30


def test_empty_string_counts_as_unset(monkeypatch):
    _clear_env(monkeypatch)
    monkeypatch.setenv("KAGGLE_USERNAME", "")

    assert Settings.from_env().kaggle_username is None


def test_dedup_window_is_configurable(monkeypatch):
    _clear_env(monkeypatch)
    monkeypatch.setenv("DEDUP_WINDOW_DAYS", "14")

    assert Settings.from_env().dedup_window_days == 14


@pytest.mark.parametrize("value", ["fourteen", "0", "-3"])
def test_invalid_dedup_window_is_rejected(monkeypatch, value):
    _clear_env(monkeypatch)
    monkeypatch.setenv("DEDUP_WINDOW_DAYS", value)

    with pytest.raises(ValueError, match="DEDUP_WINDOW_DAYS"):
        Settings.from_env()


def test_ensure_reports_every_missing_variable_at_once():
    with pytest.raises(ValueError) as excinfo:
        Settings(kaggle_username="user").ensure(*Settings.KAGGLE_FIELDS)

    message = str(excinfo.value)
    assert "KAGGLE_API_KEY" in message
    assert "PRIVATE_KAGGLE_DATASET_SLUG" in message
    assert "KAGGLE_DATASET_SLUG" in message
    assert "KAGGLE_USERNAME" not in message


def test_ensure_passes_when_fields_are_set():
    settings = Settings(telegram_bot_token="token", telegram_channel_id="channel")

    settings.ensure(*Settings.TELEGRAM_FIELDS)  # must not raise
