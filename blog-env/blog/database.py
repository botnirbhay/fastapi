from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL ='sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread":False})


# now create a session using session maker
SessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)
# now create a declarative base instance
Base=declarative_base()


