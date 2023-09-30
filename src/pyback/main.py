"""FastAPI router module."""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import database, geo_helpers, models, schemas

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


def get_db():
    """Connect to DB."""
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/poi/", response_model=schemas.PointOfInterest)
async def create_poi(
    body: schemas.PointOfInterestCreate, db: Session = Depends(get_db)
):
    """Save a point of intereset."""
    db_poi = models.PointOfInterest(**body.model_dump())
    db.add(db_poi)
    db.commit()
    db.refresh(db_poi)
    return db_poi


@app.get("/poi/{id}", response_model=schemas.PointOfInterest)
async def get_poi(id: int, db: Session = Depends(get_db)):
    """Get point of intereset by id."""
    db_poi = (
        db.query(models.PointOfInterest).filter(models.PointOfInterest.id == id).first()
    )
    if db_poi is None:
        raise HTTPException(status_code=404, detail="PoI not found")
    return db_poi


@app.get("/suggest", response_model=list[schemas.PointOfInterest])
async def suggest_poi(lat: float, lon: float, db: Session = Depends(get_db)):
    """Suggest closest points of interest."""
    pivot = schemas.Point(lat=lat, lon=lon)
    lookup_coords = geo_helpers.lookup_rect(pivot)
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
