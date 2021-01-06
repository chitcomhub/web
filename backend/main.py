from fastapi import FastAPI

from schemas import Unit
import database


app = FastAPI()


@app.get('/')
def home():
    return {"title": "Welcome to CHITCOM home page"}


@app.get('/units')
def get_units():
    result = database.select_query("units")
    return result


@app.get('/units/{unit_id}')
def get_unit(unit_id: int):
    result = database.select_query("units")
    return result[unit_id-1]


@app.post('/units/create')
def create_unit(unit: Unit):
    result = database.insert_unit(unit)
    return result
