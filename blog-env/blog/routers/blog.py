from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db:Session = Depends(database.get_db)):
     return blog.get_all(db)


@router.post("/",status_code=201)
def create(request:schemas.Blog,db:Session = Depends(database.get_db)):
    # new_blog = models.Blog(title=request.title,body=request.body,user_id=1)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog
    return blog.create(request,db)



@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def getblog(id,db:Session = Depends(database.get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # return blog
    return blog.show(id,db)


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.get_db)):
    # db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.delete(id,db)

# for updating a existing thing use put method
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session = Depends(database.get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id==id)
    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # blog.update(request.dict())
    # db.commit()
    # return 'updated'
    return blog.update(id,db,request)