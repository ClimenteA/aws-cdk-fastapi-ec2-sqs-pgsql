from pydantic_settings import BaseSettings, SettingsConfigDict

# sqlite:///database.sqlite
# sqlite+aiosqlite:///database.sqlite
# postgresql+asyncpg://admin:admin@localhost/db


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str = "sqlite+aiosqlite:///database.sqlite"
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 3000
    ALLOWED_ORIGINS: str = "*"
    LOG_LEVEL: str = "DEBUG"
    LOG_RETENTION: str = "1 week"
    LOG_PATH: str = "logs.log"
    

cfg = Config()
