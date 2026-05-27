"""Prometheus metrics module."""

import time

from prometheus_client import Gauge


class Metrics:
    """Prometheus metrics class."""

    # pylint: disable=too-few-public-methods

    def __init__(self):
        """Initialise metrics."""
        self.startup_time = Gauge(
            "app_start_time_seconds", "Timestamp from start of the server"
        )

    def set_startup_time(self):
        """Set startup time."""
        self.startup_time.set(time.time())
