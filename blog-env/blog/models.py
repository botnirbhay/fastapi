from sqlalchemy import Column, Integer
from . import database


class Blog(database.Base):
    id=Column(Integer,primary_key=True,index=True)
    tile=Column(str)
    bosy=Column(str)
