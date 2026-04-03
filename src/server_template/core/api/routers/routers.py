"""Main router module."""

from fastapi import APIRouter

from server_template.core.api.routers.default.default_router import default_router
from server_template.core.api.routers.swagger.swagger_router import swagger_router

router = APIRouter()
router.include_router(default_router, prefix="", tags=["default"])
router.include_router(swagger_router, prefix="/api")
