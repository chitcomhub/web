from fastapi import FastAPI

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
