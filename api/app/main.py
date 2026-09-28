from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import setup_logging
from app.db.init_db import init_db
from app.middleware.cors import setup_cors
from app.middleware.request_logger import request_logger
from app.api.routes import api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup and shutdown lifecycle.
    """
    setup_logging()
    init_db()

    yield


app = FastAPI(
    title="Smart Traffic AI",
    description="AI-Based Smart Traffic Violation Detection System",
    version="1.0.0",
    lifespan=lifespan,
)

setup_cors(app)
app.middleware("http")(request_logger)
app.include_router(
    api_router,
    prefix="/api/v1",
)

@app.get("/")
def root():
    return {
        "message": "Smart Traffic AI API is running",
        "version": "1.0.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }