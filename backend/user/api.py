from typing import Union, List

from fastapi import APIRouter
from user.crud import UserCrud
from user.schema import (
    UserSchema,
    UserCreateSchema
)
from user.models import User

user = APIRouter(tags=["User"])


@user.get('/members', response_model=Union[UserSchema, List[UserSchema]])
async def members():
    return await UserCrud.get_objects_all(User)


@user.get('/members/{members_id}', response_model=UserSchema)
async def members(members_id: int):
    return await UserCrud.get_object_or_404(User, members_id)


@user.post('/members')
async def member_create(user_data: UserCreateSchema):
    user_crud = UserCrud(model=User)
    object = await user_crud.create_user(data=user_data)
    return {"id": object, **user_data.dict()}
