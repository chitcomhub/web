from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def home():
    return {"title": "Welcome to CHITCOM home page"}


@app.get("/units", response_model=List[schemas.Unit])
def read_units(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    units = crud.get_units(db, skip=skip, limit=limit)
    return units


@app.get('/units/{unit_id}', response_model=schemas.Unit)
def read_unit(unit_id: int, db: Session = Depends(get_db)):
    db_unit = crud.get_unit(db, unit_id=unit_id)
    if db_unit is None:
        raise HTTPException(status_code=404, detail="Unit not found")
    return db_unit


@app.post('/units/create', response_model=schemas.Unit)
def create_unit(unit: schemas.Unit, db: Session = Depends(get_db)):
    return crud.create_unit(db=db, unit=unit)


@app.delete('/units/{unit_id}')
def delete_unit(unit_id: int, db: Session = Depends(get_db)):
    return crud.delete_unit(db=db, unit_id=unit_id)
