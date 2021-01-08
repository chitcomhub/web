from typing import Optional
from datetime import date

from pydantic import BaseModel, Field, HttpUrl


class Unit(BaseModel):
    id: int = Field(
        ...,
        title="id",
    )
    first_name: str = Field(
        ...,
        title="Имя",
        example="Арби",
        max_length=200,
    )
    last_name: str = Field(
        ...,
        title="Фамилия",
        example="Башаев",
        max_length=200,
    )
    short_bio: str = Field(
        ...,
        title="Описание",
        example="Я немного интроверт",
        max_length=200,
    )
    long_bio: Optional[str] = Field(
        None,
        title="Полное описание",
        example="Работаю программистом в компании SkinSwipe",
        max_length=600,
    )
    birthday: date
    telegram: Optional[str] = Field(
        None,
        title="Телеграм",
        example="arbios",
        max_length=200,
    )
    github: Optional[str] = Field(
        None, title="Гитхаб",
        example="arbios",
        max_length=200,
    )
    photo: Optional[HttpUrl] = Field(
        None,
        title="Фото",
        example="http://pic.com/123.png",
    )

    class Config:
        orm_mode = True
