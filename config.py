from pydantic_settings import BaseSettings, SettingsConfigDict

# sqlite:///database.sqlite
# sqlite+aiosqlite:///database.sqlite
# postgresql+asyncpg://admin:admin@localhost/db


class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    DEBUG: bool = True

    HOST: str = "0.0.0.0"
    PORT: int = 3000
    ALLOWED_ORIGINS: str = "*"

    POSTGRES_PASSWORD: str = "admin"
    POSTGRES_USER: str = "admin"
    POSTGRES_DB: str = "testdb"
    POSTGRESQL_PORT: int = 5432

    PGADMIN_DEFAULT_EMAIL: str = "admin@pgadmin.com"
    PGADMIN_DEFAULT_PASSWORD: str = "admin"
    PGADMIN_LISTEN_PORT: int = 80

    
    LOG_LEVEL: str = "DEBUG"
    LOG_RETENTION: str = "1 week"
    LOG_PATH: str = "logs.log"


    CDK_ACCOUNT: str
    CDK_REGION: str 

    def get_db_url(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@pgsql:{self.POSTGRESQL_PORT}/{self.POSTGRES_DB}"
        

cfg = Config()
