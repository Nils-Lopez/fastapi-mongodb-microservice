# auth_routes.py
from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from typing import Optional
from bson import ObjectId
from app.utils.mongo import mongo
from datetime import datetime
import logging
from app.config import settings
router = APIRouter()
logger = logging.getLogger(__name__)


class ExampleRequest(BaseModel):
    name: str
    other_field: str
    token: str

def parse_object_id(value):
    try:
        return PyObjectId(value)
    except Exception as e:
        error_message = f"Invalid ObjectId format: {e}"
        logger.error(error_message)
        raise HTTPException(status_code=400, detail=error_message)

@router.post("/")
async def example_route(
    request: ExampleRequest,
):
    try:
        if request.token != settings.secret:
            return {
                "success": False,
                "message": "Invalid token provided",
            }
        logger.info(f"Received example request")
        db = mongo.get_database()
        example_collection = db.get_collection("examples")

        new_example = Example(
            name=request.name,
            other_field=request.other_field,
        )
        result = await example_collection.insert_one(new_example.dict(by_alias=True))

        return {
            "example_id": str(result.inserted_id),
            "success": True,
            "message": "Example created successfully",
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        logger.error(error_message)
        raise HTTPException(status_code=500, detail=error_message)

