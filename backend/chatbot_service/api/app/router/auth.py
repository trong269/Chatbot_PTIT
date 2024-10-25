from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from .. import database, schemas, models, utils, oauth2
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(tags = ['Authentication'])

@router.post('/login', response_model=schemas.Token)
async def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.username == user_credentials.username).first()
    # trong tất cả mọi trường hợp user_credential luôn là:
    # username: ....
    # password: ...
    # không quan trọng user gửi gì, ví dụ như id, email,... thì vẫn luôn được lưu vào username
    # giúp cho ta interact với postman bằng form-data
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credential")
    
    if not utils.verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Invalid credential")
    
    access_token = oauth2.create_access_token(data={"user_id": user.user_id})

    return{"access_token": access_token, "token_type": "bearer"}

# @router.get('/test', response_model=List[schemas.UserOut])
# async def get_post(current_user = Depends(oauth2.get_current_user), db: Session = Depends(database.get_db)):
#     users = db.query(models.User).all()
#     return users