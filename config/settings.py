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
        extra = "allow"

        case_sensitive = False

class AWSSettings(BaseSettings):
    # AWS Settings
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "us-west-1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

        case_sensitive = False


class DynamoDBSettings(BaseSettings):
    # DynamoDB Settings
    DYNAMODB_ENDPOINT: str = ""
    DYNAMODB_REGION: str = "us-west-1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "allow"

        case_sensitive = False



settings = Settings()
aws_settings = AWSSettings()
dynamodb_settings = DynamoDBSettings()