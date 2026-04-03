"""Default router module."""

from fastapi import APIRouter

from server_template.models.basemodel.health_basemodel import HealthRead

default_router = APIRouter()


@default_router.get("/health", response_model=HealthRead)
async def health() -> HealthRead:
    """Route to check app health.

    Returns:
        HealthRead: health status.
    """
    return HealthRead(status="up")
