import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl
from datetime import date


class UserSchema(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    short_bio: str = Field()
    long_bio: Optional[str] = Field()
    birthday: Optional[date]
    telegram: Optional[str] = Field()
    github: Optional[str] = Field()
    photo: Optional[HttpUrl] = Field()
