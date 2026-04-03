"""Health basemodel."""

from pydantic import BaseModel


class HealthBase(BaseModel):
    """Health base model."""

    status: str


class HealthRead(HealthBase):
    """Health read model."""
