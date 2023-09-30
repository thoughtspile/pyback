"""FastAPI router module."""
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import database, models, schemas

models.PointOfInterest.metadata.create_all(bind=database.engine)

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
