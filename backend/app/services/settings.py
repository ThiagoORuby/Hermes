import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    DATABASE_PATH: str = os.getenv("DATABASE_PATH") or ""
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD") or ""
    DATABASE_URL: str = (
        f"postgresql+psycopg2://postgres:{POSTGRES_PASSWORD}@{DATABASE_PATH}"
    )


settings = Settings()
