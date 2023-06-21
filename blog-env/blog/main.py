from fastapi import FastAPI
from . import schemas,models,database



models.Base.metadata.create_all(database.engine)
app=FastAPI()


@app.post("/blog")
def create(request:schemas.Blog):
    return  request