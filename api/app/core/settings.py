from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    postgres_user: str = Field(..., alias="POSTGRES_USER")
    postgres_password: str = Field(..., alias="POSTGRES_PASSWORD")
    postgres_db: str = Field(..., alias="POSTGRES_DB")
    postgres_port: int = Field(5432, alias="POSTGRES_PORT")

    api_port: int = Field(8000, alias="API_PORT")

    jwt_secret_key: str = Field(..., alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field("HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(
        60,
        alias="ACCESS_TOKEN_EXPIRE_MINUTES",
    )

    cors_origins: str = Field(
        "http://localhost:5173",
        alias="CORS_ORIGINS",
    )

    log_level: str = Field("INFO", alias="LOG_LEVEL")

    # RTO Provider
    rto_provider: str = Field(
        "mock",
        alias="RTO_PROVIDER",
    )

    vahan_api_base_url: str = Field(
        ...,
        alias="VAHAN_API_BASE_URL",
    )
    vahan_api_key: str = Field(
        ...,
        alias="VAHAN_API_KEY",
    )

    sms_provider_api_key: str = Field(
        ...,
        alias="SMS_PROVIDER_API_KEY",
    )
    sms_provider_sender_id: str = Field(
        "STAAI",
        alias="SMS_PROVIDER_SENDER_ID",
    )

    inference_device: str = Field(
        "cpu",
        alias="INFERENCE_DEVICE",
    )

    frontend_port: int = Field(
        5173,
        alias="FRONTEND_PORT",
    )
    vite_api_base_url: str = Field(
        "http://localhost:8000",
        alias="VITE_API_BASE_URL",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

settings = Settings()

