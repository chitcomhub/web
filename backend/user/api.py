from typing import Union, List

from fastapi import APIRouter
from user.crud import UserCrud
from user.schema import UserSchema, UserCreateSchema
from user.models import User

user = APIRouter(tags=["User"])


@user.get('/', response_model=Union[UserSchema, List[UserSchema]])
async def index(
        pk: int = None
):
    if pk:
        obj = await UserCrud.get_object_or_404(User, pk)
    else:
        obj = await UserCrud.get_objects_all(User)
    return obj


@user.post('/')
async def user_create(
        user: UserCreateSchema
):
    object = await UserCrud.create_user(User, user)
    return {"id": object, **user.dict()}
