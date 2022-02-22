from typing import Union, List

from fastapi import APIRouter
from user.crud import UserCrud, SpecializationCrud
from user.schema import (
    UserSchema,
    UserCreateSchema,
    SpecializationSchema,
    SpecializationCreateSchema, SpecializationUpdateSchema
)
from user.models import User, Specialization

user = APIRouter(tags=["User"])


@user.get('/members', response_model=List[UserSchema])
async def members():
    return await UserCrud.get_objects_all(User)


@user.get('/members/{members_id}', response_model=UserSchema)
async def members(id: int):
    return await UserCrud.get_object_or_404(User, id)


@user.post('/members')
async def member_create(user_data: UserCreateSchema):
    user_crud = UserCrud(model=User)
    object = await user_crud.create_user(data=user_data)
    return {"id": object, **user_data.dict()}


@user.get('/specializations', response_model=List[SpecializationSchema])
async def specializations():
    return await SpecializationCrud.get_objects_all(Specialization)


@user.get(
    '/specializations/{specializations_id}',
    response_model=SpecializationSchema
)
async def specializations(id: int):
    return await SpecializationCrud.get_object_or_404(
        Specialization,
        id
    )


@user.post('/specializations', response_model=SpecializationSchema)
async def specializations(specialization_data: SpecializationCreateSchema):
    object = await SpecializationCrud.create_object_or_409(
        Specialization,
        specialization_data
    )
    return {"id": object, **specialization_data.dict()}


@user.patch(
    '/specializations/{specializations_id}',
    response_model=SpecializationUpdateSchema
)
async def specializations(
        id: int,
        specialization_data: SpecializationUpdateSchema,
):
    object = await SpecializationCrud.update_object(
        Specialization,
        specialization_data,
        id
    )
    return {"id": object, **specialization_data.dict()}


@user.delete('/specializations/{specializations_id}', )
async def specializations(id: int, ):
    return await SpecializationCrud.delete_object_404(
        Specialization,
        id
    )
