from typing import List
from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from passlib.context import CryptContext

router = APIRouter(
    prefix="/user",
    tags=['users']
)

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")

@router.post('/',response_model=schemas.ShowUser,tags=['users'])
def create_user(request:schemas.User,db:Session = Depends(database.get_db)):
    hashedpw=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.name,email=request.email,password=hashedpw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/{id}',response_model=schemas.ShowUser,tags=['users'])
def getuser(id:int,db:Session = Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return user
