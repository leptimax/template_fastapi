"""Swagger Router module."""

from fastapi import APIRouter
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from starlette.responses import HTMLResponse

from server_template.models.singleton.constants import Constants

swagger_router = APIRouter()


@swagger_router.get("/docs")
async def custom_swagger_ui_html() -> HTMLResponse:
    """Get Swagger doc.

    Returns:
        HTMLResponse: HTML Page

    """
    return get_swagger_ui_html(
        openapi_url="/api/openapi.json",
        title=Constants.API_TITLE + " - Swagger UI",
        swagger_js_url="/api/assets/swagger/swagger-ui-bundle.js",
        swagger_css_url="/api/assets/swagger/swagger-ui.css",
        swagger_favicon_url="/api/assets/server_template.ico",
    )


@swagger_router.get("/redoc", include_in_schema=False)
async def redoc_html() -> HTMLResponse:
    """Redoc Swagger page.

    Returns:
        HTMLResponse: HTML Page.

    """
    return get_redoc_html(
        openapi_url="/api/openapi.json",
        title=Constants.API_TITLE + " - Redoc",
        redoc_js_url="/api/assets/swagger/redoc.standalone.js",
        redoc_favicon_url="/api/assets/server_template.ico",
    )
