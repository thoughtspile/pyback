"""Database models for suggestor app."""

from sqlalchemy import Boolean, Column, Float, Integer, Text

from .database import Base


class PointOfInterest(Base):
    """Point of interest DB model."""

    __tablename__ = "points_of_intereset"

    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    title = Column(Text)
    description = Column(Text)

    lat = Column(Float)
    lon = Column(Float)
