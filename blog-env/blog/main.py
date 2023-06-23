from fastapi import FastAPI,Depends, HTTPException,Response,status
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext


models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


app=FastAPI()

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")


@app.post("/blog",status_code=201,tags=['blogs'])
def create(request:schemas.Blog,db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog',response_model=List[schemas.ShowBlog],tags=['blogs'])
def all(db:Session = Depends(get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
def getblog(id,response:Response,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        response.status_code=status.HTTP_404_NOT_FOUND
    return blog


@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['blogs'])
def destroy(id,db:Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return 'done'

# for updating a existing thing use put method
@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['blogs'])
def update(id,request:schemas.Blog,db:Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    blog.update(request.dict())
    db.commit()
    return 'updated'


@app.post('/user',response_model=schemas.ShowUser,tags=['users'])
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    hashedpw=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name,email=request.email,password=hashedpw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['users'])
def getuser(id:int,response:Response,db:Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user

