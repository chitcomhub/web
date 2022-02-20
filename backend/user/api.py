from fastapi import APIRouter, HTTPException
from sqlalchemy import insert, select
from datetime import datetime, timezone
from db.conf import database
from user.schema import UserSchema
from user.models import User

user = APIRouter()


@user.get('/', response_model=UserSchema)
async def index(
        id: int
):
    query = select(User).where(User.id == id)
    obj = await database.fetch_one(query)
    if not obj:
        raise HTTPException(status_code=404, detail="Item not found")
    return obj


@user.post('create/')
async def user_create(user: UserSchema):
    query = insert(User).values(**user.dict(), modified=datetime.now())
    obj_id = await database.execute(query)
    return {"id": obj_id, **user.dict()}
