"""App settings."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings."""

    POI_DB_URL: str
    AWS_URL: str
    AWS_S3_BUCKET_NAME: str
