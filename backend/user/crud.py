from datetime import datetime

from sqlalchemy import insert

from curd.general_crud import GeneralCrud
from db.conf import database


class UserCrud(GeneralCrud):


    @staticmethod
    async def create_user(model, data):
        query = insert(model).values(**data.dict(), modified=datetime.now())
        obj_id = await database.execute(query)
        return obj_id
