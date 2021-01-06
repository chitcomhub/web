from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def home():
    return {"title": "Welcome to CHITCOM home page"}
