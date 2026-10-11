from settings import Settings

from main import export_envs, load_secrets


def test_settings():
    load_secrets()
    export_envs("test")

    settings = Settings()
    assert settings.APP_NAME == "lab1"
    assert settings.ENVIRONMENT == "test"
    assert settings.FAKE_API_KEY == "123xd"
