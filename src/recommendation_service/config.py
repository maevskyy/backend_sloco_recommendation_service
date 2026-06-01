from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

AppEnv = Literal["development", "test", "production"]
LogLevel = Literal["debug", "info", "warning", "error", "critical"]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_env: AppEnv = Field(default="development", alias="APP_ENV")
    host: str = Field(default="0.0.0.0", alias="HOST")
    port: int = Field(default=8000, alias="PORT", gt=0)
    log_level: LogLevel = Field(default="info", alias="LOG_LEVEL")
    service_name: str = Field(
        default="recommendation-service",
        alias="SERVICE_NAME",
        min_length=1,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()

