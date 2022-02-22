from typing import Optional

from pydantic import BaseModel, Field, HttpUrl
from datetime import date


class UserCreateSchema(BaseModel):
    first_name: str = Field()
    last_name: str = Field()
    short_bio: str = Field()
    long_bio: Optional[str] = Field()
    birthday: Optional[date]
    telegram: Optional[str] = Field()
    github: Optional[str] = Field()
    photo: Optional[HttpUrl] = Field()


class UserSchema(UserCreateSchema):
    id: int = Field()


class SpecializationCreateSchema(BaseModel):
    name: str = Field()
    description: str = Field()


class SpecializationSchema(SpecializationCreateSchema):
    id: int = Field()


class SpecializationUpdateSchema(SpecializationCreateSchema):
    name: Optional[str] = Field()
    description: Optional[str] = Field()
