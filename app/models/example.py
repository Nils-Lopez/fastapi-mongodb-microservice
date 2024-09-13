from pydantic import BaseModel, Field
from bson import ObjectId
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from app.config import settings
from app.models.object_id import PyObjectId


class Example(BaseModel):
    """
    Example model class.

    Attributes:
        id (PyObjectId): The unique identifier for the example.
        name (str): The name of the example.
        other_field (str): Another field for the example.
        created_at (datetime): The timestamp when the example was created.
        expires_at (datetime): The timestamp when the example expires.

    Config:
        json_encoders (dict): A dictionary mapping ObjectId to str for JSON encoding.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    other_field: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime = Field(
        default_factory=lambda: datetime.utcnow() + timedelta(minutes=5)
    )

    class Config:
        json_encoders = {ObjectId: str}
