"""Data access wrappers."""
from sqlalchemy.orm import Session

from . import geo_helpers, models, schemas


def create_poi(body: schemas.PointOfInterestCreate, db: Session):
    """Save a point of intereset."""
    db_poi = models.PointOfInterest(**body.model_dump())
    db.add(db_poi)
    db.commit()
    db.refresh(db_poi)
    return db_poi


def get_poi(id: int, db: Session):
    """Get point of intereset by id."""
    return (
        db.query(models.PointOfInterest).filter(models.PointOfInterest.id == id).first()
    )


def suggest_poi(pivot: schemas.Point, db: Session):
    """Suggest closest points of interest."""
    lookup_coords = geo_helpers.lookup_rect(pivot)
    print(lookup_coords)
    db_suggest = (
        db.query(models.PointOfInterest)
        .filter(
            models.PointOfInterest.lat > lookup_coords.min_lat,
            models.PointOfInterest.lon > lookup_coords.min_lon,
            models.PointOfInterest.lat < lookup_coords.max_lat,
            models.PointOfInterest.lon < lookup_coords.max_lon,
        )
        .limit(10)
        .all()
    )
    return geo_helpers.rank(pivot, db_suggest)
