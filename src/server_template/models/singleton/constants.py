"""Constants module."""

import os

from server_template.utils.common.singleton import Singleton


class Constants(Singleton):
    """Constants class."""

    # LOGGER

    LOGS_FILE = "server_template/core/logger/logs/server_template.logs"
    LOGS_FILE_SIZE = 5 * 1080 * 1000
    NUMBER_LOGS_FILE = 4

    # SERVER

    SERVER_TITLE = "server_template"
    SERVER_VERSION = os.getenv("SERVER_VERSION", "test")
    API_TITLE = "Server Template"
