from datetime import datetime

from sqlalchemy import insert

from curd.general_crud import GeneralCrud
from db.conf import database


class UserCrud(GeneralCrud):

    def __init__(self, model):
        self.model = model

    async def create_user(self, data):
        query = insert(self.model).values(**data.dict(), modified=datetime.now())
        obj_id = await database.execute(query)
        return obj_id


class SpecializationCrud(GeneralCrud):
    def __init__(self, model):
        self.model = model
