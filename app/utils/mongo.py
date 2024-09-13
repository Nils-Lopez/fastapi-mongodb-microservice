from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings
import logging
from app.config import settings
# Load environment variables from .env file

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MongoSettings(BaseSettings):
    uri: str = settings.mongo_uri
    db_name: str = settings.mongo_db_name


settings = MongoSettings()


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.database = self.client[db_name]
        logger.info(f"Connected to MongoDB at {uri}")

    def get_database(self):
        return self.database

    async def close(self):
        logger.info("Closing MongoDB connection")
        self.client.close()


mongo = MongoDB(settings.uri, settings.db_name)
