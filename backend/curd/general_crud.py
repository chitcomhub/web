from sqlalchemy import select

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
