from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, conint

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str

class UserUpdate(BaseModel):
    password: str
    email: EmailStr
    full_name: str

class UserOut(BaseModel):
    user_id: int
    username: str
    email: str
    full_name: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

# Model tin nhắn
class MessageCreate(BaseModel):
    content: str

class MessageResponse(BaseModel):
    message_id: int
    conversation_id: int
    sender: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True

# Model cuộc trò chuyện
class ConversationResponse(BaseModel):
    conversation_id: int
    title: str
    start_time: datetime
    end_time: Optional[datetime] = None
    owner: UserOut
    messages: Optional[List[MessageResponse]] = None

    class Config:
        from_attributes = True