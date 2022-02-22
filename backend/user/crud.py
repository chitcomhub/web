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

    async def get_user_all(self):
        return await UserCrud.get_objects_all(self.model)

    async def get_user_pk(self, pk):
        return await UserCrud.get_object_or_404(self.model, pk)
