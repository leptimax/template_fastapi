"""Server Module."""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from prometheus_fastapi_instrumentator import Instrumentator

from server_template.core.api.routers.routers import router
from server_template.models.singleton.constants import Constants


class Server:
    """Class for initialize and launch a FASTAPI app with Static files and router."""

    def __init__(self):
        """Init function."""
        self.app: FastAPI = FastAPI(
            title=Constants.SERVER_TITLE,
            docs_url=None,
            redoc_url=None,
            openapi_url="/api/openapi.json",
            version=Constants.SERVER_VERSION,
        )

    def __mount_asset(self):
        """Mount local assets."""
        self.app.mount(
            "/api/assets",
            StaticFiles(directory="server_template/core/api/assets"),
            name="assets",
        )

    def __mount_metrics(self):
        """Mount metrics endpoint."""
        Instrumentator().instrument(self.app).expose(self.app, endpoint="/metrics")

    def __register_router(self):
        """Register api router."""
        self.app.include_router(router)

    def __register_middleware(self):
        """Initialize the API middleware (CORS)."""
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def run(self):
        """Call all function to initialize server."""
        self.__register_middleware()
        self.__mount_asset()
        self.__mount_metrics()
        self.__register_router()
        uvicorn.run(self.app, host="0.0.0.0", port=8000)

    def __call__(self):
        """Call method."""
        self.run()
