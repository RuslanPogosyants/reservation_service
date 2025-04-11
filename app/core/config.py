from pydantic import PostgresDsn, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


class Settings(BaseSettings):
    DATABASE_URL: PostgresDsn = Field(
        default="postgresql+asyncpg://postgres:postgre@localhost:5432/reservation_db"
    )

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
