from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException

import os
from fastapi_sqlalchemy import DBSessionMiddleware # automatically creates db session
from fastapi_sqlalchemy import db
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import crud
import schema

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get('/')
def home():
    return {"title": "Welcome to CHITCOM home page"}

@app.get("/api/members", response_model=List[schema.Member])
def get_members(skip: int = 0, limit: int = 100):
    members = crud.get_members(db_session=db.session, skip=skip, limit=limit)
    return members

@app.get('/api/members/{member_id}', response_model=schema.Member)
def get_member(member_id: int):
    db_member = crud.get_member(db_session=db.session, member_id=member_id)
    if db_member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return db_member

@app.post("/api/members/create", response_model=schema.Member)
def create_member(member: schema.Member):
    return crud.create_member(db_session=db.session, member=member)

@app.delete('/api/members/{member_id}')
def delete_member(member_id: int):
    return crud.delete_member(db_session=db.session, member_id=member_id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)