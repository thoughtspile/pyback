"""FastAPI router module."""
from fastapi import Depends, FastAPI, HTTPException, UploadFile
from sqlalchemy.orm import Session

from . import crud, database, s3, schemas

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
    return crud.create_poi(body, db)


@app.get("/poi/{id}", response_model=schemas.PointOfInterest)
async def get_poi(id: int, db: Session = Depends(get_db)):
    """Get point of intereset by id."""
    db_poi = crud.get_poi(id, db)
    if db_poi is None:
        raise HTTPException(status_code=404, detail="PoI not found")
    return db_poi


@app.get("/suggest", response_model=list[schemas.PointOfInterest])
async def suggest_poi(lat: float, lon: float, db: Session = Depends(get_db)):
    """Suggest closest points of interest."""
    return crud.suggest_poi(pivot=schemas.Point(lat=lat, lon=lon), db=db)


@app.post("/upload")
async def upload_file(file: UploadFile):
    """Upload file and return S3 key."""
    key = s3.upload_file(file.file, file.filename)
    if key:
        return {"key": key}
    raise HTTPException(status_code=500)
