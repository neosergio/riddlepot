from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Application Settings
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key"

    # Logging Configuration
    LOG_LEVEL: str = "INFO"

    # CORS Settings
    ALLOWED_ORIGINS: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        case_sensitive = False


settings = Settings()