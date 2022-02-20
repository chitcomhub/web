from fastapi import FastAPI

from user.api import user
from db.conf import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user, prefix='/user')
