from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    DateTime,
    Text,
    ForeignKey
)
from db.conf import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True, nullable=False)
    last_name = Column(String, index=True, nullable=False)
    short_bio = Column(String)
    long_bio = Column(String)
    birthday = Column(Date)
    telegram = Column(String)
    github = Column(String)
    photo = Column(String)
    modified = Column(DateTime, nullable=False)
    specialization = Column(
        Integer,
        ForeignKey('specializations.id',
                   ondelete='CASCADE',
                   name='fkey_specialization_user'),
        nullable=False,
    )


class Specialization(Base):
    __tablename__ = "specializations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False, unique=True)
    description = Column(Text)
