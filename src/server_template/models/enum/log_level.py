"""Log level enum module."""

from enum import Enum


class LogLevel(Enum):
    """Log level enum.

    DEBUG: DEBUG
    INFO: INFO
    WARNING: WARNING
    ERROR: ERROR
    CRITICAL: CRITICAL
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
