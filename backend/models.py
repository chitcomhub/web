from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime

Base = declarative_base()

class Member(Base):
    __tablename__ = "members"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    short_bio = Column(String)
    long_bio = Column(String)
    birthday = Column(Date)
    telegram = Column(String)
    github = Column(String)
    photo = Column(String)
    modified = Column(DateTime)