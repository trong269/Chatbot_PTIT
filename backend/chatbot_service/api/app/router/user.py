from typing import List
from fastapi import status, HTTPException, Depends, APIRouter, FastAPI, Response
from sqlalchemy.orm import Session
from .. import schemas, utils, models, oauth2
from ..database import get_db
from sqlalchemy import or_

router = APIRouter(
    prefix="/users",
    tags=['users']
)

# @router.get("/", response_model= List[schemas.UserOut])
# async def get_user(user_id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
#     users = db.query(models.User).all()

#     if not users:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User doesn't exist")

#     return users

@router.get("/", response_model= schemas.UserOut)
async def get_user(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # if user_id != current_user.user_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You don't have permission to do this")
    
    # Kiểm tra xem user_id có tồn tại trong group_id không
    user = db.query(models.User).filter(models.User.user_id == current_user.user_id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} doesn't exist")

    return user

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    user_query = db.query(models.User).filter(models.User.username == user.username)
    user_found = user_query.first()

    if user_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"username: {user.username} already exits")
    
    user_query = db.query(models.User).filter(models.User.email == user.email)
    user_found = user_query.first()

    if user_found:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"email: {user.email} already exits")
    
    utils.validate_password_strength(user.password)

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(**user.dict())
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)

    return new_user  

@router.put("/", response_model=schemas.UserOut)
async def update_user(user_update: schemas.UserUpdate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):        
    if user_update.email != current_user.email:
        user_query = db.query(models.User).filter(models.User.email == user_update.email)
        if user_query.first():
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"email: {user_update.email} already exits")
        
    user = db.query(models.User).filter(models.User.user_id == current_user.user_id).first()

    user.password = utils.hash(user_update.password)
    user.email = user_update.email
    user.full_name = user_update.full_name

    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    if user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"You don't have permission to do it")
    user_query = db.query(models.User).filter(models.User.user_id == user_id)

    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
