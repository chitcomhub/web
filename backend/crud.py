from datetime import datetime

from sqlalchemy.orm import Session

import models
import schemas


def get_units(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Unit).offset(skip).limit(limit).all()


def get_unit(db: Session, unit_id: int):
    return db.query(models.Unit).filter(models.Unit.id == unit_id).first()


def create_unit(db: Session, unit: schemas.Unit):
    db_unit = models.Unit(first_name=unit.first_name,
                          last_name=unit.last_name,
                          short_bio=unit.short_bio,
                          birthday=datetime.now())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit


def delete_unit(db: Session, unit_id: int):
    db_unit = db.query(models.Unit).filter(models.Unit.id == unit_id).first()
    db.delete(db_unit)
    db.commit()
    return f"Юнит {db_unit.first_name} {db_unit.last_name} [id={db_unit.id}] удален"
