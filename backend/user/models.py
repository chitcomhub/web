from sqlalchemy import Column, Integer, String, Date, DateTime
from db.conf import Base


class User(Base):
    __tablename__ = "user"

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
