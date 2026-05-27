"""Singleton class module."""

from typing import Any


class Singleton(type):
    """The Singleton metaclass."""

    _instances: dict[type, Any] = {}

    def __call__(cls, *args, **kwargs):
        """Call method.

        Returns:
            object: The singleton instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
