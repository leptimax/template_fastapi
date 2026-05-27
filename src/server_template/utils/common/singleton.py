"""Singleton class module."""


class Singleton(type):
    """The Singleton metaclass."""

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """Call method.

        Returns:
            object: The singleton instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
