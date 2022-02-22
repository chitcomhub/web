from typing import Union, List

from fastapi import APIRouter
from user.crud import UserCrud
from user.schema import UserSchema, UserCreateSchema
from user.models import User

user = APIRouter(tags=["User"])


@user.get('/members', response_model=Union[UserSchema, List[UserSchema]])
async def members():
    user_crud = UserCrud(model=User)
    users = await user_crud.get_user_all()
    return users


@user.get('/members/{members_id}', response_model=UserSchema)
async def members(
        members_id: int
):
    user_crud = UserCrud(model=User)
    user = await user_crud.get_user_pk(members_id)
    return user
