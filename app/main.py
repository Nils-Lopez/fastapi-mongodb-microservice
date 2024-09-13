from fastapi import FastAPI
from app.routes.example_routes import router as example_router

from app.utils.mongo import mongo
import logging

app = FastAPI()
logger = logging.getLogger(__name__)


@app.on_event("startup")
async def startup_db_client():
    logger.info("Starting up and connecting to MongoDB")
    # MongoDB connection is already initialized in the mongo module


@app.on_event("shutdown")
async def shutdown_db_client():
    logger.info("Shutting down and closing MongoDB connection")
    await mongo.close()


@app.get("/")
async def root():
    return {"message": "Welcome to the Template Microservice v0.1.10"}


app.include_router(example_router, prefix="/example")

