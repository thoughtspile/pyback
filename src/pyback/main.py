"""FastAPI router module."""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import database, models, schemas

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
