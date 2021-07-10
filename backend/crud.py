from datetime import datetime, timezone
from sqlalchemy.orm import Session

import models
import schema


def get_members(db_session: Session, skip: int = 0, limit: int = 100):
    return db_session.query(models.Member).offset(skip).limit(limit).all()


def get_member(db_session: Session, member_id: int):
    return db_session.query(models.Member).filter(models.Member.id == member_id).first()


def create_member(db_session: Session, member: schema.Member):
    db_member = models.Member(
                    first_name=member.first_name, 
                    last_name=member.last_name, 
                    short_bio=member.short_bio,
                    long_bio=member.long_bio,
                    birthday=member.birthday,
                    telegram=member.telegram,
                    github=member.github,
                    photo=member.photo,
                    modified=datetime.now(timezone.utc)
    )
    db_session.add(db_member)
    db_session.commit()
    db_session.refresh(db_member)
    return db_member


def delete_member(db_session: Session, member_id: int):
    db_member = db_session.query(models.Member).filter(models.Member.id == member_id).first()
    db_session.delete(db_member)
    db_session.commit()
    return f"Юнит {db_member.first_name} {db_member.last_name} [id={db_member.id}] удален"