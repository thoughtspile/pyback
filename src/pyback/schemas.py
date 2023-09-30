"""Database schema for suggestor app."""

from pydantic import BaseModel, ConfigDict


class Point(BaseModel):
    """Geographic point (lat / lon)."""

    lat: float
    lon: float


class PointOfInterestBase(Point):
    """Point of interest (tagged and descibed)."""

    description: str
    title: str

    model_config = ConfigDict(from_attributes=True)


class PointOfInterestCreate(PointOfInterestBase):
    """Point of interest for create (no id)."""

    pass


class PointOfInterest(PointOfInterestBase):
    """Point of interest with id."""

    id: int
