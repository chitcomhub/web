import databases
import sqlalchemy
from sqlalchemy.orm import declarative_base
from config.conf import RootConfig

DATABASE_URL = RootConfig.DB_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

Base = declarative_base()

# models
import user.models