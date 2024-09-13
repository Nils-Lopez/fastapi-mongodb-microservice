from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    mongo_uri: str = os.getenv("MONGO_URI")
    mongo_db_name: str = os.getenv("MONGO_DB_NAME")
    encryption_key: str = os.getenv("ENCRYPTION_KEY")
    host_url: str = os.getenv("HOST_URL")
    secret: str = os.getenv("SECRET")

    class Config:
        env_file = ".env"


settings = Settings()
