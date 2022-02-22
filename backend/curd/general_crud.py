from asyncpg import UniqueViolationError
from sqlalchemy import select, insert, update, delete

from db.conf import database
from fastapi import HTTPException


class GeneralCrud:

    @staticmethod
    async def get_object_by_pk(model, pk: int):
        query = select(model).where(model.id == pk)
        object = await database.fetch_one(query)
        return object

    @staticmethod
    async def get_objects_all(model):
        query = select(model)
        objects = await database.fetch_all(query)
        return objects

    @staticmethod
    async def get_object_or_404(model, pk):
        query = select(model).where(model.id == pk)
        object = await database.fetch_one(query)
        if not object:
            raise HTTPException(status_code=404, detail="Object not found")
        return object

    @staticmethod
    async def create_object_or_409(model, data):
        query = insert(model).values(**data.dict())
        try:
            object = await database.execute(query)
        except UniqueViolationError:
            raise HTTPException(status_code=409, detail="Object already exist")
        return object

    @staticmethod
    async def update_object(model, data, pk):
        query = (
            update(model).
                where(model.id == pk).
                values(**data.dict())
        )
        return await database.execute(query)

    @staticmethod
    async def delete_object_404(model, pk):
        query = (
            select(model).
                where(model.id == pk)
        )
        object = await database.execute(query)
        if not object:
            return await GeneralCrud.get_object_or_404(model, pk)
        else:
            query = (
                delete(model).
                where(model.id == pk)
            )
            await database.execute(query)
            return {"detail": "Object deleted!"}
