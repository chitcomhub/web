from sqlalchemy import Column, Integer, String, Date
from database import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    short_bio = Column(String, index=True)
    long_bio = Column(String, index=True)
    birthday = Column(Date)
    telegram = Column(String, index=True)
    github = Column(String, index=True)
